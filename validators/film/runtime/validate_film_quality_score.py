from __future__ import annotations

from tools.film_runtime.quality.film_quality_score_engine import SCORE_DIMENSIONS
from validators.film.runtime.preproduction_validator_utils import result


def validate(payload: dict) -> dict:
    report = payload.get("quality_score_report") or {}
    errors = []
    dims = report.get("score_dimensions") or {}
    for dim in SCORE_DIMENSIONS:
        if dim not in dims:
            errors.append(f"missing score dimension: {dim}")
            continue
        value = dims[dim]
        if not isinstance(value, (int, float)) or value < 0 or value > 10:
            errors.append(f"invalid score value for {dim}")
    if "overall_score" not in report or not isinstance(report.get("overall_score"), (int, float)):
        errors.append("overall_score missing")
    if report.get("quality_band") not in {"FAIL_WEAK_FILM", "NEEDS_MAJOR_REWRITE", "WORKABLE_DRAFT", "STRONG_DRAFT", "EXCELLENT"}:
        errors.append("quality_band invalid")
    if not isinstance(report.get("defect_list"), list):
        errors.append("defect_list missing")
    if payload.get("expect_weak") is True and report.get("overall_score", 10) > 5.0:
        errors.append("weak input score must stay at or below NEEDS_MAJOR_REWRITE threshold")
    return result("validate_film_quality_score", not errors, errors)

