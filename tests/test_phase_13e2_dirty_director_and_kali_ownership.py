from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DIRTY_MARKER = "## PHASE 13E_2 DIRTY-SCOPE 24-CRAFT CINEMA DIRECTOR OWNERSHIP"
KALI_MARKER = "## 2. PHASE 13E_2 24-CRAFT CINEMA DIRECTOR OWNERSHIP"

DIRTY_BATCH_DIRECTORS = [
    "directors/distribution/kama.md",
    "directors/kernel/aruna.md",
    "directors/research/valmiki.md",
    "directors/research/vyasa.md",
    "directors/supreme_vision/krishna.md",
]

REQUIRED_DIRTY_BOUNDARIES = [
    "phase_13e_2_status: DIRTY_SCOPE_INDEX_AWARE_OWNERSHIP_ALIGNMENT",
    "runtime_behavior_changed: false",
    "selector_modified: false",
    "active_registry_modified: false",
    "runtime_proof_claimed: false",
    "pass_claimed: false",
    "script_generation_preserved: true",
    "film_screenplay_generation_preserved: true",
    "pre_existing_dirty_hunks_preserved: true",
    "### Cinema craft ownership",
    "### Mythology fidelity lock",
    "### Cinema department authority",
    "### Route boundary",
]

REQUIRED_KALI_BOUNDARIES = [
    "phase_13e_2_status: NEW_DIRECTOR_SURFACE_CREATED_FOR_MISSING_24_CRAFT_ROLE",
    "runtime_behavior_changed: false",
    "selector_modified: false",
    "active_registry_modified: false",
    "runtime_proof_claimed: false",
    "pass_claimed: false",
    "registered_in_runtime: false",
    "dramatic_conflict_and_stakes",
    "Kali is not a virality, shock-value, controversy, rage-bait, thumbnail, shorts, or platform outrage authority.",
]


def read_repo_file(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_phase_13e2_dirty_director_batch_contains_index_aware_blocks():
    for path in DIRTY_BATCH_DIRECTORS:
        text = read_repo_file(path)
        assert DIRTY_MARKER in text, path
        for boundary in REQUIRED_DIRTY_BOUNDARIES:
            assert boundary in text, f"{path} missing {boundary}"


def test_phase_13e2_kali_strategy_surface_created_with_boundaries():
    path = "directors/strategy/kali.md"
    text = read_repo_file(path)
    assert KALI_MARKER in text
    for boundary in REQUIRED_KALI_BOUNDARIES:
        assert boundary in text, f"{path} missing {boundary}"


def test_phase_13e2_kali_not_created_under_supreme_vision():
    assert not (ROOT / "directors/supreme_vision/kali.md").exists()


if __name__ == "__main__":
    test_phase_13e2_dirty_director_batch_contains_index_aware_blocks()
    test_phase_13e2_kali_strategy_surface_created_with_boundaries()
    test_phase_13e2_kali_not_created_under_supreme_vision()
    print("phase_13e2_dirty_director_and_kali_ownership_ok")
