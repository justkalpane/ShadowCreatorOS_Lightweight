from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

MARKER = "## PHASE 13E_1 24-CRAFT CINEMA DIRECTOR OWNERSHIP"

PHASE_13E1_DIRECTORS = [
    "directors/cinematic/garuda.md",
    "directors/cinematic/nataraja.md",
    "directors/cinematic/varuna.md",
    "directors/cinematic/hanuman.md",
    "directors/cinematic/indra.md",
    "directors/production/agni.md",
    "directors/production/arjuna.md",
    "directors/production/maya.md",
    "directors/supreme_vision/brahma.md",
    "directors/supreme_vision/vishnu.md",
    "directors/supreme_vision/shiva.md",
    "directors/strategy/durga.md",
    "directors/research/ganesha.md",
    "directors/research/parashara.md",
    "directors/kernel/yama.md",
]

DEFERRED_DIRTY_DIRECTORS = [
    "directors/distribution/kama.md",
    "directors/kernel/aruna.md",
    "directors/research/valmiki.md",
    "directors/research/vyasa.md",
    "directors/supreme_vision/krishna.md",
]

REQUIRED_BOUNDARIES = [
    "phase_13e_1_status: BOUNDED_DIRECTOR_OWNERSHIP_ALIGNMENT",
    "runtime_behavior_changed: false",
    "selector_modified: false",
    "active_registry_modified: false",
    "runtime_proof_claimed: false",
    "pass_claimed: false",
    "script_generation_preserved: true",
    "film_screenplay_generation_preserved: true",
    "### Cinema craft ownership",
    "### Mythology fidelity lock",
    "### Cinema department authority",
    "### Route boundary",
]


def read_repo_file(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_phase_13e1_clean_director_batch_contains_ownership_blocks():
    for path in PHASE_13E1_DIRECTORS:
        text = read_repo_file(path)
        assert MARKER in text, path
        for boundary in REQUIRED_BOUNDARIES:
            assert boundary in text, f"{path} missing {boundary}"


def test_phase_13e1_deferred_dirty_directors_were_not_marked_by_this_batch():
    for path in DEFERRED_DIRTY_DIRECTORS:
        text = read_repo_file(path)
        assert MARKER not in text, path


def test_phase_13e1_missing_kali_surface_remains_explicitly_deferred():
    assert not (ROOT / "directors/strategy/kali.md").exists()
    assert not (ROOT / "directors/supreme_vision/kali.md").exists()


if __name__ == "__main__":
    test_phase_13e1_clean_director_batch_contains_ownership_blocks()
    test_phase_13e1_deferred_dirty_directors_were_not_marked_by_this_batch()
    test_phase_13e1_missing_kali_surface_remains_explicitly_deferred()
    print("phase_13e1_director_ownership_blocks_ok")
