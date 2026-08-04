import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "tools/film_runtime/film_screenplay_runtime_proof_runner.py"
PAYLOAD = ROOT / "tests/fixtures/film/f22_payload_feature_motivational_drama.json"


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _run_runner(output_root: Path) -> tuple[dict, Path]:
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--payload", str(PAYLOAD), "--output-root", str(output_root)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    summary = json.loads(result.stdout)
    return summary, Path(summary["artifact_root"])


def test_feature_length_and_multi_act_stress(tmp_path):
    summary, artifact_root = _run_runner(tmp_path / "film_runtime")
    assert summary["status"] == "PASS_RUNTIME_ARTIFACT_PROVEN"

    packet = _load_json(artifact_root / "screenplay_packet.json")
    report = _load_json(artifact_root / "validation_report.json")
    scene_cards = packet["scene_cards"]
    beat_sheet = packet["beat_sheet"]
    act_structure = packet["act_structure"]
    sequence_structure = packet["sequence_structure"]
    genre_report = packet["genre_grammar_report"]

    assert packet["route"] == "FILM_SCREENPLAY_GENERATION"
    assert packet["mode"] == "script_only"
    assert packet["duration_minutes"] == 118
    assert packet["estimated_duration_minutes"] == 118
    assert packet["format"] == "feature_film_screenplay"
    assert packet["format_family"] == "feature_film"

    assert len(scene_cards) >= 12
    assert len(beat_sheet) >= 12
    assert len(sequence_structure["sequences"]) >= 6
    assert act_structure["format_family"] == "feature_film"
    assert sequence_structure["format_family"] == "feature_film"
    assert len(act_structure["act_one"]) >= 3
    assert len(act_structure["act_two"]) >= 3
    assert len(act_structure["act_three"]) >= 3

    scene_numbers = [card["scene_number"] for card in scene_cards]
    assert scene_numbers == list(range(1, len(scene_cards) + 1))
    assert beat_sheet[-1]["beat_id"] == "closing_image"
    assert beat_sheet[-1]["scene_number"] == scene_cards[-1]["scene_number"]

    assert genre_report["format_family"] == "feature_film"
    assert genre_report["format_rule_map"]["story_logic"] == "layered arcs, sustained escalation, thematic closure"
    assert genre_report["checks"]["scene_count_supports_duration"] is True
    assert genre_report["passed"] is True

    duration_result = report["validator_results"]["duration"]
    assert duration_result["passed"] is True
    assert report["validator_results"]["act_structure"]["passed"] is True
    assert report["validator_results"]["sequence_structure"]["passed"] is True
    assert report["validator_results"]["genre_grammar"]["passed"] is True
    assert report["validator_results"]["scene_cards"]["passed"] is True
    assert report["validator_results"]["no_fake_pass"]["passed"] is True

    screenplay_text = (artifact_root / "screenplay.md").read_text(encoding="utf-8")
    assert screenplay_text.count("INT.") + screenplay_text.count("EXT.") >= 12
    assert "shout" not in screenplay_text.lower()
    assert "violence" not in screenplay_text.lower()

    route_state = packet["route_state"]
    assert route_state["route_id"] == "FILM_SCREENPLAY_GENERATION"
    assert route_state["mode"] == "script_only"
    assert route_state["task_mode"] == "film_screenplay_generation"
    assert route_state["dependencies_complete"] is True
    assert route_state["output_phase_started"] is True


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp:
        test_feature_length_and_multi_act_stress(Path(tmp))
    print("phase_13d_f22_feature_length_and_multi_act_stress_test_ok")
