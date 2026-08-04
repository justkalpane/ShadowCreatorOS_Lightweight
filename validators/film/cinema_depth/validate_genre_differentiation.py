"""Validate genre differentiation depth."""

from __future__ import annotations

from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet


def validate(payload):
    packet = load_screenplay_packet(payload)
    depth = (packet.get("cinema_depth_packet") or {}).get("genre_depth") or {}
    errors = []
    if len(depth.get("genre_required_turns") or []) < 3:
        errors.append("genre depth requires explicit genre turns")
    profile = depth.get("genre_pacing_profile") or {}
    if profile.get("turn_density", 0) < 0.8:
        errors.append("genre pacing turn density too low")
    errors.extend(depth.get("genre_failure_flags") or [])
    return {"validator": "validate_genre_differentiation", "passed": not errors, "status": "VALIDATION_PASSED" if not errors else "VALIDATION_FAILED", "errors": errors}
