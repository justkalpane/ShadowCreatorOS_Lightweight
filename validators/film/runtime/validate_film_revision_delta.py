from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import result


REQUIRED_FIELDS = {
    "premise",
    "logline",
    "character_arc",
    "opposing_force",
    "relationship_map",
    "midpoint",
    "visual_motivation",
    "cinematography_plan",
}


def validate(payload: dict) -> dict:
    report = payload.get("revision_delta_report") or {}
    changed = report.get("changed_fields") or {}
    errors = [f"missing changed field: {field}" for field in sorted(REQUIRED_FIELDS - set(changed))]
    if report.get("meaningful_story_change") is not True:
        errors.append("meaningful story change must be true")
    if report.get("revised_not_identical") is not True:
        errors.append("revised packet must not be identical to original")
    changed_count = 0
    for field in REQUIRED_FIELDS & set(changed):
        before = changed[field].get("before")
        after = changed[field].get("after")
        if before != after:
            changed_count += 1
    if changed_count < 5:
        errors.append("fewer than 5 meaningful story fields changed")
    return result("validate_film_revision_delta", not errors, errors)
