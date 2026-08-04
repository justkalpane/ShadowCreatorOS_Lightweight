"""Artifact-bound dialogue subtext validator for the film screenplay runtime proof."""

from __future__ import annotations

import sys
import re
from pathlib import Path
from typing import Any

try:
    from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet, screenplay_text
except ModuleNotFoundError:  # pragma: no cover - direct file execution fallback
    REPO_ROOT = Path(__file__).resolve().parents[3]
    if str(REPO_ROOT) not in sys.path:
        sys.path.insert(0, str(REPO_ROOT))
    from validators.film.runtime.runtime_artifact_utils import load_screenplay_packet, screenplay_text


PHASE = "13D_F6"
RUNTIME_BEHAVIOR_CHANGED = False
ROUTE_SELECTOR_MODIFIED = False
VALIDATOR_BOUND_TO_RUNTIME = True
GOVERNED_RUNTIME_PROOF_CLAIMED = False


def _result(status: str, passed: bool, message: str, errors: list[str] | None = None) -> dict[str, Any]:
    return {
        "validator": "validate_film_dialogue_subtext",
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
    raw_text = screenplay_text(packet, payload)
    text = raw_text.lower()
    character_bible = packet.get("character_bible") or {}
    relationship_map = packet.get("relationship_map") or {}
    dialogue_subtext_pass = packet.get("dialogue_subtext_pass") or {}
    errors: list[str] = []

    if "believe in yourself" in text or "never give up" in text:
        errors.append("dialogue reads as generic motivational speech")
    major_characters = character_bible.get("major_characters") or []
    protagonist_name = ""
    if major_characters:
        protagonist_name = str(major_characters[0].get("name", "")).strip()
    loud_patterns = [
        rf"\b{re.escape(protagonist_name)}\b[^.\n]{{0,30}}\b(?:shouts?|yells?|screams?)\b" if protagonist_name else None,
        r"\b(?:he|she|they)\b[^.\n]{0,30}\b(?:shouts?|yells?|screams?)\b",
    ]
    if any(pattern and re.search(pattern, raw_text, re.IGNORECASE) for pattern in loud_patterns):
        errors.append("main character dialogue/action contains loud escalation")

    subtext = " ".join(str(value) for value in dialogue_subtext_pass.values()).lower() if isinstance(dialogue_subtext_pass, dict) else ""
    if not subtext or not any(term in subtext for term in ["care", "fatigue", "mirror", "underneath", "subtext"]):
        errors.append("dialogue_subtext_pass does not provide relationship subtext")

    relationships = relationship_map.get("relationships") or []
    if not any("mirror" in str(item).lower() for item in relationships):
        errors.append("second character mirror function is missing from relationship map")

    if len(major_characters) < 2:
        errors.append("character bible must include at least two major characters")
    elif "emotional mirror" not in str(major_characters[1]).lower():
        errors.append("second character is not defined as an emotional mirror")

    if errors:
        return _result("VALIDATION_FAILED", False, "Film dialogue subtext validation failed.", errors)
    return _result("VALIDATION_PASSED", True, "Film dialogue subtext validation passed.")
