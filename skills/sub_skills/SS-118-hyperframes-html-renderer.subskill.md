# SUBSKILL SS-118 - HyperFrames HTML Renderer

## SECTION 1: SKILL IDENTITY & OWNERSHIP
- Skill_ID: SS-118
- Canonical_Name: HyperFrames HTML Renderer
- Archetype: rendering
- Role_Type: PRIMARY_ROLE
- Owner_Director: Vishwakarma
- Domain: HTML Motion Graphics Rendering / Local CLI Render

## SECTION 2: AUTHORITY MATRIX
- Can_Execute: Local CLI rendering of HTML/CSS/GSAP compositions to MP4/WebM.
- Cannot_Execute: AI image generation, cinematic B-roll generation, 2.5D parallax on photo images, voice/audio generation.
- Requires_Approval: N/A
- Escalation_Required: Render failure.
- Veto_Authority: NO

## SECTION 3: READS (INPUT VEINS)
### 3.1 Primary Inputs
- project_root:string (Path to the HyperFrames HTML/CSS project)
- output_path:string (Path for the output MP4/WebM file)
- alpha:boolean (Render transparent WebM if true)
- template_family:string (`playstation_dashboard_panel`, `notebooklm_dual_panel`, `image_evidence_wall`, `kinetic_principle_card`, or `webm_alpha_overlay`)
- visual_pattern:string (scene-specific motion graphics pattern)

### 3.2 Provider Context
- install_status: LOCALLY INSTALLED (not global PATH)
- binary_path: `/Users/apple/ShadowMediaFactory/07_PROJECTS/hyperframes/node_modules/.bin/hyperframes`
- control_panel_command: `python3 /Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py run-hyperframes --project-root <project> --output <mp4> --template-family <family> --visual-pattern <pattern>`
- version: 0.6.52
- provider_id: hyperframes_cli_local
- connector_assessment_contract: `runtime_contracts/HYPERFRAMES_CONNECTOR_INTEGRATION_CONTRACT.md`
- upstream_skill_paths:
  - `/Users/apple/.codex/plugins/cache/openai-curated/hyperframes/3fdeeb49/skills/hyperframes/SKILL.md`
  - `/Users/apple/.codex/plugins/cache/openai-curated/hyperframes/3fdeeb49/skills/hyperframes-cli/SKILL.md`
  - `/Users/apple/.codex/plugins/cache/openai-curated/hyperframes/3fdeeb49/skills/hyperframes-registry/SKILL.md`

## SECTION 4: WRITES (OUTPUT VEINS)
- artifact_family: media_factory_rendered_video
- output_video_path: string
- proof_json_path: string
- registry_event: `assets.jsonl` event `hyperframes_rendered`
- status: success|failed
- write_target: dossier.platform_subskills.hyperframes-html-renderer (append_only)

## SECTION 5: EXECUTION FLOW & ALGORITHM
1. Scaffold or point to an approved HyperFrames project template.
2. Confirm the project has `index.html` and optional `hyperframes_manifest.json`.
3. Run the control panel `run-hyperframes` command so proof JSON and registry evidence are emitted.
4. Export MP4/WebM at 1920x1080, 30fps unless the project explicitly states otherwise.
5. Verify output file existence, duration via ffprobe, proof JSON path, and registry event.
6. Emit the `TOOLS_CONNECTORS_PLUGINS_ASSESSMENT` row for `hyperframes_cli_local` before any generated-media claim.

## SECTION 6: SCORING FRAMEWORK
- alignment_score (0-100)
- quality_score (0-100)
- cost_efficiency_score (100) - local zero-cost rendering
- governance_compliance_score (0-100)
- acceptance_rule: quality_score >= 80

## SECTION 7: BEST PRACTICES
- **Integration with DaVinci:** Import MP4 outputs to Media Pool. Place on V1 track (slides) or V2 track (overlays). WebM alpha outputs go to V2/V3 for automatic compositing.
- Use HyperFrames for deterministic renders of NotebookLM-style dual-panel slides, programmatic data cards, kinetic title cards, animated lower-thirds, GSAP spring animations, and CSS keyframe bullet reveals.
- First-foundation non-cinematic B-roll templates are `playstation_dashboard_panel`, `notebooklm_dual_panel`, `image_evidence_wall`, `kinetic_principle_card`, and `webm_alpha_overlay`.
- For local image/video B-roll panels, declare lane assignment as `V1 background`, `V2 HyperFrames panel`, `V3 alpha overlay/CTA`, `A1 voice`, `A2 music`, `A3 SFX`.
- Required generator-draft blueprint fields are `template_family`, `visual_pattern`, `source_background`, `floating_panel_layers`, `kinetic_text_layers`, `lane_assignment`, and `proof_gate=hyperframes_proof_json`.
- Do NOT use for 2.5D parallax (use DaVinci + Depth Anything V2), cinematic B-roll, DaVinci replacement, or FFmpeg replacement.
- Supported layout templates must include: `split_card_horizontal`, `fullscreen_text_center`, and `notebook_dual_panel`. Existing project aliases such as `notebooklm_dual_panel`, `gold_title_reveal`, and `comparison_card` may map into these canonical templates.
- Font standards: use Bebas Neue for impact titles / numeric reveals; use Outfit for body, notebook, source-shelf, and explanation text.
- GSAP animation format must specify timeline events with exact offsets, e.g. `gsap_timeline_sync=highlight_1 at +3.2s ('phrase'), card_in at +0.5s, scroll_to_line_3 at +12.0s`.
- WebM alpha pipeline: render with the HyperFrames alpha flag when overlays are required, export transparent WebM, place on DaVinci V2/V3 above the base video, and preserve alpha during final assembly.

## SECTION 8: EXECUTION RULES & CONSTRAINTS
- Render outputs MUST be deterministic: same input HTML = same output MP4/WebM every time.
- Agent-automatable using CLI; no GUI required.
- **Local Performance Footprint**:
  - Render speed target: ~10 to 20 seconds to compile a 30-second 1080p video (running at ~1.5x to 3x real-time rendering speed).
  - Resource usage limits: Spawning headless Chromium browser should maintain a light memory envelope (typically 100MB–200MB of active RAM) and low background CPU/GPU loads to protect local workstation performance.
- **External Asset Injection Standard**:
  - By default, NotebookLM-style presentation templates do NOT require generating external images for core text or vectors. Pure CSS elements, grid lines, and Google fonts should be used.
  - External assets must be supplied only for:
    1. *Document Page Previews (Optional)*: If a source card in the left panel displays a visual preview thumbnail of a document page, supply a static PNG of that page (e.g. `source_doc_preview_s1.png`).
    2. *Logo & Branding Graphics*: Watermarks, icons, or channel logos loaded as SVGs or transparent PNGs.
    3. *Avatar Overlays (A-Roll)*: HeyGen talking-head presenter clips. Note: The presenter avatar is NOT rendered inside the HyperFrames HTML project; the slide is rendered as a clean background, and the HeyGen clip is chromakey-composited over the slide inside DaVinci Resolve.


## SECTION 9: FAILURE MODES & RECOVERY
- doctor_docker_missing -> non-blocking for local renders, continue execution.
- render_failed -> check HTML/CSS linting, retry.

## SECTION 10: TOOL POLICY
- Allowed_Tools: HyperFrames CLI, local Node.js, Chrome headless
- Forbidden_Tools: Cloud HTML rendering APIs

## SECTION 11: N8N + OLLAMA PLUGGABILITY
- n8n_consumer_workflows:
  - WF-400
- ollama_reasoning_injection: true
- packet_contract: hyperframes-html-renderer_packet
- replay_path: WF-021
- escalation_path: WF-900

## SECTION 12: VALIDATION & ACCEPTANCE
- Must emit output_video_path and status.
- Must verify output is valid MP4 or WebM (with alpha if requested).
- Must emit proof JSON and `assets.jsonl` registry evidence before any generated-media claim.
- Must emit `TOOLS_CONNECTORS_PLUGINS_ASSESSMENT` plus the official skill proof
  paths before any HyperFrames-generated-media claim.
- Must not silently downgrade a requested HyperFrames family to generic `ffmpeg_ken_burns`; if fallback is needed, emit `ROUTE_DOWNGRADED=true`, `fallback_reason`, `requested_hyperframes_family`, and `replacement_method`.

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
component_id: SS-118-hyperframes-html-renderer.subskill
component_layer: SKILL
component_name: HyperFrames HTML Renderer
route_families: [media_factory_handoff, visual_media_plan, media_factory_final_draft, media_factory, repo_write_mode]
activation_triggers: route_family in [media_factory]
upstream_inputs: [visual_context_packet]
downstream_outputs: [media_quality_gate_packet]
required_input_packets: [visual_context_packet]
emitted_output_packets: [media_quality_gate_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL]
quality_gates: [explicit_user_approval_gate, scope_lock_gate]
validator_bindings: [no_n8n_provider_media_execution, provider_boundary_present]
fallback_behavior: fallback to playwright headless rendering.
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

## BATCH 4 MEDIA FACTORY RUNTIME BINDING

binding_stage: BATCH_4_ROUTE_SUBSKILL_RUNTIME_BOUND
required_runtime_state_schemas:
  - schemas/runtime_state/evidence_bundle.schema.json
  - schemas/runtime_state/route_state_capsule.schema.json
required_schema_bindings:
  - schemas/media_factory/hyperframes_payload.schema.json
  - schemas/media_factory/bridge_job_packet.schema.json
  - schemas/media_factory/source_vs_render_packet.schema.json
  - schemas/media_factory/visual_qa_acceptance_packet.schema.json
required_validator_bindings:
  - validators/validate_evidence_bundle.py
  - validators/validate_route_state_capsule.py
  - validators/validate_hyperframes_payload.py
  - validators/validate_bridge_job_packet.py
  - validators/validate_source_vs_render_packet.py
  - validators/validate_visual_qa_acceptance.py
blocked_unlocks_after_batch4:
  - hyperframes_family_claim_without_proof
  - full_render_unlock_until_visual_qa
