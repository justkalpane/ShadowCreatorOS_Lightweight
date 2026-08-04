"""Cinematography and composition plan engine."""

from __future__ import annotations

from typing import Any


def generate_cinematography_plan(parsed: dict[str, Any], scene_cards: list[dict[str, Any]]) -> dict[str, Any]:
    genre = parsed["genre"]
    if genre == "thriller":
        shot_types = ["nervous medium", "threat close-up", "containment wide"]
        close_up_grammar = "close-ups isolate fear when the protagonist suppresses panic"
        wide_shot_grammar = "wides expose vulnerable exits, children, and pressure geometry"
        lens_intent = "slightly compressed naturalistic lensing to hold pressure tight"
        camera_motion = "movement advances only when threat perception changes"
        lighting = "cool practicals with pockets of shadow"
        color = "cooled neutrals against danger accents"
        rhythm = "shorter observational beats that tighten toward the midpoint reversal"
    elif genre == "romance":
        shot_types = ["hesitant two-shot", "intimate close-up", "repair wide"]
        close_up_grammar = "close-ups are reserved for withheld tenderness and confession"
        wide_shot_grammar = "wides track emotional distance before reunion"
        lens_intent = "gentle normal-lens intimacy with shallow focus for vulnerability"
        camera_motion = "movement favors emotional approach over action urgency"
        lighting = "soft evening warmth with delicate practical falloff"
        color = "muted warm palette with pockets of tenderness"
        rhythm = "breathing room around eye-lines and pauses"
    else:
        shot_types = ["observational wide", "restrained close-up", "repair two-shot"]
        close_up_grammar = "close-ups are used when emotion is contained rather than spoken"
        wide_shot_grammar = "wide shots show family geography and child vulnerability"
        lens_intent = "naturalistic normal lens language; no spectacle lensing"
        camera_motion = "movement follows emotional repair, not action energy"
        lighting = "soft evening amber with restrained shadows"
        color = "warm domestic tones against pressure shadows"
        rhythm = "held frames during anger, softer movement during repair"
    return {
        "shot_types": shot_types,
        "close_up_grammar": close_up_grammar,
        "wide_shot_grammar": wide_shot_grammar,
        "rule_of_thirds": "caregiver and children share balanced frame weight",
        "symmetry": "symmetry appears only in the repaired closing image",
        "negative_space": "negative space isolates the protagonist during restraint",
        "foreground_background_layering": "children remain foreground stakes while adults manage background pressure",
        "lens_intent": lens_intent,
        "camera_movement_motivation": camera_motion,
        "lighting_mood": lighting,
        "color_contrast": color,
        "visual_rhythm": rhythm,
        "shot_progression": [
            {
                "scene_number": card["scene_number"],
                "shot_intent": card["visual_motif"],
                "shot_type": shot_types[min(index, len(shot_types) - 1)],
                "lens_reason": lens_intent,
                "camera_reason": parsed["camera_reason_seed"],
            }
            for index, card in enumerate(scene_cards)
        ],
    }
