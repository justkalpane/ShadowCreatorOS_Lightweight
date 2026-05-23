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
    "task_intent_classified",
    "route_id",
    "registries/task_intent_routing_matrix.yaml",
    "director_skill_consumption_protocol_read",
    "script_quality_enforcement_contract_read",
    "gumloop_benchmark_output_standard_read",
    "DIRECTOR_CONSUMPTION_LEDGER",
    "AGENT_CONSUMPTION_LEDGER",
    "SUBAGENT_CONSUMPTION_LEDGER",
    "SKILL_CONSUMPTION_LEDGER",
    "SUBSKILL_CONSUMPTION_LEDGER",
    "LINE_BY_LINE_INFLUENCE_MAP",
    "TOPIC_QUALITY_GATE",
    "HOOK_GENERATION_GATE",
    "SCRIPT_QUALITY_GATE",
    "shallow_repo_routing_detected",
    "runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md",
    "runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md",
    "TASK_ROUTE_LOCK",
    "ROUTE_DEPENDENCY_EXPANSION_LOCK",
    "CONSUMPTION_LOCK",
    "SOURCE_RESEARCH_LOCK",
    "QUALITY_LOCK",
    "GOVERNANCE_LOCK",
    "route_manifest_path",
    "route_manifest_read",
    "route_dependency_expansion_lock_status",
    "route_scope_complete",
    "mandatory_files_read_before_output",
    "task_route_lock_status",
    "consumption_lock_status",
    "source_research_lock_status",
    "quality_lock_status",
    "governance_lock_status",
    "script_generated_after_all_locks",
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

SHALLOW_ROUTING_MARKERS = [
    "SHALLOW_REPO_ROUTING_ONLY",
    "DIRECTOR_CONSUMPTION_LEDGER=NONE_SELECTED",
    "DIRECTOR_CONSUMPTION_LEDGER = NONE_SELECTED",
    "AGENT_CONSUMPTION_LEDGER=NONE_SELECTED",
    "AGENT_CONSUMPTION_LEDGER = NONE_SELECTED",
    "SUBAGENT_CONSUMPTION_LEDGER=NONE_SELECTED",
    "SUBAGENT_CONSUMPTION_LEDGER = NONE_SELECTED",
    "SKILL_CONSUMPTION_LEDGER=NONE_SELECTED",
    "SKILL_CONSUMPTION_LEDGER = NONE_SELECTED",
    "SUBSKILL_CONSUMPTION_LEDGER=NONE_SELECTED",
    "SUBSKILL_CONSUMPTION_LEDGER = NONE_SELECTED",
    "skills_named_not_opened=true",
    "skill_files_named_but_not_read=true",
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
    "task_intent_classified",
    "task_intent_routing_matrix_cited",
    "director_skill_consumption_protocol_read",
    "script_quality_enforcement_contract_read",
    "gumloop_benchmark_output_standard_read",
    "task_execution_state_machine_contract_read",
    "route_dependency_expansion_protocol_read",
    "route_manifest_read",
    "route_dependency_expansion_lock_present",
    "route_scope_complete",
    "mandatory_files_read_before_output",
    "script_generated_after_all_locks",
    "director_consumption_ledger_present",
    "agent_consumption_ledger_present",
    "subagent_consumption_ledger_present",
    "skill_consumption_ledger_present",
    "subskill_consumption_ledger_present",
    "line_by_line_influence_map_present",
    "topic_quality_gate_present",
    "hook_generation_gate_present",
    "script_quality_gate_present",
]
REQUIRED_FALSE_KEYS = [
    "shallow_repo_routing_detected",
    "loaded_true_but_not_consumed_detected",
    "manual_rerun_structured_but_partial_detected",
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


def has_script_before_consumption_ledger(text: str) -> bool:
    script_markers = ["FINAL_SCRIPT", "Final script", "final_script_created=true"]
    ledger_markers = ["DIRECTOR_CONSUMPTION_LEDGER", "SKILL_CONSUMPTION_LEDGER"]
    script_positions = [text.find(marker) for marker in script_markers if text.find(marker) >= 0]
    ledger_positions = [text.find(marker) for marker in ledger_markers if text.find(marker) >= 0]
    if not script_positions or not ledger_positions:
        return False
    return min(script_positions) < min(ledger_positions)


def marker_before(text: str, first_markers: list[str], second_markers: list[str]) -> bool:
    first_positions = [text.find(marker) for marker in first_markers if text.find(marker) >= 0]
    second_positions = [text.find(marker) for marker in second_markers if text.find(marker) >= 0]
    if not first_positions or not second_positions:
        return False
    return min(first_positions) < min(second_positions)


def explicit_false(text: str, key: str) -> bool:
    value = find_key_value(text, key)
    return value is not None and value.lower() == "false"


def explicit_true(text: str, key: str) -> bool:
    value = find_key_value(text, key)
    return value is not None and value.lower() == "true"


def count_hook_variants(text: str) -> int:
    explicit = find_key_value(text, "hook_variants_count")
    if explicit and explicit.isdigit():
        return int(explicit)
    variants = set(re.findall(r"(?i)\bhook_variant[_ -]?([123])\b", text))
    return len(variants)


def missing_or_false(text: str, key: str) -> bool:
    value = find_key_value(text, key)
    return value is None or value.lower() != "true"


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
    shallow_routing_markers = [marker for marker in SHALLOW_ROUTING_MARKERS if marker in text]
    boot_signature_present = "SHADOW_BOOT_CONFIRMATION" in text
    content_before_boot_signature = has_content_before_boot_signature(text)
    sources_before_repo_route = has_sources_before_repo_route(text)
    script_before_consumption_ledger = has_script_before_consumption_ledger(text)
    hook_variant_count = count_hook_variants(text)
    script_markers = ["FINAL_SCRIPT", "Final script", "Final Script", "final_script_created=true"]
    route_manifest_unread = explicit_false(text, "route_manifest_read")
    route_manifest_missing = find_key_value(text, "route_manifest_path") in {None, ""} or route_manifest_unread
    route_dependency_expansion_lock_missing = "ROUTE_DEPENDENCY_EXPANSION_LOCK" not in text or explicit_false(text, "route_dependency_expansion_lock_present")
    route_scope_incomplete = explicit_false(text, "route_scope_complete")
    mandatory_files_not_read = explicit_false(text, "mandatory_files_read_before_output")
    bootstrap_loaded_true_but_no_route_lock = explicit_true(text, "bootstrap_loaded") and "TASK_ROUTE_LOCK" not in text
    script_before_task_route_lock = marker_before(text, script_markers, ["TASK_ROUTE_LOCK"])
    script_before_route_dependency_expansion_lock = marker_before(text, script_markers, ["ROUTE_DEPENDENCY_EXPANSION_LOCK"])
    script_before_consumption_lock = marker_before(text, script_markers, ["CONSUMPTION_LOCK"])
    final_script_before_quality_lock = marker_before(text, script_markers, ["QUALITY_LOCK"])
    final_classification_before_governance_lock = marker_before(
        text,
        ["Final Proof Classification", "proof_classification", "final_proof_classification"],
        ["GOVERNANCE_LOCK"],
    )
    source_lock_index = text.find("SOURCE_RESEARCH_LOCK")
    latest_claims_before_source_research_lock = False
    latest_match = re.search(r"(?i)\b(latest|current|this week|new update|today|2026|watch this week)\b", text)
    if latest_match and (source_lock_index < 0 or latest_match.start() < source_lock_index):
        latest_claims_before_source_research_lock = True
    manual_structured_output_missing_ledgers = explicit_true(text, "manual_rerun_structured_but_partial_detected")
    content_markers_present = any(marker in text for marker in ["TIMED_BEAT_MAP", "VOICE_GENERATION_CONTEXT", "CONTENT_MISSION_BRIEF"])
    content_engineering_present_but_no_consumption = content_markers_present and consumption_ledger_missing if "consumption_ledger_missing" in locals() else False
    hook_variants_without_scores = "HOOK_GENERATION_GATE" in text and hook_variant_count >= 3 and not (
        "score_each" in text or explicit_true(text, "hook_scores_present")
    )
    quality_gate_without_threshold = "SCRIPT_QUALITY_GATE" in text and find_key_value(text, "script_pass_threshold") is None
    selected_components_without_read_before_output = explicit_true(text, "selected_components_without_read_before_output")
    wrapper_required_mode_used = explicit_true(text, "wrapper_required_mode_used")
    wrapper_required_compatible = find_key_value(text, "codex_cloud_reliable_mode") == "WRAPPER_REQUIRED_COMPATIBLE"
    shadow_task_execution_wrapper_read = explicit_true(text, "shadow_task_execution_wrapper_read")
    plain_post_bootstrap_task_failed = explicit_true(text, "plain_post_bootstrap_task_failed")
    direct_script_after_bootstrap_without_wrapper = explicit_true(text, "direct_script_after_bootstrap_without_wrapper")
    wrapper_missing_when_required = explicit_true(text, "wrapper_missing_when_required") or (
        wrapper_required_compatible and not shadow_task_execution_wrapper_read
    )
    wrapper_used_but_locks_missing = explicit_true(text, "wrapper_used_but_locks_missing") or (
        wrapper_required_mode_used
        and (
            route_manifest_missing
            or route_dependency_expansion_lock_missing
            or route_scope_incomplete
            or mandatory_files_not_read
        )
    )

    generic_detected = any(text.lstrip().startswith(marker) for marker in GENERIC_OUTPUT_MARKERS)
    matrix_missing = "registries/native_capability_routing_matrix.yaml" not in text
    index_missing = "registries/agent_runtime_selection_index.yaml" not in text
    task_intent_matrix_missing = "registries/task_intent_routing_matrix.yaml" not in text
    route_id_missing = find_key_value(text, "route_id") in {None, ""}
    hook_variants_insufficient = hook_variant_count < 3
    script_scores_missing = find_key_value(text, "script_overall_score") is None or find_key_value(text, "script_pass_threshold") is None
    consumption_ledger_missing = any(
        marker not in text
        for marker in [
            "DIRECTOR_CONSUMPTION_LEDGER",
            "AGENT_CONSUMPTION_LEDGER",
            "SUBAGENT_CONSUMPTION_LEDGER",
            "SKILL_CONSUMPTION_LEDGER",
            "SUBSKILL_CONSUMPTION_LEDGER",
        ]
    )
    content_engineering_present_but_no_consumption = content_markers_present and consumption_ledger_missing
    quality_gate_missing = any(
        marker not in text
        for marker in ["TOPIC_QUALITY_GATE", "HOOK_GENERATION_GATE", "SCRIPT_QUALITY_GATE"]
    )
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
    required_false_failures: list[str] = []
    for key in REQUIRED_FALSE_KEYS:
        value = find_key_value(text, key)
        if value is None:
            required_false_failures.append(f"{key}=MISSING")
        elif value.lower() != "false":
            required_false_failures.append(f"{key}={value}")

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
        or shallow_routing_markers
        or script_before_consumption_ledger
        or route_scope_incomplete
        or route_manifest_unread
        or mandatory_files_not_read
        or bootstrap_loaded_true_but_no_route_lock
        or script_before_task_route_lock
        or script_before_route_dependency_expansion_lock
        or script_before_consumption_lock
        or latest_claims_before_source_research_lock
        or final_script_before_quality_lock
        or final_classification_before_governance_lock
        or hook_variants_without_scores
        or selected_components_without_read_before_output
        or direct_script_after_bootstrap_without_wrapper
        or wrapper_missing_when_required
        or wrapper_used_but_locks_missing
    ):
        status = "FAIL"
    elif (
        missing
        or invalid_statuses
        or invalid_research_modes
        or matrix_missing
        or index_missing
        or task_intent_matrix_missing
        or route_id_missing
        or hook_variants_insufficient
        or script_scores_missing
        or consumption_ledger_missing
        or quality_gate_missing
        or files_created
        or dossier_created
        or required_true_failures
        or required_false_failures
        or shadow_mode_invalid
        or route_manifest_missing
        or route_dependency_expansion_lock_missing
        or manual_structured_output_missing_ledgers
        or content_engineering_present_but_no_consumption
        or hook_variants_without_scores
        or quality_gate_without_threshold
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
    print(f"shallow_repo_routing_marker_count={len(shallow_routing_markers)}")
    for item in shallow_routing_markers:
        print(f"shallow_repo_routing_marker={item}")
    print(f"sources_before_repo_route={str(sources_before_repo_route).lower()}")
    print(f"script_before_consumption_ledger={str(script_before_consumption_ledger).lower()}")
    print(f"route_manifest_missing={str(route_manifest_missing).lower()}")
    print(f"route_manifest_unread={str(route_manifest_unread).lower()}")
    print(f"route_dependency_expansion_lock_missing={str(route_dependency_expansion_lock_missing).lower()}")
    print(f"route_scope_incomplete={str(route_scope_incomplete).lower()}")
    print(f"mandatory_files_not_read={str(mandatory_files_not_read).lower()}")
    print(f"bootstrap_loaded_true_but_no_route_lock={str(bootstrap_loaded_true_but_no_route_lock).lower()}")
    print(f"script_before_task_route_lock={str(script_before_task_route_lock).lower()}")
    print(f"script_before_route_dependency_expansion_lock={str(script_before_route_dependency_expansion_lock).lower()}")
    print(f"script_before_consumption_lock={str(script_before_consumption_lock).lower()}")
    print(f"latest_claims_before_source_research_lock={str(latest_claims_before_source_research_lock).lower()}")
    print(f"final_script_before_quality_lock={str(final_script_before_quality_lock).lower()}")
    print(f"final_classification_before_governance_lock={str(final_classification_before_governance_lock).lower()}")
    print(f"manual_structured_output_missing_ledgers={str(manual_structured_output_missing_ledgers).lower()}")
    print(f"content_engineering_present_but_no_consumption={str(content_engineering_present_but_no_consumption).lower()}")
    print(f"hook_variants_without_scores={str(hook_variants_without_scores).lower()}")
    print(f"quality_gate_without_threshold={str(quality_gate_without_threshold).lower()}")
    print(f"selected_components_without_read_before_output={str(selected_components_without_read_before_output).lower()}")
    print(f"plain_post_bootstrap_task_failed={str(plain_post_bootstrap_task_failed).lower()}")
    print(f"shadow_task_execution_wrapper_read={str(shadow_task_execution_wrapper_read).lower()}")
    print(f"wrapper_required_mode_used={str(wrapper_required_mode_used).lower()}")
    print(f"direct_script_after_bootstrap_without_wrapper={str(direct_script_after_bootstrap_without_wrapper).lower()}")
    print(f"wrapper_missing_when_required={str(wrapper_missing_when_required).lower()}")
    print(f"wrapper_used_but_locks_missing={str(wrapper_used_but_locks_missing).lower()}")
    print(f"generic_output_detected={str(generic_detected).lower()}")
    print(f"shadow_boot_confirmation_present={str(boot_signature_present).lower()}")
    print(f"content_before_shadow_boot_confirmation={str(content_before_boot_signature).lower()}")
    print(f"required_true_field_failure_count={len(required_true_failures)}")
    for item in required_true_failures:
        print(f"required_true_field_failure={item}")
    print(f"required_false_field_failure_count={len(required_false_failures)}")
    for item in required_false_failures:
        print(f"required_false_field_failure={item}")
    print(f"shadow_mode_chat_only={str(not shadow_mode_invalid).lower()}")
    print(f"capability_matrix_cited={str(not matrix_missing).lower()}")
    print(f"agent_runtime_selection_index_cited={str(not index_missing).lower()}")
    print(f"task_intent_routing_matrix_cited={str(not task_intent_matrix_missing).lower()}")
    print(f"route_id_present={str(not route_id_missing).lower()}")
    print(f"consumption_ledgers_present={str(not consumption_ledger_missing).lower()}")
    print(f"topic_quality_gate_present={str('TOPIC_QUALITY_GATE' in text).lower()}")
    print(f"hook_generation_gate_present={str('HOOK_GENERATION_GATE' in text).lower()}")
    print(f"hook_variants_count={hook_variant_count}")
    print(f"script_quality_gate_present={str('SCRIPT_QUALITY_GATE' in text).lower()}")
    print(f"script_scores_present={str(not script_scores_missing).lower()}")
    print(f"files_created_in_chat_only={str(files_created).lower()}")
    print(f"dossier_artifacts_created_in_chat_only={str(dossier_created).lower()}")
    print(f"source_claim_without_source_list={str(source_claim_without_list).lower()}")
    print(f"final_proof_classification={final_proof or 'MISSING'}")
    print(f"final_status_matches_weakest_evidence_layer={str(final_status_matches_weakest).lower()}")

    return 0 if status == "PASS" and final_status_matches_weakest else 1


if __name__ == "__main__":
    raise SystemExit(main())
