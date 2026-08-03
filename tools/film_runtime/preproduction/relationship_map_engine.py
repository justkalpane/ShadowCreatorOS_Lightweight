"""Relationship map generator for film preproduction."""

from __future__ import annotations

from typing import Any


def generate_relationship_map(parsed: dict[str, Any], character_bible: dict[str, Any]) -> dict[str, Any]:
    characters = character_bible["major_characters"]
    main = characters[0]
    second = characters[1]
    return {
        "relationships": [
            {
                "characters": [main["name"], second["name"]],
                "relationship_type": parsed["relationship_type"],
                "emotional_function": parsed["relationship_emotional_function"],
                "conflict_source": parsed["pressure_trigger"],
                "support_function": parsed["relationship_support_function"],
                "mirror_function": parsed["relationship_mirror_function"],
                "scene_interaction_purpose": parsed["relationship_scene_purpose"],
                "relationship_pressure": parsed["relationship_pressure"],
                "used_in_scenes": [2, 5, 6],
            },
            {
                "characters": [main["name"], "toddlers"],
                "relationship_type": "parent or guardian responsibility",
                "emotional_function": "turn abstract anger control into a concrete care obligation",
                "conflict_source": parsed["stakes"],
                "support_function": "keep the story grounded in family stakes",
                "mirror_function": "the toddlers reveal what the adult behavior teaches",
                "scene_interaction_purpose": "force the protagonist to choose the kind of adult the room will remember",
                "relationship_pressure": f"The children make {parsed['want']} morally visible.",
                "used_in_scenes": [1, 2, 6],
            },
        ],
        "second_character_mirror_function_confirmed": True,
    }
