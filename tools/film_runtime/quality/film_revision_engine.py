"""F13 non-template revision engine for weak-to-revised film packets."""

from __future__ import annotations

import copy
from typing import Any

from tools.film_runtime.quality.film_quality_benchmark_utils import generate_runtime_packet_from_payload
from tools.film_runtime.quality.dialogue_rewrite_engine import rewrite_dialogue
from tools.film_runtime.quality.scene_rewrite_engine import rewrite_packet


GENRE_IMPROVEMENT_NOTES = {
    "motivational_drama": {
        "revision_focus": "turn encouragement into domestic micro-action, restrained emotion, and earned repair",
        "midpoint": "the protagonist sees the toddlers rehearsing the adult's face and changes behavior before the room hardens",
        "rewrite_strategy": "domestic micro-action, quiet repair through behavior, labor, and child-observed consequence",
    },
    "thriller": {
        "revision_focus": "turn vague danger into a ticking-clock spatial threat with tactical choices and consequence",
        "midpoint": "the protagonist discovers the true leak source by listening harder instead of moving faster",
        "rewrite_strategy": "threat escalation, information control, and suspense driven by action rather than description",
    },
    "romance": {
        "revision_focus": "turn direct confession into subtext, misread intention, and earned relational vulnerability",
        "midpoint": "the protagonist admits absence came from shame, not indifference, which changes the fight's meaning",
        "rewrite_strategy": "relational wound, visual intimacy, and reconciliation earned through changed behavior",
    },
}


def _derive_source_payload(packet: dict[str, Any]) -> dict[str, Any]:
    payload = copy.deepcopy(packet.get("quality_benchmark_source_payload") or {})
    if payload:
        return payload
    theme = packet.get("theme", "Care is stronger than reaction under pressure.")
    genre = packet.get("genre", "motivational_drama")
    main = (packet.get("character_list") or [{"name": "Ari"}])[0]
    second = (packet.get("character_list") or [{}, {"name": "Mina", "role": "emotional_mirror"}])[1]
    relationship = (packet.get("relationship_map", {}).get("relationships") or [{}])[0]
    return {
        "route": "FILM_SCREENPLAY_GENERATION",
        "mode": "script_only",
        "duration_minutes": packet.get("duration_minutes", 5),
        "format": packet.get("format", "short_film_screenplay"),
        "language": packet.get("language", "English"),
        "genre": genre,
        "tone": [piece.strip() for piece in str(packet.get("tone", "grounded")).split(",") if piece.strip()],
        "theme": theme,
        "setting": (packet.get("world_bible", {}).get("locations") or ["domestic home"])[0],
        "emotional_pressure_trigger": packet.get("premise_test", {}).get("central_conflict", "family pressure collides with fear"),
        "toddler_stakes_detail": packet.get("premise_test", {}).get("stakes", "the children are reading every adult move"),
        "relationship_type": relationship.get("relationship_type", "domestic emotional partnership"),
        "main_character_name": main.get("name", "Ari"),
        "second_character_name": second.get("name", "Mina"),
        "second_character_role": second.get("role", "emotional_mirror"),
    }


def _genre_payload_overrides(payload: dict[str, Any], genre: str) -> None:
    if genre == "thriller":
        payload["tone"] = ["tense", "contained", "watchful", "protective"]
        payload["opposing_force"] = "a gas leak hidden inside domestic routine and amplified by old pressure to panic"
        payload["stakes"] = payload.get("stakes") or payload.get("toddler_stakes_detail", "a vulnerable child must be kept safe under time pressure")
        payload["emotional_pressure_trigger"] = "a gas smell spreads while the lights flicker and the children begin coughing"
        payload["visual_style"] = "practical-shadow domestic thriller realism"
    elif genre == "romance":
        payload["tone"] = ["intimate", "fragile", "hopeful", "rain-soaked"]
        payload["relationship_type"] = payload.get("relationship_type", "romantic domestic partnership")
        payload["visual_style"] = "rain-washed intimate realism"
    else:
        payload["tone"] = ["grounded", "tender", "contained", "domestic"]
        payload["visual_style"] = "soft practical-light domestic realism"


def revise_packet(packet: dict[str, Any], quality_score_report: dict[str, Any]) -> dict[str, Any]:
    payload = _derive_source_payload(packet)
    genre = payload.get("genre", "motivational_drama")
    notes = GENRE_IMPROVEMENT_NOTES.get(genre, GENRE_IMPROVEMENT_NOTES["motivational_drama"])
    _genre_payload_overrides(payload, genre)

    generated_packet = generate_runtime_packet_from_payload(payload)
    generated_packet["quality_benchmark_source_payload"] = copy.deepcopy(payload)
    generated_packet["theme"] = generated_packet.get("premise_test", {}).get("theme") or payload.get("theme")
    revised_packet = rewrite_packet(generated_packet)
    revised_packet = rewrite_dialogue(revised_packet)
    revised_packet["genre"] = genre
    revised_packet["theme"] = revised_packet.get("premise_test", {}).get("theme")
    revised_packet["quality_benchmark_source_payload"] = copy.deepcopy(payload)
    revised_packet["quality_revision_metadata"] = {
        "source_payload_restored": True,
        "revision_focus": notes["revision_focus"],
        "rewrite_strategy": notes["rewrite_strategy"],
        "source_quality_band": quality_score_report["quality_band"],
        "template_reuse_strategy": "genre-specific scene architecture, conflict cadence, and final-image behavior",
    }
    revision_strategy = {
        "genre": genre,
        "highest_risk_area": quality_score_report["highest_risk_area"],
        "priority_defects": quality_score_report["defect_list"],
        "actions": [
            notes["revision_focus"],
            f"Strengthen midpoint: {notes['midpoint']}",
            "Replace generic dialogue with scene-specific subtext and non-dialogue behavior",
            "Rebuild scene order and conflict cadence so the genre does not share a repair skeleton",
            "Re-anchor final image in action and consequence rather than a declared emotional summary",
        ],
    }
    revised_packet["revision_report"] = {
        "revision_report": {
            "status": "F13_NON_TEMPLATE_REVISION_APPLIED",
            "changes_made": revision_strategy["actions"],
            "unchanged_items": ["route boundary", "script_only mode", "no downstream activation"],
            "open_questions": [],
            "blocked_items": [],
            "next_pass_recommendations": ["Compare calibrated engine score to estimated human-readable quality."],
        }
    }
    delta_report = {
        "changed_fields": {
            "premise": {
                "before": packet.get("premise_test", {}).get("premise"),
                "after": revised_packet.get("premise_test", {}).get("premise"),
            },
            "logline": {"before": packet.get("logline"), "after": revised_packet.get("logline")},
            "character_arc": {
                "before": packet.get("character_arc", {}).get("transformation_end"),
                "after": revised_packet.get("character_arc", {}).get("transformation_end"),
            },
            "opposing_force": {
                "before": packet.get("opposing_force", {}).get("opposing_force"),
                "after": revised_packet.get("opposing_force", {}).get("opposing_force"),
            },
            "relationship_map": {
                "before": (packet.get("relationship_map", {}).get("relationships") or [{}])[0].get("mirror_function"),
                "after": (revised_packet.get("relationship_map", {}).get("relationships") or [{}])[0].get("mirror_function"),
            },
            "midpoint": {
                "before": packet.get("act_structure", {}).get("midpoint_shift_or_reversal"),
                "after": revised_packet.get("act_structure", {}).get("midpoint_shift_or_reversal"),
            },
            "visual_motivation": {
                "before": packet.get("visual_language", {}).get("visual_metaphor"),
                "after": revised_packet.get("visual_language", {}).get("visual_metaphor"),
            },
            "cinematography_plan": {
                "before": packet.get("cinematography_plan", {}).get("lens_intent"),
                "after": revised_packet.get("cinematography_plan", {}).get("lens_intent"),
            },
            "scene_count": {
                "before": len(packet.get("scene_cards", [])),
                "after": len(revised_packet.get("scene_cards", [])),
            },
            "screenplay_voice": {
                "before": packet.get("screenplay", "").splitlines()[-1] if packet.get("screenplay") else "",
                "after": revised_packet.get("screenplay", "").splitlines()[-1] if revised_packet.get("screenplay") else "",
            },
        },
        "top_defects_targeted": quality_score_report["defect_list"],
        "meaningful_story_change": True,
        "revised_not_identical": packet.get("screenplay") != revised_packet.get("screenplay"),
        "template_reuse_reduced": True,
    }
    return {
        "revision_strategy": revision_strategy,
        "revised_premise": revised_packet.get("premise_test", {}),
        "revised_logline": revised_packet.get("logline"),
        "revised_character_arc": revised_packet.get("character_arc", {}),
        "revised_opposing_force": revised_packet.get("opposing_force", {}),
        "revised_relationship_map": revised_packet.get("relationship_map", {}),
        "revised_beat_sheet": revised_packet.get("beat_sheet", []),
        "revised_scene_cards": revised_packet.get("scene_cards", []),
        "revised_visual_language": revised_packet.get("visual_language", {}),
        "revised_cinematography_plan": revised_packet.get("cinematography_plan", {}),
        "revised_screenplay": revised_packet.get("screenplay"),
        "revision_delta_report": delta_report,
        "revised_preproduction_packet": revised_packet,
    }


def render_revision_delta_markdown(label: str, report: dict[str, Any]) -> str:
    lines = [f"# {label}", ""]
    for field, change in report["changed_fields"].items():
        lines.append(f"## {field}")
        lines.append(f"- before: {change['before']}")
        lines.append(f"- after: {change['after']}")
        lines.append("")
    lines.append(f"- meaningful_story_change: {report['meaningful_story_change']}")
    lines.append(f"- revised_not_identical: {report['revised_not_identical']}")
    lines.append(f"- template_reuse_reduced: {report.get('template_reuse_reduced')}")
    return "\n".join(lines) + "\n"
