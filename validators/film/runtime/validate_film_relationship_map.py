from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    rel = data.get("relationship_map") or {}
    scene_cards = data.get("scene_cards") or []
    errors = []
    relationships = rel.get("relationships") or []
    if not relationships:
        errors.append("relationships missing")
    mirror_relationship = None
    for item in relationships:
        for field in [
            "characters",
            "relationship_type",
            "emotional_function",
            "conflict_source",
            "support_function",
            "mirror_function",
            "scene_interaction_purpose",
            "relationship_pressure",
            "used_in_scenes",
        ]:
            if field not in item or item.get(field) in ({}, [], "", None):
                errors.append(f"relationship entry missing {field}")
        if "mirror" in str(item.get("mirror_function", "")).lower() or "reflect" in str(item.get("mirror_function", "")).lower():
            mirror_relationship = item
    if mirror_relationship is None:
        errors.append("mirror_function_missing")
    else:
        used = set(mirror_relationship.get("used_in_scenes") or [])
        scene_numbers = {card.get("scene_number") for card in scene_cards}
        if not used or not used.issubset(scene_numbers):
            errors.append("relationship_not_used_in_scene_cards")
        if "support" not in str(mirror_relationship.get("support_function", "")).lower() and "hold" not in str(mirror_relationship.get("support_function", "")).lower():
            errors.append("decorative_second_character")
    return result("validate_film_relationship_map", not errors, errors)
