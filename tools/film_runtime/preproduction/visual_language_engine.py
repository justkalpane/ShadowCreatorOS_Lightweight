"""Visual language engine for script-only cinema planning."""

from __future__ import annotations

from typing import Any


def generate_visual_language(parsed: dict[str, Any], director_vision: dict[str, Any]) -> dict[str, Any]:
    return {
        "visual_grammar": director_vision["visual_grammar"],
        "staging": director_vision["staging"],
        "blocking": director_vision["blocking"],
        "scene_intention": director_vision["scene_intention"],
        "emotional_framing": director_vision["emotional_framing"],
        "camera_motivation": director_vision["camera_motivation"],
        "reveal_design": director_vision["reveal_design"],
        "silence_design": director_vision["silence_design"],
        "visual_metaphor": director_vision["visual_metaphor"],
        "frame_power_dynamics": director_vision["frame_power_dynamics"],
        "scene_visual_mapping": [
            {
                "scene_number": item["scene_number"],
                "visual_strategy": f"{director_vision['visual_grammar']} with {director_vision['frame_power_dynamics']}",
                "blocking_reason": director_vision["blocking"],
            }
            for item in director_vision.get("scene_direction_map", [])
        ],
    }
