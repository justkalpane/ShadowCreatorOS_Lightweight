import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

PHASE_OWNERSHIP_MARKERS = [
    "PHASE 13E_1 24-CRAFT CINEMA DIRECTOR OWNERSHIP",
    "PHASE 13E_2",
    "PHASE 13E_4 REMAINING 24-CRAFT CINEMA DIRECTOR OWNERSHIP",
]

EXPECTED_24_DIRECTORS = {
    "Vyasa": "directors/research/vyasa.md",
    "Valmiki": "directors/research/valmiki.md",
    "Krishna": "directors/supreme_vision/krishna.md",
    "Saraswati": "directors/distribution/saraswati.md",
    "Nataraja": "directors/cinematic/nataraja.md",
    "Varuna": "directors/cinematic/varuna.md",
    "Garuda": "directors/cinematic/garuda.md",
    "Hanuman": "directors/cinematic/hanuman.md",
    "Ganesha": "directors/research/ganesha.md",
    "Indra": "directors/cinematic/indra.md",
    "Shakti": "directors/supreme_vision/shakti.md",
    "Durga": "directors/strategy/durga.md",
    "Kali": "directors/strategy/kali.md",
    "Agni": "directors/production/agni.md",
    "Maya": "directors/production/maya.md",
    "Brahma": "directors/supreme_vision/brahma.md",
    "Vishnu": "directors/supreme_vision/vishnu.md",
    "Shiva": "directors/supreme_vision/shiva.md",
    "Narada": "directors/strategy/narada.md",
    "Kama": "directors/distribution/kama.md",
    "Aruna": "directors/kernel/aruna.md",
    "Yama": "directors/kernel/yama.md",
    "Parashara": "directors/research/parashara.md",
    "Arjuna": "directors/production/arjuna.md",
}


def read_repo_file(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def load_director_registry_module():
    path = ROOT / "directors/DIRECTORS_COMPLETE_REGISTRY.py"
    spec = importlib.util.spec_from_file_location("directors_complete_registry", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_all_24_mythology_director_surfaces_have_phase_13e_ownership_markers():
    for name, path in EXPECTED_24_DIRECTORS.items():
        text = read_repo_file(path)
        assert any(marker in text for marker in PHASE_OWNERSHIP_MARKERS), name
        assert "runtime_behavior_changed: false" in text, name
        assert "selector_modified: false" in text, name
        assert "runtime_proof_claimed: false" in text, name
        assert "pass_claimed: false" in text, name


def test_yaml_manifest_contains_additive_24_craft_overlay_and_kali():
    text = read_repo_file("directors/DIRECTOR_REGISTRY_MANIFEST.yaml")
    assert "phase_13e_4_cinema_24_craft_director_registry_overlay:" in text
    assert "target_mythology_director_count: 24" in text
    assert "name: Kali" in text
    assert 'file: "directors/strategy/kali.md"' in text
    assert "SCRIPT_GENERATION_preserved: true" in text
    assert "FILM_SCREENPLAY_GENERATION_preserved: true" in text


def test_python_registry_contains_additive_24_craft_overlay():
    module = load_director_registry_module()
    registry = module.CINEMA_24_CRAFT_DIRECTOR_REGISTRY
    assert set(registry) == set(EXPECTED_24_DIRECTORS)
    assert registry["Kali"]["file"] == "directors/strategy/kali.md"
    assert module.CINEMA_24_CRAFT_DIRECTOR_BOUNDARY["runtime_behavior_changed"] is False
    assert module.CINEMA_24_CRAFT_DIRECTOR_BOUNDARY["selector_modified"] is False
    assert module.CINEMA_24_CRAFT_DIRECTOR_BOUNDARY["pass_claimed"] is False


if __name__ == "__main__":
    test_all_24_mythology_director_surfaces_have_phase_13e_ownership_markers()
    test_yaml_manifest_contains_additive_24_craft_overlay_and_kali()
    test_python_registry_contains_additive_24_craft_overlay()
    print("phase_13e4_director_registry_coherence_ok")
