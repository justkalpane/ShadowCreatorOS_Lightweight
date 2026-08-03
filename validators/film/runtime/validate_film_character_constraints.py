"""Artifact-bound character constraint validator for the film screenplay runtime proof."""

from __future__ import annotations

import sys
from typing import Any

from pathlib import Path

try:
    from validators.film.runtime.runtime_artifact_utils import contains_any, load_screenplay_packet, screenplay_text
except ModuleNotFoundError:  # pragma: no cover - direct file execution fallback
    REPO_ROOT = Path(__file__).resolve().parents[3]
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from validators.film.runtime.runtime_artifact_utils import contains_any, load_screenplay_packet, screenplay_text


PHASE = "13D_F3"
RUNTIME_BEHAVIOR_CHANGED = False
ROUTE_SELECTOR_MODIFIED = False
VALIDATOR_BOUND_TO_RUNTIME = True
GOVERNED_RUNTIME_PROOF_CLAIMED = False


def _result(status: str, passed: bool, message: str, errors: list[str] | None = None) -> dict[str, Any]:
    return {
        "validator": "validate_film_character_constraints",
        "phase": PHASE,
        "status": status,
        "passed": passed,
        "enforced": True,
        "runtime_behavior_changed": RUNTIME_BEHAVIOR_CHANGED,
        "route_selector_modified": ROUTE_SELECTOR_MODIFIED,
        "validator_bound_to_runtime": VALIDATOR_BOUND_TO_RUNTIME,
        "governed_runtime_proof_claimed": GOVERNED_RUNTIME_PROOF_CLAIMED,
        "errors": errors or [],
        "message": message,
    }


def validate(payload: dict[str, Any]) -> dict[str, Any]:
    packet = load_screenplay_packet(payload)
    text = screenplay_text(packet, payload)
    errors: list[str] = []

    characters = packet.get("character_list") or []
    if not isinstance(characters, list) or len(characters) < 2:
        errors.append("at least 2 named characters are required")

    main = characters[0] if characters else {}
    main_traits = " ".join(main.get("traits", [])) if isinstance(main, dict) else ""
    main_context = " ".join(main.get("life_context", [])) if isinstance(main, dict) else ""
    forbidden = " ".join(main.get("forbidden_behaviors", [])) if isinstance(main, dict) else ""
    if not contains_any(main_traits, ["soft-spoken", "warm", "controlled", "internally angry", "non-explosive"]):
        errors.append("main character traits do not match the controlled-anger profile")
    if not contains_any(main_context, ["parent", "guardian", "toddlers"]):
        errors.append("main character life context does not include toddler parenting/guardianship")
    if contains_any(forbidden, ["shouting", "violence", "threats", "abuse"]) is False:
        errors.append("main character forbidden behaviors not declared")

    if contains_any(text, ["shout", "shouting", "violence", "abuse", "threaten", "threats"]):
        errors.append("screenplay text contains forbidden aggression markers")

    if not contains_any(text, ["toddler", "toddlers", "twins", "children", "child"]):
        errors.append("toddler stakes are not integrated into the screenplay text")

    if errors:
        return _result("VALIDATION_FAILED", False, "Film character constraint validation failed.", errors)

    return _result("VALIDATION_PASSED", True, "Film character constraint validation passed.")
