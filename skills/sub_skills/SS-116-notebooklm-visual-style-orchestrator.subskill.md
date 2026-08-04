# SUBSKILL SS-116 - NotebookLM Visual Style Orchestrator

## SECTION 1: SKILL IDENTITY & OWNERSHIP
- Skill_ID: SS-116
- Canonical_Name: NotebookLM Visual Style Orchestrator
- Archetype: integration
- Role_Type: PRIMARY_ROLE
- Owner_Director: Maya
- Domain: Visual Rendering

## SECTION 2: AUTHORITY MATRIX
- Can_Execute: layout template loading, dynamic highlights, HyperFrames CLI rendering, Playwright browser rendering, frame sequence compilation
- Cannot_Execute: policy override, direct file export outside mission targets, unauthorized network calls
- Requires_Approval: provider fallback if local headless rendering is blocked
- Escalation_Required: Playwright startup failure, frame capture timeout
- Veto_Authority: NO

## SECTION 3: READS (INPUT VEINS)
### 3.1 Primary Inputs
- dossier_id:string
- sources_list:array (list of documents displayed on the left panel)
- active_note_text:string (text displayed on the right panel card)
- highlight_phrases:array (strings that glow orange/gold sequentially)
- scroll_velocity:number (scroll speed rate)
- duration_seconds:number

### 3.2 Provider Context
- hyperframes_cli (Primary: /Users/apple/ShadowMediaFactory/07_PROJECTS/hyperframes/node_modules/.bin/hyperframes)
- local_playwright_instance (Fallback)
- local_ffmpeg_assembler
- provider_id: hyperframes_cli_local
- connector_assessment_contract: `runtime_contracts/HYPERFRAMES_CONNECTOR_INTEGRATION_CONTRACT.md`

## SECTION 4: WRITES (OUTPUT VEINS)
- artifact_family:notebooklm-rendered-broll_packet
- output_video_path:string
- status:success|failed|degraded
- write_target: dossier.platform_subskills.notebooklm-visual-style-orchestrator (append_only)
- write_target: se_packet_index (append_only)

## SECTION 5: EXECUTION FLOW & ALGORITHM
1. Load HTML/CSS template containing the dual-panel NotebookLM layout.
2. Inject `sources_list` and `active_note_text` into the DOM.
3. Run `python3 /Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py run-hyperframes --project-root <project> --output <file.mp4> --template-family notebooklm_dual_panel --visual-pattern notebooklm_clean_dual_panel` so proof JSON and registry evidence are emitted.
4. Trigger CSS keyframe animations for sequential word highlights matched to timeline stamps.
5. (Fallback) If HyperFrames fails, launch Playwright headless browser instance to capture frames at 60fps and use FFmpeg to assemble MP4.
6. Verify file integrity and register output packet in lineage indexes.
7. Verify `proof_json_path` and `assets.jsonl` registry event before claiming any NotebookLM-style video artifact.

## SECTION 6: SCORING FRAMEWORK
- alignment_score (0-100)
- quality_score (0-100)
- cost_efficiency_score (100) - always 100 for local zero-cost renders
- governance_compliance_score (0-100)
- acceptance_rule: governance_compliance_score >= 90 and quality_score >= 80

## SECTION 7: BEST PRACTICES
- Use clean modern typography resembling the actual NotebookLM platform.
- Ensure text highlights have a high color contrast ratio matching a11y guidelines.
- Align dynamic document scrolling with voice narration timestamps to maintain pacing.
- Render in Rec.709 color space and standard 1080p resolution.
- **Prefer HyperFrames CLI render** for deterministic output; HyperFrames binary path: `/Users/apple/ShadowMediaFactory/07_PROJECTS/hyperframes/node_modules/.bin/hyperframes`.
- Required dual-panel layout: left source shelf, right active note card, gold/orange highlight glow, typing cursor, and clean browser-chrome-free canvas.
- Required HyperFrames Config block fields: `font_family`, `theme_styling`, `typing_animation`, `scroll_trigger`, `gsap_timeline_sync`, and `davinci_layering`.
- Required asset inventory: list every SVG/PNG/background canvas used by the source shelf or active note; if none are needed, state `assets_needed=NONE (CSS vectors only)`.
- Required DaVinci composite layout: V1 must be the rendered slide background MP4/WebM; V2 may be a chromakeyed HeyGen presenter or empty presenter lane.
- Required proof parity: every rendered NotebookLM-style panel must have HyperFrames proof JSON with `providers_called=false`, `n8n_used=false`, `template_family=notebooklm_dual_panel`, and an `assets.jsonl` registry event.
- Required connector parity: when the HyperFrames path is claimed, the output must also include `TOOLS_CONNECTORS_PLUGINS_ASSESSMENT` for `hyperframes_cli_local` and the upstream HyperFrames skill proof chain.
- Required scene blueprint fields when this lane is used inside a generator draft: `template_family=notebooklm_dual_panel`, `visual_pattern`, `source_background`, `floating_panel_layers`, `kinetic_text_layers`, `lane_assignment`, and `proof_gate=hyperframes_proof_json`.
- Anti-drift: This subskill simulates the NotebookLM visual style locally. It must not claim to operate Google NotebookLM or use actual cloud NotebookLM as a renderer.

## SECTION 8: EXECUTION RULES & CONSTRAINTS
- Enforce patch-only mutation on dossier data writes.
- Do not make external API requests; render entirely locally.
- Retain temporary screenshot sequences only until video assembly completes.

## SECTION 9: FAILURE MODES & RECOVERY
- hyperframes_render_failed -> fallback to playwright_headless
- playwright_launch_failed -> fallback to static slide fallback using Python Pillow
- render_timeout -> clear cache, retry with half frame rate (30fps)
- compile_failed -> trigger manual timeline warning and raise alert

## SECTION 10: TOOL POLICY
- Allowed_Tools: HyperFrames CLI, Playwright headless browser, FFmpeg CLI, local python utilities
- Forbidden_Tools: external slide generation APIs, web screenshot scrapers

## HYPERFRAMES INTEGRATION ADDENDUM
- Utilizes the `notebooklm_dual_panel` project template.
- Can render transparent WebM outputs using the `--alpha` flag if needed for overlay usage.
- Uses control panel command: `python3 /Users/apple/ShadowMediaFactory/control_panel/bin/shadow_factory_ctl.py run-hyperframes --project-root <project> --output <mp4> --template-family notebooklm_dual_panel --visual-pattern notebooklm_clean_dual_panel`
- **Capabilities vs. Actual Web App Comparison**:
  - *Video Export*: Local HyperFrames supports programmatic, headless rendering to high-quality MP4/WebM videos directly. Actual Google NotebookLM has no video export (manual screen-recording looks amateur).
  - *Highlight & Audio Sync*: Local HyperFrames achieves millisecond-accurate text highlighting synced via GSAP timelines to the ElevenLabs voice track. Actual NotebookLM highlights dynamically as it streams text, which is impossible to sync to an audio track.
  - *Clutter & Layout Cleanliness*: Local HyperFrames templates remove toolbars, profile badges, chat input boxes, and settings icons to keep visual presentation clean. Actual NotebookLM retains cluttered browser frames and widgets.
  - *Typing Animation*: Local HyperFrames simulates typing using JS string interpolation to fake character printouts in real-time. Actual NotebookLM uses standard dynamic chat streaming with variable delays.
  - *Technical Curve*: Local HyperFrames requires developer skill (HTML/CSS/JS editing) to modify variables/templates, whereas Actual NotebookLM has zero skill curve (standard cloud GUI).
- **Template Synchronization Constraints**:
  - All rendered templates must remove browser chrome, feedback widgets, and toolbars.
  - Typing animations must be simulated via JS interpolation.
  - Timeline highlights must be defined dynamically in millisecond offsets to lock step with voiceovers.


## SECTION 11: N8N + OLLAMA PLUGGABILITY
- n8n_consumer_workflows:
  - WF-400
- ollama_reasoning_injection: true
- packet_contract: notebooklm-visual-style-orchestrator_packet
- replay_path: WF-021
- escalation_path: WF-900

## SECTION 12: VALIDATION & ACCEPTANCE
- Must emit output_video_path, status, and duration validation checks.
- Must pass file-level schema validation.

## MAC-06.2B UNIVERSAL COMPONENT CONTRACT UPGRADE
component_id: SS-116-notebooklm-visual-style-orchestrator.subskill
component_layer: SKILL
component_name: Ss 116 Notebooklm Visual Style Orchestrator.Subskill
route_families: [media_factory_handoff, visual_media_plan, media_factory_final_draft, media_factory, repo_write_mode]
activation_triggers: route_family in [media_factory, repo_write_mode] or explicit registry selection
upstream_inputs: [visual_context_packet, editing_timeline_packet, approval_packet]
downstream_outputs: [media_quality_gate_packet]
required_input_packets: [visual_context_packet, editing_timeline_packet, approval_packet]
emitted_output_packets: [media_quality_gate_packet]
communication_pointers: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL]
quality_gates: [explicit_user_approval_gate, scope_lock_gate]
validator_bindings: [no_n8n_provider_media_execution, provider_boundary_present]
fallback_behavior: BLOCKED_BEFORE_OUTPUT until explicit user approval is present.
lineage_fields: [approval_packet_id, user_decision, scope]
provider_boundary: provider_execution_allowed=false by default; execution remains entirely local
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

## MAC-06.2D ROUTE-SPECIFIC PRODUCTION DEPTH ENRICHMENT
component_depth_status: PRODUCTION_DEPTH_ENRICHED
route_profile_applied: media_factory_profile
route_family_resolved: [media_factory_handoff, visual_media_plan, media_factory_final_draft, media_factory, repo_write_mode]
activation_triggers_resolved: [storyboard, visual plan]
required_input_packets_resolved: [visual_context_packet, editing_timeline_packet, approval_packet]
emitted_output_packets_resolved: [media_quality_gate_packet]
communication_pointer_ids_resolved: [PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL]
validator_bindings_resolved: [no_n8n_provider_media_execution, provider_boundary_present]
quality_gates_resolved: [explicit_user_approval_gate, scope_lock_gate]
fallback_behavior_resolved: BLOCKED_BEFORE_OUTPUT until explicit user approval is present.
lineage_fields_resolved: [approval_packet_id, user_decision, scope]
provider_boundary_resolved: provider_execution_allowed=false by default; execution remains local
handoff_targets_resolved: [media_quality_gate_packet, PTR_DIRECTOR_AGENT, PTR_AGENT_SUBAGENT, PTR_SUBAGENT_SKILL, PTR_SKILL_SUBSKILL]
production_score_fields_resolved: [handoff_completeness_score, risk_score, lineage_score]
human_approval_points_resolved: [approve_patch, approve_commit, reject]
status_limits_resolved: [no provider-called claim without execution proof]
evidence_used_for_resolution: component_path=skills/sub_skills/SS-116-notebooklm-visual-style-orchestrator.subskill.md; component_id=SS-116-notebooklm-visual-style-orchestrator
remaining_unknowns: none

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
  - local_engine_execution_claim_without_bridge_job_packet
  - full_render_unlock_until_visual_qa
