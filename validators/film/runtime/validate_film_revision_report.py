from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, require_fields, result


def validate(payload: dict) -> dict:
    revision = packet(payload).get("revision_report") or {}
    if "revision_report" in revision and isinstance(revision["revision_report"], dict):
        revision = revision["revision_report"]
    errors = require_fields(revision, ["status", "changes_made", "unchanged_items", "open_questions", "next_pass_recommendations"])
    if not revision.get("next_pass_recommendations"):
        errors.append("revision_without_next_pass")
    if "blocked_items" not in revision:
        errors.append("blocked_items_missing")
    if not isinstance(revision.get("unchanged_items"), list):
        errors.append("unchanged_items missing")
    return result("validate_film_revision_report", not errors, errors)
