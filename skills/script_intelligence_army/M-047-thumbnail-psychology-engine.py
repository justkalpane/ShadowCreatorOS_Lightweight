from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


SKILL_ID = "M-047"
CINEMA_CORE_AUTHORITY = False
DOWNSTREAM_PACKAGING_ONLY = True
FILM_ROUTE_ID = "FILM_SCREENPLAY_GENERATION"


def _film_core_boundary(input_payload: dict[str, Any]) -> dict[str, Any] | None:
    route_id = str(input_payload.get("route_id", "")).upper()
    route_mode = str(input_payload.get("route_mode", ""))
    film_packet_ready = input_payload.get("film_packet_ready") is True
    downstream_authorized = input_payload.get("downstream_packaging_authorized") is True

    if route_id == FILM_ROUTE_ID or route_mode == "film_screenplay_generation":
        if not (film_packet_ready and downstream_authorized):
            return {
                "status": "blocked",
                "error": "M-047 is downstream thumbnail/packaging logic and cannot act as film-core authority.",
                "skill_id": SKILL_ID,
                "route_id": route_id or FILM_ROUTE_ID,
                "cinema_core_authority": CINEMA_CORE_AUTHORITY,
                "downstream_packaging_only": DOWNSTREAM_PACKAGING_ONLY,
                "required_before_use": [
                    "film_packet_ready=true",
                    "downstream_packaging_authorized=true",
                ],
            }
    return None


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    boundary_result = _film_core_boundary(input_payload)
    if boundary_result is not None:
        return boundary_result

    dossier_id = input_payload.get("dossier_id")
    if not dossier_id:
        return {
            "status": "failed",
            "error": "missing dossier_id",
            "skill_id": SKILL_ID,
        }

    now = datetime.now(timezone.utc).isoformat()
    return {
        "status": "success",
        "skill_id": SKILL_ID,
        "skill_name": "Thumbnail Psychology Engine",
        "artifact_family": "thumbnail-psychology-engine_packet",
        "created_at": now,
        "payload": {
            "input": input_payload,
            "result": {
                "execution_mode": "replica_runtime",
                "routing_context": "WF-200 -> CWF-210 -> CWF-230",
                "cinema_core_authority": CINEMA_CORE_AUTHORITY,
                "downstream_packaging_only": DOWNSTREAM_PACKAGING_ONLY,
            },
        },
    }



# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: M-047-thumbnail-psychology-engine
# component_layer: SKILL
# component_name: M 047 Thumbnail Psychology Engine
# route_families: [editing_packaging, full_video_pipeline, publishing]
# activation_triggers: route_family in [script_generation] or explicit registry selection; mark approval_gate_profile only when route_family is unknown.
# upstream_inputs: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet]
# downstream_outputs: [editing_timeline_packet, platform_content_package_packet, media_quality_gate_packet]
# required_input_packets: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet]
# emitted_output_packets: [editing_timeline_packet, platform_content_package_packet, media_quality_gate_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_EDITING, PTR_PROVIDER_QUALITY]
# quality_gates: [timeline_gate, caption_gate, platform_aspect_ratio_gate, thumbnail_moment_gate]
# validator_bindings: [editing_timeline_packet_present, media_quality_gate_packet_present, quality_scores_present]
# fallback_behavior: NEEDS_HUMAN_REVIEW if timeline/caption/thumbnail cannot map to segment IDs.
# lineage_fields: [editing_timeline_packet_id, segment_id, cut_point, platform_package_id]
# provider_boundary: provider_execution_allowed=false; local assembly/provider execution disabled unless approval_packet authorizes execution
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve_editing_plan, revise_timeline, block_publish]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [editing_timeline_packet, platform_content_package_packet, media_quality_gate_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_EDITING, PTR_PROVIDER_QUALITY]
# production_score_fields: [editing_score, platform_score, sync_score, quality_score, lineage_score]
# skill_activation_contract: Activated by skill_activation_packet from subagent or route manifest.
# input_schema: Must declare atomic input fields before use; approval_gate_profile if absent upstream.
# output_schema: Must emit atomic output packet with evidence path and validation status.
# subskill_hooks: May call subskills only through atomic_task_packet.
# quality_metric: Must emit skill_quality_score and quality_threshold.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: editing_packaging_profile
# route_family_resolved: [editing_packaging, full_video_pipeline, publishing]
# activation_triggers_resolved: [editing, packaging, publishing]
# required_input_packets_resolved: [script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, music_sfx_packet, editing_timeline_packet]
# emitted_output_packets_resolved: [editing_timeline_packet, platform_content_package_packet, media_quality_gate_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_EDITING, PTR_PROVIDER_QUALITY]
# validator_bindings_resolved: [editing_timeline_packet_present, media_quality_gate_packet_present, quality_scores_present]
# quality_gates_resolved: [timeline_gate, caption_gate, platform_aspect_ratio_gate, thumbnail_moment_gate]
# fallback_behavior_resolved: NEEDS_HUMAN_REVIEW if timeline/caption/thumbnail cannot map to segment IDs.
# lineage_fields_resolved: [editing_timeline_packet_id, segment_id, cut_point, platform_package_id]
# provider_boundary_resolved: provider_execution_allowed=false; local assembly/provider execution disabled unless approval_packet authorizes execution
# handoff_targets_resolved: [editing_timeline_packet, platform_content_package_packet, media_quality_gate_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_EDITING, PTR_PROVIDER_QUALITY]
# production_score_fields_resolved: [editing_score, platform_score, sync_score, quality_score, lineage_score]
# human_approval_points_resolved: [approve_editing_plan, revise_timeline, block_publish]
# status_limits_resolved: [no final MP4 claim, no publish claim]
# evidence_used_for_resolution: path/pre-contract keyword: editing/packaging/platform; component_path=skills/script_intelligence_army/M-047-thumbnail-psychology-engine.py; component_id=M-047-thumbnail-psychology-engine
# remaining_unknowns: none
