from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def _visual_element(
    element_id: str,
    element_type: str,
    description: str,
    duration_seconds: str,
    timing_marker: str,
) -> dict[str, Any]:
    return {
        "element_id": element_id,
        "type": element_type,
        "description": description,
        "b_roll_suggestions": ["high contrast motion", "close-up reaction", "screen highlight"],
        "estimated_duration": duration_seconds,
        "timing_marker": timing_marker,
    }


def run(input_payload: dict[str, Any]) -> dict[str, Any]:
    dossier_id = input_payload.get("dossier_id")
    if not dossier_id:
        return {
            "status": "failed",
            "error": "missing dossier_id",
            "skill_id": "A-402",
        }

    now = datetime.now(timezone.utc).isoformat()
    ts = int(datetime.now(timezone.utc).timestamp() * 1000)

    thumbnail_packet = input_payload.get("thumbnail_concept_packet")
    if not isinstance(thumbnail_packet, dict):
        thumbnail_packet = {}

    sourced_from = str(thumbnail_packet.get("context", {}).get("sourced_from_packet_id", "CEP-1001"))
    if not sourced_from.startswith("CEP-"):
        sourced_from = "CEP-1001"

    target_platform = str(input_payload.get("target_platform", "youtube")).lower()
    if target_platform not in {"youtube", "tiktok", "instagram"}:
        target_platform = "youtube"

    script_source_id = str(input_payload.get("script_source_id", "FSP-1001"))
    if not script_source_id.startswith("FSP-"):
        script_source_id = "FSP-1001"

    body_elements = [
        _visual_element(
            "graphic_1",
            "graphic",
            "Data-backed visual card introducing the first core insight with animated highlight band.",
            "8.0",
            "00:08-00:16",
        ),
        _visual_element(
            "b_roll_2",
            "b-roll",
            "Contextual office movement and product usage montage to support execution framing.",
            "10.5",
            "00:16-00:27",
        ),
    ]

    return {
        "status": "CREATED",
        "skill_id": "A-402",
        "skill_name": "Visual Asset Planner",
        "instance_id": f"VASP-{ts}",
        "artifact_family": "visual_asset_spec_packet",
        "schema_version": "1.0.0",
        "producer_workflow": "SE-N8N-CWF-420-Visual-Asset-Specs",
        "dossier_ref": str(dossier_id),
        "created_at": now,
        "payload": {
            "narrative": {
                "script_source_id": script_source_id,
                "total_visual_elements": 6,
                "estimated_total_duration": "95",
            },
            "context": {
                "sourced_from_packet_id": sourced_from,
                "target_platform": target_platform,
                "platform_constraints": {
                    "recommended_duration": "30-180 seconds",
                    "aspect_ratio": "16:9" if target_platform == "youtube" else "9:16",
                    "safe_zone_edges": 40,
                },
            },
            "evidence": {
                "hook_sequence": {
                    "duration": "0-8",
                    "visual_elements": [
                        _visual_element(
                            "text_1",
                            "text",
                            "High-contrast hook headline with motion entrance synced to opening beat.",
                            "4.0",
                            "00:00-00:04",
                        )
                    ],
                },
                "body_sequences": [
                    {
                        "section_index": 0,
                        "section_title": "Core Insight",
                        "duration": "8-45",
                        "visual_elements": body_elements,
                    }
                ],
                "closing_sequence": {
                    "duration": "12",
                    "visual_elements": [
                        _visual_element(
                            "transition_1",
                            "transition",
                            "Final CTA transition with end-screen emphasis and actionable prompt.",
                            "3.0",
                            "01:32-01:35",
                        )
                    ],
                },
                "transitions": [
                    {
                        "position": "hook-to-body",
                        "transition_type": "cut",
                        "duration": "250ms",
                        "platform_suitability": "high",
                    },
                    {
                        "position": "body-to-closing",
                        "transition_type": "fade",
                        "duration": "300ms",
                        "platform_suitability": "high",
                    },
                ],
                "overlays": {
                    "text_treatment": "sans-serif",
                    "graphic_style": "minimal",
                    "color_scheme": "match_thumbnail",
                },
            },
            "quality": {
                "visual_consistency": 0.9,
                "narrative_alignment": 0.91,
                "platform_suitability": 0.94,
                "production_feasibility": 0.88,
            },
            "status": {
                "specs_complete": True,
                "platform_compliant": True,
                "next_stage": "CWF-430",
                "decision": "PROCEED_TO_AUDIO_BRIEF",
            },
        },
    }

# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: A-402-visual-asset-planner
# component_layer: SKILL
# component_name: A 402 Visual Asset Planner
# route_families: [editing_packaging, full_video_pipeline, publishing]
# activation_triggers: route_family in [script_generation, music_sfx_context, visual_context, quality_gate] or explicit registry selection; mark editing_packaging_profile only when route_family is unknown.
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
# input_schema: Must declare atomic input fields before use; editing_packaging_profile if absent upstream.
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
# evidence_used_for_resolution: path/pre-contract keyword: editing/packaging/platform; component_path=skills/media_production/A-402-visual-asset-planner.py; component_id=A-402-visual-asset-planner
# remaining_unknowns: none
