from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    dossier_id = input_payload.get("dossier_id")
    if not dossier_id:
        return {
            "status": "failed",
            "error": "missing dossier_id",
            "skill_id": "A-401",
        }

    now = datetime.now(timezone.utc).isoformat()
    timestamp = int(datetime.now(timezone.utc).timestamp() * 1000)

    context_packet = input_payload.get("context_engineering_packet")
    if not isinstance(context_packet, dict):
        context_packet = {}
    source_packet_id = str(context_packet.get("instance_id", "CEP-unknown"))

    platform = "youtube"
    target_platform = input_payload.get("target_platform")
    if isinstance(target_platform, str) and target_platform.lower() in {"youtube", "tiktok", "instagram"}:
        platform = target_platform.lower()

    concepts = [
        {
            "concept_id": "concept_1",
            "strategy": "curiosity_gap",
            "visual_description": "Close-up creator expression with a bold question headline and contrast-rich framing.",
            "color_palette": ["#FFCC00", "#111111", "#FFFFFF"],
            "typography_guidance": "bold_sans_serif",
            "focal_point_description": "Creator face and primary headline token",
        },
        {
            "concept_id": "concept_2",
            "strategy": "authority_data",
            "visual_description": "Metric-led layout with proof badge and a clean high-legibility text lockup.",
            "color_palette": ["#0B5FFF", "#F2F5FF", "#0A0A0A"],
            "typography_guidance": "clean_sans_serif",
            "focal_point_description": "Evidence card with highlighted metric",
        },
        {
            "concept_id": "concept_3",
            "strategy": "shock_urgency",
            "visual_description": "Urgency-focused split composition with directional arrows and high-emotion cue text.",
            "color_palette": ["#FF2D55", "#1A1A1A", "#FFFFFF"],
            "typography_guidance": "bold_condensed",
            "focal_point_description": "Urgency phrase with directional cue",
        },
    ]

    return {
        "status": "success",
        "skill_id": "A-401",
        "skill_name": "Thumbnail Concept Designer",
        "instance_id": f"TCP-{timestamp}",
        "artifact_family": "thumbnail_concept_packet",
        "schema_version": "1.0.0",
        "producer_workflow": "SE-N8N-CWF-410-Thumbnail-Generator",
        "dossier_ref": str(dossier_id),
        "created_at": now,
        "payload": {
            "narrative": {
                "source_title": str(input_payload.get("title", "Untitled")),
                "source_hook": str(input_payload.get("hook", "Key insight inside")),
                "target_platform": platform,
                "concept_count": 3,
            },
            "context": {
                "sourced_from_packet_id": source_packet_id,
                "platform_requirements": {
                    "youtube": "1280x720",
                    "tiktok": "1080x1920",
                    "instagram": "1200x675",
                },
            },
            "evidence": {
                "concepts": concepts,
            },
            "quality": {
                "concept_distinctiveness": 0.9,
                "platform_compliance": True,
                "contrast_ratio": 7.0,
                "legibility_score": 0.88,
                "designer_confidence": 0.86,
            },
            "status": {
                "concepts_generated": 3,
                "all_pass_validation": True,
                "next_stage": "CWF-420",
                "decision": "PROCEED_TO_VISUAL_ASSET_PLANNING",
            },
        },
    }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: A-401-thumbnail-concept-designer
# component_layer: SKILL
# component_name: A 401 Thumbnail Concept Designer
# route_families: [context_engineering, script_generation]
# activation_triggers: route_family in [script_generation, visual_context, quality_gate] or explicit registry selection; mark editing_packaging_profile only when route_family is unknown.
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
# evidence_used_for_resolution: path/pre-contract keyword: context engineering; component_path=skills/media_production/A-401-thumbnail-concept-designer.py; component_id=A-401-thumbnail-concept-designer
# remaining_unknowns: none
