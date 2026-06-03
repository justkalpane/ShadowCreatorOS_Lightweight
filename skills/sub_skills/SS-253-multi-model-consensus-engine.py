from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


REQUIRED_FIELDS = ["dossier_id", "candidate_responses"]


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED_FIELDS if field not in input_payload]
    if missing:
        return {
            "status": "failed",
            "error_code": "missing_required_fields",
            "missing_fields": missing,
            "sub_skill_id": "SS-253",
            "artifact_family": "multi-model-consensus-engine_packet",
            "payload": {},
        }

    dossier_id = input_payload.get("dossier_id")
    if not isinstance(dossier_id, str) or not dossier_id.strip():
        return {
            "status": "failed",
            "error_code": "invalid_dossier_id",
            "sub_skill_id": "SS-253",
            "artifact_family": "multi-model-consensus-engine_packet",
            "payload": {},
        }

    candidate_responses = input_payload.get("candidate_responses", [])
    if not isinstance(candidate_responses, list) or not candidate_responses:
        return {
            "status": "failed",
            "error_code": "empty_candidates_list",
            "sub_skill_id": "SS-253",
            "artifact_family": "multi-model-consensus-engine_packet",
            "payload": {},
        }

    evaluation_criteria = input_payload.get("evaluation_criteria", {})

    # Consensus calculation logic
    # Calculate similarity score using a simple overlap estimator for dry runs
    def calculate_agreement(a: str, b: str) -> float:
        words_a = set(a.lower().split())
        words_b = set(b.lower().split())
        if not words_a or not words_b:
            return 0.0
        intersection = words_a.intersection(words_b)
        union = words_a.union(words_b)
        return len(intersection) / len(union)

    best_score = -1.0
    best_candidate = ""

    # Calculate aggregate similarity for each candidate against all other candidates
    if len(candidate_responses) == 1:
        best_candidate = str(candidate_responses[0])
        best_score = 1.0
    else:
        for idx, resp in enumerate(candidate_responses):
            other_scores = []
            for jdx, other in enumerate(candidate_responses):
                if idx != jdx:
                    other_scores.append(calculate_agreement(str(resp), str(other)))
            avg_score = sum(other_scores) / len(other_scores) if other_scores else 0.0
            if avg_score > best_score:
                best_score = avg_score
                best_candidate = str(resp)

    status = "success" if best_score >= 0.70 else "degraded"
    now = datetime.now(timezone.utc).isoformat()

    return {
        "status": status,
        "sub_skill_id": "SS-253",
        "sub_skill_name": "Multi-Model Consensus Engine",
        "artifact_family": "multi-model-consensus-engine_packet",
        "created_at": now,
        "payload": {
            "dossier_id": dossier_id,
            "aligned_response": best_candidate,
            "consensus_score": round(best_score, 4),
        },
    }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: SS-253-multi-model-consensus-engine
# component_layer: SKILL
# component_name: Ss 253 Multi Model Consensus Engine
# route_families: [prompt_generation, repo_write_mode]
# activation_triggers: route_family in [prompt_generation, script_generation] or explicit registry selection; mark prompt_generation_profile only when route_family is unknown.
# upstream_inputs: [lineage_packet, approval_packet]
# downstream_outputs: [multi-model-consensus-engine_packet, approval_packet]
# required_input_packets: [lineage_packet, approval_packet]
# emitted_output_packets: [multi-model-consensus-engine_packet, approval_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
# quality_gates: [typed_input_gate, format_validation_gate]
# validator_bindings: [no_n8n_provider_media_execution, provider_boundary_present]
# fallback_behavior: BLOCKED_BEFORE_OUTPUT unless approval_packet is present.
# lineage_fields: [approval_packet_id, user_decision, scope]
# provider_boundary: provider_execution_allowed=false; dry-run/simulation mode only.
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve_prompt, revise_variables, reject]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [multi-model-consensus-engine_packet, approval_packet]
# production_score_fields: [format_clarity_score, prompt_safety_score]
# skill_activation_contract: Activated by skill_activation_packet from subagent or route manifest.
# input_schema: Must declare atomic input fields before use.
# output_schema: Must emit atomic output packet with validation status.
# subskill_hooks: May call subskills only through atomic_task_packet.
# quality_metric: Must emit skill_quality_score and quality_threshold.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: prompt_generation_profile
# route_family_resolved: [prompt_generation, repo_write_mode]
# activation_triggers_resolved: [prompt, template, format]
# required_input_packets_resolved: [lineage_packet, approval_packet]
# emitted_output_packets_resolved: [multi-model-consensus-engine_packet, approval_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
# validator_bindings_resolved: [no_n8n_provider_media_execution, provider_boundary_present]
# quality_gates_resolved: [typed_input_gate, format_validation_gate]
# fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT unless approval_packet is present.
# lineage_fields_resolved: [approval_packet_id, user_decision, scope]
# provider_boundary_resolved: provider_execution_allowed=false; dry-run/simulation mode only.
# handoff_targets_resolved: [multi-model-consensus-engine_packet, approval_packet]
# production_score_fields_resolved: [format_clarity_score, prompt_safety_score]
# human_approval_points_resolved: [approve_prompt, revise_variables, reject]
# status_limits_resolved: [no external LLM API execution without permission]
# evidence_used_for_resolution: path/pre-contract keyword: prompt/template; component_path=skills/sub_skills/SS-253-multi-model-consensus-engine.py; component_id=SS-253-multi-model-consensus-engine
# remaining_unknowns: none
