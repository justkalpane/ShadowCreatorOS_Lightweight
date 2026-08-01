"""Local fixture/payload validator for film route-selection boundaries.

This validator is intentionally not bound to runtime. It validates explicit
fixture-style payloads so the film route can advance one enforcement layer
without modifying selector behavior or claiming governed runtime proof.
"""

from __future__ import annotations

import re
from typing import Any


PHASE = "13E_38"
RUNTIME_BEHAVIOR_CHANGED = False
ROUTE_SELECTOR_MODIFIED = False
VALIDATOR_BOUND_TO_RUNTIME = False
GOVERNED_RUNTIME_PROOF_CLAIMED = False

FILM_ROUTE = "FILM_SCREENPLAY_GENERATION"
SCRIPT_ROUTE = "SCRIPT_GENERATION"
DOWNSTREAM_ROUTES = {
    "FULL_VIDEO_PIPELINE",
    "FILM_RELEASE_PACKAGING",
    "FILM_RELEASE_DISTRIBUTION",
}

ROUTE_TO_MODE = {
    FILM_ROUTE: "film_core",
    SCRIPT_ROUTE: "content",
    "FULL_VIDEO_PIPELINE": "downstream",
    "FILM_RELEASE_PACKAGING": "downstream",
    "FILM_RELEASE_DISTRIBUTION": "downstream",
}

FILM_CORE_PATTERNS = [
    r"\bscreenplay\b",
    r"\bshort film\b",
    r"\bfeature film\b",
    r"\bshooting script\b",
    r"\bfilm scene\b",
    r"\bdialogue scene\b",
    r"\bcharacter arc film\b",
    r"\banimated short film\b",
    r"\bdocudrama film\b",
    r"\breal[- ]incident short film\b",
]

CONTENT_PATTERNS = [
    r"\byoutube\b",
    r"\bshorts\b",
    r"\binstagram\b",
    r"\breel\b",
    r"\btiktok\b",
    r"\bvoiceover script\b",
    r"\bexplainer\b",
    r"\bcontent script\b",
    r"\bcreator video\b",
    r"\bhook[- ]focused\b",
    r"\bretention[- ]focused\b",
    r"\bcontent packet\b",
]

DOWNSTREAM_PATTERN_ROUTES = [
    (r"\bfull video pipeline\b", "FULL_VIDEO_PIPELINE"),
    (r"\bmedia factory handoff\b", "FULL_VIDEO_PIPELINE"),
    (r"\bthumbnail\b|\btitle pack\b|\btitle\b", "FILM_RELEASE_PACKAGING"),
    (r"\btrailer\b|\bteaser\b|\bsocial cutdown\b|\brelease\b", "FILM_RELEASE_DISTRIBUTION"),
]


def _matches(patterns: list[str], text: str) -> bool:
    return any(re.search(pattern, text) for pattern in patterns)


def _normalize_text(payload: dict[str, Any]) -> str:
    text = payload.get("input_prompt") or payload.get("input_packet_summary") or ""
    return str(text).strip().lower()


def _expected_mode_for_route(route: str) -> str | None:
    return ROUTE_TO_MODE.get(route)


def _infer_expected_route(text: str) -> str | None:
    for pattern, route in DOWNSTREAM_PATTERN_ROUTES:
        if re.search(pattern, text):
            return route

    if _matches(CONTENT_PATTERNS, text):
        return SCRIPT_ROUTE

    if _matches(FILM_CORE_PATTERNS, text):
        return FILM_ROUTE

    return None


def _result(status: str, passed: bool, message: str, errors: list[str] | None = None) -> dict[str, Any]:
    return {
        "validator": "validate_film_route_selection",
        "phase": PHASE,
        "status": status,
        "passed": passed,
        "enforced": status != "SKELETON_ONLY",
        "runtime_behavior_changed": RUNTIME_BEHAVIOR_CHANGED,
        "route_selector_modified": ROUTE_SELECTOR_MODIFIED,
        "validator_bound_to_runtime": VALIDATOR_BOUND_TO_RUNTIME,
        "governed_runtime_proof_claimed": GOVERNED_RUNTIME_PROOF_CLAIMED,
        "pass_claimed": False,
        "errors": errors or [],
        "message": message,
    }


def validate(payload: dict) -> dict:
    if not payload:
        return _result(
            "SKELETON_ONLY",
            False,
            "No payload supplied. Runtime harness remains blocked until it passes governed validator inputs.",
        )

    errors: list[str] = []
    fixture_family = payload.get("fixture_family")
    expected_route = payload.get("expected_route")
    expected_mode = payload.get("expected_mode")
    text = _normalize_text(payload)

    if fixture_family not in {"route_selection", "content_preservation"}:
        errors.append("fixture_family must be route_selection or content_preservation")
    if not text:
        errors.append("input_prompt or input_packet_summary is required")
    if expected_route not in ROUTE_TO_MODE:
        errors.append(f"expected_route must be one of {sorted(ROUTE_TO_MODE)}")

    inferred_route = _infer_expected_route(text) if text else None
    if inferred_route and expected_route and inferred_route != expected_route:
        errors.append(f"expected_route {expected_route} conflicts with inferred route {inferred_route}")

    route_mode = _expected_mode_for_route(str(expected_route)) if expected_route else None
    if expected_mode is None and fixture_family == "content_preservation" and expected_route == SCRIPT_ROUTE:
        expected_mode = "content"
    if route_mode and expected_mode != route_mode:
        errors.append(f"expected_mode {expected_mode} conflicts with route mode {route_mode}")

    if expected_route == FILM_ROUTE and _matches(CONTENT_PATTERNS, text):
        errors.append("content/platform trigger cannot be promoted to film-core route")
    if expected_route == FILM_ROUTE and any(re.search(pattern, text) for pattern, _ in DOWNSTREAM_PATTERN_ROUTES):
        errors.append("downstream trigger cannot be promoted to film-core route")
    if expected_route == SCRIPT_ROUTE and _matches(FILM_CORE_PATTERNS, text) and not _matches(CONTENT_PATTERNS, text):
        errors.append("explicit screenplay/film trigger cannot be flattened into content route")
    if expected_route in DOWNSTREAM_ROUTES and expected_mode != "downstream":
        errors.append("downstream route must use expected_mode downstream")

    should_pass_later = payload.get("should_pass_later")
    should_fail_later = payload.get("should_fail_later")
    if should_pass_later is not True:
        errors.append("route-selection enforcement currently accepts only should_pass_later=true fixtures")
    if should_fail_later is not False:
        errors.append("route-selection enforcement currently accepts only should_fail_later=false fixtures")

    if errors:
        return _result(
            "VALIDATION_FAILED",
            False,
            "Film route-selection payload failed local enforcement.",
            errors,
        )

    return _result(
        "VALIDATION_PASSED",
        True,
        "Film route-selection payload passed local enforcement without runtime binding.",
    )
