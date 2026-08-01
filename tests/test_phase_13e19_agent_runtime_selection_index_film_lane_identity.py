import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from agents.common.sub_agent_matrix import get_sub_agent_entry


TARGET_AGENTS = {
    "vyasa_wf200_script_generation": {
        "agent_name": "Vyasa Script Generation Agent",
        "agent_file_path": "agents/vyasa/vyasa_agent.py",
        "task_family": "script_generation",
        "subagent_binding": "registries/sub_agent_matrix.json#CWF-210",
        "selection_use": "WF-200 script generation owner; cite for script_generation tasks.",
        "matrix_slug": "cwf_210",
        "lane": "film_screenplay_draft_lane",
        "role": "screenplay drafting selection mirror",
    },
    "krishna_wf200_script_debate": {
        "agent_name": "Krishna Script Debate Agent",
        "agent_file_path": "agents/krishna/krishna_agent.py",
        "task_family": "script_debate",
        "subagent_binding": "registries/sub_agent_matrix.json#CWF-220",
        "selection_use": "WF-200 script debate owner; cite for debate and critique tasks.",
        "matrix_slug": "cwf_220",
        "lane": "film_screenplay_critique_lane",
        "role": "screenplay critique and debate selection mirror",
    },
    "saraswati_wf200_script_refinement": {
        "agent_name": "Saraswati Script Refinement Agent",
        "agent_file_path": "agents/saraswati/saraswati_agent.py",
        "task_family": "script_refinement",
        "subagent_binding": "registries/sub_agent_matrix.json#CWF-230",
        "selection_use": "WF-200 script refinement owner; cite for refinement/final shaping tasks.",
        "matrix_slug": "cwf_230",
        "lane": "film_screenplay_revision_lane",
        "role": "screenplay refinement and revision selection mirror",
    },
    "durga_wf200_quality_gate": {
        "agent_name": "Durga Script Quality Gate Agent",
        "agent_file_path": "agents/durga/durga_agent.py",
        "task_family": "quality_gate",
        "subagent_binding": "registries/sub_agent_matrix.json#CWF-240",
        "selection_use": "WF-200 quality gate support; cite for content quality validation.",
        "matrix_slug": "cwf_240",
        "lane": "film_screenplay_output_packet_lane",
        "role": "screenplay output quality gate selection mirror",
    },
    "yama_wf200_boundary_gate": {
        "agent_name": "Yama Boundary Gate Agent",
        "agent_file_path": "agents/yama/yama_agent.py",
        "task_family": "provider_handoff_packet",
        "subagent_binding": "registries/sub_agent_matrix.json#CWF-240",
        "selection_use": "WF-200 provider/media boundary support; cite for no-execution handoff safety.",
        "matrix_slug": "cwf_240",
        "lane": "film_screenplay_output_packet_lane",
        "role": "screenplay output boundary and no-execution handoff selection mirror",
    },
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_index() -> dict:
    script = (
        "require 'json'; require 'psych'; "
        "puts JSON.generate(Psych.load_file('registries/agent_runtime_selection_index.yaml'))"
    )
    result = subprocess.run(
        ["ruby", "-e", script],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    return json.loads(result.stdout)


def target_entry(index: dict, agent_id: str) -> dict:
    for entry in index["agent_runtime_selection_index"]:
        if entry.get("agent_id") == agent_id:
            return entry
    raise AssertionError(f"missing agent entry {agent_id}")


def test_agent_runtime_selection_index_preserves_existing_selection_fields():
    index = load_index()
    assert len(index["agent_runtime_selection_index"]) == 85

    for agent_id, expected in TARGET_AGENTS.items():
        entry = target_entry(index, agent_id)
        assert entry["agent_name"] == expected["agent_name"], agent_id
        assert entry["agent_file_path"] == expected["agent_file_path"], agent_id
        assert entry["task_family"] == expected["task_family"], agent_id
        assert entry["director_binding"] == "registries/director_binding_wf200.yaml", agent_id
        assert entry["subagent_binding"] == expected["subagent_binding"], agent_id
        assert entry["skill_binding"] == "registries/skill_registry_wf200.yaml", agent_id
        assert entry["selection_use"] == expected["selection_use"], agent_id
        assert entry["evidence_status"] == "PROVEN_BY_FILE_DISCOVERY", agent_id


def test_target_index_entries_expose_additive_film_lane_identity():
    index = load_index()

    for agent_id, expected in TARGET_AGENTS.items():
        entry = target_entry(index, agent_id)
        overlay = entry["phase_13e_19_film_lane_identity"]
        matrix_overlay = get_sub_agent_entry(expected["matrix_slug"])["phase_13e_16_film_lane_identity"]

        assert overlay["status"] == "ADDITIVE_AGENT_RUNTIME_SELECTION_FILM_LANE_IDENTITY", agent_id
        assert overlay["source_phase"] == "13E_19", agent_id
        assert overlay["mirrors_subagent_matrix_phase"] == "13E_16", agent_id
        assert overlay["mirrors_workflow_contract_phase"] == "13E_13", agent_id
        assert overlay["runtime_behavior_changed"] is False, agent_id
        assert overlay["selector_modified"] is False, agent_id
        assert overlay["active_route_registry_modified"] is False, agent_id
        assert overlay["selection_rule_modified"] is False, agent_id
        assert overlay["subagent_binding_modified"] is False, agent_id
        assert overlay["director_binding_modified"] is False, agent_id
        assert overlay["skill_binding_modified"] is False, agent_id
        assert overlay["task_family_modified"] is False, agent_id
        assert overlay["evidence_status_modified"] is False, agent_id
        assert overlay["pass_claimed"] is False, agent_id
        assert overlay["runtime_proof_claimed"] is False, agent_id
        assert overlay["script_generation_preserved"] is True, agent_id
        assert overlay["film_screenplay_generation_preserved"] is True, agent_id
        assert overlay["shared_with_script_generation"] is True, agent_id
        assert overlay["film_route_id"] == "FILM_SCREENPLAY_GENERATION", agent_id
        assert overlay["script_route_id"] == "SCRIPT_GENERATION", agent_id
        assert overlay["referenced_subagent_binding"] == expected["subagent_binding"], agent_id
        assert overlay["referenced_matrix_lane"] == expected["lane"], agent_id
        assert overlay["cinema_department_lane"] == expected["lane"], agent_id
        assert overlay["cinema_department_lane"] == matrix_overlay["cinema_department_lane"], agent_id
        assert overlay["cinema_agent_role"] == expected["role"], agent_id
        assert overlay["matrix_mirror_only"] is True, agent_id
        assert overlay["no_fake_pass_boundary"] is True, agent_id


def test_film_lane_identity_overlay_is_limited_to_approved_agent_entries():
    index = load_index()
    entries_with_overlay = {
        entry["agent_id"]
        for entry in index["agent_runtime_selection_index"]
        if "phase_13e_19_film_lane_identity" in entry
    }
    assert entries_with_overlay == set(TARGET_AGENTS)


def test_phase_13e19_did_not_touch_route_boundary_files():
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
    test_agent_runtime_selection_index_preserves_existing_selection_fields()
    test_target_index_entries_expose_additive_film_lane_identity()
    test_film_lane_identity_overlay_is_limited_to_approved_agent_entries()
    test_phase_13e19_did_not_touch_route_boundary_files()
    print("phase_13e19_agent_runtime_selection_index_film_lane_identity_ok")
