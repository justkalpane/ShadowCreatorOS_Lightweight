# VISUAL_CONTEXT_PACKET Contract

packet_id: VISUAL_CONTEXT_PACKET
producer_component: visual_context_agent
consumer_component: image_or_video_provider_handoff
required_fields:
- style_bible
- scene_prompts
- subject_consistency
- composition
- lighting
- color_palette
- negative_prompts
- aspect_ratio
- brand_rules
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
