from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
from agents.common.production_agent_base import ProductionAgentBase, print_run


class MayaAgent(ProductionAgentBase):
    PALETTES = {
        "yash_story_arc": {
            "palette_id": "yash_story_arc",
            "purpose": "Opening cinematic struggle-to-rise arc for the Yash self-investment mission.",
            "primary": "#0E1B24",
            "secondary": "#F5A623",
            "accent": "#FFD54F",
            "shadow": "#111111",
            "delivery_standard": "Rec.709",
            "notes": "Teal city shadows, amber sodium practicals, gold transformation highlights."
        },
        "yash_presenter": {
            "palette_id": "yash_presenter",
            "purpose": "Presenter A-roll continuity for direct motivational teaching blocks.",
            "primary": "#2C2C2C",
            "secondary": "#D89B2B",
            "accent": "#FFFFFF",
            "shadow": "#171717",
            "delivery_standard": "Rec.709",
            "notes": "Charcoal studio, warm gold rim light, white captions with gold keyword emphasis."
        },
        "yash_notebooklm": {
            "palette_id": "yash_notebooklm",
            "purpose": "NotebookLM-style HyperFrames slide scenes.",
            "primary": "#FBF9F6",
            "secondary": "#2C2C2C",
            "accent": "#FFB300",
            "shadow": "#E8E0D0",
            "delivery_standard": "Rec.709",
            "notes": "Warm paper background, dark gray text, gold active-note glow and highlight boxes."
        }
    }

    def __init__(
        self,
        timeout_seconds: float = 8.0,
        max_retries: int = 2,
        backoff_seconds: float = 0.4,
    ) -> None:
        super().__init__(
            agent_slug="maya",
            director_binding="Maya",
            artifact_family="maya-agent-packet",
            timeout_seconds=timeout_seconds,
            max_retries=max_retries,
            backoff_seconds=backoff_seconds,
        )

    def get_palette(self, palette_id: str) -> dict:
        palette = self.PALETTES.get(palette_id)
        if not palette:
            return {
                "palette_id": palette_id,
                "status": "NEEDS_CONFIRMATION",
                "reason": "Unknown Maya palette id. Use one of: yash_story_arc, yash_presenter, yash_notebooklm."
            }
        return {"status": "PASS", **palette}


if __name__ == "__main__":
    print_run(MayaAgent())


# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: maya_agent
# component_layer: AGENT
# component_name: Maya Agent
# director_binding: Maya (DIR-PRODv1-003) — Visual Production + Creative Visualization + Visual Effects + Color Grading + Storyboard
# class_family: named_director
# runtime_base: ProductionAgentBase
# route_families: [media_factory_handoff, avatar_video_context, context_engineering]
# activation_triggers: route_family in [media_factory_handoff, avatar_video_context] or explicit registry selection; activated when storyboard, scene prompt, color grading, visual plan, or local engine handoff tasks are routed.
# upstream_inputs: [scene_brief_packet, script_segment_packet, director_intent_packet]
# downstream_outputs: [scene_prompt_packet, visual_design_brief_packet, color_grading_packet, storyboard_export_packet]
# required_input_packets: [scene_brief_packet, script_segment_packet]
# emitted_output_packets: [scene_prompt_packet, visual_design_brief_packet, color_grading_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_IMAGE]
# quality_gates: [visual_dna_compliance_gate, storyboard_export_gate, color_grading_quality_gate]
# validator_bindings: [visual_dna_fields_complete, scene_sync_matrix_present, provider_boundary_present, media_factory_sync_lock_status]
# fallback_behavior: NEEDS_CONFIRMATION if visual DNA fields are incomplete or scene_brief_packet is missing.
# lineage_fields: [scene_id, visual_dna_version, color_palette_id, storyboard_frame_ref, instance_id]
# provider_boundary: provider_execution_allowed=false; local engine execution allowed only after explicit approval_packet; provider/media/n8n execution disabled by default
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof. All 15 visual DNA fields must be present for PASS.
# human_approval_points: [approve_visual_plan, approve_storyboard_export, approve_color_grade, approve_local_engine_execution]
# failure_modes: missing_scene_brief_packet, missing_visual_dna_field, missing_scene_sync_matrix, provider_boundary_violation, incomplete_storyboard_export.
# handoff_targets: [scene_prompt_packet, visual_design_brief_packet, color_grading_packet, storyboard_export_packet, PTR_DIRECTOR_AGENT, PTR_FINAL_SCRIPT_IMAGE, PTR_AGENT_SUBAGENT]
# production_score_fields: [visual_dna_compliance_score, storyboard_completeness_score, color_palette_consistency_score]
# workflow_ownership: Owns the visual production stage — from scene_brief_packet consumption to scene_prompt_packet and storyboard_export_packet emission.
# input_packet_consumption_rules: Must read and cite scene_brief_packet and script_segment_packet before visual stage execution.
# output_packet_emission_rules: Must emit scene_prompt_packet with all 15 visual DNA fields and SCENE_SYNC_MATRIX row.
# cross_agent_handoff_rules: Must hand off only through communication pointer registry packets.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: media_factory_visual_production_profile
# route_family_resolved: [media_factory_handoff, avatar_video_context]
# activation_triggers_resolved: [storyboard request, scene prompt task, color grading task, visual plan request, local engine handoff]
# required_input_packets_resolved: [scene_brief_packet, script_segment_packet, director_intent_packet]
# emitted_output_packets_resolved: [scene_prompt_packet, visual_design_brief_packet, color_grading_packet, storyboard_export_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_FINAL_SCRIPT_IMAGE]
# validator_bindings_resolved: [visual_dna_fields_complete, scene_sync_matrix_present, provider_boundary_present, media_factory_sync_lock_status]
# quality_gates_resolved: [visual_dna_compliance_gate, storyboard_export_gate, color_grading_quality_gate, provider_honesty_gate]
# fallback_behavior_resolved: NEEDS_CONFIRMATION if visual DNA fields incomplete or scene_brief_packet missing.
# lineage_fields_resolved: [scene_id, visual_dna_version, color_palette_id, storyboard_frame_ref, instance_id]
# provider_boundary_resolved: provider_execution_allowed=false; local engine allowed after approval_packet; provider/media/n8n disabled by default
# handoff_targets_resolved: [scene_prompt_packet, visual_design_brief_packet, color_grading_packet, storyboard_export_packet, PTR_DIRECTOR_AGENT, PTR_FINAL_SCRIPT_IMAGE]
# production_score_fields_resolved: [visual_dna_compliance_score, storyboard_completeness_score, color_palette_consistency_score]
# human_approval_points_resolved: [approve_visual_plan, approve_storyboard_export, approve_color_grade, approve_local_engine_execution]
# status_limits_resolved: [no fake realtime claim, no provider execution, all 15 visual DNA fields required for PASS]
# evidence_used_for_resolution: path/pre-contract keyword: visual/cinematic/storyboard/color; component_path=agents/maya/maya_agent.py; component_id=maya_agent; director_file=directors/production/maya.md
# remaining_unknowns: none

# PHASE 13E_6 NAMED AGENT 24-CRAFT CINEMA ALIGNMENT
# phase_13e_6_status: NAMED_AGENT_24_CRAFT_CINEMA_ALIGNMENT
# runtime_behavior_changed: false
# selector_modified: false
# active_route_registry_modified: false
# runtime_proof_claimed: false
# pass_claimed: false
# script_generation_preserved: true
# film_screenplay_generation_preserved: true
# cinema_craft_authority: 11 production_design_and_worldbuilding; 16 animation_and_style_system; 09 cinematography_and_visual_grammar
# mythology_fidelity_lock: illusion, appearance, perception, designed reality, and visual world construction
# cinema_department_execution_role: Execute film-world texture, production design, visual perception, and animation style continuity.
# downstream_boundary: Media Factory visuals are downstream execution and do not replace preproduction worldbuilding.
# content_platform_drift_not_marked_as_film_core_authority: true

