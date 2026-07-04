# SCRIPT_SEGMENT_PACKET Contract

packet_id: SCRIPT_SEGMENT_PACKET
producer_component: script_agent_or_refinement_agent
consumer_component: voice_context_agent, visual_context_agent, video_context_agent, editing_agent
required_fields:
- segment_id
- start_time
- end_time
- narration_text
- visual_intent
- emotion
- retention_purpose
- CTA_role
- evidence_reference
- downstream_voice_required
- downstream_visual_required
- downstream_video_required
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
