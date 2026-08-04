"""Validate dialogue voice differentiation and subtext."""

from __future__ import annotations

from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet


def validate(payload):
    packet = load_screenplay_packet(payload)
    depth = (packet.get("cinema_depth_packet") or {}).get("dialogue_depth") or {}
    errors = []
    fingerprints = depth.get("character_voice_fingerprints") or {}
    if len(fingerprints) < 2:
        errors.append("need at least two distinct dialogue voices")
    if len(depth.get("subtext_map") or []) < 2:
        errors.append("key scenes lack subtextual dialogue moments")
    errors.extend(depth.get("same_voice_risk_flags") or [])
    errors.extend(depth.get("generic_dialogue_flags") or [])
    if len(depth.get("exposition_dump_flags") or []) >= 2:
        errors.append("dialogue contains exposition-dump behavior")
    return {"validator": "validate_dialogue_voice_subtext", "passed": not errors, "status": "VALIDATION_PASSED" if not errors else "VALIDATION_FAILED", "errors": errors}
