# Platform Content Package Contract

status: ACTIVE_PLANNING_CONTRACT
provider_execution_enabled: false
required_inputs:
- final_script_packet
- script_segment_packet
- editing_timeline_packet
required_outputs:
- platform_content_package_packet
- title_variants
- description_copy
- thumbnail_moment
- caption_style
- CTA_map
validator_bindings:
- editing_timeline_packet_present
- quality_scores_present
human_review_checkpoint: required_before_publish_or_provider_execution
