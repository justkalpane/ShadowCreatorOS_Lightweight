"""Continuity bible builder for the film preproduction packet."""

from __future__ import annotations

from typing import Any


def generate_continuity_bible(parsed: dict[str, Any], scene_cards: list[dict[str, Any]], beat_sheet: list[dict[str, Any]]) -> dict[str, Any]:
    toddler_stakes = parsed["toddler_stakes_detail"]
    return {
        "timeline": [
            {"scene_number": card["scene_number"], "time_of_day": card["time_of_day"], "slugline": card["slugline"]}
            for card in scene_cards
        ],
        "location_continuity": [
            {"scene_number": card["scene_number"], "location": card["location"]}
            for card in scene_cards
        ],
        "character_emotional_state_by_scene": [
            {
                "scene_number": card["scene_number"],
                "start": card["emotional_value_start"],
                "end": card["emotional_value_end"],
            }
            for card in scene_cards
        ],
        "toddler_stakes_continuity": [
            {"scene_number": card["scene_number"], "stakes": toddler_stakes}
            for card in scene_cards
            if "toddlers" in card["characters_present"] or "toddler" in " ".join(card["continuity_dependencies"]).lower()
        ],
        "object_or_visual_motif_continuity": [
            {"scene_number": card["scene_number"], "visual_motif": card["visual_motif"]}
            for card in scene_cards
        ],
        "unresolved_promises": [
            "The protagonist must return to the room with repair, not explanation."
        ],
        "resolved_promises": [
            "The closing image protects the toddler stakes.",
            "The beat sheet moves from pressure to visible restraint to repair.",
        ],
        "beat_order": [beat["beat_id"] for beat in beat_sheet],
    }
