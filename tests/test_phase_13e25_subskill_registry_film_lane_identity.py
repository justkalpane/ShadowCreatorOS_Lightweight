import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = "registries/subskill_runtime_registry.yaml"

TARGETS = {
    "SS-110": {
        "name": "openrouter_llm_route_governor",
        "consumer_workflows": ["WF-010", "WF-100", "WF-200"],
        "classification": "SYSTEM_SUPPORT_METADATA_ONLY",
    },
    "SS-111": {
        "name": "ollama_local_inference_optimizer",
        "consumer_workflows": ["WF-010", "WF-100", "WF-200"],
        "classification": "SYSTEM_SUPPORT_METADATA_ONLY",
    },
    "SS-230": {
        "name": "content_angle_generator",
        "consumer_workflows": ["WF-200", "CWF-210", "CWF-230"],
        "classification": "SCRIPT_GENERATION_ONLY",
    },
    "SS-231": {
        "name": "unique_value_proposition_builder",
        "consumer_workflows": ["WF-200", "CWF-210", "CWF-230"],
        "classification": "SCRIPT_GENERATION_ONLY",
    },
    "SS-232": {
        "name": "series_strategy_planner",
        "consumer_workflows": ["WF-200", "CWF-210", "CWF-230"],
        "classification": "SCRIPT_GENERATION_ONLY",
    },
    "SS-233": {
        "name": "content_calendar_generator",
        "consumer_workflows": ["WF-200", "CWF-210", "CWF-230"],
        "classification": "SCRIPT_GENERATION_ONLY",
    },
    "SS-234": {
        "name": "platform_strategy_mapper",
        "consumer_workflows": ["WF-200", "CWF-210", "CWF-230"],
        "classification": "SCRIPT_GENERATION_ONLY",
    },
    "SS-240": {
        "name": "hook_variation_generator",
        "consumer_workflows": ["WF-200", "CWF-220", "CWF-240"],
        "classification": "SCRIPT_GENERATION_ONLY",
    },
    "SS-241": {
        "name": "open_loop_generator",
        "consumer_workflows": ["WF-200", "CWF-220", "CWF-240"],
        "classification": "SCRIPT_GENERATION_ONLY",
    },
    "SS-242": {
        "name": "story_tension_builder",
        "consumer_workflows": ["WF-200", "CWF-220", "CWF-240"],
        "classification": "FILM_SCREENPLAY_SUPPORT_METADATA_ONLY",
    },
    "SS-243": {
        "name": "pacing_controller",
        "consumer_workflows": ["WF-200", "CWF-220", "CWF-240"],
        "classification": "FILM_SCREENPLAY_SUPPORT_METADATA_ONLY",
    },
    "SS-244": {
        "name": "retention_loop_engine",
        "consumer_workflows": ["WF-200", "CWF-220", "CWF-240"],
        "classification": "SCRIPT_GENERATION_ONLY",
    },
    "SS-245": {
        "name": "cliffhanger_designer",
        "consumer_workflows": ["WF-200", "CWF-220", "CWF-240"],
        "classification": "FILM_SCREENPLAY_SUPPORT_METADATA_ONLY",
    },
    "SS-250": {
        "name": "dynamic_prompt_builder",
        "consumer_workflows": ["WF-010", "WF-100", "WF-200"],
        "classification": "SYSTEM_SUPPORT_METADATA_ONLY",
    },
    "SS-251": {
        "name": "context_window_optimizer",
        "consumer_workflows": ["WF-010", "WF-100", "WF-200"],
        "classification": "SYSTEM_SUPPORT_METADATA_ONLY",
    },
    "SS-252": {
        "name": "token_efficiency_engine",
        "consumer_workflows": ["WF-010", "WF-100", "WF-200"],
        "classification": "SYSTEM_SUPPORT_METADATA_ONLY",
    },
    "SS-253": {
        "name": "multi_model_consensus_engine",
        "consumer_workflows": ["WF-010", "WF-100", "WF-200"],
        "classification": "SYSTEM_SUPPORT_METADATA_ONLY",
    },
    "SS-254": {
        "name": "fallback_prompt_engine",
        "consumer_workflows": ["WF-010", "WF-100", "WF-200"],
        "classification": "SYSTEM_SUPPORT_METADATA_ONLY",
    },
}

DIRTY_SUBSKILL_PATHS = [
    "skills/sub_skills/SS-241-open-loop-generator.py",
    "skills/sub_skills/SS-241-open-loop-generator.subskill.md",
    "skills/sub_skills/SS-243-pacing-controller.py",
    "skills/sub_skills/SS-244-retention-loop-engine.py",
    "skills/sub_skills/SS-244-retention-loop-engine.subskill.md",
]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_registry() -> dict:
    script = (
        "require 'json'; require 'psych'; "
        f"puts JSON.generate(Psych.load_file('{REGISTRY_PATH}'))"
    )
    result = subprocess.run(
        ["ruby", "-e", script],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(result.stdout)


def entries_by_id(registry: dict) -> dict:
    return {entry["subskill_id"]: entry for entry in registry["subskills"]}


def test_subskill_registry_preserves_entry_shape_and_target_scope():
    registry = load_registry()
    entries = entries_by_id(registry)

    assert registry["version"] == 1
    assert len(registry["subskills"]) == 40
    assert len(entries) == 40

    entries_with_overlay = {
        entry["subskill_id"]
        for entry in registry["subskills"]
        if "phase_13e_25_film_lane_identity" in entry
    }
    assert entries_with_overlay == set(TARGETS)


def test_target_subskill_registry_entries_preserve_existing_fields():
    entries = entries_by_id(load_registry())

    for subskill_id, expected in TARGETS.items():
        entry = entries[subskill_id]
        assert entry["name"] == expected["name"], subskill_id
        assert entry["consumer_workflows"] == expected["consumer_workflows"], subskill_id
        assert entry["spec_file"].startswith("skills/sub_skills/"), subskill_id
        assert entry["runtime_file"].startswith("skills/sub_skills/"), subskill_id
        assert Path(ROOT / entry["spec_file"]).is_file(), subskill_id
        assert Path(ROOT / entry["runtime_file"]).is_file(), subskill_id


def test_target_subskill_registry_entries_expose_additive_film_lane_identity():
    entries = entries_by_id(load_registry())

    for subskill_id, expected in TARGETS.items():
        overlay = entries[subskill_id]["phase_13e_25_film_lane_identity"]
        assert overlay["status"] == "ADDITIVE_SUBSKILL_REGISTRY_FILM_LANE_IDENTITY", subskill_id
        assert overlay["source_phase"] == "13E_25", subskill_id
        assert overlay["mirrors_skill_registry_phase"] == "13E_22", subskill_id
        assert overlay["mirrors_agent_runtime_index_phase"] == "13E_19", subskill_id
        assert overlay["mirrors_subagent_matrix_phase"] == "13E_16", subskill_id
        assert overlay["mirrors_workflow_contract_phase"] == "13E_13", subskill_id
        assert overlay["classification"] == expected["classification"], subskill_id
        assert overlay["runtime_behavior_changed"] is False, subskill_id
        assert overlay["selector_modified"] is False, subskill_id
        assert overlay["active_route_registry_modified"] is False, subskill_id
        assert overlay["subskill_ids_modified"] is False, subskill_id
        assert overlay["consumer_workflows_modified"] is False, subskill_id
        assert overlay["spec_files_modified"] is False, subskill_id
        assert overlay["runtime_files_modified"] is False, subskill_id
        assert overlay["subskill_runtime_behavior_modified"] is False, subskill_id
        assert overlay["script_generation_preserved"] is True, subskill_id
        assert overlay["film_screenplay_generation_preserved"] is True, subskill_id
        assert overlay["film_route_id"] == "FILM_SCREENPLAY_GENERATION", subskill_id
        assert overlay["script_route_id"] == "SCRIPT_GENERATION", subskill_id
        assert overlay["registry_mirror_only"] is True, subskill_id
        assert overlay["no_fake_pass_boundary"] is True, subskill_id
        assert overlay["not_film_core_authority"] is True, subskill_id


def test_phase_13e25_did_not_add_metadata_to_subskill_files_or_route_boundaries():
    for path in DIRTY_SUBSKILL_PATHS:
        assert "phase_13e_25_film_lane_identity" not in read(path), path

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
    test_subskill_registry_preserves_entry_shape_and_target_scope()
    test_target_subskill_registry_entries_preserve_existing_fields()
    test_target_subskill_registry_entries_expose_additive_film_lane_identity()
    test_phase_13e25_did_not_add_metadata_to_subskill_files_or_route_boundaries()
    print("phase_13e25_subskill_registry_film_lane_identity_ok")
