import copy
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from validators.film.runtime import validate_clean_film_script_boundary
from validators.film.runtime import validate_film_act_structure
from validators.film.runtime import validate_film_character_arc
from validators.film.runtime import validate_film_cinematography_plan
from validators.film.runtime import validate_film_department_handoffs
from validators.film.runtime import validate_film_premise
from validators.film.runtime import validate_film_preproduction_packet
from validators.film.runtime import validate_film_production_risk
from validators.film.runtime import validate_film_revision_report
from validators.film.runtime import validate_film_scene_cards
from validators.film.runtime import validate_film_stakes_escalation
from validators.film.runtime import validate_film_visual_language
from validators.film.runtime import validate_film_world_bible


RUNNER = ROOT / "tools/film_runtime/film_screenplay_runtime_proof_runner.py"
PAYLOAD = ROOT / "tests/fixtures/film/f9_payload_motivational_drama.json"


def run_runner(output_root: Path) -> tuple[Path, dict]:
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--payload", str(PAYLOAD), "--output-root", str(output_root)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    summary = json.loads(result.stdout)
    artifact_root = Path(summary["artifact_root"])
    packet = json.loads((artifact_root / "preproduction_packet.json").read_text(encoding="utf-8"))
    return artifact_root, packet


def assert_failed(res: dict, label: str, report: dict) -> None:
    report[label] = res["passed"] is False
    assert res["passed"] is False, label


def test_mutation_resistance_cinema_validators(output_root: Path = ROOT / "artifacts/film_runtime_proof"):
    _, base_packet = run_runner(output_root)
    report = {}

    broken = copy.deepcopy(base_packet)
    broken["premise_test"]["external_goal"] = ""
    assert_failed(validate_film_premise.validate({"preproduction_packet": broken}), "delete_protagonist_goal", report)

    broken = copy.deepcopy(base_packet)
    broken.pop("opposing_force", None)
    assert_failed(validate_film_preproduction_packet.validate({"preproduction_packet": broken}), "delete_opposing_force", report)

    broken = copy.deepcopy(base_packet)
    broken["character_arc"]["want"] = broken["character_arc"]["need"]
    assert_failed(validate_film_character_arc.validate({"preproduction_packet": broken}), "make_want_equal_need", report)

    broken = copy.deepcopy(base_packet)
    broken["act_structure"]["midpoint_shift_or_reversal"] = ""
    assert_failed(validate_film_act_structure.validate({"preproduction_packet": broken}), "remove_midpoint", report)

    broken = copy.deepcopy(base_packet)
    for beat in broken["beat_sheet"]:
        beat["stakes_change"] = "same"
    assert_failed(validate_film_stakes_escalation.validate({"preproduction_packet": broken}), "flatten_stakes", report)

    broken = copy.deepcopy(base_packet)
    broken["scene_cards"][1]["conflict"] = ""
    assert_failed(validate_film_scene_cards.validate({"preproduction_packet": broken}), "remove_scene_card_conflict", report)

    broken = copy.deepcopy(base_packet)
    broken["world_bible"]["consequence_chain"] = []
    assert_failed(validate_film_world_bible.validate({"preproduction_packet": broken}), "remove_world_consequence_chain", report)

    broken = copy.deepcopy(base_packet)
    broken["world_bible"]["locations"] = ["isolated warehouse"]
    assert_failed(validate_film_world_bible.validate({"preproduction_packet": broken}), "remove_location_usage", report)

    broken = copy.deepcopy(base_packet)
    broken["visual_language"]["scene_visual_mapping"] = []
    assert_failed(validate_film_visual_language.validate({"preproduction_packet": broken}), "remove_visual_scene_mapping", report)

    broken = copy.deepcopy(base_packet)
    broken["cinematography_plan"]["lens_intent"] = ""
    assert_failed(validate_film_cinematography_plan.validate({"preproduction_packet": broken}), "remove_lens_intent", report)

    broken = copy.deepcopy(base_packet)
    broken["department_handoffs"]["development"]["owner_director"] = ""
    assert_failed(validate_film_department_handoffs.validate({"preproduction_packet": broken}), "remove_department_owner", report)

    broken = copy.deepcopy(base_packet)
    broken["department_handoffs"]["story"]["handoff_to"] = "validation_audit"
    assert_failed(validate_film_department_handoffs.validate({"preproduction_packet": broken}), "break_department_handoff_chain", report)

    broken = copy.deepcopy(base_packet)
    broken["production_risk_sheet"]["production_risk_sheet"][0]["mitigation"] = ""
    assert_failed(validate_film_production_risk.validate({"preproduction_packet": broken}), "remove_risk_mitigation", report)

    broken = copy.deepcopy(base_packet)
    broken["revision_report"]["revision_report"]["next_pass_recommendations"] = []
    assert_failed(validate_film_revision_report.validate({"preproduction_packet": broken}), "remove_revision_next_pass", report)

    broken = copy.deepcopy(base_packet)
    broken["route_state"]["mode"] = "media_generation"
    broken["mode"] = "media_generation"
    assert_failed(validate_film_preproduction_packet.validate({"preproduction_packet": broken}), "set_route_state_mode_to_media", report)

    broken = copy.deepcopy(base_packet)
    broken["downstream_adapter_boundary"]["media_provider_triggered"] = True
    assert_failed(validate_clean_film_script_boundary.validate({"preproduction_packet": broken}), "set_media_provider_triggered_true", report)

    broken = copy.deepcopy(base_packet)
    broken["production_risk_sheet"]["production_risk_sheet"][0]["risk"] = "youtube hook leakage into film route"
    assert_failed(validate_clean_film_script_boundary.validate({"preproduction_packet": broken}), "inject_youtube_hook_term_into_film_core", report)

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    test_mutation_resistance_cinema_validators()
    print("phase_13d_f10_mutation_resistance_ok")
