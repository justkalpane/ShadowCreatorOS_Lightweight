import importlib.util
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "tools/film_runtime/film_screenplay_runtime_proof_runner.py"
PAYLOAD = ROOT / "tests/fixtures/film/controlled_5min_motivational_screenplay_payload.json"
SCHEMA = ROOT / "schemas/film/preproduction_packet.schema.json"


EXPECTED_ARTIFACTS = {
    "concept_note.md",
    "premise_test.json",
    "framework_selection.json",
    "framework_conflict_report.json",
    "treatment.md",
    "synopsis.md",
    "character_bible.json",
    "character_arc.json",
    "opposing_force.json",
    "relationship_map.json",
    "moral_dilemma.json",
    "world_bible.json",
    "genre_grammar_report.json",
    "beat_sheet.json",
    "act_structure.json",
    "sequence_structure.json",
    "scene_cards.json",
    "director_vision.json",
    "visual_language.json",
    "cinematography_plan.json",
    "continuity_bible.json",
    "department_handoffs.json",
    "production_risk_sheet.json",
    "revision_report.json",
    "source_evidence_ledger.json",
    "screenplay.md",
    "screenplay_packet.json",
    "preproduction_packet.json",
    "route_state_capsule.json",
    "validation_report.json",
    "execution.log",
}


VALIDATOR_EXPECTATIONS = [
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
    "department_handoffs",
    "production_risk",
    "revision_report",
    "clean_film_script_boundary",
    "preproduction_packet",
]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
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


def test_openworker_gap_closure_cinema_engine_v1(tmp_path):
    artifact_root = run_runner(tmp_path / "film_runtime")
    produced = {path.name for path in artifact_root.iterdir() if path.is_file()}
    assert EXPECTED_ARTIFACTS <= produced

    packet = load_json(artifact_root / "preproduction_packet.json")
    report = load_json(artifact_root / "validation_report.json")
    schema = load_json(SCHEMA)

    for field in schema["required"]:
        assert field in packet, field

    assert (ROOT / "registries/film/best_practice_registry.yaml").is_file()
    assert (ROOT / "registries/film/film_genre_rules.yaml").is_file()
    assert (ROOT / "registries/film/cinema_template_registry.yaml").is_file()
    validator_registry = load_module(ROOT / "validators/film/validator_registry.py", "film_validator_registry")
    registry_paths = validator_registry.validator_paths()
    assert "preproduction_packet" in registry_paths
    assert "clean_film_script_boundary" in registry_paths

    framework_selection = load_json(artifact_root / "framework_selection.json")
    framework_conflict = load_json(artifact_root / "framework_conflict_report.json")
    assert framework_selection["registries_loaded"]["best_practice_registry"] is True
    assert framework_selection["registries_loaded"]["genre_rules_registry"] is True
    assert framework_selection["registries_loaded"]["cinema_template_registry"] is True
    assert framework_selection["registries_loaded"]["validator_registry"] is True
    assert framework_conflict["status"] == "NO_BLOCKING_CONFLICTS"

    assert packet["route"] == "FILM_SCREENPLAY_GENERATION"
    assert packet["mode"] == "script_only"
    assert packet["route_state"]["mode"] == "script_only"
    assert packet["route_state"]["route"] == "FILM_SCREENPLAY_GENERATION"
    assert packet["genre_grammar_report"]["passed"] is True
    assert "domestic_world_context" in packet["world_bible"]
    assert "director_note" in packet["director_vision"]
    assert "shot_types" in packet["cinematography_plan"]
    assert "production_risk_sheet" in packet["production_risk_sheet"]
    assert packet["source_evidence_ledger"]["source_policy"] == "fictional_local_payload_no_external_sources_required"

    for key in VALIDATOR_EXPECTATIONS:
        assert report["validator_results"][key]["passed"] is True, key
    assert report["status"] == "PASS_RUNTIME_ARTIFACT_PROVEN"

    screenplay = (artifact_root / "screenplay.md").read_text(encoding="utf-8")
    assert "Scene objective:" in screenplay
    assert "Turning point:" in screenplay

    execution_log = (artifact_root / "execution.log").read_text(encoding="utf-8").lower()
    assert "provider" not in execution_log
    assert "media" not in execution_log

    selector = (ROOT / "runtime/state/route_chain_mode_selector.yaml").read_text(encoding="utf-8")
    assert "default_mode: script_only" in selector
    script_manifest = (ROOT / "registries/route_manifests/script_generation.yaml").read_text(encoding="utf-8")
    assert "route_id: SCRIPT_GENERATION" in script_manifest


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as tmp:
        test_openworker_gap_closure_cinema_engine_v1(Path(tmp))
    print("phase_13d_f7_openworker_gap_closure_cinema_engine_ok")
