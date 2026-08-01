import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "validators/film/route/validate_film_route_selection.py"
ROUTE_SELECTION_FIXTURES = ROOT / "tests/fixtures/film_route_selection"
CONTENT_PRESERVATION_FIXTURES = ROOT / "tests/fixtures/content_preservation"


def load_validator():
    spec = importlib.util.spec_from_file_location("validate_film_route_selection", VALIDATOR_PATH)
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


def test_phase_12a_route_selection_fixtures_pass_local_enforcement():
    validator = load_validator()
    paths = sorted(ROUTE_SELECTION_FIXTURES.glob("*.json"))

    assert len(paths) == 10
    for path in paths:
        result = validator.validate(load_json(path))
        assert result["status"] == "VALIDATION_PASSED", path
        assert result["passed"] is True, path
        assert result["enforced"] is True, path
        assert result["runtime_behavior_changed"] is False, path
        assert result["route_selector_modified"] is False, path
        assert result["validator_bound_to_runtime"] is False, path
        assert result["governed_runtime_proof_claimed"] is False, path
        assert result["pass_claimed"] is False, path


def test_phase_12a_content_preservation_fixtures_keep_script_generation():
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


def test_content_platform_prompts_cannot_be_promoted_to_film_core():
    validator = load_validator()
    payload = {
        "fixture_family": "route_selection",
        "input_prompt": "Write a YouTube script about NEET.",
        "expected_route": "FILM_SCREENPLAY_GENERATION",
        "expected_mode": "film_core",
        "should_pass_later": True,
        "should_fail_later": False,
    }

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_FAILED"
    assert result["passed"] is False
    assert result["enforced"] is True
    assert any("content/platform trigger" in error for error in result["errors"])


def test_explicit_film_prompt_cannot_be_flattened_to_content_route():
    validator = load_validator()
    payload = {
        "fixture_family": "route_selection",
        "input_prompt": "Create a short film on the NEET paper issue.",
        "expected_route": "SCRIPT_GENERATION",
        "expected_mode": "content",
        "should_pass_later": True,
        "should_fail_later": False,
    }

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_FAILED"
    assert result["passed"] is False
    assert result["enforced"] is True
    assert any("explicit screenplay/film trigger" in error for error in result["errors"])


def test_downstream_prompts_cannot_be_promoted_to_film_core():
    validator = load_validator()
    payload = {
        "fixture_family": "route_selection",
        "input_prompt": "Create a trailer for the NEET short film.",
        "expected_route": "FILM_SCREENPLAY_GENERATION",
        "expected_mode": "film_core",
        "should_pass_later": True,
        "should_fail_later": False,
    }

    result = validator.validate(payload)

    assert result["status"] == "VALIDATION_FAILED"
    assert result["passed"] is False
    assert result["enforced"] is True
    assert any("downstream trigger" in error for error in result["errors"])


if __name__ == "__main__":
    test_empty_payload_remains_non_runtime_proof_for_harness_compatibility()
    test_phase_12a_route_selection_fixtures_pass_local_enforcement()
    test_phase_12a_content_preservation_fixtures_keep_script_generation()
    test_content_platform_prompts_cannot_be_promoted_to_film_core()
    test_explicit_film_prompt_cannot_be_flattened_to_content_route()
    test_downstream_prompts_cannot_be_promoted_to_film_core()
    print("phase_13e38_film_route_selection_validator_ok")
