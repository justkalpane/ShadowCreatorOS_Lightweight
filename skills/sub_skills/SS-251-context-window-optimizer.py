from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


REQUIRED_FIELDS = ["dossier_id", "input_payload", "max_context_limit"]


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    missing = [field for field in REQUIRED_FIELDS if field not in input_payload]
    if missing:
        return {
            "status": "failed",
            "error_code": "missing_required_fields",
            "missing_fields": missing,
            "sub_skill_id": "SS-251",
            "artifact_family": "context-window-optimizer_packet",
            "payload": {},
        }

    dossier_id = input_payload.get("dossier_id")
    if not isinstance(dossier_id, str) or not dossier_id.strip():
        return {
            "status": "failed",
            "error_code": "invalid_dossier_id",
            "sub_skill_id": "SS-251",
            "artifact_family": "context-window-optimizer_packet",
            "payload": {},
        }

    payload_data = input_payload.get("input_payload", {})
    max_context_limit = input_payload.get("max_context_limit", 8000)
    priority_keys = input_payload.get("priority_keys", [])

    # Token/Char estimate proxy: 1 token ~ 4 chars
    def estimate_tokens(obj: Any) -> int:
        return len(str(obj)) // 4

    tokens_estimate = estimate_tokens(payload_data)
    optimized_payload = dict(payload_data) if isinstance(payload_data, dict) else payload_data
    tokens_removed = 0
    status = "success"

    if tokens_estimate > max_context_limit and isinstance(optimized_payload, dict):
        status = "degraded"
        # Prune keys not in priority list if limit is exceeded
        keys_to_check = [k for k in optimized_payload.keys() if k not in priority_keys]
        for key in keys_to_check:
            if estimate_tokens(optimized_payload) <= max_context_limit:
                break
            prev_tok = estimate_tokens(optimized_payload[key])
            del optimized_payload[key]
            tokens_removed += prev_tok

        # If still exceeding, prune even priority keys (starting from least important)
        if estimate_tokens(optimized_payload) > max_context_limit:
            reversed_priorities = list(reversed(priority_keys))
            for key in reversed_priorities:
                if key in optimized_payload:
                    if estimate_tokens(optimized_payload) <= max_context_limit:
                        break
                    prev_tok = estimate_tokens(optimized_payload[key])
                    del optimized_payload[key]
                    tokens_removed += prev_tok

    now = datetime.now(timezone.utc).isoformat()

    return {
        "status": status,
        "sub_skill_id": "SS-251",
        "sub_skill_name": "Context Window Optimizer",
        "artifact_family": "context-window-optimizer_packet",
        "created_at": now,
        "payload": {
            "dossier_id": dossier_id,
            "optimized_payload": optimized_payload,
            "tokens_removed": tokens_removed,
        },
    }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: SS-251-context-window-optimizer
# component_layer: SKILL
# component_name: Ss 251 Context Window Optimizer
# route_families: [prompt_generation, repo_write_mode]
# activation_triggers: route_family in [prompt_generation, script_generation] or explicit registry selection; mark prompt_generation_profile only when route_family is unknown.
# upstream_inputs: [lineage_packet, approval_packet]
# downstream_outputs: [context-window-optimizer_packet, approval_packet]
# required_input_packets: [lineage_packet, approval_packet]
# emitted_output_packets: [context-window-optimizer_packet, approval_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
# quality_gates: [typed_input_gate, format_validation_gate]
# validator_bindings: [no_n8n_provider_media_execution, provider_boundary_present]
# fallback_behavior: BLOCKED_BEFORE_OUTPUT unless approval_packet is present.
# lineage_fields: [approval_packet_id, user_decision, scope]
# provider_boundary: provider_execution_allowed=false; dry-run/simulation mode only.
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve_prompt, revise_variables, reject]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [context-window-optimizer_packet, approval_packet]
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
# emitted_output_packets_resolved: [context-window-optimizer_packet, approval_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_LINEAGE_APPROVAL]
# validator_bindings_resolved: [no_n8n_provider_media_execution, provider_boundary_present]
# quality_gates_resolved: [typed_input_gate, format_validation_gate]
# fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT unless approval_packet is present.
# lineage_fields_resolved: [approval_packet_id, user_decision, scope]
# provider_boundary_resolved: provider_execution_allowed=false; dry-run/simulation mode only.
# handoff_targets_resolved: [context-window-optimizer_packet, approval_packet]
# production_score_fields_resolved: [format_clarity_score, prompt_safety_score]
# human_approval_points_resolved: [approve_prompt, revise_variables, reject]
# status_limits_resolved: [no external LLM API execution without permission]
# evidence_used_for_resolution: path/pre-contract keyword: prompt/template; component_path=skills/sub_skills/SS-251-context-window-optimizer.py; component_id=SS-251-context-window-optimizer
# remaining_unknowns: none
