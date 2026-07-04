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
    "SCRIPT_BODY_DEPTH_LOCK",
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
    "SEMANTIC_INFLUENCE_MAP",
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

NAMED_REAL_PERSON_HINTS = [
    "public figure test anchor",
    "case study actor",
    "verified founder",
    "yash",
    "naveen kumar gowda",
    "rocky bhai",
    "kgf",
]

CUSTOM_INVALID_STATUS_TOKENS = {
    "PASS_WITH_NOTICE",
    "PASS_WITH_REFINEMENT",
    "READY_FOR_USER_DECISION",
}

SCRIPT_ALIGNMENT_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "because", "by", "for", "from",
    "had", "has", "have", "he", "her", "his", "i", "if", "in", "into", "is",
    "it", "its", "me", "my", "of", "on", "or", "our", "she", "so", "that",
    "the", "their", "them", "they", "this", "to", "was", "we", "were", "what",
    "when", "who", "with", "you", "your",
}
FACT_ALIGNMENT_HINT_VERBS = {
    "arrived", "asked", "boarded", "branded", "called", "crossed", "drove",
    "earned", "founded", "grossed", "joined", "left", "made", "moved",
    "performed", "rose", "said", "served", "skipped", "slept", "spent",
    "started", "swept", "trained", "won", "worked",
}
ABSOLUTE_CLAIM_TOKENS = {
    "every", "always", "never", "only", "all", "entire", "zero shortcuts",
}
OFF_TOPIC_PROMO_PATTERNS = [
    "upcoming film",
    "upcoming movie",
    "watch out for",
    "teaser",
    "trailer",
    "linked above",
    "linked below",
    "i've linked",
    "directed by",
    "coming soon",
]
DRAMATIZATION_MARKERS = [
    "rain-soaked",
    "ceiling fan",
    "mirror",
    "dusty theater spotlight",
    "dust motes",
    "slow-motion",
    "counting coins",
    "slept on the theater floors",
]
MEDIA_CONTEXT_SECTIONS = [
    "VOICE_GENERATION_CONTEXT",
    "IMAGE_GENERATION_CONTEXT",
    "VIDEO_GENERATION_CONTEXT",
    "MUSIC_AND_SFX_CONTEXT",
    "EDITING_CONTEXT",
    "PLATFORM_PACKAGING",
]

MEDIA_FACTORY_PRODUCTION_BASE_SECTIONS = [
    "PRODUCTION_ORDER_LOCK",
    "ASSET_INVENTORY_LEDGER",
    "ASSET_DEPENDENCY_GRAPH",
    "CONTROL_PANEL_EXECUTION_PLAN",
    "DAVINCI_TIMELINE_PACKET",
    "PRODUCTION_PROOF_GATE",
]

MEDIA_FACTORY_EXECUTION_PACKET_SECTIONS = [
    "MISSION_MEDIA_OUTPUT_BUNDLE",
    "SCENE_EXECUTION_BLOCKS",
]

GENERATOR_BATCH_PLAN_SECTIONS = [
    "VOICE_BATCH_PLAN",
    "A_ROLL_BATCH_PLAN",
    "MUSIC_SFX_BATCH_PLAN",
    "IMAGE_BATCH_PLAN",
    "CINEMATIC_BROLL_BATCH_PLAN",
    "MOTION_GRAPHICS_BATCH_PLAN",
    "ASSEMBLY_SYNC_PLAN",
]

REPO_WRITE_APPROVAL_KEYS = [
    "repo_write_approved",
    "repo_write_for_visual_plan_approved",
    "repo_write_for_generation_bundle_approved",
    "consolidated_repo_write_mode_approved",
    "user_approved_repo_write",
]

VISUAL_PLAN_FILE_WRITE_MARKERS = [
    "implementation_plan.md",
    "task.md",
    "file_created=true",
    "folder_created=true",
    "documents_created=true",
    "folders_created=true",
    "repo_write_used=true",
    "created_file=",
    "created_folder=",
    "wrote_file=",
    "updated_file=",
]

PRODUCTION_ORDER_PHASES = [
    "freeze_approved_script_and_scene_ids",
    "generate_or_confirm_scene_sync_matrix",
    "generate_master_voice_track",
    "align_voice_timestamps_to_scene_rows",
    "generate_music_segments",
    "generate_individual_sfx_clips",
    "generate_character_consistency_reference_assets",
    "generate_storyboard_and_still_image_assets",
    "render_hyperframes_slides_cards_and_alpha_overlays",
    "generate_depth_maps_for_still_parallax_assets",
    "generate_heygen_a_roll_batches",
    "generate_premium_cinematic_b_roll_clips",
    "build_davinci_timeline_from_packet",
    "assemble_v1_v2_v3_and_a1_to_a5_tracks",
    "qc_sync_captions_safe_zones_color_and_audio",
    "export_youtube_master",
    "collect_proofs_and_update_registry",
]

ASSET_INVENTORY_CLASSES = [
    "voice_assets",
    "music_segments",
    "sfx_clips",
    "character_consistency_assets",
    "storyboard_stills",
    "depth_parallax_stills",
    "hyperframes_slide_assets",
    "hyperframes_overlay_assets",
    "cinematic_broll_clips",
    "a_roll_batches",
    "davinci_project_assets",
    "thumbnail_assets",
]

DAVINCI_TRACKS = ["V1", "V2", "V3", "A1", "A2", "A3", "A4", "A5"]
PRODUCTION_PHASE_REQUIRED_FIELDS = {
    "phase_id",
    "phase_order",
    "phase_name",
    "depends_on_phase_ids",
    "blocking_prerequisites",
    "output_asset_classes",
    "execution_mode",
    "approval_gate",
    "proof_gate",
    "status",
}
CONTROL_PANEL_PHASE_REQUIRED_FIELDS = {
    "phase_id",
    "plan_state",
    "control_panel_entrypoint",
    "preflight_dependency",
    "downgrade_on_failure",
    "proof_artifacts",
    "status",
}
CONTROL_PANEL_ALLOWED_STATES = {
    "plan_only",
    "preflight",
    "ready_after_approval",
    "blocked",
    "blocked_until_required_assets_exist",
    "requires_confirmation",
    "completed_with_proof",
}
CANONICAL_MEDIA_FACTORY_PHASE_IDS = [
    f"P{index:02d}" for index in range(1, len(PRODUCTION_ORDER_PHASES) + 1)
]
SCENE_EXECUTION_REQUIRED_FIELDS = {
    "scene_id",
    "visual_method",
    "generation_stage",
    "primary_tool_or_provider",
    "input_dependencies",
    "output_path",
    "naming_convention",
    "handoff_target",
    "proof_gate",
    "status",
}
MISSION_MEDIA_OUTPUT_REQUIRED_MARKERS = [
    "mission_root=",
    "consolidated_plan_doc=",
    "scene_packets_dir=",
    "voice_dir=",
    "music_dir=",
    "sfx_dir=",
    "images_dir=",
    "broll_dir=",
    "aroll_dir=",
    "hyperframes_dir=",
    "davinci_dir=",
    "proofs_dir=",
    "supporting_image_generation_txt=",
    "supporting_voice_generation_txt=",
    "supporting_music_sfx_txt=",
    "supporting_editing_txt=",
    "supporting_hyperframes_txt=",
    "cleanup_policy=keep_required_delete_temporary",
]
PRODUCTION_PHASE_DEPENDENCY_MINIMUMS = {
    "generate_or_confirm_scene_sync_matrix": {"freeze_approved_script_and_scene_ids"},
    "generate_master_voice_track": {"generate_or_confirm_scene_sync_matrix"},
    "align_voice_timestamps_to_scene_rows": {"generate_master_voice_track"},
    "generate_music_segments": {"align_voice_timestamps_to_scene_rows"},
    "generate_individual_sfx_clips": {"align_voice_timestamps_to_scene_rows"},
    "generate_character_consistency_reference_assets": {"generate_or_confirm_scene_sync_matrix"},
    "generate_storyboard_and_still_image_assets": {"generate_or_confirm_scene_sync_matrix"},
    "render_hyperframes_slides_cards_and_alpha_overlays": {"generate_storyboard_and_still_image_assets"},
    "generate_depth_maps_for_still_parallax_assets": {"generate_storyboard_and_still_image_assets"},
    "generate_heygen_a_roll_batches": {"generate_master_voice_track"},
    "generate_premium_cinematic_b_roll_clips": {"generate_storyboard_and_still_image_assets"},
    "build_davinci_timeline_from_packet": {
        "align_voice_timestamps_to_scene_rows",
        "generate_music_segments",
        "generate_individual_sfx_clips",
        "render_hyperframes_slides_cards_and_alpha_overlays",
        "generate_depth_maps_for_still_parallax_assets",
        "generate_heygen_a_roll_batches",
        "generate_premium_cinematic_b_roll_clips",
    },
    "assemble_v1_v2_v3_and_a1_to_a5_tracks": {"build_davinci_timeline_from_packet"},
    "qc_sync_captions_safe_zones_color_and_audio": {"assemble_v1_v2_v3_and_a1_to_a5_tracks"},
    "export_youtube_master": {"qc_sync_captions_safe_zones_color_and_audio"},
    "collect_proofs_and_update_registry": {"export_youtube_master"},
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

LEDGER_SECTIONS = [
    "DIRECTOR_CONSUMPTION_LEDGER",
    "AGENT_CONSUMPTION_LEDGER",
    "SUBAGENT_CONSUMPTION_LEDGER",
    "SKILL_CONSUMPTION_LEDGER",
    "SUBSKILL_CONSUMPTION_LEDGER",
]
EVIDENCE_LINEAGE_SECTIONS = [
    "RULE_CONSUMPTION_EVIDENCE_LEDGER",
    "EXACT_RULE_LINEAGE_MAP",
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


def any_bool_value(text: str, keys: list[str]) -> bool:
    return any(bool_value(text, key) is True for key in keys)


def int_value(text: str, key: str) -> int | None:
    value = key_value(text, key)
    if value is None:
        return None
    match = re.search(r"-?\d+", value)
    return int(match.group(0)) if match else None


def bounded_int_value(text: str, key: str) -> int | None:
    """Read integer fields, including keys that contain dots such as AGENTS.md_read_count."""
    return int_value(text, key)


def line_ref_present(text: str, path: str) -> bool:
    return bool(re.search(rf"(?m){re.escape(path)}#L\d+", text))


def audit_lists_path(text: str, path_fragment: str) -> bool:
    body = section_text(text, "ROUTE_SCOPE_FILE_AUDIT")
    return path_fragment in body


def explicit_read_true(text: str, key: str) -> bool:
    return bool_value(text, key) is True


def section_pos_or_end(text: str, section: str) -> int:
    pos = section_position(text, section)
    return pos if pos >= 0 else len(text) + 1


def semantic_influence_present(text: str) -> bool:
    return has_section(text, "SEMANTIC_INFLUENCE_MAP") or (
        bool_value(text, "semantic_influence_map_present") is True
    )


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


def section_position(text: str, section: str) -> int:
    matches = list(re.finditer(rf"(?m)^{re.escape(section)}\s*$", text))
    return matches[-1].start() if matches else -1


def placeholder_value(value: object) -> bool:
    if isinstance(value, str):
        lowered = value.strip().lower()
        return not lowered or any(
            token in lowered
            for token in ["tbd", "placeholder", "coming soon", "needs_creative", "sample"]
        )
    return False


def normalized_list_value(value: object) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if value is None:
        return []
    if isinstance(value, str):
        raw = value.strip()
        if raw.startswith("[") and raw.endswith("]"):
            raw = raw[1:-1]
        parts = re.split(r"[,|]", raw)
        return [part.strip(" `\"'") for part in parts if part.strip(" `\"'")]
    return [str(value).strip()]


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


def timeline_row_duration_seconds(row: dict) -> int | None:
    start = parse_timestamp_seconds(row.get("start_time"))
    end = parse_timestamp_seconds(row.get("end_time"))
    if start is None or end is None or end < start:
        return None
    return end - start


def sum_scene_sync_durations(scene_rows: list[dict]) -> int | None:
    durations: list[int] = []
    for row in scene_rows:
        duration = row.get("duration_seconds")
        if isinstance(duration, (int, float)):
            durations.append(int(duration))
            continue
        parsed = parse_timestamp_seconds(duration)
        if parsed is None:
            return None
        durations.append(parsed)
    return sum(durations)


def extract_runtime_target_seconds(text: str) -> int | None:
    for key in [
        "total_duration_seconds",
        "total_runtime_seconds",
        "runtime_seconds",
        "master_runtime_seconds",
    ]:
        value = int_value(text, key)
        if value is not None:
            return value
    runtime_match = re.search(
        r"(?im)\btotal\s+runtime\s*[:=]\s*(\d+)\s*(?:s|sec|secs|seconds)\b",
        text,
    )
    if runtime_match:
        return int(runtime_match.group(1))
    return None


def normalized_contains(haystack: str, needle: str) -> bool:
    compact = lambda value: re.sub(r"\s+", " ", value.casefold()).strip()
    return bool(needle.strip()) and compact(needle) in compact(haystack)


def root_domain_url(url: str) -> bool:
    raw = url.strip().strip("`\"'.,)")
    return bool(re.fullmatch(r"https?://(?:www\.)?[^/\s]+/?", raw))


def visual_plan_file_write_claimed(text: str) -> bool:
    lowered = text.casefold()
    if any(marker in lowered for marker in VISUAL_PLAN_FILE_WRITE_MARKERS):
        return True
    return bool(
        re.search(
            r"(?is)\b(?:created|updated|wrote|generated)\b.{0,80}\b(?:file|folder|doc|document|implementation_plan\.md|task\.md)\b",
            text,
        )
    )


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


def meaningful_tokens(value: str) -> set[str]:
    tokens = re.findall(r"[^\W_]+", value.casefold(), flags=re.UNICODE)
    return {
        token
        for token in tokens
        if token not in SCRIPT_ALIGNMENT_STOPWORDS and (len(token) > 2 or token.isdigit())
    }


def final_script_lines(text: str) -> list[str]:
    body = section_text(text, "FINAL_SCRIPT") or section_text(text, "MAIN_SCRIPT_IN_ENGLISH")
    lines: list[str] = []
    for raw_line in body.splitlines():
        line = raw_line.strip()
        if not line or line == "status=present":
            continue
        if line.startswith("script_body="):
            line = line.split("=", 1)[1].strip()
        line = line.lstrip("> -*")
        if not line:
            continue
        if re.fullmatch(r"\[.*\]", line):
            continue
        if line.lower().startswith("voice vibe"):
            continue
        sentence_like_parts = [
            part.strip()
            for part in re.split(r"(?<=[.!?])\s+", line)
            if part.strip()
        ]
        lines.extend(sentence_like_parts or [line])
    return lines


def final_script_spoken_word_count(text: str) -> int:
    """Approximate spoken narration words, excluding production directions."""
    spoken_lines: list[str] = []
    for line in final_script_lines(text):
        lowered = line.strip().casefold()
        if lowered.startswith(("visual:", "visuals:", "sfx:", "music:", "caption:", "captions:")):
            continue
        if re.match(r"^\(?\s*(visual|visuals|sfx|music|caption|captions)\s*:", lowered):
            continue
        spoken_lines.append(line)
    spoken_text = " ".join(spoken_lines)
    spoken_text = re.sub(r"\([^)]*\)", " ", spoken_text)
    return len(re.findall(r"[A-Za-z0-9₹]+(?:[-'][A-Za-z0-9]+)?", spoken_text))


def evidence_alignment_corpus(source_rows: list[dict], fact_rows: list[dict]) -> tuple[list[str], set[str]]:
    claims: list[str] = []
    for row in fact_rows:
        for field in ("claim", "risk_note", "source"):
            value = str(row.get(field, "")).strip()
            if value:
                claims.append(value)
    for row in source_rows:
        for field in ("claim_supported", "title"):
            value = str(row.get(field, "")).strip()
            if value:
                claims.append(value)
    anchors: set[str] = set()
    for claim in claims:
        anchors.update(meaningful_tokens(claim))
    return claims, anchors


def alignment_score(line: str, claim: str) -> float:
    line_tokens = meaningful_tokens(line)
    claim_tokens = meaningful_tokens(claim)
    if not line_tokens or not claim_tokens:
        return 0.0
    overlap = len(line_tokens & claim_tokens)
    return overlap / max(3, min(len(line_tokens), len(claim_tokens)))


def is_fact_like_script_line(line: str, anchor_tokens: set[str], named_real_person: bool) -> bool:
    lowered = line.casefold()
    tokens = meaningful_tokens(line)
    has_number = bool(re.search(r"(₹|\brs\b|\d)", lowered))
    has_named_anchor = any(hint in lowered for hint in NAMED_REAL_PERSON_HINTS)
    has_fact_verb = any(re.search(rf"\b{re.escape(token)}\b", lowered) for token in FACT_ALIGNMENT_HINT_VERBS)
    anchor_overlap = bool(tokens & anchor_tokens)
    return has_number or (has_named_anchor and has_fact_verb) or (named_real_person and anchor_overlap and has_fact_verb)


def line_has_absolute_claim(line: str) -> bool:
    lowered = line.casefold()
    return any(token in lowered for token in ABSOLUTE_CLAIM_TOKENS)


def line_has_off_topic_promo(line: str) -> bool:
    lowered = line.casefold()
    return any(pattern in lowered for pattern in OFF_TOPIC_PROMO_PATTERNS)


def meaningful_field_value(text: str, key: str) -> bool:
    value = (key_value(text, key) or "").strip("`\"' ")
    return bool(value) and value.casefold() not in {"false", "none", "n/a", "unknown", "[]", "{}"}


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


def detects_named_real_person_anchor(text: str) -> bool:
    lowered = text.casefold()
    return any(hint in lowered for hint in NAMED_REAL_PERSON_HINTS)


def named_real_person_composite_override_approved(text: str) -> bool:
    keys = [
        "named_real_person_composite_override_approved",
        "fictionalized_retelling_requested",
        "user_explicitly_requested_composite",
        "fictionalized_or_composite_override_approved",
    ]
    return any(bool_value(text, key) is True for key in keys)


def full_media_context_present(text: str) -> bool:
    required = [
        "VOICE_GENERATION_CONTEXT",
        "IMAGE_GENERATION_CONTEXT",
        "VIDEO_GENERATION_CONTEXT",
        "MUSIC_AND_SFX_CONTEXT",
        "EDITING_CONTEXT",
        "PLATFORM_PACKAGING",
        "LOCAL_CLOUD_HYBRID_EXECUTION_PLAN",
    ]
    return all(has_section(text, section) for section in required)


def validate_consumption_ledgers(text: str, result: ValidationResult) -> None:
    for section in LEDGER_SECTIONS:
        present = has_section(text, section)
        result.checks[f"{section.lower()}_present"] = present
        if not present:
            result.partial(f"consumption_ledger_missing:{section}")
    for section in EVIDENCE_LINEAGE_SECTIONS:
        present = has_section(text, section)
        result.checks[f"{section.lower()}_present"] = present
        if not present:
            result.partial(f"consumption_lineage_missing:{section}")

    proxy_markers = [
        "manifest proxy",
        "proxy binding",
        "route-manifest registry binding",
        "manifest registry proxy",
        "role_summary",
        "role summary",
    ]
    synthetic_consumption_markers = [
        "i can't read all",
        "i cannot read all",
        "within the time limit",
        "synthesizing the ledger",
        "synthesize the ledger",
        "synthesized ledger",
        "evaluated internally",
        "marked as used",
        "additional consumption ledgers",
        "assumed consumed",
    ]
    lowered = text.casefold()
    if any(marker in lowered for marker in proxy_markers):
        result.partial("proxy_only_consumption_evidence_detected")
    detected_synthetic_markers = [
        marker for marker in synthetic_consumption_markers if marker in lowered
    ]
    result.checks["synthetic_consumption_markers_absent"] = not detected_synthetic_markers
    if detected_synthetic_markers:
        result.fail(
            "synthetic_consumption_evidence_detected:"
            + ",".join(detected_synthetic_markers)
        )
    if bool_value(text, "director_files_individually_opened") is not True:
        result.partial("director_files_not_individually_opened")
    if bool_value(text, "agent_files_individually_opened") is not True:
        result.partial("agent_files_not_individually_opened")
    if bool_value(text, "subagent_files_individually_opened") is not True:
        result.partial("subagent_files_not_individually_opened")
    if "status=NEEDS_CONFIRMATION" in section_text(text, "DIRECTOR_CONSUMPTION_LEDGER"):
        result.partial("director_consumption_not_fully_proven")
    if "status=NEEDS_CONFIRMATION" in section_text(text, "AGENT_CONSUMPTION_LEDGER"):
        result.partial("agent_consumption_not_fully_proven")
    if "status=NEEDS_CONFIRMATION" in section_text(text, "SUBAGENT_CONSUMPTION_LEDGER"):
        result.partial("subagent_consumption_not_fully_proven")
    if "status=NEEDS_CONFIRMATION" in section_text(text, "SUBSKILL_CONSUMPTION_LEDGER"):
        result.partial("subskill_consumption_not_fully_proven")
    if "status=BLOCKED" in section_text(text, "DIRECTOR_CONSUMPTION_LEDGER"):
        result.fail("director_consumption_blocked")
    if "status=BLOCKED" in section_text(text, "AGENT_CONSUMPTION_LEDGER"):
        result.fail("agent_consumption_blocked")


def validate_invalid_status_tokens(text: str, result: ValidationResult) -> None:
    invalid = sorted({token for token in CUSTOM_INVALID_STATUS_TOKENS if token in text})
    result.checks["invalid_custom_status_tokens_absent"] = not invalid
    if invalid:
        result.fail("invalid_custom_status_tokens_present:" + ",".join(invalid))


def validate_chat_output_cleanness(text: str, result: ValidationResult) -> None:
    final_script_pos = section_position(text, "FINAL_SCRIPT")
    media_positions = [
        section_position(text, section)
        for section in MEDIA_CONTEXT_SECTIONS
        if section_position(text, section) >= 0
    ]
    final_script_before_media = final_script_pos >= 0 and all(
        final_script_pos < media_pos for media_pos in media_positions
    )
    result.checks["chat_output_primary_asset"] = "FINAL_SCRIPT" if final_script_pos >= 0 else None
    result.checks["final_script_before_media_context_sections"] = final_script_before_media
    if final_script_pos >= 0 and media_positions and not final_script_before_media:
        result.partial("final_script_not_presented_before_media_context_sections")


def validate_source_to_script_alignment(
    text: str,
    result: ValidationResult,
    source_rows: list[dict],
    fact_rows: list[dict],
    named_real_person: bool,
) -> None:
    lines = final_script_lines(text)
    claim_corpus, anchor_tokens = evidence_alignment_corpus(source_rows, fact_rows)
    fact_like_lines: list[str] = []
    unaligned_lines: list[str] = []
    unsupported_absolute_lines: list[str] = []
    off_topic_promo_lines: list[str] = []
    best_scores: list[float] = []
    promo_allowed = any(
        bool_value(text, key) is True
        for key in [
            "off_topic_promo_requested",
            "cross_sell_requested",
            "current_release_tie_in_requested",
        ]
    )

    for line in lines:
        if line_has_off_topic_promo(line) and not promo_allowed:
            off_topic_promo_lines.append(line)
        if not is_fact_like_script_line(line, anchor_tokens, named_real_person):
            continue
        fact_like_lines.append(line)
        best_score = max((alignment_score(line, claim) for claim in claim_corpus), default=0.0)
        best_scores.append(best_score)
        if best_score < 0.45:
            unaligned_lines.append(line)
        if line_has_absolute_claim(line) and best_score < 0.8:
            unsupported_absolute_lines.append(line)

    result.checks["fact_like_script_lines_checked"] = len(fact_like_lines)
    result.checks["aligned_fact_like_lines"] = max(len(fact_like_lines) - len(unaligned_lines), 0)
    result.checks["unaligned_fact_like_lines"] = len(unaligned_lines)
    result.checks["absolute_claim_lines_checked"] = sum(
        1 for line in fact_like_lines if line_has_absolute_claim(line)
    )
    result.checks["unsupported_absolute_claims"] = len(unsupported_absolute_lines)
    result.checks["off_topic_promo_lines_detected"] = len(off_topic_promo_lines)
    result.checks["best_fact_alignment_score"] = round(max(best_scores, default=0.0), 4)

    if unaligned_lines:
        snippets = "; ".join(line[:90] for line in unaligned_lines[:3])
        result.fail("source_to_script_alignment_missing:" + snippets)
    if unsupported_absolute_lines:
        snippets = "; ".join(line[:90] for line in unsupported_absolute_lines[:3])
        result.fail("unsupported_absolute_biographical_claims:" + snippets)
    if off_topic_promo_lines:
        snippets = "; ".join(line[:90] for line in off_topic_promo_lines[:2])
        result.fail("off_topic_current_promo_in_final_script:" + snippets)


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
    duration = script_duration_minutes(text)
    if duration is None:
        return False
    return "youtube" in platform.lower() and 3 <= duration <= 10


def script_duration_minutes(text: str) -> float | None:
    patterns = [
        r"(?im)^\s*script_duration_minutes\s*[:=]\s*(\d+(?:\.\d+)?)",
        r"(?im)^\s*duration_minutes\s*[:=]\s*(\d+(?:\.\d+)?)",
        r"(?im)^\s*duration\s*[:=]\s*(\d+(?:\.\d+)?)\s*(?:minutes?|mins?|min)\b",
        r"(?im)^\s*duration\s*[:=]\s*(\d+(?:\.\d+)?)\s*$",
        r"(?i)\b(\d+(?:\.\d+)?)\s*(?:minute|minutes|min)\s+(?:youtube|long-form|longform|video|script)\b",
        r"(?i)\b(\d+(?:\.\d+)?)\s*-\s*(?:minute|min)\s+(?:youtube|long-form|longform|video|script)\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return float(match.group(1))
    return None


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
    return any(marker in lowered for marker in REAL_WORLD_MARKERS) or detects_named_real_person_anchor(text)


def detects_current_claims(text: str) -> bool:
    lowered = text.lower()
    return any(marker in lowered for marker in CURRENT_MARKERS)


def validate_media_factory_production_layer(text: str, result: ValidationResult) -> None:
    visual_plan_requested = bool_value(text, "visual_media_plan_requested") is True
    generator_draft_requested = (
        bool_value(text, "visual_media_generator_draft_requested") is True
    )
    media_factory_final_requested = (
        bool_value(text, "media_factory_final_draft_requested") is True
    )
    repo_write_approved = any_bool_value(text, REPO_WRITE_APPROVAL_KEYS)

    result.checks["visual_media_generator_draft_requested"] = generator_draft_requested
    result.checks["visual_plan_depth_gate_status"] = True
    result.checks["repo_write_approved_for_media_output"] = repo_write_approved

    if (
        visual_plan_requested
        and not generator_draft_requested
        and not media_factory_final_requested
        and not repo_write_approved
        and visual_plan_file_write_claimed(text)
    ):
        result.checks["unauthorized_repo_write_for_visual_plan_status"] = False
        result.fail("unauthorized_repo_write_for_visual_plan")
    else:
        result.checks["unauthorized_repo_write_for_visual_plan_status"] = True

    for section in MEDIA_FACTORY_PRODUCTION_BASE_SECTIONS:
        present = has_section(text, section)
        result.checks[f"{section.lower()}_present"] = present
        if not present:
            result.fail(f"media_factory_production_section_missing:{section}")

    production_order_body = section_text(text, "PRODUCTION_ORDER_LOCK")
    missing_phases = [
        phase for phase in PRODUCTION_ORDER_PHASES if phase not in production_order_body
    ]
    result.checks["production_order_all_phases_present"] = not missing_phases
    if missing_phases:
        result.fail("production_order_phases_missing:" + ",".join(missing_phases))
    if "master_voice" not in production_order_body.lower() and "voice" not in production_order_body.lower():
        result.fail("production_order_missing_voice_timeline_anchor")
    phase_rows = scoped_json_rows(text, "PRODUCTION_ORDER_LOCK", "production_phase_row_json")
    invalid_phase_rows = [
        str(row.get("phase_id", "unknown"))
        for row in phase_rows
        if not PRODUCTION_PHASE_REQUIRED_FIELDS.issubset(row)
        or any(placeholder_value(row.get(field)) for field in PRODUCTION_PHASE_REQUIRED_FIELDS)
    ]
    result.checks["production_phase_rows_detected"] = len(phase_rows)
    result.checks["production_phase_rows_present"] = bool(phase_rows)
    result.checks["production_phase_rows_valid"] = not invalid_phase_rows
    if not phase_rows:
        result.fail("production_phase_rows_missing")
    if phase_rows and len(phase_rows) != len(PRODUCTION_ORDER_PHASES):
        result.fail(
            f"production_phase_rows_count_mismatch:{len(phase_rows)}"
        )
    if invalid_phase_rows:
        result.fail("production_phase_rows_incomplete:" + ",".join(invalid_phase_rows))
    ordered_rows = sorted(
        phase_rows,
        key=lambda row: int(row.get("phase_order", 10**6))
        if str(row.get("phase_order", "")).isdigit()
        else 10**6,
    )
    expected_pairs = list(enumerate(PRODUCTION_ORDER_PHASES, start=1))
    exact_order_ok = len(ordered_rows) == len(expected_pairs)
    if exact_order_ok:
        for (expected_order, expected_name), row in zip(expected_pairs, ordered_rows):
            if int(row.get("phase_order", -1)) != expected_order:
                exact_order_ok = False
                break
            if str(row.get("phase_name", "")).strip() != expected_name:
                exact_order_ok = False
                break
            expected_phase_id = CANONICAL_MEDIA_FACTORY_PHASE_IDS[expected_order - 1]
            if str(row.get("phase_id", "")).strip() != expected_phase_id:
                exact_order_ok = False
                break
    result.checks["production_phase_rows_exact_order"] = exact_order_ok
    if phase_rows and not exact_order_ok:
        result.fail("production_phase_rows_out_of_order_or_incomplete")
    dependency_failures: list[str] = []
    for row in ordered_rows:
        phase_name = str(row.get("phase_name", "")).strip()
        required_dependencies = {
            CANONICAL_MEDIA_FACTORY_PHASE_IDS[PRODUCTION_ORDER_PHASES.index(dep)]
            for dep in PRODUCTION_PHASE_DEPENDENCY_MINIMUMS.get(phase_name, set())
            if dep in PRODUCTION_ORDER_PHASES
        }
        declared_dependencies = set(normalized_list_value(row.get("depends_on_phase_ids")))
        if required_dependencies and not required_dependencies.issubset(declared_dependencies):
            dependency_failures.append(phase_name)
    result.checks["production_phase_dependencies_valid"] = not dependency_failures
    if dependency_failures:
        result.fail("production_phase_dependency_gaps:" + ",".join(dependency_failures))

    asset_body = section_text(text, "ASSET_INVENTORY_LEDGER")
    missing_asset_classes = [
        asset_class for asset_class in ASSET_INVENTORY_CLASSES if asset_class not in asset_body
    ]
    result.checks["asset_inventory_classes_complete"] = not missing_asset_classes
    if missing_asset_classes:
        result.fail("asset_inventory_classes_missing:" + ",".join(missing_asset_classes))
    voice_asset_count = int_value(asset_body, "voice_assets")
    music_segment_count = int_value(asset_body, "music_segments")
    sfx_clip_count = int_value(asset_body, "sfx_clips")
    storyboard_still_count = int_value(asset_body, "storyboard_stills")
    depth_parallax_count = int_value(asset_body, "depth_parallax_stills")
    result.checks["voice_asset_count_is_master_track"] = voice_asset_count == 1
    result.checks["music_segments_are_multi_arc"] = (
        music_segment_count is not None and music_segment_count >= 3
    )
    result.checks["sfx_clip_count_has_production_depth"] = (
        sfx_clip_count is not None and sfx_clip_count >= 10
    )
    result.checks["storyboard_stills_exceed_depth_only_stills"] = (
        storyboard_still_count is not None
        and depth_parallax_count is not None
        and storyboard_still_count > depth_parallax_count
    )
    if voice_asset_count is not None and voice_asset_count != 1:
        result.fail(f"voice_asset_count_must_be_one_master_track:{voice_asset_count}")
    if music_segment_count is not None and music_segment_count < 3:
        result.fail(f"music_segments_too_shallow:{music_segment_count}")
    if sfx_clip_count is not None and sfx_clip_count < 10:
        result.fail(f"sfx_clip_count_too_shallow:{sfx_clip_count}")
    if (
        storyboard_still_count is not None
        and depth_parallax_count is not None
        and storyboard_still_count <= depth_parallax_count
    ):
        result.fail("storyboard_stills_not_broader_than_depth_parallax_subset")
    if re.search(r"(?im)^\s*still_images_required\s*[:=]\s*\d+\s*$", text):
        if "depth_parallax_stills_only" not in text and "storyboard_stills" not in asset_body:
            result.fail("still_images_required_without_asset_class_scope")

    asset_rows = scoped_json_rows(text, "ASSET_DEPENDENCY_GRAPH", "asset_row_json")
    required_asset_fields = {
        "asset_id",
        "asset_type",
        "depends_on",
        "generation_lane",
        "tool_or_provider",
        "approval_required",
        "expected_output_path",
        "proof_required",
        "status",
    }
    invalid_asset_rows = [
        str(row.get("asset_id", "unknown"))
        for row in asset_rows
        if not required_asset_fields.issubset(row)
        or any(placeholder_value(row.get(field)) for field in required_asset_fields)
    ]
    result.checks["asset_dependency_rows_detected"] = len(asset_rows)
    result.checks["asset_dependency_rows_valid"] = not invalid_asset_rows
    if not asset_rows:
        result.fail("asset_dependency_graph_has_no_structured_rows")
    if asset_rows and len(asset_rows) < 10:
        result.fail(f"asset_dependency_graph_too_shallow:{len(asset_rows)}")
    if invalid_asset_rows:
        result.fail("asset_dependency_rows_incomplete:" + ",".join(invalid_asset_rows))
    joined_assets = json.dumps(asset_rows).lower()
    for required_relation in ["master_voice", "heygen", "davinci", "proof"]:
        result.checks[f"asset_dependency_mentions_{required_relation}"] = (
            required_relation in joined_assets
        )
        if required_relation not in joined_assets:
            result.fail(f"asset_dependency_graph_missing_relation:{required_relation}")
    asset_map = {str(row.get("asset_id", "")).strip(): row for row in asset_rows}
    master_voice_row = asset_map.get("master_voice_5m05s")
    if master_voice_row:
        if "elevenlabs" not in str(master_voice_row.get("tool_or_provider", "")).lower():
            result.fail("cloud_first_voice_lane_missing_elevenlabs")
        if "cloud" not in str(master_voice_row.get("generation_lane", "")).lower():
            result.fail("cloud_first_voice_lane_not_declared_cloud")
    heygen_row = asset_map.get("heygen_batch_pack")
    if heygen_row:
        if "heygen" not in str(heygen_row.get("tool_or_provider", "")).lower():
            result.fail("cloud_first_a_roll_lane_missing_heygen")
        if "cloud" not in str(heygen_row.get("generation_lane", "")).lower():
            result.fail("cloud_first_a_roll_lane_not_declared_cloud")
    cinematic_row = asset_map.get("cinematic_broll_pack")
    if cinematic_row:
        cinematic_provider = str(cinematic_row.get("tool_or_provider", "")).lower()
        cinematic_lane = str(cinematic_row.get("generation_lane", "")).lower()
        if not any(marker in cinematic_provider for marker in ["runway", "kling", "premium cloud"]):
            result.fail("cloud_first_cinematic_broll_lane_missing_premium_cloud_provider")
        if "cloud" not in cinematic_lane:
            result.fail("cloud_first_cinematic_broll_lane_not_declared_cloud")
        if any(marker in cinematic_provider for marker in ["wan", "comfyui", "flux", "animatediff"]):
            result.fail("experimental_local_video_lane_used_as_primary_cinematic_broll")
    storyboard_row = asset_map.get("storyboard_stills_pack")
    if storyboard_row:
        still_provider = str(storyboard_row.get("tool_or_provider", "")).lower()
        if not any(marker in still_provider for marker in ["chatgpt", "approved still provider"]):
            result.fail("approved_cloud_still_generation_lane_missing_for_storyboard_stills")
    scene_prompt_body = section_text(text, "SCENE_PROMPT_PACKETS").lower()
    video_prompt_body = section_text(text, "VIDEO_PROMPT_PACKETS").lower()
    if any(marker in scene_prompt_body for marker in ["comfyui_local", "flux_schnell", "wan_local"]):
        result.fail("local_experimental_engine_listed_as_primary_scene_prompt_target")
    if any(marker in video_prompt_body for marker in ["wan_local", "comfyui_local", "animatediff", "flux_schnell"]):
        result.fail("local_experimental_engine_listed_as_primary_video_prompt_target")
    result.checks["cloud_first_method_lock_status"] = not any(
        issue.startswith(
            (
                "cloud_first_",
                "experimental_local_video_lane_",
                "approved_cloud_still_generation_lane_",
                "local_experimental_engine_listed_as_primary_",
            )
        )
        for issue in result.errors
    )

    control_body = section_text(text, "CONTROL_PANEL_EXECUTION_PLAN")
    required_control_markers = [
        "registries/local_media_factory_bridge.yaml",
        "shadow_factory_ctl.py",
        "job_packet_dir",
        "preflight_required=true",
        "render_requires_user_approval=true",
        "proof_json_required=true",
        "registry_update_required=true",
    ]
    missing_control_markers = [
        marker for marker in required_control_markers if marker not in control_body
    ]
    result.checks["control_panel_execution_plan_complete"] = not missing_control_markers
    if missing_control_markers:
        result.fail("control_panel_execution_markers_missing:" + ",".join(missing_control_markers))
    control_rows = scoped_json_rows(
        text, "CONTROL_PANEL_EXECUTION_PLAN", "control_panel_phase_row_json"
    )
    invalid_control_rows = [
        str(row.get("phase_id", "unknown"))
        for row in control_rows
        if not CONTROL_PANEL_PHASE_REQUIRED_FIELDS.issubset(row)
        or any(placeholder_value(row.get(field)) for field in CONTROL_PANEL_PHASE_REQUIRED_FIELDS)
        or str(row.get("plan_state", "")).strip() not in CONTROL_PANEL_ALLOWED_STATES
    ]
    result.checks["control_panel_phase_rows_detected"] = len(control_rows)
    result.checks["control_panel_phase_rows_present"] = bool(control_rows)
    result.checks["control_panel_phase_rows_valid"] = not invalid_control_rows
    if not control_rows:
        result.fail("control_panel_phase_rows_missing")
    if control_rows and len(control_rows) != len(CANONICAL_MEDIA_FACTORY_PHASE_IDS):
        result.fail(
            f"control_panel_phase_rows_count_mismatch:{len(control_rows)}"
        )
    if invalid_control_rows:
        result.fail("control_panel_phase_rows_invalid:" + ",".join(invalid_control_rows))
    control_phase_ids = [str(row.get("phase_id", "")).strip() for row in control_rows]
    if control_phase_ids != CANONICAL_MEDIA_FACTORY_PHASE_IDS:
        result.fail("control_panel_phase_coverage_incomplete")

    davinci_body = section_text(text, "DAVINCI_TIMELINE_PACKET")
    missing_tracks = [track for track in DAVINCI_TRACKS if f"{track}=" not in davinci_body]
    result.checks["davinci_track_map_complete"] = not missing_tracks
    if missing_tracks:
        result.fail("davinci_track_map_missing:" + ",".join(missing_tracks))
    davinci_rows = scoped_json_rows(text, "DAVINCI_TIMELINE_PACKET", "davinci_timeline_row_json")
    required_davinci_fields = {
        "scene_id",
        "source_asset_id",
        "start_time",
        "end_time",
        "track",
        "transition_in",
        "transition_out",
        "proof_dependency",
    }
    invalid_davinci_rows = [
        str(row.get("scene_id", "unknown"))
        for row in davinci_rows
        if not required_davinci_fields.issubset(row)
        or any(placeholder_value(row.get(field)) for field in required_davinci_fields)
    ]
    result.checks["davinci_timeline_rows_detected"] = len(davinci_rows)
    result.checks["davinci_timeline_rows_valid"] = not invalid_davinci_rows
    if not davinci_rows:
        result.fail("davinci_timeline_packet_has_no_structured_rows")
    if invalid_davinci_rows:
        result.fail("davinci_timeline_rows_incomplete:" + ",".join(invalid_davinci_rows))
    scene_rows = scoped_json_rows(text, "SCENE_SYNC_MATRIX", "scene_row_json")
    runtime_target_seconds = extract_runtime_target_seconds(text)
    scene_sync_duration_seconds = sum_scene_sync_durations(scene_rows) if scene_rows else None
    davinci_duration_seconds = sum(
        duration
        for duration in (
            timeline_row_duration_seconds(row) for row in davinci_rows
        )
        if duration is not None
    )
    if runtime_target_seconds is not None and scene_sync_duration_seconds is not None:
        result.checks["scene_sync_duration_matches_runtime_target"] = (
            scene_sync_duration_seconds == runtime_target_seconds
        )
        if scene_sync_duration_seconds != runtime_target_seconds:
            result.fail(
                f"scene_sync_duration_mismatch:{scene_sync_duration_seconds}!={runtime_target_seconds}"
            )
    if runtime_target_seconds is not None and davinci_rows:
        result.checks["davinci_duration_matches_runtime_target"] = (
            davinci_duration_seconds == runtime_target_seconds
        )
        if davinci_duration_seconds != runtime_target_seconds:
            result.fail(
                f"davinci_duration_mismatch:{davinci_duration_seconds}!={runtime_target_seconds}"
            )
    result.checks["duration_reconciliation_status"] = not any(
        issue.startswith(("scene_sync_duration_mismatch:", "davinci_duration_mismatch:"))
        for issue in result.errors
    )

    scene_execution_body = section_text(text, "SCENE_EXECUTION_BLOCKS")
    scene_execution_rows = scoped_json_rows(
        text, "SCENE_EXECUTION_BLOCKS", "scene_execution_block_json"
    )
    result.checks["scene_execution_blocks_present"] = (
        bool(scene_execution_body.strip()) if generator_draft_requested else True
    )
    if generator_draft_requested:
        if not scene_execution_body.strip():
            result.fail("scene_execution_blocks_missing")
        invalid_scene_execution_rows = [
            str(row.get("scene_id", "unknown"))
            for row in scene_execution_rows
            if not SCENE_EXECUTION_REQUIRED_FIELDS.issubset(row)
            or any(placeholder_value(row.get(field)) for field in SCENE_EXECUTION_REQUIRED_FIELDS)
        ]
        if not scene_execution_rows:
            result.fail("scene_execution_blocks_have_no_structured_rows")
        if invalid_scene_execution_rows:
            result.fail(
                "scene_execution_blocks_incomplete:" + ",".join(invalid_scene_execution_rows)
            )
        execution_methods = {
            str(row.get("visual_method", "")).strip() for row in scene_execution_rows
        }
        required_execution_methods = {
            "A_ROLL_AVATAR",
            "CINEMATIC_BROLL_VIDEO",
            "IMAGE_MOTION_GRAPHICS_BROLL_METHOD",
        }
        if scene_execution_rows and not required_execution_methods.issubset(execution_methods):
            result.fail("scene_execution_blocks_missing_required_visual_method_coverage")

    scene_breakout_body = section_text(text, "SCENE_BREAKOUT_BLOCKS")
    scene_breakout_ids = re.findall(
        r"(?m)^SCENE_BREAKOUT_TABLE:\s*([A-Za-z0-9_:-]+)\s*$", scene_breakout_body
    )
    result.checks["scene_breakout_blocks_present"] = bool(scene_breakout_body.strip())
    result.checks["scene_breakout_table_count"] = len(scene_breakout_ids)
    if not scene_breakout_body.strip():
        result.fail("scene_breakout_blocks_missing")
    if scene_breakout_body.strip() and not scene_breakout_ids:
        result.fail("scene_breakout_blocks_have_no_scene_tables")
    if scene_rows and scene_breakout_ids:
        unique_breakout_ids = []
        seen_breakout_ids = set()
        for scene_id in scene_breakout_ids:
            if scene_id not in seen_breakout_ids:
                unique_breakout_ids.append(scene_id)
                seen_breakout_ids.add(scene_id)
        expected_scene_ids = [str(row.get("scene_id", "")).strip() for row in scene_rows]
        if unique_breakout_ids != expected_scene_ids:
            result.fail("scene_breakout_scene_coverage_mismatch")
    result.checks["scene_breakout_format_status"] = not any(
        issue.startswith("scene_breakout_") for issue in result.errors
    )

    mission_bundle_body = section_text(text, "MISSION_MEDIA_OUTPUT_BUNDLE")
    result.checks["mission_media_output_bundle_present"] = bool(
        mission_bundle_body.strip()
    ) if generator_draft_requested else True
    if generator_draft_requested and not mission_bundle_body.strip():
        result.fail("mission_media_output_bundle_missing")
    missing_mission_bundle_markers = [
        marker
        for marker in MISSION_MEDIA_OUTPUT_REQUIRED_MARKERS
        if marker not in mission_bundle_body
    ] if generator_draft_requested else []
    if generator_draft_requested and missing_mission_bundle_markers:
        result.fail(
            "mission_media_output_bundle_markers_missing:"
            + ",".join(missing_mission_bundle_markers)
        )
    result.checks["mission_media_output_bundle_status"] = not any(
        issue.startswith("mission_media_output_bundle_") for issue in result.errors
    )

    missing_batch_sections = [
        section
        for section in GENERATOR_BATCH_PLAN_SECTIONS
        if generator_draft_requested and not has_section(text, section)
    ]
    result.checks["generator_batch_plan_status"] = not missing_batch_sections
    if missing_batch_sections:
        result.fail(
            "generator_draft_batch_plan_sections_missing:"
            + ",".join(missing_batch_sections)
        )

    proof_body = section_text(text, "PRODUCTION_PROOF_GATE")
    required_proof_markers = [
        "artifact_path=",
        "proof_json_path=",
        "registry_entry_path=",
        "engine_or_provider_used=",
        "source_packet_ref=",
        "validation_result=",
        "human_review_status=",
        "status=",
    ]
    missing_proof_markers = [
        marker for marker in required_proof_markers if marker not in proof_body
    ]
    result.checks["production_proof_gate_complete"] = not missing_proof_markers
    if missing_proof_markers:
        result.fail("production_proof_gate_markers_missing:" + ",".join(missing_proof_markers))


def validate(text: str) -> ValidationResult:
    result = ValidationResult()
    validate_repo_propagation(result)
    validate_invalid_status_tokens(text, result)
    route_id = (key_value(text, "route_id") or "").strip("`\"' ")
    route_scope_status = (key_value(text, "route_scope_status") or "").strip("`\"' ").upper()
    route_scope_claims_pass = route_scope_status == "PASS"
    route_scope_file_audit_present = has_section(text, "ROUTE_SCOPE_FILE_AUDIT")
    canonical_route_id = (key_value(text, "canonical_route_id") or "").strip("`\"' ")

    def audit_int(key: str) -> int | None:
        value = key_value(text, key)
        if not value:
            return None
        match = re.search(r"\d+", value)
        return int(match.group(0)) if match else None

    route_scope_counts = {
        "startup_docs_read_count": audit_int("startup_docs_read_count"),
        "runtime_contracts_read_count": audit_int("runtime_contracts_read_count"),
        "registries_read_count": audit_int("registries_read_count"),
        "directors_read_count": audit_int("directors_read_count"),
        "agents_read_count": audit_int("agents_read_count"),
        "subagents_read_count": audit_int("subagents_read_count"),
        "skills_read_count": audit_int("skills_read_count"),
        "subskills_read_count": audit_int("subskills_read_count"),
        "total_route_scope_files_read": audit_int("total_route_scope_files_read"),
    }
    audit_body = section_text(text, "ROUTE_SCOPE_FILE_AUDIT")
    listed_audit_paths = sorted(
        {
            match.strip("` ")
            for match in re.findall(
                r"(?m)^\s*`?((?:AGENTS|START_HERE_FOR_AGENTS|AGENT_READ_ORDER|AGENT_REPO_FIRST_OPERATING_DOCTRINE|AGENT_ANTI_DRIFT_RULES)\.md|(?:runtime_contracts|registries|directors|agents|subagents|skills)/[^\s`]+)`?\s*$",
                audit_body,
            )
        }
    )
    listed_scope_counts = {
        "startup_docs_listed_count": sum(
            path
            in {
                "AGENTS.md",
                "START_HERE_FOR_AGENTS.md",
                "AGENT_READ_ORDER.md",
                "AGENT_REPO_FIRST_OPERATING_DOCTRINE.md",
                "AGENT_ANTI_DRIFT_RULES.md",
            }
            for path in listed_audit_paths
        ),
        "runtime_contracts_listed_count": sum(
            path.startswith("runtime_contracts/") for path in listed_audit_paths
        ),
        "registries_listed_count": sum(
            path.startswith("registries/")
            or path == "agents/AGENT_RUNTIME_REGISTRY.yaml"
            or path == "subagents/SUB_AGENT_RUNTIME_REGISTRY.yaml"
            for path in listed_audit_paths
        ),
        "directors_listed_count": sum(
            path.startswith("directors/") for path in listed_audit_paths
        ),
        "agents_listed_count": sum(
            path.startswith("agents/") and path.endswith("_agent.py")
            for path in listed_audit_paths
        ),
        "subagents_listed_count": sum(
            path.startswith("subagents/") and path.endswith("_sub_agent.py")
            for path in listed_audit_paths
        ),
        "skills_listed_count": sum(
            path.startswith("skills/script_intelligence/")
            or path.startswith("skills/script_intelligence_army/")
            for path in listed_audit_paths
        ),
        "subskills_listed_count": sum(
            path.startswith("skills/sub_skills/") for path in listed_audit_paths
        ),
    }
    listed_scope_counts["total_route_scope_files_listed"] = len(listed_audit_paths)
    missing_listed_paths = [
        path for path in listed_audit_paths if not Path(path).exists()
    ]
    story_required = duration_requires_story(text)
    real_world_proof = detects_real_world_proof(text)
    named_real_person = detects_named_real_person_anchor(text)
    web_evidence_required = real_world_proof or detects_current_claims(text)
    explicit_script_only = bool_value(text, "explicit_script_only_request") is True
    repo_only_approved = bool_value(text, "user_approved_repo_only_continuation") is True
    explicit_language = bool_value(text, "explicit_language_requested") is True
    task_mode = (key_value(text, "task_mode") or "").strip("`\"' ")
    script_only_mode = task_mode == "script_only" or (
        not task_mode
        and (route_id == "SCRIPT_GENERATION" or canonical_route_id == "SCRIPT_GENERATION")
        and not explicit_script_only
    )
    drift_audit_mode = task_mode == "repo_drift_audit" or bool_value(text, "drift_audit_mode") is True
    regression_mode = (
        task_mode == "media_factory_regression_audit"
        or bool_value(text, "regression_mode") is True
    )
    continue_previous_mission = bool_value(text, "continue_previous_mission") is True
    explicit_user_reference = bool_value(text, "explicit_user_reference") is True
    dependencies_complete = bool_value(text, "dependencies_complete") is True
    output_phase_started = bool_value(text, "output_phase_started") is True
    selected_route_slice_read = (
        bool_value(text, "selected_route_slice_read") is True
        or bool_value(text, "route_slice_used") is True
    )
    mandatory_route_slice_paths_consumed = (
        bool_value(text, "mandatory_route_slice_paths_consumed") is True
    )
    final_deliverable_generated = (
        bool_value(text, "final_deliverable_generated") is True
        or has_section(text, "FINAL_SCRIPT")
    )
    compaction_detected = bool_value(text, "compaction_detected") is True or (
        "conversation was compacted" in text.casefold()
    )
    semantic_map_present = semantic_influence_present(text)
    media_factory_final = bool_value(text, "media_factory_final_draft_requested") is True
    visual_media_plan = bool_value(text, "visual_media_plan_requested") is True
    visual_media_generator_draft = (
        bool_value(text, "visual_media_generator_draft_requested") is True
    )
    production_ready_media_context = full_media_context_present(text) and not explicit_script_only
    mandatory_route_actors_opened = all(
        bool_value(text, key) is True
        for key in [
            "director_files_individually_opened",
            "agent_files_individually_opened",
            "subagent_files_individually_opened",
        ]
    )
    rule_evidence_present = has_section(text, "RULE_CONSUMPTION_EVIDENCE_LEDGER")
    exact_lineage_present = has_section(text, "EXACT_RULE_LINEAGE_MAP")

    result.checks.update(
        {
            "story_required": story_required,
            "real_world_proof_detected": real_world_proof,
            "named_real_person_detected": named_real_person,
            "web_evidence_required": web_evidence_required,
            "explicit_script_only_request": explicit_script_only,
            "task_mode": task_mode or None,
            "script_only_mode": script_only_mode,
            "drift_audit_mode": drift_audit_mode,
            "regression_mode": regression_mode,
            "continue_previous_mission": continue_previous_mission,
            "explicit_user_reference": explicit_user_reference,
            "dependencies_complete": dependencies_complete,
            "output_phase_started": output_phase_started,
            "selected_route_slice_read": selected_route_slice_read,
            "mandatory_route_slice_paths_consumed": mandatory_route_slice_paths_consumed,
            "final_deliverable_generated": final_deliverable_generated,
            "compaction_detected": compaction_detected,
            "semantic_influence_map_present": semantic_map_present,
            "file_counts_are_telemetry_only": bool_value(text, "file_counts_are_telemetry_only") is True,
            "media_factory_final_draft_requested": media_factory_final,
            "visual_media_plan_requested": visual_media_plan,
            "visual_media_generator_draft_requested": visual_media_generator_draft,
            "production_ready_media_context_detected": production_ready_media_context,
            "mandatory_route_actors_individually_opened": mandatory_route_actors_opened,
            "rule_consumption_evidence_ledger_present": rule_evidence_present,
            "exact_rule_lineage_map_present": exact_lineage_present,
            "route_id": route_id,
            "canonical_route_id": canonical_route_id,
            "route_scope_status": route_scope_status,
            "route_scope_file_audit_present": route_scope_file_audit_present,
            "route_scope_files_listed_count": len(listed_audit_paths),
            "route_scope_audit_listed_paths_exist": not missing_listed_paths,
            **route_scope_counts,
            **listed_scope_counts,
        }
    )

    boot_read_count_keys = [
        "AGENTS.md_read_count",
        "START_HERE_FOR_AGENTS.md_read_count",
        "AGENT_READ_ORDER.md_read_count",
        "AGENT_REPO_FIRST_OPERATING_DOCTRINE.md_read_count",
        "AGENT_ANTI_DRIFT_RULES.md_read_count",
    ]
    boot_read_counts = {
        key: bounded_int_value(text, key)
        for key in boot_read_count_keys
        if bounded_int_value(text, key) is not None
    }
    result.checks["boot_file_read_counts"] = boot_read_counts
    allowed_reread_reasons = {
        "file_hash_changed",
        "audit_mode",
        "validator_mode",
        "explicit_user_requested_compare",
        "route_manifest_changed",
        "krishna_directive_dependency_trace",
        "semantic_influence_verification",
        "compaction_recovery_validation",
    }
    reread_reason = (key_value(text, "reread_reason") or "").strip("`\"' ")
    reread_allowed = reread_reason in allowed_reread_reasons
    boot_count_failures = [
        f"{key}={count}"
        for key, count in boot_read_counts.items()
        if count > 1 and not reread_allowed
    ]
    if boot_count_failures:
        result.fail("boot_files_reread_after_route_lock:" + ",".join(boot_count_failures))

    route_locked = bool_value(text, "route_locked") is True or has_section(text, "TASK_ROUTE_LOCK")
    if route_locked and not reread_allowed:
        repeated_boot_refs = [
            path
            for path in [
                "AGENTS.md",
                "START_HERE_FOR_AGENTS.md",
                "AGENT_READ_ORDER.md",
                "AGENT_REPO_FIRST_OPERATING_DOCTRINE.md",
                "AGENT_ANTI_DRIFT_RULES.md",
            ]
            if len(re.findall(rf"{re.escape(path)}#L\d+", text)) > 1
        ]
        if repeated_boot_refs:
            result.fail("boot_files_reread_after_route_lock:" + ",".join(repeated_boot_refs))

    if compaction_detected:
        compaction_restart_markers = [
            marker
            for marker in [
                "boot_restart_after_compaction=true",
                "I will read AGENTS.md as required by step 1",
                "I will view the AGENTS.md file",
                "I will start by analyzing the workspace directory",
            ]
            if marker.casefold() in text.casefold()
        ]
        if compaction_restart_markers and bool_value(text, "compaction_resume_from_route_state") is not True:
            result.fail("compaction_restart_boot")

    if dependencies_complete and not output_phase_started:
        result.fail("dependencies_complete_but_no_output_phase")

    if route_scope_claims_pass and not semantic_map_present:
        result.fail("file_count_pass_without_semantic_influence")
    if route_scope_claims_pass and not selected_route_slice_read:
        result.fail("route_scope_pass_without_selected_route_slice")
    if route_scope_claims_pass and not mandatory_route_slice_paths_consumed:
        result.fail("route_scope_pass_without_mandatory_route_slice_completion")
    if route_scope_claims_pass and not dependencies_complete:
        result.fail("route_scope_pass_without_dependencies_complete")
    if route_scope_claims_pass and not output_phase_started:
        result.fail("route_scope_pass_without_output_phase_started")
    if route_scope_claims_pass and not final_deliverable_generated:
        result.fail("route_scope_pass_without_final_deliverable")
    if "semantic_use_status=NOT_PROVEN" in text:
        result.fail("selected_component_not_used")
    if bool_value(text, "selected_component_not_used") is True:
        result.fail("selected_component_not_used")
    if bool_value(text, "selected_skill_not_consumed") is True:
        result.fail("selected_skill_not_consumed")
    if bool_value(text, "selected_subskill_not_consumed") is True:
        result.fail("selected_subskill_not_consumed")

    final_script_start = section_pos_or_end(text, "FINAL_SCRIPT")
    media_contracts_read_pre_script = [
        path
        for path in [
            "runtime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md",
            "runtime_contracts/LOCAL_CLOUD_HYBRID_MEDIA_EXECUTION_CONTRACT.md",
            "MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md",
            "LOCAL_CLOUD_HYBRID_MEDIA_EXECUTION_CONTRACT.md",
        ]
        if (
            (line_ref_present(text[:final_script_start], path) or audit_lists_path(text, path))
            and not (visual_media_plan or visual_media_generator_draft or media_factory_final)
        )
    ]
    if script_only_mode and media_contracts_read_pre_script:
        result.fail(
            "script_route_consumed_media_contract_before_script_output:"
            + ",".join(sorted(set(media_contracts_read_pre_script)))
        )

    historical_output_read = (
        line_ref_present(text, "outputs/missions")
        or audit_lists_path(text, "outputs/missions")
        or explicit_read_true(text, "outputs_missions_read")
    )
    if script_only_mode and historical_output_read and not (
        regression_mode or continue_previous_mission or explicit_user_reference
    ):
        result.fail("historical_output_read_without_regression_mode")

    chat_transcript_read = (
        line_ref_present(text, "chat_transcript.txt")
        or audit_lists_path(text, "chat_transcript.txt")
        or explicit_read_true(text, "chat_transcript_read")
    )
    if script_only_mode and chat_transcript_read and not (drift_audit_mode or explicit_user_reference):
        result.fail("chat_transcript_read_without_drift_audit_mode")

    if script_only_mode and bool_value(text, "analysis_without_output") is True:
        result.fail("analysis_without_output")
    if (
        script_only_mode
        and has_section(text, "ROUTE_SCOPE_FILE_AUDIT")
        and not has_section(text, "FINAL_SCRIPT")
        and bool_value(text, "output_missing") is not False
    ):
        result.fail("analysis_without_output")

    if route_id and route_id != "SCRIPT_GENERATION":
        result.fail(f"non_canonical_script_generation_route_id:{route_id}")
    if route_scope_claims_pass:
        if not route_scope_file_audit_present:
            result.fail("route_scope_pass_without_route_scope_file_audit")
        if canonical_route_id and canonical_route_id != "SCRIPT_GENERATION":
            result.fail(f"route_scope_audit_non_canonical_route_id:{canonical_route_id}")
        if missing_listed_paths:
            result.fail("route_scope_file_audit_paths_missing_on_disk:" + ",".join(missing_listed_paths[:10]))

    if not explicit_script_only:
        validate_consumption_ledgers(text, result)
        validate_chat_output_cleanness(text, result)
    if media_factory_final or visual_media_plan or visual_media_generator_draft:
        if not mandatory_route_actors_opened:
            result.fail("mandatory_route_actors_not_individually_opened")
        if not rule_evidence_present:
            result.fail("rule_consumption_evidence_ledger_missing_for_production_route")
        if not exact_lineage_present:
            result.fail("exact_rule_lineage_map_missing_for_production_route")

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
            if (
                named_real_person
                and story_basis in {
                    "realistic_composite",
                    "mythological_parallel",
                    "hybrid_modern_mythological_reference",
                }
                and not named_real_person_composite_override_approved(text)
            ):
                result.fail("named_real_person_cannot_be_silently_recast_as_composite")
            if bool_value(text, "generic_motivation_filler") is True:
                result.fail("cinematic_story_is_generic_motivation_filler")
            if bool_value(text, "cinematic_reconstruction") is True:
                disclosure_present = (
                    bool_value(text, "biopic_reconstruction_disclosure_present") is True
                    or meaningful_field_value(text, "verified_scene_details")
                )
                result.checks["biopic_reconstruction_disclosure_present"] = disclosure_present
                if real_world_proof and not disclosure_present:
                    result.fail("biopic_reconstruction_disclosure_missing")
                if (
                    real_world_proof
                    and not disclosure_present
                    and any(
                        marker in (section_text(text, "CINEMATIC_SHORT_STORY_BLOCK") + "\n" + section_text(text, "FINAL_SCRIPT")).casefold()
                        for marker in DRAMATIZATION_MARKERS
                    )
                ):
                    result.fail("dramatized_biopic_details_without_disclosure")
            story_body = section_text(text, "CINEMATIC_SHORT_STORY_BLOCK")
            if (
                re.search(r"(?im)^\s*verified_scene_details\s*[:=]\s*false\s*$", story_body)
                and re.search(r"(?im)^\s*status\s*[:=]\s*PASS\s*$", story_body)
            ):
                result.fail("verified_scene_details_false_cannot_pass")

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
    freshness_class = (key_value(text, "freshness_class") or "").casefold()
    if "evergreen" in freshness_class and (
        bool_value(text, "current_data_required") is True
        or bool_value(text, "real_time_sources_used") is True
        or bool_value(text, "real_time_research_claimed") is True
    ):
        result.fail("evergreen_topic_current_realtime_inflation")

    web_search_claimed = bool_value(text, "web_search_conducted") is True
    source_lock_pass_claimed = bool(
        re.search(r"(?ims)^\s*SOURCE_RESEARCH_LOCK\s*$.*?^\s*status\s*[:=]\s*PASS\s*$", text)
        or re.search(r"(?ims)^\s*SOURCE_BREADTH_LOCK\s*$.*?^\s*status\s*[:=]\s*PASS\s*$", text)
    )
    if web_search_claimed or source_lock_pass_claimed:
        source_rows_for_claim = scoped_json_rows(text, "SOURCE_LEDGER", "source_row_json")
        fact_rows_for_claim = scoped_json_rows(text, "FACT_VS_ANECDOTE_MAP", "fact_map_row_json")
        per_tool_body = section_text(text, "PER_TOOL_SOURCE_MAP")
        structured_source_urls = key_values(per_tool_body, "source_url")
        actual_structured_urls = [
            url for url in structured_source_urls if re.match(r"https?://", url.strip())
        ]
        result.checks["web_or_source_lock_claim_requires_structured_source_rows"] = True
        result.checks["per_tool_source_map_structured_urls_count"] = len(actual_structured_urls)
        if not source_rows_for_claim:
            result.fail("source_lock_pass_without_structured_source_ledger_rows")
        if not fact_rows_for_claim:
            result.fail("source_lock_pass_without_structured_fact_map_rows")
        if not actual_structured_urls and not source_rows_for_claim:
            result.fail("per_tool_source_map_missing_structured_source_urls")

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
        root_domain_source_urls = [url for url in source_urls if root_domain_url(url)]
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
        result.checks["source_ledger_root_domain_urls_absent"] = not root_domain_source_urls
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
        if root_domain_source_urls:
            result.fail("source_ledger_uses_root_domain_urls:" + ",".join(root_domain_source_urls))
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
        fact_map_body = section_text(text, "FACT_VS_ANECDOTE_MAP")
        weak_inference_presented_strongly = (
            re.search(r"(?is)\binference\b.{0,240}\b(?:entirely|every single rupee|all the money|all earnings|every rupee)\b", fact_map_body)
            is not None
        )
        result.checks["weak_inference_presented_strongly_absent"] = (
            not weak_inference_presented_strongly
        )
        if weak_inference_presented_strongly:
            result.fail("weak_inference_presented_too_strongly")
        validate_source_to_script_alignment(
            text=text,
            result=result,
            source_rows=source_rows,
            fact_rows=fact_rows,
            named_real_person=named_real_person,
        )

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
        depth_lock_present = has_section(text, "SCRIPT_BODY_DEPTH_LOCK")
        spoken_word_count = final_script_spoken_word_count(text)
        minimum_spoken_words = int(duration_minutes * 135)
        maximum_spoken_words = int(duration_minutes * 190)
        result.checks["script_body_depth_lock_present"] = depth_lock_present
        result.checks["final_script_spoken_word_count"] = spoken_word_count
        result.checks["final_script_minimum_spoken_words"] = minimum_spoken_words
        result.checks["final_script_maximum_spoken_words"] = maximum_spoken_words
        result.checks["final_script_word_count_fits_declared_duration"] = (
            minimum_spoken_words <= spoken_word_count <= maximum_spoken_words
        )
        if not depth_lock_present:
            result.partial("script_body_depth_lock_missing")
        if spoken_word_count < minimum_spoken_words:
            result.fail(
                f"final_script_too_short_for_declared_duration:{spoken_word_count}<{minimum_spoken_words}"
            )
        if spoken_word_count > maximum_spoken_words:
            result.partial(
                f"final_script_may_exceed_declared_duration:{spoken_word_count}>{maximum_spoken_words}"
            )
        depth_status = (key_value(text, "duration_fit_status") or "").strip("`\"' ").upper()
        if depth_lock_present and depth_status != "PASS":
            result.fail("script_body_depth_lock_duration_fit_not_pass")
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

    if production_ready_media_context and not media_factory_final:
        scene_sync_present = has_section(text, "SCENE_SYNC_MATRIX")
        result.checks["scene_sync_required_for_production_media_context"] = True
        if not scene_sync_present:
            result.partial("scene_sync_matrix_missing_for_production_ready_media_context")

    if (
        media_factory_final
        or visual_media_plan
        or visual_media_generator_draft
        or production_ready_media_context
    ):
        if media_factory_final or visual_media_plan or visual_media_generator_draft:
            validate_media_factory_production_layer(text, result)
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
character=Public Figure Test Anchor
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


def fixture_production_phase_rows() -> list[dict]:
    phase_modes = {
        "freeze_approved_script_and_scene_ids": "plan_only",
        "generate_or_confirm_scene_sync_matrix": "plan_only",
        "generate_master_voice_track": "cloud_after_approval",
        "align_voice_timestamps_to_scene_rows": "requires_confirmation",
        "generate_music_segments": "cloud_after_approval",
        "generate_individual_sfx_clips": "cloud_after_approval",
        "generate_character_consistency_reference_assets": "cloud_after_approval",
        "generate_storyboard_and_still_image_assets": "cloud_after_approval",
        "render_hyperframes_slides_cards_and_alpha_overlays": "local_after_approval",
        "generate_depth_maps_for_still_parallax_assets": "local_after_approval",
        "generate_heygen_a_roll_batches": "cloud_after_approval",
        "generate_premium_cinematic_b_roll_clips": "cloud_after_approval",
        "build_davinci_timeline_from_packet": "blocked_until_assets_exist",
        "assemble_v1_v2_v3_and_a1_to_a5_tracks": "blocked_until_assets_exist",
        "qc_sync_captions_safe_zones_color_and_audio": "requires_confirmation",
        "export_youtube_master": "requires_confirmation",
        "collect_proofs_and_update_registry": "requires_confirmation",
    }
    phase_outputs = {
        "freeze_approved_script_and_scene_ids": ["frozen_script", "scene_ids"],
        "generate_or_confirm_scene_sync_matrix": ["scene_sync_matrix"],
        "generate_master_voice_track": ["voice_assets"],
        "align_voice_timestamps_to_scene_rows": ["voice_alignment_packet"],
        "generate_music_segments": ["music_segments"],
        "generate_individual_sfx_clips": ["sfx_clips"],
        "generate_character_consistency_reference_assets": ["character_consistency_assets"],
        "generate_storyboard_and_still_image_assets": ["storyboard_stills", "depth_parallax_stills"],
        "render_hyperframes_slides_cards_and_alpha_overlays": ["hyperframes_slide_assets", "hyperframes_overlay_assets"],
        "generate_depth_maps_for_still_parallax_assets": ["depth_maps"],
        "generate_heygen_a_roll_batches": ["a_roll_batches"],
        "generate_premium_cinematic_b_roll_clips": ["cinematic_broll_clips"],
        "build_davinci_timeline_from_packet": ["davinci_project_assets"],
        "assemble_v1_v2_v3_and_a1_to_a5_tracks": ["assembled_timeline"],
        "qc_sync_captions_safe_zones_color_and_audio": ["qc_report"],
        "export_youtube_master": ["youtube_master_export"],
        "collect_proofs_and_update_registry": ["proof_registry_updates"],
    }
    return [
        {
            "phase_id": CANONICAL_MEDIA_FACTORY_PHASE_IDS[index - 1],
            "phase_order": index,
            "phase_name": phase,
            "depends_on_phase_ids": [
                CANONICAL_MEDIA_FACTORY_PHASE_IDS[
                    PRODUCTION_ORDER_PHASES.index(dep)
                ]
                for dep in PRODUCTION_PHASE_DEPENDENCY_MINIMUMS.get(phase, [])
            ],
            "blocking_prerequisites": ["approved_route"] if index == 1 else ["upstream_phase_complete"],
            "output_asset_classes": phase_outputs[phase],
            "execution_mode": phase_modes[phase],
            "approval_gate": "route_lock" if phase in {
                "freeze_approved_script_and_scene_ids",
                "generate_or_confirm_scene_sync_matrix",
            } else "user_approval_required",
            "proof_gate": "proof_json_required",
            "status": (
                "PASS"
                if phase in {"freeze_approved_script_and_scene_ids", "generate_or_confirm_scene_sync_matrix"}
                else "NEEDS_USER_APPROVAL"
                if "approval" in phase_modes[phase]
                else "NEEDS_CONFIRMATION"
            ),
        }
        for index, phase in enumerate(PRODUCTION_ORDER_PHASES, start=1)
    ]


def fixture_control_panel_phase_rows() -> list[dict]:
    phase_states = {
        "freeze_approved_script_and_scene_ids": "preflight",
        "generate_or_confirm_scene_sync_matrix": "preflight",
        "generate_master_voice_track": "ready_after_approval",
        "align_voice_timestamps_to_scene_rows": "requires_confirmation",
        "generate_music_segments": "ready_after_approval",
        "generate_individual_sfx_clips": "ready_after_approval",
        "generate_character_consistency_reference_assets": "ready_after_approval",
        "generate_storyboard_and_still_image_assets": "ready_after_approval",
        "render_hyperframes_slides_cards_and_alpha_overlays": "ready_after_approval",
        "generate_depth_maps_for_still_parallax_assets": "ready_after_approval",
        "generate_heygen_a_roll_batches": "ready_after_approval",
        "generate_premium_cinematic_b_roll_clips": "ready_after_approval",
        "build_davinci_timeline_from_packet": "blocked_until_required_assets_exist",
        "assemble_v1_v2_v3_and_a1_to_a5_tracks": "blocked_until_required_assets_exist",
        "qc_sync_captions_safe_zones_color_and_audio": "requires_confirmation",
        "export_youtube_master": "blocked_until_required_assets_exist",
        "collect_proofs_and_update_registry": "blocked_until_required_assets_exist",
    }
    return [
        {
            "phase_id": CANONICAL_MEDIA_FACTORY_PHASE_IDS[index],
            "plan_state": state,
            "control_panel_entrypoint": "shadow_factory_ctl.py",
            "preflight_dependency": "job_packet_preflight",
            "downgrade_on_failure": "downgrade_to_animatic_or_block",
            "proof_artifacts": ["proof_json", "registry_entry"],
            "status": (
                "PASS"
                if state == "preflight"
                else "NEEDS_USER_APPROVAL"
                if state == "ready_after_approval"
                else "NEEDS_CONFIRMATION"
            ),
        }
        for index, phase_name in enumerate(PRODUCTION_ORDER_PHASES)
        for state in [phase_states[phase_name]]
    ]


def valid_full_fixture() -> str:
    sections = "\n".join(f"{section}\nstatus=present" for section in FULL_CONTENT_ENGINEERING_SECTIONS)
    ledgers = """
DIRECTOR_CONSUMPTION_LEDGER
director_files_individually_opened=true
asset_name=Krishna
read_before_output=true
status=USED
asset_name=Vyasa
read_before_output=true
status=USED
asset_name=Valmiki
read_before_output=true
status=USED
asset_name=Saraswati
read_before_output=true
status=USED
asset_name=Yama
read_before_output=true
status=USED
AGENT_CONSUMPTION_LEDGER
agent_files_individually_opened=true
asset_name=krishna_agent
read_before_output=true
status=USED
asset_name=vyasa_agent
read_before_output=true
status=USED
asset_name=valmiki_agent
read_before_output=true
status=USED
asset_name=saraswati_agent
read_before_output=true
status=USED
asset_name=yama_agent
read_before_output=true
status=USED
SUBAGENT_CONSUMPTION_LEDGER
subagent_files_individually_opened=true
asset_name=wf_200
read_before_output=true
status=USED
asset_name=cwf_210
read_before_output=true
status=USED
asset_name=cwf_220
read_before_output=true
status=USED
asset_name=cwf_230
read_before_output=true
status=USED
SKILL_CONSUMPTION_LEDGER
asset_name=shadow-content-orchestration
read_before_output=true
status=USED
asset_name=S-201-hook-optimizer
read_before_output=true
status=USED
asset_name=S-202-first-draft-generation
read_before_output=true
status=USED
asset_name=M-039-re-hook-system
read_before_output=true
status=USED
SUBSKILL_CONSUMPTION_LEDGER
asset_name=SS-240-hook-variation-generator
read_before_output=true
status=USED
asset_name=SS-241-open-loop-generator
read_before_output=true
status=USED
asset_name=SS-242-story-tension-builder
read_before_output=true
status=USED
asset_name=SS-243-pacing-controller
read_before_output=true
status=USED
asset_name=SS-244-retention-loop-engine
read_before_output=true
status=USED
asset_name=SS-245-cliffhanger-designer
read_before_output=true
status=USED
"""
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
    depth_filler = " ".join([
        "Focus your next hour on one skill, protect your attention, and turn daily practice into proof."
        for _ in range(52)
    ])
    script_body = " ".join([
        "Stop scrolling. Your future needs a real investment plan.",
        rehooks[0]["hook_line"],
        "Choose one skill and protect time for deliberate practice.",
        rehooks[1]["hook_line"],
        "Treat your time and money like seeds for the person you are building.",
        rehooks[2]["hook_line"],
        depth_filler,
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
language_body_gate_status=PASS
rehook_reality_gate_status=PASS
source_ledger_gate_status=PASS
fact_vs_anecdote_gate_status=PASS
scene_sync_gate_status=PASS
media_factory_sync_lock_status=PASS
quality_lock_status=PASS
governance_lock_status=PASS
{sections}
{ledgers}
RULE_CONSUMPTION_EVIDENCE_LEDGER
component_name=Vyasa
component_type=director
source_file=directors/research/vyasa.md
exact_rule_id_or_text=Build the English master script with a 45-75 second cinematic story and a RECURRING_REHOOK_MAP.
source_section_or_line=Lines 517-518
read_before_output=true
output_decision_changed=Three internal re-hooks plus a CTA hook are required and mapped into the script structure.
output_line_or_section_affected=FINAL_SCRIPT
evidence_depth=EXACT_RULE
status=USED
EXACT_RULE_LINEAGE_MAP
output_line_or_section=FINAL_SCRIPT
component_name=Krishna
source_file=directors/supreme_vision/krishna.md
exact_rule_id_or_text=Reject final approval if a 3-10 minute script lacks recurring re-hooks and active-layer evidence.
source_section_or_line=Lines 636-642
decision_changed=The final script contains recurring re-hooks and production evidence instead of a single opening hook.
SOURCE_LEDGER
{chr(10).join(json_row("source_row_json", row) for row in source_rows)}
FACT_VS_ANECDOTE_MAP
{chr(10).join(json_row("fact_map_row_json", row) for row in fact_rows)}
CINEMATIC_SHORT_STORY_BLOCK
duration_target_seconds=60
story_basis=real_person_public_arc
cinematic_reconstruction=true
biopic_reconstruction_disclosure_present=true
verified_scene_details=verified public arc anchors are sourced; sensory continuity details remain cinematic reconstruction
character=Public Figure Test Anchor
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
SCRIPT_BODY_DEPTH_LOCK
target_runtime_seconds=300
estimated_spoken_word_count=760
narration_pacing_wpm=145
pause_buffer_seconds=30
estimated_spoken_runtime_seconds=300
duration_fit_status=PASS
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
VOICE_GENERATION_CONTEXT
voice_style=firm cinematic narrator
IMAGE_GENERATION_CONTEXT
thumbnail_concept=self-investment focus split image
VIDEO_GENERATION_CONTEXT
scene_prompts=focused creator action montage
MUSIC_AND_SFX_CONTEXT
music_mood=rising resolve
EDITING_CONTEXT
retention_cuts=hard cuts at attention resets
PLATFORM_PACKAGING
title_ideas=Invest in yourself before distraction drains you
LOCAL_CLOUD_HYBRID_EXECUTION_PLAN
local_options=local render and edit
cloud_options=cloud-optional visual render
hybrid_strategy=local assembly with cloud-optional assets
fallback=local context-only handoff
SCENE_SYNC_MATRIX
scene_sync_matrix_complete=true
media_contexts_synchronized=true
influence_map_creative_depth_complete=true
rehooks_mapped_to_scene_sync_matrix=true
repo_lineage_only=false
why_line_exists=establishes urgency and redirects attention toward self-investment
emotion_triggered=resolve
retention_function=opens a curiosity loop before the roadmap
topic_support=connects action to self-investment
media_dependency=voice emphasis and hard-cut visual punctuation
{chr(10).join(json_row("scene_row_json", fixture_scene(row)) for row in rehooks)}
"""


def valid_media_fixture() -> str:
    return valid_full_fixture() + f"""
media_factory_final_draft_requested=true
visual_media_generator_draft_requested=true
media_factory_sync_lock_status=PASS
PRODUCTION_ORDER_LOCK
timeline_anchor=master_voice_track
parallelization_rule=parallelize only when dependency IDs prove no downstream asset depends on unfinished work
{chr(10).join(f"{idx}. {phase}" for idx, phase in enumerate(PRODUCTION_ORDER_PHASES, start=1))}
{chr(10).join(json_row("production_phase_row_json", row) for row in fixture_production_phase_rows())}
ASSET_INVENTORY_LEDGER
voice_assets=1
music_segments=4
sfx_clips=35
character_consistency_assets=3
storyboard_stills=46
depth_parallax_stills=3
hyperframes_slide_assets=7
hyperframes_overlay_assets=1
cinematic_broll_clips=3
a_roll_batches=4
davinci_project_assets=1
thumbnail_assets=3
ASSET_DEPENDENCY_GRAPH
asset_row_json={{"asset_id":"master_voice_5m05s","asset_type":"voice","depends_on":["approved_script","scene_sync_matrix"],"generation_lane":"cloud_voice","tool_or_provider":"ElevenLabs","approval_required":true,"expected_output_path":"/voice/master_voice_5m05s.wav","proof_required":true,"status":"NEEDS_USER_APPROVAL"}}
asset_row_json={{"asset_id":"voice_alignment_timestamp_pack","asset_type":"voice_alignment","depends_on":["master_voice_5m05s","scene_sync_matrix"],"generation_lane":"local_alignment","tool_or_provider":"Whisper timestamp alignment","approval_required":false,"expected_output_path":"/voice/voice_alignment.json","proof_required":true,"status":"NEEDS_CONFIRMATION"}}
asset_row_json={{"asset_id":"music_segment_pack","asset_type":"music","depends_on":["voice_alignment_timestamp_pack"],"generation_lane":"cloud_music","tool_or_provider":"Suno or licensed music library","approval_required":true,"expected_output_path":"/audio/music/","proof_required":true,"status":"NEEDS_USER_APPROVAL"}}
asset_row_json={{"asset_id":"sfx_library_pack","asset_type":"sfx","depends_on":["voice_alignment_timestamp_pack","scene_sync_matrix"],"generation_lane":"cloud_or_local_sfx","tool_or_provider":"Suno or local licensed library","approval_required":true,"expected_output_path":"/audio/sfx/","proof_required":true,"status":"NEEDS_USER_APPROVAL"}}
asset_row_json={{"asset_id":"character_consistency_reference_pack","asset_type":"reference_assets","depends_on":["scene_sync_matrix"],"generation_lane":"cloud_image_reference","tool_or_provider":"ChatGPT image generation or approved still provider","approval_required":true,"expected_output_path":"/references/","proof_required":true,"status":"NEEDS_USER_APPROVAL"}}
asset_row_json={{"asset_id":"storyboard_stills_pack","asset_type":"storyboard_stills","depends_on":["character_consistency_reference_pack","scene_prompt_packets"],"generation_lane":"cloud_image","tool_or_provider":"ChatGPT image generation or approved still provider","approval_required":true,"expected_output_path":"/storyboard_stills/","proof_required":true,"status":"NEEDS_USER_APPROVAL"}}
asset_row_json={{"asset_id":"hyperframes_render_pack","asset_type":"motion_graphics","depends_on":["scene_sync_matrix","storyboard_stills_pack"],"generation_lane":"local_hyperframes","tool_or_provider":"HyperFrames CLI","approval_required":true,"expected_output_path":"/hyperframes/","proof_required":true,"status":"NEEDS_USER_APPROVAL"}}
asset_row_json={{"asset_id":"depth_map_pack","asset_type":"depth_maps","depends_on":["storyboard_stills_pack"],"generation_lane":"local_depth","tool_or_provider":"Depth Anything V2","approval_required":true,"expected_output_path":"/depth_maps/","proof_required":true,"status":"NEEDS_USER_APPROVAL"}}
asset_row_json={{"asset_id":"heygen_batch_pack","asset_type":"a_roll_batches","depends_on":["master_voice_5m05s"],"generation_lane":"cloud_avatar","tool_or_provider":"HeyGen","approval_required":true,"expected_output_path":"/aroll/","proof_required":true,"status":"NEEDS_USER_APPROVAL"}}
asset_row_json={{"asset_id":"cinematic_broll_pack","asset_type":"cinematic_broll","depends_on":["scene_prompt_packets","video_prompt_packets"],"generation_lane":"cloud_video","tool_or_provider":"Runway or Kling","approval_required":true,"expected_output_path":"/broll_cinematic/","proof_required":true,"status":"NEEDS_USER_APPROVAL"}}
asset_row_json={{"asset_id":"davinci_master_timeline","asset_type":"edit_timeline","depends_on":["master_voice_5m05s","music_segment_pack","sfx_library_pack","hyperframes_render_pack","depth_map_pack","heygen_batch_pack","cinematic_broll_pack"],"generation_lane":"local_edit","tool_or_provider":"DaVinci Resolve","approval_required":false,"expected_output_path":"/davinci/mission_master_timeline.drp","proof_required":true,"status":"NEEDS_CONFIRMATION"}}
asset_row_json={{"asset_id":"qc_proof_pack","asset_type":"qc_report","depends_on":["davinci_master_timeline"],"generation_lane":"local_qc","tool_or_provider":"DaVinci Resolve + FFmpeg + human review","approval_required":false,"expected_output_path":"/qc/qc_report.json","proof_required":true,"status":"NEEDS_CONFIRMATION"}}
asset_row_json={{"asset_id":"thumbnail_pack","asset_type":"thumbnail_assets","depends_on":["storyboard_stills_pack","scene_prompt_packets"],"generation_lane":"cloud_or_local_thumbnail","tool_or_provider":"ChatGPT image generation or local design tool","approval_required":true,"expected_output_path":"/thumbnails/","proof_required":true,"status":"NEEDS_USER_APPROVAL"}}
CONTROL_PANEL_EXECUTION_PLAN
bridge_registry=registries/local_media_factory_bridge.yaml
control_panel_cli=/Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py
job_packet_dir=/Users/apple/ShadowMediaFactory/control_panel/jobs/mission_test/01_timeline
preflight_required=true
render_requires_user_approval=true
proof_json_required=true
registry_update_required=true
{chr(10).join(json_row("control_panel_phase_row_json", row) for row in fixture_control_panel_phase_rows())}
DAVINCI_TIMELINE_PACKET
V1=primary_video
V2=overlays_and_chromakey_presenter
V3=captions_and_kinetic_text
A1=master_voice
A2=music_segments
A3=sfx_impact_transition
A4=sfx_ambient_foley
A5=sfx_overflow
davinci_timeline_row_json={{"scene_id":"scene_075","source_asset_id":"heygen_batch_pack","start_time":"01:15","end_time":"01:21","track":"V2","transition_in":"hard_cut","transition_out":"hard_cut","proof_dependency":"heygen_proof_json"}}
davinci_timeline_row_json={{"scene_id":"scene_150","source_asset_id":"cinematic_broll_pack","start_time":"02:30","end_time":"02:36","track":"V1","transition_in":"soft_dissolve","transition_out":"hard_cut","proof_dependency":"cinematic_broll_proof_json"}}
davinci_timeline_row_json={{"scene_id":"scene_225","source_asset_id":"hyperframes_render_pack","start_time":"03:45","end_time":"03:51","track":"V1","transition_in":"hard_cut","transition_out":"hard_cut","proof_dependency":"hyperframes_proof_json"}}
SCENE_EXECUTION_BLOCKS
scene_execution_block_json={{"scene_id":"scene_075","visual_method":"A_ROLL_AVATAR","generation_stage":"a_roll_generation","primary_tool_or_provider":"HeyGen","input_dependencies":["master_voice_5m05s","scene_sync_matrix"],"output_path":"/aroll/scene_075_presenter.mp4","naming_convention":"scene_<scene_id>_<descriptor>.mp4","handoff_target":"DaVinci V2 track","proof_gate":"heygen_proof_json","status":"NEEDS_USER_APPROVAL"}}
scene_execution_block_json={{"scene_id":"scene_150","visual_method":"CINEMATIC_BROLL_VIDEO","generation_stage":"premium_broll_generation","primary_tool_or_provider":"Runway or Kling","input_dependencies":["scene_prompt_packets","video_prompt_packets"],"output_path":"/broll_cinematic/scene_150_city_reveal.mp4","naming_convention":"scene_<scene_id>_<descriptor>.mp4","handoff_target":"DaVinci V1 track","proof_gate":"cinematic_broll_proof_json","status":"NEEDS_USER_APPROVAL"}}
scene_execution_block_json={{"scene_id":"scene_225","visual_method":"IMAGE_MOTION_GRAPHICS_BROLL_METHOD","generation_stage":"still_plus_depth_parallax","primary_tool_or_provider":"ChatGPT image generation + Depth Anything V2 + DaVinci Fusion","input_dependencies":["storyboard_stills_pack","depth_map_pack"],"output_path":"/motion_graphics/scene_225_depth_parallax.mov","naming_convention":"scene_<scene_id>_<descriptor>.mov","handoff_target":"DaVinci V1 track","proof_gate":"depth_map_proof_json","status":"NEEDS_USER_APPROVAL"}}
SCENE_BREAKOUT_BLOCKS
scene_breakout_format=one_scene_per_table_vertical
SCENE_BREAKOUT_TABLE: scene_075
| Field | Value |
| --- | --- |
| visual_method | A_ROLL_AVATAR |
| generation_stage | a_roll_generation |
| output_path | /aroll/scene_075_presenter.mp4 |
SCENE_BREAKOUT_TABLE: scene_150
| Field | Value |
| --- | --- |
| visual_method | CINEMATIC_BROLL_VIDEO |
| generation_stage | premium_broll_generation |
| output_path | /broll_cinematic/scene_150_city_reveal.mp4 |
SCENE_BREAKOUT_TABLE: scene_225
| Field | Value |
| --- | --- |
| visual_method | IMAGE_MOTION_GRAPHICS_BROLL_METHOD |
| generation_stage | still_plus_depth_parallax |
| output_path | /motion_graphics/scene_225_depth_parallax.mov |
MISSION_MEDIA_OUTPUT_BUNDLE
mission_root=outputs/missions/mission_test/
consolidated_plan_doc=outputs/missions/mission_test/mission_test_visual_media_generator.docx
scene_packets_dir=outputs/missions/mission_test/packets/
voice_dir=outputs/missions/mission_test/voice/
music_dir=outputs/missions/mission_test/music/
sfx_dir=outputs/missions/mission_test/sfx/
images_dir=outputs/missions/mission_test/images/
broll_dir=outputs/missions/mission_test/broll/
aroll_dir=outputs/missions/mission_test/aroll/
hyperframes_dir=outputs/missions/mission_test/hyperframes/
davinci_dir=outputs/missions/mission_test/davinci/
proofs_dir=outputs/missions/mission_test/proofs/
supporting_image_generation_txt=outputs/missions/mission_test/supporting_image_generation.txt
supporting_voice_generation_txt=outputs/missions/mission_test/supporting_voice_generation.txt
supporting_music_sfx_txt=outputs/missions/mission_test/supporting_music_sfx.txt
supporting_editing_txt=outputs/missions/mission_test/supporting_editing.txt
supporting_hyperframes_txt=outputs/missions/mission_test/supporting_hyperframes.txt
cleanup_policy=keep_required_delete_temporary
VOICE_BATCH_PLAN
batch_scope=Generate the master narration as one ElevenLabs pass, then split by timestamp alignment.
save_order=voice/master_voice_5m05s.wav -> voice/voice_alignment.json
A_ROLL_BATCH_PLAN
batch_scope=Generate HeyGen presenter lanes in batches A-D after master voice exists.
save_order=aroll/heygen_batch_a.mp4 -> aroll/heygen_batch_d.mp4
MUSIC_SFX_BATCH_PLAN
batch_scope=Generate music arcs as grouped beds and SFX as timestamped clips after voice alignment.
save_order=music/arc_01.wav -> sfx/<timestamp>_<cue>.wav
IMAGE_BATCH_PLAN
batch_scope=Generate reference stills, storyboard stills, depth-parallax still inputs, and thumbnails in controlled batches.
save_order=references/ -> storyboard_stills/ -> images/ -> thumbnails/
CINEMATIC_BROLL_BATCH_PLAN
batch_scope=Generate premium cinematic B-roll after scene and video prompt packets are locked.
save_order=broll_cinematic/scene_150_city_reveal.mp4
MOTION_GRAPHICS_BATCH_PLAN
batch_scope=Render HyperFrames slides and depth-map parallax lanes after storyboard stills exist.
save_order=hyperframes/ -> depth_maps/ -> motion_graphics/
ASSEMBLY_SYNC_PLAN
batch_scope=Assemble DaVinci only after voice, music, SFX, A-roll, B-roll, HyperFrames, and depth-map lanes pass proof.
save_order=davinci/mission_master_timeline.drp -> qc/qc_report.json -> exports/master.mp4
PRODUCTION_PROOF_GATE
artifact_path=/Users/apple/ShadowMediaFactory/08_EXPORTS/mission_test_master.mp4
proof_json_path=/Users/apple/ShadowMediaFactory/control_panel/proofs/mission_test_master_proof.json
registry_entry_path=/Users/apple/ShadowMediaFactory/control_panel/registry/assets.jsonl
engine_or_provider_used=DaVinci Resolve
source_packet_ref=outputs/missions/mission_test/packets/media_factory_packet.json
validation_result=NEEDS_CONFIRMATION
human_review_status=pending
status=NEEDS_CONFIRMATION
total_duration_seconds=18
"""


def valid_visual_plan_fixture() -> str:
    text = valid_media_fixture()
    text = text.replace("media_factory_final_draft_requested=true\n", "")
    text = text.replace("visual_media_generator_draft_requested=true\n", "")
    text = text.replace("media_factory_sync_lock_status=PASS\n", "visual_media_plan_requested=true\nmedia_factory_sync_lock_status=PASS\n")
    text = re.sub(r"\nSCENE_EXECUTION_BLOCKS.*?\nSCENE_BREAKOUT_BLOCKS", "\nSCENE_BREAKOUT_BLOCKS", text, flags=re.S)
    text = re.sub(r"\nMISSION_MEDIA_OUTPUT_BUNDLE.*?\nVOICE_BATCH_PLAN", "\nVOICE_BATCH_PLAN", text, flags=re.S)
    text = re.sub(r"\nVOICE_BATCH_PLAN.*?\nPRODUCTION_PROOF_GATE", "\nPRODUCTION_PROOF_GATE", text, flags=re.S)
    return text


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
        ("neg_scene_heading_without_rows", remove_rows(valid_full_fixture(), "scene_row_json"), "FAIL"),
        ("neg_scene_missing_nested_context", valid_media_fixture().replace('"voice":{"tone":"firm","emotion":"productive discomfort","pacing":"brief acceleration then pause","pause_points":["after the re-hook"],"pronunciation_notes":[]},', "", 1), "FAIL"),
        ("neg_status_final_status_alias", valid_full_fixture().replace("source_research_lock_status=PASS", "source_research_lock_status=PARTIAL"), "FAIL"),
        ("neg_named_real_person_recast_as_composite", valid_full_fixture().replace("story_basis=real_person_public_arc", "story_basis=realistic_composite"), "FAIL"),
        ("neg_source_to_script_drift", valid_full_fixture().replace("Choose one skill and protect time for deliberate practice.", "Public Figure Test Anchor was branded arrogant for skipping parties every weekend."), "FAIL"),
        ("neg_absolute_claim_not_source_backed", valid_full_fixture().replace("Treat your time and money like seeds for the person you are building.", "Every single rupee Public Figure Test Anchor earned went straight back into acting classes."), "FAIL"),
        ("neg_off_topic_current_promo", valid_full_fixture().replace("Start today. Put one action on your calendar and follow through.", "Watch out for his upcoming film teaser. I've linked it above."), "FAIL"),
        ("neg_chat_output_script_buried", valid_full_fixture() + "\nFINAL_SCRIPT\nscript_body=Stop scrolling. Put one honest hour into yourself today.\n", "FAIL"),
        ("neg_biopic_reconstruction_without_disclosure", valid_full_fixture().replace("biopic_reconstruction_disclosure_present=true\n", "").replace("verified_scene_details=verified public arc anchors are sourced; sensory continuity details remain cinematic reconstruction", "verified_scene_details=false"), "FAIL"),
        ("neg_invalid_custom_status_token", valid_full_fixture().replace("final_status=PASS", "final_status=PASS_WITH_NOTICE"), "FAIL"),
        ("neg_proxy_only_consumption", valid_full_fixture().replace("director_files_individually_opened=true", "director_files_individually_opened=false").replace("agent_files_individually_opened=true", "agent_files_individually_opened=false").replace("subagent_files_individually_opened=true", "subagent_files_individually_opened=false"), "FAIL"),
        ("neg_production_media_context_without_scene_sync", re.sub(r"\nSCENE_SYNC_MATRIX.*", "", valid_full_fixture(), flags=re.S), "FAIL"),
        ("neg_unsupported_claims", valid_full_fixture().replace("unsupported_claims=[]", "unsupported_claims=[unverified claim]"), "FAIL"),
        ("neg_realtime_claim_without_sources", valid_full_fixture().replace("real_time_sources_used=true", "real_time_sources_used=false"), "FAIL"),
        ("neg_evergreen_realtime_inflation", valid_full_fixture() + "\nfreshness_class=EVERGREEN_WITH_REAL_WORLD_PROOF\ncurrent_data_required=true\n", "FAIL"),
        ("neg_root_domain_source_ledger", valid_full_fixture().replace("https://example.com/official", "https://example.com"), "FAIL"),
        ("neg_verified_scene_false_story_pass", valid_full_fixture() + "\nCINEMATIC_SHORT_STORY_BLOCK\nverified_scene_details=false\nstatus=PASS\n", "FAIL"),
        ("neg_weak_inference_too_strong", valid_full_fixture() + "\nFACT_VS_ANECDOTE_MAP\nInference [Logical Deduction]: Every single rupee was invested entirely in himself.\n", "FAIL"),
        ("neg_uniform_grid_without_reason", valid_full_fixture().replace("uniform_15_second_grid=false", "uniform_15_second_grid=true"), "FAIL"),
        ("neg_one_hook_only", remove_rows(valid_full_fixture(), "rehook_row_json").replace("recurring_rehook_count=3", "recurring_rehook_count=0"), "FAIL"),
        ("neg_media_factory_requires_scene_rows", remove_rows(valid_media_fixture(), "scene_row_json"), "FAIL"),
        ("neg_media_factory_missing_production_control_layer", re.sub(r"\nPRODUCTION_ORDER_LOCK.*", "\nSCENE_SYNC_MATRIX\nscene_sync_matrix_complete=true\nmedia_contexts_synchronized=true\n", valid_media_fixture(), flags=re.S), "FAIL"),
        ("neg_media_factory_missing_phase_rows", remove_rows(valid_media_fixture(), "production_phase_row_json"), "FAIL"),
        ("neg_media_factory_missing_lineage_evidence", re.sub(r"\nRULE_CONSUMPTION_EVIDENCE_LEDGER.*?EXACT_RULE_LINEAGE_MAP.*?SOURCE_LEDGER", "\nSOURCE_LEDGER", valid_media_fixture(), flags=re.S), "FAIL"),
        ("neg_media_factory_local_experimental_primary_lane", valid_media_fixture().replace("Runway or Kling", "wan_local | comfyui_local", 1), "FAIL"),
        ("neg_media_factory_duration_mismatch", valid_media_fixture().replace("total_duration_seconds=18", "total_duration_seconds=22"), "FAIL"),
        ("neg_media_factory_missing_scene_execution_blocks", re.sub(r"\nSCENE_EXECUTION_BLOCKS.*?\nPRODUCTION_PROOF_GATE", "\nPRODUCTION_PROOF_GATE", valid_media_fixture(), flags=re.S), "FAIL"),
        ("neg_media_factory_missing_scene_breakout_blocks", re.sub(r"\nSCENE_BREAKOUT_BLOCKS.*?\nMISSION_MEDIA_OUTPUT_BUNDLE", "\nMISSION_MEDIA_OUTPUT_BUNDLE", valid_media_fixture(), flags=re.S), "FAIL"),
        ("neg_media_factory_missing_mission_media_output_bundle", re.sub(r"\nMISSION_MEDIA_OUTPUT_BUNDLE.*?\nPRODUCTION_PROOF_GATE", "\nPRODUCTION_PROOF_GATE", valid_media_fixture(), flags=re.S), "FAIL"),
        (
            "neg_boot_reread_after_route_lock",
            valid_full_fixture()
            + "\nroute_id=SCRIPT_GENERATION\ntask_mode=script_only\nTASK_ROUTE_LOCK\nstatus=PASS\nroute_locked=true\nAGENTS.md_read_count=2\nSTART_HERE_FOR_AGENTS.md_read_count=1\n",
            "FAIL",
        ),
        (
            "neg_script_only_media_contract_before_final_script",
            "route_id=SCRIPT_GENERATION\ntask_mode=script_only\nTASK_ROUTE_LOCK\nstatus=PASS\nROUTE_SCOPE_FILE_AUDIT\nruntime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md#L1-L50\n"
            + valid_full_fixture(),
            "FAIL",
        ),
        (
            "neg_historical_output_without_regression_mode",
            "route_id=SCRIPT_GENERATION\ntask_mode=script_only\nTASK_ROUTE_LOCK\nstatus=PASS\nROUTE_SCOPE_FILE_AUDIT\noutputs/missions/yash_self_investment/MISSION_OUTPUT.md#L1-L50\n"
            + valid_full_fixture(),
            "FAIL",
        ),
        (
            "neg_chat_transcript_without_drift_audit_mode",
            "route_id=SCRIPT_GENERATION\ntask_mode=script_only\nTASK_ROUTE_LOCK\nstatus=PASS\nROUTE_SCOPE_FILE_AUDIT\ndownloads/chat_transcript.txt#L1-L50\n"
            + valid_full_fixture(),
            "FAIL",
        ),
        (
            "neg_dependencies_complete_without_output_phase",
            valid_full_fixture()
            + "\nroute_id=SCRIPT_GENERATION\ntask_mode=script_only\ndependencies_complete=true\noutput_phase_started=false\n",
            "FAIL",
        ),
        (
            "neg_route_scope_pass_without_semantic_influence",
            valid_full_fixture().replace("SEMANTIC_INFLUENCE_MAP\nstatus=present\n", "")
            + "\nroute_id=SCRIPT_GENERATION\ntask_mode=script_only\nroute_scope_status=PASS\n",
            "FAIL",
        ),
        (
            "neg_compaction_restart_boot",
            valid_full_fixture()
            + "\nroute_id=SCRIPT_GENERATION\ntask_mode=script_only\ncompaction_detected=true\nI will view the AGENTS.md file as required by the Shadow Boot confirmation law.\n",
            "FAIL",
        ),
        ("neg_generator_draft_missing_batch_plan", re.sub(r"\nVOICE_BATCH_PLAN.*?\nPRODUCTION_PROOF_GATE", "\nPRODUCTION_PROOF_GATE", valid_media_fixture(), flags=re.S), "FAIL"),
        ("neg_visual_plan_created_files_before_approval", valid_visual_plan_fixture() + "\nI have prepared the implementation_plan.md and updated task.md for this visual media plan.\n", "FAIL"),
        ("valid_visual_plan_without_generator_bundle", valid_visual_plan_fixture(), "PASS"),
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
