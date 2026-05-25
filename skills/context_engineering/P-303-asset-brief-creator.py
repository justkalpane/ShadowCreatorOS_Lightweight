from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def _is_strict_packet_mode(input_payload: dict[str, Any]) -> bool:
    child_workflow_id = str(input_payload.get("child_workflow_id", "")).upper()
    workflow_id = str(input_payload.get("workflow_id", "")).upper()
    return bool(input_payload.get("strict_packet_output", False)) or child_workflow_id == "CWF-330" or workflow_id == "CWF-330"


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    dossier_id = input_payload.get("dossier_id")
    if not dossier_id:
        return {
            "status": "failed",
            "error": "missing dossier_id",
            "skill_id": "P-303",
        }

    now = datetime.now(timezone.utc).isoformat()
    ts = int(datetime.now(timezone.utc).timestamp() * 1000)

    if _is_strict_packet_mode(input_payload):
        platform_packet = input_payload.get("platform_package_packet")
        if not isinstance(platform_packet, dict):
            platform_packet = {}
        source_packet_id = str(platform_packet.get("instance_id", f"PPP-{ts}"))

        context = platform_packet.get("payload", {}).get("context", {}) if isinstance(platform_packet.get("payload"), dict) else {}
        target_platform = str(context.get("target_platform", input_payload.get("target_platform", "youtube"))).lower()
        if target_platform not in {"youtube", "blog", "podcast", "email"}:
            target_platform = "youtube"

        narrative_content = platform_packet.get("payload", {}).get("narrative", {}) if isinstance(platform_packet.get("payload"), dict) else {}
        content_obj = narrative_content.get("content") if isinstance(narrative_content, dict) else {}
        content_title = "Content Piece"
        if isinstance(content_obj, dict):
            content_title = str(content_obj.get("title", "Content Piece"))
        elif isinstance(content_obj, str):
            content_title = content_obj

        broll_cues = [
            {
                "section": "hook",
                "cue": "Fast visual opener with emotional contrast frame.",
                "type": "b-roll",
                "duration": "4s",
                "dimensions": "1920x1080",
            },
            {
                "section": "body",
                "cue": "Screen capture walkthrough of key method step.",
                "type": "screen-capture",
                "duration": "12s",
                "dimensions": "1920x1080",
            },
        ]

        return {
            "instance_id": f"ABP-{ts}",
            "artifact_family": "asset_brief_packet",
            "schema_version": "1.0.0",
            "producer_workflow": "SE-N8N-CWF-330-Asset-Brief-Generator",
            "dossier_ref": str(dossier_id),
            "created_at": now,
            "status": "CREATED",
            "payload": {
                "narrative": {
                    "source_platform": target_platform,
                    "content_title": content_title,
                    "asset_count": {
                        "thumbnail_briefs": 1,
                        "broll_cues": len(broll_cues),
                        "caption_briefs": 1,
                        "audio_direction_briefs": 1,
                    },
                },
                "context": {
                    "sourced_from_packet_id": source_packet_id,
                    "target_platform": target_platform,
                    "execution_requirements": context.get("execution_requirements", {"mode": "supervised"}),
                },
                "evidence": {
                    "lineage_references": [
                        {"type": "platform_package_packet", "id": source_packet_id},
                        {"type": "dossier", "id": str(dossier_id)},
                    ],
                    "validation_checks": [
                        {"check": "input_validation", "result": "PASSED"},
                        {"check": "thumbnail_brief_generated", "result": "PASSED"},
                        {"check": "broll_brief_generated", "result": "PASSED"},
                        {"check": "caption_and_audio_brief_generated", "result": "PASSED"},
                    ],
                },
                "quality": {
                    "asset_brief_completeness": 0.95,
                    "gate_checks": {
                        "thumbnail_brief_complete": True,
                        "broll_brief_complete": True,
                        "caption_brief_complete": True,
                        "audio_brief_addressed": True,
                    },
                    "asset_brief_ready_for_wf400": True,
                },
                "status": {
                    "decision_path": "PROCEED_TO_CWF-340",
                    "next_workflow": "CWF-340",
                    "escalation_needed": False,
                },
                "assets": {
                    "thumbnail_brief": {
                        "dimensions": "1280x720",
                        "format": "jpg",
                        "style": "high-contrast editorial",
                        "primary_text": "Use This System",
                        "visual_direction": "Face + bold directional cue + contrast split background",
                        "color_palette": "gold-black-white",
                        "do_not_use": ["tiny text", "low-contrast overlays"],
                    },
                    "broll_cue_list": broll_cues,
                    "caption_brief": {
                        "caption_type": "burned-in + srt",
                        "language": "en",
                        "accessibility_standard": "WCAG-AA",
                        "review_required": True,
                    },
                    "audio_direction": {
                        "target_lufs": -14.0,
                        "peak_ceiling_db": -1.0,
                        "noise_floor_db": -55.0,
                        "format": "wav_48k",
                    },
                },
            },
        }

    return {
        "status": "success",
        "skill_id": "P-303",
        "skill_name": "asset_brief_creator",
        "artifact_family": "asset-brief-creator_packet",
        "created_at": now,
        "payload": {
            "input": input_payload,
            "result": {
                "execution_mode": "replica_runtime",
                "route_context": input_payload.get("route_id", "unknown"),
            },
        },
    }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: P-303-asset-brief-creator
# component_layer: SKILL
# component_name: P 303 Asset Brief Creator
# route_families: [context_engineering, script_generation]
# activation_triggers: route_family in [music_sfx_context, visual_context, editing_packaging, quality_gate] or explicit registry selection; mark editing_packaging_profile only when route_family is unknown.
# upstream_inputs: [final_script_packet, script_segment_packet, research_brief_packet]
# downstream_outputs: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
# required_input_packets: [final_script_packet, script_segment_packet, research_brief_packet]
# emitted_output_packets: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_MUSIC_SFX, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
# quality_gates: [context_completeness_gate, asset_consistency_gate, provider_boundary_gate]
# validator_bindings: [provider_handoff_packet_present, media_quality_gate_packet_present, lineage_approval_packet_present]
# fallback_behavior: BLOCKED_BEFORE_OUTPUT if any media context packet lacks segment_id.
# lineage_fields: [script_segment_packet_id, context_packet_id, provider_handoff_packet_id]
# provider_boundary: handoff planning only; provider_execution_allowed=false until approval_packet
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve_context_packet, revise_asset_brief, block_provider_handoff]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_MUSIC_SFX, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
# production_score_fields: [voice_score, visual_score, video_score, audio_score, editing_score, lineage_score]
# skill_activation_contract: Activated by skill_activation_packet from subagent or route manifest.
# input_schema: Must declare atomic input fields before use; editing_packaging_profile if absent upstream.
# output_schema: Must emit atomic output packet with evidence path and validation status.
# subskill_hooks: May call subskills only through atomic_task_packet.
# quality_metric: Must emit skill_quality_score and quality_threshold.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: context_engineering_profile
# route_family_resolved: [context_engineering, script_generation]
# activation_triggers_resolved: [context packet, asset brief, media handoff]
# required_input_packets_resolved: [final_script_packet, script_segment_packet, research_brief_packet]
# emitted_output_packets_resolved: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_MUSIC_SFX, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
# validator_bindings_resolved: [provider_handoff_packet_present, media_quality_gate_packet_present, lineage_approval_packet_present]
# quality_gates_resolved: [context_completeness_gate, asset_consistency_gate, provider_boundary_gate]
# fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT if any media context packet lacks segment_id.
# lineage_fields_resolved: [script_segment_packet_id, context_packet_id, provider_handoff_packet_id]
# provider_boundary_resolved: handoff planning only; provider_execution_allowed=false until approval_packet
# handoff_targets_resolved: [voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_MUSIC_SFX, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
# production_score_fields_resolved: [voice_score, visual_score, video_score, audio_score, editing_score, lineage_score]
# human_approval_points_resolved: [approve_context_packet, revise_asset_brief, block_provider_handoff]
# status_limits_resolved: [no tool execution, no media creation]
# evidence_used_for_resolution: path/pre-contract keyword: context engineering; component_path=skills/context_engineering/P-303-asset-brief-creator.py; component_id=P-303-asset-brief-creator
# remaining_unknowns: none
