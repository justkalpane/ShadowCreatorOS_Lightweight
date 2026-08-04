"""Cinema-depth genre differentiation analysis."""

from __future__ import annotations

from typing import Any


def build_genre_depth_map(parsed: dict[str, Any], beat_sheet: list[dict[str, Any]], scene_cards: list[dict[str, Any]]) -> dict[str, Any]:
    genre = parsed.get("genre")
    conflict_blob = " ".join(str(card.get("conflict", "")) for card in scene_cards).lower()
    turn_blob = " ".join(str(card.get("turning_point", "")) for card in scene_cards).lower()
    required_turns = []
    failure_flags = []
    if genre == "thriller":
        required_turns = ["threat escalates", "midpoint reversal", "climax under danger"]
        if not any(term in conflict_blob for term in ["threat", "danger", "panic", "fear", "risk"]):
            failure_flags.append("thriller lacks escalating threat language")
    elif genre == "romance":
        required_turns = ["relationship rupture", "misread reversal", "earned reconciliation"]
        if not any(term in conflict_blob for term in ["distance", "trust", "wound", "withdrawal", "intimacy"]):
            failure_flags.append("romance lacks relationship-state conflict")
    else:
        required_turns = ["belief tested", "midpoint self-recognition", "repair through action"]
        if not any(term in conflict_blob for term in ["anger", "pressure", "legacy", "trust", "repair"]):
            failure_flags.append("motivational drama lacks belief-action pressure")

    genre_pacing_profile = {
        "beat_count": len(beat_sheet),
        "scene_count": len(scene_cards),
        "turn_density": len([card for card in scene_cards if card.get("turning_point")]) / max(1, len(scene_cards)),
    }
    if genre_pacing_profile["turn_density"] < 0.8:
        failure_flags.append("genre pacing lacks enough turning points")

    return {
        "genre_depth_map": {
            "genre": genre,
            "conflict_pattern": conflict_blob,
            "turn_pattern": turn_blob,
        },
        "genre_required_turns": required_turns,
        "genre_specific_conflict_pattern": conflict_blob,
        "genre_pacing_profile": genre_pacing_profile,
        "genre_failure_flags": failure_flags,
    }
