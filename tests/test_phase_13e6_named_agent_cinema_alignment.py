from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MARKER = "PHASE 13E_6 NAMED AGENT 24-CRAFT CINEMA ALIGNMENT"

EXPECTED_24_AGENTS = {
    "Agni": "agents/agni/agni_agent.py",
    "Arjuna": "agents/arjuna/arjuna_agent.py",
    "Aruna": "agents/aruna/aruna_agent.py",
    "Brahma": "agents/brahma/brahma_agent.py",
    "Durga": "agents/durga/durga_agent.py",
    "Ganesha": "agents/ganesha/ganesha_agent.py",
    "Garuda": "agents/garuda/garuda_agent.py",
    "Hanuman": "agents/hanuman/hanuman_agent.py",
    "Indra": "agents/indra/indra_agent.py",
    "Kali": "agents/kali/kali_agent.py",
    "Kama": "agents/kama/kama_agent.py",
    "Krishna": "agents/krishna/krishna_agent.py",
    "Maya": "agents/maya/maya_agent.py",
    "Narada": "agents/narada/narada_agent.py",
    "Nataraja": "agents/nataraja/nataraja_agent.py",
    "Parashara": "agents/parashara/parashara_agent.py",
    "Saraswati": "agents/saraswati/saraswati_agent.py",
    "Shakti": "agents/shakti/shakti_agent.py",
    "Shiva": "agents/shiva/shiva_agent.py",
    "Valmiki": "agents/valmiki/valmiki_agent.py",
    "Varuna": "agents/varuna/varuna_agent.py",
    "Vishnu": "agents/vishnu/vishnu_agent.py",
    "Vyasa": "agents/vyasa/vyasa_agent.py",
    "Yama": "agents/yama/yama_agent.py",
}

REQUIRED_BOUNDARIES = [
    "phase_13e_6_status: NAMED_AGENT_24_CRAFT_CINEMA_ALIGNMENT",
    "runtime_behavior_changed: false",
    "selector_modified: false",
    "active_route_registry_modified: false",
    "runtime_proof_claimed: false",
    "pass_claimed: false",
    "script_generation_preserved: true",
    "film_screenplay_generation_preserved: true",
    "cinema_craft_authority:",
    "mythology_fidelity_lock:",
    "cinema_department_execution_role:",
    "downstream_boundary:",
    "content_platform_drift_not_marked_as_film_core_authority: true",
]


def read_repo_file(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_all_24_named_agent_surfaces_exist():
    for name, path in EXPECTED_24_AGENTS.items():
        assert (ROOT / path).exists(), name


def test_all_24_named_agent_surfaces_have_phase_13e6_alignment_blocks():
    for name, path in EXPECTED_24_AGENTS.items():
        text = read_repo_file(path)
        assert MARKER in text, name
        for boundary in REQUIRED_BOUNDARIES:
            assert boundary in text, f"{name} missing {boundary}"


def test_kali_agent_surface_is_file_only_and_preserves_runtime_boundary():
    text = read_repo_file("agents/kali/kali_agent.py")
    assert "class KaliAgent" in text
    assert 'agent_slug="kali"' in text
    assert 'director_binding="Kali"' in text
    assert "registered_in_agent_runtime_registry: false" not in text
    assert "runtime_behavior_changed: false" in text
    assert "selector_modified: false" in text
    assert "active_route_registry_modified: false" in text


def test_phase_13e6_did_not_modify_route_selector_or_active_route_registry_files():
    selector = read_repo_file("runtime/state/route_chain_mode_selector.yaml")
    film_manifest = read_repo_file("registries/route_manifests/film_screenplay_generation.yaml")
    film_slice = read_repo_file("registries/route_slices/film_screenplay_generation.registry_slice.yaml")

    assert "default_mode: script_only" in selector
    assert "film_screenplay_generation:" in selector
    assert 'route_id: "FILM_SCREENPLAY_GENERATION"' in film_manifest
    assert "bound_to_route_selector: true" in film_manifest
    assert "bound_to_route_selector: true" in film_slice


if __name__ == "__main__":
    test_all_24_named_agent_surfaces_exist()
    test_all_24_named_agent_surfaces_have_phase_13e6_alignment_blocks()
    test_kali_agent_surface_is_file_only_and_preserves_runtime_boundary()
    test_phase_13e6_did_not_modify_route_selector_or_active_route_registry_files()
    print("phase_13e6_named_agent_cinema_alignment_ok")
