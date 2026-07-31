import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from agents.common.workflow_binding_contracts import get_workflow_contract


TARGET_WORKFLOWS = {
    "wf_200": {
        "workflow_id": "WF-200",
        "workflow_name": "wf200_script_intelligence_pack",
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
        "route_bindings": [],
        "required_inputs": ["topic_finalization_packet", "research_synthesis_packet"],
        "allowed_directors": ["Vyasa", "Saraswati", "Krishna"],
        "lane": "film_screenplay_draft_lane",
        "preservation_key": "route_bindings_preserved_as_empty_child_lane",
    },
    "cwf_220": {
        "workflow_id": "CWF-220",
        "workflow_name": "cwf220_script_debate",
        "route_bindings": [],
        "required_inputs": ["script_draft_packet"],
        "allowed_directors": ["Krishna", "Durga", "Yama", "Saraswati"],
        "lane": "film_screenplay_critique_lane",
        "preservation_key": "route_bindings_preserved_as_empty_child_lane",
    },
    "cwf_230": {
        "workflow_id": "CWF-230",
        "workflow_name": "cwf230_script_refinement",
        "route_bindings": [],
        "required_inputs": ["script_debate_packet"],
        "allowed_directors": ["Saraswati", "Krishna", "Vyasa"],
        "lane": "film_screenplay_revision_lane",
        "preservation_key": "route_bindings_preserved_as_empty_child_lane",
    },
    "cwf_240": {
        "workflow_id": "CWF-240",
        "workflow_name": "cwf240_final_script_shaping",
        "route_bindings": [],
        "required_inputs": ["script_refinement_packet"],
        "allowed_directors": ["Krishna", "Saraswati", "Durga"],
        "lane": "film_screenplay_output_packet_lane",
        "preservation_key": "route_bindings_preserved_as_empty_child_lane",
    },
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_target_workflow_contracts_preserve_existing_behavioral_fields():
    for slug, expected in TARGET_WORKFLOWS.items():
        contract = get_workflow_contract(slug)
        assert contract["workflow_id"] == expected["workflow_id"], slug
        assert contract["workflow_name"] == expected["workflow_name"], slug
        assert contract["route_bindings"] == expected["route_bindings"], slug
        assert contract["required_inputs"] == expected["required_inputs"], slug
        assert contract["allowed_directors"] == expected["allowed_directors"], slug
        assert contract["gate_rules"]["enforce_director_binding"] is True, slug
        assert contract["gate_rules"]["require_dossier_id"] is True, slug
        assert contract["gate_rules"]["require_declared_inputs"] is True, slug
        assert contract["gate_rules"]["require_governance_ack_on_release"] is False, slug
        assert contract["gate_rules"]["escalate_to"] == "WF-900", slug


def test_target_workflow_contracts_expose_additive_film_lane_identity():
    for slug, expected in TARGET_WORKFLOWS.items():
        overlay = get_workflow_contract(slug)["phase_13e_13_film_lane_identity"]
        assert overlay["status"] == "ADDITIVE_WORKFLOW_BINDING_FILM_LANE_IDENTITY", slug
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
        assert "SCRIPT_GENERATION criteria only" in overlay["content_route_boundary"], slug
        assert "downstream" in overlay["downstream_boundary"], slug
        assert overlay["no_fake_pass_boundary"] is True, slug
        assert expected["preservation_key"] in overlay, slug


def test_phase_13e10_subagent_overlay_and_route_boundary_files_still_align():
    registry = read("subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml")
    selector = read("runtime/state/route_chain_mode_selector.yaml")
    film_manifest = read("registries/route_manifests/film_screenplay_generation.yaml")
    film_slice = read("registries/route_slices/film_screenplay_generation.registry_slice.yaml")
    script_slice = read("registries/route_slices/script_generation.registry_slice.yaml")

    assert "phase_13e_10_subagent_cinema_lane_overlay:" in registry
    assert "default_mode: script_only" in selector
    assert "film_screenplay_generation:" in selector
    assert 'route_id: "FILM_SCREENPLAY_GENERATION"' in film_manifest
    assert "bound_to_route_selector: false" in film_manifest
    assert "bound_to_route_selector: false" in film_slice
    assert "SCRIPT_GENERATION_PRESERVED: true" in film_slice

    for subagent_path in [
        "subagents/wf_200/wf_200_sub_agent.py",
        "subagents/cwf_210/cwf_210_sub_agent.py",
        "subagents/cwf_220/cwf_220_sub_agent.py",
        "subagents/cwf_230/cwf_230_sub_agent.py",
        "subagents/cwf_240/cwf_240_sub_agent.py",
    ]:
        assert subagent_path in film_manifest
        assert subagent_path in script_slice


if __name__ == "__main__":
    test_target_workflow_contracts_preserve_existing_behavioral_fields()
    test_target_workflow_contracts_expose_additive_film_lane_identity()
    test_phase_13e10_subagent_overlay_and_route_boundary_files_still_align()
    print("phase_13e13_workflow_binding_film_lane_identity_ok")
