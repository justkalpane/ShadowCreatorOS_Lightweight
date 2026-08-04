import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: str) -> dict:
    script = (
        "require 'json'; require 'psych'; "
        f"puts JSON.generate(Psych.load_file('{path}'))"
    )
    result = subprocess.run(
        ["ruby", "-e", script],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(result.stdout)


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_active_film_route_metadata_matches_selector_binding():
    selector = load_yaml("runtime/state/route_chain_mode_selector.yaml")
    manifest = load_yaml("registries/route_manifests/film_screenplay_generation.yaml")
    route_slice = load_yaml("registries/route_slices/film_screenplay_generation.registry_slice.yaml")

    film_mode = selector["modes"]["film_screenplay_generation"]
    assert selector["default_mode"] == "script_only"
    assert film_mode["allowed_route_ids"] == ["FILM_SCREENPLAY_GENERATION"]

    assert manifest["route_id"] == "FILM_SCREENPLAY_GENERATION"
    assert manifest["active_route"] is True
    assert manifest["registered"] is True
    assert manifest["bound_to_route_selector"] is True
    assert manifest["selector_binding_reconciled"] is True
    assert manifest["selector_binding_source_phase"] == "12L-K"
    assert manifest["selector_binding_reconciliation_phase"] == "13E_29"
    assert manifest["runtime_behavior_changed"] is False
    assert manifest["governed_runtime_proof_claimed"] is False
    assert manifest["pass_claimed"] is False

    assert route_slice["route_id"] == "FILM_SCREENPLAY_GENERATION"
    assert route_slice["active_slice"] is True
    assert route_slice["registered"] is True
    assert route_slice["bound_to_route_selector"] is True
    assert route_slice["selector_binding_reconciled"] is True
    assert route_slice["selector_binding_source_phase"] == "12L-K"
    assert route_slice["selector_binding_reconciliation_phase"] == "13E_29"
    assert route_slice["runtime_behavior_changed"] is False
    assert route_slice["governed_runtime_proof_claimed"] is False
    assert route_slice["pass_claimed"] is False

    requirements = route_slice["runtime_state_requirements"]
    assert requirements["selector_binding_required"] is True
    assert requirements["route_activation_requires_later_selector_patch"] is False
    assert route_slice["laws"]["FILM_SCREENPLAY_GENERATION_NOT_SELECTOR_BOUND"] is False


def test_script_generation_and_no_proof_boundaries_remain_present():
    selector_text = read("runtime/state/route_chain_mode_selector.yaml")
    script_slice = load_yaml("registries/route_slices/script_generation.registry_slice.yaml")
    film_slice_text = read("registries/route_slices/film_screenplay_generation.registry_slice.yaml")
    manifest_text = read("registries/route_manifests/film_screenplay_generation.yaml")

    assert "default_mode: script_only" in selector_text
    assert script_slice["route_id"] == "SCRIPT_GENERATION"
    assert "SCRIPT_GENERATION_PRESERVED: true" in film_slice_text
    assert "governed_runtime_proof_claimed: false" in manifest_text
    assert "governed_runtime_proof_claimed: false" in film_slice_text
    assert "pass_claimed: false" in manifest_text
    assert "pass_claimed: false" in film_slice_text


if __name__ == "__main__":
    test_active_film_route_metadata_matches_selector_binding()
    test_script_generation_and_no_proof_boundaries_remain_present()
    print("phase_13e29_active_film_route_binding_metadata_ok")
