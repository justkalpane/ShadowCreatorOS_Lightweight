"""Cinema-depth character arc progression analysis."""

from __future__ import annotations

from typing import Any


def build_character_arc_progression(
    character_arc: dict[str, Any],
    relationship_map: dict[str, Any],
    scene_cards: list[dict[str, Any]],
) -> dict[str, Any]:
    protagonist = character_arc.get("protagonist")
    want = str(character_arc.get("want", "")).strip()
    need = str(character_arc.get("need", "")).strip()
    flaw = str(character_arc.get("flaw", "")).strip()
    wound = str(character_arc.get("wound", "")).strip()
    contradiction = str(character_arc.get("contradiction", "")).strip()
    relationship = (relationship_map.get("relationships") or [{}])[0]
    flaw_tokens = {
        token.lower().strip(".,!?;:'\"")
        for token in f"{flaw} {character_arc.get('opposing_force', '')} {character_arc.get('relationship_pressure', '')}".split()
        if len(token.strip(".,!?;:'\"")) > 4
    }
    pressure_aliases = {
        "silence": {"silence", "quiet", "disappearing", "withdrawal", "distance", "unspoken"},
        "control": {"control", "right", "protecting", "contained", "restraint"},
        "anger": {"anger", "shame", "fear", "coldness", "force", "panic"},
        "trust": {"trust", "bond", "tenderness", "repair", "honesty"},
        "pressure": {"pressure", "costing", "watches", "children", "partner"},
    }

    decision_progression = []
    for card in scene_cards:
        decision_progression.append(
            {
                "scene_number": card.get("scene_number"),
                "decision": card.get("scene_objective"),
                "conflict": card.get("conflict"),
                "turning_point": card.get("turning_point"),
                "behavior_shift": card.get("emotional_value_end") != card.get("emotional_value_start"),
            }
        )

    relationship_shift_map = [
        {
            "scene_number": card.get("scene_number"),
            "relationship_pressure": relationship.get("conflict_source"),
            "mirror_function_active": "mirror" in str(card.get("dialogue_subtext_goal", "")).lower(),
            "end_state": card.get("emotional_value_end"),
        }
        for card in scene_cards
    ]
    arc_completion_status = (
        want
        and need
        and want != need
        and character_arc.get("transformation_start") != character_arc.get("transformation_end")
        and any(item["behavior_shift"] for item in decision_progression[-3:])
    )
    return {
        "character_arc_map": {
            "protagonist": protagonist,
            "want": want,
            "need": need,
            "flaw": flaw,
            "wound": wound,
            "contradiction": contradiction,
            "transformation_start": character_arc.get("transformation_start"),
            "transformation_midpoint": character_arc.get("transformation_midpoint"),
            "transformation_end": character_arc.get("transformation_end"),
        },
        "want_need_gap": want != need and bool(want and need),
        "flaw_pressure_points": [
            item["scene_number"]
            for item in decision_progression
            if (
                flaw_tokens.intersection(set(str(item["conflict"]).lower().replace(",", " ").replace(".", " ").split()))
                or any(
                    token in str(item["conflict"]).lower()
                    for base, aliases in pressure_aliases.items()
                    if base in " ".join(sorted(flaw_tokens))
                    for token in aliases
                )
                or any(
                    token in str(item["turning_point"]).lower()
                    for token in {"shame", "distance", "withdrawal", "tenderness", "trust", "panic", "force"}
                )
            )
        ],
        "relationship_shift_map": relationship_shift_map,
        "decision_progression": decision_progression,
        "arc_completion_status": arc_completion_status,
    }
