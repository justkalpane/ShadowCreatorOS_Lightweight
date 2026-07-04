# VIDEO_CONTEXT_PACKET Contract

packet_id: VIDEO_CONTEXT_PACKET
producer_component: video_context_agent
consumer_component: video_provider_handoff_or_editing_agent
required_fields:
  - scene_id
  - duration
  - motion
  - camera_movement
  - transition
  - sync_point
  - caption_moment
  - continuity_notes
  - provider_constraints
  - camera_movement_type
  - lens_focal_logic
  - frame_rate
  - aspect_ratio
  - motion_intensity
  - subject_action
  - background_motion
  - animation_style_classification
  - cinematic_delivery_standard
  - local_tool_targets
  - controlnet_guidance_types
optional_fields:
  - provider_notes
  - user_review_notes
  - version
  - ip_adapter_reference_path
  - reference_image_for_controlnet
  - color_grade_lut_ref
  - storyboard_image_ref
camera_movement_vocabulary:
  - static
  - pan_left
  - pan_right
  - tilt_up
  - tilt_down
  - dolly_in
  - dolly_out
  - crane_up
  - crane_down
  - handheld
  - orbit_left
  - orbit_right
  - zoom_in
  - zoom_out
  - pull_back
  - push_in
  - whip_pan
  - dutch_tilt
animation_style_classes:
  - cinematic_realism
  - stylized_animation
  - graphic_novel
  - anime_inspired
  - 3d_render
  - photorealistic
  - illustration
  - mixed_media
local_tool_targets_allowed:
  - AnimateDiff
  - Wan
  - LTX
  - CogVideoX
  - ComfyUI_SVD
  - ffmpeg_assembly
  - local_video_model
controlnet_guidance_types_allowed:
  - Canny
  - OpenPose
  - Depth
  - Lineart
  - SoftEdge
  - IP-Adapter
  - None
validation_rules:
  - all required_fields must be present before downstream stage runs
  - packet must include lineage_fields and quality_metrics
  - provider_execution_allowed=false unless explicitly approved
  - cinematic_delivery_standard must be declared (default Rec.709)
  - camera_movement_type must use approved vocabulary
  - animation_style_classification must use approved class names
  - local_tool_targets must list at least one engine when local execution is planned
  - controlnet_guidance_types must be declared (use None if not applicable)
  - frame_rate must be numeric (common values: 24 | 25 | 30 | 60)
  - aspect_ratio must be declared (common values: 16:9 | 9:16 | 1:1 | 4:3)
quality_metrics:
  - completeness_score
  - sync_score
  - consistency_score
  - risk_score
  - camera_motion_clarity_score
  - tool_translation_readiness_score
fallback_behavior: BLOCKED_BEFORE_OUTPUT or NEEDS_HUMAN_REVIEW when required fields are missing
lineage_fields:
  - upstream_packet_id
  - downstream_packet_id
  - source_component_id
  - evidence_path
  - beat_map_scene_id
  - storyboard_image_ref
  - prompt_packet_schema_version
approval_required: true when provider execution, media creation, repo write, or segment regeneration is requested
provider_execution_allowed: false
