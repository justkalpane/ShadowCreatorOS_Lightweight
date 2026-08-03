from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import contains_any, packet, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    world = data.get("world_bible") or {}
    scene_cards = data.get("scene_cards") or []
    chain_text = " ".join(world.get("consequence_chain", [])).lower()
    errors = []
    if "pressure" not in chain_text and "threat" not in chain_text:
        errors.append("consequence chain missing pressure")
    if "anger" not in chain_text and "fear" not in chain_text and "distance" not in chain_text:
        errors.append("consequence chain missing emotional driver")
    if "repair" not in chain_text and "trust" not in chain_text:
        errors.append("consequence chain missing repair")
    scene_text = " ".join(str(card.get("turning_point", "")) + " " + str(card.get("conflict", "")) for card in scene_cards).lower()
    if not contains_any(scene_text, ["repair", "trust", "fear", "anger", "distance"]):
        errors.append("consequence chain not reflected in scenes")
    return result("validate_film_consequence_logic", not errors, errors)
