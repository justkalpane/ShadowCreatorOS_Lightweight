from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import contains_any, packet, require_fields, result


def validate(payload: dict) -> dict:
    arc = packet(payload).get("character_arc") or {}
    errors = require_fields(
        arc,
        [
            "protagonist",
            "want",
            "need",
            "flaw",
            "wound",
            "contradiction",
            "moral_dilemma",
            "opposing_force",
            "transformation_start",
            "transformation_midpoint",
            "transformation_end",
            "relationship_pressure",
            "emotional_continuity_by_scene",
            "behavioral_consistency_rules",
            "arc_turning_points",
        ],
    )
    if str(arc.get("want", "")).strip().lower() == str(arc.get("need", "")).strip().lower():
        errors.append("want_equals_need")
    if not contains_any(str(arc.get("flaw", "")).lower(), str(arc.get("relationship_pressure", "")).lower().split() + str(arc.get("moral_dilemma", "")).lower().split()):
        errors.append("flaw_not_used")
    if not contains_any(str(arc.get("moral_dilemma", "")).lower(), ["or", "versus", "protect", "betray", "trust", "fear"]):
        errors.append("moral_dilemma_missing_choice")
    if str(arc.get("transformation_start", "")).strip().lower() == str(arc.get("transformation_end", "")).strip().lower():
        errors.append("character_no_transformation")
    if not contains_any(str(arc.get("opposing_force", "")).lower(), str(arc.get("wound", "")).lower().split() + str(arc.get("flaw", "")).lower().split()):
        errors.append("opposing_force_not_connected")
    continuity = arc.get("emotional_continuity_by_scene") or []
    if not isinstance(continuity, list) or len(continuity) < 3:
        errors.append("character arc must track emotional continuity by scene")
    return result("validate_film_character_arc", not errors, errors)
