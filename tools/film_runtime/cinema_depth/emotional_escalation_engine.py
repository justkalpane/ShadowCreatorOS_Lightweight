"""Cinema-depth emotional escalation analysis."""

from __future__ import annotations

from typing import Any


def _act_label(scene_number: int, total_scenes: int) -> str:
    if total_scenes <= 3:
        return "act_one" if scene_number == 1 else "act_two" if scene_number == 2 else "act_three"
    first_cut = max(1, total_scenes // 3)
    second_cut = max(first_cut + 1, (2 * total_scenes) // 3)
    if scene_number <= first_cut:
        return "act_one"
    if scene_number <= second_cut:
        return "act_two"
    return "act_three"


def build_emotional_escalation_packet(
    beat_sheet: list[dict[str, Any]],
    scene_cards: list[dict[str, Any]],
) -> dict[str, Any]:
    total_scenes = max((card.get("scene_number", 0) for card in scene_cards), default=0)
    scene_emotional_state: list[dict[str, Any]] = []
    emotional_turning_points: list[dict[str, Any]] = []
    flatline_risk_flags: list[str] = []
    progression_by_act: dict[str, list[str]] = {"act_one": [], "act_two": [], "act_three": []}

    previous_after = None
    repeated_count = 0
    for beat in beat_sheet:
        after = str(beat.get("emotional_state_after", "")).strip().lower()
        before = str(beat.get("emotional_state_before", "")).strip().lower()
        scene_number = int(beat.get("scene_number", 0))
        act = _act_label(scene_number, total_scenes or len(beat_sheet))
        scene_emotional_state.append(
            {
                "scene_number": scene_number,
                "act": act,
                "beat_id": beat.get("beat_id"),
                "before": before,
                "after": after,
                "decision_link": beat.get("character_action", ""),
            }
        )
        progression_by_act.setdefault(act, []).append(after)
        if previous_after == after and after:
            repeated_count += 1
        else:
            repeated_count = 0
        if repeated_count >= 2:
            flatline_risk_flags.append(
                f"emotional repetition risk by scene {scene_number}: repeated state {after}"
            )
        if before and after and before != after:
            emotional_turning_points.append(
                {
                    "scene_number": scene_number,
                    "beat_id": beat.get("beat_id"),
                    "before": before,
                    "after": after,
                    "turn_type": "reversal" if "not" in after or "but" in beat.get("story_function", "").lower() else "progression",
                }
            )
        previous_after = after

    act_emotional_progression = {
        act: {
            "states": states,
            "distinct_state_count": len({state for state in states if state}),
            "flatline": len({state for state in states if state}) <= 1 and len(states) > 1,
        }
        for act, states in progression_by_act.items()
    }
    for act, details in act_emotional_progression.items():
        if details["flatline"]:
            flatline_risk_flags.append(f"{act} emotional progression is flat")

    return {
        "emotional_arc_map": scene_emotional_state,
        "scene_emotional_state": scene_emotional_state,
        "act_emotional_progression": act_emotional_progression,
        "emotional_turning_points": emotional_turning_points,
        "flatline_risk_flags": flatline_risk_flags,
    }
