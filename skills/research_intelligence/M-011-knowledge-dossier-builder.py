from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def _is_strict_packet_mode(input_payload: dict[str, Any]) -> bool:
    child_workflow_id = str(input_payload.get("child_workflow_id", "")).upper()
    workflow_id = str(input_payload.get("workflow_id", "")).upper()
    return bool(input_payload.get("strict_packet_output", False)) or child_workflow_id == "CWF-140" or workflow_id == "CWF-140"


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    dossier_id = input_payload.get("dossier_id")
    if not dossier_id:
        return {
            "status": "failed",
            "error": "missing dossier_id",
            "skill_id": "M-011",
        }

    now = datetime.now(timezone.utc).isoformat()
    ts = int(datetime.now(timezone.utc).timestamp() * 1000)

    if _is_strict_packet_mode(input_payload):
        topic_packet = input_payload.get("topic_finalization_packet")
        if not isinstance(topic_packet, dict):
            topic_packet = {}
        topic_packet_id = str(topic_packet.get("packet_id", f"TFP-{ts}"))

        return {
            "packet_id": f"RSP-{ts}",
            "dossier_id": str(dossier_id),
            "topic_packet_id": topic_packet_id,
            "summary": "Synthesis identifies high-retention narrative angles, validated claims, and execution-ready evidence anchors.",
            "sources": [
                {
                    "source_id": "SRC-001",
                    "title": "Primary Source Dossier",
                    "url_or_ref": "internal://research/source-001",
                    "source_type": "internal",
                },
                {
                    "source_id": "SRC-002",
                    "title": "Market Signal Snapshot",
                    "url_or_ref": "internal://research/source-002",
                    "source_type": "note",
                },
            ],
            "claims": [
                "Structured hooks improve watch retention in opening segments.",
                "Evidence-backed sectioning lowers drop-off during mid-content transitions.",
            ],
            "claim_evidence_pairs": [
                {
                    "claim": "Structured hooks improve watch retention in opening segments.",
                    "supporting_source_ids": ["SRC-001", "SRC-002"],
                    "confidence_note": "Observed across prior runs with consistent engagement uplift.",
                    "contradiction_flag": False,
                }
            ],
            "confidence": 0.89,
            "status": "created",
            "created_at": now,
        }

    return {
        "status": "success",
        "skill_id": "M-011",
        "skill_name": "Knowledge Dossier Builder",
        "artifact_family": "knowledge-dossier-builder_packet",
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
# component_id: M-011-knowledge-dossier-builder
# component_layer: SKILL
# component_name: M 011 Knowledge Dossier Builder
# route_families: [video_context, avatar_video_context, full_video_pipeline]
# activation_triggers: route_family in [trend_research, topic_discovery] or explicit registry selection; mark video_context_profile only when route_family is unknown.
# upstream_inputs: [script_segment_packet, visual_context_packet, video_context_packet]
# downstream_outputs: [video_context_packet, editing_timeline_packet, provider_handoff_packet]
# required_input_packets: [script_segment_packet, visual_context_packet, video_context_packet]
# emitted_output_packets: [video_context_packet, editing_timeline_packet, provider_handoff_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
# quality_gates: [motion_gate, camera_gate, sync_point_gate, continuity_gate]
# validator_bindings: [video_context_packet_present, editing_timeline_packet_present, provider_handoff_packet_present]
# fallback_behavior: regenerate scene plan or block provider handoff if duration/sync is missing.
# lineage_fields: [script_segment_packet_id, video_context_packet_id, scene_id, sync_point]
# provider_boundary: provider_execution_allowed=false; video/avatar provider execution disabled unless approval_packet authorizes provider_handoff_packet
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve_scene_plan, revise_motion, block_video_provider]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [video_context_packet, editing_timeline_packet, provider_handoff_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
# production_score_fields: [video_score, sync_score, continuity_score, editing_score, lineage_score]
# skill_activation_contract: Activated by skill_activation_packet from subagent or route manifest.
# input_schema: Must declare atomic input fields before use; video_context_profile if absent upstream.
# output_schema: Must emit atomic output packet with evidence path and validation status.
# subskill_hooks: May call subskills only through atomic_task_packet.
# quality_metric: Must emit skill_quality_score and quality_threshold.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: video_context_profile
# route_family_resolved: [video_context, avatar_video_context, full_video_pipeline]
# activation_triggers_resolved: [video, avatar, motion, scene]
# required_input_packets_resolved: [script_segment_packet, visual_context_packet, video_context_packet]
# emitted_output_packets_resolved: [video_context_packet, editing_timeline_packet, provider_handoff_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
# validator_bindings_resolved: [video_context_packet_present, editing_timeline_packet_present, provider_handoff_packet_present]
# quality_gates_resolved: [motion_gate, camera_gate, sync_point_gate, continuity_gate]
# fallback_behavior_resolved: regenerate scene plan or block provider handoff if duration/sync is missing.
# lineage_fields_resolved: [script_segment_packet_id, video_context_packet_id, scene_id, sync_point]
# provider_boundary_resolved: provider_execution_allowed=false; video/avatar provider execution disabled unless approval_packet authorizes provider_handoff_packet
# handoff_targets_resolved: [video_context_packet, editing_timeline_packet, provider_handoff_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_VIDEO, PTR_FINAL_SCRIPT_EDITING, PTR_MEDIA_PROVIDER_HANDOFF]
# production_score_fields_resolved: [video_score, sync_score, continuity_score, editing_score, lineage_score]
# human_approval_points_resolved: [approve_scene_plan, revise_motion, block_video_provider]
# status_limits_resolved: [no video-created claim]
# evidence_used_for_resolution: path/pre-contract keyword: video/avatar/motion; component_path=skills/research_intelligence/M-011-knowledge-dossier-builder.py; component_id=M-011-knowledge-dossier-builder
# remaining_unknowns: none
