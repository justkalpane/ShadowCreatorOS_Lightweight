import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


PRIMARY_REGISTRY = "registries/skill_registry_wf200.yaml"
SECONDARY_REGISTRY = "registries/skill_registry_wf-200.yaml"

PRIMARY_SKILLS = [
    "M-031",
    "M-032",
    "M-033",
    "M-034",
    "M-035",
    "M-036",
    "M-037",
    "M-038",
    "M-039",
    "M-040",
]

SECONDARY_SKILLS = [
    "M-041",
    "M-042",
    "M-043",
    "M-044",
    "M-051",
    "M-052",
    "M-053",
    "M-054",
    "M-061",
    "M-062",
    "M-063",
    "M-064",
    "M-071",
    "M-072",
    "M-073",
    "M-074",
]

EXPECTED_CLASSIFICATIONS = {
    "M-031": "SCRIPT_GENERATION_ONLY",
    "M-032": "FILM_SCREENPLAY_SUPPORT_METADATA_ONLY",
    "M-033": "SCRIPT_GENERATION_ONLY",
    "M-034": "FILM_SCREENPLAY_SUPPORT_METADATA_ONLY",
    "M-035": "SCRIPT_GENERATION_ONLY",
    "M-036": "FILM_SCREENPLAY_SUPPORT_METADATA_ONLY",
    "M-037": "SCRIPT_GENERATION_ONLY",
    "M-038": "FILM_SCREENPLAY_SUPPORT_METADATA_ONLY",
    "M-039": "SCRIPT_GENERATION_ONLY",
    "M-040": "FILM_SCREENPLAY_SUPPORT_METADATA_ONLY",
    "M-041": "FILM_SCREENPLAY_SUPPORT_METADATA_ONLY",
    "M-042": "DOWNSTREAM_ONLY",
    "M-043": "DOWNSTREAM_ONLY",
    "M-044": "DOWNSTREAM_ONLY",
    "M-051": "SCRIPT_GENERATION_ONLY",
    "M-052": "SCRIPT_GENERATION_ONLY",
    "M-053": "SCRIPT_GENERATION_ONLY",
    "M-054": "SCRIPT_GENERATION_ONLY",
    "M-061": "SYSTEM_SUPPORT_METADATA_ONLY",
    "M-062": "SYSTEM_SUPPORT_METADATA_ONLY",
    "M-063": "SYSTEM_SUPPORT_METADATA_ONLY",
    "M-064": "SYSTEM_SUPPORT_METADATA_ONLY",
    "M-071": "SYSTEM_SUPPORT_METADATA_ONLY",
    "M-072": "SYSTEM_SUPPORT_METADATA_ONLY",
    "M-073": "SCRIPT_GENERATION_ONLY",
    "M-074": "SCRIPT_GENERATION_ONLY",
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


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


def assert_overlay(registry: dict, expected_skills: list[str]):
    overlay = registry["phase_13e_22_film_lane_identity"]
    assert overlay["status"] == "ADDITIVE_SKILL_REGISTRY_FILM_LANE_IDENTITY"
    assert overlay["source_phase"] == "13E_22"
    assert overlay["mirrors_agent_runtime_index_phase"] == "13E_19"
    assert overlay["mirrors_subagent_matrix_phase"] == "13E_16"
    assert overlay["mirrors_workflow_contract_phase"] == "13E_13"
    assert overlay["runtime_behavior_changed"] is False
    assert overlay["selector_modified"] is False
    assert overlay["active_route_registry_modified"] is False
    assert overlay["skill_ids_modified"] is False
    assert overlay["skill_implementations_modified"] is False
    assert overlay["skill_runtime_behavior_modified"] is False
    assert overlay["script_generation_preserved"] is True
    assert overlay["film_screenplay_generation_preserved"] is True
    assert overlay["film_route_id"] == "FILM_SCREENPLAY_GENERATION"
    assert overlay["script_route_id"] == "SCRIPT_GENERATION"
    assert overlay["registry_mirror_only"] is True
    assert overlay["no_fake_pass_boundary"] is True
    assert overlay["target_skill_count"] == len(expected_skills)

    classifications = overlay["per_skill_classification"]
    assert set(classifications) == set(expected_skills)
    for skill_id in expected_skills:
        assert classifications[skill_id]["classification"] == EXPECTED_CLASSIFICATIONS[skill_id]
        assert classifications[skill_id]["not_film_core_authority"] is True


def test_wf200_skill_registries_preserve_skill_ids_and_order():
    primary = load_yaml(PRIMARY_REGISTRY)
    secondary = load_yaml(SECONDARY_REGISTRY)

    assert primary["workflow_pack"] == "WF-200"
    assert primary["description"] == (
        "Script Intelligence pack skill list. Canonical M-xxx skill IDs aligned "
        "with master skill_registry.yaml (script_vein assignment)."
    )
    assert primary["skills"] == PRIMARY_SKILLS

    assert secondary["workflow_pack"] == "WF-200"
    assert secondary["pack_name"] == "Script Intelligence Pipeline"
    assert secondary["phase"] == "Phase-1"
    assert secondary["stage"] == "Stage-C"
    assert secondary["skills"] == SECONDARY_SKILLS


def test_target_registries_expose_additive_film_lane_identity_metadata():
    assert_overlay(load_yaml(PRIMARY_REGISTRY), PRIMARY_SKILLS)
    assert_overlay(load_yaml(SECONDARY_REGISTRY), SECONDARY_SKILLS)


def test_master_skill_registry_was_not_promoted_in_phase_13e22():
    master = read("registries/skill_registry.yaml")
    assert "phase_13e_22_film_lane_identity" not in master


def test_phase_13e22_did_not_touch_route_boundary_files():
    selector = read("runtime/state/route_chain_mode_selector.yaml")
    film_manifest = read("registries/route_manifests/film_screenplay_generation.yaml")
    film_slice = read("registries/route_slices/film_screenplay_generation.registry_slice.yaml")
    script_slice = read("registries/route_slices/script_generation.registry_slice.yaml")

    assert "default_mode: script_only" in selector
    assert "film_screenplay_generation:" in selector
    assert 'route_id: "FILM_SCREENPLAY_GENERATION"' in film_manifest
    assert "bound_to_route_selector: true" in film_manifest
    assert "bound_to_route_selector: true" in film_slice
    assert "SCRIPT_GENERATION_PRESERVED: true" in film_slice
    assert "route_id: SCRIPT_GENERATION" in script_slice


if __name__ == "__main__":
    test_wf200_skill_registries_preserve_skill_ids_and_order()
    test_target_registries_expose_additive_film_lane_identity_metadata()
    test_master_skill_registry_was_not_promoted_in_phase_13e22()
    test_phase_13e22_did_not_touch_route_boundary_files()
    print("phase_13e22_skill_registry_film_lane_identity_ok")
