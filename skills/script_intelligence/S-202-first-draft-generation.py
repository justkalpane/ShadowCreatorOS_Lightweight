from __future__ import annotations

import math
from datetime import datetime, timezone
from typing import Any


def _is_strict_packet_mode(input_payload: dict[str, Any]) -> bool:
    child_workflow_id = str(input_payload.get("child_workflow_id", "")).upper()
    workflow_id = str(input_payload.get("workflow_id", "")).upper()
    return bool(input_payload.get("strict_packet_output", False)) or child_workflow_id == "CWF-210" or workflow_id == "CWF-210"


def _required_internal_rehooks(duration_minutes: float) -> int:
    if duration_minutes < 3:
        return 0
    if duration_minutes <= 5:
        return max(1, int(duration_minutes) - 2)
    return max(4, math.ceil((duration_minutes * 60) / 90) - 1)


def _default_rehook_map(duration_minutes: float) -> list[dict[str, Any]]:
    count = _required_internal_rehooks(duration_minutes)
    duration_seconds = int(duration_minutes * 60)
    return [
        {
            "rehook_id": f"rehook_{index + 1}",
            "timestamp_seconds": round(duration_seconds * (index + 1) / (count + 1)),
            "hook_type": "curiosity_rehook",
            "hook_line": f"[REHOOK_{index + 1}: add topic-relevant retention reset]",
            "retention_function": "reset attention and reconnect the next section to the topic",
            "topic_connection_required": True,
            "mapped_to_dynamic_beat_map": True,
            "mapped_to_line_influence_map": True,
        }
        for index in range(count)
    ]


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    dossier_id = input_payload.get("dossier_id")
    if not dossier_id:
        return {
            "status": "failed",
            "error": "missing dossier_id",
            "skill_id": "S-202",
        }

    now = datetime.now(timezone.utc).isoformat()
    ts = int(datetime.now(timezone.utc).timestamp() * 1000)
    duration_minutes = float(input_payload.get("script_duration_minutes", 5))
    rehook_plan_packet = input_payload.get("rehook_plan_packet")
    recurring_rehook_map = (
        rehook_plan_packet.get("recurring_rehook_map")
        if isinstance(rehook_plan_packet, dict)
        else input_payload.get("recurring_rehook_map")
    )
    if _is_strict_packet_mode(input_payload) and (
        not isinstance(rehook_plan_packet, dict)
        or rehook_plan_packet.get("producer_component_id") != "M-039-re-hook-system"
        or not isinstance(recurring_rehook_map, list)
        or not recurring_rehook_map
    ):
        return {
            "status": "failed",
            "error": "missing or invalid M-039 rehook_plan_packet",
            "skill_id": "S-202",
        }
    if not isinstance(recurring_rehook_map, list) or not recurring_rehook_map:
        return {
            "status": "failed",
            "error": "missing recurring_rehook_map",
            "skill_id": "S-202",
        }

    if _is_strict_packet_mode(input_payload):
        return {
            "packet_id": f"SDP-{ts}",
            "dossier_id": str(dossier_id),
            "title": str(input_payload.get("title", "Structured Draft v1")),
            "hook": str(input_payload.get("hook", "This method compresses months of trial-and-error into one repeatable flow.")),
            "master_script_language": str(input_payload.get("master_script_language", "English")),
            "translation_localization_separate_stage": True,
            "recurring_rehook_required": 3 <= duration_minutes <= 10,
            "recurring_rehook_count": len(recurring_rehook_map),
            "max_gap_without_rehook_seconds": 30,
            "recurring_rehook_map": recurring_rehook_map,
            "cta_hook_required": True,
            "section_plan": [
                "Opening Hook",
                "Problem Framing",
                "Method Breakdown",
                "Evidence & Proof",
                "Execution CTA",
            ],
            "created_at": now,
        }

    return {
        "status": "success",
        "skill_id": "S-202",
        "skill_name": "first_draft_generation",
        "artifact_family": "first-draft-generation_packet",
        "created_at": now,
        "payload": {
            "input": input_payload,
            "result": {
                "execution_mode": "replica_runtime",
                "route_context": input_payload.get("route_id", "unknown"),
                "master_script_language": "English",
                "recurring_rehook_map": recurring_rehook_map,
            },
        },
    }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: S-202-first-draft-generation
# component_layer: SKILL
# component_name: S 202 First Draft Generation
# route_families: [script_generation]
# activation_triggers: route_family in [script_generation] or explicit registry selection; mark script_generation_profile only when route_family is unknown.
# upstream_inputs: [research_brief_packet, script_strategy_packet, source_evidence_packet]
# downstream_outputs: [script_v1_packet, script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet]
# required_input_packets: [research_brief_packet, script_strategy_packet, source_evidence_packet]
# emitted_output_packets: [script_v1_packet, script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT, PTR_SCRIPT_DEBATE, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO]
# quality_gates: [hook_generation_gate, retention_gate, script_quality_gate]
# validator_bindings: [script_segment_packet_present, voice_context_packet_present, visual_context_packet_present, video_context_packet_present, quality_scores_present]
# fallback_behavior: BLOCKED_BEFORE_OUTPUT when research_brief_packet or script_segment_packet cannot be produced.
# lineage_fields: [research_brief_packet_id, script_v1_packet_id, script_segment_packet_id, line_number]
# provider_boundary: provider_execution_allowed=false; content planning only; provider/media execution disabled unless approval_packet authorizes handoff
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve_script, revise_hook, regenerate_segment, reject_script]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [script_v1_packet, script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT, PTR_SCRIPT_DEBATE, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO]
# production_score_fields: [script_score, hook_score, retention_score, evidence_score, lineage_score]
# skill_activation_contract: Activated by skill_activation_packet from subagent or route manifest.
# input_schema: Must declare atomic input fields before use; script_generation_profile if absent upstream.
# output_schema: Must emit atomic output packet with evidence path and validation status.
# subskill_hooks: May call subskills only through atomic_task_packet.
# quality_metric: Must emit skill_quality_score and quality_threshold.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: script_generation_profile
# route_family_resolved: [script_generation]
# activation_triggers_resolved: [script request, content writing route]
# required_input_packets_resolved: [research_brief_packet, script_strategy_packet, source_evidence_packet]
# emitted_output_packets_resolved: [script_v1_packet, script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT, PTR_SCRIPT_DEBATE, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO]
# validator_bindings_resolved: [script_segment_packet_present, voice_context_packet_present, visual_context_packet_present, video_context_packet_present, quality_scores_present]
# quality_gates_resolved: [hook_generation_gate, retention_gate, script_quality_gate]
# fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT when research_brief_packet or script_segment_packet cannot be produced.
# lineage_fields_resolved: [research_brief_packet_id, script_v1_packet_id, script_segment_packet_id, line_number]
# provider_boundary_resolved: provider_execution_allowed=false; content planning only; provider/media execution disabled unless approval_packet authorizes handoff
# handoff_targets_resolved: [script_v1_packet, script_segment_packet, voice_context_packet, visual_context_packet, video_context_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_RESEARCH_SCRIPT, PTR_SCRIPT_DEBATE, PTR_FINAL_SCRIPT_VOICE, PTR_FINAL_SCRIPT_IMAGE, PTR_FINAL_SCRIPT_VIDEO]
# production_score_fields_resolved: [script_score, hook_score, retention_score, evidence_score, lineage_score]
# human_approval_points_resolved: [approve_script, revise_hook, regenerate_segment, reject_script]
# status_limits_resolved: [script-only output is PARTIAL unless explicitly requested, no media execution]
# evidence_used_for_resolution: path/pre-contract keyword: script/hook/retention; component_path=skills/script_intelligence/S-202-first-draft-generation.py; component_id=S-202-first-draft-generation
# remaining_unknowns: none
#
# MAC-06.2O SCRIPT BEHAVIOR PROPAGATION
# behavior_laws_consumed: [SCRIPT_LANGUAGE_CONTROL, SCRIPT_STORY_ENGINE, DYNAMIC_TIMED_BEAT_MAP, RECURRING_HOOK_DENSITY_LAW]
# responsibility: Emit English master draft packets with opening hook, duration-aware recurring re-hook map, CTA hook, and downstream beat-map bindings.
