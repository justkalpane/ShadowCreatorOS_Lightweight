from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    timeline = (data.get("world_bible") or {}).get("timeline") or []
    scene_cards = data.get("scene_cards") or []
    errors = []
    if len(timeline) < 3:
        errors.append("timeline must cover at least 3 scenes")
    numbers = []
    for item in timeline:
        if not isinstance(item, dict):
            errors.append("timeline entries must be objects")
            continue
        for field in ["scene_number", "time_of_day", "location"]:
            if field not in item:
                errors.append(f"timeline entry missing {field}")
        if "scene_number" in item:
            numbers.append(item["scene_number"])
    if numbers and numbers != sorted(numbers):
        errors.append("timeline scene numbers must be ordered")
    if len(numbers) != len(scene_cards):
        errors.append("timeline must align to scene card count")
    for card, item in zip(scene_cards, timeline):
        if card.get("location") != item.get("location"):
            errors.append("timeline location does not match scene card")
    return result("validate_film_timeline_continuity", not errors, errors)
