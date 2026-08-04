# EDITING_TIMELINE_PACKET Contract

packet_id: EDITING_TIMELINE_PACKET
producer_component: editing_agent
consumer_component: quality_gate_or_assembly_handoff
required_fields:
- timeline_segments
- cut_points
- transitions
- caption_style
- audio_video_sync
- broll_or_generated_scene_map
- platform_aspect_ratio
- thumbnail_moment
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
