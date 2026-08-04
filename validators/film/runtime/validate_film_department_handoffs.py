from __future__ import annotations

from tools.film_runtime.preproduction.department_handoff_engine import DEPARTMENTS
from validators.film.runtime.preproduction_validator_utils import packet, result


REQUIRED_FIELDS = [
    "department_name",
    "owner_director",
    "purpose",
    "required_inputs",
    "required_outputs",
    "handoff_to",
    "validator_required",
    "blocking_failure_conditions",
    "artifact_dependency",
    "route_boundary",
]


def validate(payload: dict) -> dict:
    handoffs = packet(payload).get("department_handoffs") or {}
    errors = [f"missing_department:{name}" for name in DEPARTMENTS if name not in handoffs]
    expected_next = {name: DEPARTMENTS[index + 1] if index < len(DEPARTMENTS) - 1 else "MEDIA_FACTORY_HANDOFF" for index, name in enumerate(DEPARTMENTS)}
    for name in DEPARTMENTS:
        item = handoffs.get(name)
        if not isinstance(item, dict):
            continue
        for field in REQUIRED_FIELDS:
            if field not in item or item.get(field) in ({}, [], "", None):
                errors.append(f"{name} missing {field}")
        if item.get("department_name") != name:
            errors.append(f"{name} department_name mismatch")
        if item.get("handoff_to") != expected_next[name]:
            errors.append("handoff_chain_broken")
        if not str(item.get("owner_director", "")).strip():
            errors.append("missing_department_owner")
        if name != "packaging_distribution" and item.get("handoff_to") == "MEDIA_FACTORY_HANDOFF":
            errors.append(f"{name} cannot hand off directly to MEDIA_FACTORY_HANDOFF")
    return result("validate_film_department_handoffs", not errors, errors)
