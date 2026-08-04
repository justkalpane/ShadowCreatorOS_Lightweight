"""Local validator for film-vs-content packet separation.

This validator is intentionally not bound to runtime. It checks fixture-style
payloads for route-boundary collisions between content packets and film packets
without claiming film screenplay packet quality or governed runtime proof.
"""

from __future__ import annotations

from typing import Any


PHASE = "13E_40"
RUNTIME_BEHAVIOR_CHANGED = False
ROUTE_SELECTOR_MODIFIED = False
VALIDATOR_BOUND_TO_RUNTIME = False
GOVERNED_RUNTIME_PROOF_CLAIMED = False

FILM_ROUTE = "FILM_SCREENPLAY_GENERATION"
SCRIPT_ROUTE = "SCRIPT_GENERATION"

ALLOWED_FAMILIES = {
    "content_preservation",
    "film_packet_validation",
    "no_fake_pass",
}

CONTENT_DRIFT_TERMS = [
    "content-mode",
    "content mode",
    "content packet",
    "content script",
    "content validator",
    "hook",
    "re-hook",
    "retention",
    "platform packaging",
    "youtube",
    "shorts",
    "instagram",
    "reel",
    "tiktok",
    "thumbnail",
]

FILM_SHAPE_TERMS = [
    "film packet",
    "logline",
    "theme",
    "premise",
    "genre",
    "tone",
    "beat sheet",
    "character arc",
    "scene turns",
    "dialogue subtext",
    "visual motif",
    "camera notes",
    "screenplay body",
]

CONTENT_VALIDATOR_FOR_FILM_CLAIM = "content_validator_pass_for_film_packet"


def _text(payload: dict[str, Any]) -> str:
    parts = [
        payload.get("input_prompt"),
        payload.get("input_packet_summary"),
        payload.get("input_summary"),
        payload.get("purpose"),
        payload.get("risk_if_missing"),
    ]
    return " ".join(str(part) for part in parts if part).lower()


def _has_any(text: str, terms: list[str]) -> bool:
    return any(term in text for term in terms)


def _result(status: str, passed: bool, message: str, errors: list[str] | None = None) -> dict[str, Any]:
    return {
        "validator": "validate_film_content_packet_separation",
        "phase": PHASE,
        "status": status,
        "passed": passed,
        "enforced": status != "SKELETON_ONLY",
        "runtime_behavior_changed": RUNTIME_BEHAVIOR_CHANGED,
        "route_selector_modified": ROUTE_SELECTOR_MODIFIED,
        "validator_bound_to_runtime": VALIDATOR_BOUND_TO_RUNTIME,
        "governed_runtime_proof_claimed": GOVERNED_RUNTIME_PROOF_CLAIMED,
        "pass_claimed": False,
        "separation_boundary_only": True,
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
    family = payload.get("fixture_family")
    expected_route = payload.get("expected_route")
    expected_result = payload.get("expected_result")
    text = _text(payload)
    missing_required_fields = payload.get("missing_required_fields") or []
    prohibited_claims = payload.get("prohibited_claims") or []

    if family not in ALLOWED_FAMILIES:
        errors.append(f"fixture_family must be one of {sorted(ALLOWED_FAMILIES)}")
    if not text:
        errors.append("input_prompt, input_packet_summary, or input_summary is required")

    if family == "content_preservation":
        if expected_route != SCRIPT_ROUTE:
            errors.append("content-preservation payload must preserve SCRIPT_GENERATION")
        if payload.get("should_pass_later") is not True or payload.get("should_fail_later") is not False:
            errors.append("content-preservation payload must be a positive preservation fixture")
        if expected_route == FILM_ROUTE or _has_any(text, ["pretending to be a film packet"]):
            errors.append("content-preservation payload cannot claim film-core authority")

    if family == "film_packet_validation":
        if expected_route != FILM_ROUTE:
            errors.append("film-packet payload must stay under FILM_SCREENPLAY_GENERATION")
        if "content-mode" in text or "content script" in text or "pretending" in text:
            errors.append("content packet cannot impersonate a film packet")
        if "hook" in text and "retention" in text and missing_required_fields:
            errors.append("content hook/retention metrics cannot substitute for filmcraft packet fields")
        if expected_result == "PASS_LATER" and not _has_any(text, FILM_SHAPE_TERMS):
            errors.append("positive film boundary fixture must contain film packet shape evidence")

    if family == "no_fake_pass":
        if CONTENT_VALIDATOR_FOR_FILM_CLAIM in prohibited_claims or "content validator" in text:
            errors.append("content validator cannot pass or approve a film packet")
        else:
            return _result(
                "VALIDATION_DEFERRED",
                False,
                "No-fake-PASS fixture is outside content-packet separation scope.",
            )

    if errors:
        return _result(
            "VALIDATION_FAILED",
            False,
            "Film/content packet separation payload failed local enforcement.",
            errors,
        )

    return _result(
        "VALIDATION_PASSED",
        True,
        "Film/content packet separation payload passed local boundary enforcement only.",
    )
