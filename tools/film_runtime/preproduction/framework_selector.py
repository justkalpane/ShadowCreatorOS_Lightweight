"""Selects local cinema craft frameworks without external calls."""

from __future__ import annotations

from typing import Any


def select_frameworks(parsed: dict[str, Any], registries_loaded: dict[str, bool]) -> dict[str, Any]:
    genre = parsed.get("genre", "motivational_drama")
    frameworks = ["objective_conflict_turn", "want_need_flaw_arc", "grounded_domestic_drama"]
    if genre == "motivational_drama":
        frameworks.extend(["visible_restraint_arc", "earned_hope_resolution"])
    return {
        "selected_genre": genre,
        "frameworks": frameworks,
        "selection_reason": "local deterministic selection based on genre and script-only film route",
        "registries_loaded": registries_loaded,
        "paid_api_required": False,
    }
