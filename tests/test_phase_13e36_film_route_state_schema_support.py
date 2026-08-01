import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROUTE_STATE_SCHEMA = ROOT / "runtime/state/route_state.schema.json"
HARNESS_PATH = ROOT / "tools/film_runtime/film_route_runtime_proof_harness.py"

PRE_EXISTING_TASK_MODES = {
    "script_only",
    "script_plus_visual_plan",
    "script_plus_visual_generation_draft",
    "script_plus_media_factory_handoff",
    "full_content_packet",
    "repo_drift_audit",
    "media_factory_regression_audit",
}


def load_harness():
    spec = importlib.util.spec_from_file_location("film_route_runtime_proof_harness", HARNESS_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def task_modes():
    schema = json.loads(ROUTE_STATE_SCHEMA.read_text(encoding="utf-8"))
    return set(schema["properties"]["task_mode"]["enum"])


def test_route_state_schema_preserves_existing_task_modes_and_adds_film_mode():
    modes = task_modes()

    assert PRE_EXISTING_TASK_MODES.issubset(modes)
    assert "film_screenplay_generation" in modes


def test_phase_13e34_harness_advances_to_skeleton_validator_blocker():
    harness = load_harness()
    report = harness.evaluate(ROOT)

    assert report["route_state_schema_compatible"] is True
    assert report["status"] == "FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS"
    assert report["film_validators_enforceable"] is False
    assert report["runtime_execution_performed"] is False
    assert report["film_output_generated"] is False
    assert report["pass_claimed"] is False
    assert report["governed_runtime_proof_claimed"] is False


if __name__ == "__main__":
    test_route_state_schema_preserves_existing_task_modes_and_adds_film_mode()
    test_phase_13e34_harness_advances_to_skeleton_validator_blocker()
    print("phase_13e36_film_route_state_schema_support_ok")
