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
    "SHADOW_BOOT_CONFIRMATION",
    "shadow_boot_confirmation_present",
    "first_visible_output_is_boot_confirmation",
    "AGENTS.md",
    "agents_md_detected",
    "agents_md_read",
    "repo_first_orchestration_started",
    "layman_task_trigger_contract_read",
    "generic_direct_answer_avoided",
    "shadow_mode=CHAT_ONLY_MODE",
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

INTERNET_FIRST_MARKERS = [
    "web_access_used_before_repo_route=true",
    "internet_first_behavior_detected=true",
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
REQUIRED_TRUE_KEYS = [
    "shadow_boot_confirmation_present",
    "first_visible_output_is_boot_confirmation",
    "agents_md_detected",
    "agents_md_read",
    "repo_first_orchestration_started",
    "generic_direct_answer_avoided",
]


def contains(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def find_key_value(text: str, key: str) -> str | None:
    match = re.search(rf"(?im)^\s*[-*]?\s*`?{re.escape(key)}`?\s*=\s*([A-Za-z0-9_./:-]+)", text)
    return match.group(1) if match else None


def has_content_before_boot_signature(text: str) -> bool:
    boot_index = text.find("SHADOW_BOOT_CONFIRMATION")
    if boot_index < 0:
        return True
    return bool(text[:boot_index].strip())


def has_sources_before_repo_route(text: str) -> bool:
    route_markers = [
        "TASK_TO_CAPABILITY_ROUTING",
        "Registry-First Route",
        "registries/native_capability_routing_matrix.yaml",
    ]
    route_positions = [text.find(marker) for marker in route_markers if text.find(marker) >= 0]
    if not route_positions:
        return False
    route_index = min(route_positions)
    before_route = text[:route_index]
    return bool(re.search(r"(?im)^\s*(source_list|sources?)\s*[:=]\s*(https?://|\[?https?://)", before_route))


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
    internet_first_markers = [marker for marker in INTERNET_FIRST_MARKERS if marker in text]
    boot_signature_present = "SHADOW_BOOT_CONFIRMATION" in text
    content_before_boot_signature = has_content_before_boot_signature(text)
    sources_before_repo_route = has_sources_before_repo_route(text)

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
    required_true_failures: list[str] = []
    for key in REQUIRED_TRUE_KEYS:
        value = find_key_value(text, key)
        if value is None:
            required_true_failures.append(f"{key}=MISSING")
        elif value.lower() != "true":
            required_true_failures.append(f"{key}={value}")

    shadow_mode = find_key_value(text, "shadow_mode")
    shadow_mode_invalid = shadow_mode not in {"CHAT_ONLY_MODE"}

    status = "PASS"
    if (
        false_claims
        or generic_detected
        or source_claim_without_list
        or not boot_signature_present
        or content_before_boot_signature
        or internet_first_markers
        or sources_before_repo_route
    ):
        status = "FAIL"
    elif (
        missing
        or invalid_statuses
        or invalid_research_modes
        or matrix_missing
        or index_missing
        or files_created
        or dossier_created
        or required_true_failures
        or shadow_mode_invalid
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
    print(f"internet_first_marker_count={len(internet_first_markers)}")
    for item in internet_first_markers:
        print(f"internet_first_marker={item}")
    print(f"sources_before_repo_route={str(sources_before_repo_route).lower()}")
    print(f"generic_output_detected={str(generic_detected).lower()}")
    print(f"shadow_boot_confirmation_present={str(boot_signature_present).lower()}")
    print(f"content_before_shadow_boot_confirmation={str(content_before_boot_signature).lower()}")
    print(f"required_true_field_failure_count={len(required_true_failures)}")
    for item in required_true_failures:
        print(f"required_true_field_failure={item}")
    print(f"shadow_mode_chat_only={str(not shadow_mode_invalid).lower()}")
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
