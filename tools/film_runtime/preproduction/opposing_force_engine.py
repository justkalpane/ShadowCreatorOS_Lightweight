"""Opposing force builder for compact film preproduction."""

from __future__ import annotations

from typing import Any


def generate_opposing_force(parsed: dict[str, Any], character_bible: dict[str, Any]) -> dict[str, Any]:
    main = character_bible["major_characters"][0]
    return {
        "opposing_force": parsed["opposing_force"],
        "type": f"{parsed['genre']}_pressure_engine",
        "external_face": parsed["pressure_trigger"],
        "internal_face": main["flaw"],
        "opposes": main["name"],
        "relationship_pressure": parsed["relationship_pressure"],
        "story_function": "force the protagonist to choose between reaction and care",
        "antagonist_required": parsed["genre"] in {"thriller", "crime", "action"},
    }
