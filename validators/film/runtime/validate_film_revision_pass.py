from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, require_fields, result


def validate(payload: dict) -> dict:
    revision = packet(payload).get("revision_report") or {}
    if "revision_report" in revision and isinstance(revision["revision_report"], dict):
        revision = revision["revision_report"]
    errors = require_fields(revision, ["status", "changes_made", "unchanged_items", "open_questions", "next_pass_recommendations"])
    if "blocked_items" not in revision:
        errors.append("blocked_items_missing")
    if not isinstance(revision.get("changes_made"), list) or len(revision.get("changes_made", [])) < 2:
        errors.append("changes_made must include meaningful revision actions")
    if not isinstance(revision.get("unchanged_items"), list) or "SCRIPT_GENERATION route remains preserved" not in revision.get("unchanged_items", []):
        errors.append("revision must record preserved route boundaries")
    if not isinstance(revision.get("next_pass_recommendations"), list) or not revision.get("next_pass_recommendations"):
        errors.append("revision_without_next_pass")
    return result("validate_film_revision_pass", not errors, errors)
