from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import result


def validate(payload: dict) -> dict:
    original = payload.get("original_quality_score") or {}
    revised = payload.get("revised_quality_score") or {}
    validator_results = payload.get("validator_results") or {}
    delta = payload.get("revision_delta_report") or {}
    packet = payload.get("revised_preproduction_packet") or {}
    errors = []
    if revised.get("overall_score", 0) <= original.get("overall_score", 10):
        errors.append("revised score must be higher than original score")
    if len(revised.get("defect_list", [])) >= len(original.get("defect_list", [])):
        errors.append("top defects were not reduced")
    if packet.get("mode") != "script_only" or packet.get("route") != "FILM_SCREENPLAY_GENERATION":
        errors.append("route preservation failed on revised packet")
    boundary = packet.get("downstream_adapter_boundary") or {}
    if boundary.get("media_provider_triggered") is not False or boundary.get("paid_api_triggered") is not False:
        errors.append("revised packet triggered provider/media boundary")
    failing = [name for name, report in validator_results.items() if report.get("passed") is not True]
    if failing:
        errors.append("revised packet failed existing validators: " + ", ".join(sorted(failing)))
    if delta.get("revised_not_identical") is not True:
        errors.append("revision delta does not prove material change")
    return result("validate_film_revised_packet_improvement", not errors, errors)

