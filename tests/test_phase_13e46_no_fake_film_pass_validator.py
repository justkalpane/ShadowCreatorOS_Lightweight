import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "validators/film/validation/validate_no_fake_film_pass.py"
NO_FAKE_PASS_FIXTURES = ROOT / "tests/fixtures/no_fake_pass"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_no_fake_film_pass", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def assert_boundary_flags(result):
    assert result["runtime_behavior_changed"] is False
    assert result["route_selector_modified"] is False
    assert result["validator_bound_to_runtime"] is False
    assert result["governed_runtime_proof_claimed"] is False
    assert result["pass_claimed"] is False


def test_empty_payload_remains_non_runtime_proof_for_harness_compatibility():
    validator = load_validator()
    result = validator.validate({})

    assert result["status"] == "SKELETON_ONLY"
    assert result["passed"] is False
    assert result["enforced"] is False
    assert_boundary_flags(result)


def test_all_phase_12a_no_fake_pass_fixtures_fail_local_enforcement():
    validator = load_validator()
    paths = sorted(NO_FAKE_PASS_FIXTURES.glob("*.json"))

    assert len(paths) == 7
    for path in paths:
        result = validator.validate(load_json(path))
        assert result["status"] == "VALIDATION_FAILED", path
        assert result["passed"] is False, path
        assert result["enforced"] is True, path
        assert result["errors"], path
        assert_boundary_flags(result)


def test_local_positive_control_passes_without_pass_or_runtime_proof_claims():
    validator = load_validator()
    payload = {
        "target_route": "FILM_SCREENPLAY_GENERATION",
        "validator_type": "film",
        "pass_claimed": False,
        "film_pass_claimed": False,
        "runtime_pass_claimed": False,
        "governed_runtime_proof_claimed": False,
        "claims_film_schema_valid": True,
        "film_schema_evidence": {"schema_path": "schemas/film/output_packet/film_screenplay_output_packet.schema.json"},
        "claims_source_backed": True,
        "source_ledger": {"status": "present"},
        "claims_route_lineage_complete": True,
        "route_lineage_ledger": {"status": "present"},
        "claims_filmcraft_scorecard_complete": True,
        "filmcraft_scorecard": {"status": "present"},
        "claims_governed_runtime_proof_from_repo_read": False,
        "runtime_artifact_claims": [],
    }

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_PASSED"
    assert result["passed"] is True
    assert result["enforced"] is True
    assert result["errors"] == []
    assert_boundary_flags(result)


def test_content_validator_cannot_pass_film_packet():
    validator = load_validator()
    result = validator.validate({
        "target_route": "FILM_SCREENPLAY_GENERATION",
        "validator_type": "content",
    })

    assert result["status"] == "VALIDATION_FAILED"
    assert any("content validator cannot pass" in error for error in result["errors"])
    assert_boundary_flags(result)


def test_runtime_artifact_names_cannot_be_invented():
    validator = load_validator()
    result = validator.validate({
        "target_route": "FILM_SCREENPLAY_GENERATION",
        "runtime_artifact_claims": ["repository_lock_id", "completion_certificate"],
    })

    assert result["status"] == "VALIDATION_FAILED"
    assert any("runtime artifact names cannot be invented" in error for error in result["errors"])
    assert_boundary_flags(result)


def test_github_read_cannot_be_governed_runtime_proof():
    validator = load_validator()
    result = validator.validate({
        "target_route": "FILM_SCREENPLAY_GENERATION",
        "claims_governed_runtime_proof_from_repo_read": True,
    })

    assert result["status"] == "VALIDATION_FAILED"
    assert any("not governed runtime proof" in error for error in result["errors"])
    assert_boundary_flags(result)


if __name__ == "__main__":
    test_empty_payload_remains_non_runtime_proof_for_harness_compatibility()
    test_all_phase_12a_no_fake_pass_fixtures_fail_local_enforcement()
    test_local_positive_control_passes_without_pass_or_runtime_proof_claims()
    test_content_validator_cannot_pass_film_packet()
    test_runtime_artifact_names_cannot_be_invented()
    test_github_read_cannot_be_governed_runtime_proof()
    print("phase_13e46_no_fake_film_pass_validator_ok")
