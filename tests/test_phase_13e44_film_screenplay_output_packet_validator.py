import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "validators/film/output_packet/validate_film_screenplay_packet.py"
SCHEMA_PATH = ROOT / "schemas/film/output_packet/film_screenplay_output_packet.schema.json"
FILM_PACKET_FIXTURES = ROOT / "tests/fixtures/film_packet_validation"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_film_screenplay_packet", VALIDATOR_PATH)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def build_minimal_packet():
    schema = load_json(SCHEMA_PATH)
    packet = {}
    for field in schema["required"]:
        kind = schema["properties"][field]["type"]
        if kind == "object":
            packet[field] = {"status": "present"}
        elif kind == "array":
            packet[field] = ["present"]
        else:
            packet[field] = f"{field}_present"
    packet["route_state_capsule"] = {"route_id": "FILM_SCREENPLAY_GENERATION"}
    packet["film_intent_lock"] = "FILM_SCREENPLAY_GENERATION"
    packet["no_fake_pass_gate"] = {"pass_claimed": False}
    return packet


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


def test_complete_synthetic_packet_passes_local_required_field_validation():
    validator = load_validator()
    result = validator.validate(build_minimal_packet())

    assert result["status"] == "VALIDATION_PASSED"
    assert result["passed"] is True
    assert result["enforced"] is True
    assert result["required_field_count"] == 20
    assert result["errors"] == []
    assert_boundary_flags(result)


def test_missing_schema_required_field_fails_with_field_ledger():
    validator = load_validator()
    packet = build_minimal_packet()
    packet.pop("beat_sheet")

    result = validator.validate(packet)

    assert result["status"] == "VALIDATION_FAILED"
    assert result["passed"] is False
    assert result["enforced"] is True
    assert "missing required field: beat_sheet" in result["errors"]
    assert_boundary_flags(result)


def test_phase_12a_positive_fixture_maps_to_complete_local_packet():
    validator = load_validator()
    payload = load_json(FILM_PACKET_FIXTURES / "valid_minimal_film_packet.json")

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_PASSED"
    assert result["passed"] is True
    assert result["payload_kind"] == "phase_12a_fixture_descriptor"
    assert result["required_field_count"] == 20
    assert_boundary_flags(result)


def test_phase_12a_failure_fixtures_fail_local_output_validation():
    validator = load_validator()
    paths = sorted(
        path for path in FILM_PACKET_FIXTURES.glob("*.json")
        if path.name != "valid_minimal_film_packet.json"
    )

    assert len(paths) == 9
    for path in paths:
        result = validator.validate(load_json(path))
        assert result["status"] == "VALIDATION_FAILED", path
        assert result["passed"] is False, path
        assert result["enforced"] is True, path
        assert result["errors"], path
        assert_boundary_flags(result)


def test_content_platform_packet_cannot_pass_output_validation():
    validator = load_validator()
    packet = build_minimal_packet()
    packet["packet_type"] = "youtube_script"

    result = validator.validate(packet)

    assert result["status"] == "VALIDATION_FAILED"
    assert result["passed"] is False
    assert result["enforced"] is True
    assert any("content/platform packet" in error for error in result["errors"])
    assert_boundary_flags(result)


if __name__ == "__main__":
    test_empty_payload_remains_non_runtime_proof_for_harness_compatibility()
    test_complete_synthetic_packet_passes_local_required_field_validation()
    test_missing_schema_required_field_fails_with_field_ledger()
    test_phase_12a_positive_fixture_maps_to_complete_local_packet()
    test_phase_12a_failure_fixtures_fail_local_output_validation()
    test_content_platform_packet_cannot_pass_output_validation()
    print("phase_13e44_film_screenplay_output_packet_validator_ok")
