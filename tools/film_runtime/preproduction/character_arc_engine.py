"""Character arc engine for film preproduction."""

from __future__ import annotations

from typing import Any


def generate_character_arc(parsed: dict[str, Any], character_bible: dict[str, Any], beat_sheet: list[dict[str, Any]]) -> dict[str, Any]:
    main = character_bible["major_characters"][0]
    genre = parsed["genre"]
    scene_numbers = sorted({beat["scene_number"] for beat in beat_sheet})
    midpoint_lookup = {
        "motivational_drama": "self-aware enough to interrupt anger",
        "thriller": "strategic enough to stop panic from becoming danger",
        "romance": "vulnerable enough to tell the truth instead of protecting pride",
    }
    ending_lookup = {
        "motivational_drama": "able to repair through tenderness",
        "thriller": "able to restore safety through calm precision",
        "romance": "able to repair intimacy through honest tenderness",
    }
    statement_lookup = {
        "motivational_drama": "The protagonist changes from contained anger to chosen repair.",
        "thriller": "The protagonist changes from panic-threatened control to calm protective action.",
        "romance": "The protagonist changes from guarded pride to vulnerable relational repair.",
    }
    return {
        "protagonist": main["name"],
        "want": parsed["want"],
        "need": parsed["need"],
        "external_goal": main["external_goal"],
        "internal_need": main["internal_need"],
        "flaw": main["flaw"],
        "wound": main["wound"],
        "contradiction": main["contradiction"],
        "moral_dilemma": parsed["moral_axis"],
        "opposing_force": parsed["opposing_force"],
        "arc_start": main["arc_start"],
        "arc_turning_points": [
            beat["beat_id"] for beat in beat_sheet if beat["beat_id"] in {"pressure_trigger", "visible_restraint", "self_awareness", "repair_choice", "midpoint_reversal"}
        ],
        "arc_end": main["arc_end"],
        "transformation_start": "suppressed and pressure-loaded",
        "transformation_midpoint": midpoint_lookup.get(genre, "self-aware enough to interrupt the old pattern"),
        "transformation_end": ending_lookup.get(genre, "able to repair through a changed action"),
        "relationship_pressure": parsed["relationship_pressure"],
        "emotional_continuity_by_scene": [
            {
                "scene_number": number,
                "emotional_state": next(beat["emotional_state_after"] for beat in beat_sheet if beat["scene_number"] == number),
            }
            for number in scene_numbers
        ],
        "behavioral_consistency_rules": [
            "main character stays soft-spoken",
            "main character does not shout",
            "main character does not become violent",
            "repair must occur through action",
        ],
        "transformation_statement": statement_lookup.get(genre, "The protagonist changes through consequence and repair."),
    }
