# MEDIA_QUALITY_GATE_PACKET Contract

packet_id: MEDIA_QUALITY_GATE_PACKET
producer_component: quality_agent
consumer_component: lineage_agent_or_approval_gate
required_fields:
- script_score
- hook_score
- retention_score
- voice_score
- visual_score
- video_score
- audio_score
- editing_score
- platform_score
- lineage_score
- final_pass_fail
optional_fields:
- provider_notes
- user_review_notes
- version
validation_rules:
- all required_fields must be present before downstream stage runs
- packet must include lineage_fields and quality_metrics
- provider_execution_allowed=false unless explicitly approved
quality_metrics:
- completeness_score
- sync_score
- consistency_score
- risk_score
fallback_behavior: BLOCKED_BEFORE_OUTPUT or NEEDS_HUMAN_REVIEW when required fields are missing
lineage_fields:
- upstream_packet_id
- downstream_packet_id
- source_component_id
- evidence_path
approval_required: true when provider execution, media creation, repo write, or segment regeneration is requested
provider_execution_allowed: false
