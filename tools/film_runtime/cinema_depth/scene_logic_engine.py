"""Cinema-depth scene logic analysis."""

from __future__ import annotations

from typing import Any


def build_scene_logic_map(scene_cards: list[dict[str, Any]]) -> dict[str, Any]:
    scene_logic_map = []
    scene_objectives = []
    scene_conflicts = []
    turning_points = []
    scene_consequences = []
    cause_effect_links = []
    duplicate_conflict_flags = []
    summary_scene_flags = []

    seen_pairs: dict[tuple[str, str], int] = {}
    previous_turn = ""
    for index, card in enumerate(scene_cards):
        objective = str(card.get("scene_objective") or card.get("objective") or "").strip()
        conflict = str(card.get("conflict") or "").strip()
        turn = str(card.get("turning_point") or card.get("turn") or "").strip()
        consequence = str(card.get("scene_consequence") or f"{turn} forces the next scene to respond.").strip()
        scene_number = card.get("scene_number")
        scene_logic_map.append(
            {
                "scene_number": scene_number,
                "objective": objective,
                "conflict": conflict,
                "turning_point": turn,
                "consequence": consequence,
                "next_scene_dependency": card.get("next_scene_dependency") or consequence,
            }
        )
        scene_objectives.append(objective)
        scene_conflicts.append(conflict)
        turning_points.append(turn)
        scene_consequences.append(consequence)
        if conflict:
            pair = (conflict.lower(), turn.lower())
            seen_pairs[pair] = seen_pairs.get(pair, 0) + 1
            if seen_pairs[pair] >= 3:
                duplicate_conflict_flags.append(
                    f"scene {scene_number} repeats conflict pattern too often: {conflict}"
                )
        if previous_turn:
            cause_effect_links.append(
                {
                    "from_scene": scene_cards[index - 1].get("scene_number"),
                    "to_scene": scene_number,
                    "cause": previous_turn,
                    "effect": objective or conflict,
                }
            )
        previous_turn = turn
        if len(conflict.split()) < 4 and len(turn.split()) < 4:
            summary_scene_flags.append(f"scene {scene_number} reads like summary rather than dramatic event")

    return {
        "scene_logic_map": scene_logic_map,
        "scene_objectives": scene_objectives,
        "scene_conflicts": scene_conflicts,
        "turning_points": turning_points,
        "scene_consequences": scene_consequences,
        "cause_effect_links": cause_effect_links,
        "duplicate_conflict_flags": duplicate_conflict_flags,
        "summary_scene_flags": summary_scene_flags,
    }
