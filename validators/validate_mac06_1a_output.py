#!/usr/bin/env python3
"""Validate MAC-06.1A fresh-agent output text.

Usage:
  python validators/validate_mac06_1a_output.py path/to/output.txt
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from functools import lru_cache
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
    "VALIDATION_SCORECARD",
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

PROOF_CLASSIFICATIONS = {"PASS", "NEEDS_CONFIRMATION", "PARTIAL", "FAIL"}
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

DEFAULT_REQUIRED_WRAPPER_BLOCKS = {
    "SHADOW_BOOT_CONFIRMATION",
    "TASK_ROUTE_LOCK",
    "ROUTE_DEPENDENCY_EXPANSION_LOCK",
    "ROUTE_STATE_CAPSULE",
    "READ_LEDGER_SUMMARY",
    "ROUTE_SCOPE_FILE_AUDIT",
    "CONSUMPTION_LOCK",
    "QUALITY_LOCK",
    "GOVERNANCE_LOCK",
}
ROUTE_MANIFEST_SUPPLEMENTS = {
    "SCRIPT_GENERATION": {
        "route_manifest_path": "registries/route_manifests/script_generation.yaml",
        "mandatory_output_blocks": {
            "GATE_VISIBILITY_LOG",
            "PROOF_TRACE_BUNDLE",
            "PER_TOOL_SOURCE_MAP",
            "RULE_CONSUMPTION_EVIDENCE_LEDGER",
            "EXACT_RULE_LINEAGE_MAP",
            "TOPIC_QUALITY_GATE",
            "HOOK_GENERATION_GATE",
            "SCRIPT_QUALITY_GATE",
            "CADENCE_AND_RETENTION_GATE",
            "SCRIPT_BODY_DEPTH_LOCK",
            "VALIDATION_SCORECARD",
            "LINE_BY_LINE_INFLUENCE_MAP",
            "FINAL_SCRIPT",
        },
    },
    "TOPIC_DISCOVERY": {
        "route_manifest_path": "registries/route_manifests/topic_discovery.yaml",
        "mandatory_output_blocks": {
            "topic_options",
            "scores",
            "reason",
            "approval_gate",
        },
    },
    "CONTEXT_ENGINEERING": {
        "route_manifest_path": "registries/route_manifests/context_engineering.yaml",
        "mandatory_output_blocks": {
            "VOICE_GENERATION_CONTEXT",
            "IMAGE_GENERATION_CONTEXT",
            "VIDEO_GENERATION_CONTEXT",
            "EDITING_CONTEXT",
            "PROVIDER_HANDOFF_BOUNDARY",
        },
    },
}
LOCK_TO_STATUS_KEY = {
    "TASK_ROUTE_LOCK": "task_route_lock_status",
    "ROUTE_DEPENDENCY_EXPANSION_LOCK": "route_dependency_expansion_lock_status",
    "CONSUMPTION_LOCK": "consumption_lock_status",
    "SOURCE_RESEARCH_LOCK": "source_research_lock_status",
    "QUALITY_LOCK": "quality_lock_status",
    "GOVERNANCE_LOCK": "governance_lock_status",
    "SOURCE_BREADTH_LOCK": "source_breadth_lock_status",
    "RULE_CONSUMPTION_EVIDENCE_LOCK": "rule_consumption_evidence_lock_status",
    "MEDIA_FACTORY_SYNC_LOCK": "media_factory_sync_lock_status",
}
ABSTRACT_OUTPUT_BLOCK_RULES = {
    "all content engineering sections": {
        "all_of": {
            "CONTENT_MISSION_BRIEF",
            "RESEARCH_AND_SOURCE_STATUS",
            "SCRIPT_STRUCTURE",
            "TIMED_BEAT_MAP",
            "VOICE_GENERATION_CONTEXT",
            "IMAGE_GENERATION_CONTEXT",
            "VIDEO_GENERATION_CONTEXT",
            "MUSIC_AND_SFX_CONTEXT",
            "EDITING_CONTEXT",
            "PLATFORM_PACKAGING",
        }
    },
    "approval checkpoints": {
        "any_of": {
            "SHADOW_GATE_STATUS",
            "Final Approval Gate",
            "User Approval Log",
            "APPROVAL_CHECKPOINTS",
        }
    },
    "provider boundary": {
        "any_of": {
            "PROVIDER_HANDOFF_BOUNDARY",
            "Provider Handoff Boundary",
        }
    },
}
STRUCTURED_OUTPUT_RULE_KEY_MAP = {
    "topic_discovery_core": {
        "all_of": {"topic_options", "scores", "reason", "approval_gate"},
    },
    "voice_context_core": {
        "all_of": {"VOICE_GENERATION_CONTEXT", "PROVIDER_HANDOFF_BOUNDARY"},
    },
    "avatar_video_context_core": {
        "all_of": {
            "IMAGE_GENERATION_CONTEXT",
            "VIDEO_GENERATION_CONTEXT",
            "PROVIDER_HANDOFF_BOUNDARY",
        },
    },
    "context_engineering_core": {
        "all_of": {
            "VOICE_GENERATION_CONTEXT",
            "IMAGE_GENERATION_CONTEXT",
            "VIDEO_GENERATION_CONTEXT",
            "EDITING_CONTEXT",
            "PROVIDER_HANDOFF_BOUNDARY",
        },
    },
    "editing_packaging_core": {
        "all_of": {"EDITING_CONTEXT", "PLATFORM_PACKAGING"},
    },
    "script_refinement_core": {
        "all_of": {"critique", "rewrite_decision", "SCRIPT_QUALITY_GATE"},
    },
    "all_content_engineering_sections": {
        "all_of": {
            "CONTENT_MISSION_BRIEF",
            "RESEARCH_AND_SOURCE_STATUS",
            "SCRIPT_STRUCTURE",
            "TIMED_BEAT_MAP",
            "VOICE_GENERATION_CONTEXT",
            "IMAGE_GENERATION_CONTEXT",
            "VIDEO_GENERATION_CONTEXT",
            "MUSIC_AND_SFX_CONTEXT",
            "EDITING_CONTEXT",
            "PLATFORM_PACKAGING",
        },
    },
    "approval_checkpoints_present": {
        "any_of": {"SHADOW_GATE_STATUS", "Final Approval Gate", "User Approval Log", "APPROVAL_CHECKPOINTS"},
    },
    "provider_boundary": {
        "any_of": {"PROVIDER_HANDOFF_BOUNDARY", "Provider Handoff Boundary"},
    },
    "media_factory_visual_plan_base": {
        "all_of": {
            "SCENE_SYNC_MATRIX",
            "SCENE_BREAKOUT_BLOCKS",
            "PRODUCTION_ORDER_LOCK",
            "ASSET_INVENTORY_LEDGER",
            "ASSET_DEPENDENCY_GRAPH",
            "CONTROL_PANEL_EXECUTION_PLAN",
            "DAVINCI_TIMELINE_PACKET",
            "PRODUCTION_PROOF_GATE",
            "PROVIDER_HONESTY_GATE",
        },
    },
    "media_factory_final_draft_base": {
        "all_of": {
            "SCENE_SYNC_MATRIX",
            "SCENE_BREAKOUT_BLOCKS",
            "SCENE_PROMPT_PACKETS",
            "VIDEO_PROMPT_PACKETS",
            "STORYBOARD_EXPORT_PLAN",
            "PRODUCTION_ORDER_LOCK",
            "ASSET_INVENTORY_LEDGER",
            "ASSET_DEPENDENCY_GRAPH",
            "CONTROL_PANEL_EXECUTION_PLAN",
            "DAVINCI_TIMELINE_PACKET",
            "LOCAL_MEDIA_FACTORY_BRIDGE_STATUS",
            "PRODUCTION_PROOF_GATE",
            "PROVIDER_HONESTY_GATE",
        },
    },
    "media_factory_generator_draft_base": {
        "all_of": {
            "SCENE_SYNC_MATRIX",
            "SCENE_BREAKOUT_BLOCKS",
            "SCENE_PROMPT_PACKETS",
            "VIDEO_PROMPT_PACKETS",
            "STORYBOARD_EXPORT_PLAN",
            "PRODUCTION_ORDER_LOCK",
            "ASSET_INVENTORY_LEDGER",
            "ASSET_DEPENDENCY_GRAPH",
            "MISSION_MEDIA_OUTPUT_BUNDLE",
            "VOICE_BATCH_PLAN",
            "A_ROLL_BATCH_PLAN",
            "MUSIC_SFX_BATCH_PLAN",
            "IMAGE_BATCH_PLAN",
            "CINEMATIC_BROLL_BATCH_PLAN",
            "MOTION_GRAPHICS_BATCH_PLAN",
            "ASSEMBLY_SYNC_PLAN",
            "CONTROL_PANEL_EXECUTION_PLAN",
            "DAVINCI_TIMELINE_PACKET",
            "SCENE_EXECUTION_BLOCKS",
            "LOCAL_MEDIA_FACTORY_BRIDGE_STATUS",
            "PRODUCTION_PROOF_GATE",
            "PROVIDER_HONESTY_GATE",
        },
    },
}

CURRENT_SENSITIVE_PATTERN = re.compile(r"(?i)\b(latest|current|this week|today|2026|trending|new update|source update)\b")
WATCHLIST_PATTERN = re.compile(r"(?i)\b(watchlist|tools to watch|watch this week)\b")
THREE_TO_TEN_MIN_PATTERN = re.compile(r"(?i)\b(3 ?- ?10 ?minute|5 ?minute|five minute)\b")


def contains(text: str, needle: str) -> bool:
    return needle.lower() in text.lower()


def find_key_value(text: str, key: str) -> str | None:
    matches = list(
        re.finditer(rf"(?im)^\s*[-*]?\s*`?{re.escape(key)}`?\s*=\s*([A-Za-z0-9_./:-]+)", text)
    )
    return matches[-1].group(1) if matches else None


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


def section_present(text: str, heading: str) -> bool:
    return re.search(rf"(?m)^\s*{re.escape(heading)}\s*$", text) is not None


def parse_inline_list(manifest_text: str, key: str) -> set[str]:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*\[(.+?)\]\s*$", manifest_text)
    if not match:
        return set()
    return {
        item.strip().strip("'\"")
        for item in match.group(1).split(",")
        if item.strip()
    }


def parse_block_list(manifest_text: str, key: str) -> set[str]:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*\n((?:[ \t]+-\s*[^\n]*\n)+)", manifest_text)
    if not match:
        return set()
    return {
        item.strip().strip("'\"")
        for item in re.findall(r"(?m)^\s*-\s*(.+?)\s*$", match.group(1))
        if item.strip()
    }


def parse_manifest_list(manifest_text: str, key: str) -> set[str]:
    return parse_inline_list(manifest_text, key) | parse_block_list(manifest_text, key)


def parse_manifest_scalar(manifest_text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", manifest_text)
    if not match:
        return None
    return match.group(1).strip().strip("'\"")


def parse_manifest_bool(manifest_text: str, key: str) -> bool | None:
    value = parse_manifest_scalar(manifest_text, key)
    if value is None:
        return None
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    return None


def parse_object_path_list(manifest_text: str, key: str) -> set[str]:
    match = re.search(rf"(?ms)^{re.escape(key)}:\s*\n((?:[ \t]+.+\n)+?)(?=^\S|\Z)", manifest_text)
    if not match:
        return set()
    return {
        item.strip().strip("'\"")
        for item in re.findall(r"(?m)^\s*path:\s*(.+?)\s*$", match.group(1))
        if item.strip()
    }


def parse_yaml_scalar_any_indent(manifest_text: str, key: str) -> str | None:
    match = re.search(rf"(?m)^[ \t]*{re.escape(key)}:\s*(.+?)\s*$", manifest_text)
    if not match:
        return None
    return match.group(1).strip().strip("'\"")


def parse_yaml_list_any_indent(manifest_text: str, key: str) -> set[str]:
    inline = re.search(rf"(?m)^[ \t]*{re.escape(key)}:\s*\[(.+?)\]\s*$", manifest_text)
    values: set[str] = set()
    if inline:
        values |= {
            item.strip().strip("'\"")
            for item in inline.group(1).split(",")
            if item.strip()
        }
    block = re.search(
        rf"(?m)^[ \t]*{re.escape(key)}:\s*\n((?:[ \t]+-\s*[^\n]*\n)+)",
        manifest_text,
    )
    if block:
        values |= {
            item.strip().strip("'\"")
            for item in re.findall(r"(?m)^\s*-\s*(.+?)\s*$", block.group(1))
            if item.strip()
        }
    return values


def expand_output_block_rules(blocks: set[str]) -> set[str]:
    expanded: set[str] = set()
    for block in blocks:
        rule = ABSTRACT_OUTPUT_BLOCK_RULES.get(block.lower())
        if rule:
            expanded.update(rule.get("all_of", set()))
            expanded.update(rule.get("any_of", set()))
        else:
            expanded.add(block)
    return expanded


def block_present(text: str, block: str) -> bool:
    rule = ABSTRACT_OUTPUT_BLOCK_RULES.get(block.lower())
    if not rule:
        return section_present(text, block)
    all_of = rule.get("all_of")
    any_of = rule.get("any_of")
    if all_of and not all(section_present(text, item) for item in all_of):
        return False
    if any_of:
        return any(section_present(text, item) for item in any_of)
    return bool(all_of)


def structured_rule_present(text: str, rule_key: str) -> bool:
    rule = STRUCTURED_OUTPUT_RULE_KEY_MAP.get(rule_key)
    if not rule:
        return False
    all_of = rule.get("all_of")
    any_of = rule.get("any_of")
    if all_of and not all(section_present(text, item) for item in all_of):
        return False
    if any_of:
        return any(section_present(text, item) for item in any_of)
    return bool(all_of)


def task_is_current_sensitive(text: str) -> bool:
    return bool(CURRENT_SENSITIVE_PATTERN.search(text))


def task_is_watchlist(text: str) -> bool:
    return bool(WATCHLIST_PATTERN.search(text))


def task_is_three_to_ten_min_script(text: str) -> bool:
    duration = find_key_value(text, "script_duration_minutes")
    if duration and duration.isdigit():
        minutes = int(duration)
        if 3 <= minutes <= 10:
            return True
    return bool(THREE_TO_TEN_MIN_PATTERN.search(text))


def route_manifest_inventory(repo_root: Path) -> tuple[dict[str, dict[str, object]], dict[str, str]]:
    manifests_by_route_id: dict[str, dict[str, object]] = {}
    manifests_by_path: dict[str, str] = {}
    manifest_root = repo_root / "registries/route_manifests"
    if not manifest_root.is_dir():
        return manifests_by_route_id, manifests_by_path
    for manifest_path in sorted(manifest_root.glob("*.yaml")):
        rel_path = manifest_path.relative_to(repo_root).as_posix()
        manifest_text = manifest_path.read_text(encoding="utf-8")
        route_id = parse_manifest_scalar(manifest_text, "route_id")
        if not route_id:
            continue
        manifests_by_route_id[route_id] = {
            "route_id": route_id,
            "manifest_path": rel_path,
            "mandatory_output_blocks": parse_manifest_list(manifest_text, "mandatory_output_blocks")
            | parse_manifest_list(manifest_text, "output_blocks"),
            "required_locks": parse_manifest_list(manifest_text, "required_locks"),
            "trigger_aliases": parse_manifest_list(manifest_text, "trigger_aliases"),
            "mandatory_directors": parse_manifest_list(manifest_text, "mandatory_directors")
            | parse_object_path_list(manifest_text, "mandatory_directors"),
            "mandatory_agents": parse_manifest_list(manifest_text, "mandatory_agents"),
            "mandatory_subagents": parse_manifest_list(manifest_text, "mandatory_subagents"),
            "mandatory_skills": parse_manifest_list(manifest_text, "mandatory_skills"),
            "mandatory_subskills": parse_manifest_list(manifest_text, "mandatory_subskills"),
            "validator_required_checks": parse_manifest_list(manifest_text, "validator_required_checks"),
            "structured_output_rule_keys": parse_manifest_list(manifest_text, "structured_output_rule_keys"),
            "conditional_required_locks_current_terms": parse_manifest_list(
                manifest_text, "conditional_required_locks_current_terms"
            ),
            "conditional_required_locks_watchlist": parse_manifest_list(
                manifest_text, "conditional_required_locks_watchlist"
            ),
            "conditional_required_locks_3_to_10_min_script": parse_manifest_list(
                manifest_text, "conditional_required_locks_3_to_10_min_script"
            ),
            "hard_fail_if_any_mandatory_output_block_missing": parse_manifest_bool(
                manifest_text, "hard_fail_if_any_mandatory_output_block_missing"
            ),
            "hard_fail_if_required_lock_status_not_pass": parse_manifest_bool(
                manifest_text, "hard_fail_if_required_lock_status_not_pass"
            ),
            "hard_fail_if_alias_route_id_contradiction_present": parse_manifest_bool(
                manifest_text, "hard_fail_if_alias_route_id_contradiction_present"
            ),
            "hard_fail_if_wrapper_output_order_invalid": parse_manifest_bool(
                manifest_text, "hard_fail_if_wrapper_output_order_invalid"
            ),
            "exists": True,
        }
        manifests_by_path[rel_path] = route_id
    return manifests_by_route_id, manifests_by_path


@lru_cache(maxsize=1)
def cached_route_manifest_inventory() -> tuple[dict[str, dict[str, object]], dict[str, str]]:
    return route_manifest_inventory(Path(__file__).resolve().parents[1])


def route_slice_inventory(repo_root: Path) -> tuple[dict[str, list[dict[str, object]]], dict[str, dict[str, object]]]:
    slices_by_route_id: dict[str, list[dict[str, object]]] = {}
    slices_by_path: dict[str, dict[str, object]] = {}
    slice_root = repo_root / "registries/route_slices"
    if not slice_root.is_dir():
        return slices_by_route_id, slices_by_path
    for slice_path in sorted(slice_root.glob("*.registry_slice.yaml")):
        rel_path = slice_path.relative_to(repo_root).as_posix()
        text = slice_path.read_text(encoding="utf-8")
        route_id = parse_yaml_scalar_any_indent(text, "route_id")
        metadata = {
            "slice_path": rel_path,
            "slice_id": parse_yaml_scalar_any_indent(text, "slice_id"),
            "route_id": route_id,
            "task_mode": parse_yaml_scalar_any_indent(text, "task_mode")
            or parse_yaml_scalar_any_indent(text, "default_task_mode"),
            "source_manifest": parse_yaml_scalar_any_indent(text, "source_manifest"),
            "validators": parse_yaml_list_any_indent(text, "validators"),
            "output_contracts": parse_yaml_list_any_indent(text, "output_contracts")
            | parse_yaml_list_any_indent(text, "additional_output_contracts"),
            "directors": parse_yaml_list_any_indent(text, "directors"),
            "agents": parse_yaml_list_any_indent(text, "agents"),
            "subagents": parse_yaml_list_any_indent(text, "subagents"),
            "skills": parse_yaml_list_any_indent(text, "skills"),
            "subskills": parse_yaml_list_any_indent(text, "subskills"),
            "exists": True,
        }
        slices_by_path[rel_path] = metadata
        if route_id:
            slices_by_route_id.setdefault(route_id, []).append(metadata)
    return slices_by_route_id, slices_by_path


@lru_cache(maxsize=1)
def cached_route_slice_inventory() -> tuple[dict[str, list[dict[str, object]]], dict[str, dict[str, object]]]:
    return route_slice_inventory(Path(__file__).resolve().parents[1])


def load_route_slice_metadata(
    repo_root: Path, route_id: str | None, route_manifest_path: str | None, task_mode: str | None
) -> dict[str, object]:
    slices_by_route_id, slices_by_path = cached_route_slice_inventory()
    if route_id is None:
        return {"exists": False, "expected": False}
    candidates = list(slices_by_route_id.get(route_id, []))
    if not candidates:
        return {"exists": False, "expected": False}
    if route_manifest_path:
        manifest_matches = [
            slice_metadata
            for slice_metadata in candidates
            if slice_metadata.get("source_manifest") == route_manifest_path
        ]
        if manifest_matches:
            candidates = manifest_matches
    if task_mode:
        task_matches = [
            slice_metadata
            for slice_metadata in candidates
            if slice_metadata.get("task_mode") == task_mode
        ]
        if task_matches:
            candidates = task_matches
    if not candidates:
        return {"exists": False, "expected": True}
    selected = candidates[0]
    return {
        "exists": True,
        "expected": True,
        "slice_path": selected.get("slice_path"),
        "source_manifest": selected.get("source_manifest"),
        "validators": set(selected.get("validators", set())),
        "output_contracts": set(selected.get("output_contracts", set())),
        "directors": set(selected.get("directors", set())),
        "agents": set(selected.get("agents", set())),
        "subagents": set(selected.get("subagents", set())),
        "skills": set(selected.get("skills", set())),
        "subskills": set(selected.get("subskills", set())),
    }


def registry_file_set(repo_root: Path, rel_path: str, field_name: str) -> set[str]:
    path = repo_root / rel_path
    if not path.is_file():
        return set()
    text = path.read_text(encoding="utf-8")
    return {
        item.strip()
        for item in re.findall(rf"(?m)^\s*(?:-\s*)?{re.escape(field_name)}:\s*(.+?)\s*$", text)
        if item.strip()
    }


@lru_cache(maxsize=1)
def cached_registered_agents() -> set[str]:
    repo_root = Path(__file__).resolve().parents[1]
    return registry_file_set(repo_root, "agents/AGENT_RUNTIME_REGISTRY.yaml", "file")


@lru_cache(maxsize=1)
def cached_registered_subagents() -> set[str]:
    repo_root = Path(__file__).resolve().parents[1]
    return registry_file_set(repo_root, "subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml", "file")


@lru_cache(maxsize=1)
def cached_registered_skills() -> set[str]:
    repo_root = Path(__file__).resolve().parents[1]
    return registry_file_set(repo_root, "registries/skill_registry.yaml", "file_path")


@lru_cache(maxsize=1)
def cached_registered_subskills() -> set[str]:
    repo_root = Path(__file__).resolve().parents[1]
    return registry_file_set(repo_root, "registries/subskill_runtime_registry.yaml", "spec_file")


def load_route_manifest_metadata(
    repo_root: Path, route_id: str | None, route_manifest_path: str | None
) -> dict[str, object]:
    manifests_by_route_id, manifests_by_path = cached_route_manifest_inventory()
    supplement = ROUTE_MANIFEST_SUPPLEMENTS.get(route_id or "", {})
    manifest_rel_path = route_manifest_path
    manifest_route_id = route_id or ""
    if manifest_rel_path and manifest_rel_path in manifests_by_path:
        manifest_route_id = manifests_by_path[manifest_rel_path]
    elif manifest_route_id and manifest_route_id in manifests_by_route_id:
        manifest_rel_path = str(manifests_by_route_id[manifest_route_id]["manifest_path"])
    elif supplement.get("route_manifest_path"):
        manifest_rel_path = str(supplement["route_manifest_path"])
    if not manifest_rel_path or not manifest_route_id:
        return {
            "route_id": route_id,
            "manifest_path": None,
            "mandatory_output_blocks": set(DEFAULT_REQUIRED_WRAPPER_BLOCKS),
            "required_locks": set(),
            "trigger_aliases": set(),
            "mandatory_directors": set(),
            "mandatory_agents": set(),
            "mandatory_subagents": set(),
            "mandatory_skills": set(),
            "mandatory_subskills": set(),
            "validator_required_checks": set(),
            "structured_output_rule_keys": set(),
            "conditional_required_locks_current_terms": set(),
            "conditional_required_locks_watchlist": set(),
            "conditional_required_locks_3_to_10_min_script": set(),
            "hard_fail_if_any_mandatory_output_block_missing": True,
            "hard_fail_if_required_lock_status_not_pass": True,
            "hard_fail_if_alias_route_id_contradiction_present": True,
            "hard_fail_if_wrapper_output_order_invalid": True,
            "exists": False,
        }
    manifest_metadata = manifests_by_route_id.get(manifest_route_id)
    if not manifest_metadata:
        return {
            "manifest_path": str(manifest_rel_path),
            "mandatory_output_blocks": set(DEFAULT_REQUIRED_WRAPPER_BLOCKS)
            | set(supplement.get("mandatory_output_blocks", set())),
            "required_locks": set(),
            "trigger_aliases": set(),
            "mandatory_directors": set(),
            "mandatory_agents": set(),
            "mandatory_subagents": set(),
            "mandatory_skills": set(),
            "mandatory_subskills": set(),
            "validator_required_checks": set(),
            "structured_output_rule_keys": set(),
            "conditional_required_locks_current_terms": set(),
            "conditional_required_locks_watchlist": set(),
            "conditional_required_locks_3_to_10_min_script": set(),
            "hard_fail_if_any_mandatory_output_block_missing": True,
            "hard_fail_if_required_lock_status_not_pass": True,
            "hard_fail_if_alias_route_id_contradiction_present": True,
            "hard_fail_if_wrapper_output_order_invalid": True,
            "exists": False,
        }
    return {
        "route_id": manifest_route_id,
        "manifest_path": str(manifest_rel_path),
        "mandatory_output_blocks": expand_output_block_rules(
            set(DEFAULT_REQUIRED_WRAPPER_BLOCKS)
            | set(manifest_metadata["mandatory_output_blocks"])
            | set(supplement.get("mandatory_output_blocks", set()))
        ),
        "required_locks": set(manifest_metadata["required_locks"]),
        "trigger_aliases": set(manifest_metadata["trigger_aliases"]),
        "mandatory_directors": set(manifest_metadata["mandatory_directors"]),
        "mandatory_agents": set(manifest_metadata["mandatory_agents"]),
        "mandatory_subagents": set(manifest_metadata["mandatory_subagents"]),
        "mandatory_skills": set(manifest_metadata["mandatory_skills"]),
        "mandatory_subskills": set(manifest_metadata["mandatory_subskills"]),
        "validator_required_checks": set(manifest_metadata["validator_required_checks"]),
        "structured_output_rule_keys": set(manifest_metadata["structured_output_rule_keys"]),
        "conditional_required_locks_current_terms": set(manifest_metadata["conditional_required_locks_current_terms"]),
        "conditional_required_locks_watchlist": set(manifest_metadata["conditional_required_locks_watchlist"]),
        "conditional_required_locks_3_to_10_min_script": set(
            manifest_metadata["conditional_required_locks_3_to_10_min_script"]
        ),
        "hard_fail_if_any_mandatory_output_block_missing": bool(
            manifest_metadata["hard_fail_if_any_mandatory_output_block_missing"]
        ),
        "hard_fail_if_required_lock_status_not_pass": bool(
            manifest_metadata["hard_fail_if_required_lock_status_not_pass"]
        ),
        "hard_fail_if_alias_route_id_contradiction_present": bool(
            manifest_metadata["hard_fail_if_alias_route_id_contradiction_present"]
        ),
        "hard_fail_if_wrapper_output_order_invalid": bool(
            manifest_metadata["hard_fail_if_wrapper_output_order_invalid"]
        ),
        "exists": True,
    }


def effective_required_locks(text: str, manifest_metadata: dict[str, object]) -> set[str]:
    required = set(manifest_metadata.get("required_locks", set()))
    if task_is_current_sensitive(text):
        required |= set(manifest_metadata.get("conditional_required_locks_current_terms", set()))
    if task_is_watchlist(text):
        required |= set(manifest_metadata.get("conditional_required_locks_watchlist", set()))
    if task_is_three_to_ten_min_script(text):
        required |= set(manifest_metadata.get("conditional_required_locks_3_to_10_min_script", set()))
    return required


def validator_check_failures(
    manifest_metadata: dict[str, object],
    named_checks: dict[str, bool],
) -> list[str]:
    failures: list[str] = []
    for check_name in sorted(set(manifest_metadata.get("validator_required_checks", set()))):
        if not named_checks.get(check_name, False):
            failures.append(check_name)
    return failures


def derive_quality_scores_present(text: str) -> bool:
    required = [
        "emotional_strength_score",
        "clarity_score",
        "retention_score",
        "spoken_cadence_score",
        "article_like_risk_score",
        "overall_score",
        "pass_threshold",
    ]
    return all(find_key_value(text, key) is not None for key in required)


def derive_provider_boundary_present(text: str) -> bool:
    return (
        "PROVIDER_HANDOFF_BOUNDARY" in text
        or "Provider Handoff Boundary" in text
        or find_key_value(text, "provider_boundary_present") == "true"
    )


def derive_no_provider_execution(text: str) -> bool:
    forbidden = [
        "providers_called=true",
        "n8n_used=true",
        "workflow_executed=true",
        "media_artifacts_claimed=true",
        "provider_execution_allowed=true",
    ]
    return not any(marker in text for marker in forbidden)


def derive_selected_components_are_registered(text: str, route_metadata: dict[str, object]) -> bool:
    repo_root = Path(__file__).resolve().parents[1]
    required_directors = set(
        route_metadata.get("directors", route_metadata.get("mandatory_directors", set()))
    )
    required_agents = set(
        route_metadata.get("agents", route_metadata.get("mandatory_agents", set()))
    )
    required_subagents = set(
        route_metadata.get("subagents", route_metadata.get("mandatory_subagents", set()))
    )
    required_skills = set(
        route_metadata.get("skills", route_metadata.get("mandatory_skills", set()))
    )
    required_subskills = set(
        route_metadata.get("subskills", route_metadata.get("mandatory_subskills", set()))
    )

    def all_present(paths: set[str]) -> bool:
        return all(path in text for path in paths)

    def all_exist(paths: set[str]) -> bool:
        return all((repo_root / path).is_file() for path in paths)

    skill_registry = cached_registered_skills()
    registered_skill_or_repo_skill = all(
        (path in skill_registry) or path.startswith(".agents/skills/") or (repo_root / path).is_file()
        for path in required_skills
    )

    return (
        all_present(required_directors | required_agents | required_subagents | required_skills | required_subskills)
        and all_exist(required_directors)
        and required_agents.issubset(cached_registered_agents())
        and required_subagents.issubset(cached_registered_subagents())
        and registered_skill_or_repo_skill
        and required_subskills.issubset(cached_registered_subskills())
    )


def route_alias_matches_text(text: str, manifest_metadata: dict[str, object]) -> bool:
    aliases = list(manifest_metadata.get("trigger_aliases", set()))
    return any(alias in text for alias in aliases)


def check_required_lock_statuses(text: str, required_locks: set[str]) -> list[str]:
    failures: list[str] = []
    for lock_name in sorted(required_locks):
        status_key = LOCK_TO_STATUS_KEY.get(lock_name)
        if not status_key:
            continue
        if find_key_value(text, status_key) != "PASS":
            failures.append(f"{status_key}!=PASS")
    return failures


def ordered_positions(text: str, items: list[str]) -> list[tuple[str, int]]:
    positions: list[tuple[str, int]] = []
    for item in items:
        pos = text.find(item)
        if pos >= 0:
            positions.append((item, pos))
    return positions


def wrapper_output_order_failures(text: str) -> list[str]:
    order = [
        "SHADOW_BOOT_CONFIRMATION",
        "TASK_ROUTE_LOCK",
        "ROUTE_DEPENDENCY_EXPANSION_LOCK",
        "ROUTE_STATE_CAPSULE",
        "READ_LEDGER_SUMMARY",
        "ROUTE_SCOPE_FILE_AUDIT",
        "CONSUMPTION_LOCK",
        "SOURCE_RESEARCH_LOCK",
        "QUALITY_LOCK",
        "GOVERNANCE_LOCK",
        "DIRECTOR_CONSUMPTION_LEDGER",
        "AGENT_CONSUMPTION_LEDGER",
        "SUBAGENT_CONSUMPTION_LEDGER",
        "SKILL_CONSUMPTION_LEDGER",
        "SUBSKILL_CONSUMPTION_LEDGER",
    ]
    failures: list[str] = []
    positions = ordered_positions(text, order)
    for (left_name, left_pos), (right_name, right_pos) in zip(positions, positions[1:]):
        if left_pos > right_pos:
            failures.append(f"{left_name}_after_{right_name}")
    return failures


def derive_route_scope_complete(text: str) -> bool:
    return (
        "ROUTE_SCOPE_FILE_AUDIT" in text
        and find_key_value(text, "route_manifest_read") == "true"
        and find_key_value(text, "route_scope_complete") == "true"
    )


def derive_script_generated_after_all_locks(text: str) -> bool:
    positions = [pos for pos in [text.find("FINAL_SCRIPT"), text.find("Final script")] if pos >= 0]
    script_pos = min(positions, default=-1)
    if script_pos < 0:
        return False
    required = [
        "TASK_ROUTE_LOCK",
        "ROUTE_DEPENDENCY_EXPANSION_LOCK",
        "CONSUMPTION_LOCK",
        "QUALITY_LOCK",
        "GOVERNANCE_LOCK",
    ]
    return all(text.find(marker) >= 0 and text.find(marker) < script_pos for marker in required)


def run_json_command(repo_root: Path, args: list[str]) -> tuple[bool, dict]:
    try:
        proc = subprocess.run(
            args,
            cwd=repo_root,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=20,
        )
        data = json.loads(proc.stdout)
        return proc.returncode == 0 and data.get("pass") is True, data
    except Exception as exc:
        return False, {"error": str(exc), "command": args}


def structural_runtime_status() -> dict[str, bool]:
    repo_root = Path(__file__).resolve().parents[1]
    routes = [
        "topic_discovery",
        "research_synthesis",
        "script_generation",
        "script_debate",
        "script_refinement",
        "final_script_shaping",
        "context_engineering",
        "voice_context",
        "visual_context",
        "video_context",
        "music_sfx_context",
        "editing_packaging",
        "provider_handoff",
        "media_quality_gate",
        "lineage",
        "approval",
    ]

    route_results = [
        run_json_command(repo_root, ["python3", "tools/shadow_runtime/route_graph_builder.py", "--route", route])[0]
        for route in routes
    ]
    vein_results = [
        run_json_command(repo_root, ["python3", "tools/shadow_runtime/communication_vein_validator.py", "--route", route])[0]
        for route in routes
    ]
    flow_results = [
        run_json_command(repo_root, ["python3", "tools/shadow_runtime/packet_flow_runner.py", "--route", route, "--dry-run"])[0]
        for route in routes
    ]
    packet_ok, _ = run_json_command(repo_root, ["python3", "tools/shadow_runtime/schema_rationalizer.py"])
    provider_ok, _ = run_json_command(repo_root, ["python3", "tools/shadow_runtime/provider_boundary_validator.py", "--route", "script_generation"])
    quality_ok, _ = run_json_command(
        repo_root,
        [
            "python3",
            "tools/shadow_runtime/quality_scorecard_runtime.py",
            "--scorecard",
            "tests/shadow_runtime/fixtures/quality/scorecard.valid.json",
        ],
    )
    lifecycle_ok, lifecycle_data = run_json_command(repo_root, ["python3", "tools/shadow_runtime/shadow_cli.py", "validate-lifecycle"])
    lineage_ok = (repo_root / "runtime_state/lineage_store.json").exists() and (
        repo_root / "runtime_state/approval_store.json"
    ).exists()

    return {
        "route_dag_validation_pass": all(route_results),
        "packet_schema_validation_pass": packet_ok,
        "packet_flow_validation_pass": all(flow_results),
        "communication_vein_validation_pass": all(vein_results),
        "lifecycle_validation_pass": lifecycle_ok and not lifecycle_data.get("active_not_consumed"),
        "lineage_approval_validation_pass": lineage_ok,
        "quality_scorecard_validation_pass": quality_ok,
        "provider_boundary_validation_pass": provider_ok,
        "fake_depth_detected": not lifecycle_ok,
        "contract_only_detected": not all(vein_results),
        "text_label_only_detected": False,
    }


def collect_invalid_research_modes(text: str) -> list[str]:
    modes = re.findall(r"(?im)^\s*[-*]?\s*`?research_mode`?\s*=\s*([A-Za-z0-9_]+)", text)
    return [mode for mode in modes if mode not in CANONICAL_RESEARCH_MODES]


def collect_invalid_gate_values(text: str) -> list[str]:
    values = re.findall(r"(?im)^\s*[-*]?\s*`?(?:current_status|gate_status)`?\s*=\s*([A-Z_]+)", text)
    return [value for value in values if value not in GATE_STATUSES]


def _validate_text(text: str) -> int:
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
    route_id_value = find_key_value(text, "route_id")
    task_mode_value = find_key_value(text, "task_mode")
    route_manifest_path_value = find_key_value(text, "route_manifest_path")
    route_manifest_unread = explicit_false(text, "route_manifest_read")
    route_manifest_missing = route_manifest_path_value in {None, ""} or route_manifest_unread
    route_dependency_expansion_lock_missing = "ROUTE_DEPENDENCY_EXPANSION_LOCK" not in text or explicit_false(text, "route_dependency_expansion_lock_present")
    route_scope_incomplete = not derive_route_scope_complete(text)
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
    manifest_metadata = load_route_manifest_metadata(
        Path(__file__).resolve().parents[1],
        route_id_value,
        route_manifest_path_value,
    )
    route_slice_metadata = load_route_slice_metadata(
        Path(__file__).resolve().parents[1],
        route_id_value,
        route_manifest_path_value,
        task_mode_value,
    )
    resolved_required_locks = effective_required_locks(text, manifest_metadata)
    all_core_locks_pass = not check_required_lock_statuses(text, resolved_required_locks)
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
    selected_components_not_registered = False
    provider_boundary_missing = False
    false_n8n_provider_media_claims = False
    operator_mode_claims_pass_without_lock_summary = (
        operator_mode_used
        and (find_key_value(text, "proof_classification") == "PASS")
        and not operator_mode_compact_proof_present
    )
    operator_mode_missing_compact_proof = operator_mode_used and not operator_mode_compact_proof_present
    raw_plain_task_claimed_production_proof = explicit_true(text, "raw_plain_task_claimed_production_proof")
    component_depth_validation_required = True
    universal_component_contract_present = explicit_true(text, "universal_component_contract_present") or (
        "runtime_contracts/UNIVERSAL_COMPONENT_CONTRACT_STANDARD.md" in text
    )
    component_selected_but_not_consumed = explicit_true(text, "component_selected_but_not_consumed")
    selected_component_missing_input_schema = explicit_true(text, "selected_component_missing_input_schema")
    selected_component_missing_output_schema = explicit_true(text, "selected_component_missing_output_schema")
    selected_component_missing_communication_pointer = explicit_true(
        text, "selected_component_missing_communication_pointer"
    )
    selected_component_missing_validator_binding = explicit_true(text, "selected_component_missing_validator_binding")
    selected_component_missing_fallback = explicit_true(text, "selected_component_missing_fallback")
    script_segment_packet_present = explicit_true(text, "script_segment_packet_present")
    voice_context_packet_present = explicit_true(text, "voice_context_packet_present")
    visual_context_packet_present = explicit_true(text, "visual_context_packet_present")
    video_context_packet_present = explicit_true(text, "video_context_packet_present")
    music_sfx_packet_present = explicit_true(text, "music_sfx_packet_present")
    editing_timeline_packet_present = explicit_true(text, "editing_timeline_packet_present")
    provider_handoff_packet_present = explicit_true(text, "provider_handoff_packet_present")
    media_quality_gate_packet_present = explicit_true(text, "media_quality_gate_packet_present")
    lineage_approval_packet_present = explicit_true(text, "lineage_approval_packet_present")
    quality_scores_present = derive_quality_scores_present(text)
    segment_level_regeneration_actions_present = explicit_true(
        text, "segment_level_regeneration_actions_present"
    )
    runtime_structure_validation_required = True
    structural_status = structural_runtime_status()
    route_dag_validation_pass = structural_status.get("route_dag_validation_pass", not explicit_false(text, "route_dag_validation_pass")) and not explicit_false(text, "route_dag_validation_pass")
    packet_schema_validation_pass = structural_status.get("packet_schema_validation_pass", not explicit_false(text, "packet_schema_validation_pass")) and not explicit_false(text, "packet_schema_validation_pass")
    packet_flow_validation_pass = structural_status.get("packet_flow_validation_pass", not explicit_false(text, "packet_flow_validation_pass")) and not explicit_false(text, "packet_flow_validation_pass")
    communication_vein_validation_pass = structural_status.get("communication_vein_validation_pass", not explicit_false(text, "communication_vein_validation_pass")) and not explicit_false(text, "communication_vein_validation_pass")
    lifecycle_validation_pass = structural_status.get("lifecycle_validation_pass", not explicit_false(text, "lifecycle_validation_pass")) and not explicit_false(text, "lifecycle_validation_pass")
    lineage_approval_validation_pass = structural_status.get("lineage_approval_validation_pass", not explicit_false(text, "lineage_approval_validation_pass")) and not explicit_false(text, "lineage_approval_validation_pass")
    quality_scorecard_validation_pass = structural_status.get("quality_scorecard_validation_pass", not explicit_false(text, "quality_scorecard_validation_pass")) and not explicit_false(text, "quality_scorecard_validation_pass")
    provider_boundary_validation_pass = structural_status.get("provider_boundary_validation_pass", not explicit_false(text, "provider_boundary_validation_pass")) and not explicit_false(text, "provider_boundary_validation_pass")
    fake_depth_detected = structural_status.get("fake_depth_detected", False) or explicit_true(text, "fake_depth_detected")
    contract_only_detected = structural_status.get("contract_only_detected", False) or explicit_true(text, "contract_only_detected")
    text_label_only_detected = structural_status.get("text_label_only_detected", False) or explicit_true(text, "text_label_only_detected")
    component_template_only_shallow = explicit_true(text, "component_template_only_shallow")
    active_component_unknown_needs_review = explicit_true(text, "active_component_unknown_needs_review")
    generic_input_output_packets = explicit_true(text, "generic_input_output_packets")
    pointer_file_only_no_pointer_id = explicit_true(text, "pointer_file_only_no_pointer_id")
    component_registry_all_needs_review = explicit_true(text, "component_registry_all_needs_review")
    article_pipeline_contract_only_not_route_connected = explicit_true(
        text, "article_pipeline_contract_only_not_route_connected"
    )
    active_component_missing_route_profile = explicit_true(text, "active_component_missing_route_profile")
    active_component_missing_provider_boundary = explicit_true(text, "active_component_missing_provider_boundary")
    active_component_missing_lineage = explicit_true(text, "active_component_missing_lineage")

    runtime_structure_failure = runtime_structure_validation_required and (
        not route_dag_validation_pass
        or not packet_schema_validation_pass
        or not packet_flow_validation_pass
        or not communication_vein_validation_pass
        or not lifecycle_validation_pass
        or not lineage_approval_validation_pass
        or not quality_scorecard_validation_pass
        or not provider_boundary_validation_pass
        or fake_depth_detected
        or contract_only_detected
        or text_label_only_detected
    )
    component_depth_failure = component_depth_validation_required and (
        not universal_component_contract_present
        or component_selected_but_not_consumed
        or selected_component_missing_input_schema
        or selected_component_missing_output_schema
        or selected_component_missing_communication_pointer
        or selected_component_missing_validator_binding
        or selected_component_missing_fallback
        or not script_segment_packet_present
        or not voice_context_packet_present
        or not visual_context_packet_present
        or not video_context_packet_present
        or not music_sfx_packet_present
        or not editing_timeline_packet_present
        or not provider_handoff_packet_present
        or not media_quality_gate_packet_present
        or not lineage_approval_packet_present
        or not quality_scores_present
        or not segment_level_regeneration_actions_present
        or component_template_only_shallow
        or active_component_unknown_needs_review
        or generic_input_output_packets
        or pointer_file_only_no_pointer_id
        or component_registry_all_needs_review
        or article_pipeline_contract_only_not_route_connected
        or active_component_missing_route_profile
        or active_component_missing_provider_boundary
        or active_component_missing_lineage
    )

    generic_detected = any(text.lstrip().startswith(marker) for marker in GENERIC_OUTPUT_MARKERS)
    matrix_missing = "registries/native_capability_routing_matrix.yaml" not in text
    index_missing = "registries/agent_runtime_selection_index.yaml" not in text
    task_intent_matrix_missing = "registries/task_intent_routing_matrix.yaml" not in text
    route_id_missing = route_id_value in {None, ""}
    derived_selected_components_are_registered = derive_selected_components_are_registered(
        text, manifest_metadata
    )
    selected_components_are_registered = derived_selected_components_are_registered
    selected_components_not_registered = not derived_selected_components_are_registered
    route_slice_loaded = bool(route_slice_metadata.get("exists"))
    route_slice_expected = bool(route_slice_metadata.get("expected"))
    route_slice_source_manifest_matches_route_manifest = (
        not route_slice_loaded
        or route_slice_metadata.get("source_manifest") == manifest_metadata.get("manifest_path")
    )
    route_slice_output_contracts = set(route_slice_metadata.get("output_contracts", set()))
    route_slice_output_contracts_present = (
        not route_slice_loaded
        or all(block_present(text, contract) for contract in route_slice_output_contracts)
    )
    current_validator_rel = Path(__file__).relative_to(Path(__file__).resolve().parents[1]).as_posix()
    route_slice_validator_binding_present = (
        not route_slice_loaded
        or current_validator_rel in set(route_slice_metadata.get("validators", set()))
        or route_id_value == "SCRIPT_GENERATION"
    )
    derived_provider_boundary_present = derive_provider_boundary_present(text)
    provider_boundary_present = derived_provider_boundary_present
    provider_boundary_missing = not derived_provider_boundary_present
    derived_no_n8n_provider_media_execution = derive_no_provider_execution(text)
    no_n8n_provider_media_execution = derived_no_n8n_provider_media_execution
    false_n8n_provider_media_claims = not derived_no_n8n_provider_media_execution
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
    manifest_required_blocks = set(manifest_metadata["mandatory_output_blocks"])
    manifest_missing_blocks = sorted(
        block for block in manifest_required_blocks if not block_present(text, block)
    )
    manifest_required_blocks_missing = bool(manifest_missing_blocks)
    manifest_exists_for_route = bool(manifest_metadata["exists"])
    required_lock_status_failures = check_required_lock_statuses(text, resolved_required_locks)
    route_alias_route_id_mismatch = (
        shadow_command_alias_detected and not route_alias_matches_text(text, manifest_metadata)
    )
    wrapper_order_failures = wrapper_output_order_failures(text)
    wrapper_output_order_invalid = bool(wrapper_order_failures)
    structured_rule_failures = sorted(
        rule_key
        for rule_key in set(manifest_metadata.get("structured_output_rule_keys", set()))
        if not structured_rule_present(text, rule_key)
    )
    named_check_state_base = {
        "shadow_command_alias_detected": shadow_command_alias_detected,
        "internal_wrapper_applied": internal_wrapper_applied,
        "route_manifest_loaded": route_manifest_loaded,
        "route_slice_loaded": route_slice_loaded,
        "route_slice_source_manifest_matches_route_manifest": route_slice_source_manifest_matches_route_manifest,
        "route_slice_output_contracts_present": route_slice_output_contracts_present,
        "route_slice_validator_binding_present": route_slice_validator_binding_present,
        "provider_boundary_present": derived_provider_boundary_present,
        "no_n8n_provider_media_execution": derived_no_n8n_provider_media_execution,
        "topic_options_present": section_present(text, "topic_options"),
        "topic_scores_present": section_present(text, "scores") and section_present(text, "reason"),
        "approval_gate_present": section_present(text, "approval_gate"),
        "voice_generation_context_present": section_present(text, "VOICE_GENERATION_CONTEXT"),
        "image_generation_context_present": section_present(text, "IMAGE_GENERATION_CONTEXT"),
        "video_generation_context_present": section_present(text, "VIDEO_GENERATION_CONTEXT"),
        "editing_context_present": section_present(text, "EDITING_CONTEXT"),
        "platform_packaging_present": section_present(text, "PLATFORM_PACKAGING"),
        "critique_present": section_present(text, "critique"),
        "rewrite_decision_present": section_present(text, "rewrite_decision"),
        "script_quality_gate_present": "SCRIPT_QUALITY_GATE" in text,
        "scene_sync_matrix_present": section_present(text, "SCENE_SYNC_MATRIX"),
        "production_order_lock_present": section_present(text, "PRODUCTION_ORDER_LOCK"),
        "asset_dependency_graph_present": section_present(text, "ASSET_DEPENDENCY_GRAPH"),
        "control_panel_execution_plan_present": section_present(text, "CONTROL_PANEL_EXECUTION_PLAN"),
        "davinci_timeline_packet_present": section_present(text, "DAVINCI_TIMELINE_PACKET"),
        "scene_breakout_blocks_present": section_present(text, "SCENE_BREAKOUT_BLOCKS"),
        "production_proof_gate_present": section_present(text, "PRODUCTION_PROOF_GATE"),
        "local_media_factory_bridge_status_present": section_present(text, "LOCAL_MEDIA_FACTORY_BRIDGE_STATUS"),
        "provider_honesty_gate_present": section_present(text, "PROVIDER_HONESTY_GATE"),
        "content_engineering_sections_present": structured_rule_present(text, "all_content_engineering_sections"),
        "approval_checkpoints_present": structured_rule_present(text, "approval_checkpoints_present"),
    }
    pre_status_validator_required_check_failures = validator_check_failures(
        {
            "validator_required_checks": set(
                manifest_metadata.get("validator_required_checks", set())
            )
            - {"weakest_layer_status_respected"}
        },
        named_check_state_base,
    )
    selected_components_claim_contradicted = (
        explicit_true(text, "selected_components_are_registered")
        and not derived_selected_components_are_registered
    )
    quality_scores_claim_contradicted = (
        explicit_true(text, "quality_scores_present") and not quality_scores_present
    )
    provider_boundary_claim_contradicted = (
        explicit_true(text, "provider_boundary_present") and not derived_provider_boundary_present
    )
    provider_execution_claim_contradicted = (
        explicit_true(text, "no_n8n_provider_media_execution")
        and not derived_no_n8n_provider_media_execution
    )
    script_generated_after_all_locks_claim_contradicted = (
        explicit_true(text, "script_generated_after_all_locks")
        and not derive_script_generated_after_all_locks(text)
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
        or quality_gate_without_threshold
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
        or (route_slice_expected and not route_slice_loaded)
        or (route_slice_loaded and not route_slice_source_manifest_matches_route_manifest)
        or (route_slice_loaded and not route_slice_output_contracts_present)
        or (route_slice_loaded and not route_slice_validator_binding_present)
        or provider_boundary_missing
        or false_n8n_provider_media_claims
        or route_manifest_path_does_not_exist
        or not manifest_exists_for_route
        or operator_mode_missing_compact_proof
        or operator_mode_claims_pass_without_lock_summary
        or raw_plain_task_claimed_production_proof
        or (
            manifest_metadata["hard_fail_if_any_mandatory_output_block_missing"]
            and (manifest_required_blocks_missing or bool(structured_rule_failures))
        )
        or (
            manifest_metadata["hard_fail_if_required_lock_status_not_pass"]
            and required_lock_status_failures
        )
        or bool(pre_status_validator_required_check_failures)
        or (
            manifest_metadata["hard_fail_if_alias_route_id_contradiction_present"]
            and route_alias_route_id_mismatch
        )
        or (
            manifest_metadata["hard_fail_if_wrapper_output_order_invalid"]
            and wrapper_output_order_invalid
        )
        or selected_components_claim_contradicted
        or quality_scores_claim_contradicted
        or provider_boundary_claim_contradicted
        or provider_execution_claim_contradicted
        or script_generated_after_all_locks_claim_contradicted
        or component_depth_failure
        or runtime_structure_failure
    ):
        status = "FAIL"
    elif (
        depth_weak_but_downgraded
        or source_breadth_status == "NEEDS_CONFIRMATION"
        or rule_consumption_evidence_status == "NEEDS_CONFIRMATION"
    ):
        status = "NEEDS_CONFIRMATION"
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
    named_check_state = dict(named_check_state_base)
    named_check_state["weakest_layer_status_respected"] = final_status_matches_weakest
    validator_required_check_failures = validator_check_failures(manifest_metadata, named_check_state)
    if status == "PASS" and validator_required_check_failures:
        status = "FAIL"

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
    print(f"route_slice_loaded={str(route_slice_loaded).lower()}")
    print(
        "route_slice_source_manifest_matches_route_manifest="
        f"{str(route_slice_source_manifest_matches_route_manifest).lower()}"
    )
    print(
        "route_slice_output_contracts_present="
        f"{str(route_slice_output_contracts_present).lower()}"
    )
    print(
        "route_slice_validator_binding_present="
        f"{str(route_slice_validator_binding_present).lower()}"
    )
    print(f"provider_boundary_present={str(provider_boundary_present).lower()}")
    print(f"no_n8n_provider_media_execution={str(no_n8n_provider_media_execution).lower()}")
    print(f"manifest_required_blocks_missing={str(manifest_required_blocks_missing).lower()}")
    print(f"manifest_missing_blocks_count={len(manifest_missing_blocks)}")
    for item in manifest_missing_blocks:
        print(f"manifest_missing_block={item}")
    print(f"structured_rule_failure_count={len(structured_rule_failures)}")
    for item in structured_rule_failures:
        print(f"structured_rule_failure={item}")
    print(f"manifest_exists_for_route={str(manifest_exists_for_route).lower()}")
    print(f"required_lock_status_failure_count={len(required_lock_status_failures)}")
    for item in required_lock_status_failures:
        print(f"required_lock_status_failure={item}")
    print(f"validator_required_check_failure_count={len(validator_required_check_failures)}")
    for item in validator_required_check_failures:
        print(f"validator_required_check_failure={item}")
    print(f"route_alias_route_id_mismatch={str(route_alias_route_id_mismatch).lower()}")
    print(f"wrapper_output_order_invalid={str(wrapper_output_order_invalid).lower()}")
    print(f"wrapper_output_order_failure_count={len(wrapper_order_failures)}")
    for item in wrapper_order_failures:
        print(f"wrapper_output_order_failure={item}")
    print(f"selected_components_claim_contradicted={str(selected_components_claim_contradicted).lower()}")
    print(f"quality_scores_claim_contradicted={str(quality_scores_claim_contradicted).lower()}")
    print(f"provider_boundary_claim_contradicted={str(provider_boundary_claim_contradicted).lower()}")
    print(f"provider_execution_claim_contradicted={str(provider_execution_claim_contradicted).lower()}")
    print(
        "script_generated_after_all_locks_claim_contradicted="
        f"{str(script_generated_after_all_locks_claim_contradicted).lower()}"
    )
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
    print(f"component_depth_validation_required={str(component_depth_validation_required).lower()}")
    print(f"universal_component_contract_present={str(universal_component_contract_present).lower()}")
    print(f"component_selected_but_not_consumed={str(component_selected_but_not_consumed).lower()}")
    print(f"selected_component_missing_input_schema={str(selected_component_missing_input_schema).lower()}")
    print(f"selected_component_missing_output_schema={str(selected_component_missing_output_schema).lower()}")
    print(
        "selected_component_missing_communication_pointer="
        f"{str(selected_component_missing_communication_pointer).lower()}"
    )
    print(f"selected_component_missing_validator_binding={str(selected_component_missing_validator_binding).lower()}")
    print(f"selected_component_missing_fallback={str(selected_component_missing_fallback).lower()}")
    print(f"script_segment_packet_present={str(script_segment_packet_present).lower()}")
    print(f"voice_context_packet_present={str(voice_context_packet_present).lower()}")
    print(f"visual_context_packet_present={str(visual_context_packet_present).lower()}")
    print(f"video_context_packet_present={str(video_context_packet_present).lower()}")
    print(f"music_sfx_packet_present={str(music_sfx_packet_present).lower()}")
    print(f"editing_timeline_packet_present={str(editing_timeline_packet_present).lower()}")
    print(f"provider_handoff_packet_present={str(provider_handoff_packet_present).lower()}")
    print(f"media_quality_gate_packet_present={str(media_quality_gate_packet_present).lower()}")
    print(f"lineage_approval_packet_present={str(lineage_approval_packet_present).lower()}")
    print(f"quality_scores_present={str(quality_scores_present).lower()}")
    print(
        "segment_level_regeneration_actions_present="
        f"{str(segment_level_regeneration_actions_present).lower()}"
    )
    print(f"component_template_only_shallow={str(component_template_only_shallow).lower()}")
    print(f"active_component_unknown_needs_review={str(active_component_unknown_needs_review).lower()}")
    print(f"generic_input_output_packets={str(generic_input_output_packets).lower()}")
    print(f"pointer_file_only_no_pointer_id={str(pointer_file_only_no_pointer_id).lower()}")
    print(f"component_registry_all_needs_review={str(component_registry_all_needs_review).lower()}")
    print(
        "article_pipeline_contract_only_not_route_connected="
        f"{str(article_pipeline_contract_only_not_route_connected).lower()}"
    )
    print(f"active_component_missing_route_profile={str(active_component_missing_route_profile).lower()}")
    print(f"active_component_missing_provider_boundary={str(active_component_missing_provider_boundary).lower()}")
    print(f"active_component_missing_lineage={str(active_component_missing_lineage).lower()}")
    print(f"route_dag_validation_pass={str(route_dag_validation_pass).lower()}")
    print(f"packet_schema_validation_pass={str(packet_schema_validation_pass).lower()}")
    print(f"packet_flow_validation_pass={str(packet_flow_validation_pass).lower()}")
    print(f"communication_vein_validation_pass={str(communication_vein_validation_pass).lower()}")
    print(f"lifecycle_validation_pass={str(lifecycle_validation_pass).lower()}")
    print(f"lineage_approval_validation_pass={str(lineage_approval_validation_pass).lower()}")
    print(f"quality_scorecard_validation_pass={str(quality_scorecard_validation_pass).lower()}")
    print(f"provider_boundary_validation_pass={str(provider_boundary_validation_pass).lower()}")
    print(f"fake_depth_detected={str(fake_depth_detected).lower()}")
    print(f"contract_only_detected={str(contract_only_detected).lower()}")
    print(f"text_label_only_detected={str(text_label_only_detected).lower()}")
    print(f"runtime_structure_validation_required={str(runtime_structure_validation_required).lower()}")
    print(f"runtime_structure_failure={str(runtime_structure_failure).lower()}")
    print(f"component_depth_failure={str(component_depth_failure).lower()}")
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

    return 0 if status in {"PASS", "NEEDS_CONFIRMATION"} and final_status_matches_weakest else 1


def main_with_path(path: Path) -> int:
    return _validate_text(path.read_text(errors="replace"))


def run_self_test() -> int:
    cases = [
        (
            "script_route_valid_minimal",
            """
SHADOW_BOOT_CONFIRMATION
AGENTS.md
shadow_boot_confirmation_present=true
first_visible_output_is_boot_confirmation=true
agents_md_detected=true
agents_md_read=true
repo_first_orchestration_started=true
layman_task_trigger_contract_read=true
generic_direct_answer_avoided=true
shadow_mode=CHAT_ONLY_MODE
NATIVE_AGENT_CAPABILITY_ASSESSMENT
TASK_FRESHNESS_CLASSIFICATION
RESEARCH_MODE_DECISION
Research Sufficiency Gate
TASK_TO_CAPABILITY_ROUTING
registries/native_capability_routing_matrix.yaml
task_intent_classified=true
task_intent_routing_matrix_cited=true
route_id=SCRIPT_GENERATION
registries/task_intent_routing_matrix.yaml
director_skill_consumption_protocol_read=true
script_quality_enforcement_contract_read=true
gumloop_benchmark_output_standard_read=true
task_execution_state_machine_contract_read=true
route_dependency_expansion_protocol_read=true
runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md
runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md
route_manifest_path=registries/route_manifests/script_generation.yaml
route_manifest_read=true
route_dependency_expansion_lock_present=true
route_scope_complete=true
mandatory_files_read_before_output=true
script_generated_after_all_locks=true
director_consumption_ledger_present=true
agent_consumption_ledger_present=true
subagent_consumption_ledger_present=true
skill_consumption_ledger_present=true
subskill_consumption_ledger_present=true
line_by_line_influence_map_present=true
topic_quality_gate_present=true
hook_generation_gate_present=true
script_quality_gate_present=true
shallow_repo_routing_detected=false
chat_only_mode_used=true
files_created=false
dossier_artifacts_created=false
plain_post_bootstrap_task_failed=false
shadow_task_execution_wrapper_read=true
wrapper_required_mode_used=true
codex_cloud_reliable_mode=WRAPPER_REQUIRED_COMPATIBLE
layman_command_gateway_used=true
shadow_command_alias_detected=true
raw_user_task_preserved=true
alias_matrix_entry_used=true
route_id_resolved=true
route_manifest_loaded=true
internal_wrapper_applied=true
gateway_contract_loaded_before_alias=true
output_mode_contract_loaded=true
output_mode=OPERATOR_MODE
operator_mode_used=true
operator_mode_compact_proof_present=true
compact_or_proof_output_allowed_only_after_locks=true
registry_paths_exist=true
route_components_exist=true
provider_boundary_present=true
no_n8n_provider_media_execution=true
selected_components_are_registered=true
selected_components_without_read_before_output=false
loaded_true_but_not_consumed_detected=false
manual_rerun_structured_but_partial_detected=false
exact_rule_evidence_present=true
exact_rule_lineage_map_present=true
per_tool_source_map_present=true
universal_component_contract_present=true
script_segment_packet_present=true
voice_context_packet_present=true
visual_context_packet_present=true
video_context_packet_present=true
music_sfx_packet_present=true
editing_timeline_packet_present=true
provider_handoff_packet_present=true
media_quality_gate_packet_present=true
lineage_approval_packet_present=true
segment_level_regeneration_actions_present=true
task_route_lock_status=PASS
route_dependency_expansion_lock_status=PASS
consumption_lock_status=PASS
source_research_lock_status=PASS
source_breadth_lock_status=PASS
rule_consumption_evidence_lock_status=PASS
quality_lock_status=PASS
governance_lock_status=PASS
Shadow script: write a youtube script
TASK_ROUTE_LOCK
ROUTE_DEPENDENCY_EXPANSION_LOCK
ROUTE_STATE_CAPSULE
READ_LEDGER_SUMMARY
ROUTE_SCOPE_FILE_AUDIT
CONSUMPTION_LOCK
SOURCE_RESEARCH_LOCK
SOURCE_BREADTH_LOCK
RULE_CONSUMPTION_EVIDENCE_LOCK
SOURCE_INTEGRITY_GATE
QUALITY_LOCK
RECURRING_HOOK_DENSITY_LOCK
GOVERNANCE_LOCK
DIRECTOR_CONSUMPTION_LEDGER
AGENT_CONSUMPTION_LEDGER
SUBAGENT_CONSUMPTION_LEDGER
SKILL_CONSUMPTION_LEDGER
SUBSKILL_CONSUMPTION_LEDGER
Registry-First Route
Director Selection
AGENT_RUNTIME_SELECTION
registries/agent_runtime_selection_index.yaml
Subagent Selection
Skill Selection
Subskill Selection
TOOLS_CONNECTORS_PLUGINS_ASSESSMENT
SHADOW_MISSION_PACKET
SCRIPT_LANGUAGE_DECLARATION
USER_LANGUAGE_REQUEST_CHECK
CONTENT_MISSION_BRIEF
RESEARCH_AND_SOURCE_STATUS
SOURCE_LEDGER
SOURCE_LIMITATION_NOTES
FACT_VS_ANECDOTE_MAP
CLAIM_EVIDENCE_STATUS
TOPIC_QUALITY_GATE
HOOK_VARIANTS
HOOK_GENERATION_GATE
SELECTED_HOOK_REASON
score_each=present
hook_variant_1=One
hook_variant_2=Two
hook_variant_3=Three
RECURRING_REHOOK_MAP
CINEMATIC_SHORT_STORY_BLOCK
SOURCE_INTEGRITY_GATE
script_overall_score=90
script_pass_threshold=80
SCRIPT_QUALITY_GATE
VALIDATION_SCORECARD
RULE_CONSUMPTION_EVIDENCE_LEDGER
EXACT_RULE_LINEAGE_MAP
GATE_VISIBILITY_LOG
PROOF_TRACE_BUNDLE
CADENCE_AND_RETENTION_GATE
LIVE_HOST_REALTIME_BEHAVIOR_GATE
ARTICLE_LIKE_RISK_GATE
RECURRING_HOOK_DENSITY_LOCK
SCRIPT_BODY_DEPTH_LOCK
PER_TOOL_SOURCE_MAP
LINE_BY_LINE_INFLUENCE_MAP
SCRIPT_STRUCTURE
DYNAMIC_TIMED_BEAT_MAP
Final script
FINAL_SCRIPT
TIMED_BEAT_MAP
VOICE_GENERATION_CONTEXT
IMAGE_GENERATION_CONTEXT
VIDEO_GENERATION_CONTEXT
MUSIC_AND_SFX_CONTEXT
EDITING_CONTEXT
PLATFORM_PACKAGING
Provider Handoff Boundary
PROVIDER_HANDOFF_BOUNDARY
QUALITY_GATE
LINEAGE_SUMMARY
LOCAL_CLOUD_HYBRID_EXECUTION_PLAN
Quality Gate
Lineage Summary
Final Proof Classification
Source Summary
Compact Final Proof
proof_classification=PASS
directors/supreme_vision/krishna.md
directors/kernel/aruna.md
directors/research/vyasa.md
directors/research/valmiki.md
directors/distribution/saraswati.md
directors/kernel/yama.md
agents/krishna/krishna_agent.py
agents/aruna/aruna_agent.py
agents/vyasa/vyasa_agent.py
agents/valmiki/valmiki_agent.py
agents/saraswati/saraswati_agent.py
agents/yama/yama_agent.py
subagents/wf_200/wf_200_sub_agent.py
subagents/cwf_210/cwf_210_sub_agent.py
subagents/cwf_220/cwf_220_sub_agent.py
subagents/cwf_230/cwf_230_sub_agent.py
subagents/cwf_240/cwf_240_sub_agent.py
skills/script_intelligence/S-201-hook-optimizer.skill.md
skills/script_intelligence/S-202-first-draft-generation.skill.md
skills/script_intelligence/S-203-retention-engineer.skill.md
skills/script_intelligence/S-206-emotion-amplifier.skill.md
skills/script_intelligence/S-208-governance-safety-checker.skill.md
skills/script_intelligence/S-210-final-script-packager.skill.md
skills/script_intelligence_army/M-031-mrbeast-hook-system.skill.md
skills/script_intelligence_army/M-036-emotional-spike-system.skill.md
skills/script_intelligence_army/M-039-re-hook-system.skill.md
skills/script_intelligence_army/M-040-story-momentum-engine.skill.md
skills/sub_skills/SS-230-content-angle-generator.subskill.md
skills/sub_skills/SS-231-unique-value-proposition-builder.subskill.md
skills/sub_skills/SS-240-hook-variation-generator.subskill.md
skills/sub_skills/SS-241-open-loop-generator.subskill.md
skills/sub_skills/SS-242-story-tension-builder.subskill.md
skills/sub_skills/SS-243-pacing-controller.subskill.md
skills/sub_skills/SS-244-retention-loop-engine.subskill.md
skills/sub_skills/SS-245-cliffhanger-designer.subskill.md
emotional_strength_score=90
clarity_score=91
retention_score=92
spoken_cadence_score=89
article_like_risk_score=8
overall_score=90
pass_threshold=80
""",
            0,
        ),
        (
            "route_alias_mismatch_rejected",
            """
SHADOW_BOOT_CONFIRMATION
shadow_boot_confirmation_present=true
first_visible_output_is_boot_confirmation=true
agents_md_detected=true
agents_md_read=true
repo_first_orchestration_started=true
generic_direct_answer_avoided=true
shadow_mode=CHAT_ONLY_MODE
task_intent_classified=true
task_intent_routing_matrix_cited=true
director_skill_consumption_protocol_read=true
script_quality_enforcement_contract_read=true
gumloop_benchmark_output_standard_read=true
task_execution_state_machine_contract_read=true
route_dependency_expansion_protocol_read=true
route_manifest_path=registries/route_manifests/topic_discovery.yaml
route_manifest_read=true
route_dependency_expansion_lock_present=true
route_scope_complete=true
mandatory_files_read_before_output=true
script_generated_after_all_locks=true
chat_only_mode_used=true
files_created=false
dossier_artifacts_created=false
shadow_task_execution_wrapper_read=true
wrapper_required_mode_used=true
layman_command_gateway_used=true
shadow_command_alias_detected=true
raw_user_task_preserved=true
alias_matrix_entry_used=true
route_id_resolved=true
route_manifest_loaded=true
internal_wrapper_applied=true
gateway_contract_loaded_before_alias=true
output_mode_contract_loaded=true
output_mode=OPERATOR_MODE
operator_mode_used=true
operator_mode_compact_proof_present=true
compact_or_proof_output_allowed_only_after_locks=true
registry_paths_exist=true
route_components_exist=true
provider_boundary_present=true
no_n8n_provider_media_execution=true
selected_components_are_registered=true
selected_components_without_read_before_output=false
loaded_true_but_not_consumed_detected=false
manual_rerun_structured_but_partial_detected=false
route_id=SCRIPT_GENERATION
Shadow topic: find me a viral topic
TASK_ROUTE_LOCK
ROUTE_DEPENDENCY_EXPANSION_LOCK
ROUTE_STATE_CAPSULE
READ_LEDGER_SUMMARY
ROUTE_SCOPE_FILE_AUDIT
CONSUMPTION_LOCK
SOURCE_RESEARCH_LOCK
QUALITY_LOCK
GOVERNANCE_LOCK
DIRECTOR_CONSUMPTION_LEDGER
AGENT_CONSUMPTION_LEDGER
SUBAGENT_CONSUMPTION_LEDGER
SKILL_CONSUMPTION_LEDGER
SUBSKILL_CONSUMPTION_LEDGER
SCRIPT_STRUCTURE
Final script
""",
            1,
        ),
        (
            "wrapper_order_violation_rejected",
            """
TASK_ROUTE_LOCK
SHADOW_BOOT_CONFIRMATION
shadow_boot_confirmation_present=true
first_visible_output_is_boot_confirmation=true
agents_md_detected=true
agents_md_read=true
repo_first_orchestration_started=true
generic_direct_answer_avoided=true
shadow_mode=CHAT_ONLY_MODE
task_intent_classified=true
task_intent_routing_matrix_cited=true
director_skill_consumption_protocol_read=true
script_quality_enforcement_contract_read=true
gumloop_benchmark_output_standard_read=true
task_execution_state_machine_contract_read=true
route_dependency_expansion_protocol_read=true
route_manifest_path=registries/route_manifests/script_generation.yaml
route_manifest_read=true
route_dependency_expansion_lock_present=true
route_scope_complete=true
mandatory_files_read_before_output=true
script_generated_after_all_locks=true
chat_only_mode_used=true
files_created=false
dossier_artifacts_created=false
shadow_task_execution_wrapper_read=true
wrapper_required_mode_used=true
route_id=SCRIPT_GENERATION
loaded_true_but_not_consumed_detected=false
manual_rerun_structured_but_partial_detected=false
selected_components_without_read_before_output=false
TASK_ROUTE_LOCK
ROUTE_DEPENDENCY_EXPANSION_LOCK
ROUTE_STATE_CAPSULE
READ_LEDGER_SUMMARY
ROUTE_SCOPE_FILE_AUDIT
CONSUMPTION_LOCK
QUALITY_LOCK
GOVERNANCE_LOCK
DIRECTOR_CONSUMPTION_LEDGER
AGENT_CONSUMPTION_LEDGER
SUBAGENT_CONSUMPTION_LEDGER
SKILL_CONSUMPTION_LEDGER
SUBSKILL_CONSUMPTION_LEDGER
""",
            1,
        ),
        (
            "voice_context_valid_minimal",
            """
SHADOW_BOOT_CONFIRMATION
AGENTS.md
shadow_boot_confirmation_present=true
first_visible_output_is_boot_confirmation=true
agents_md_detected=true
agents_md_read=true
repo_first_orchestration_started=true
layman_task_trigger_contract_read=true
generic_direct_answer_avoided=true
shadow_mode=CHAT_ONLY_MODE
NATIVE_AGENT_CAPABILITY_ASSESSMENT
TASK_FRESHNESS_CLASSIFICATION
RESEARCH_MODE_DECISION
Research Sufficiency Gate
TASK_TO_CAPABILITY_ROUTING
registries/native_capability_routing_matrix.yaml
task_intent_classified=true
task_intent_routing_matrix_cited=true
route_id=VOICE_CONTEXT
registries/task_intent_routing_matrix.yaml
director_skill_consumption_protocol_read=true
script_quality_enforcement_contract_read=true
gumloop_benchmark_output_standard_read=true
task_execution_state_machine_contract_read=true
route_dependency_expansion_protocol_read=true
runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md
runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md
route_manifest_path=registries/route_manifests/voice_context.yaml
route_manifest_read=true
route_dependency_expansion_lock_present=true
route_scope_complete=true
mandatory_files_read_before_output=true
script_generated_after_all_locks=true
director_consumption_ledger_present=true
agent_consumption_ledger_present=true
subagent_consumption_ledger_present=true
skill_consumption_ledger_present=true
subskill_consumption_ledger_present=true
line_by_line_influence_map_present=true
topic_quality_gate_present=true
hook_generation_gate_present=true
script_quality_gate_present=true
shallow_repo_routing_detected=false
chat_only_mode_used=true
files_created=false
dossier_artifacts_created=false
plain_post_bootstrap_task_failed=false
shadow_task_execution_wrapper_read=true
wrapper_required_mode_used=true
codex_cloud_reliable_mode=WRAPPER_REQUIRED_COMPATIBLE
layman_command_gateway_used=true
shadow_command_alias_detected=true
raw_user_task_preserved=true
alias_matrix_entry_used=true
route_id_resolved=true
route_manifest_loaded=true
internal_wrapper_applied=true
gateway_contract_loaded_before_alias=true
output_mode_contract_loaded=true
output_mode=OPERATOR_MODE
operator_mode_used=true
operator_mode_compact_proof_present=true
compact_or_proof_output_allowed_only_after_locks=true
registry_paths_exist=true
route_components_exist=true
provider_boundary_present=true
no_n8n_provider_media_execution=true
selected_components_are_registered=true
selected_components_without_read_before_output=false
loaded_true_but_not_consumed_detected=false
manual_rerun_structured_but_partial_detected=false
exact_rule_evidence_present=true
exact_rule_lineage_map_present=true
per_tool_source_map_present=true
universal_component_contract_present=true
script_segment_packet_present=true
voice_context_packet_present=true
visual_context_packet_present=true
video_context_packet_present=true
music_sfx_packet_present=true
editing_timeline_packet_present=true
provider_handoff_packet_present=true
media_quality_gate_packet_present=true
lineage_approval_packet_present=true
segment_level_regeneration_actions_present=true
task_route_lock_status=PASS
route_dependency_expansion_lock_status=PASS
consumption_lock_status=PASS
source_research_lock_status=PASS
rule_consumption_evidence_lock_status=PASS
quality_lock_status=PASS
governance_lock_status=PASS
Shadow voice: create an elevenlabs packet
TASK_ROUTE_LOCK
ROUTE_DEPENDENCY_EXPANSION_LOCK
ROUTE_STATE_CAPSULE
READ_LEDGER_SUMMARY
ROUTE_SCOPE_FILE_AUDIT
CONSUMPTION_LOCK
SOURCE_RESEARCH_LOCK
QUALITY_LOCK
GOVERNANCE_LOCK
DIRECTOR_CONSUMPTION_LEDGER
AGENT_CONSUMPTION_LEDGER
SUBAGENT_CONSUMPTION_LEDGER
SKILL_CONSUMPTION_LEDGER
SUBSKILL_CONSUMPTION_LEDGER
Registry-First Route
Director Selection
AGENT_RUNTIME_SELECTION
registries/agent_runtime_selection_index.yaml
Subagent Selection
Skill Selection
Subskill Selection
TOOLS_CONNECTORS_PLUGINS_ASSESSMENT
CONTENT_MISSION_BRIEF
RESEARCH_AND_SOURCE_STATUS
TOPIC_QUALITY_GATE
HOOK_GENERATION_GATE
score_each=present
hook_variant_1=One
hook_variant_2=Two
hook_variant_3=Three
script_overall_score=90
script_pass_threshold=80
SCRIPT_QUALITY_GATE
VALIDATION_SCORECARD
RULE_CONSUMPTION_EVIDENCE_LEDGER
EXACT_RULE_LINEAGE_MAP
GATE_VISIBILITY_LOG
PROOF_TRACE_BUNDLE
LINE_BY_LINE_INFLUENCE_MAP
SCRIPT_STRUCTURE
Final script
FINAL_SCRIPT
TIMED_BEAT_MAP
VOICE_GENERATION_CONTEXT
IMAGE_GENERATION_CONTEXT
VIDEO_GENERATION_CONTEXT
MUSIC_AND_SFX_CONTEXT
EDITING_CONTEXT
PLATFORM_PACKAGING
Provider Handoff Boundary
PROVIDER_HANDOFF_BOUNDARY
Quality Gate
Lineage Summary
Final Proof Classification
Source Summary
Compact Final Proof
proof_classification=PASS
directors/distribution/saraswati.md
directors/production/tumburu.md
directors/cinematic/varuna.md
agents/saraswati/saraswati_agent.py
agents/tumburu/tumburu_agent.py
agents/varuna/varuna_agent.py
subagents/cwf_430/cwf_430_sub_agent.py
subagents/wf_400/wf_400_sub_agent.py
skills/media_audio/M-231-voiceover-direction-script.skill.md
skills/media_audio/M-238-compression-eq-specifications.skill.md
skills/media_audio/M-240-audio-mixing-guide.skill.md
skills/operations/M-162-voice-identity-cloner.skill.md
skills/operations/M-163-speech-emotion-engine.skill.md
skills/sub_skills/SS-101-elevenlabs-voice-generation-optimizer.subskill.md
emotional_strength_score=90
clarity_score=91
retention_score=92
spoken_cadence_score=89
article_like_risk_score=8
overall_score=90
pass_threshold=80
""",
            0,
        ),
        (
            "voice_context_alias_mismatch_rejected",
            """
SHADOW_BOOT_CONFIRMATION
shadow_boot_confirmation_present=true
first_visible_output_is_boot_confirmation=true
agents_md_detected=true
agents_md_read=true
repo_first_orchestration_started=true
generic_direct_answer_avoided=true
shadow_mode=CHAT_ONLY_MODE
task_intent_classified=true
task_intent_routing_matrix_cited=true
director_skill_consumption_protocol_read=true
script_quality_enforcement_contract_read=true
gumloop_benchmark_output_standard_read=true
task_execution_state_machine_contract_read=true
route_dependency_expansion_protocol_read=true
route_manifest_path=registries/route_manifests/voice_context.yaml
route_manifest_read=true
route_dependency_expansion_lock_present=true
route_scope_complete=true
mandatory_files_read_before_output=true
script_generated_after_all_locks=true
chat_only_mode_used=true
files_created=false
dossier_artifacts_created=false
shadow_task_execution_wrapper_read=true
wrapper_required_mode_used=true
layman_command_gateway_used=true
shadow_command_alias_detected=true
raw_user_task_preserved=true
alias_matrix_entry_used=true
route_id_resolved=true
route_manifest_loaded=true
internal_wrapper_applied=true
gateway_contract_loaded_before_alias=true
output_mode_contract_loaded=true
output_mode=OPERATOR_MODE
operator_mode_used=true
operator_mode_compact_proof_present=true
compact_or_proof_output_allowed_only_after_locks=true
registry_paths_exist=true
route_components_exist=true
provider_boundary_present=true
no_n8n_provider_media_execution=true
selected_components_are_registered=true
selected_components_without_read_before_output=false
loaded_true_but_not_consumed_detected=false
manual_rerun_structured_but_partial_detected=false
route_id=EDITING_PACKAGING
Shadow voice: create an elevenlabs packet
TASK_ROUTE_LOCK
ROUTE_DEPENDENCY_EXPANSION_LOCK
ROUTE_STATE_CAPSULE
READ_LEDGER_SUMMARY
ROUTE_SCOPE_FILE_AUDIT
CONSUMPTION_LOCK
QUALITY_LOCK
GOVERNANCE_LOCK
DIRECTOR_CONSUMPTION_LEDGER
AGENT_CONSUMPTION_LEDGER
SUBAGENT_CONSUMPTION_LEDGER
SKILL_CONSUMPTION_LEDGER
SUBSKILL_CONSUMPTION_LEDGER
VOICE_GENERATION_CONTEXT
Provider Handoff Boundary
PROVIDER_HANDOFF_BOUNDARY
SCRIPT_STRUCTURE
Final script
""",
            1,
        ),
    ]
    results: list[dict[str, object]] = []
    passed = True
    for name, fixture, expected_exit in cases:
        path = Path("/tmp") / f"validate_mac06_1a_{name}.txt"
        path.write_text(fixture, encoding="utf-8")
        actual_exit = main_with_path(path)
        case_passed = actual_exit == expected_exit
        passed = passed and case_passed
        results.append(
            {
                "name": name,
                "expected_exit": expected_exit,
                "actual_exit": actual_exit,
                "passed": case_passed,
            }
        )
    print(json.dumps({"self_test_passed": passed, "tests": results}, indent=2))
    return 0 if passed else 1


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    if not args.output_file:
        print("usage: validate_mac06_1a_output.py <output.txt>")
        return 2
    path = Path(args.output_file)
    if not path.is_file():
        print(f"VALIDATION_STATUS=FAIL\nreason=file_not_found\npath={path}")
        return 1
    return main_with_path(path)


if __name__ == "__main__":
    raise SystemExit(main())
