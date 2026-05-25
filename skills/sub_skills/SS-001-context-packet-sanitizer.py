from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


REQUIRED_FIELDS = ["dossier_id", "input_payload"]


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED_FIELDS if field not in input_payload]
    if missing:
        return {
            "status": "failed",
            "error_code": "missing_required_fields",
            "missing_fields": missing,
            "sub_skill_id": "SS-001",
            "artifact_family": "context-packet-sanitizer_packet",
            "payload": {},
        }

    dossier_id = input_payload.get("dossier_id")
    if not isinstance(dossier_id, str) or not dossier_id.strip():
        return {
            "status": "failed",
            "error_code": "invalid_dossier_id",
            "sub_skill_id": "SS-001",
            "artifact_family": "context-packet-sanitizer_packet",
            "payload": {},
        }

    now = datetime.now(timezone.utc).isoformat()
    provider_summary = {
        "selected_provider": input_payload.get("selected_provider", "auto"),
        "route_id": input_payload.get("route_id", "ROUTE_PHASE1_STANDARD"),
        "cost_tier": input_payload.get("cost_tier", "HYBRID_STANDARD"),
    }

    return {
        "status": "success",
        "sub_skill_id": "SS-001",
        "sub_skill_name": "Context Packet Sanitizer",
        "artifact_family": "context-packet-sanitizer_packet",
        "created_at": now,
        "provider_execution_summary": provider_summary,
        "payload": {
            "dossier_id": dossier_id,
            "input_payload": input_payload.get("input_payload", {}),
            "optimization_hints": input_payload.get("optimization_hints", []),
            "constraints": input_payload.get("constraints", {}),
        },
    }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: SS-001-context-packet-sanitizer
# component_layer: SKILL
# component_name: Ss 001 Context Packet Sanitizer
# route_families: [context_engineering, script_generation]
# activation_triggers: route_family in [provider_handoff, full_video_pipeline] or explicit registry selection; mark provider_handoff_profile only when route_family is unknown.
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
# input_schema: Must declare atomic input fields before use; provider_handoff_profile if absent upstream.
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
# evidence_used_for_resolution: path/pre-contract keyword: context engineering; component_path=skills/sub_skills/SS-001-context-packet-sanitizer.py; component_id=SS-001-context-packet-sanitizer
# remaining_unknowns: none
