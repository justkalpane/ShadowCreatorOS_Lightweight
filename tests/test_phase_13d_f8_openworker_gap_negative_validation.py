import copy
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from validators.film.runtime import validate_film_act_structure
from validators.film.runtime import validate_film_character_arc
from validators.film.runtime import validate_film_character_constraints
from validators.film.runtime import validate_film_cinematography_plan
from validators.film.runtime import validate_film_continuity
from validators.film.runtime import validate_film_consequence_logic
from validators.film.runtime import validate_film_department_handoffs
from validators.film.runtime import validate_film_dialogue_subtext
from validators.film.runtime import validate_film_director_vision
from validators.film.runtime import validate_film_duration
from validators.film.runtime import validate_film_downstream_boundary
from validators.film.runtime import validate_film_emotional_beat_map
from validators.film.runtime import validate_film_emotional_continuity
from validators.film.runtime import validate_film_genre_grammar
from validators.film.runtime import validate_film_logline
from validators.film.runtime import validate_film_premise
from validators.film.runtime import validate_film_preproduction_packet
from validators.film.runtime import validate_film_production_risk
from validators.film.runtime import validate_film_relationship_map
from validators.film.runtime import validate_film_revision_report
from validators.film.runtime import validate_film_revision_pass
from validators.film.runtime import validate_film_scene_cards
from validators.film.runtime import validate_film_sequence_structure
from validators.film.runtime import validate_film_stakes_escalation
from validators.film.runtime import validate_film_theme_alignment
from validators.film.runtime import validate_film_timeline_continuity
from validators.film.runtime import validate_film_visual_language
from validators.film.runtime import validate_film_world_bible
from validators.film.runtime import validate_clean_film_script_boundary

RUNNER = ROOT / "tools/film_runtime/film_screenplay_runtime_proof_runner.py"
PAYLOAD = ROOT / "tests/fixtures/film/controlled_5min_motivational_screenplay_payload.json"

NEGATIVE_VALIDATOR_COVERAGE = [
    "duration",
    "character_constraints",
    "emotional_beat_map",
    "continuity",
    "dialogue_subtext",
    "scene_cards",
    "premise",
    "logline",
    "theme_alignment",
    "act_structure",
    "sequence_structure",
    "stakes_escalation",
    "revision_pass",
    "character_arc",
    "relationship_map",
    "emotional_continuity",
    "world_bible",
    "timeline_continuity",
    "consequence_logic",
    "director_vision",
    "visual_language",
    "cinematography_plan",
    "genre_grammar",
    "department_handoffs",
    "production_risk",
    "revision_report",
    "clean_film_script_boundary",
    "downstream_boundary",
    "preproduction_packet",
]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


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
    packet = load_json(artifact_root / "preproduction_packet.json")
    return artifact_root, packet


def assert_failed(result: dict, label: str):
    assert result["passed"] is False, f"{label} unexpectedly passed"


def test_openworker_gap_negative_validation(tmp_path):
    _, base_packet = run_runner(tmp_path / "film_runtime")

    broken = copy.deepcopy(base_packet)
    del broken["beat_sheet"]
    assert_failed(validate_film_preproduction_packet.validate({"preproduction_packet": broken}), "missing_beat_sheet_fails")

    broken = copy.deepcopy(base_packet)
    del broken["act_structure"]
    assert_failed(validate_film_act_structure.validate({"preproduction_packet": broken}), "missing_act_structure_fails")

    broken = copy.deepcopy(base_packet)
    del broken["sequence_structure"]
    assert_failed(validate_film_sequence_structure.validate({"preproduction_packet": broken}), "missing_sequence_structure_fails")

    broken = copy.deepcopy(base_packet)
    del broken["character_arc"]
    assert_failed(validate_film_character_arc.validate({"preproduction_packet": broken}), "missing_character_arc_fails")

    broken = copy.deepcopy(base_packet)
    del broken["world_bible"]
    assert_failed(validate_film_world_bible.validate({"preproduction_packet": broken}), "missing_world_bible_fails")

    broken = copy.deepcopy(base_packet)
    del broken["director_vision"]
    assert_failed(validate_film_director_vision.validate({"preproduction_packet": broken}), "missing_director_vision_fails")

    broken = copy.deepcopy(base_packet)
    del broken["visual_language"]
    assert_failed(validate_film_visual_language.validate({"preproduction_packet": broken}), "missing_visual_language_fails")

    broken = copy.deepcopy(base_packet)
    del broken["cinematography_plan"]
    assert_failed(validate_film_cinematography_plan.validate({"preproduction_packet": broken}), "missing_cinematography_plan_fails")

    broken = copy.deepcopy(base_packet)
    del broken["department_handoffs"]
    assert_failed(validate_film_department_handoffs.validate({"preproduction_packet": broken}), "missing_department_handoffs_fails")

    broken = copy.deepcopy(base_packet)
    del broken["production_risk_sheet"]
    assert_failed(validate_film_production_risk.validate({"preproduction_packet": broken}), "missing_production_risk_fails")

    broken = copy.deepcopy(base_packet)
    del broken["revision_report"]
    assert_failed(validate_film_revision_report.validate({"preproduction_packet": broken}), "missing_revision_report_fails")

    broken = copy.deepcopy(base_packet)
    broken["route_state"]["mode"] = "film_core"
    assert_failed(validate_film_preproduction_packet.validate({"preproduction_packet": broken}), "wrong_route_state_mode_fails")

    broken = copy.deepcopy(base_packet)
    broken["route"] = "SCRIPT_GENERATION"
    assert_failed(validate_clean_film_script_boundary.validate({"preproduction_packet": broken}), "SCRIPT_GENERATION_leak_into_FILM_route_fails")

    broken = copy.deepcopy(base_packet)
    broken["downstream_adapter_boundary"]["media_provider_triggered"] = True
    assert_failed(validate_film_downstream_boundary.validate({"preproduction_packet": broken}), "media_provider_flag_true_fails")

    broken = copy.deepcopy(base_packet)
    broken["production_risk_sheet"]["production_risk_sheet"][0]["risk"] = "thumbnail and youtube hook optimization inside film core"
    assert_failed(validate_clean_film_script_boundary.validate({"preproduction_packet": broken}), "content_route_terms_inside_film_core_fail")

    assert validate_film_genre_grammar.validate({"preproduction_packet": base_packet})["passed"] is True


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp:
        test_openworker_gap_negative_validation(Path(tmp))
    print("phase_13d_f8_openworker_gap_negative_validation_ok")
