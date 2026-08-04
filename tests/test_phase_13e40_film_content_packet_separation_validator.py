import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "validators/film/validation/validate_film_content_packet_separation.py"
CONTENT_PRESERVATION_FIXTURES = ROOT / "tests/fixtures/content_preservation"
FILM_PACKET_FIXTURES = ROOT / "tests/fixtures/film_packet_validation"
NO_FAKE_PASS_FIXTURES = ROOT / "tests/fixtures/no_fake_pass"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_film_content_packet_separation", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_empty_payload_remains_non_runtime_proof_for_harness_compatibility():
    validator = load_validator()
    result = validator.validate({})

    assert result["status"] == "SKELETON_ONLY"
    assert result["passed"] is False
    assert result["enforced"] is False
    assert result["runtime_behavior_changed"] is False
    assert result["route_selector_modified"] is False
    assert result["validator_bound_to_runtime"] is False
    assert result["governed_runtime_proof_claimed"] is False
    assert result["pass_claimed"] is False


def test_content_preservation_fixtures_pass_local_separation_enforcement():
    validator = load_validator()
    paths = sorted(CONTENT_PRESERVATION_FIXTURES.glob("*.json"))

    assert len(paths) == 6
    for path in paths:
        payload = load_json(path)
        assert payload["expected_route"] == "SCRIPT_GENERATION", path
        result = validator.validate(payload)
        assert result["status"] == "VALIDATION_PASSED", path
        assert result["passed"] is True, path
        assert result["enforced"] is True, path
        assert result["separation_boundary_only"] is True, path
        assert result["runtime_behavior_changed"] is False, path
        assert result["route_selector_modified"] is False, path
        assert result["validator_bound_to_runtime"] is False, path
        assert result["governed_runtime_proof_claimed"] is False, path
        assert result["pass_claimed"] is False, path


def test_positive_film_baseline_passes_boundary_only_not_full_packet_proof():
    validator = load_validator()
    payload = load_json(FILM_PACKET_FIXTURES / "valid_minimal_film_packet.json")

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_PASSED"
    assert result["passed"] is True
    assert result["enforced"] is True
    assert result["separation_boundary_only"] is True
    assert result["validator_bound_to_runtime"] is False
    assert result["governed_runtime_proof_claimed"] is False
    assert result["pass_claimed"] is False


def test_film_packet_missing_craft_fields_is_delegated_not_content_drift():
    validator = load_validator()
    payload = load_json(FILM_PACKET_FIXTURES / "missing_beat_sheet_should_fail.json")

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_PASSED"
    assert result["passed"] is True
    assert result["enforced"] is True
    assert result["separation_boundary_only"] is True
    assert result["pass_claimed"] is False


def test_content_packet_pretending_film_fails_local_separation():
    validator = load_validator()
    payload = load_json(FILM_PACKET_FIXTURES / "content_packet_pretending_film_should_fail.json")

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_FAILED"
    assert result["passed"] is False
    assert result["enforced"] is True
    assert any("content packet cannot impersonate" in error for error in result["errors"])


def test_hook_retention_only_film_packet_fails_local_separation():
    validator = load_validator()
    payload = load_json(FILM_PACKET_FIXTURES / "hook_retention_only_packet_should_fail.json")

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_FAILED"
    assert result["passed"] is False
    assert result["enforced"] is True
    assert any("content hook/retention metrics" in error for error in result["errors"])


def test_content_validator_cannot_pass_film_packet():
    validator = load_validator()
    payload = load_json(NO_FAKE_PASS_FIXTURES / "content_validator_cannot_pass_film_packet.json")

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_FAILED"
    assert result["passed"] is False
    assert result["enforced"] is True
    assert any("content validator cannot pass" in error for error in result["errors"])


def test_unrelated_no_fake_pass_fixture_is_deferred_to_no_fake_pass_validator():
    validator = load_validator()
    payload = load_json(NO_FAKE_PASS_FIXTURES / "runtime_artifact_names_cannot_be_invented.json")

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_DEFERRED"
    assert result["passed"] is False
    assert result["enforced"] is True
    assert result["pass_claimed"] is False


if __name__ == "__main__":
    test_empty_payload_remains_non_runtime_proof_for_harness_compatibility()
    test_content_preservation_fixtures_pass_local_separation_enforcement()
    test_positive_film_baseline_passes_boundary_only_not_full_packet_proof()
    test_film_packet_missing_craft_fields_is_delegated_not_content_drift()
    test_content_packet_pretending_film_fails_local_separation()
    test_hook_retention_only_film_packet_fails_local_separation()
    test_content_validator_cannot_pass_film_packet()
    test_unrelated_no_fake_pass_fixture_is_deferred_to_no_fake_pass_validator()
    print("phase_13e40_film_content_packet_separation_validator_ok")
