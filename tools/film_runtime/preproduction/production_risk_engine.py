"""Production risk sheet generator for film preproduction."""

from __future__ import annotations

from typing import Any


def generate_production_risk_sheet(parsed: dict[str, Any], world_bible: dict[str, Any]) -> dict[str, Any]:
    return {
        "production_risk_sheet": [
            {
                "risk": "dialogue becomes generic motivational speech",
                "severity": "high",
                "owner": "writing_room",
                "packet_area": "dialogue_subtext",
                "mitigation": "dialogue_subtext validator and relationship mirror function",
            },
            {
                "risk": "content route drift into platform hook or retention logic",
                "severity": "critical",
                "owner": "validation_audit",
                "packet_area": "route_boundary",
                "mitigation": "clean film/script boundary validator keeps platform optimization outside film-core authority",
            },
            {
                "risk": "world logic is too thin for domestic drama",
                "severity": "medium",
                "owner": "story",
                "packet_area": "world_bible",
                "mitigation": "compact domestic world bible with consequence chain",
            },
        ],
        "open_questions": ["Should later phases add genre-specific template variants beyond motivational_drama?"],
        "blocked_items": [],
        "next_pass_recommendations": ["Add deeper genre-specific craft validators before claiming production-grade completeness."],
        "world_context_checked": bool(world_bible.get("domestic_world_context")),
    }
