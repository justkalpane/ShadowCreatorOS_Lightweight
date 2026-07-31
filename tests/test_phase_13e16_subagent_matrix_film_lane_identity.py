import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from agents.common.sub_agent_matrix import get_sub_agent_entry, load_sub_agent_matrix
from agents.common.workflow_binding_contracts import get_workflow_contract


TARGET_WORKFLOWS = {
    "wf_200": {
        "workflow_id": "WF-200",
        "workflow_name": "wf200_script_intelligence_pack",
        "workflow_class": "parent_pack",
        "workflow_family": "parent_pack",
        "parent_pack": "",
        "route_bindings": ["ROUTE_PHASE1_STANDARD", "ROUTE_PHASE1_FAST"],
        "required_inputs": [
            "topic_finalization_packet",
            "research_synthesis_packet",
            "orchestration_decision",
        ],
        "allowed_directors": ["Vyasa", "Yama", "Kubera"],
        "lane": "film_screenplay_parent_lane",
        "preservation_key": "legacy_route_bindings_preserved",
    },
    "cwf_210": {
        "workflow_id": "CWF-210",
        "workflow_name": "cwf210_script_generation",
        "workflow_class": "child",
        "workflow_family": "script",
        "parent_pack": "WF-200",
        "route_bindings": [],
        "required_inputs": ["topic_finalization_packet", "research_synthesis_packet"],
        "allowed_directors": ["Vyasa", "Saraswati", "Krishna"],
        "lane": "film_screenplay_draft_lane",
        "preservation_key": "route_bindings_preserved_as_empty_child_lane",
    },
    "cwf_220": {
        "workflow_id": "CWF-220",
        "workflow_name": "cwf220_script_debate",
        "workflow_class": "child",
        "workflow_family": "script",
        "parent_pack": "WF-200",
        "route_bindings": [],
        "required_inputs": ["script_draft_packet"],
        "allowed_directors": ["Krishna", "Durga", "Yama", "Saraswati"],
        "lane": "film_screenplay_critique_lane",
        "preservation_key": "route_bindings_preserved_as_empty_child_lane",
    },
    "cwf_230": {
        "workflow_id": "CWF-230",
        "workflow_name": "cwf230_script_refinement",
        "workflow_class": "child",
        "workflow_family": "script",
        "parent_pack": "WF-200",
        "route_bindings": [],
        "required_inputs": ["script_debate_packet"],
        "allowed_directors": ["Saraswati", "Krishna", "Vyasa"],
        "lane": "film_screenplay_revision_lane",
        "preservation_key": "route_bindings_preserved_as_empty_child_lane",
    },
    "cwf_240": {
        "workflow_id": "CWF-240",
        "workflow_name": "cwf240_final_script_shaping",
        "workflow_class": "child",
        "workflow_family": "script",
        "parent_pack": "WF-200",
        "route_bindings": [],
        "required_inputs": ["script_refinement_packet"],
        "allowed_directors": ["Krishna", "Saraswati", "Durga"],
        "lane": "film_screenplay_output_packet_lane",
        "preservation_key": "route_bindings_preserved_as_empty_child_lane",
    },
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_subagent_matrix_preserves_structural_invariants():
    matrix = load_sub_agent_matrix()
    assert matrix["matrix_name"] == "sub_agent_matrix"
    assert matrix["schema_version"] == "1.0.0"
    assert matrix["source_registry"] == "subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml"
    assert matrix["total_sub_agents"] == 36
    assert len(matrix["entries"]) == 36

    for slug, expected in TARGET_WORKFLOWS.items():
        entry = get_sub_agent_entry(slug)
        assert entry["workflow_id"] == expected["workflow_id"], slug
        assert entry["workflow_name"] == expected["workflow_name"], slug
        assert entry["workflow_class"] == expected["workflow_class"], slug
        assert entry["workflow_family"] == expected["workflow_family"], slug
        assert entry["parent_pack"] == expected["parent_pack"], slug
        assert entry["route_bindings"] == expected["route_bindings"], slug
        assert entry["required_inputs"] == expected["required_inputs"], slug
        assert entry["allowed_directors"] == expected["allowed_directors"], slug
        assert entry["gate_rules"]["enforce_director_binding"] is True, slug
        assert entry["gate_rules"]["require_dossier_id"] is True, slug
        assert entry["gate_rules"]["require_declared_inputs"] is True, slug
        assert entry["gate_rules"]["require_governance_ack_on_release"] is False, slug
        assert entry["gate_rules"]["escalate_to"] == "WF-900", slug
        assert entry["runtime_base"] == "WorkflowSubAgentBase", slug
        assert entry["binding_runtime_check"] == "WorkflowSubAgentBase", slug


def test_target_matrix_entries_expose_additive_film_lane_identity():
    for slug, expected in TARGET_WORKFLOWS.items():
        entry = get_sub_agent_entry(slug)
        overlay = entry["phase_13e_16_film_lane_identity"]
        contract_overlay = get_workflow_contract(slug)["phase_13e_13_film_lane_identity"]

        assert overlay["status"] == "ADDITIVE_SUBAGENT_MATRIX_FILM_LANE_IDENTITY", slug
        assert overlay["source_phase"] == "13E_16", slug
        assert overlay["mirrors_workflow_contract_phase"] == "13E_13", slug
        assert overlay["runtime_behavior_changed"] is False, slug
        assert overlay["selector_modified"] is False, slug
        assert overlay["active_route_registry_modified"] is False, slug
        assert overlay["route_binding_modified"] is False, slug
        assert overlay["required_inputs_modified"] is False, slug
        assert overlay["allowed_directors_modified"] is False, slug
        assert overlay["gate_rules_modified"] is False, slug
        assert overlay["pass_claimed"] is False, slug
        assert overlay["runtime_proof_claimed"] is False, slug
        assert overlay["script_generation_preserved"] is True, slug
        assert overlay["film_screenplay_generation_preserved"] is True, slug
        assert overlay["shared_with_script_generation"] is True, slug
        assert overlay["film_route_id"] == "FILM_SCREENPLAY_GENERATION", slug
        assert overlay["script_route_id"] == "SCRIPT_GENERATION", slug
        assert overlay["cinema_department_lane"] == expected["lane"], slug
        assert overlay["cinema_department_lane"] == contract_overlay["cinema_department_lane"], slug
        assert overlay["cinema_craft_responsibility"] == contract_overlay["cinema_craft_responsibility"], slug
        assert overlay["content_route_boundary"] == contract_overlay["content_route_boundary"], slug
        assert overlay["downstream_boundary"] == contract_overlay["downstream_boundary"], slug
        assert overlay["matrix_mirror_only"] is True, slug
        assert overlay["no_fake_pass_boundary"] is True, slug
        assert expected["preservation_key"] in overlay, slug


def test_film_lane_identity_overlay_is_limited_to_approved_targets():
    approved = set(TARGET_WORKFLOWS)
    entries_with_overlay = {
        entry["workflow_slug"]
        for entry in load_sub_agent_matrix()["entries"]
        if "phase_13e_16_film_lane_identity" in entry
    }
    assert entries_with_overlay == approved


def test_phase_13e16_did_not_touch_route_boundary_files():
    selector = read("runtime/state/route_chain_mode_selector.yaml")
    film_manifest = read("registries/route_manifests/film_screenplay_generation.yaml")
    film_slice = read("registries/route_slices/film_screenplay_generation.registry_slice.yaml")
    script_slice = read("registries/route_slices/script_generation.registry_slice.yaml")

    assert "default_mode: script_only" in selector
    assert "film_screenplay_generation:" in selector
    assert 'route_id: "FILM_SCREENPLAY_GENERATION"' in film_manifest
    assert "bound_to_route_selector: false" in film_manifest
    assert "bound_to_route_selector: false" in film_slice
    assert "SCRIPT_GENERATION_PRESERVED: true" in film_slice
    assert "route_id: SCRIPT_GENERATION" in script_slice


if __name__ == "__main__":
    test_subagent_matrix_preserves_structural_invariants()
    test_target_matrix_entries_expose_additive_film_lane_identity()
    test_film_lane_identity_overlay_is_limited_to_approved_targets()
    test_phase_13e16_did_not_touch_route_boundary_files()
    print("phase_13e16_subagent_matrix_film_lane_identity_ok")
