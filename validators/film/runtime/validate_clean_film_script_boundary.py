from __future__ import annotations

import json

from validators.film.runtime.preproduction_validator_utils import packet, result


FORBIDDEN_FILM_CORE_TERMS = ["youtube hook", "thumbnail", "retention loop", "shorts", "tiktok", "reels", "ctr", "viral"]


def validate(payload: dict) -> dict:
    data = packet(payload)
    text = json.dumps({"preproduction_packet": data, "route_state": data.get("route_state")}).lower()
    errors = []
    if data.get("mode") != "script_only":
        errors.append("mode must remain script_only")
    if data.get("route") != "FILM_SCREENPLAY_GENERATION":
        errors.append("route must remain FILM_SCREENPLAY_GENERATION")
    for term in FORBIDDEN_FILM_CORE_TERMS:
        if term in text:
            errors.append(f"film route imports content/platform term: {term}")
    boundary = data.get("downstream_adapter_boundary") or {}
    if boundary.get("downstream_execution_triggered") is not False:
        errors.append("film route cannot trigger downstream execution in script_only mode")
    if boundary.get("media_provider_triggered") is not False:
        errors.append("film route cannot trigger media providers in script_only mode")
    if data.get("route_state", {}).get("mode") != "script_only":
        errors.append("route_state.mode must remain script_only")
    return result("validate_clean_film_script_boundary", not errors, errors)
