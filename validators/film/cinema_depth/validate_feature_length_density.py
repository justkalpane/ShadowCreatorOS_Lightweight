"""Validate feature-length density depth."""

from __future__ import annotations

from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet


def validate(payload):
    packet = load_screenplay_packet(payload)
    depth = (packet.get("cinema_depth_packet") or {}).get("feature_density") or {}
    errors = []
    if packet.get("format_family") == "feature_film":
        if depth.get("actual_scene_count", 0) < 12:
            errors.append("feature packet must include at least 12 macro scenes")
        if depth.get("actual_sub_scene_count", 0) < 36:
            errors.append("feature packet must include at least 36 sub-scenes")
        if depth.get("sequence_density_score", 0) <= 1:
            errors.append("feature sequence density too low")
    errors.extend(depth.get("feature_thinness_flags") or [])
    return {"validator": "validate_feature_length_density", "passed": not errors, "status": "VALIDATION_PASSED" if not errors else "VALIDATION_FAILED", "errors": errors}
