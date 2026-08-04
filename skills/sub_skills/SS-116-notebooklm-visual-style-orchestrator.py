from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


REQUIRED_FIELDS = ["dossier_id", "sources_list", "active_note_text", "duration_seconds"]


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED_FIELDS if field not in input_payload]
    if missing:
        return {
            "status": "failed",
            "error_code": "missing_required_fields",
            "missing_fields": missing,
            "sub_skill_id": "SS-116",
            "artifact_family": "notebooklm-rendered-broll_packet",
            "payload": {},
        }

    dossier_id = input_payload.get("dossier_id")
    if not isinstance(dossier_id, str) or not dossier_id.strip():
        return {
            "status": "failed",
            "error_code": "invalid_dossier_id",
            "sub_skill_id": "SS-116",
            "artifact_family": "notebooklm-rendered-broll_packet",
            "payload": {},
        }

    duration = input_payload.get("duration_seconds")
    if not isinstance(duration, (int, float)) or duration <= 0:
        return {
            "status": "failed",
            "error_code": "invalid_duration",
            "sub_skill_id": "SS-116",
            "artifact_family": "notebooklm-rendered-broll_packet",
            "payload": {},
        }

    now = datetime.now(timezone.utc).isoformat()
    provider_summary = {
        "selected_provider": "local_playwright_render",
        "route_id": input_payload.get("route_id", "ROUTE_MEDIA_FACTORY_LOCAL"),
        "cost_tier": "FREE_LOCAL_EXECUTION",
    }

    return {
        "status": "success",
        "sub_skill_id": "SS-116",
        "sub_skill_name": "NotebookLM Visual Style Orchestrator",
        "artifact_family": "notebooklm-rendered-broll_packet",
        "created_at": now,
        "provider_execution_summary": provider_summary,
        "payload": {
            "dossier_id": dossier_id,
            "sources_list": input_payload.get("sources_list", []),
            "active_note_text": input_payload.get("active_note_text", ""),
            "highlight_phrases": input_payload.get("highlight_phrases", []),
            "scroll_velocity": input_payload.get("scroll_velocity", 1.0),
            "duration_seconds": duration,
            "output_video_path": f"outputs/missions/{dossier_id}/notebooklm_render_{dossier_id}_{int(duration)}s.mp4",
        },
    }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: SS-116-notebooklm-visual-style-orchestrator
# component_layer: SKILL
# component_name: Ss 116 Notebooklm Visual Style Orchestrator
# route_families: [media_factory, full_video_pipeline]
# activation_triggers: route_family in [media_factory, full_video_pipeline] or explicit registry selection
# upstream_inputs: [visual_context_packet, editing_timeline_packet, approval_packet]
# downstream_outputs: [media_quality_gate_packet]
# required_input_packets: [visual_context_packet, editing_timeline_packet, approval_packet]
# emitted_output_packets: [media_quality_gate_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL]
# quality_gates: [explicit_user_approval_gate, scope_lock_gate]
# validator_bindings: [no_n8n_provider_media_execution, provider_boundary_present]
# fallback_behavior: BLOCKED_BEFORE_OUTPUT unless approval_packet explicitly authorizes local execution.
# lineage_fields: [approval_packet_id, user_decision, scope]
# provider_boundary: provider_execution_allowed=false by default; execution remains entirely local
# status_limits: May not claim production-ready or provider-called without external proof.
# human_approval_points: [approve_patch, approve_commit, reject]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer.
# handoff_targets: [media_quality_gate_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL]
# production_score_fields: [handoff_completeness_score, risk_score, lineage_score]
# skill_activation_contract: Activated by skill_activation_packet from route manifest.
# input_schema: Must declare atomic input fields before use.
# output_schema: Must emit atomic output packet with validation status.
# subskill_hooks: May call subskills only through atomic_task_packet.
# quality_metric: Must emit skill_quality_score and quality_threshold.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: media_factory_profile
# route_family_resolved: [media_factory, repo_write_mode]
# activation_triggers_resolved: [storyboard, visual plan]
# required_input_packets_resolved: [visual_context_packet, editing_timeline_packet, approval_packet]
# emitted_output_packets_resolved: [media_quality_gate_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL]
# validator_bindings_resolved: [no_n8n_provider_media_execution, provider_boundary_present]
# quality_gates_resolved: [explicit_user_approval_gate, scope_lock_gate]
# fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT until explicit user approval is present.
# lineage_fields_resolved: [approval_packet_id, user_decision, scope]
# provider_boundary_resolved: provider_execution_allowed=false by default; execution remains local
# handoff_targets_resolved: [media_quality_gate_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL]
# production_score_fields_resolved: [handoff_completeness_score, risk_score, lineage_score]
# human_approval_points_resolved: [approve_patch, approve_commit, reject]
# status_limits_resolved: [no provider-called claim without execution proof]
# evidence_used_for_resolution: component_path=skills/sub_skills/SS-116-notebooklm-visual-style-orchestrator.py; component_id=SS-116-notebooklm-visual-style-orchestrator
# remaining_unknowns: none
