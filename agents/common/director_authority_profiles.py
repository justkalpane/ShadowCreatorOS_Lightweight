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
