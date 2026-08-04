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
from validators.film.runtime import validate_film_genre_grammar
from validators.film.runtime import validate_film_logline
from validators.film.runtime import validate_film_premise
from validators.film.runtime import validate_film_production_risk
from validators.film.runtime import validate_film_relationship_map
from validators.film.runtime import validate_film_revision_report
from validators.film.runtime import validate_film_stakes_escalation
from validators.film.runtime import validate_film_theme_alignment
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


def write_failure_report(root: Path, report: dict) -> None:
    (root / "semantic_validator_failure_report.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    lines = ["# F9 Semantic Validator Failure Report", ""]
    for key, value in report.items():
        lines.append(f"- {key}: {value}")
    (root / "semantic_validator_failure_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_semantic_validator_failures(output_root: Path = ROOT / "artifacts/film_runtime_proof"):
    artifact_root, base_packet = run_runner(output_root)
    report = {}

    broken = copy.deepcopy(base_packet)
    broken["premise_test"]["premise"] = "Be better."
    broken["premise_test"]["stakes"] = ""
    assert_failed(validate_film_premise.validate({"preproduction_packet": broken}), "generic_premise_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["logline"] = "A parent changes."
    assert_failed(validate_film_logline.validate({"preproduction_packet": broken}), "logline_without_obstacle_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["beat_sheet"] = []
    assert_failed(validate_film_theme_alignment.validate({"preproduction_packet": broken}), "theme_only_in_metadata_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["act_structure"]["midpoint_shift_or_reversal"] = ""
    assert_failed(validate_film_act_structure.validate({"preproduction_packet": broken}), "missing_midpoint_fails", report)

    broken = copy.deepcopy(base_packet)
    for beat in broken["beat_sheet"]:
        beat["stakes_change"] = "same"
    assert_failed(validate_film_stakes_escalation.validate({"preproduction_packet": broken}), "flat_stakes_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["character_arc"]["want"] = broken["character_arc"]["need"]
    assert_failed(validate_film_character_arc.validate({"preproduction_packet": broken}), "want_equals_need_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["character_arc"]["transformation_end"] = broken["character_arc"]["transformation_start"]
    assert_failed(validate_film_character_arc.validate({"preproduction_packet": broken}), "character_no_transformation_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["relationship_map"]["relationships"][0]["mirror_function"] = "pleasant company"
    assert_failed(validate_film_relationship_map.validate({"preproduction_packet": broken}), "decorative_second_character_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["world_bible"]["locations"] = ["other place"]
    assert_failed(validate_film_world_bible.validate({"preproduction_packet": broken}), "world_locations_not_used_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["visual_language"]["scene_visual_mapping"] = []
    assert_failed(validate_film_visual_language.validate({"preproduction_packet": broken}), "visual_language_not_scene_mapped_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["cinematography_plan"]["lens_intent"] = ""
    assert_failed(validate_film_cinematography_plan.validate({"preproduction_packet": broken}), "cinematography_without_lens_intent_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["department_handoffs"]["development"]["owner_director"] = ""
    assert_failed(validate_film_department_handoffs.validate({"preproduction_packet": broken}), "missing_department_owner_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["production_risk_sheet"]["production_risk_sheet"][0]["mitigation"] = ""
    assert_failed(validate_film_production_risk.validate({"preproduction_packet": broken}), "risk_without_mitigation_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["revision_report"]["revision_report"]["next_pass_recommendations"] = []
    assert_failed(validate_film_revision_report.validate({"preproduction_packet": broken}), "revision_without_next_pass_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["genre_grammar_report"]["genre"] = "invalid_genre"
    assert_failed(validate_film_genre_grammar.validate({"preproduction_packet": broken}), "invalid_genre_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["downstream_adapter_boundary"]["media_provider_triggered"] = True
    assert_failed(validate_clean_film_script_boundary.validate({"preproduction_packet": broken}), "media_provider_flag_true_fails", report)

    broken = copy.deepcopy(base_packet)
    broken["production_risk_sheet"]["production_risk_sheet"][0]["risk"] = "youtube hook leakage"
    assert_failed(validate_clean_film_script_boundary.validate({"preproduction_packet": broken}), "film_route_imports_content_hook_logic_fails", report)

    write_failure_report(artifact_root, report)


if __name__ == "__main__":
    test_semantic_validator_failures()
    print("phase_13d_f9_semantic_validator_failures_ok")
