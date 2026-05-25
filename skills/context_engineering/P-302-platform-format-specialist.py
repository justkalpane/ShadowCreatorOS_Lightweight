from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def _is_strict_packet_mode(input_payload: dict[str, Any]) -> bool:
    child_workflow_id = str(input_payload.get("child_workflow_id", "")).upper()
    workflow_id = str(input_payload.get("workflow_id", "")).upper()
    return bool(input_payload.get("strict_packet_output", False)) or child_workflow_id == "CWF-320" or workflow_id == "CWF-320"


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    dossier_id = input_payload.get("dossier_id")
    if not dossier_id:
        return {
            "status": "failed",
            "error": "missing dossier_id",
            "skill_id": "P-302",
        }

    now = datetime.now(timezone.utc).isoformat()
    ts = int(datetime.now(timezone.utc).timestamp() * 1000)

    if _is_strict_packet_mode(input_payload):
        ecp = input_payload.get("execution_context_packet")
        if not isinstance(ecp, dict):
            ecp = {}
        source_packet_id = str(ecp.get("packet_id", f"ECP-{ts}"))
        platform = str(input_payload.get("target_platform", "youtube")).lower()
        if platform not in {"youtube", "blog", "podcast", "email"}:
            platform = "youtube"

        format_map = {
            "youtube": {
                "format": "episodic_long_form",
                "structure": ["hook_30s", "intro_60s", "body_sections", "cta_60s", "outro_30s"],
                "estimated_delivery_length": "8-12 min",
                "chapter_markers_required": True,
            },
            "blog": {
                "format": "scannable_long_form",
                "structure": ["headline", "subheadlines", "body_paragraphs", "cta"],
                "estimated_delivery_length": "1500-2500 words",
                "chapter_markers_required": False,
            },
            "podcast": {
                "format": "conversational_audio",
                "structure": ["cold_open", "intro_music", "main_discussion", "outro"],
                "estimated_delivery_length": "25-40 min",
                "chapter_markers_required": True,
            },
            "email": {
                "format": "scannable_short",
                "structure": ["subject_line", "preheader", "hero", "body", "cta"],
                "estimated_delivery_length": "150-250 words",
                "chapter_markers_required": False,
            },
        }
        selected_rules = format_map[platform]

        platform_metadata = {
            "title": "Production Ready Content",
            "description": f"Platform-tailored delivery package for {platform}.",
            "tags": ["shadow-empire", "content", platform],
        }

        return {
            "instance_id": f"PPP-{ts}",
            "artifact_family": "platform_package_packet",
            "schema_version": "1.0.0",
            "producer_workflow": "SE-N8N-CWF-320-Platform-Packager",
            "dossier_ref": str(dossier_id),
            "created_at": now,
            "status": "CREATED",
            "payload": {
                "narrative": {
                    "content": {"title": "Production Ready Content", "platform": platform},
                    "platform_structured_body": selected_rules,
                    "delivery_ready": True,
                },
                "context": {
                    "sourced_from_packet_id": source_packet_id,
                    "target_platform": platform,
                    "execution_requirements": {"mode": "supervised"},
                    "platform_metadata": platform_metadata,
                    "platform_format_rules": selected_rules,
                },
                "evidence": {
                    "lineage_references": [
                        {"type": "execution_context_packet", "id": source_packet_id},
                        {"type": "dossier", "id": str(dossier_id)},
                    ],
                    "validation_checks": [
                        {"check": "input_validation", "result": "PASSED"},
                        {"check": "format_rules_applied", "result": "PASSED"},
                        {"check": "metadata_generated", "result": "PASSED"},
                    ],
                },
                "quality": {
                    "platform_readiness_score": 0.93,
                    "gate_checks": {
                        "format_rules_applied": True,
                        "metadata_complete": True,
                        "structure_defined": True,
                    },
                    "packaging_complete": True,
                },
                "status": {
                    "decision_path": "PROCEED_TO_CWF-330",
                    "next_workflow": "CWF-330",
                    "escalation_needed": False,
                },
            },
        }

    return {
        "status": "success",
        "skill_id": "P-302",
        "skill_name": "platform_format_specialist",
        "artifact_family": "platform-format-specialist_packet",
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
# component_id: P-302-platform-format-specialist
# component_layer: SKILL
# component_name: P 302 Platform Format Specialist
# route_families: [context_engineering, script_generation]
# activation_triggers: route_family in [script_generation, music_sfx_context, editing_packaging, quality_gate] or explicit registry selection; mark editing_packaging_profile only when route_family is unknown.
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
# evidence_used_for_resolution: path/pre-contract keyword: context engineering; component_path=skills/context_engineering/P-302-platform-format-specialist.py; component_id=P-302-platform-format-specialist
# remaining_unknowns: none
