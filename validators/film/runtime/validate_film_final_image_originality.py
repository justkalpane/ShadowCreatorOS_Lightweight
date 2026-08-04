from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import result


def validate(payload: dict) -> dict:
    packets = payload.get("packets") or []
    errors = []
    finals = [str(packet.get("final_image_line", "")).lower() for packet in packets]
    if len(finals) < 2:
        errors.append("at least two packets are required")
        return result("validate_film_final_image_originality", False, errors)
    if len(set(finals)) != len(finals):
        errors.append("final images duplicate exactly")
    forbidden = "carry "
    if any("without naming it twice" in line for line in finals):
        errors.append("shared final image cadence remains")
    if all("repair" in line or "quieter" in line for line in finals):
        errors.append("same symbolic closure pattern remains")
    if not any("toy truck" in line for line in finals):
        errors.append("thriller final image missing consequence image")
    if not any("glass" in line for line in finals):
        errors.append("romance final image missing intimate image")
    if not any("worksheets" in line or "children fall asleep" in line for line in finals):
        errors.append("motivational final image missing domestic repair image")
    return result("validate_film_final_image_originality", not errors, errors)
