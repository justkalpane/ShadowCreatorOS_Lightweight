"""Local registry of film runtime validators used by the preproduction proof runner."""

from __future__ import annotations


FILM_RUNTIME_VALIDATORS = {
    "route_selection": "validators/film/route/validate_film_route_selection.py",
    "duration": "validators/film/runtime/validate_film_duration.py",
    "character_constraints": "validators/film/runtime/validate_film_character_constraints.py",
    "emotional_beat_map": "validators/film/runtime/validate_film_emotional_beat_map.py",
    "continuity": "validators/film/runtime/validate_film_continuity.py",
    "dialogue_subtext": "validators/film/runtime/validate_film_dialogue_subtext.py",
    "scene_cards": "validators/film/runtime/validate_film_scene_cards.py",
    "premise": "validators/film/runtime/validate_film_premise.py",
    "logline": "validators/film/runtime/validate_film_logline.py",
    "theme_alignment": "validators/film/runtime/validate_film_theme_alignment.py",
    "genre_grammar": "validators/film/runtime/validate_film_genre_grammar.py",
    "act_structure": "validators/film/runtime/validate_film_act_structure.py",
    "sequence_structure": "validators/film/runtime/validate_film_sequence_structure.py",
    "stakes_escalation": "validators/film/runtime/validate_film_stakes_escalation.py",
    "revision_pass": "validators/film/runtime/validate_film_revision_pass.py",
    "character_arc": "validators/film/runtime/validate_film_character_arc.py",
    "relationship_map": "validators/film/runtime/validate_film_relationship_map.py",
    "emotional_continuity": "validators/film/runtime/validate_film_emotional_continuity.py",
    "world_bible": "validators/film/runtime/validate_film_world_bible.py",
    "timeline_continuity": "validators/film/runtime/validate_film_timeline_continuity.py",
    "consequence_logic": "validators/film/runtime/validate_film_consequence_logic.py",
    "director_vision": "validators/film/runtime/validate_film_director_vision.py",
    "visual_language": "validators/film/runtime/validate_film_visual_language.py",
    "cinematography_plan": "validators/film/runtime/validate_film_cinematography_plan.py",
    "department_handoffs": "validators/film/runtime/validate_film_department_handoffs.py",
    "production_risk": "validators/film/runtime/validate_film_production_risk.py",
    "revision_report": "validators/film/runtime/validate_film_revision_report.py",
    "emotional_escalation_depth": "validators/film/cinema_depth/validate_emotional_escalation.py",
    "character_arc_progression_depth": "validators/film/cinema_depth/validate_character_arc_progression.py",
    "scene_logic_depth": "validators/film/cinema_depth/validate_scene_logic_depth.py",
    "dialogue_voice_subtext_depth": "validators/film/cinema_depth/validate_dialogue_voice_subtext.py",
    "genre_differentiation_depth": "validators/film/cinema_depth/validate_genre_differentiation.py",
    "feature_length_density_depth": "validators/film/cinema_depth/validate_feature_length_density.py",
    "continuity_tracking_depth": "validators/film/cinema_depth/validate_continuity_tracking.py",
    "clean_film_script_boundary": "validators/film/runtime/validate_clean_film_script_boundary.py",
    "downstream_boundary": "validators/film/runtime/validate_film_downstream_boundary.py",
    "preproduction_packet": "validators/film/runtime/validate_film_preproduction_packet.py",
    "screenplay_packet": "validators/film/output_packet/validate_film_screenplay_packet.py",
    "no_fake_pass": "validators/film/validation/validate_no_fake_film_pass.py",
}


def validator_paths() -> dict[str, str]:
    return dict(FILM_RUNTIME_VALIDATORS)
