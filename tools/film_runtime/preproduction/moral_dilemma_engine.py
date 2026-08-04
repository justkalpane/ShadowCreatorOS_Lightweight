"""Moral dilemma generator for film preproduction."""

from __future__ import annotations

from typing import Any


def generate_moral_dilemma(parsed: dict[str, Any], character_arc: dict[str, Any]) -> dict[str, Any]:
    choice_b = {
        "motivational_drama": "Pause, repair, and teach safety.",
        "thriller": "Stay calm, read the threat correctly, and keep the room safe.",
        "romance": "Tell the truth, risk tenderness, and repair the bond.",
    }.get(parsed["genre"], "Choose care over the old reflex.")
    return {
        "moral_dilemma": parsed["moral_axis"],
        "dilemma": f"Will the protagonist {parsed['moral_axis']}?",
        "choice_a": "Protect pride, force, or panic and deepen the damage.",
        "choice_b": choice_b,
        "cost_of_choice_a": f"{parsed['stakes']} becomes more fragile.",
        "cost_of_choice_b": "The protagonist must admit vulnerability.",
        "resolved_by": character_arc["arc_turning_points"][-1],
    }
