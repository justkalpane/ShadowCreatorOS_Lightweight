"""Validate continuity tracking depth."""

from __future__ import annotations

from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet


def validate(payload):
    packet = load_screenplay_packet(payload)
    depth = (packet.get("cinema_depth_packet") or {}).get("continuity_depth") or {}
    errors = []
    if len(depth.get("setup_payoff_tracker") or []) < 3:
        errors.append("continuity tracking is too shallow")
    if not any(item.get("remembers_prior_turn") for item in depth.get("decision_memory") or [][1:]):
        errors.append("later scenes do not remember prior turns")
    errors.extend(depth.get("unresolved_thread_flags") or [])
    return {"validator": "validate_continuity_tracking", "passed": not errors, "status": "VALIDATION_PASSED" if not errors else "VALIDATION_FAILED", "errors": errors}
