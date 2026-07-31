import ast
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

EXPECTED_24_AGENTS = {
    "agni": "agents/agni/agni_agent.py",
    "arjuna": "agents/arjuna/arjuna_agent.py",
    "aruna": "agents/aruna/aruna_agent.py",
    "brahma": "agents/brahma/brahma_agent.py",
    "durga": "agents/durga/durga_agent.py",
    "ganesha": "agents/ganesha/ganesha_agent.py",
    "garuda": "agents/garuda/garuda_agent.py",
    "hanuman": "agents/hanuman/hanuman_agent.py",
    "indra": "agents/indra/indra_agent.py",
    "kali": "agents/kali/kali_agent.py",
    "kama": "agents/kama/kama_agent.py",
    "krishna": "agents/krishna/krishna_agent.py",
    "maya": "agents/maya/maya_agent.py",
    "narada": "agents/narada/narada_agent.py",
    "nataraja": "agents/nataraja/nataraja_agent.py",
    "parashara": "agents/parashara/parashara_agent.py",
    "saraswati": "agents/saraswati/saraswati_agent.py",
    "shakti": "agents/shakti/shakti_agent.py",
    "shiva": "agents/shiva/shiva_agent.py",
    "valmiki": "agents/valmiki/valmiki_agent.py",
    "varuna": "agents/varuna/varuna_agent.py",
    "vishnu": "agents/vishnu/vishnu_agent.py",
    "vyasa": "agents/vyasa/vyasa_agent.py",
    "yama": "agents/yama/yama_agent.py",
}


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_profile_assignments():
    source = read("agents/common/director_authority_profiles.py")
    module = ast.parse(source)
    assignments = {}
    for node in module.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.target.id in {
                "DIRECTOR_AUTHORITY_PROFILES",
                "PHASE_13E_8_NAMED_AGENT_CINEMA_PROFILE_OVERLAY",
            }:
                assignments[node.target.id] = ast.literal_eval(node.value)
    return assignments


def load_matrix():
    return json.loads(read("registries/agent_class_matrix.json"))


def test_all_24_named_agent_files_remain_present_and_marked():
    marker = "PHASE 13E_6 NAMED AGENT 24-CRAFT CINEMA ALIGNMENT"
    for slug, path in EXPECTED_24_AGENTS.items():
        text = read(path)
        assert marker in text, slug


def test_runtime_registry_lists_all_24_named_agent_surfaces():
    registry = read("agents/AGENT_RUNTIME_REGISTRY.yaml")
    for slug, path in EXPECTED_24_AGENTS.items():
        assert f"file: {path}" in registry, slug
    assert "phase_13e_8_named_agent_cinema_profile_overlay:" in registry
    assert "kali_added_to_runtime_registry: true" in registry
    assert "named_agent_count: 24" in registry


def test_agent_class_matrix_adds_kali_without_losing_legacy_entries():
    matrix = load_matrix()
    entries = matrix["entries"]
    assert matrix["total_agents"] == 115
    assert matrix["family_totals"]["named_director"] == 33
    assert len(entries) == matrix["total_agents"]

    by_slug = {}
    for entry in entries:
        by_slug.setdefault(entry["agent_slug"], []).append(entry)

    for slug in EXPECTED_24_AGENTS:
        assert len(by_slug.get(slug, [])) == 1, slug

    kali = by_slug["kali"][0]
    assert kali["registry_path"] == "agents/kali/kali_agent.py"
    assert kali["agent_class"] == "KaliAgent"
    assert kali["director_binding"] == "Kali"
    assert kali["artifact_family"] == "kali-agent-packet"
    assert kali["phase_13e_8_additive_registry_profile_coherence"]["selector_modified"] is False
    assert kali["phase_13e_8_additive_registry_profile_coherence"]["runtime_proof_claimed"] is False


def test_authority_profiles_include_all_24_named_agents_and_cinema_overlay():
    assignments = load_profile_assignments()
    profiles = assignments["DIRECTOR_AUTHORITY_PROFILES"]
    overlay = assignments["PHASE_13E_8_NAMED_AGENT_CINEMA_PROFILE_OVERLAY"]

    for slug in EXPECTED_24_AGENTS:
        assert slug in profiles, slug
        assert slug in overlay, slug
        assert "cinema_craft_authority" in overlay[slug], slug
        assert "mythology_fidelity_lock" in overlay[slug], slug
        assert "downstream_boundary" in overlay[slug], slug

    assert profiles["kali"]["director_name"] == "Kali"
    assert profiles["kali"]["director_id"] == "DIR-CINv1-006"
    assert profiles["kali"]["role"] == "Revision Rupture | Moral Conflict | Decisive Cut"
    assert "thumbnail provocation" in overlay["kali"]["downstream_boundary"]


def test_get_director_profile_unknown_fallback_is_preserved():
    from agents.common.director_authority_profiles import get_director_profile

    unknown = get_director_profile("UnknownPhase13E8Probe")
    assert unknown["director_id"] == "UNKNOWN"
    assert unknown["role"] == "Generic Director"
    assert unknown["authority_mode"] == "general"


def test_selector_and_active_route_files_keep_boundary_markers():
    selector = read("runtime/state/route_chain_mode_selector.yaml")
    film_manifest = read("registries/route_manifests/film_screenplay_generation.yaml")
    film_slice = read("registries/route_slices/film_screenplay_generation.registry_slice.yaml")

    assert "default_mode: script_only" in selector
    assert "film_screenplay_generation:" in selector
    assert 'route_id: "FILM_SCREENPLAY_GENERATION"' in film_manifest
    assert "bound_to_route_selector: false" in film_manifest
    assert "bound_to_route_selector: false" in film_slice


if __name__ == "__main__":
    test_all_24_named_agent_files_remain_present_and_marked()
    test_runtime_registry_lists_all_24_named_agent_surfaces()
    test_agent_class_matrix_adds_kali_without_losing_legacy_entries()
    test_authority_profiles_include_all_24_named_agents_and_cinema_overlay()
    test_get_director_profile_unknown_fallback_is_preserved()
    test_selector_and_active_route_files_keep_boundary_markers()
    print("phase_13e8_named_agent_registry_profile_coherence_ok")
