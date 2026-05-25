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

FALSE_ONBOARDING_CLAIMS = [
    "safe_to_declare_default_bootstrap_mode_onboarded=true",
    "safe_to_declare_lightweight_os_onboarded=true",
    "codex_cloud_safe_as_primary_operator=true",
    "lightweight_os_onboarded=true",
    "default_bootstrap_mode_onboarded=true",
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

PROOF_CLASSIFICATIONS = {"PASS", "PASS_WITH_NOTICE", "PARTIAL", "FAIL"}
VALID_OUTPUT_MODES = {"PROOF_MODE", "OPERATOR_MODE", "DEBUG_MODE"}
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


def explicit_status(text: str, key: str) -> str | None:
    value = find_key_value(text, key)
    return value.upper() if value else None


def explicit_not_true(text: str, key: str) -> bool:
    value = find_key_value(text, key)
    return value is not None and value.lower() != "true"


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
    false_onboarding_claims = [claim for claim in FALSE_ONBOARDING_CLAIMS if claim in text]
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
    latest_or_watchlist_task = bool(
        re.search(r"(?i)\b(latest|current|this week|new update|today|2026|watchlist|tools to watch)\b", text)
    )
    source_breadth_status = explicit_status(text, "source_breadth_lock_status") or explicit_status(text, "source_breadth_status")
    rule_consumption_evidence_status = explicit_status(text, "rule_consumption_evidence_lock_status")
    per_tool_source_map_present = explicit_true(text, "per_tool_source_map_present") or "PER_TOOL_SOURCE_MAP" in text
    per_tool_source_map_count_value = find_key_value(text, "per_tool_source_map_count")
    per_tool_source_map_count = int(per_tool_source_map_count_value) if per_tool_source_map_count_value and per_tool_source_map_count_value.isdigit() else 0
    non_openai_value = find_key_value(text, "non_openai_tool_sources_count")
    non_openai_tool_sources_count = int(non_openai_value) if non_openai_value and non_openai_value.isdigit() else 0
    per_tool_source_map_missing = latest_or_watchlist_task and not per_tool_source_map_present
    source_breadth_lock_missing = latest_or_watchlist_task and source_breadth_status is None
    source_breadth_lock_fail = source_breadth_status == "FAIL"
    broad_watchlist_one_vendor_only = latest_or_watchlist_task and per_tool_source_map_present and non_openai_tool_sources_count == 0
    named_tool_without_source_map = explicit_false(text, "named_tool_claims_all_mapped")
    unsupported_tool_claims_missing = "unsupported_tool_claims" not in text and latest_or_watchlist_task
    exact_rule_evidence_missing = explicit_false(text, "exact_rule_evidence_present") or (
        "RULE_CONSUMPTION_EVIDENCE_LEDGER" not in text and "exact_rule_id_or_text" not in text
    )
    role_summary_only_detected = explicit_true(text, "role_summary_only_detected") or "evidence_depth=ROLE_SUMMARY" in text
    exact_rule_lineage_map_missing = explicit_false(text, "exact_rule_lineage_map_present") or "EXACT_RULE_LINEAGE_MAP" not in text
    rule_consumption_evidence_lock_missing = rule_consumption_evidence_status is None
    all_core_locks_pass = all(
        find_key_value(text, key) == "PASS"
        for key in [
            "task_route_lock_status",
            "route_dependency_expansion_lock_status",
            "consumption_lock_status",
            "source_research_lock_status",
            "quality_lock_status",
            "governance_lock_status",
        ]
    )
    depth_weak_but_downgraded = (
        (role_summary_only_detected or exact_rule_evidence_missing or exact_rule_lineage_map_missing)
        and all_core_locks_pass
        and explicit_true(text, "final_status_downgraded_if_depth_weak")
    )
    final_status_not_downgraded_when_evidence_weak = (
        (role_summary_only_detected or exact_rule_lineage_map_missing)
        and (find_key_value(text, "proof_classification") == "PASS")
        and not explicit_true(text, "final_status_downgraded_if_depth_weak")
    )
    layman_command_gateway_used = explicit_true(text, "layman_command_gateway_used")
    shadow_command_alias_detected = explicit_true(text, "shadow_command_alias_detected")
    raw_user_task_preserved = explicit_true(text, "raw_user_task_preserved")
    internal_wrapper_applied = explicit_true(text, "internal_wrapper_applied")
    alias_matrix_entry_used = explicit_true(text, "alias_matrix_entry_used")
    route_id_resolved = explicit_true(text, "route_id_resolved")
    route_manifest_loaded = explicit_true(text, "route_manifest_loaded")
    gateway_contract_loaded_before_alias = explicit_true(text, "gateway_contract_loaded_before_alias")
    output_mode_contract_loaded = explicit_true(text, "output_mode_contract_loaded")
    registry_paths_exist = explicit_true(text, "registry_paths_exist")
    route_components_exist = explicit_true(text, "route_components_exist")
    selected_components_are_registered = explicit_true(text, "selected_components_are_registered")
    provider_boundary_present = explicit_true(text, "provider_boundary_present")
    no_n8n_provider_media_execution = explicit_true(text, "no_n8n_provider_media_execution")
    compact_or_proof_output_allowed_only_after_locks = explicit_true(
        text, "compact_or_proof_output_allowed_only_after_locks"
    )
    output_mode = find_key_value(text, "output_mode")
    output_mode_valid = output_mode in VALID_OUTPUT_MODES
    operator_mode_used = explicit_true(text, "operator_mode_used") or output_mode == "OPERATOR_MODE"
    operator_mode_compact_proof_present = (
        explicit_true(text, "operator_mode_compact_proof_present")
        or all(marker in text for marker in ["Shadow Boot / Route Summary", "Gate Summary", "Compact Final Proof"])
    )
    source_summary_missing_in_operator_mode = operator_mode_used and "Source Summary" not in text and not explicit_true(
        text, "source_summary_present"
    )
    shadow_alias_without_internal_locks = shadow_command_alias_detected and not internal_wrapper_applied
    shadow_alias_without_gateway_contract = shadow_command_alias_detected and not gateway_contract_loaded_before_alias
    shadow_alias_without_alias_matrix = shadow_command_alias_detected and not alias_matrix_entry_used
    shadow_alias_without_route_resolution = shadow_command_alias_detected and not route_id_resolved
    shadow_alias_without_route_manifest_loaded = shadow_command_alias_detected and not route_manifest_loaded
    shadow_alias_without_output_mode_contract = shadow_command_alias_detected and not output_mode_contract_loaded
    shadow_alias_without_lock_gated_output = (
        shadow_command_alias_detected and not compact_or_proof_output_allowed_only_after_locks
    )
    registry_paths_missing = explicit_false(text, "registry_paths_exist") or explicit_not_true(text, "registry_paths_exist")
    route_components_missing = explicit_false(text, "route_components_exist") or explicit_not_true(
        text, "route_components_exist"
    )
    selected_components_not_registered = explicit_false(text, "selected_components_are_registered") or explicit_not_true(
        text, "selected_components_are_registered"
    )
    provider_boundary_missing = explicit_false(text, "provider_boundary_present") or explicit_not_true(
        text, "provider_boundary_present"
    )
    false_n8n_provider_media_claims = explicit_false(text, "no_n8n_provider_media_execution") or explicit_not_true(
        text, "no_n8n_provider_media_execution"
    )
    operator_mode_claims_pass_without_lock_summary = (
        operator_mode_used
        and (find_key_value(text, "proof_classification") == "PASS")
        and not operator_mode_compact_proof_present
    )
    operator_mode_missing_compact_proof = operator_mode_used and not operator_mode_compact_proof_present
    raw_plain_task_claimed_production_proof = explicit_true(text, "raw_plain_task_claimed_production_proof")

    generic_detected = any(text.lstrip().startswith(marker) for marker in GENERIC_OUTPUT_MARKERS)
    matrix_missing = "registries/native_capability_routing_matrix.yaml" not in text
    index_missing = "registries/agent_runtime_selection_index.yaml" not in text
    task_intent_matrix_missing = "registries/task_intent_routing_matrix.yaml" not in text
    route_id_missing = find_key_value(text, "route_id") in {None, ""}
    route_manifest_path_value = find_key_value(text, "route_manifest_path")
    route_manifest_path_does_not_exist = bool(route_manifest_path_value) and not Path(route_manifest_path_value).is_file()
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
        or false_onboarding_claims
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
        or per_tool_source_map_missing
        or source_breadth_lock_fail
        or broad_watchlist_one_vendor_only
        or named_tool_without_source_map
        or shadow_alias_without_internal_locks
        or shadow_alias_without_gateway_contract
        or shadow_alias_without_alias_matrix
        or shadow_alias_without_route_resolution
        or shadow_alias_without_route_manifest_loaded
        or shadow_alias_without_output_mode_contract
        or shadow_alias_without_lock_gated_output
        or registry_paths_missing
        or route_components_missing
        or selected_components_not_registered
        or provider_boundary_missing
        or false_n8n_provider_media_claims
        or route_manifest_path_does_not_exist
        or operator_mode_missing_compact_proof
        or operator_mode_claims_pass_without_lock_summary
        or raw_plain_task_claimed_production_proof
    ):
        status = "FAIL"
    elif (
        depth_weak_but_downgraded
        or source_breadth_status == "PASS_WITH_NOTICE"
        or rule_consumption_evidence_status == "PASS_WITH_NOTICE"
    ):
        status = "PASS_WITH_NOTICE"
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
        or source_breadth_lock_missing
        or rule_consumption_evidence_lock_missing
        or unsupported_tool_claims_missing
        or role_summary_only_detected
        or exact_rule_evidence_missing
        or exact_rule_lineage_map_missing
        or final_status_not_downgraded_when_evidence_weak
        or (layman_command_gateway_used and not output_mode_valid)
        or (shadow_command_alias_detected and not raw_user_task_preserved)
        or source_summary_missing_in_operator_mode
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
    print(f"false_onboarding_claim_count={len(false_onboarding_claims)}")
    for item in false_onboarding_claims:
        print(f"false_onboarding_claim={item}")
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
    print(f"per_tool_source_map_missing={str(per_tool_source_map_missing).lower()}")
    print(f"broad_watchlist_one_vendor_only={str(broad_watchlist_one_vendor_only).lower()}")
    print(f"named_tool_without_source_map={str(named_tool_without_source_map).lower()}")
    print(f"unsupported_tool_claims_missing={str(unsupported_tool_claims_missing).lower()}")
    print(f"source_breadth_lock_missing={str(source_breadth_lock_missing).lower()}")
    print(f"source_breadth_lock_fail={str(source_breadth_lock_fail).lower()}")
    print(f"rule_consumption_evidence_lock_missing={str(rule_consumption_evidence_lock_missing).lower()}")
    print(f"exact_rule_evidence_missing={str(exact_rule_evidence_missing).lower()}")
    print(f"role_summary_only_detected={str(role_summary_only_detected).lower()}")
    print(f"exact_rule_lineage_map_missing={str(exact_rule_lineage_map_missing).lower()}")
    print(f"final_status_not_downgraded_when_evidence_weak={str(final_status_not_downgraded_when_evidence_weak).lower()}")
    print(f"layman_command_gateway_used={str(layman_command_gateway_used).lower()}")
    print(f"shadow_command_alias_detected={str(shadow_command_alias_detected).lower()}")
    print(f"raw_user_task_preserved={str(raw_user_task_preserved).lower()}")
    print(f"alias_matrix_entry_used={str(alias_matrix_entry_used).lower()}")
    print(f"route_id_resolved={str(route_id_resolved).lower()}")
    print(f"route_manifest_loaded={str(route_manifest_loaded).lower()}")
    print(f"internal_wrapper_applied={str(internal_wrapper_applied).lower()}")
    print(f"gateway_contract_loaded_before_alias={str(gateway_contract_loaded_before_alias).lower()}")
    print(f"output_mode_contract_loaded={str(output_mode_contract_loaded).lower()}")
    print(f"registry_paths_exist={str(registry_paths_exist).lower()}")
    print(f"route_components_exist={str(route_components_exist).lower()}")
    print(f"selected_components_are_registered={str(selected_components_are_registered).lower()}")
    print(f"provider_boundary_present={str(provider_boundary_present).lower()}")
    print(f"no_n8n_provider_media_execution={str(no_n8n_provider_media_execution).lower()}")
    print(
        "compact_or_proof_output_allowed_only_after_locks="
        f"{str(compact_or_proof_output_allowed_only_after_locks).lower()}"
    )
    print(f"output_mode={output_mode or 'MISSING'}")
    print(f"output_mode_valid={str(output_mode_valid).lower()}")
    print(f"operator_mode_used={str(operator_mode_used).lower()}")
    print(f"operator_mode_compact_proof_present={str(operator_mode_compact_proof_present).lower()}")
    print(f"source_summary_missing_in_operator_mode={str(source_summary_missing_in_operator_mode).lower()}")
    print(f"shadow_alias_without_internal_locks={str(shadow_alias_without_internal_locks).lower()}")
    print(f"shadow_alias_without_gateway_contract={str(shadow_alias_without_gateway_contract).lower()}")
    print(f"shadow_alias_without_alias_matrix={str(shadow_alias_without_alias_matrix).lower()}")
    print(f"shadow_alias_without_route_resolution={str(shadow_alias_without_route_resolution).lower()}")
    print(f"shadow_alias_without_route_manifest_loaded={str(shadow_alias_without_route_manifest_loaded).lower()}")
    print(f"shadow_alias_without_output_mode_contract={str(shadow_alias_without_output_mode_contract).lower()}")
    print(f"shadow_alias_without_lock_gated_output={str(shadow_alias_without_lock_gated_output).lower()}")
    print(f"registry_paths_missing={str(registry_paths_missing).lower()}")
    print(f"route_components_missing={str(route_components_missing).lower()}")
    print(f"selected_components_not_registered={str(selected_components_not_registered).lower()}")
    print(f"provider_boundary_missing={str(provider_boundary_missing).lower()}")
    print(f"false_n8n_provider_media_claims={str(false_n8n_provider_media_claims).lower()}")
    print(f"route_manifest_path_does_not_exist={str(route_manifest_path_does_not_exist).lower()}")
    print(f"operator_mode_claims_pass_without_lock_summary={str(operator_mode_claims_pass_without_lock_summary).lower()}")
    print(f"operator_mode_missing_compact_proof={str(operator_mode_missing_compact_proof).lower()}")
    print(f"raw_plain_task_claimed_production_proof={str(raw_plain_task_claimed_production_proof).lower()}")
    print(f"all_core_locks_pass={str(all_core_locks_pass).lower()}")
    print(f"per_tool_source_map_count={per_tool_source_map_count}")
    print(f"non_openai_tool_sources_count={non_openai_tool_sources_count}")
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

    return 0 if status in {"PASS", "PASS_WITH_NOTICE"} and final_status_matches_weakest else 1


if __name__ == "__main__":
    raise SystemExit(main())
