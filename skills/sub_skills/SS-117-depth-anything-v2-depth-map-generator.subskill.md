# SUBSKILL SS-117 - Depth Anything V2 Depth Map Generator

## SECTION 1: SKILL IDENTITY & OWNERSHIP
- Skill_ID: SS-117
- Canonical_Name: Depth Anything V2 Depth Map Generator
- Archetype: machine_learning
- Role_Type: PRIMARY_ROLE
- Owner_Director: Vishwakarma
- Domain: Depth Map Generation / Local ML Inference

## SECTION 2: AUTHORITY MATRIX
- Can_Execute: Local ML inference using Depth Anything V2 model, batch processing of still images.
- Cannot_Execute: Modifying image generation prompts with depth-cues (auto-detects).
- Requires_Approval: N/A
- Escalation_Required: Model load failure, out of memory (OOM).
- Veto_Authority: NO

## SECTION 3: READS (INPUT VEINS)
### 3.1 Primary Inputs
- input_images_dir:string (Directory containing source still images)
- output_maps_dir:string (Directory to save depth maps)
- batch_processing:boolean

### 3.2 Provider Context
- local_python_env: /Users/apple/ShadowMediaFactory/tools/depth_anything_v2/
- hardware: Apple M1 Max (MPS backend)
- model: ViT-B (Base)
- model_variant_recommendation:
  - Small / ViT-S for CPU-safe or laptop-conservative runs.
  - Base / ViT-B for balanced M1 Max MPS runs.
  - Large / ViT-L only for GPU-capable runs with explicit resource approval.

## SECTION 4: WRITES (OUTPUT VEINS)
- artifact_family: depth_map_packet
- output_map_paths: array (List of generated depth map PNGs)
- status: success|failed
- write_target: dossier.platform_subskills.depth-anything-v2 (append_only)

## SECTION 5: EXECUTION FLOW & ALGORITHM
1. Validate presence of `input_images_dir`.
2. Load Depth Anything V2 ViT-B model into M1 Max unified memory via MPS.
3. Iterate over input still images.
4. For each image, run inference to generate a float32 normalized grayscale depth map.
5. Export as `depth_{original_filename}.png` in `output_maps_dir`.
6. Unload model to return GPU/CPU load to zero.
7. Return paths of generated depth maps.

## SECTION 6: SCORING FRAMEWORK
- alignment_score (0-100)
- quality_score (0-100)
- cost_efficiency_score (100) - always 100 for local zero-cost renders
- governance_compliance_score (0-100)
- acceptance_rule: quality_score >= 80

## SECTION 7: BEST PRACTICES
- **DaVinci Integration:** Import generated depth map into DaVinci Resolve. Use as a Fusion mask via the Luma Keyer node. Apply different Transform speeds to layers for true 2.5D parallax.
- **Performance:** Expect ~1-2 seconds per image on M1 Max. RAM usage peaks at ~1.5GB during the run.
- **Prompting:** Depth Anything V2 auto-detects depth from any image. DO NOT modify original image generation prompts with explicit depth-cue text.
- **Masking Tool Only:** Depth Anything V2 generates depth masks. It is not an image generator, video generator, cinematic B-roll generator, or visual style prompt engine.
- **DaVinci Fusion Node Graph:** MediaIn(source still) -> duplicate foreground/midground/background layers -> MediaIn(depth_map_png) -> Luma Keyer / Matte Control masks -> Transform nodes per layer -> Merge -> color/blur polish -> MediaOut.
- **Default Parallax Parameters:** foreground drift +6px to +10px, midground drift +2px to +4px, background counter-drift -3px to -6px, slow zoom 100% to 104-106% unless the storyboard specifies otherwise.
- **Laptop Safety:** Prefer Small or Base variants for laptop-safe runs. Use Large only after confirming free RAM/GPU headroom and closing other heavy ML processes.

## SECTION 8: EXECUTION RULES & CONSTRAINTS
- Enforce batch processing to minimize model load/unload cycles overhead.
- Ensure the model unloads cleanly after execution.

## SECTION 9: FAILURE MODES & RECOVERY
- inference_failed -> fallback to DaVinci dual-layer simulation method (no depth map).
- oom_error -> restart script, ensure other Heavy ML processes are closed.

## SECTION 10: TOOL POLICY
- Allowed_Tools: Local Python, MPS backend
- Forbidden_Tools: Cloud depth estimation APIs

## SECTION 11: N8N + OLLAMA PLUGGABILITY
- n8n_consumer_workflows:
  - WF-400
- ollama_reasoning_injection: true
- packet_contract: depth-anything-v2-depth-map-generator_packet
- replay_path: WF-021
- escalation_path: WF-900

## SECTION 12: VALIDATION & ACCEPTANCE
- Must emit output_map_paths and status.
- Must verify depth map is 8-bit or 16-bit grayscale PNG.

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
component_id: SS-117-depth-anything-v2-depth-map-generator.subskill
component_layer: SKILL
component_name: Depth Anything V2 Depth Map Generator
route_families: [media_factory, repo_write_mode]
activation_triggers: route_family in [media_factory]
upstream_inputs: [visual_context_packet]
downstream_outputs: [media_quality_gate_packet]
required_input_packets: [visual_context_packet]
emitted_output_packets: [media_quality_gate_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL]
quality_gates: [explicit_user_approval_gate, scope_lock_gate]
validator_bindings: [no_n8n_provider_media_execution, provider_boundary_present]
fallback_behavior: fallback to DaVinci dual-layer simulation method.
lineage_fields: [approval_packet_id, user_decision, scope]
provider_boundary: provider_execution_allowed=false; execution remains entirely local
status_limits: May not claim production-ready or provider-called without external proof.
human_approval_points: [approve_patch, approve_commit, reject]
failure_modes: missing_input_packet, missing_output_schema, missing_validator_binding, missing_pointer.
handoff_targets: [media_quality_gate_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL]
production_score_fields: [handoff_completeness_score, risk_score, lineage_score]
skill_activation_contract: Activated by skill_activation_packet from route manifest.
input_schema: Must declare atomic input fields before use.
output_schema: Must emit atomic output packet with validation status.
subskill_hooks: May call subskills only through atomic_task_packet.
quality_metric: Must emit skill_quality_score and quality_threshold.
