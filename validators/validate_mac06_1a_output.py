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
    "agents_md_detected",
    "agents_md_read",
    "layman_task_trigger_contract_read",
    "generic_direct_answer_avoided",
    "NATIVE_AGENT_CAPABILITY_ASSESSMENT",
    "TASK_FRESHNESS_CLASSIFICATION",
    "RESEARCH_MODE_DECISION",
    "Research Sufficiency Gate",
    "TASK_TO_CAPABILITY_ROUTING",
    "registries/native_capability_routing_matrix.yaml",
    "Registry-First Route",
    "Director Selection",
    "AGENT_RUNTIME_SELECTION",
    "registries/agent_runtime_selection_index.yaml",
    "Subagent Selection",
    "Skill Selection",
    "Subskill Selection",
    "TOOLS_CONNECTORS_PLUGINS_ASSESSMENT",
    "CONTENT_MISSION_BRIEF",
    "RESEARCH_AND_SOURCE_STATUS",
    "SCRIPT_STRUCTURE",
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
    "proof_classification",
    "chat_only_mode_used",
    "files_created=false",
    "dossier_artifacts_created=false",
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
    "workflow_executed=true",
    "gemini_api_called=true",
]

GENERIC_OUTPUT_MARKERS = [
    "Here is a script",
    "Here's a script",
    "Sure, here",
    "Here is your script",
    "Here's your script",
]

CANONICAL_RESEARCH_MODES = {
    "repo_only",
    "repo_plus_static_knowledge",
    "web_assisted",
    "real_time_web",
    "provider_api_assisted",
}

GATE_STATUSES = {
    "PASS",
    "BLOCKED",
    "NEEDS_USER_APPROVAL",
    "NEEDS_CONFIRMATION",
}

PROOF_CLASSIFICATIONS = {"PASS", "PARTIAL", "FAIL"}


def contains(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def find_key_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?im)^\s*[-*]?\s*`?{re.escape(key)}`?\s*=\s*([A-Za-z0-9_./:-]+)", text)
    return match.group(1) if match else None


def collect_invalid_research_modes(text: str) -> list[str]:
    modes = re.findall(r"(?im)^\s*[-*]?\s*`?research_mode`?\s*=\s*([A-Za-z0-9_]+)", text)
    return [mode for mode in modes if mode not in CANONICAL_RESEARCH_MODES]


def collect_invalid_gate_values(text: str) -> list[str]:
    values = re.findall(r"(?im)^\s*[-*]?\s*`?(?:current_status|gate_status)`?\s*=\s*([A-Z_]+)", text)
    return [value for value in values if value not in GATE_STATUSES]


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
    invalid_statuses.extend(collect_invalid_gate_values(text))
    invalid_research_modes = collect_invalid_research_modes(text)
    false_claims = [claim for claim in FALSE_EXECUTION_CLAIMS if claim in text]

    generic_detected = any(text.lstrip().startswith(marker) for marker in GENERIC_OUTPUT_MARKERS)
    matrix_missing = "registries/native_capability_routing_matrix.yaml" not in text
    index_missing = "registries/agent_runtime_selection_index.yaml" not in text
    files_created = re.search(r"(?im)^\s*[-*]?\s*`?files_created`?\s*=\s*true\b", text) is not None
    dossier_created = re.search(r"(?im)^\s*[-*]?\s*`?dossier_artifacts_created`?\s*=\s*true\b", text) is not None
    source_claim_without_list = (
        re.search(r"(?im)^\s*[-*]?\s*`?real_time_sources_used`?\s*=\s*true\b", text) is not None
        and not re.search(r"(?im)^\s*[-*]?\s*`?source_list(?:_present)?`?\s*=\s*(true|\[|http)", text)
    )
    final_proof = find_key_value(text, "proof_classification") or find_key_value(text, "final_proof_classification")

    status = "PASS"
    if false_claims or generic_detected or source_claim_without_list:
        status = "FAIL"
    elif (
        missing
        or invalid_statuses
        or invalid_research_modes
        or matrix_missing
        or index_missing
        or files_created
        or dossier_created
    ):
        status = "PARTIAL"

    final_status_matches_weakest = not (final_proof == "PASS" and status != "PASS")

    print(f"VALIDATION_STATUS={status}")
    print(f"missing_required_sections_count={len(missing)}")
    for item in missing:
        print(f"missing={item}")
    print(f"invalid_gate_status_count={len(invalid_statuses)}")
    for item in invalid_statuses:
        print(f"invalid_gate_status={item}")
    print(f"invalid_research_mode_count={len(invalid_research_modes)}")
    for item in invalid_research_modes:
        print(f"invalid_research_mode={item}")
    print(f"false_execution_claim_count={len(false_claims)}")
    for item in false_claims:
        print(f"false_execution_claim={item}")
    print(f"generic_output_detected={str(generic_detected).lower()}")
    print(f"capability_matrix_cited={str(not matrix_missing).lower()}")
    print(f"agent_runtime_selection_index_cited={str(not index_missing).lower()}")
    print(f"files_created_in_chat_only={str(files_created).lower()}")
    print(f"dossier_artifacts_created_in_chat_only={str(dossier_created).lower()}")
    print(f"source_claim_without_source_list={str(source_claim_without_list).lower()}")
    print(f"final_proof_classification={final_proof or 'MISSING'}")
    print(f"final_status_matches_weakest_evidence_layer={str(final_status_matches_weakest).lower()}")

    return 0 if status == "PASS" and final_status_matches_weakest else 1


if __name__ == "__main__":
    raise SystemExit(main())
