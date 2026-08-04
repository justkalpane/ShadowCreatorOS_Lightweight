import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "tools/film_runtime/film_screenplay_runtime_proof_runner.py"
PAYLOAD = ROOT / "tests/fixtures/film/controlled_5min_motivational_screenplay_payload.json"
DIALOGUE_VALIDATOR = ROOT / "validators/film/runtime/validate_film_dialogue_subtext.py"
SCENE_CARD_VALIDATOR = ROOT / "validators/film/runtime/validate_film_scene_cards.py"


REQUIRED_ARTIFACTS = {
    "treatment.md",
    "synopsis.md",
    "character_bible.json",
    "relationship_map.json",
    "beat_sheet.json",
    "scene_cards.json",
    "continuity_bible.json",
    "genre_grammar_report.json",
    "screenplay.md",
    "screenplay_packet.json",
    "route_state_capsule.json",
    "validation_report.json",
    "execution.log",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_validator(path: Path, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_runner(output_root: Path) -> Path:
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--payload", str(PAYLOAD), "--output-root", str(output_root)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    summary = json.loads(result.stdout)
    return Path(summary["artifact_root"])


def test_cinema_preproduction_brain_layer_generates_and_validates(tmp_path):
    artifact_root = run_runner(tmp_path / "film_runtime")
    produced = {path.name for path in artifact_root.iterdir() if path.is_file()}
    assert REQUIRED_ARTIFACTS <= produced

    packet = load_json(artifact_root / "screenplay_packet.json")
    report = load_json(artifact_root / "validation_report.json")
    character_bible = load_json(artifact_root / "character_bible.json")
    relationship_map = load_json(artifact_root / "relationship_map.json")
    beat_sheet = load_json(artifact_root / "beat_sheet.json")["beats"]
    scene_cards = load_json(artifact_root / "scene_cards.json")["scene_cards"]
    continuity_bible = load_json(artifact_root / "continuity_bible.json")
    genre_report = load_json(artifact_root / "genre_grammar_report.json")
    screenplay = (artifact_root / "screenplay.md").read_text(encoding="utf-8")

    for key in [
        "film_intent_lock",
        "treatment",
        "synopsis",
        "character_bible",
        "relationship_map",
        "beat_sheet",
        "scene_cards",
        "continuity_bible",
        "genre_grammar_report",
        "screenplay",
        "scene_breakdown",
        "dialogue_subtext_pass",
        "validation_report",
        "route_state",
    ]:
        assert key in packet

    main = character_bible["major_characters"][0]
    second = character_bible["major_characters"][1]
    main_text = json.dumps(main).lower()
    assert "soft-spoken" in main_text
    assert "warm" in main_text
    assert "controlled internal anger" in main_text
    assert "does not shout" in main_text
    assert "does not become violent" in main_text
    assert "does not become abusive" in main_text
    assert "toddlers" in main_text

    assert "emotional mirror" in json.dumps(second).lower()
    assert relationship_map["second_character_mirror_function_confirmed"] is True

    continuity_text = json.dumps(continuity_bible).lower()
    scene_card_text = json.dumps(scene_cards).lower()
    assert "toddler" in continuity_text
    assert "toddler" in scene_card_text
    assert len(continuity_bible["toddler_stakes_continuity"]) >= 3

    assert len(beat_sheet) == 8
    assert [beat["beat_id"] for beat in beat_sheet] == [
        "opening_image",
        "setup",
        "pressure_trigger",
        "internal_anger",
        "visible_restraint",
        "self_awareness",
        "repair_choice",
        "closing_image",
    ]
    assert len(scene_cards) >= 3
    assert packet["scene_breakdown"] == packet["scene_cards"]
    assert all(card["slugline"] in screenplay for card in scene_cards[:3])
    assert any(card["action_lines"][0] in screenplay for card in scene_cards[:3])
    assert any("pressure" in json.dumps(card).lower() for card in scene_cards)
    assert any("restraint" in json.dumps(card).lower() for card in scene_cards)
    assert any("repair" in json.dumps(card).lower() for card in scene_cards)

    assert genre_report["passed"] is True
    assert report["status"] == "PASS_RUNTIME_ARTIFACT_PROVEN"
    assert report["validator_results"]["dialogue_subtext"]["passed"] is True
    assert report["validator_results"]["scene_cards"]["passed"] is True

    dialogue_validator = load_validator(DIALOGUE_VALIDATOR, "validate_film_dialogue_subtext")
    scene_card_validator = load_validator(SCENE_CARD_VALIDATOR, "validate_film_scene_cards")
    assert dialogue_validator.validate({"artifact_root": artifact_root})["passed"] is True
    assert scene_card_validator.validate({"artifact_root": artifact_root})["passed"] is True

    execution_log = (artifact_root / "execution.log").read_text(encoding="utf-8").lower()
    assert "provider" not in execution_log
    assert "media" not in execution_log

    selector = (ROOT / "runtime/state/route_chain_mode_selector.yaml").read_text(encoding="utf-8")
    assert "default_mode: script_only" in selector
    assert "FILM_SCREENPLAY_GENERATION" in selector
    script_manifest = (ROOT / "registries/route_manifests/script_generation.yaml").read_text(encoding="utf-8")
    assert "route_id: SCRIPT_GENERATION" in script_manifest


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp:
        test_cinema_preproduction_brain_layer_generates_and_validates(Path(tmp))
    print("phase_13d_f6_cinema_preproduction_brain_layer_ok")
