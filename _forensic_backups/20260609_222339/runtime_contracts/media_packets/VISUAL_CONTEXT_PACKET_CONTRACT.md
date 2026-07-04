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
  - subject
  - environment
  - camera_framing
  - lens_focal_logic
  - lighting_setup
  - emotional_tone
  - cinematic_delivery_standard
  - style_lock
  - movement_intent
  - drift_prevention
  - continuity_constraints
  - brand_persona_consistency
  - safety_real_person_handling
  - tool_targets
  - tool_specific_translation_readiness
optional_fields:
  - provider_notes
  - user_review_notes
  - version
  - ip_adapter_reference_path
  - controlnet_source_image_path
  - color_grade_lut_ref
validation_rules:
  - all required_fields must be present before downstream stage runs
  - packet must include lineage_fields and quality_metrics
  - provider_execution_allowed=false unless explicitly approved
  - cinematic_delivery_standard must be declared (default Rec.709)
  - safety_real_person_handling must be set when any real person is depicted
  - tool_targets must list at least one engine (local or cloud)
  - tool_specific_translation_readiness must be PACKET_READY or higher before engine execution
  - negative_prompts must include at minimum: blurry, watermark, face deformation
visual_dna_compliance:
  subject_required: true
  environment_required: true
  camera_framing_required: true
  lens_focal_logic_required: true
  lighting_setup_required: true
  emotional_tone_required: true
  color_palette_required: true
  cinematic_delivery_standard_default: Rec.709
  style_lock_required: true
  movement_intent_required: true
  negative_prompt_required: true
  drift_prevention_required: true
  continuity_constraints_required: true
  brand_persona_consistency_required: true
  safety_real_person_handling_required: true
  tool_specific_translation_readiness_required: true
tool_translation_targets:
  - comfyui_sdxl: requires style_lock, negative_prompt, lighting_setup, color_palette, camera_framing
  - animatediff: requires movement_intent, motion_intensity (if video)
  - flux_style: requires subject, environment, emotional_tone, style_lock, negative_prompt
  - ip_adapter: requires drift_prevention reference path
  - controlnet: requires controlnet_source_image_path
  - davinci_resolve: requires color_palette, cinematic_delivery_standard
quality_metrics:
  - completeness_score
  - sync_score
  - consistency_score
  - risk_score
  - visual_dna_compliance_score
  - tool_translation_readiness_score
fallback_behavior: BLOCKED_BEFORE_OUTPUT or NEEDS_HUMAN_REVIEW when required fields are missing
lineage_fields:
  - upstream_packet_id
  - downstream_packet_id
  - source_component_id
  - evidence_path
  - storyboard_export_path
  - prompt_packet_schema_version
approval_required: true when provider execution, media creation, repo write, or segment regeneration is requested
provider_execution_allowed: false
