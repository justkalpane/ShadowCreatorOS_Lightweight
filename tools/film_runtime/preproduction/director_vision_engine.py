"""Director vision engine for film preproduction."""

from __future__ import annotations

from typing import Any


def generate_director_vision(parsed: dict[str, Any], treatment: dict[str, Any], scene_cards: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "director_note": treatment["emotional_promise"],
        "mood_map": {"opening": parsed["mood_opening"], "middle": parsed["mood_middle"], "ending": parsed["mood_ending"]},
        "visual_grammar": parsed["visual_grammar_seed"],
        "staging": parsed["staging_seed"],
        "blocking": parsed["blocking_seed"],
        "scene_intention": [card["scene_objective"] for card in scene_cards],
        "emotional_framing": parsed["emotional_framing_seed"],
        "camera_motivation": parsed["camera_reason_seed"],
        "reveal_design": parsed["reveal_design_seed"],
        "silence_design": parsed["silence_design_seed"],
        "visual_metaphor": parsed["visual_metaphor_seed"],
        "frame_power_dynamics": parsed["frame_power_dynamics_seed"],
        "scene_direction_map": [
            {"scene_number": card["scene_number"], "objective": card["scene_objective"], "emotion": card["emotional_value_end"]}
            for card in scene_cards
        ],
    }
