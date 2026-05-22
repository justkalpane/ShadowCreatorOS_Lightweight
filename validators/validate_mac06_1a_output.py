#!/usr/bin/env python3
"""Validate MAC-06.1A fresh-agent output text.

Usage:
  python validators/validate_mac06_1a_output.py path/to/output.txt
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "AGENTS.md",
    "NATIVE_AGENT_CAPABILITY_ASSESSMENT",
    "TASK_FRESHNESS_CLASSIFICATION",
    "RESEARCH_MODE_DECISION",
    "Research Sufficiency Gate",
    "TASK_TO_CAPABILITY_ROUTING",
    "Registry-First Route",
    "Director Selection",
    "AGENT_RUNTIME_SELECTION",
    "Subagent Selection",
    "Skill Selection",
    "Subskill Selection",
    "TOOLS_CONNECTORS_PLUGINS_ASSESSMENT",
    "CONTENT_MISSION_BRIEF",
    "Final script",
    "TIMED_BEAT_MAP",
    "VOICE_GENERATION_CONTEXT",
    "IMAGE_GENERATION_CONTEXT",
    "VIDEO_GENERATION_CONTEXT",
    "MUSIC_AND_SFX_CONTEXT",
    "EDITING_CONTEXT",
    "PLATFORM_PACKAGING",
    "Provider Handoff Boundary",
    "Quality Gate",
    "Lineage Summary",
    "Final Proof Classification",
]

INVALID_GATE_STATUSES = [
    "PASS_WITH_NOTICE",
    "PASS_WITH_REFINEMENT",
    "READY_FOR_USER_DECISION",
]

FALSE_EXECUTION_CLAIMS = [
    "n8n_used=true",
    "providers_called=true",
    "media_artifacts_claimed=true",
]

GENERIC_OUTPUT_MARKERS = [
    "Here is a script",
    "Here's a script",
    "Sure, here",
]


def contains(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_mac06_1a_output.py <output.txt>")
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"VALIDATION_STATUS=FAIL\nreason=file_not_found\npath={path}")
        return 1

    text = path.read_text(errors="replace")
    missing = [section for section in REQUIRED_SECTIONS if not contains(text, section)]
    invalid_statuses = [status for status in INVALID_GATE_STATUSES if status in text]
    false_claims = [claim for claim in FALSE_EXECUTION_CLAIMS if claim in text]

    generic_detected = any(text.lstrip().startswith(marker) for marker in GENERIC_OUTPUT_MARKERS)
    matrix_missing = "registries/native_capability_routing_matrix.yaml" not in text
    index_missing = "registries/agent_runtime_selection_index.yaml" not in text

    status = "PASS"
    if false_claims or generic_detected:
        status = "FAIL"
    elif missing or invalid_statuses or matrix_missing or index_missing:
        status = "PARTIAL"

    print(f"VALIDATION_STATUS={status}")
    print(f"missing_required_sections_count={len(missing)}")
    for item in missing:
        print(f"missing={item}")
    print(f"invalid_gate_status_count={len(invalid_statuses)}")
    for item in invalid_statuses:
        print(f"invalid_gate_status={item}")
    print(f"false_execution_claim_count={len(false_claims)}")
    for item in false_claims:
        print(f"false_execution_claim={item}")
    print(f"generic_output_detected={str(generic_detected).lower()}")
    print(f"capability_matrix_cited={str(not matrix_missing).lower()}")
    print(f"agent_runtime_selection_index_cited={str(not index_missing).lower()}")

    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
