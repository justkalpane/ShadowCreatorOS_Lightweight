import importlib.util
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HARNESS_PATH = ROOT / "tools/film_runtime/film_route_runtime_proof_harness.py"


def load_harness():
    spec = importlib.util.spec_from_file_location("film_route_runtime_proof_harness", HARNESS_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_harness_reports_blocked_skeleton_validators_without_runtime_proof():
    harness = load_harness()
    report = harness.evaluate(ROOT)

    assert report["status"] == "FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS"
    assert report["route_id"] == "FILM_SCREENPLAY_GENERATION"
    assert report["route_mode"] == "film_screenplay_generation"
    assert report["default_mode_before"] == "script_only"
    assert report["default_mode_after"] == "script_only"
    assert report["selector_mode_resolved"] is True
    assert report["script_generation_preserved"] is True
    assert report["post_binding_checker_status"] == "POST_BINDING_FILM_ROUTE_STATE_READY"
    assert report["route_state_schema_compatible"] is True
    assert report["runtime_execution_performed"] is False
    assert report["film_output_generated"] is False
    assert report["pass_claimed"] is False
    assert report["governed_runtime_proof_claimed"] is False


def test_harness_records_skeleton_validator_reality():
    harness = load_harness()
    report = harness.evaluate(ROOT)

    assert report["film_validators_enforceable"] is False
    statuses = {item["path"]: item["status"] for item in report["validator_ledger"]}
    assert statuses["validators/film/output_packet/validate_film_screenplay_packet.py"] == "SKELETON_ONLY"
    assert statuses["validators/film/validation/validate_no_fake_film_pass.py"] == "SKELETON_ONLY"
    assert statuses["validators/film/validation/validate_film_content_packet_separation.py"] == "SKELETON_ONLY"
    assert statuses["validators/film/route/validate_film_route_selection.py"] == "SKELETON_ONLY"


def test_harness_creates_route_state_template_in_memory_only():
    harness = load_harness()
    report = harness.evaluate(ROOT)
    capsule = report["route_state_capsule_template"]

    assert report["route_state_capsule_template_created"] is True
    assert report["route_state_capsule_written"] is False
    assert capsule["route_id"] == "FILM_SCREENPLAY_GENERATION"
    assert capsule["task_mode"] == "film_screenplay_generation"
    assert capsule["route_phase"] == "BLOCKED"
    assert capsule["dependencies_complete"] is False
    assert capsule["output_phase_started"] is False


def test_harness_cli_prints_report_and_exits_blocked():
    result = subprocess.run(
        ["python3", str(HARNESS_PATH)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 1
    assert "FILM_RUNTIME_PROOF_HARNESS_REPORT" in result.stdout
    assert "status=FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS" in result.stdout
    assert "route_state_schema_compatible=true" in result.stdout
    assert "film_validators_enforceable=false" in result.stdout
    assert "runtime_execution_performed=false" in result.stdout
    assert "film_output_generated=false" in result.stdout
    assert "pass_claimed=false" in result.stdout
    assert "governed_runtime_proof_claimed=false" in result.stdout


if __name__ == "__main__":
    test_harness_reports_blocked_skeleton_validators_without_runtime_proof()
    test_harness_records_skeleton_validator_reality()
    test_harness_creates_route_state_template_in_memory_only()
    test_harness_cli_prints_report_and_exits_blocked()
    print("phase_13e34_film_route_runtime_proof_harness_ok")
