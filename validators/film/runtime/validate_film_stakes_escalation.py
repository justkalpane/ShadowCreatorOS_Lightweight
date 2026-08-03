from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import contains_any, packet, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    beats = data.get("beat_sheet") or []
    scene_cards = data.get("scene_cards") or []
    character_arc = data.get("character_arc") or {}
    errors = []
    if not beats:
        errors.append("beat_sheet missing")
    stakes_changes = [str(beat.get("stakes_change", "")).lower() for beat in beats]
    if any(not change for change in stakes_changes):
        errors.append("each beat must include stakes_change")
    if len(set(stakes_changes)) < 3:
        errors.append("flat_stakes")
    if not contains_any(" ".join(stakes_changes), [str(character_arc.get("want", "")).lower().split()[0], "trust", "family", "child", "safety"]):
        errors.append("stakes_not_tied_to_character")
    if "toddler" not in " ".join(stakes_changes) and "child" not in " ".join(stakes_changes):
        errors.append("stakes must preserve toddler/family pressure")
    card_text = " ".join(str(card.get("conflict", "")) + " " + str(card.get("turning_point", "")) for card in scene_cards).lower()
    if not contains_any(card_text, ["trust", "family", "child", "anger", "fear", "love"]):
        errors.append("stakes_not_reflected_in_scene_cards")
    return result("validate_film_stakes_escalation", not errors, errors)
