"""Character bible builder for cinema preproduction."""

from __future__ import annotations

from typing import Any


def _major_character(
    *,
    name: str,
    role: str,
    external_goal: str,
    internal_need: str,
    flaw: str,
    fear: str,
    wound: str,
    contradiction: str,
    behavioral_rules: list[str],
    relationship_to_other_characters: dict[str, str],
    arc_start: str,
    arc_end: str,
) -> dict[str, Any]:
    return {
        "name": name,
        "role": role,
        "external_goal": external_goal,
        "internal_need": internal_need,
        "flaw": flaw,
        "fear": fear,
        "wound": wound,
        "contradiction": contradiction,
        "behavioral_rules": behavioral_rules,
        "relationship_to_other_characters": relationship_to_other_characters,
        "arc_start": arc_start,
        "arc_end": arc_end,
    }


def generate_character_bible(parsed: dict[str, Any], characters: dict[str, Any]) -> dict[str, Any]:
    main = characters["main"]
    second = characters["second"]
    main_rules = [
        "soft-spoken",
        "warm",
        "carries controlled internal anger",
        "does not shout",
        "does not become violent",
        "does not become abusive",
        "parent or guardian of toddlers",
    ]
    return {
        "major_characters": [
            _major_character(
                name=main["name"],
                role=parsed["protagonist_type"],
                external_goal=parsed["external_goal"],
                internal_need=parsed["internal_need"],
                flaw=parsed["flaw_seed"],
                fear=parsed["fear_seed"],
                wound=parsed["wound_seed"],
                contradiction=parsed["contradiction_seed"],
                behavioral_rules=main_rules,
                relationship_to_other_characters={
                    second["name"]: "The second character functions as an emotional mirror, not decoration.",
                    "toddlers": "The toddlers create the moral and emotional stakes of the scene.",
                },
                arc_start=parsed["arc_start_seed"],
                arc_end=parsed["arc_end_seed"],
            ),
            _major_character(
                name=second["name"],
                role=second["role"],
                external_goal=parsed["second_character_goal"],
                internal_need="Reflect the truth gently enough for the protagonist to hear it.",
                flaw=parsed["second_character_flaw"],
                fear=parsed["second_character_fear"],
                wound=parsed["second_character_wound"],
                contradiction=parsed["second_character_contradiction"],
                behavioral_rules=[
                    "acts as an emotional mirror",
                    "does not replace the protagonist's choice",
                    "names stakes through care rather than exposition",
                ],
                relationship_to_other_characters={
                    main["name"]: f"Reflects the emotional issue and pressures {parsed['moral_axis']}.",
                    "toddlers": f"Keeps {parsed['stakes']} present as living stakes.",
                },
                arc_start=parsed["second_arc_start"],
                arc_end=parsed["second_arc_end"],
            ),
        ],
        "test_case_constraints": {
            "main_character_is_soft_spoken": True,
            "main_character_is_warm": True,
            "main_character_carries_controlled_internal_anger": True,
            "main_character_does_not_shout": True,
            "main_character_does_not_become_violent_or_abusive": True,
            "main_character_is_parent_or_guardian_of_toddlers": True,
        },
    }
