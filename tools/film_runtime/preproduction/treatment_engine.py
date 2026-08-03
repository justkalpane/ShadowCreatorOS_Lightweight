"""Deterministic treatment builder for film screenplay preproduction."""

from __future__ import annotations

from typing import Any


def generate_treatment(parsed: dict[str, Any], characters: dict[str, Any]) -> dict[str, Any]:
    main = characters["main"]
    second = characters["second"]
    premise_axis = {
        "motivational_drama": "restraint before harm",
        "thriller": "clarity before panic",
        "romance": "vulnerability before distance",
    }.get(parsed["genre"], "truth before avoidance")

    return {
        "treatment_title": f"{main['name']} and the Choice Inside {parsed['setting'].title()}",
        "central_premise": (
            f"In {parsed['setting']}, {main['name']} must protect {parsed['stakes']} when "
            f"{parsed['pressure_trigger']} tests the hidden fault line between {main['role']} and {premise_axis}."
        ),
        "emotional_promise": f"A {parsed['genre'].replace('_', ' ')} built around {premise_axis}.",
        "protagonist_external_goal": parsed["external_goal"],
        "protagonist_internal_need": parsed["internal_need"],
        "central_conflict": (
            f"{main['name']}'s need to protect {parsed['stakes']} collides with {parsed['opposing_force']} "
            f"while {second['name']} mirrors the emotional cost of the moment."
        ),
        "stakes": parsed["stakes"],
        "turning_points": [
            parsed["opening_image_seed"],
            f"The pressure trigger turns {parsed['want']} into a live test.",
            f"A midpoint shift forces {main['name']} to face {parsed['moral_axis']}.",
            parsed["ending_image"],
        ],
        "ending_image": parsed["ending_image"],
    }
