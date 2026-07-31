from __future__ import annotations

from typing import Any

DIRECTOR_AUTHORITY_PROFILES: dict[str, dict[str, Any]] = {
    'agastya': {
        'director_name': 'Agastya',
        'director_id': 'DIR-RSRCHv1-003',
        'council': 'Research',
        'role': 'Deep Analysis | Insight Extraction',
        'skill_bindings': 7,
        'release_blocking': False,
        'authority_mode': 'analysis',
        'can_veto': False,
        'escalation_workflow': 'WF-600',
    },
    'agni': {
        'director_name': 'Agni',
        'director_id': 'DIR-PRODv1-005',
        'council': 'Production',
        'role': 'Energy/Momentum | Urgency Injection',
        'skill_bindings': 6,
        'release_blocking': False,
        'authority_mode': 'general',
        'can_veto': False,
        'escalation_workflow': 'WF-900',
    },
    'arjuna': {
        'director_name': 'Arjuna',
        'director_id': 'DIR-PRODv1-002',
        'council': 'Production',
        'role': 'Script Execution | Narrative Warfare',
        'skill_bindings': 8,
        'release_blocking': True,
        'authority_mode': 'general',
        'can_veto': False,
        'escalation_workflow': 'WF-900',
    },
    'aruna': {
        'director_name': 'Aruna',
        'director_id': 'KERNEL-FLOW-001',
        'council': 'Distribution & Evolution (Kernel Spine)',
        'role': 'Flow Building | Resource Gating | Neural Routing',
        'skill_bindings': 5,
        'release_blocking': True,
        'authority_mode': 'kernel_governance',
        'can_veto': True,
        'escalation_workflow': 'WF-020',
    },
    'brahma': {
        'director_name': 'Brahma',
        'director_id': 'DIR-ORCHv1-004',
        'council': 'Supreme Vision',
        'role': 'Governance Keeper | Councils Coordinator',
        'skill_bindings': 18,
        'release_blocking': True,
        'authority_mode': 'governance',
        'can_veto': True,
        'escalation_workflow': 'WF-900',
    },
    'chanakya': {
        'director_name': 'Chanakya',
        'director_id': 'DIR-STRTv1-001',
        'council': 'Strategy',
        'role': 'Strategic Filtering | Opportunity Selection',
        'skill_bindings': 4,
        'release_blocking': True,
        'authority_mode': 'general',
        'can_veto': False,
        'escalation_workflow': 'WF-900',
    },
    'chandra': {
        'director_name': 'Chandra',
        'director_id': 'DIR-ANLYv1-001',
        'council': 'Analytics',
        'role': 'Audience Intelligence | Analytics Orchestration',
        'skill_bindings': 3,
        'release_blocking': True,
        'authority_mode': 'analysis',
        'can_veto': True,
        'escalation_workflow': 'WF-600',
    },
    'chitragupta': {
        'director_name': 'Chitragupta',
        'director_id': 'DIR-AUDTv1-001',
        'council': 'Analytics',
        'role': 'Audit Trail | Lineage Tracking | Data Integrity',
        'skill_bindings': 4,
        'release_blocking': True,
        'authority_mode': 'governance',
        'can_veto': True,
        'escalation_workflow': 'WF-900',
    },
    'durga': {
        'director_name': 'Durga',
        'director_id': 'DIR-STRTv1-004',
        'council': 'Strategy',
        'role': 'Protection | Veto Logic | Safety Enforcement',
        'skill_bindings': 5,
        'release_blocking': False,
        'authority_mode': 'safety_veto',
        'can_veto': True,
        'escalation_workflow': 'WF-900',
    },
    'ganesha': {
        'director_name': 'Ganesha',
        'director_id': 'DIR-RSRCHv1-005',
        'council': 'Research',
        'role': 'Neural Index Router | Routing Intelligence',
        'skill_bindings': 8,
        'release_blocking': True,
        'authority_mode': 'routing_gate',
        'can_veto': False,
        'escalation_workflow': 'WF-900',
    },
    'garuda': {
        'director_name': 'Garuda',
        'director_id': 'DIR-CINv1-003',
        'council': 'Cinematic',
        'role': 'Distribution Velocity | Rapid Publishing',
        'skill_bindings': 7,
        'release_blocking': False,
        'authority_mode': 'distribution',
        'can_veto': False,
        'escalation_workflow': 'WF-500',
    },
    'hanuman': {
        'director_name': 'Hanuman',
        'director_id': 'DIR-CINv1-001',
        'council': 'Cinematic',
        'role': 'Speed | Fast-Track Execution',
        'skill_bindings': 6,
        'release_blocking': False,
        'authority_mode': 'general',
        'can_veto': False,
        'escalation_workflow': 'WF-900',
    },
    'indra': {
        'director_name': 'Indra',
        'director_id': 'DIR-CINv1-005',
        'council': 'Cinematic',
        'role': 'Premium Tier | High-Value Production',
        'skill_bindings': 7,
        'release_blocking': False,
        'authority_mode': 'production',
        'can_veto': False,
        'escalation_workflow': 'WF-400',
    },
    'kali': {
        'director_name': 'Kali',
        'director_id': 'DIR-CINv1-006',
        'council': 'Cinematic',
        'role': 'Revision Rupture | Moral Conflict | Decisive Cut',
        'skill_bindings': 0,
        'release_blocking': False,
        'authority_mode': 'general',
        'can_veto': False,
        'escalation_workflow': 'WF-900',
    },
    'kama': {
        'director_name': 'Kama',
        'director_id': 'DIR-DISTv1-001',
        'council': 'Distribution & Evolution',
        'role': 'Engagement | Conversion | Audience Attraction',
        'skill_bindings': 10,
        'release_blocking': True,
        'authority_mode': 'distribution',
        'can_veto': False,
        'escalation_workflow': 'WF-500',
    },
    'krishna': {
        'director_name': 'Krishna',
        'director_id': 'DIR-ORCHv1-001',
        'council': 'Supreme Vision',
        'role': 'Orchestrator | Decision Arbiter | Multi-Domain Controller',
        'skill_bindings': 29,
        'release_blocking': True,
        'authority_mode': 'orchestrator',
        'can_veto': True,
        'escalation_workflow': 'WF-010',
    },
    'kubera': {
        'director_name': 'Kubera',
        'director_id': 'KERNEL-COST-001',
        'council': 'Distribution & Evolution (Kernel Spine)',
        'role': 'Cost/Budget Authority | Financial Gate',
        'skill_bindings': 5,
        'release_blocking': True,
        'authority_mode': 'cost_gate',
        'can_veto': False,
        'escalation_workflow': 'WF-020',
    },
    'maya': {
        'director_name': 'Maya',
        'director_id': 'DIR-PRODv1-003',
        'council': 'Production',
        'role': 'Visual Production | Creative Visualization',
        'skill_bindings': 9,
        'release_blocking': True,
        'authority_mode': 'production',
        'can_veto': False,
        'escalation_workflow': 'WF-400',
    },
    'narada': {
        'director_name': 'Narada',
        'director_id': 'DIR-STRTv1-002',
        'council': 'Strategy',
        'role': 'Operations | Distribution | Optimization',
        'skill_bindings': 18,
        'release_blocking': True,
        'authority_mode': 'distribution',
        'can_veto': False,
        'escalation_workflow': 'WF-500',
    },
    'nataraja': {
        'director_name': 'Nataraja',
        'director_id': 'DIR-CINv1-002',
        'council': 'Cinematic',
        'role': 'Pacing | Editing | Flow Control',
        'skill_bindings': 9,
        'release_blocking': True,
        'authority_mode': 'production',
        'can_veto': False,
        'escalation_workflow': 'WF-400',
    },
    'parashara': {
        'director_name': 'Parashara',
        'director_id': 'DIR-RSRCHv1-004',
        'council': 'Research',
        'role': 'Trend Analysis | Pattern Discovery',
        'skill_bindings': 6,
        'release_blocking': True,
        'authority_mode': 'analysis',
        'can_veto': False,
        'escalation_workflow': 'WF-600',
    },
    'ravana': {
        'director_name': 'Ravana',
        'director_id': 'DIR-STRTv1-003',
        'council': 'Strategy',
        'role': 'Alternative Strategy | Conflict Manager',
        'skill_bindings': 6,
        'release_blocking': False,
        'authority_mode': 'general',
        'can_veto': False,
        'escalation_workflow': 'WF-900',
    },
    'saraswati': {
        'director_name': 'Saraswati',
        'director_id': 'DIR-DISTv1-002',
        'council': 'Distribution & Evolution',
        'role': 'Knowledge Dissemination | Content Multiplication',
        'skill_bindings': 9,
        'release_blocking': True,
        'authority_mode': 'analysis',
        'can_veto': False,
        'escalation_workflow': 'WF-600',
    },
    'shakti': {
        'director_name': 'Shakti',
        'director_id': 'DIR-ORCHv1-005',
        'council': 'Supreme Vision',
        'role': 'Creative Force Amplifier | Distribution Velocity',
        'skill_bindings': 7,
        'release_blocking': False,
        'authority_mode': 'distribution',
        'can_veto': False,
        'escalation_workflow': 'WF-500',
    },
    'shiva': {
        'director_name': 'Shiva',
        'director_id': 'DIR-ORCHv1-003',
        'council': 'Supreme Vision',
        'role': 'Autonomous Intelligence Loop | Creative Destruction',
        'skill_bindings': 9,
        'release_blocking': True,
        'authority_mode': 'general',
        'can_veto': False,
        'escalation_workflow': 'WF-900',
    },
    'tumburu': {
        'director_name': 'Tumburu',
        'director_id': 'DIR-PRODv1-001',
        'council': 'Production',
        'role': 'Audio Production | Voice Direction',
        'skill_bindings': 10,
        'release_blocking': True,
        'authority_mode': 'production',
        'can_veto': False,
        'escalation_workflow': 'WF-400',
    },
    'valmiki': {
        'director_name': 'Valmiki',
        'director_id': 'DIR-RSRCHv1-001',
        'council': 'Research',
        'role': 'Research Synthesis | Knowledge Structuring',
        'skill_bindings': 8,
        'release_blocking': True,
        'authority_mode': 'analysis',
        'can_veto': False,
        'escalation_workflow': 'WF-600',
    },
    'varuna': {
        'director_name': 'Varuna',
        'director_id': 'DIR-CINv1-004',
        'council': 'Cinematic',
        'role': 'Flow | Liquid Narrative | Adaptability',
        'skill_bindings': 8,
        'release_blocking': False,
        'authority_mode': 'general',
        'can_veto': False,
        'escalation_workflow': 'WF-900',
    },
    'vishnu': {
        'director_name': 'Vishnu',
        'director_id': 'DIR-ORCHv1-002',
        'council': 'Supreme Vision',
        'role': 'HA Coordinator | Failover Master',
        'skill_bindings': 12,
        'release_blocking': True,
        'authority_mode': 'failover',
        'can_veto': False,
        'escalation_workflow': 'WF-900',
    },
    'vishwakarma': {
        'director_name': 'Vishwakarma',
        'director_id': 'DIR-PRODv1-004',
        'council': 'Production',
        'role': 'Architecture | Technical Production',
        'skill_bindings': 7,
        'release_blocking': True,
        'authority_mode': 'production',
        'can_veto': False,
        'escalation_workflow': 'WF-400',
    },
    'vyasa': {
        'director_name': 'Vyasa',
        'director_id': 'DIR-RSRCHv1-002',
        'council': 'Research',
        'role': 'Content Creation | Knowledge Graph Management',
        'skill_bindings': 12,
        'release_blocking': True,
        'authority_mode': 'analysis',
        'can_veto': False,
        'escalation_workflow': 'WF-600',
    },
    'yama': {
        'director_name': 'Yama',
        'director_id': 'KERNEL-POLICY-001',
        'council': 'Distribution & Evolution (Kernel Spine)',
        'role': 'Policy/Legality Gate | Governance Enforcement',
        'skill_bindings': 5,
        'release_blocking': True,
        'authority_mode': 'policy_gate',
        'can_veto': True,
        'escalation_workflow': 'WF-020',
    },
    'yudhishthira': {
        'director_name': 'Yudhishthira',
        'director_id': 'DIR-STRTv1-005',
        'council': 'Strategy',
        'role': 'Dharma/Governance Validation',
        'skill_bindings': 4,
        'release_blocking': False,
        'authority_mode': 'governance',
        'can_veto': True,
        'escalation_workflow': 'WF-900',
    },
}

PHASE_13E_8_NAMED_AGENT_CINEMA_PROFILE_OVERLAY: dict[str, dict[str, Any]] = {
    'agni': {
        'cinema_craft_authority': ['10 lighting_and_mood', '14 sound_design_and_atmosphere', '22 post_production_and_finishing'],
        'cinema_department_execution_role': 'Light, sound atmosphere, purification, intensity, and finishing transformation.',
        'mythology_fidelity_lock': 'Agni works through ignition, transformation, purification, and finishing heat.',
        'downstream_boundary': 'Platform urgency, viral energy, and recurring re-hook pressure remain SCRIPT_GENERATION support only.',
    },
    'arjuna': {
        'cinema_craft_authority': ['09 shot_design', '11 blocking_and_staging', '20 storyboard_and_shotlist'],
        'cinema_department_execution_role': 'Precision targeting for shots, blocking, staging, and craft-under-pressure decisions.',
        'mythology_fidelity_lock': 'Arjuna works through disciplined focus, aim, shot selection, and ethical pressure.',
        'downstream_boundary': 'Tactical content optimization cannot override screenplay or shot truth.',
    },
    'aruna': {
        'cinema_craft_authority': ['03 act_and_sequence_design', '13 editing_rhythm', '21 production_flow'],
        'cinema_department_execution_role': 'Awakening, transition, scene flow, and editorial momentum.',
        'mythology_fidelity_lock': 'Aruna works as dawn, threshold, transition, and charioteer of forward motion.',
        'downstream_boundary': 'Kernel routing remains separate from film-core screenplay criteria.',
    },
    'brahma': {
        'cinema_craft_authority': ['01 story_world', '12 production_design', '18 animation_world_logic'],
        'cinema_department_execution_role': 'World creation, production design, and animation architecture.',
        'mythology_fidelity_lock': 'Brahma works through creation, ordering, world origination, and structural genesis.',
        'downstream_boundary': 'Governance coordination does not replace cinematic world-building evidence.',
    },
    'durga': {
        'cinema_craft_authority': ['07 dramatic_conflict_and_stakes', '17 docudrama_ethics', '23 safety_and_ethics'],
        'cinema_department_execution_role': 'Protective conflict pressure, ethical stakes, and harm-prevention review.',
        'mythology_fidelity_lock': 'Durga works through protection, force, confrontation, and defense of the vulnerable.',
        'downstream_boundary': 'Safety gates do not authorize fake PASS or runtime proof.',
    },
    'ganesha': {
        'cinema_craft_authority': ['00 preflight_and_gatekeeping', '16 source_vs_render_separation', '23 safety_and_ethics'],
        'cinema_department_execution_role': 'Obstacle removal, preflight checks, source separation, and no-fake-PASS support.',
        'mythology_fidelity_lock': 'Ganesha works through beginnings, gatekeeping, obstacle removal, and clear entry paths.',
        'downstream_boundary': 'Routing intelligence cannot silently bind routes or selectors.',
    },
    'garuda': {
        'cinema_craft_authority': ['09 shot_design', '19 visual_motif_system', '20 storyboard_and_shotlist'],
        'cinema_department_execution_role': 'Aerial vision, scout intelligence, macro-to-micro shot grammar, and handoff speed.',
        'mythology_fidelity_lock': 'Garuda works through swift aerial vision, signal intelligence, obstacle detection, and handoff.',
        'downstream_boundary': 'Distribution velocity and rapid publishing are not film-core authority.',
    },
    'hanuman': {
        'cinema_craft_authority': ['06 character_arc_and_performance', '15 continuity_supervision', '21 production_flow'],
        'cinema_department_execution_role': 'Continuity rescue, emotional courage, repair, and impossible-task execution.',
        'mythology_fidelity_lock': 'Hanuman works through devotion, humility, strength, rescue, repair, and courageous continuity.',
        'downstream_boundary': 'Fast-track execution cannot compress screenplay craft gates.',
    },
    'indra': {
        'cinema_craft_authority': ['07 dramatic_conflict_and_stakes', '21 production_flow', '24 command_and_escalation'],
        'cinema_department_execution_role': 'Production command, storm pressure, escalation, and strategic deployment.',
        'mythology_fidelity_lock': 'Indra works through command, storm authority, war-room decision, and escalation.',
        'downstream_boundary': 'Premium production labels cannot stand in for cinematic command evidence.',
    },
    'kali': {
        'cinema_craft_authority': ['07 dramatic_conflict_and_stakes', '13 editing_rhythm', '22 post_production_and_finishing'],
        'cinema_department_execution_role': 'Decisive revision, moral rupture, conflict pressure, and severance of false material.',
        'mythology_fidelity_lock': 'Kali works through rupture, moral cleansing, fearless confrontation, and decisive cut.',
        'downstream_boundary': 'Shock value, outrage, thumbnail provocation, and platform conflict are not film-core authority.',
    },
    'kama': {
        'cinema_craft_authority': ['04 desire_line', '06 character_arc_and_performance', '05 dialogue_and_language'],
        'cinema_department_execution_role': 'Desire, attraction, relational pull, and character want without conversion drift.',
        'mythology_fidelity_lock': 'Kama works through desire, longing, emotional magnetism, and relational pull.',
        'downstream_boundary': 'Engagement, conversion, and audience attraction remain downstream/content concerns.',
    },
    'krishna': {
        'cinema_craft_authority': ['05 dialogue_and_language', '06 character_arc_and_performance', '08 directorial_vision'],
        'cinema_department_execution_role': 'Directorial counsel, character motivation, dharma complexity, and subtext.',
        'mythology_fidelity_lock': 'Krishna works through strategy, counsel, dharma complexity, emotional intelligence, and subtext.',
        'downstream_boundary': 'Multi-agent orchestration cannot override cinema character truth.',
    },
    'maya': {
        'cinema_craft_authority': ['12 production_design', '18 animation_world_logic', '19 visual_motif_system'],
        'cinema_department_execution_role': 'Perception, illusion, world texture, visual design, and animation style logic.',
        'mythology_fidelity_lock': 'Maya works through illusion, perception, world texture, and visual manifestation.',
        'downstream_boundary': 'Media generation and avatar routes remain downstream of film preproduction authority.',
    },
    'narada': {
        'cinema_craft_authority': ['02 theme_and_message', '16 source_vs_render_separation', '21 production_flow'],
        'cinema_department_execution_role': 'Truth signal, message flow, source handoff, and downstream distribution separation.',
        'mythology_fidelity_lock': 'Narada works through message carrying, signal movement, provocation, and truth transmission.',
        'downstream_boundary': 'Distribution optimization cannot become film-core screenplay routing authority.',
    },
    'nataraja': {
        'cinema_craft_authority': ['11 blocking_and_staging', '13 editing_rhythm', '18 animation_world_logic'],
        'cinema_department_execution_role': 'Rhythm, motion, choreography, movement, and edit cadence.',
        'mythology_fidelity_lock': 'Nataraja works through cosmic dance, transformation, rhythm, and choreographed motion.',
        'downstream_boundary': 'Pacing for retention is separate from cinematic rhythm and movement.',
    },
    'parashara': {
        'cinema_craft_authority': ['16 source_vs_render_separation', '17 docudrama_ethics', '02 theme_and_message'],
        'cinema_department_execution_role': 'World-truth research, foresight, pattern reading, and source-aware film grounding.',
        'mythology_fidelity_lock': 'Parashara works through foresight, lineage insight, pattern reading, and hidden causes.',
        'downstream_boundary': 'Trend discovery cannot replace source-led docudrama truth.',
    },
    'saraswati': {
        'cinema_craft_authority': ['05 dialogue_and_language', '14 sound_design_and_atmosphere', '06 character_arc_and_performance'],
        'cinema_department_execution_role': 'Dialogue, music motif, actor voice, language clarity, and prosody.',
        'mythology_fidelity_lock': 'Saraswati works through language, learning, music, voice, and articulation.',
        'downstream_boundary': 'Content multiplication is not film-core dialogue craft.',
    },
    'shakti': {
        'cinema_craft_authority': ['07 dramatic_conflict_and_stakes', '22 post_production_and_finishing', '24 command_and_escalation'],
        'cinema_department_execution_role': 'Creative force, protective intensity, activation, and finishing power.',
        'mythology_fidelity_lock': 'Shakti works through force, creative power, protection, and activation.',
        'downstream_boundary': 'Distribution velocity remains downstream of film craft.',
    },
    'shiva': {
        'cinema_craft_authority': ['13 editing_rhythm', '22 post_production_and_finishing', '08 directorial_vision'],
        'cinema_department_execution_role': 'Revision, destructive reset, transformation, edit rhythm, and finishing judgment.',
        'mythology_fidelity_lock': 'Shiva works through destruction, transformation, stillness, and renewal.',
        'downstream_boundary': 'Autonomous loops do not claim governed runtime proof.',
    },
    'valmiki': {
        'cinema_craft_authority': ['01 story_world', '02 theme_and_message', '03 act_and_sequence_design'],
        'cinema_department_execution_role': 'Story origin, poetic foundation, scene genesis, and narrative root.',
        'mythology_fidelity_lock': 'Valmiki works through origin story, poetry, witness, and epic narration.',
        'downstream_boundary': 'Research synthesis cannot replace screenplay genesis.',
    },
    'varuna': {
        'cinema_craft_authority': ['10 lighting_and_mood', '14 sound_design_and_atmosphere', '19 visual_motif_system'],
        'cinema_department_execution_role': 'Atmosphere, hidden truth, water mood, lighting weather, and sound depth.',
        'mythology_fidelity_lock': 'Varuna works through depth, water, atmosphere, hidden truth, and emotional weather.',
        'downstream_boundary': 'Liquid narrative flexibility cannot bypass source or continuity gates.',
    },
    'vishnu': {
        'cinema_craft_authority': ['15 continuity_supervision', '03 act_and_sequence_design', '21 production_flow'],
        'cinema_department_execution_role': 'Continuity preservation, balance, supervision, and structural protection.',
        'mythology_fidelity_lock': 'Vishnu works through preservation, balance, continuity, and restoration.',
        'downstream_boundary': 'HA/failover runtime authority remains separate from screenplay continuity authority.',
    },
    'vyasa': {
        'cinema_craft_authority': ['01 story_world', '03 act_and_sequence_design', '15 continuity_supervision'],
        'cinema_department_execution_role': 'Story canon, screenplay structure, sequence architecture, and narrative continuity.',
        'mythology_fidelity_lock': 'Vyasa works through epic authorship, canon, narration, and structural continuity.',
        'downstream_boundary': 'Content creation and knowledge graph work cannot replace film story canon.',
    },
    'yama': {
        'cinema_craft_authority': ['16 source_vs_render_separation', '17 docudrama_ethics', '23 safety_and_ethics'],
        'cinema_department_execution_role': 'Ethics, source-vs-render law, truth boundary, and no-fake-PASS governance.',
        'mythology_fidelity_lock': 'Yama works through law, consequence, moral boundary, death truth, and final judgment.',
        'downstream_boundary': 'Policy gates cannot invent PASS or governed runtime proof.',
    },
}


def get_director_profile(director_name: str) -> dict[str, Any]:
    slug = director_name.lower()
    return DIRECTOR_AUTHORITY_PROFILES.get(
        slug,
        {
            "director_name": director_name,
            "director_id": "UNKNOWN",
            "council": "Unknown",
            "role": "Generic Director",
            "skill_bindings": 0,
            "release_blocking": False,
            "authority_mode": "general",
            "can_veto": False,
            "escalation_workflow": "WF-900",
        },
    )


# MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
# Append-only MAC-06.2B contract metadata.
# component_id: director_authority_profiles
# component_layer: AGENT
# component_name: Director Authority Profiles
# route_families: [lineage_summary, approval_gate]
# activation_triggers: route_family in [script_generation, trend_research, voice_context, music_sfx_context] or explicit registry selection; mark script_generation_profile only when route_family is unknown.
# upstream_inputs: [media_quality_gate_packet, lineage_packet, approval_packet]
# downstream_outputs: [lineage_packet, approval_packet]
# required_input_packets: [media_quality_gate_packet, lineage_packet, approval_packet]
# emitted_output_packets: [lineage_packet, approval_packet]
# communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE, PTR_LINEAGE_APPROVAL]
# quality_gates: [lineage_completeness_gate, decision_trace_gate, approval_options_gate]
# validator_bindings: [lineage_approval_packet_present, segment_level_regeneration_actions_present, quality_scores_present]
# fallback_behavior: NEEDS_HUMAN_REVIEW if upstream packet IDs or approval choices are missing.
# lineage_fields: [upstream_packet_ids, downstream_packet_ids, decision_log, evidence_paths]
# provider_boundary: provider_execution_allowed=false; approval may authorize future execution; default is no provider/media/n8n execution
# status_limits: May not claim production-ready, onboarded, provider-called, media-created, or n8n-executed without external proof.
# human_approval_points: [approve, revise_segment, regenerate_media, reject]
# failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer, low_quality_score, provider_boundary_violation.
# handoff_targets: [lineage_packet, approval_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE, PTR_LINEAGE_APPROVAL]
# production_score_fields: [lineage_score, approval_clarity_score, risk_score]
# workflow_ownership: Owns one workflow stage from input packet consumption to output packet emission.
# input_packet_consumption_rules: Must read and cite required upstream packet before stage execution.
# output_packet_emission_rules: Must emit structured downstream packet with lineage and quality score.
# cross_agent_handoff_rules: Must hand off only through communication pointer registry packets.
#
# MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
# component_depth_status: PRODUCTION_DEPTH_ENRICHED
# route_profile_applied: lineage_profile
# route_family_resolved: [lineage_summary, approval_gate]
# activation_triggers_resolved: [lineage, trace, decision log]
# required_input_packets_resolved: [media_quality_gate_packet, lineage_packet, approval_packet]
# emitted_output_packets_resolved: [lineage_packet, approval_packet]
# communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE, PTR_LINEAGE_APPROVAL]
# validator_bindings_resolved: [lineage_approval_packet_present, segment_level_regeneration_actions_present, quality_scores_present]
# quality_gates_resolved: [lineage_completeness_gate, decision_trace_gate, approval_options_gate]
# fallback_behavior_resolved: NEEDS_HUMAN_REVIEW if upstream packet IDs or approval choices are missing.
# lineage_fields_resolved: [upstream_packet_ids, downstream_packet_ids, decision_log, evidence_paths]
# provider_boundary_resolved: provider_execution_allowed=false; approval may authorize future execution; default is no provider/media/n8n execution; approval_packet_required_for_any_execution
# handoff_targets_resolved: [lineage_packet, approval_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL, PTR_QUALITY_LINEAGE, PTR_LINEAGE_APPROVAL]
# production_score_fields_resolved: [lineage_score, approval_clarity_score, risk_score]
# human_approval_points_resolved: [approve, revise_segment, regenerate_media, reject]
# status_limits_resolved: [no silent approval, no execution without explicit approval]
# evidence_used_for_resolution: path/pre-contract keyword: lineage/trace; component_path=agents/common/director_authority_profiles.py; component_id=director_authority_profiles
# remaining_unknowns: none
