from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

TARGET_SUBAGENTS = {
    "wf_200": {
        "path": "subagents/wf_200/wf_200_sub_agent.py",
        "lane": "film_screenplay_parent_lane",
        "responsibility": "story architecture",
        "script_marker": "script_generation_parent_lane",
    },
    "cwf_210": {
        "path": "subagents/cwf_210/cwf_210_sub_agent.py",
        "lane": "film_screenplay_draft_lane",
        "responsibility": "screenplay structure",
        "script_marker": "script_generation_draft_lane",
    },
    "cwf_220": {
        "path": "subagents/cwf_220/cwf_220_sub_agent.py",
        "lane": "film_screenplay_critique_lane",
        "responsibility": "scene dramaturgy",
        "script_marker": "script_generation_critique_lane",
    },
    "cwf_230": {
        "path": "subagents/cwf_230/cwf_230_sub_agent.py",
        "lane": "film_screenplay_revision_lane",
        "responsibility": "act/sequence repair",
        "script_marker": "script_generation_refinement_lane",
    },
    "cwf_240": {
        "path": "subagents/cwf_240/cwf_240_sub_agent.py",
        "lane": "film_screenplay_output_packet_lane",
        "responsibility": "screenplay packet closure",
        "script_marker": "script_generation_packaging_lane",
    },
}

REQUIRED_OVERLAY_MARKERS = [
    "PHASE 13E_10 SUBAGENT CINEMA DEPARTMENT LANE OVERLAY",
    "phase_13e_10_status: SUBAGENT_CINEMA_DEPARTMENT_LANE_OVERLAY",
    "runtime_behavior_changed: false",
    "selector_modified: false",
    "active_route_registry_modified: false",
    "runtime_proof_claimed: false",
    "pass_claimed: false",
    "script_generation_preserved: true",
    "film_screenplay_generation_preserved: true",
    "shared_with_script_generation: true",
    "film_route_id: FILM_SCREENPLAY_GENERATION",
    "script_route_id: SCRIPT_GENERATION",
    "cinema_department_lane:",
    "cinema_craft_responsibility:",
    "content_route_boundary:",
    "downstream_boundary:",
    "no_fake_pass_boundary: true",
]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_target_subagents_have_phase_13e10_overlay_and_preserve_script_markers():
    for slug, config in TARGET_SUBAGENTS.items():
        text = read(config["path"])
        for marker in REQUIRED_OVERLAY_MARKERS:
            assert marker in text, f"{slug} missing {marker}"
        assert config["lane"] in text, slug
        assert config["responsibility"] in text, slug
        assert config["script_marker"] in text, slug


def test_subagent_runtime_registry_has_phase_13e10_overlay():
    text = read("subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml")
    assert "phase_13e_10_subagent_cinema_lane_overlay:" in text
    assert "status: ADDITIVE_CINEMA_DEPARTMENT_LANE_OVERLAY" in text
    assert "target_subagent_count: 5" in text
    assert "film_route_id: FILM_SCREENPLAY_GENERATION" in text
    assert "script_route_id: SCRIPT_GENERATION" in text
    assert "script_generation_preserved: true" in text
    assert "film_screenplay_generation_preserved: true" in text
    for config in TARGET_SUBAGENTS.values():
        assert f"file: {config['path']}" in text
        assert config["lane"] in text


def test_film_and_script_route_subagent_sharing_is_explicitly_preserved():
    film_manifest = read("registries/route_manifests/film_screenplay_generation.yaml")
    script_manifest = read("registries/route_manifests/script_generation.yaml")
    for config in TARGET_SUBAGENTS.values():
        assert config["path"] in film_manifest
        assert config["path"] in script_manifest


def test_selector_and_active_route_boundary_markers_remain_present():
    selector = read("runtime/state/route_chain_mode_selector.yaml")
    film_manifest = read("registries/route_manifests/film_screenplay_generation.yaml")
    film_slice = read("registries/route_slices/film_screenplay_generation.registry_slice.yaml")

    assert "default_mode: script_only" in selector
    assert "film_screenplay_generation:" in selector
    assert 'route_id: "FILM_SCREENPLAY_GENERATION"' in film_manifest
    assert "bound_to_route_selector: true" in film_manifest
    assert "bound_to_route_selector: true" in film_slice


if __name__ == "__main__":
    test_target_subagents_have_phase_13e10_overlay_and_preserve_script_markers()
    test_subagent_runtime_registry_has_phase_13e10_overlay()
    test_film_and_script_route_subagent_sharing_is_explicitly_preserved()
    test_selector_and_active_route_boundary_markers_remain_present()
    print("phase_13e10_subagent_cinema_lane_overlay_ok")
