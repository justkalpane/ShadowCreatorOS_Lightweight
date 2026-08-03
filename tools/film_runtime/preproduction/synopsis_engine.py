"""Synopsis builder for the film screenplay preproduction packet."""

from __future__ import annotations

from typing import Any


def generate_synopsis(parsed: dict[str, Any], treatment: dict[str, Any], characters: dict[str, Any]) -> dict[str, Any]:
    main = characters["main"]["name"]
    second = characters["second"]["name"]
    genre_label = parsed["genre"].replace("_", " ")

    return {
        "one_sentence_synopsis": f"In this {genre_label}, {main} must face {parsed['pressure_trigger']} before it can cost {parsed['stakes']}.",
        "short_synopsis": (
            f"{main} moves through {parsed['setting']} carrying {parsed['wound_seed']}. "
            f"When {parsed['pressure_trigger']} threatens {parsed['stakes']}, {second} quietly mirrors what is at stake and forces a choice."
        ),
        "expanded_synopsis": (
            f"The film opens inside {parsed['setting']}, where the emotional weather is already unstable. "
            f"{parsed['pressure_trigger'].capitalize()} pushes {main} toward {parsed['flaw_seed']}. "
            f"Instead of repeating that pattern, {main} is forced through a midpoint of self-recognition and returns with a choice that changes the room. "
            f"The ending fulfills the treatment promise: {treatment['ending_image']}"
        ),
        "beginning_middle_end_summary": {
            "beginning": f"{main} enters {parsed['setting']} carrying a private weakness that can endanger {parsed['stakes']}.",
            "middle": f"{parsed['pressure_trigger'].capitalize()} forces a confrontation between {parsed['want']} and {parsed['need']}.",
            "ending": f"{main} chooses a final action that redefines the relationship with {second}.",
        },
    }
