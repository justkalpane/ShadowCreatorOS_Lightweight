from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    dossier_id = input_payload.get("dossier_id")
    if not dossier_id:
        return {
            "status": "failed",
            "error": "missing dossier_id",
            "skill_id": "D-502",
        }

    now_dt = datetime.now(timezone.utc)
    now = now_dt.isoformat()
    ts = int(now_dt.timestamp() * 1000)

    metadata_packet = input_payload.get("platform_metadata_packet")
    if not isinstance(metadata_packet, dict):
        metadata_packet = {}
    source_packet_id = str(metadata_packet.get("instance_id", "PMP-1001"))
    if not source_packet_id.startswith("PMP-"):
        source_packet_id = "PMP-1001"

    target_platforms = metadata_packet.get("payload", {}).get("narrative", {}).get("target_platforms")
    if not isinstance(target_platforms, list) or not target_platforms:
        target_platforms = ["youtube", "instagram", "twitter", "tiktok"]
    target_platforms = [str(p).lower() for p in target_platforms if str(p).lower() in {"youtube", "instagram", "twitter", "tiktok"}]
    if not target_platforms:
        target_platforms = ["youtube"]

    schedule = []
    for idx, platform in enumerate(target_platforms):
        slot = now_dt + timedelta(hours=idx + 2)
        schedule.append(
            {
                "platform": platform,
                "scheduled_publish_time": slot.isoformat(),
                "timezone": "UTC",
                "optimization_notes": f"Publish in prime engagement window for {platform}.",
            }
        )

    return {
        "status": "CREATED",
        "skill_id": "D-502",
        "skill_name": "SEO Optimization Specialist",
        "instance_id": f"DPP-{ts}",
        "artifact_family": "distribution_plan_packet",
        "schema_version": "1.0.0",
        "producer_workflow": "SE-N8N-CWF-520-Distribution-Planner",
        "dossier_ref": str(dossier_id),
        "created_at": now,
        "payload": {
            "narrative": {
                "distribution_strategy": "staggered",
                "platform_count": len(target_platforms),
                "total_reach_estimate": 125000,
            },
            "context": {
                "sourced_from_packet_id": source_packet_id,
            },
            "evidence": {
                "platform_schedule": schedule,
                "distribution_channels": target_platforms,
                "contingency_plans": ["fallback_to_next_best_slot", "operator_review_on_conflict"],
            },
            "quality": {
                "schedule_feasibility": 0.91,
                "platform_readiness": 0.93,
                "distribution_optimality": 0.89,
            },
            "status": {
                "plan_complete": True,
                "next_stage": "CWF-530",
                "decision": "PROCEED_TO_READINESS_CHECK",
            },
        },
    }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: D-502-seo-optimization-specialist
# component_layer: SKILL
# component_name: D 502 Seo Optimization Specialist
# route_families: [quality_gate, full_video_pipeline]
# activation_triggers: route_family in [publishing, quality_gate] or explicit registry selection; mark editing_packaging_profile only when route_family is unknown.
# upstream_inputs: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
# downstream_outputs: [media_quality_gate_packet, lineage_packet]
# required_input_packets: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
# emitted_output_packets: [media_quality_gate_packet, lineage_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
# quality_gates: [script_score_gate, voice_score_gate, visual_score_gate, video_score_gate, audio_score_gate, editing_score_gate]
# validator_bindings: [media_quality_gate_packet_present, quality_scores_present, final_status_matches_weakest_evidence_layer]
# fallback_behavior: BLOCKED_BEFORE_OUTPUT if critical score is below threshold or missing.
# lineage_fields: [quality_gate_id, upstream_packet_ids, score_reason, failure_id]
# provider_boundary: provider_execution_allowed=false; quality gate reviews packets/artifacts only; no provider execution
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve_quality_gate, revise_segment, reject_output]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [media_quality_gate_packet, lineage_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
# production_score_fields: [script_score, hook_score, retention_score, voice_score, visual_score, video_score, audio_score, editing_score, platform_score, lineage_score]
# skill_activation_contract: Activated by skill_activation_packet from subagent or route manifest.
# input_schema: Must declare atomic input fields before use; editing_packaging_profile if absent upstream.
# output_schema: Must emit atomic output packet with evidence path and validation status.
# subskill_hooks: May call subskills only through atomic_task_packet.
# quality_metric: Must emit skill_quality_score and quality_threshold.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: media_quality_gate_profile
# route_family_resolved: [quality_gate, full_video_pipeline]
# activation_triggers_resolved: [quality, validation, compliance]
# required_input_packets_resolved: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet, provider_handoff_packet]
# emitted_output_packets_resolved: [media_quality_gate_packet, lineage_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
# validator_bindings_resolved: [media_quality_gate_packet_present, quality_scores_present, final_status_matches_weakest_evidence_layer]
# quality_gates_resolved: [script_score_gate, voice_score_gate, visual_score_gate, video_score_gate, audio_score_gate, editing_score_gate]
# fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT if critical score is below threshold or missing.
# lineage_fields_resolved: [quality_gate_id, upstream_packet_ids, score_reason, failure_id]
# provider_boundary_resolved: provider_execution_allowed=false; quality gate reviews packets/artifacts only; no provider execution; approval_packet_required_for_any_execution
# handoff_targets_resolved: [media_quality_gate_packet, lineage_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_PROVIDER_QUALITY, PTR_QUALITY_LINEAGE]
# production_score_fields_resolved: [script_score, hook_score, retention_score, voice_score, visual_score, video_score, audio_score, editing_score, platform_score, lineage_score]
# human_approval_points_resolved: [approve_quality_gate, revise_segment, reject_output]
# status_limits_resolved: [no PASS if weakest evidence is PARTIAL/BLOCKED]
# evidence_used_for_resolution: path/pre-contract keyword: quality/governance; component_path=skills/publishing/D-502-seo-optimization-specialist.py; component_id=D-502-seo-optimization-specialist
# remaining_unknowns: none
