# Phase 5 Subskill Platform Drift Ledger

This ledger focuses on the subskills that most strongly encode content-retention defaults, platform-first micro-behavior, or reusable support behavior.

Registry evidence:

- registry entries checked in `registries/subskill_runtime_registry.yaml`: 40
- missing registry-file pairs: 0

| Subskill/File | Line or evidence reference | Term/finding | Current context | Classification | Reason | Proposed film-mode equivalent | Keep downstream? | Risk if ignored |
|---|---|---|---|---|---|---|---|---|
| `skills/sub_skills/SS-230-content-angle-generator.subskill.md` | lines 1, 52-65, 121-136 | content angle, audience pain points, channel history | Content-angle micro-behavior | REPLACE | This is a content-first selection heuristic, not screenplay craft | `film_premise_angle_pressure_test` | No | Film prompts may be reduced to creator-angle optimization. |
| `skills/sub_skills/SS-231-unique-value-proposition-builder.subskill.md` | lines 1, 51-65, 121-136 | UVP, competitor baseline, audience intent | Content UVP scoring | REPLACE | Useful for content positioning but not film narrative structure | `film_theme_and_premise_refiner` | No | Story could be judged by market fit alone. |
| `skills/sub_skills/SS-232-series-strategy-planner.subskill.md` | lines 8, 51, 65, 120-135 | retention objective per episode | Series retention planning | MOVE | Best used downstream for episodic distribution | `series_release_adaptation_planner` | Yes | Episode-by-episode retention logic could leak into film development. |
| `skills/sub_skills/SS-233-content-calendar-generator.subskill.md` | lines 51-54, 121-136 | cadence, evergreen/trend blend, audience activity | Publishing cadence planning | MOVE | Distribution and release scheduling only | `film_release_calendar_planner` | Yes | Calendar logic should not define screenplay shape. |
| `skills/sub_skills/SS-234-platform-strategy-mapper.subskill.md` | lines 52-56, 97-137 | platform-specific success metrics, channel priorities | Platform distribution strategy | MOVE | Strong downstream release support | `film_distribution_strategy_mapper` | Yes | Platform logic should stay outside film core. |
| `skills/sub_skills/SS-240-hook-variation-generator.subskill.md` | lines 51-66, 143-145 | opening-hook candidates, recurring re-hook candidates | Hook and retention design | REPLACE | Core micro-behavior is click/retention oriented | `cinematic_opening_tension_variation_engine` | No | Hook-first behavior can dominate the film opening. |
| `skills/sub_skills/SS-241-open-loop-generator.subskill.md` | lines 50, 143-145 | open loops with recurring re-hooks | Retention loop design | REPLACE | Directly encodes content-retention loops | `cinematic_opening_question_and_payoff_engine` | No | Can push screenplay writing toward cliffhanger-first behavior. |
| `skills/sub_skills/SS-242-story-tension-builder.subskill.md` | lines 52-54, 143-144 | contrast beats, tension resets | Story tension support | REFACTOR | Useful, but wording still comes from the content-retention lane | `scene_tension_and_turn_builder` | Yes | Needs film-native language to avoid retention framing. |
| `skills/sub_skills/SS-243-pacing-controller.subskill.md` | lines 50-54, 143-146 | retention-risk pacing, platform form factor, re-hook gap | Pacing optimization | REFACTOR | Valuable, but still optimized around platform retention | `cinematic_pacing_and_act_turn_checker` | Yes | Without refactor, pacing may remain platform-shaped. |
| `skills/sub_skills/SS-244-retention-loop-engine.subskill.md` | lines 50-54, 143-147 | loop-back cues, payoff cadence, analytics attribution | Retention system | REPLACE | This is the clearest content-retention lock in the subskill layer | `film_scene_momentum_and_payoff_checker` | No | Very high risk if used in screenplay core. |
| `skills/sub_skills/SS-245-cliffhanger-designer.subskill.md` | lines 50-54, 143-145 | cliffhangers, continuation hooks, series strategy | Cliffhanger / continuation design | REPLACE | Great for serialized content, wrong default for screenplay core | `cinematic_act_button_and_next-step_promise_engine` | Yes, downstream | Can make scenes feel like episodes instead of dramatic units. |
| `skills/sub_skills/SS-101-elevenlabs-voice-generation-optimizer.subskill.md` | lines 57-62, 104-131 | voice consistency, pacing, pronunciation, scene compilations | Voice generation support | KEEP | Strong production asset, not a film-core drift source | `film_dialogue_narration_voice_engine` | Yes | Low risk if kept as support. |
| `skills/sub_skills/SS-102-heygen-avatar-render-orchestrator.subskill.md` | lines 59-72, 114-141 | avatar-motion consistency, lip-sync, batch render lanes | Avatar rendering support | KEEP | Downstream rendering support only | `film_presenter_overlay_renderer` | Yes | Keep out of screenplay core. |
| `skills/sub_skills/SS-103-nanobanana-visual-generation-optimizer.subskill.md` | lines 52-55, 97-126 | camera intent, style guardrails, visual compliance | Visual generation support | KEEP | Good visual production support | `film_visual_prompt_optimizer` | Yes | Low risk, downstream support. |
| `skills/sub_skills/SS-104-sora-video-generation-orchestrator.subskill.md` | lines 52-56, 97-126 | storyboard-first decomposition, temporal continuity | Video generation support | KEEP | Strong downstream production support | `film_scene_to_shot_orchestrator` | Yes | Keep as media production, not screenplay logic. |
| `skills/sub_skills/SS-105-higgsfield-cinematic-motion-director.subskill.md` | lines 52-54, 97-126 | cinematic motion arcs, camera intent | Cinematic motion support | KEEP | One of the few already film-native support items | `film_camera_motion_director` | Yes | Low risk; keep and reuse. |
| `skills/sub_skills/SS-106-kling-video-prompt-optimizer.subskill.md` | lines 52-55, 97-126 | camera, subject, lighting, motion prompt blocks | Video prompt support | KEEP | Downstream visual generation support | `film_visual_prompt_block_builder` | Yes | Keep outside core screenplay logic. |
| `skills/sub_skills/SS-107-suno-music-generation-optimizer.subskill.md` | lines 52-56, 98-124 | emotion curve, tempo, key, instrumentation | Music and sound support | KEEP | Useful for trailer and film scoring | `film_sound_motif_composer` | Yes | Support only, not screenplay core. |
| `skills/sub_skills/SS-108-youtube-publish-oauth-guard.subskill.md` | lines 53, 64-67, 96-125 | duplicate-publish suppression, quota, publish lane | YouTube release guard | MOVE | Belongs downstream in release/distribution | `film_release_publish_guard` | Yes | Should not influence film writing. |
| `skills/sub_skills/SS-109-youtube-analytics-ingestion-governor.subskill.md` | lines 51, 54, 64, 96-122 | analytics ingest keys, stale token states | YouTube analytics ingestion | MOVE | Release and analytics only | `film_release_analytics_governor` | Yes | Downstream only. |
| `skills/sub_skills/SS-110-openrouter-llm-route-governor.subskill.md` | lines 54-56, 122-140 | model fallback and deterministic envelopes | Generic routing support | KEEP | Reusable governance infrastructure | None | Yes | Low risk. |
| `skills/sub_skills/SS-111-ollama-local-inference-optimizer.subskill.md` | lines 52, 121-139 | local inference optimization | Generic infrastructure support | KEEP | Reusable infra support | None | Yes | Low risk. |
| `skills/sub_skills/SS-112-ffmpeg-render-assembly-guard.subskill.md` | lines 54-59, 119-152 | platform-target render presets, AV sync, J/L cuts | Render assembly support | KEEP | Downstream media production support | `film_render_assembly_guard` | Yes | Keep below screenplay layer. |
| `skills/sub_skills/SS-113-wav2lip-lipsync-quality-guard.subskill.md` | lines 53, 66, 95-130 | timing drift, lip-sync quality gate | Lip-sync QA | KEEP | Production support only | `film_lipsync_quality_guard` | Yes | Downstream only. |
| `skills/sub_skills/SS-114-yt-dlp-ingestion-compliance-guard.subskill.md` | lines 37-47, 95-130 | ingestion compliance, publish gate | Ingestion compliance | MOVE | Distribution-only guard | `film_source_ingestion_compliance_guard` | Yes | Not relevant to screenplay core. |
| `skills/sub_skills/SS-115-gemini-multimodal-research-optimizer.subskill.md` | lines 51-52, 97-123 | multimodal research with citation requirement | Research support | KEEP | Useful for proof-backed film research | None | Yes | Low risk. |
| `skills/sub_skills/SS-116-notebooklm-visual-style-orchestrator.subskill.md` | lines 42-69, 92-100, 142-182 | dual-panel rendering, timeline highlights, local HyperFrames | Visual rendering support | KEEP | Downstream presentation/render support | `film_visual_reference_renderer` | Yes | Keep out of screenplay core. |
| `skills/sub_skills/SS-117-depth-anything-v2-depth-map-generator.subskill.md` | lines 56-79, 85-86, 120-163 | depth-map generation, 2.5D parallax, masking only | Visual motion support | KEEP | Useful downstream support | `film_parallax_depth_support` | Yes | Low risk when kept as tool support. |
| `skills/sub_skills/SS-118-hyperframes-html-renderer.subskill.md` | lines 47-71, 82-89, 115-158 | deterministic HTML/GSAP rendering, alpha WebM | Rendering support | KEEP | Strong downstream rendering support | `film_motion_graphics_renderer` | Yes | Low risk downstream. |
| `skills/sub_skills/SS-220-deep-research-agent.subskill.md` | lines 52-56, 98-124 | source diversity, primary-source preference | Research support | KEEP | Reusable research capability | None | Yes | Low risk. |
| `skills/sub_skills/SS-221-source-credibility-evaluator.subskill.md` | lines 50-65, 96-134 | authority, recency, corroboration, source drift | Source quality support | KEEP | Reusable governance support | None | Yes | Low risk. |
| `skills/sub_skills/SS-222-fact-verification-engine.subskill.md` | line 67 and surrounding validator flow | contradiction routing and fact checking | Fact verification support | KEEP | Reusable across film and content routes | None | Yes | Low risk. |
| `skills/sub_skills/SS-223-knowledge-synthesizer.subskill.md` | lines 65, 80, 93-139 | citation retention and context compression | Knowledge synthesis | KEEP | Reusable support capability | None | Yes | Low risk. |
| `skills/sub_skills/SS-224-contradiction-detector.subskill.md` | lines 50-54, 92-134 | contradiction detection and severity | Governance support | KEEP | Reusable safety layer | None | Yes | Low risk. |
| `skills/sub_skills/SS-250-dynamic-prompt-builder.subskill.md` | lines 43, 53, 86-127 | prompt formatting and hash tracking | Prompt support | KEEP | Generic infrastructure | None | Yes | Low risk. |
| `skills/sub_skills/SS-251-context-window-optimizer.subskill.md` | lines 40-43, 86-126 | token length estimation and truncation | Context support | KEEP | Generic infrastructure | None | Yes | Low risk. |
| `skills/sub_skills/SS-252-token-efficiency-engine.subskill.md` | lines 39-42, 85-123 | token compression and structure consolidation | Token support | KEEP | Generic infrastructure | None | Yes | Low risk. |
| `skills/sub_skills/SS-253-multi-model-consensus-engine.subskill.md` | lines 50-52, 56-64, 85-123 | semantic consensus scoring and schema alignment | Consensus support | KEEP | Generic validation support | None | Yes | Low risk. |
| `skills/sub_skills/SS-254-fallback-prompt-engine.subskill.md` | lines 39-53, 85-123 | fallback prompt generation and structural simplification | Fallback support | KEEP | Generic safety support | None | Yes | Low risk. |

## 3. Classification summary

- KEEP: 25
- REFACTOR: 2
- MOVE: 6
- REPLACE: 6
- DUPLICATE: 0
- DELETE: 0
- NEEDS_DESIGN_DECISION: 0
- MISSING_FILMCRAFT_CAPABILITY: 29
- REGISTRY_FILE_MISMATCH: 0
- READ_BLOCKED: 0

## 4. Top 10 highest-risk subskill drifts

1. `SS-244-retention-loop-engine` - retention loops and analytics attribution
2. `SS-240-hook-variation-generator` - opening hooks and recurring re-hooks
3. `SS-241-open-loop-generator` - open-loop design directly tied to retention
4. `SS-245-cliffhanger-designer` - continuation hooks and series strategy
5. `SS-230-content-angle-generator` - content angle selection driving premise choice
6. `SS-231-unique-value-proposition-builder` - UVP fit steering narrative selection
7. `SS-233-content-calendar-generator` - cadence logic can pull the route into publishing mode
8. `SS-234-platform-strategy-mapper` - platform success metrics can dominate creative decisions
9. `SS-243-pacing-controller` - platform form factor and re-hook gaps can distort film rhythm
10. `SS-232-series-strategy-planner` - retention objective per episode can make a screenplay behave like a serial content plan

## 5. Top 10 most reusable cinema-compatible subskill capabilities

1. `SS-105-higgsfield-cinematic-motion-director`
2. `SS-116-notebooklm-visual-style-orchestrator`
3. `SS-117-depth-anything-v2-depth-map-generator`
4. `SS-118-hyperframes-html-renderer`
5. `SS-113-wav2lip-lipsync-quality-guard`
6. `SS-112-ffmpeg-render-assembly-guard`
7. `SS-115-gemini-multimodal-research-optimizer`
8. `SS-221-source-credibility-evaluator`
9. `SS-222-fact-verification-engine`
10. `SS-223-knowledge-synthesizer`

## 6. Missing filmcraft subskill capabilities

The repo does not show dedicated subskills for:

- Save the Cat beat calibration
- three-act transition checking
- eight-sequence escalation checking
- Hero’s Journey mapping
- Dan Harmon story circle checking
- McKee scene value turns
- Syd Field plot point checking
- character want vs need
- character flaw pressure
- character transformation
- character web
- antagonistic force calibration
- scene objective
- scene obstacle
- scene tactic
- scene value turn
- dialogue subtext
- dialogue voice distinctness
- mise-en-scene detail
- blocking intent
- composition intent
- lens grammar
- camera movement
- visual motif recurrence
- sound motif recurrence
- performance beat
- screenplay format micro-pass
- continuity micro-pass
- film validation micro-pass

## 7. Non-goals

Phase 5 does not patch subskills yet.

It does not:

- delete the content engine
- create film routes
- create contracts
- create validators
- change runtime behavior
- claim any PASS state

