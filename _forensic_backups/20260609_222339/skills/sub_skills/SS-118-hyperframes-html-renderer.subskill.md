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

### 3.2 Provider Context
- install_status: LOCALLY INSTALLED (not global PATH)
- binary_path: `/Users/apple/ShadowMediaFactory/07_PROJECTS/hyperframes/node_modules/.bin/hyperframes`
- control_panel_command: `python3 /Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py run-hyperframes --project-root <project> --output <mp4>`
- version: 0.6.52

## SECTION 4: WRITES (OUTPUT VEINS)
- artifact_family: media_factory_rendered_video
- output_video_path: string
- status: success|failed
- write_target: dossier.platform_subskills.hyperframes-html-renderer (append_only)

## SECTION 5: EXECUTION FLOW & ALGORITHM
1. Scaffold or point to a HyperFrames project template (e.g., `notebooklm_dual_panel`, `gold_title_reveal`, `comparison_card`).
2. Run `hyperframes lint <project>` to validate HTML/JS composition.
3. Run `hyperframes preview <project>` for local browser preview (optional).
4. Run `hyperframes render <project> --output <file.mp4>` (or `--alpha` for WebM) to render the composition.
5. Export MP4 at 1920x1080, 30fps.
6. Verify output file existence and integrity.

## SECTION 6: SCORING FRAMEWORK
- alignment_score (0-100)
- quality_score (0-100)
- cost_efficiency_score (100) - local zero-cost rendering
- governance_compliance_score (0-100)
- acceptance_rule: quality_score >= 80

## SECTION 7: BEST PRACTICES
- **Integration with DaVinci:** Import MP4 outputs to Media Pool. Place on V1 track (slides) or V2 track (overlays). WebM alpha outputs go to V2/V3 for automatic compositing.
- Use HyperFrames for deterministic renders of NotebookLM-style dual-panel slides, programmatic data cards, kinetic title cards, animated lower-thirds, GSAP spring animations, and CSS keyframe bullet reveals.
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
