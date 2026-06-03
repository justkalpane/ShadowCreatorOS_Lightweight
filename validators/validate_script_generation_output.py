#!/usr/bin/env python3
"""Validate production-depth Shadow script-generation output.

This validator checks script story, research honesty, content-engineering
coverage, and weakest-layer status. It does not call the web or providers.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


FULL_CONTENT_ENGINEERING_SECTIONS = [
    "SCRIPT_LANGUAGE_DECLARATION",
    "USER_LANGUAGE_REQUEST_CHECK",
    "SHADOW_MISSION_PACKET",
    "RESEARCH_AND_SOURCE_STATUS",
    "SOURCE_LEDGER",
    "SOURCE_LIMITATION_NOTES",
    "FACT_VS_ANECDOTE_MAP",
    "CLAIM_EVIDENCE_STATUS",
    "HOOK_VARIANTS",
    "SELECTED_HOOK_REASON",
    "RECURRING_REHOOK_MAP",
    "CINEMATIC_SHORT_STORY_BLOCK",
    "SCRIPT_STRUCTURE",
    "FINAL_SCRIPT",
    "DYNAMIC_TIMED_BEAT_MAP",
    "VOICE_GENERATION_CONTEXT",
    "IMAGE_GENERATION_CONTEXT",
    "VIDEO_GENERATION_CONTEXT",
    "MUSIC_AND_SFX_CONTEXT",
    "EDITING_CONTEXT",
    "PLATFORM_PACKAGING",
    "PROVIDER_HANDOFF_BOUNDARY",
    "QUALITY_GATE",
    "LINEAGE_SUMMARY",
    "LOCAL_CLOUD_HYBRID_EXECUTION_PLAN",
]

STORY_FIELDS = [
    "character",
    "setting",
    "conflict",
    "stakes",
    "turning_point",
    "cinematic_visuals",
    "emotional_peak",
    "lesson_bridge",
    "topic_connection",
]

REAL_WORLD_MARKERS = [
    "real_person_used=true",
    "real_incident_used=true",
    "biographical_claims_present=true",
    "career_claims_present=true",
    "real_world_example_as_proof=true",
    "story_basis=real_person_public_arc",
    "story_basis=verified_real_incident",
]

CURRENT_MARKERS = [
    "current_data_required=true",
    "latest_claims_present=true",
    "real_time_claims_present=true",
]

ALLOWED_STORY_BASES = {
    "verified_real_incident",
    "real_person_public_arc",
    "realistic_composite",
    "mythological_parallel",
    "hybrid_modern_mythological_reference",
}

DYNAMIC_BEAT_FIELDS = [
    "scene_id",
    "start_time",
    "end_time",
    "duration_seconds",
    "duration_reason",
    "spoken_line_or_summary",
    "scene_purpose",
    "emotional_cue",
    "voice_cue",
    "visual_cue",
    "avatar_cue",
    "broll_or_image_cue",
    "music_sfx_cue",
    "transition_cue",
    "platform_dependency",
    "local_cloud_hybrid_dependency",
]

HYBRID_PLAN_FIELDS = [
    "local_options",
    "cloud_options",
    "hybrid_strategy",
    "fallback",
]

INFLUENCE_DEPTH_FIELDS = [
    "why_line_exists",
    "emotion_triggered",
    "retention_function",
    "topic_support",
    "media_dependency",
]

REHOOK_MAPPING_FIELDS = [
    "rehooks_mapped_to_final_script",
    "rehooks_mapped_to_dynamic_beat_map",
    "rehooks_mapped_to_editing_context",
    "rehooks_mapped_to_line_influence_map",
]

PROPAGATION_MARKER = "MAC-06.2O SCRIPT BEHAVIOR PROPAGATION"
REPO_ROOT = Path(__file__).resolve().parents[1]
PROPAGATION_FILES = {
    "DIRECTOR": [
        "directors/supreme_vision/krishna.md",
        "directors/kernel/aruna.md",
        "directors/research/vyasa.md",
        "directors/research/valmiki.md",
        "directors/distribution/saraswati.md",
        "directors/kernel/yama.md",
        "directors/production/agni.md",
        "directors/research/ganesha.md",
        "directors/strategy/narada.md",
        "directors/distribution/kama.md",
    ],
    "AGENT": [
        "agents/agastya/agastya_agent.py",
        "agents/krishna/krishna_agent.py",
        "agents/aruna/aruna_agent.py",
        "agents/vyasa/vyasa_agent.py",
        "agents/valmiki/valmiki_agent.py",
        "agents/saraswati/saraswati_agent.py",
        "agents/yama/yama_agent.py",
        "agents/agni/agni_agent.py",
        "agents/ganesha/ganesha_agent.py",
        "agents/narada/narada_agent.py",
        "agents/kama/kama_agent.py",
    ],
    "SUBAGENT": [
        "subagents/wf_200/wf_200_sub_agent.py",
        "subagents/cwf_210/cwf_210_sub_agent.py",
        "subagents/cwf_220/cwf_220_sub_agent.py",
        "subagents/cwf_230/cwf_230_sub_agent.py",
        "subagents/cwf_240/cwf_240_sub_agent.py",
    ],
    "SCRIPT_SKILL": [
        "skills/script_intelligence/S-201-hook-optimizer.skill.md",
        "skills/script_intelligence/S-202-first-draft-generation.skill.md",
        "skills/script_intelligence/S-203-retention-engineer.skill.md",
        "skills/script_intelligence/S-206-emotion-amplifier.skill.md",
        "skills/script_intelligence/S-208-governance-safety-checker.skill.md",
        "skills/script_intelligence/S-210-final-script-packager.skill.md",
        "skills/script_intelligence_army/M-031-mrbeast-hook-system.skill.md",
        "skills/script_intelligence_army/M-036-emotional-spike-system.skill.md",
        "skills/script_intelligence_army/M-039-re-hook-system.skill.md",
        "skills/script_intelligence_army/M-040-story-momentum-engine.skill.md",
        "skills/script_intelligence_army/M-042-editing-optimization-engine.skill.md",
    ],
    "SUBSKILL": [
        "skills/sub_skills/SS-240-hook-variation-generator.subskill.md",
        "skills/sub_skills/SS-241-open-loop-generator.subskill.md",
        "skills/sub_skills/SS-242-story-tension-builder.subskill.md",
        "skills/sub_skills/SS-243-pacing-controller.subskill.md",
        "skills/sub_skills/SS-244-retention-loop-engine.subskill.md",
        "skills/sub_skills/SS-245-cliffhanger-designer.subskill.md",
    ],
    "EXECUTABLE_SKILL": [
        "skills/script_intelligence/S-201-research-to-script-brief.py",
        "skills/script_intelligence/S-202-first-draft-generation.py",
        "skills/script_intelligence/S-210-final-script-packager.py",
        "skills/media_production/A-405-media-qa-validator.py",
        "skills/context_engineering/P-304-lineage-chain-validator.py",
        "skills/script_intelligence_army/M-031-mrbeast-hook-system.py",
        "skills/script_intelligence_army/M-032-pattern-interrupt-engine.py",
        "skills/script_intelligence_army/M-033-curiosity-gap-generator.py",
        "skills/script_intelligence_army/M-034-micro-cliffhanger-engine.py",
        "skills/script_intelligence_army/M-035-engagement-loop-builder.py",
        "skills/script_intelligence_army/M-036-emotional-spike-system.py",
        "skills/script_intelligence_army/M-039-re-hook-system.py",
        "skills/script_intelligence_army/M-040-story-momentum-engine.py",
        "skills/script_intelligence_army/M-042-editing-optimization-engine.py",
        "skills/sub_skills/SS-240-hook-variation-generator.py",
        "skills/sub_skills/SS-241-open-loop-generator.py",
        "skills/sub_skills/SS-242-story-tension-builder.py",
        "skills/sub_skills/SS-243-pacing-controller.py",
        "skills/sub_skills/SS-244-retention-loop-engine.py",
        "skills/sub_skills/SS-245-cliffhanger-designer.py",
    ],
}


@dataclass
class ValidationResult:
    classification: str = "PASS"
    errors: list[str] = field(default_factory=list)
    partials: list[str] = field(default_factory=list)
    checks: dict[str, bool] = field(default_factory=dict)

    def fail(self, issue: str) -> None:
        if issue not in self.errors:
            self.errors.append(issue)
        self.classification = "FAIL"

    def partial(self, issue: str) -> None:
        if issue not in self.partials:
            self.partials.append(issue)
        if self.classification == "PASS":
            self.classification = "PARTIAL"


def key_value(text: str, key: str) -> str | None:
    match = re.search(
        rf"(?im)^\s*[-*]?\s*`?{re.escape(key)}`?\s*[:=]\s*(.+?)\s*$", text
    )
    return match.group(1).strip() if match else None


def bool_value(text: str, key: str) -> bool | None:
    value = key_value(text, key)
    if value is None:
        return None
    normalized = value.strip("`\"' ").lower()
    if normalized == "true":
        return True
    if normalized == "false":
        return False
    return None


def int_value(text: str, key: str) -> int | None:
    value = key_value(text, key)
    if value is None:
        return None
    match = re.search(r"-?\d+", value)
    return int(match.group(0)) if match else None


def key_values(text: str, key: str) -> list[str]:
    return [
        value.strip()
        for value in re.findall(
            rf"(?im)^\s*[-*]?\s*`?{re.escape(key)}`?\s*[:=]\s*(.+?)\s*$",
            text,
        )
    ]


def section_bodies(text: str, section: str) -> list[str]:
    """Return every body for a named all-caps output section."""
    lines = text.splitlines()
    bodies: list[str] = []
    active: list[str] | None = None
    heading = re.compile(r"^\s*#*\s*([A-Z][A-Z0-9_ ]{2,})\s*$")
    for line in lines:
        match = heading.match(line)
        if match:
            if active is not None:
                bodies.append("\n".join(active))
            active = [] if match.group(1).strip() == section else None
            continue
        if active is not None:
            active.append(line)
    if active is not None:
        bodies.append("\n".join(active))
    return bodies


def section_text(text: str, section: str) -> str:
    return "\n".join(section_bodies(text, section))


def scoped_json_rows(text: str, section: str, key: str) -> list[dict]:
    rows: list[dict] = []
    for body in section_bodies(text, section):
        for raw in key_values(body, key):
            try:
                row = json.loads(raw)
            except json.JSONDecodeError:
                continue
            if isinstance(row, dict):
                rows.append(row)
    return rows


def placeholder_value(value: object) -> bool:
    if isinstance(value, str):
        lowered = value.strip().lower()
        return not lowered or any(
            token in lowered
            for token in ["tbd", "placeholder", "coming soon", "needs_creative", "sample"]
        )
    return False


def parse_timestamp_seconds(value: object) -> int | None:
    if isinstance(value, (int, float)):
        return int(value)
    if not isinstance(value, str):
        return None
    raw = value.strip().lower()
    if "-" in raw:
        raw = raw.split("-", 1)[0].strip()
    match = re.fullmatch(r"(\d{1,2}):(\d{1,2})", raw)
    if match:
        return int(match.group(1)) * 60 + int(match.group(2))
    match = re.search(r"(\d+)\s*(?:s|sec|secs|second|seconds)?", raw)
    return int(match.group(1)) if match else None


def normalized_contains(haystack: str, needle: str) -> bool:
    compact = lambda value: re.sub(r"\s+", " ", value.casefold()).strip()
    return bool(needle.strip()) and compact(needle) in compact(haystack)


HINDI_HINGLISH_TOKENS = {
    "aaj", "aap", "ab", "agar", "apna", "apni", "aur", "bas", "bhi", "bano",
    "duniya", "hai", "hain", "ho", "hum", "ka", "kar", "karo", "ke", "ki",
    "ko", "kya", "kyun", "main", "mat", "mein", "mila", "nahi", "paisa",
    "paise", "pe", "se", "sirf", "soch", "tha", "toh", "tum", "tumhe", "usne",
    "waqt", "ye", "yeh",
}
INDIC_SCRIPT = re.compile(r"[\u0900-\u0d7f]")


def script_body_language(text: str) -> tuple[str, float]:
    body = section_text(text, "FINAL_SCRIPT") or section_text(text, "MAIN_SCRIPT_IN_ENGLISH")
    tokens = re.findall(r"[^\W\d_]+", body.casefold(), flags=re.UNICODE)
    if not tokens:
        return "UNKNOWN", 0.0
    non_english = sum(
        token in HINDI_HINGLISH_TOKENS or bool(INDIC_SCRIPT.search(token))
        for token in tokens
    )
    ratio = non_english / len(tokens)
    if INDIC_SCRIPT.search(body):
        return "INDIAN_LANGUAGE_SCRIPT", ratio
    if ratio >= 0.12:
        return "HINGLISH_OR_HINDI", ratio
    return "ENGLISH", ratio


def recursive_schema_errors(instance: object, schema: dict, path: str = "scene") -> list[str]:
    errors: list[str] = []
    expected = schema.get("type")
    if expected == "object":
        if not isinstance(instance, dict):
            return [f"{path}:expected_object"]
        for key in schema.get("required", []):
            if key not in instance:
                errors.append(f"{path}.{key}:missing")
        for key, child_schema in schema.get("properties", {}).items():
            if key in instance:
                errors.extend(recursive_schema_errors(instance[key], child_schema, f"{path}.{key}"))
    elif expected == "array" and not isinstance(instance, list):
        errors.append(f"{path}:expected_array")
    elif expected == "string":
        if not isinstance(instance, str):
            errors.append(f"{path}:expected_string")
        elif len(instance) < schema.get("minLength", 0):
            errors.append(f"{path}:too_short")
    elif expected == "number":
        if not isinstance(instance, (int, float)) or isinstance(instance, bool):
            errors.append(f"{path}:expected_number")
        else:
            if instance < schema.get("minimum", instance):
                errors.append(f"{path}:below_minimum")
            if instance > schema.get("maximum", instance):
                errors.append(f"{path}:above_maximum")
    elif expected == "boolean" and not isinstance(instance, bool):
        errors.append(f"{path}:expected_boolean")
    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}:const_mismatch")
    if isinstance(instance, dict) and instance.get("hook_marker") is True:
        for key in ["rehook_type", "retention_reset_goal"]:
            if not str(instance.get(key, "")).strip():
                errors.append(f"{path}.{key}:missing_for_hook")
    return errors


def responsibility_specific_enforcement(layer: str, text: str) -> bool:
    lowered = text.lower()
    tokens = {
        "DIRECTOR": ["reject", "block", "require", "cannot pass", "must downgrade", "weakest gate"],
        "AGENT": ["validate", "reject", "enforce", "emit gate", "downgrade status"],
        "SUBAGENT": ["route lock", "quality lock", "rehook map", "scene sync", "validation lane", "fallback"],
        "SCRIPT_SKILL": ["generate", "validate", "score", "map", "synchronize", "classify", "enforce"],
        "SUBSKILL": ["rehook", "open loop", "tension", "pacing", "retention", "cliffhanger", "cta", "timestamp", "gap"],
        "EXECUTABLE_SKILL": ["def run", "validate", "recurring_rehook", "scene_sync", "retention"],
    }
    return any(token in lowered for token in tokens.get(layer, []))


def m039_dag_alignment() -> tuple[bool, dict[str, object]]:
    registry = json.loads(
        (REPO_ROOT / "registries/route_dag_registry.yaml").read_text(encoding="utf-8")
    )
    route = next(
        (item for item in registry.get("route_dags", []) if item.get("route_id") == "script_generation"),
        {},
    )
    nodes = route.get("ordered_nodes", [])
    ids = [node.get("component_id") for node in nodes]
    m039_index = ids.index("M-039-re-hook-system") if "M-039-re-hook-system" in ids else -1
    s202_index = ids.index("S-202-first-draft-generation") if "S-202-first-draft-generation" in ids else -1
    aligned = (
        0 <= m039_index < s202_index
        and "rehook_plan_packet" in nodes[m039_index].get("emitted_output_packets", [])
        and "rehook_plan_packet" in nodes[s202_index].get("required_input_packets", [])
    )
    return aligned, {
        "m039_dag_present": m039_index >= 0,
        "s202_executes_directly": s202_index >= 0,
        "m039_before_s202": 0 <= m039_index < s202_index,
        "typed_rehook_packet_bound": aligned,
    }


def has_section(text: str, section: str) -> bool:
    return bool(re.search(rf"(?im)^\s*#*\s*{re.escape(section)}\b", text))


def nonempty_value(text: str, key: str) -> bool:
    value = key_value(text, key)
    if value is None:
        return False
    normalized = value.strip().lower()
    return normalized not in {"", "[]", "{}", "none", "null", "false", '""', "''"}


def unsupported_claims_present(text: str) -> bool:
    return nonempty_value(text, "unsupported_claims")


def source_research_pass_claimed(text: str) -> bool:
    value = key_value(text, "source_research_lock_status")
    if value and value.strip("`\"' ").upper() == "PASS":
        return True
    return bool(re.search(r"(?im)^\s*SOURCE_RESEARCH_LOCK(?:_STATUS)?\s*[:=]\s*PASS\s*$", text))


def final_proof_status(text: str) -> str | None:
    for key in [
        "final_status",
        "final_proof_classification",
        "proof_classification",
        "final_classification",
    ]:
        value = key_value(text, key)
        if value:
            return value.strip("`\"' ").upper()
    mac_status = re.search(r"(?im)^\s*MAC_[A-Z0-9_]+_STATUS\s*[:=]\s*(\w+)", text)
    if mac_status:
        return mac_status.group(1).upper()
    return None


def duration_requires_story(text: str) -> bool:
    if bool_value(text, "cinematic_story_required") is True:
        return True
    platform = key_value(text, "platform") or ""
    match = re.search(r"(?im)^\s*script_duration_minutes\s*[:=]\s*(\d+(?:\.\d+)?)", text)
    if not match:
        return False
    duration = float(match.group(1))
    return "youtube" in platform.lower() and 3 <= duration <= 10


def script_duration_minutes(text: str) -> float | None:
    match = re.search(
        r"(?im)^\s*script_duration_minutes\s*[:=]\s*(\d+(?:\.\d+)?)", text
    )
    return float(match.group(1)) if match else None


def required_internal_rehooks(duration_minutes: float) -> int:
    if duration_minutes < 3:
        return 0
    if duration_minutes <= 5:
        return max(1, int(duration_minutes) - 2)
    return max(4, math.ceil((duration_minutes * 60) / 90) - 1)


def validate_repo_propagation(result: ValidationResult) -> None:
    missing: list[str] = []
    marker_only: list[str] = []
    layer_totals: dict[str, int] = {}
    for layer, relative_paths in PROPAGATION_FILES.items():
        layer_totals[layer] = len(relative_paths)
        for relative_path in relative_paths:
            path = REPO_ROOT / relative_path
            if not path.exists():
                missing.append(f"{relative_path}:file_missing")
                continue
            text = path.read_text(encoding="utf-8")
            if PROPAGATION_MARKER not in text:
                missing.append(f"{relative_path}:marker_missing")
            elif not responsibility_specific_enforcement(layer, text):
                marker_only.append(f"{relative_path}:marker_only")
    result.checks["repo_wide_propagation_gate_present"] = True
    result.checks["repo_wide_propagation_complete"] = not missing and not marker_only
    result.checks["marker_only_files_absent"] = not marker_only
    result.checks["responsibility_enforced_files"] = (
        sum(layer_totals.values()) - len(missing) - len(marker_only)
    )
    result.checks["director_propagation_complete"] = not any(
        item.startswith("directors/") for item in missing
    )
    result.checks["agent_propagation_complete"] = not any(
        item.startswith("agents/") for item in missing
    )
    result.checks["subagent_propagation_complete"] = not any(
        item.startswith("subagents/") for item in missing
    )
    result.checks["skill_propagation_complete"] = not any(
        item.startswith("skills/script_") for item in missing
    )
    result.checks["subskill_propagation_complete"] = not any(
        item.startswith("skills/sub_skills/") for item in missing
    )
    result.checks["propagation_files_checked"] = sum(layer_totals.values()) > 0
    if missing:
        result.fail("repo_wide_propagation_missing:" + ",".join(missing))
    if marker_only:
        result.fail("repo_wide_propagation_marker_only:" + ",".join(marker_only))
    dag_aligned, dag_checks = m039_dag_alignment()
    result.checks.update({f"m039_{key}": value for key, value in dag_checks.items()})
    if not dag_aligned:
        result.fail("m039_executable_dag_alignment_missing")


def detects_real_world_proof(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in REAL_WORLD_MARKERS)


def detects_current_claims(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in CURRENT_MARKERS)


def validate(text: str) -> ValidationResult:
    result = ValidationResult()
    validate_repo_propagation(result)
    story_required = duration_requires_story(text)
    real_world_proof = detects_real_world_proof(text)
    web_evidence_required = real_world_proof or detects_current_claims(text)
    explicit_script_only = bool_value(text, "explicit_script_only_request") is True
    repo_only_approved = bool_value(text, "user_approved_repo_only_continuation") is True
    explicit_language = bool_value(text, "explicit_language_requested") is True
    media_factory_final = bool_value(text, "media_factory_final_draft_requested") is True

    result.checks.update(
        {
            "story_required": story_required,
            "real_world_proof_detected": real_world_proof,
            "web_evidence_required": web_evidence_required,
            "explicit_script_only_request": explicit_script_only,
            "media_factory_final_draft_requested": media_factory_final,
        }
    )

    language_declaration = has_section(text, "SCRIPT_LANGUAGE_DECLARATION")
    language_request_check = has_section(text, "USER_LANGUAGE_REQUEST_CHECK")
    result.checks["script_language_declaration_present"] = language_declaration
    result.checks["user_language_request_check_present"] = language_request_check
    if not language_declaration:
        result.partial("script_language_declaration_missing")
    if not language_request_check:
        result.partial("user_language_request_check_missing")
    master_language = (key_value(text, "master_script_language") or "").strip("`\"' ")
    result.checks["master_script_language_present"] = bool(master_language)
    if not master_language:
        result.partial("master_script_language_missing")
    if not explicit_language and master_language.lower() != "english":
        result.fail("language_drift:default_master_script_must_be_english")
    detected_body_language, non_english_ratio = script_body_language(text)
    result.checks["script_body_language_detected"] = detected_body_language
    result.checks["script_body_non_english_ratio"] = round(non_english_ratio, 4)
    result.checks["script_body_language_matches_default"] = (
        explicit_language or detected_body_language in {"ENGLISH", "UNKNOWN"}
    )
    if (
        not explicit_language
        and master_language.lower() == "english"
        and detected_body_language not in {"ENGLISH", "UNKNOWN"}
    ):
        result.fail("language_drift:declared_english_but_script_body_is_not_english")

    if story_required:
        story_present = has_section(text, "CINEMATIC_SHORT_STORY_BLOCK")
        result.checks["cinematic_story_block_present"] = story_present
        if not story_present:
            result.partial("cinematic_story_block_missing")
        else:
            for story_field in STORY_FIELDS:
                present = nonempty_value(text, story_field)
                result.checks[f"story_{story_field}_present"] = present
                if not present:
                    result.partial(f"cinematic_story_missing_field:{story_field}")
            duration_value = key_value(text, "duration_target_seconds")
            duration_ok = bool(
                duration_value
                and re.search(r"(45\s*-\s*75|45_to_75|[4-7]\d)", duration_value)
            )
            result.checks["story_duration_target_present"] = duration_ok
            if not duration_ok:
                result.partial("cinematic_story_duration_target_missing_or_invalid")
            if real_world_proof and not nonempty_value(text, "source_references"):
                result.fail("real_world_story_source_references_missing")
            story_basis = (key_value(text, "story_basis") or "").strip("`\"' ")
            result.checks["story_basis_allowed"] = story_basis in ALLOWED_STORY_BASES
            if story_basis not in ALLOWED_STORY_BASES:
                result.partial("cinematic_story_basis_missing_or_invalid")
            if bool_value(text, "generic_motivation_filler") is True:
                result.fail("cinematic_story_is_generic_motivation_filler")
            if bool_value(text, "cinematic_reconstruction") is True:
                if bool_value(text, "verified_scene_details") is not False:
                    result.fail("cinematic_reconstruction_must_disclose_unverified_scene_details")

    if web_evidence_required:
        web_required = bool_value(text, "web_required")
        web_used = bool_value(text, "web_access_used")
        source_list_present = bool_value(text, "source_list_present")
        result.checks["web_required_true"] = web_required is True
        result.checks["web_access_used_true"] = web_used is True
        result.checks["source_list_present_true"] = source_list_present is True
        if web_required is not True:
            result.fail("web_required_must_be_true_for_real_world_or_current_claims")
        if web_used is not True and not repo_only_approved:
            result.fail("required_web_research_not_used")
        if web_used is True and source_list_present is not True:
            result.fail("web_research_used_without_source_list")

    if bool_value(text, "real_time_sources_used") is True:
        if bool_value(text, "source_list_present") is not True:
            result.fail("real_time_sources_used_without_source_list")
    if bool_value(text, "real_time_research_claimed") is True:
        if bool_value(text, "real_time_sources_used") is not True:
            result.fail("real_time_research_claimed_without_real_time_sources")

    unsupported = unsupported_claims_present(text)
    result.checks["unsupported_claims_empty"] = not unsupported
    if unsupported and source_research_pass_claimed(text):
        result.fail("unsupported_claims_present_but_source_research_lock_passed")

    if real_world_proof:
        source_rows = scoped_json_rows(text, "SOURCE_LEDGER", "source_row_json")
        fact_rows = scoped_json_rows(text, "FACT_VS_ANECDOTE_MAP", "fact_map_row_json")
        required_source_fields = {
            "source_id", "url", "title", "date", "source_type", "claim_supported", "limitation"
        }
        incomplete_source_rows = [
            str(row.get("source_id", "unknown"))
            for row in source_rows
            if not required_source_fields.issubset(row)
            or any(placeholder_value(row.get(field)) for field in required_source_fields)
        ]
        source_urls = [str(row["url"]) for row in source_rows if "url" in row]
        source_types = [str(row.get("source_type", "")).lower() for row in source_rows]
        source_count = len(set(source_urls))
        non_encyclopedia_count = sum(
            source_type != "encyclopedia_background" for source_type in source_types
        )
        source_category_count = len(set(source_types))
        fact_map_present = has_section(text, "FACT_VS_ANECDOTE_MAP")
        required_fact_fields = {
            "claim", "source", "classification", "script_usage_allowed", "risk_note"
        }
        incomplete_fact_rows = [
            str(row.get("claim", "unknown"))
            for row in fact_rows
            if not required_fact_fields.issubset(row)
            or any(placeholder_value(row.get(field)) for field in required_fact_fields)
        ]
        anecdote_as_fact = any(
            str(row.get("classification", "")).upper() == "ANECDOTAL_SUPPORT"
            and row.get("script_usage_allowed") in {True, "true", "VERIFIED", "verified_fact"}
            for row in fact_rows
        )
        result.checks["ledger_source_rows_detected"] = len(source_rows)
        result.checks["ledger_urls_count"] = source_count
        result.checks["urls_outside_ledger_ignored"] = True
        result.checks["source_ledger_rows_complete"] = not incomplete_source_rows
        result.checks["fact_map_rows_detected"] = len(fact_rows)
        result.checks["fact_vs_anecdote_rows_complete"] = not incomplete_fact_rows
        result.checks["source_count_sufficient"] = source_count is not None and source_count >= 3
        result.checks["non_encyclopedia_source_count_sufficient"] = (
            non_encyclopedia_count is not None and non_encyclopedia_count >= 2
        )
        result.checks["source_category_count_sufficient"] = (
            source_category_count is not None and source_category_count >= 3
        )
        result.checks["fact_vs_anecdote_map_present"] = fact_map_present
        if not source_rows:
            result.fail("source_ledger_has_no_structured_rows")
        if source_count < 3:
            result.partial("real_person_source_count_below_three")
        if incomplete_source_rows:
            result.fail("source_ledger_rows_incomplete:" + ",".join(incomplete_source_rows))
        if non_encyclopedia_count < 2:
            result.partial("real_person_non_encyclopedia_source_count_below_two")
        if source_category_count < 3:
            result.partial("real_person_source_category_count_below_three")
        if not fact_map_present:
            result.partial("fact_vs_anecdote_map_missing")
        elif not fact_rows:
            result.fail("fact_vs_anecdote_map_has_no_structured_rows")
        if incomplete_fact_rows:
            result.fail("fact_vs_anecdote_rows_incomplete:" + ",".join(incomplete_fact_rows))
        if anecdote_as_fact or bool_value(text, "anecdote_used_as_verified_fact") is True:
            result.fail("anecdotal_support_used_as_verified_fact")

    if not explicit_script_only:
        for section in FULL_CONTENT_ENGINEERING_SECTIONS:
            present = has_section(text, section)
            result.checks[f"section_{section.lower()}_present"] = present
            if not present:
                result.partial(f"content_engineering_section_missing:{section}")

    if not explicit_script_only:
        dynamic_map_present = has_section(text, "DYNAMIC_TIMED_BEAT_MAP")
        result.checks["dynamic_timed_beat_map_present"] = dynamic_map_present
        if not dynamic_map_present:
            result.partial("dynamic_timed_beat_map_missing")
        if bool_value(text, "beat_duration_dynamic") is not True:
            result.partial("beat_duration_dynamic_not_confirmed")
        if bool_value(text, "uniform_15_second_grid") is True:
            if bool_value(text, "uniform_grid_justification_present") is not True:
                result.fail("uniform_15_second_grid_without_justification")
        for beat_field in DYNAMIC_BEAT_FIELDS:
            present = nonempty_value(text, beat_field)
            result.checks[f"dynamic_beat_{beat_field}_present"] = present
            if not present:
                result.partial(f"dynamic_beat_field_missing:{beat_field}")
        hybrid_plan_present = has_section(text, "LOCAL_CLOUD_HYBRID_EXECUTION_PLAN")
        result.checks["local_cloud_hybrid_execution_plan_present"] = hybrid_plan_present
        if not hybrid_plan_present:
            result.partial("local_cloud_hybrid_execution_plan_missing")
        for hybrid_field in HYBRID_PLAN_FIELDS:
            present = nonempty_value(text, hybrid_field)
            result.checks[f"hybrid_plan_{hybrid_field}_present"] = present
            if not present:
                result.partial(f"local_cloud_hybrid_field_missing:{hybrid_field}")

    duration_minutes = script_duration_minutes(text)
    if (
        duration_minutes is not None
        and 3 <= duration_minutes <= 10
        and "youtube" in (key_value(text, "platform") or "").lower()
    ):
        result.checks["opening_hook_present"] = bool_value(text, "opening_hook_present") is True
        if bool_value(text, "opening_hook_present") is not True:
            result.partial("opening_hook_missing")
        if bool_value(text, "recurring_rehook_required") is not True:
            result.partial("recurring_rehook_required_not_confirmed")
        required_rehooks = required_internal_rehooks(duration_minutes)
        recurring_rehook_count = int_value(text, "recurring_rehook_count")
        result.checks["recurring_rehook_count_sufficient"] = (
            recurring_rehook_count is not None
            and recurring_rehook_count >= required_rehooks
        )
        if recurring_rehook_count is None or recurring_rehook_count < required_rehooks:
            result.partial(
                f"recurring_rehook_count_below_duration_minimum:{required_rehooks}"
            )
        max_gap = int_value(text, "max_gap_without_rehook_seconds")
        interval_reason = bool_value(text, "rehook_interval_reason_present") is True
        result.checks["max_gap_without_rehook_within_limit_or_justified"] = (
            max_gap is not None and (max_gap <= 90 or interval_reason)
        )
        if max_gap is None:
            result.partial("max_gap_without_rehook_seconds_missing")
        elif max_gap > 90 and not interval_reason:
            result.fail("max_gap_without_rehook_exceeds_90_without_justification")
        if bool_value(text, "rehook_interval_dynamic") is not True:
            result.partial("rehook_interval_dynamic_not_confirmed")
        if not interval_reason:
            result.partial("rehook_interval_reason_missing")
        if bool_value(text, "hook_marker") is not True:
            result.partial("dynamic_beat_map_rehook_marker_missing")
        if not nonempty_value(text, "rehook_type"):
            result.partial("dynamic_beat_map_rehook_type_missing")
        if not nonempty_value(text, "retention_reset_goal"):
            result.partial("dynamic_beat_map_retention_reset_goal_missing")
        for mapping_field in REHOOK_MAPPING_FIELDS:
            present = bool_value(text, mapping_field) is True
            result.checks[mapping_field] = present
            if not present:
                result.partial(f"recurring_rehook_mapping_missing:{mapping_field}")
        if bool_value(text, "rehooks_topic_connected") is not True:
            result.partial("recurring_rehooks_not_confirmed_topic_connected")
        if bool_value(text, "generic_rehooks_present") is True:
            result.fail("generic_rehooks_are_not_allowed")
        if bool_value(text, "cta_hook_present") is not True:
            result.partial("cta_hook_missing")
        if bool_value(text, "proof_based_rehook_present") is True:
            if not has_section(text, "FACT_VS_ANECDOTE_MAP"):
                result.fail("proof_based_rehook_missing_fact_vs_anecdote_map")
        rehook_rows = scoped_json_rows(text, "RECURRING_REHOOK_MAP", "rehook_row_json")
        required_rehook_fields = {
            "rehook_id",
            "hook_type",
            "hook_line",
            "retention_function",
            "emotional_trigger",
            "topic_connection",
            "beat_map_scene_id",
            "line_influence_reference",
        }
        invalid_rehook_rows: list[str] = []
        rehook_timestamps: list[int] = []
        final_script = section_text(text, "FINAL_SCRIPT")
        beat_map = section_text(text, "DYNAMIC_TIMED_BEAT_MAP")
        influence_map = section_text(text, "LINE_BY_LINE_INFLUENCE_MAP")
        for row in rehook_rows:
            row_id = str(row.get("rehook_id", "unknown"))
            timestamp = parse_timestamp_seconds(
                row.get("timestamp_seconds", row.get("timestamp_range"))
            )
            if (
                not required_rehook_fields.issubset(row)
                or timestamp is None
                or any(placeholder_value(row.get(field)) for field in required_rehook_fields)
            ):
                invalid_rehook_rows.append(row_id)
                continue
            rehook_timestamps.append(timestamp)
            if not normalized_contains(final_script, str(row["hook_line"])):
                invalid_rehook_rows.append(f"{row_id}:missing_from_final_script")
            if str(row["beat_map_scene_id"]) not in beat_map:
                invalid_rehook_rows.append(f"{row_id}:missing_from_beat_map")
            if str(row["line_influence_reference"]) not in influence_map:
                invalid_rehook_rows.append(f"{row_id}:missing_from_influence_map")
        duration_seconds = int(duration_minutes * 60)
        reset_points = [0, *sorted(set(rehook_timestamps))]
        if bool_value(text, "cta_hook_present") is True:
            reset_points.append(duration_seconds)
        calculated_max_gap = max(
            (right - left for left, right in zip(reset_points, reset_points[1:])),
            default=duration_seconds,
        )
        result.checks["rehook_rows_detected"] = len(rehook_rows)
        result.checks["internal_rehook_count"] = len(rehook_timestamps)
        result.checks["placeholder_rehooks_absent"] = not invalid_rehook_rows
        result.checks["calculated_max_gap_without_rehook_seconds"] = calculated_max_gap
        result.checks["rehooks_present_in_final_script"] = not any(
            "missing_from_final_script" in issue for issue in invalid_rehook_rows
        )
        result.checks["rehooks_present_in_beat_map"] = not any(
            "missing_from_beat_map" in issue for issue in invalid_rehook_rows
        )
        result.checks["rehooks_present_in_influence_map"] = not any(
            "missing_from_influence_map" in issue for issue in invalid_rehook_rows
        )
        if not rehook_rows:
            result.fail("recurring_rehook_map_has_no_structured_rows")
        if len(rehook_timestamps) < required_rehooks:
            result.fail(f"structured_rehook_rows_below_duration_minimum:{required_rehooks}")
        if invalid_rehook_rows:
            result.fail("invalid_or_unbound_rehook_rows:" + ",".join(invalid_rehook_rows))
        if calculated_max_gap > 90 and not interval_reason:
            result.fail("calculated_rehook_gap_exceeds_90_without_justification")

    if media_factory_final:
        scene_sync_present = has_section(text, "SCENE_SYNC_MATRIX")
        result.checks["scene_sync_matrix_present"] = scene_sync_present
        if not scene_sync_present:
            result.partial("scene_sync_matrix_missing_for_media_factory_final_draft")
        if bool_value(text, "scene_sync_matrix_complete") is not True:
            result.partial("scene_sync_matrix_not_complete")
        if bool_value(text, "media_contexts_synchronized") is not True:
            result.partial("media_contexts_not_synchronized")
        if bool_value(text, "rehooks_mapped_to_scene_sync_matrix") is not True:
            result.partial("recurring_rehooks_not_mapped_to_scene_sync_matrix")
        if bool_value(text, "influence_map_creative_depth_complete") is not True:
            result.partial("line_by_line_influence_map_is_shallow")
        if bool_value(text, "repo_lineage_only") is True:
            result.fail("line_by_line_influence_map_is_repo_lineage_only")
        for influence_field in INFLUENCE_DEPTH_FIELDS:
            present = nonempty_value(text, influence_field)
            result.checks[f"influence_{influence_field}_present"] = present
            if not present:
                result.partial(f"line_by_line_influence_field_missing:{influence_field}")
        scene_rows = scoped_json_rows(text, "SCENE_SYNC_MATRIX", "scene_row_json")
        schema_path = REPO_ROOT / "schemas/media_factory/scene_sync_matrix.schema.json"
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        scene_errors: list[str] = []
        rehook_scene_rows = 0
        for row in scene_rows:
            scene_id = str(row.get("scene_id", "unknown"))
            row_errors = recursive_schema_errors(row, schema, scene_id)
            scene_errors.extend(row_errors)
            if row.get("hook_marker") is True and row.get("rehook_type") != "opening_hook":
                rehook_scene_rows += 1
        required_scene_rehooks = len(
            scoped_json_rows(text, "RECURRING_REHOOK_MAP", "rehook_row_json")
        )
        result.checks["scene_rows_detected"] = len(scene_rows)
        result.checks["scene_sync_schema_validation_pass"] = not scene_errors
        result.checks["rehook_scene_rows"] = rehook_scene_rows
        result.checks["rehook_rows_synchronized"] = rehook_scene_rows >= required_scene_rehooks
        if not scene_rows:
            result.fail("scene_sync_matrix_has_no_structured_rows")
        if scene_errors:
            result.fail("scene_sync_schema_validation_failed:" + ",".join(scene_errors))
        if rehook_scene_rows < required_scene_rehooks:
            result.fail("scene_sync_matrix_missing_rehook_rows")

    mandatory_gate_keys = [
        "source_research_lock_status",
        "language_body_gate_status",
        "rehook_reality_gate_status",
        "source_ledger_gate_status",
        "fact_vs_anecdote_gate_status",
        "scene_sync_gate_status",
        "media_factory_sync_lock_status",
        "quality_lock_status",
        "governance_lock_status",
    ]
    weak_gate_values = {"PARTIAL", "FAIL", "BLOCKED", "NEEDS_CONFIRMATION"}
    weakest_gate_rows: list[str] = []
    for key in mandatory_gate_keys:
        value = key_value(text, key)
        normalized = value.strip("`\"' ").upper() if value else ""
        if normalized in weak_gate_values:
            weakest_gate_rows.append(f"{key}={normalized}")
    result.checks["weakest_gate_rows_detected"] = len(weakest_gate_rows)
    if weakest_gate_rows:
        result.partial("mandatory_gate_not_pass:" + ",".join(weakest_gate_rows))
    proof_status = final_proof_status(text)
    result.checks["final_proof_status_present"] = proof_status is not None
    if proof_status == "PASS" and (result.errors or result.partials):
        result.fail("final_proof_status_does_not_match_weakest_evidence_layer")

    return result


def valid_full_fixture() -> str:
    sections = "\n".join(f"{section}\nstatus=present" for section in FULL_CONTENT_ENGINEERING_SECTIONS)
    return f"""
platform=YouTube
script_duration_minutes=5
cinematic_story_required=true
real_person_used=true
SCRIPT_LANGUAGE_DECLARATION
master_script_language=English
translation_stage_required=true
non_english_generation_allowed=false
language_inference_blocked=true
USER_LANGUAGE_REQUEST_CHECK
explicit_language_requested=false
requested_language=not specified
output_language_decision=English master draft
web_required=true
web_access_used=true
source_list_present=true
real_time_sources_used=true
real_time_research_claimed=true
unsupported_claims=[]
source_research_lock_status=PASS
SOURCE_LEDGER
source_id=source_1
url=https://example.com/official
source_type=official_source
source_id=source_2
url=https://example.com/news
source_type=credible_news_article
source_id=source_3
url=https://example.com/interview
source_type=interview_reporting
final_proof_classification=PASS
explicit_script_only_request=false
{sections}
duration_target_seconds=60
story_basis=real_person_public_arc
cinematic_reconstruction=true
verified_scene_details=false
character=Yash
setting=early career
conflict=limited resources and ambition
stakes=career growth under rejection
turning_point=reinvesting effort into craft
cinematic_visuals=night practice and disciplined work
emotional_peak=choosing long-term growth over display
lesson_bridge=invest in your own development
topic_connection=self-investment under rejection
source_references=[https://example.com/source]
beat_duration_dynamic=true
uniform_15_second_grid=false
scene_id=scene_01
start_time=00:00
end_time=00:06
duration_seconds=6
duration_reason=fast hook
spoken_line_or_summary=stop scrolling
scene_purpose=hook
emotional_cue=urgency
voice_cue=firm
visual_cue=phone close-up
avatar_cue=direct eye contact
broll_or_image_cue=scrolling hand
music_sfx_cue=impact
transition_cue=hard cut
platform_dependency=YouTube long-form
local_cloud_hybrid_dependency=local edit with cloud-optional visuals
opening_hook_present=true
recurring_rehook_required=true
recurring_rehook_count=3
rehook_interval_seconds=80
max_gap_without_rehook_seconds=80
rehook_interval_dynamic=true
rehook_interval_reason_present=true
rehooks_mapped_to_final_script=true
rehooks_mapped_to_dynamic_beat_map=true
rehooks_mapped_to_editing_context=true
rehooks_mapped_to_line_influence_map=true
rehooks_topic_connected=true
generic_rehooks_present=false
cta_hook_present=true
proof_based_rehook_present=true
hook_marker=true
rehook_type=curiosity_rehook
retention_reset_goal=reset attention before the next major section
local_options=local render and edit
cloud_options=cloud-optional visual render
hybrid_strategy=local assembly with cloud-optional assets
fallback=local context-only handoff
"""


def run_self_test() -> int:
    cases = [
        ("valid_full_packet", valid_full_fixture(), "PASS"),
        (
            "missing_story_block_with_inflated_pass",
            valid_full_fixture().replace("CINEMATIC_SHORT_STORY_BLOCK\nstatus=present\n", ""),
            "FAIL",
        ),
        (
            "missing_story_block_with_honest_partial",
            valid_full_fixture()
            .replace("CINEMATIC_SHORT_STORY_BLOCK\nstatus=present\n", "")
            .replace("final_proof_classification=PASS", "final_proof_classification=PARTIAL"),
            "PARTIAL",
        ),
        (
            "unsupported_claims_cannot_pass",
            valid_full_fixture().replace("unsupported_claims=[]", "unsupported_claims=[unverified career claim]"),
            "FAIL",
        ),
        (
            "real_person_requires_web",
            valid_full_fixture()
            .replace("web_required=true", "web_required=false")
            .replace("web_access_used=true", "web_access_used=false"),
            "FAIL",
        ),
        (
            "explicit_script_only_allowed",
            """
explicit_script_only_request=true
SCRIPT_LANGUAGE_DECLARATION
master_script_language=English
USER_LANGUAGE_REQUEST_CHECK
explicit_language_requested=false
web_required=false
unsupported_claims=[]
final_proof_classification=PASS
FINAL_SCRIPT
Only the requested script.
""",
            "PASS",
        ),
        (
            "default_hindi_master_script_rejected",
            valid_full_fixture().replace("master_script_language=English", "master_script_language=Hindi"),
            "FAIL",
        ),
        (
            "realtime_claim_without_realtime_sources_rejected",
            valid_full_fixture().replace("real_time_sources_used=true", "real_time_sources_used=false"),
            "FAIL",
        ),
        (
            "single_encyclopedia_authority_cannot_pass",
            re.sub(
                r"SOURCE_LEDGER\nsource_id=source_1.*?source_type=interview_reporting\n",
                "SOURCE_LEDGER\nsource_id=source_1\nurl=https://example.com/wiki\nsource_type=encyclopedia_background\n",
                valid_full_fixture(),
                flags=re.S,
            ),
            "FAIL",
        ),
        (
            "anecdote_used_as_fact_rejected",
            valid_full_fixture() + "\nanecdote_used_as_verified_fact=true\n",
            "FAIL",
        ),
        (
            "uniform_15_second_grid_without_reason_rejected",
            valid_full_fixture().replace("uniform_15_second_grid=false", "uniform_15_second_grid=true"),
            "FAIL",
        ),
        (
            "local_cloud_hybrid_plan_fields_required",
            valid_full_fixture().replace("fallback=local context-only handoff", "fallback="),
            "FAIL",
        ),
        (
            "opening_hook_only_rejected",
            valid_full_fixture()
            .replace("recurring_rehook_count=3", "recurring_rehook_count=0")
            .replace("rehooks_mapped_to_final_script=true", "rehooks_mapped_to_final_script=false"),
            "FAIL",
        ),
        (
            "rehook_gap_above_90_without_reason_rejected",
            valid_full_fixture()
            .replace("max_gap_without_rehook_seconds=80", "max_gap_without_rehook_seconds=100")
            .replace("rehook_interval_reason_present=true", "rehook_interval_reason_present=false"),
            "FAIL",
        ),
        (
            "media_factory_final_requires_scene_sync",
            valid_full_fixture() + "\nmedia_factory_final_draft_requested=true\n",
            "FAIL",
        ),
        (
            "media_factory_final_with_scene_sync_passes",
            valid_full_fixture()
            + """
media_factory_final_draft_requested=true
SCENE_SYNC_MATRIX
scene_sync_matrix_complete=true
media_contexts_synchronized=true
influence_map_creative_depth_complete=true
rehooks_mapped_to_scene_sync_matrix=true
repo_lineage_only=false
why_line_exists=establishes urgency
emotion_triggered=resolve
retention_function=opens a curiosity loop
topic_support=connects action to self-investment
media_dependency=voice emphasis and hard-cut visual
""",
            "PASS",
        ),
    ]
    results = []
    for name, fixture, expected in cases:
        actual = validate(fixture)
        results.append(
            {
                "name": name,
                "expected": expected,
                "actual": actual.classification,
                "passed": actual.classification == expected,
                "errors": actual.errors,
                "partials": actual.partials,
            }
        )
    passed = all(item["passed"] for item in results)
    print(json.dumps({"self_test_passed": passed, "tests": results}, indent=2))
    return 0 if passed else 1


# MAC-06.2P1 structured fixtures supersede the legacy marker-oriented fixtures
# above. They stay nearby so prior evidence remains readable in git history.
def json_row(key: str, row: dict) -> str:
    return f"{key}={json.dumps(row, separators=(',', ':'))}"


def fixture_rehooks() -> list[dict]:
    return [
        {
            "rehook_id": "rehook_1",
            "timestamp_seconds": 75,
            "hook_type": "question_rehook",
            "hook_line": "What if the comfort you defend is the reason you stay stuck?",
            "retention_function": "reset attention before the practical framework",
            "emotional_trigger": "productive discomfort",
            "topic_connection": "self-investment requires redirecting attention",
            "beat_map_scene_id": "scene_075",
            "line_influence_reference": "influence_rehook_1",
        },
        {
            "rehook_id": "rehook_2",
            "timestamp_seconds": 150,
            "hook_type": "proof_rehook",
            "hook_line": "The question is not whether growth costs money. The question is what staying unchanged will cost you.",
            "retention_function": "raise the cost of inaction before the proof section",
            "emotional_trigger": "loss aversion",
            "topic_connection": "self-investment compounds while delay compounds regret",
            "beat_map_scene_id": "scene_150",
            "line_influence_reference": "influence_rehook_2",
        },
        {
            "rehook_id": "rehook_3",
            "timestamp_seconds": 225,
            "hook_type": "contrarian_rehook",
            "hook_line": "Motivation is not the finish line. It is the moment you choose a harder calendar.",
            "retention_function": "convert emotion into action before the roadmap",
            "emotional_trigger": "resolve",
            "topic_connection": "self-investment must become scheduled behavior",
            "beat_map_scene_id": "scene_225",
            "line_influence_reference": "influence_rehook_3",
        },
    ]


def fixture_scene(row: dict) -> dict:
    seconds = row["timestamp_seconds"]
    return {
        "scene_id": row["beat_map_scene_id"],
        "start_time": f"{seconds // 60:02d}:{seconds % 60:02d}",
        "end_time": f"{seconds // 60:02d}:{seconds % 60 + 6:02d}",
        "duration_seconds": 6,
        "duration_reason": "short pattern interrupt at an attention-reset moment",
        "hook_marker": True,
        "rehook_type": row["hook_type"],
        "retention_reset_goal": row["retention_function"],
        "script": {
            "spoken_text": row["hook_line"],
            "line_intent": row["topic_connection"],
            "retention_function": row["retention_function"],
        },
        "voice": {
            "tone": "firm",
            "emotion": row["emotional_trigger"],
            "pacing": "brief acceleration then pause",
            "pause_points": ["after the re-hook"],
            "pronunciation_notes": [],
        },
        "image": {
            "prompt": "A focused creator closes a distracting phone and opens a notebook.",
            "style": "cinematic realism",
            "lighting": "high-contrast warm desk light",
            "composition": "tight foreground action with clean caption space",
        },
        "video": {
            "shot_type": "close-up",
            "camera_motion": "fast push-in then hold",
            "duration": 6,
            "continuity_notes": "match the surrounding self-investment sequence",
        },
        "music_sfx": {"music_mood": "rising resolve", "sfx": ["soft impact"]},
        "editing": {
            "cut_type": "hard cut",
            "transition": "pattern interrupt",
            "caption_style": "single emphasized phrase",
        },
        "platform": {
            "target": "YouTube long-form",
            "aspect_ratio": "16:9",
            "safe_zone": "center-safe captions",
        },
        "influence": {
            "why_line_exists": row["retention_function"],
            "emotion_triggered": row["emotional_trigger"],
            "retention_goal": "restore attention",
            "topic_support": row["topic_connection"],
        },
        "execution": {
            "local_possible": True,
            "cloud_possible": True,
            "hybrid_recommended": True,
            "fallback_provider_or_tool": "local edit with context-only visual placeholder",
        },
        "provider_execution_allowed": False,
    }


def valid_full_fixture() -> str:
    sections = "\n".join(f"{section}\nstatus=present" for section in FULL_CONTENT_ENGINEERING_SECTIONS)
    source_rows = [
        {"source_id": "source_1", "url": "https://example.com/official", "title": "Official profile", "date": "2026-06-02", "source_type": "official_source", "claim_supported": "career identity", "limitation": "official summary only"},
        {"source_id": "source_2", "url": "https://example.com/news", "title": "Career interview coverage", "date": "2026-05-20", "source_type": "credible_news_article", "claim_supported": "career arc", "limitation": "secondary reporting"},
        {"source_id": "source_3", "url": "https://example.com/interview", "title": "Direct interview", "date": "2026-05-18", "source_type": "interview_reporting", "claim_supported": "reported anecdote", "limitation": "anecdotal support only"},
    ]
    fact_rows = [
        {"claim": "The public career arc supports a self-investment theme.", "source": "source_1 + source_2", "classification": "CROSS_VERIFIED", "script_usage_allowed": True, "risk_note": "Use as a broad arc, not a reconstructed scene."},
        {"claim": "An interview anecdote can add emotional context.", "source": "source_3", "classification": "ANECDOTAL_SUPPORT", "script_usage_allowed": "anecdotal_support_only", "risk_note": "Do not present the anecdote as independent factual proof."},
    ]
    rehooks = fixture_rehooks()
    script_body = " ".join([
        "Stop scrolling. Your future needs a real investment plan.",
        rehooks[0]["hook_line"],
        "Choose one skill and protect time for deliberate practice.",
        rehooks[1]["hook_line"],
        "Treat your time and money like seeds for the person you are building.",
        rehooks[2]["hook_line"],
        "Start today. Put one action on your calendar and follow through.",
    ])
    return f"""
platform=YouTube
script_duration_minutes=5
cinematic_story_required=true
real_person_used=true
explicit_script_only_request=false
SCRIPT_LANGUAGE_DECLARATION
master_script_language=English
translation_stage_required=true
USER_LANGUAGE_REQUEST_CHECK
explicit_language_requested=false
web_required=true
web_access_used=true
source_list_present=true
real_time_sources_used=true
real_time_research_claimed=true
unsupported_claims=[]
source_research_lock_status=PASS
final_status=PASS
{sections}
SOURCE_LEDGER
{chr(10).join(json_row("source_row_json", row) for row in source_rows)}
FACT_VS_ANECDOTE_MAP
{chr(10).join(json_row("fact_map_row_json", row) for row in fact_rows)}
CINEMATIC_SHORT_STORY_BLOCK
duration_target_seconds=60
story_basis=real_person_public_arc
cinematic_reconstruction=true
verified_scene_details=false
character=Yash
setting=early career
conflict=limited resources and ambition
stakes=career growth under rejection
turning_point=reinvesting effort into craft
cinematic_visuals=disciplined work and deliberate practice
emotional_peak=choosing long-term growth over display
lesson_bridge=invest in your own development
topic_connection=self-investment under rejection
source_references=[source_1,source_2]
RECURRING_REHOOK_MAP
{chr(10).join(json_row("rehook_row_json", row) for row in rehooks)}
FINAL_SCRIPT
script_body={script_body}
DYNAMIC_TIMED_BEAT_MAP
beat_duration_dynamic=true
uniform_15_second_grid=false
scene_id=scene_001
start_time=00:00
end_time=00:06
duration_seconds=6
duration_reason=fast hook
spoken_line_or_summary=stop scrolling
scene_purpose=hook
emotional_cue=urgency
voice_cue=firm
visual_cue=phone close-up
avatar_cue=direct eye contact
broll_or_image_cue=scrolling hand
music_sfx_cue=impact
transition_cue=hard cut
platform_dependency=YouTube long-form
local_cloud_hybrid_dependency=local edit with cloud-optional visuals
beat_map_scene_id=scene_075
beat_map_scene_id=scene_150
beat_map_scene_id=scene_225
LINE_BY_LINE_INFLUENCE_MAP
line_influence_reference=influence_rehook_1
line_influence_reference=influence_rehook_2
line_influence_reference=influence_rehook_3
opening_hook_present=true
recurring_rehook_required=true
recurring_rehook_count=3
max_gap_without_rehook_seconds=75
rehook_interval_dynamic=true
rehook_interval_reason_present=true
rehooks_mapped_to_final_script=true
rehooks_mapped_to_dynamic_beat_map=true
rehooks_mapped_to_editing_context=true
rehooks_mapped_to_line_influence_map=true
rehooks_topic_connected=true
generic_rehooks_present=false
cta_hook_present=true
proof_based_rehook_present=true
hook_marker=true
rehook_type=curiosity_rehook
retention_reset_goal=reset attention before the next major section
local_options=local render and edit
cloud_options=cloud-optional visual render
hybrid_strategy=local assembly with cloud-optional assets
fallback=local context-only handoff
"""


def valid_media_fixture() -> str:
    scenes = "\n".join(json_row("scene_row_json", fixture_scene(row)) for row in fixture_rehooks())
    return valid_full_fixture() + f"""
media_factory_final_draft_requested=true
SCENE_SYNC_MATRIX
scene_sync_matrix_complete=true
media_contexts_synchronized=true
influence_map_creative_depth_complete=true
rehooks_mapped_to_scene_sync_matrix=true
repo_lineage_only=false
why_line_exists=establishes urgency
emotion_triggered=resolve
retention_function=opens a curiosity loop
topic_support=connects action to self-investment
media_dependency=voice emphasis and hard-cut visual
{scenes}
"""


def run_self_test() -> int:
    remove_rows = lambda text, key: re.sub(rf"(?m)^{key}=.*\n?", "", text)
    cases = [
        ("valid_full_packet", valid_full_fixture(), "PASS"),
        ("neg_lang_hinglish_body_declared_english", re.sub(r"script_body=.*", "script_body=Tum aaj bhi scroll kar rahe ho. Kya tum khud pe paisa aur waqt invest karoge ya nahi?", valid_full_fixture()), "FAIL"),
        ("neg_rehook_heading_without_rows", remove_rows(valid_full_fixture(), "rehook_row_json"), "FAIL"),
        ("neg_rehook_rows_missing_from_final_script", valid_full_fixture().replace("What if the comfort you defend is the reason you stay stuck?", "What if your habits quietly decide your future?", 1), "FAIL"),
        ("neg_rehook_gap_above_90", valid_full_fixture().replace('"timestamp_seconds":75', '"timestamp_seconds":110').replace("rehook_interval_reason_present=true", "rehook_interval_reason_present=false"), "FAIL"),
        ("neg_source_heading_without_rows", remove_rows(valid_full_fixture(), "source_row_json"), "FAIL"),
        ("neg_source_urls_outside_ledger_ignored", remove_rows(valid_full_fixture(), "source_row_json") + "\nurl=https://outside.example/one\nurl=https://outside.example/two\nurl=https://outside.example/three\n", "FAIL"),
        ("neg_fact_heading_without_rows", remove_rows(valid_full_fixture(), "fact_map_row_json"), "FAIL"),
        ("neg_fact_anecdote_as_verified", valid_full_fixture().replace('"script_usage_allowed":"anecdotal_support_only"', '"script_usage_allowed":true'), "FAIL"),
        ("neg_scene_heading_without_rows", valid_full_fixture() + "\nmedia_factory_final_draft_requested=true\nSCENE_SYNC_MATRIX\nscene_sync_matrix_complete=true\nmedia_contexts_synchronized=true\nrehooks_mapped_to_scene_sync_matrix=true\n", "FAIL"),
        ("neg_scene_missing_nested_context", valid_media_fixture().replace('"voice":{"tone":"firm","emotion":"productive discomfort","pacing":"brief acceleration then pause","pause_points":["after the re-hook"],"pronunciation_notes":[]},', "", 1), "FAIL"),
        ("neg_status_final_status_alias", valid_full_fixture().replace("source_research_lock_status=PASS", "source_research_lock_status=PARTIAL"), "FAIL"),
        ("neg_unsupported_claims", valid_full_fixture().replace("unsupported_claims=[]", "unsupported_claims=[unverified claim]"), "FAIL"),
        ("neg_realtime_claim_without_sources", valid_full_fixture().replace("real_time_sources_used=true", "real_time_sources_used=false"), "FAIL"),
        ("neg_uniform_grid_without_reason", valid_full_fixture().replace("uniform_15_second_grid=false", "uniform_15_second_grid=true"), "FAIL"),
        ("neg_one_hook_only", remove_rows(valid_full_fixture(), "rehook_row_json").replace("recurring_rehook_count=3", "recurring_rehook_count=0"), "FAIL"),
        ("neg_media_factory_requires_scene_rows", valid_full_fixture() + "\nmedia_factory_final_draft_requested=true\nSCENE_SYNC_MATRIX\n", "FAIL"),
        ("valid_media_factory_scene_sync", valid_media_fixture(), "PASS"),
    ]
    results = []
    for name, fixture, expected in cases:
        actual = validate(fixture)
        results.append({"name": name, "expected": expected, "actual": actual.classification, "passed": actual.classification == expected, "errors": actual.errors, "partials": actual.partials})
    marker_only_rejected = not responsibility_specific_enforcement("DIRECTOR", f"# {PROPAGATION_MARKER}\n")
    dag_aligned, dag_details = m039_dag_alignment()
    results.extend([
        {"name": "neg_prop_marker_only_actor", "expected": True, "actual": marker_only_rejected, "passed": marker_only_rejected},
        {"name": "m039_executable_dag_alignment", "expected": True, "actual": dag_aligned, "passed": dag_aligned, "details": dag_details},
    ])
    passed = all(item["passed"] for item in results)
    print(json.dumps({"self_test_passed": passed, "tests": results}, indent=2))
    return 0 if passed else 1


def reality_check_report(result: ValidationResult) -> dict[str, dict[str, object]]:
    checks = result.checks
    return {
        "SCRIPT_BODY_LANGUAGE_CHECK": {
            "detected_body_language": checks.get("script_body_language_detected"),
            "non_english_token_ratio": checks.get("script_body_non_english_ratio"),
            "language_body_gate_status": "PASS" if checks.get("script_body_language_matches_default") else "FAIL",
        },
        "REHOOK_REALITY_CHECK": {
            "rehook_rows_detected": checks.get("rehook_rows_detected"),
            "internal_rehook_count": checks.get("internal_rehook_count"),
            "max_gap_without_rehook_seconds": checks.get("calculated_max_gap_without_rehook_seconds"),
            "rehook_reality_gate_status": "PASS" if checks.get("placeholder_rehooks_absent") else "FAIL",
        },
        "SOURCE_LEDGER_REALITY_CHECK": {
            "ledger_source_rows_detected": checks.get("ledger_source_rows_detected"),
            "ledger_urls_count": checks.get("ledger_urls_count"),
            "urls_outside_ledger_ignored": checks.get("urls_outside_ledger_ignored"),
            "source_ledger_gate_status": "PASS" if checks.get("source_ledger_rows_complete") else "FAIL",
        },
        "FACT_VS_ANECDOTE_REALITY_CHECK": {
            "fact_map_rows_detected": checks.get("fact_map_rows_detected"),
            "fact_vs_anecdote_gate_status": "PASS" if checks.get("fact_vs_anecdote_rows_complete") else "FAIL",
        },
        "SCENE_SYNC_REALITY_CHECK": {
            "scene_rows_detected": checks.get("scene_rows_detected"),
            "schema_validation_status": "PASS" if checks.get("scene_sync_schema_validation_pass") else "FAIL",
            "rehook_rows_synchronized": checks.get("rehook_rows_synchronized"),
        },
        "WEAKEST_GATE_REALITY_CHECK": {
            "final_status_detected": checks.get("final_proof_status_present"),
            "weakest_gate_rows_detected": checks.get("weakest_gate_rows_detected"),
            "weakest_gate_status": "PASS" if not result.errors and not result.partials else result.classification,
        },
        "PROPAGATION_REALITY_CHECK": {
            "marker_only_files_absent": checks.get("marker_only_files_absent"),
            "responsibility_enforced_files": checks.get("responsibility_enforced_files"),
            "propagation_reality_gate_status": "PASS" if checks.get("repo_wide_propagation_complete") else "FAIL",
        },
        "M039_DAG_ALIGNMENT": {
            "m039_dag_present": checks.get("m039_m039_dag_present"),
            "s202_executes_directly": checks.get("m039_s202_executes_directly"),
            "typed_rehook_packet_bound": checks.get("m039_typed_rehook_packet_bound"),
            "dag_alignment_status": "PASS" if checks.get("m039_typed_rehook_packet_bound") else "FAIL",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output_file", nargs="?")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        return run_self_test()
    if not args.output_file:
        parser.error("output_file is required unless --self-test is used")
    text = Path(args.output_file).read_text(encoding="utf-8")
    result = validate(text)
    print(
        json.dumps(
            {
                "classification": result.classification,
                "errors": result.errors,
                "partials": result.partials,
                "checks": result.checks,
                "reality_checks": reality_check_report(result),
            },
            indent=2,
            sort_keys=True,
        )
    )
    return 0 if result.classification == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
