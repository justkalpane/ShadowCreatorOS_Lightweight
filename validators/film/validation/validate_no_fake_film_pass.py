"""Local validator that blocks fake film PASS/runtime-proof claims.

This validator is intentionally not bound to runtime. Empty-payload calls remain
non-proof-producing for existing harness compatibility.
"""

from __future__ import annotations

from typing import Any

PHASE = "13E_46"
RUNTIME_BEHAVIOR_CHANGED = False
ROUTE_SELECTOR_MODIFIED = False
VALIDATOR_BOUND_TO_RUNTIME = False
GOVERNED_RUNTIME_PROOF_CLAIMED = False
PASS_CLAIMED = False

PROHIBITED_CLAIM_MESSAGES = {
    "film_screenplay_output_packet": "film screenplay output packet cannot be claimed without film schema evidence",
    "content_validator_pass_for_film_packet": "content validator cannot pass or approve a film packet",
    "source_backed_film_claim": "source-backed film claim requires a source ledger",
    "route_lineage_complete": "route lineage completion requires a lineage or consumption ledger",
    "filmcraft_scorecard_complete": "filmcraft scorecard completion requires scorecard evidence",
    "governed_runtime_proof_from_repo_read": "GitHub or repo inspection is not governed runtime proof",
    "repository_lock_id": "runtime artifact names cannot be invented",
    "proof_contract_id": "runtime artifact names cannot be invented",
    "context_packet_id": "runtime artifact names cannot be invented",
    "prompt_package_id": "runtime artifact names cannot be invented",
    "evaluation_report_id": "runtime artifact names cannot be invented",
    "completion_certificate": "runtime artifact names cannot be invented",
}

PASS_KEYS = {
    "pass",
    "pass_claimed",
    "film_pass_claimed",
    "runtime_pass_claimed",
    "governed_runtime_proof_claimed",
}


def _result(status: str, passed: bool, message: str, errors: list[str] | None = None) -> dict[str, Any]:
    return {
        "validator": "validate_no_fake_film_pass",
        "phase": PHASE,
        "status": status,
        "passed": passed,
        "enforced": status != "SKELETON_ONLY",
        "runtime_behavior_changed": RUNTIME_BEHAVIOR_CHANGED,
        "route_selector_modified": ROUTE_SELECTOR_MODIFIED,
        "validator_bound_to_runtime": VALIDATOR_BOUND_TO_RUNTIME,
        "governed_runtime_proof_claimed": GOVERNED_RUNTIME_PROOF_CLAIMED,
        "pass_claimed": PASS_CLAIMED,
        "no_fake_pass_boundary_only": True,
        "errors": errors or [],
        "message": message,
    }


def _has_evidence(payload: dict[str, Any], *keys: str) -> bool:
    return any(bool(payload.get(key)) for key in keys)


def _fixture_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    prohibited_claims = payload.get("prohibited_claims") or []

    if payload.get("fixture_family") != "no_fake_pass":
        errors.append("fixture_family must be no_fake_pass for no-fake film PASS validation")

    for claim in prohibited_claims:
        message = PROHIBITED_CLAIM_MESSAGES.get(claim, f"prohibited film PASS claim detected: {claim}")
        if message not in errors:
            errors.append(message)

    if payload.get("should_fail_later") is True and not prohibited_claims:
        errors.append("negative no-fake fixture must list prohibited claims")

    return errors


def _payload_errors(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for key in PASS_KEYS:
        if payload.get(key) is True:
            errors.append(f"{key}=true is not allowed in local no-fake-PASS validation")

    if payload.get("validator_type") == "content" and payload.get("target_route") == "FILM_SCREENPLAY_GENERATION":
        errors.append("content validator cannot pass or approve a film packet")

    if payload.get("claims_film_schema_valid") is True and not _has_evidence(payload, "film_schema_evidence", "film_screenplay_output_packet"):
        errors.append("film schema validity claim requires film schema evidence")

    if payload.get("claims_source_backed") is True and not _has_evidence(payload, "source_ledger"):
        errors.append("source-backed film claim requires a source ledger")

    if payload.get("claims_route_lineage_complete") is True and not _has_evidence(payload, "route_lineage_ledger", "consumption_ledger"):
        errors.append("route lineage completion requires a lineage or consumption ledger")

    if payload.get("claims_filmcraft_scorecard_complete") is True and not _has_evidence(payload, "filmcraft_scorecard", "film_validation_scorecard"):
        errors.append("filmcraft scorecard completion requires scorecard evidence")

    if payload.get("claims_governed_runtime_proof_from_repo_read") is True:
        errors.append("GitHub or repo inspection is not governed runtime proof")

    artifact_claims = payload.get("runtime_artifact_claims") or []
    invented_artifacts = [
        claim for claim in artifact_claims
        if claim in PROHIBITED_CLAIM_MESSAGES and not _has_evidence(payload, "governed_runtime_artifact_ledger")
    ]
    if invented_artifacts:
        errors.append("runtime artifact names cannot be invented")

    prohibited_claims = payload.get("prohibited_claims") or []
    for claim in prohibited_claims:
        message = PROHIBITED_CLAIM_MESSAGES.get(claim, f"prohibited film PASS claim detected: {claim}")
        if message not in errors:
            errors.append(message)

    return errors


def validate(payload: dict) -> dict:
    if not payload:
        return _result(
            "SKELETON_ONLY",
            False,
            "No payload supplied. Runtime harness remains blocked until it passes governed validator inputs.",
        )

    if payload.get("fixture_family") == "no_fake_pass":
        errors = _fixture_errors(payload)
    else:
        errors = _payload_errors(payload)

    if errors:
        return _result(
            "VALIDATION_FAILED",
            False,
            "No-fake film PASS payload failed local enforcement.",
            errors,
        )

    return _result(
        "VALIDATION_PASSED",
        True,
        "No-fake film PASS payload passed local boundary enforcement without runtime binding.",
    )
