from __future__ import annotations

from validators.film.runtime.preproduction_validator_utils import packet, result


def validate(payload: dict) -> dict:
    data = packet(payload)
    sequences = (data.get("sequence_structure") or {}).get("sequences") or []
    scene_numbers = {card.get("scene_number") for card in data.get("scene_cards") or []}
    errors = []
    if len(sequences) < 3:
        errors.append("at least 3 sequences are required")
    previous = -1
    for sequence in sequences:
        for field in ["sequence_id", "scene_numbers", "objective", "conflict", "turning_point", "output_scene_numbers"]:
            if field not in sequence or sequence.get(field) in ({}, [], "", None):
                errors.append(f"sequence missing {field}")
        if "conflict" not in sequence or not str(sequence.get("conflict")).strip():
            errors.append("sequence_without_conflict")
        if "turning_point" not in sequence or not str(sequence.get("turning_point")).strip():
            errors.append("sequence_without_turning_point")
        numbers = sequence.get("scene_numbers") or []
        if numbers and min(numbers) <= previous:
            errors.append("sequence order is not logical")
        if numbers:
            previous = max(numbers)
        if not set(sequence.get("output_scene_numbers") or []).issubset(scene_numbers):
            errors.append("sequence_not_connected_to_scene_cards")
    return result("validate_film_sequence_structure", not errors, errors)
