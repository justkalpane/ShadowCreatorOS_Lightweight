from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import contains_any, packet, require_fields, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    world = data.get("world_bible") or {}
    scene_cards = data.get("scene_cards") or []
    errors = require_fields(
        world,
        [
            "world_type",
            "domestic_world_context",
            "timeline",
            "locations",
            "geography_or_spatial_logic",
            "culture_or_social_context",
            "world_rules",
            "power_dynamics",
            "consequence_chain",
            "continuity_across_scenes",
        ],
    )
    locations = world.get("locations") or []
    scene_locations = {card.get("location") for card in scene_cards}
    if not locations:
        errors.append("world_bible_empty")
    if scene_locations and not scene_locations.issubset(set(locations)):
        errors.append("locations_not_used")
    if not contains_any(" ".join(world.get("consequence_chain") or []).lower(), ["repair", "trust", "fear", "child"]):
        errors.append("consequence_chain_missing")
    if not any(contains_any(str(rule).lower(), [str(card.get("location", "")).lower().split()[0], "repair", "child"]) for rule in world.get("world_rules", []) for card in scene_cards):
        errors.append("world_rules_not_connected_to_scene_cards")
    return result("validate_film_world_bible", not errors, errors)
