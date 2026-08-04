"""Cinema-depth continuity tracker."""

from __future__ import annotations

from typing import Any


ALIASES = {
    "visible": {"visible", "pause", "restraint", "contained", "honesty", "staying"},
    "restraint": {"restraint", "pause", "contained", "quiet", "honesty", "vulnerability", "stays"},
    "interrupts": {"interrupts", "stops", "breaks", "chooses", "returns", "interrupts", "softens"},
    "escalation": {"escalation", "pressure", "anger", "friction", "distance", "withdrawal", "pride"},
    "self-awareness": {"self-awareness", "realizes", "understands", "lucid"},
    "reframes": {"reframes", "changes", "turns", "pivots"},
    "consequence": {"consequence", "stakes", "legacy", "memory"},
    "repair": {"repair", "returns", "restores", "trust"},
    "mistakes": {"mistakes", "misreads", "protects", "hides"},
    "silence": {"silence", "quiet", "soft-spoken", "pause"},
    "control": {"control", "contained", "discipline", "authority"},
    "anger": {"anger", "pressure", "friction", "temper"},
}


def _semantic_token_match(tokens: list[str], scene_blob: str) -> bool:
    matched = 0
    for token in tokens:
        forms = ALIASES.get(token, {token})
        if any(form in scene_blob for form in forms):
            matched += 1
    return matched >= min(2, len(tokens))


def build_continuity_map(
    scene_cards: list[dict[str, Any]],
    beat_sheet: list[dict[str, Any]],
    world_bible: dict[str, Any],
) -> dict[str, Any]:
    setup_payoff_tracker = []
    decision_memory = []
    unresolved_thread_flags = []
    relationship_continuity = []
    location_continuity = []
    prior_turns: list[str] = []
    prior_tokens: set[str] = set()
    for card in scene_cards:
        scene_number = card.get("scene_number")
        turn = str(card.get("turning_point", "")).strip()
        deps = card.get("continuity_dependencies", [])
        objective = str(card.get("scene_objective", "")).lower()
        conflict = str(card.get("conflict", "")).lower()
        setup_payoff_tracker.append(
            {
                "scene_number": scene_number,
                "setup": deps[0] if deps else turn,
                "payoff": turn,
            }
        )
        decision_memory.append(
            {
                "scene_number": scene_number,
                "remembers_prior_turn": scene_number == 1 or bool(prior_tokens.intersection(set((" ".join(deps) + " " + objective + " " + conflict).lower().split()))),
                "decision": card.get("scene_objective"),
            }
        )
        relationship_continuity.append(
            {
                "scene_number": scene_number,
                "relationship_state": card.get("emotional_value_end"),
            }
        )
        location_continuity.append(
            {
                "scene_number": scene_number,
                "location": card.get("location"),
                "time_of_day": card.get("time_of_day"),
            }
        )
        current_tokens = set((turn + " " + objective + " " + conflict + " " + " ".join(deps)).lower().split())
        if scene_number > 1 and deps and not prior_tokens.intersection(current_tokens):
            unresolved_thread_flags.append(f"scene {scene_number} does not clearly pay off earlier turns")
        prior_turns.append(turn)
        prior_tokens.update(token for token in current_tokens if len(token) > 4)

    scene_blob = " ".join(
        f"{card.get('scene_objective', '')} {card.get('conflict', '')} {card.get('turning_point', '')}"
        for card in scene_cards
    ).lower()
    for consequence in world_bible.get("consequence_chain", []):
        anchor_tokens = [token.lower().strip(".,!?;:'\"") for token in str(consequence).split() if len(token.strip(".,!?;:'\"")) > 4]
        if anchor_tokens and not _semantic_token_match(anchor_tokens[:8], scene_blob):
            unresolved_thread_flags.append(f"world consequence not visible in scenes: {consequence}")

    return {
        "continuity_map": {
            "scenes_tracked": len(scene_cards),
            "beats_tracked": len(beat_sheet),
        },
        "setup_payoff_tracker": setup_payoff_tracker,
        "decision_memory": decision_memory,
        "relationship_continuity": relationship_continuity,
        "location_continuity": location_continuity,
        "unresolved_thread_flags": unresolved_thread_flags,
    }
