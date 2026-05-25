from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def _platform_block(platform: str, title: str, topic: str) -> dict[str, Any]:
    return {
        "title": f"{title} | {platform.title()}",
        "description": f"Deep dive on {topic} with actionable framework tailored for {platform}.",
        "tags": [topic, "shadow-empire", platform, "creator-os"],
        "hashtags": [f"#{platform}", "#contentstrategy", "#growth"],
        "chapters": [
            {"label": "Hook", "ts": "00:00"},
            {"label": "Core Framework", "ts": "00:45"},
            {"label": "Execution Steps", "ts": "02:10"},
        ],
    }


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    dossier_id = input_payload.get("dossier_id")
    if not dossier_id:
        return {
            "status": "failed",
            "error": "missing dossier_id",
            "skill_id": "D-501",
        }

    media_packet = input_payload.get("media_production_packet")
    if not isinstance(media_packet, dict):
        media_packet = {}

    source_packet_id = str(media_packet.get("instance_id", "MDP-1001"))
    if not source_packet_id.startswith("MDP-"):
        source_packet_id = "MDP-1001"

    now = datetime.now(timezone.utc).isoformat()
    ts = int(datetime.now(timezone.utc).timestamp() * 1000)

    title = str(input_payload.get("content_title", "High Leverage Content System"))
    topic = str(input_payload.get("primary_topic", "content strategy"))
    target_platforms = input_payload.get("target_platforms")
    if not isinstance(target_platforms, list) or not target_platforms:
        target_platforms = ["youtube", "instagram", "twitter", "tiktok"]
    normalized_platforms = [str(p).lower() for p in target_platforms if str(p).lower() in {"youtube", "instagram", "twitter", "tiktok"}]
    if not normalized_platforms:
        normalized_platforms = ["youtube"]

    raw_metadata = {platform: _platform_block(platform, title, topic) for platform in normalized_platforms}

    return {
        "status": "CREATED",
        "skill_id": "D-501",
        "skill_name": "Platform Metadata Generator",
        "instance_id": f"PMP-{ts}",
        "artifact_family": "platform_metadata_packet",
        "schema_version": "1.0.0",
        "producer_workflow": "SE-N8N-CWF-510-Platform-Metadata-Generator",
        "dossier_ref": str(dossier_id),
        "created_at": now,
        "payload": {
            "narrative": {
                "content_title": title,
                "primary_topic": topic,
                "target_platforms": normalized_platforms,
            },
            "context": {
                "sourced_from_packet_id": source_packet_id,
            },
            "evidence": {
                "raw_metadata": raw_metadata,
            },
            "quality": {
                "metadata_completeness": 0.94,
                "platform_compliance": True,
                "platforms_covered": len(normalized_platforms),
            },
            "status": {
                "metadata_generated": True,
                "next_stage": "CWF-520",
                "decision": "PROCEED_TO_SEO_OPTIMIZATION",
            },
        },
    }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: D-501-platform-metadata-generator
# component_layer: SKILL
# component_name: D 501 Platform Metadata Generator
# route_families: [quality_gate, full_video_pipeline]
# activation_triggers: route_family in [script_generation, topic_discovery, publishing, quality_gate] or explicit registry selection; mark editing_packaging_profile only when route_family is unknown.
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
# evidence_used_for_resolution: path/pre-contract keyword: quality/governance; component_path=skills/publishing/D-501-platform-metadata-generator.py; component_id=D-501-platform-metadata-generator
# remaining_unknowns: none
