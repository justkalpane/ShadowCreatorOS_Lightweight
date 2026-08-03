"""Compact world bible engine for realistic domestic drama."""

from __future__ import annotations

from typing import Any


def generate_world_bible(parsed: dict[str, Any], scene_cards: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "world_type": "domestic_realism",
        "domestic_world_context": f"The story world is a realistic family space inside {parsed['setting']}, pressured by {parsed['social_context_seed']}.",
        "timeline": [
            {"scene_number": card["scene_number"], "time_of_day": card["time_of_day"], "location": card["location"]}
            for card in scene_cards
        ],
        "locations": sorted({card["location"] for card in scene_cards}),
        "geography_or_spatial_logic": parsed["location_logic_seed"],
        "culture_or_social_context": parsed["social_context_seed"],
        "world_rules": [
            parsed["world_rule_seed"],
            f"{parsed['stakes']} must stay present in every major choice",
            "repair must be shown through action, not speechmaking",
        ],
        "power_dynamics": parsed["power_dynamics_seed"],
        "consequences": [
            "If anger rules, the room becomes unsafe.",
            "If restraint holds, the room can be repaired.",
        ],
        "consequence_chain": [
            f"pressure trigger threatens {parsed['stakes']}",
            f"internal anger activates {parsed['flaw_seed']}",
            "visible restraint interrupts escalation",
            f"self-awareness reframes the consequence around {parsed['stakes']}",
            "repair restores trust through action",
        ],
        "continuity_across_scenes": [
            {
                "scene_number": card["scene_number"],
                "location": card["location"],
                "pressure_state": card["emotional_value_start"],
                "repair_state": card["emotional_value_end"],
                "world_rule_in_play": parsed["world_rule_seed"],
            }
            for card in scene_cards
        ],
    }
