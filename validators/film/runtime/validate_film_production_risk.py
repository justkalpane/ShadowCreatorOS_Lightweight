from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, require_fields, result


def validate(payload: dict) -> dict:
    risk = packet(payload).get("production_risk_sheet") or {}
    errors = require_fields(risk, ["production_risk_sheet", "open_questions", "next_pass_recommendations"])
    if "blocked_items" not in risk:
        errors.append("blocked_items_missing")
    entries = risk.get("production_risk_sheet") or []
    if not isinstance(entries, list) or len(entries) < 3:
        errors.append("empty_risk_sheet")
    for entry in entries:
        for field in ["risk", "severity", "owner", "packet_area", "mitigation"]:
            if field not in entry or entry.get(field) in ({}, [], "", None):
                errors.append(f"risk entry missing {field}")
        if "mitigation" in entry and not str(entry.get("mitigation", "")).strip():
            errors.append("risk_without_mitigation")
    return result("validate_film_production_risk", not errors, errors)
