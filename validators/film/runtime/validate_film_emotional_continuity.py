from __future__ import annotations

import json

from validators.film.runtime.preproduction_validator_utils import contains_any, packet, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    continuity = data.get("continuity_bible") or {}
    states = continuity.get("character_emotional_state_by_scene") or []
    scene_cards = data.get("scene_cards") or []
    errors = []
    if len(states) < 3:
        errors.append("emotional continuity requires at least 3 scene states")
    numbers = []
    for state in states:
        if not isinstance(state, dict):
            errors.append("emotional continuity entries must be objects")
            continue
        if any(field not in state for field in ["scene_number", "start", "end"]):
            errors.append("emotional continuity states must include scene_number/start/end")
            continue
        numbers.append(state["scene_number"])
    if numbers and numbers != sorted(numbers):
        errors.append("emotional continuity scene order invalid")
    if len(states) != len(scene_cards):
        errors.append("emotional continuity must align to scene cards")
    joined = json.dumps(continuity).lower()
    if not contains_any(joined, ["repair", "hopeful", "trust", "softened"]):
        errors.append("emotional continuity missing repair/hopeful resolution")
    if "toddler" not in joined and "child" not in joined:
        errors.append("emotional continuity must preserve toddler stakes")
    return result("validate_film_emotional_continuity", not errors, errors)
