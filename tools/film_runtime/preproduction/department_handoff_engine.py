"""Department handoff engine for production-house planning."""

from __future__ import annotations

from typing import Any


DEPARTMENTS = [
    "development",
    "writing_room",
    "story",
    "character",
    "direction",
    "cinematography",
    "art",
    "costume",
    "sound_planning",
    "continuity",
    "production_management",
    "validation_audit",
    "packaging_distribution",
]

DEPARTMENT_OWNERS = {
    "development": "krishna",
    "writing_room": "saraswati",
    "story": "vyasa",
    "character": "krishna",
    "direction": "indra",
    "cinematography": "arjuna",
    "art": "vishvakarma",
    "costume": "lakshmi",
    "sound_planning": "nataraja",
    "continuity": "ganesha",
    "production_management": "hanuman",
    "validation_audit": "garuda",
    "packaging_distribution": "varuna",
}


def generate_department_handoffs(parsed: dict[str, Any]) -> dict[str, Any]:
    handoffs: dict[str, Any] = {}
    purpose_map = {
        "development": "lock the concept, route boundary, and genre mandate",
        "writing_room": "translate premise into playable narrative language",
        "story": "enforce beat, act, and sequence causality",
        "character": "carry want/need/wound/relationship pressure into all scenes",
        "direction": "set emotional framing and scene intention",
        "cinematography": "bind camera, lens, and spatial logic to scene pressure",
        "art": "support location logic and motif continuity",
        "costume": "support character pressure and status readability",
        "sound_planning": "prepare silence, atmosphere, and pressure cues",
        "continuity": "keep timeline, state, and object continuity coherent",
        "production_management": "track feasibility, dependencies, and blockers",
        "validation_audit": "gate false pass claims and boundary violations",
        "packaging_distribution": "prepare a future downstream handoff without activating it",
    }
    artifact_dependency = {
        "development": "concept_note.md",
        "writing_room": "treatment.md",
        "story": "beat_sheet.json",
        "character": "character_bible.json",
        "direction": "director_vision.json",
        "cinematography": "cinematography_plan.json",
        "art": "world_bible.json",
        "costume": "character_bible.json",
        "sound_planning": "continuity_bible.json",
        "continuity": "scene_cards.json",
        "production_management": "production_risk_sheet.json",
        "validation_audit": "validation_report.json",
        "packaging_distribution": "revision_report.json",
    }
    for department in DEPARTMENTS:
        next_handoff = "MEDIA_FACTORY_HANDOFF" if department == "packaging_distribution" else DEPARTMENTS[DEPARTMENTS.index(department) + 1]
        handoffs[department] = {
            "department_name": department,
            "owner_director": DEPARTMENT_OWNERS[department],
            "purpose": purpose_map[department],
            "required_inputs": ["film_intent_lock", artifact_dependency[department]],
            "required_outputs": [f"{department}_handoff_notes", f"{department}_approval_ready"],
            "handoff_to": next_handoff,
            "validator_required": f"validate_film_department_handoffs::{department}",
            "blocking_failure_conditions": [
                "required packet missing",
                "route boundary violated",
                "department owner absent",
            ],
            "artifact_dependency": artifact_dependency[department],
            "route_boundary": "FILM_SCREENPLAY_GENERATION owns preproduction only; MEDIA_FACTORY_HANDOFF remains downstream only",
        }
    return handoffs
