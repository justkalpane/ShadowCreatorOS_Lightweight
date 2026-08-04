# Phase 5 Subskill Route Split Plan

## 1. Objective

Phase 5 audits the subskill layer so we can separate cinema-first screenplay behavior from the existing content-retention micro-behaviors that still sit underneath `SCRIPT_GENERATION` and related routes.

This phase keeps the useful downstream stack intact and identifies where a parallel filmcraft subskill family is needed for:

- premise pressure
- theme refinement
- beat calibration
- character arc pressure
- scene objective and turn detection
- dialogue subtext
- visual motif recurrence
- blocking and camera intent
- sound and performance microcraft

## 2. Relationship to Phases 1 to 4

- Phase 1 found director-level platform drift.
- Phase 2 found agent-level content/platform drift.
- Phase 3 found subagent-level hook, retention, and trend drift.
- Phase 4 found skill-level content-hook, retention, and platform drift, plus missing filmcraft skills.
- Phase 5 now checks the smallest behavioral units, where the default content rhythm can silently dominate cinema output if we do not split it cleanly.

## 3. Subskill inventory

The subskill layer scan covered 128 files under `skills/sub_skills/` and checked the registry against the on-disk files.

- registry entries checked in `registries/subskill_runtime_registry.yaml`: 40
- missing registry-file pairs: 0
- focused in-depth subskill files line-read for this audit: 39

Focused in-depth files:

| Subskill | File path | Current role | Cinema-core ready? | Platform/content drift? | Recommended mode split | Patch priority | Notes |
|---|---|---|---|---|---|---|---|
| ElevenLabs Voice Generation Optimizer | `skills/sub_skills/SS-101-elevenlabs-voice-generation-optimizer.subskill.md` | Voice generation and scene-consistent narration support | Partial | Low | Keep downstream support, add film narration mirror later | Medium | Useful for voice and performance, not screenplay structure. |
| HeyGen Avatar Render Orchestrator | `skills/sub_skills/SS-102-heygen-avatar-render-orchestrator.subskill.md` | Avatar render orchestration and lip-sync support | No | Low | Keep downstream only | Medium | Strong production support, not film-writing craft. |
| NanoBanana Visual Generation Optimizer | `skills/sub_skills/SS-103-nanobanana-visual-generation-optimizer.subskill.md` | Visual generation and style constraints | Partial | Low | Keep downstream support | Medium | Good visual support; not a screenplay skill. |
| Sora Video Generation Orchestrator | `skills/sub_skills/SS-104-sora-video-generation-orchestrator.subskill.md` | Shot-sequence video generation support | Partial | Low | Keep downstream support | Medium | Valuable for media production, not core film writing. |
| Higgsfield Cinematic Motion Director | `skills/sub_skills/SS-105-higgsfield-cinematic-motion-director.subskill.md` | Cinematic motion planning | Yes | Low | Keep as reusable film-support | Low | One of the strongest subskill-level film assets already present. |
| Kling Video Prompt Optimizer | `skills/sub_skills/SS-106-kling-video-prompt-optimizer.subskill.md` | Prompt optimization for video generation | Partial | Low | Keep downstream support | Medium | Use for media generation, not screenplay core. |
| Suno Music Generation Optimizer | `skills/sub_skills/SS-107-suno-music-generation-optimizer.subskill.md` | Music generation and emotion curve support | Partial | Low | Keep downstream support | Medium | Useful for sound design and trailer scoring. |
| OpenRouter LLM Route Governor | `skills/sub_skills/SS-110-openrouter-llm-route-governor.subskill.md` | Model routing governance | Yes | None | Keep as governance support | Low | Good generic control-plane support. |
| Ollama Local Inference Optimizer | `skills/sub_skills/SS-111-ollama-local-inference-optimizer.subskill.md` | Local inference optimization | Yes | None | Keep as infrastructure support | Low | Reusable infra support. |
| FFmpeg Render Assembly Guard | `skills/sub_skills/SS-112-ffmpeg-render-assembly-guard.subskill.md` | Render assembly and QC | Yes | Low | Keep downstream support | Low | Important for render safety, not screenplay craft. |
| Wav2Lip LipSync Quality Guard | `skills/sub_skills/SS-113-wav2lip-lipsync-quality-guard.subskill.md` | Lip-sync quality control | Yes | Low | Keep downstream support | Low | Good for production finishing. |
| Gemini Multimodal Research Optimizer | `skills/sub_skills/SS-115-gemini-multimodal-research-optimizer.subskill.md` | Multimodal research support | Yes | Low | Keep as research support | Low | Useful across content and film modes. |
| NotebookLM Visual Style Orchestrator | `skills/sub_skills/SS-116-notebooklm-visual-style-orchestrator.subskill.md` | Local presentation/render style orchestration | Yes | Low | Keep downstream support | Low | Strong visual production support, clearly downstream. |
| Depth Anything V2 Depth Map Generator | `skills/sub_skills/SS-117-depth-anything-v2-depth-map-generator.subskill.md` | Depth-map generation for parallax | Yes | Low | Keep downstream support | Low | Good for motion graphics and parallax, not screenplay logic. |
| HyperFrames HTML Renderer | `skills/sub_skills/SS-118-hyperframes-html-renderer.subskill.md` | Local HTML/GSAP rendering | Yes | Low | Keep downstream support | Low | Strong media-factory support. |
| Deep Research Agent | `skills/sub_skills/SS-220-deep-research-agent.subskill.md` | Research planning and source diversity | Yes | Low | Keep as research support | Low | Reusable in film research. |
| Source Credibility Evaluator | `skills/sub_skills/SS-221-source-credibility-evaluator.subskill.md` | Source trust scoring | Yes | Low | Keep as research/governance support | Low | Valuable for proof-backed film work. |
| Fact Verification Engine | `skills/sub_skills/SS-222-fact-verification-engine.subskill.md` | Fact validation and contradiction escalation | Yes | Low | Keep as verification support | Low | Reusable across film and content modes. |
| Knowledge Synthesizer | `skills/sub_skills/SS-223-knowledge-synthesizer.subskill.md` | Knowledge fusion and citation retention | Yes | Low | Keep as synthesis support | Low | Useful across both modes. |
| Contradiction Detector | `skills/sub_skills/SS-224-contradiction-detector.subskill.md` | Semantic contradiction detection | Yes | Low | Keep as governance support | Low | Good safety layer for film sourcing. |
| Content Angle Generator | `skills/sub_skills/SS-230-content-angle-generator.subskill.md` | Content angle selection | No | Yes | Replace core use, keep content mode only | High | This is a creator/content-default micro-behavior. |
| Unique Value Proposition Builder | `skills/sub_skills/SS-231-unique-value-proposition-builder.subskill.md` | UVP selection and competitor fit | No | Yes | Replace core use, keep content mode only | High | Works for content strategy, not screenplay structure. |
| Series Strategy Planner | `skills/sub_skills/SS-232-series-strategy-planner.subskill.md` | Episode retention objectives | No | Yes | Move downstream or content mode only | High | Better as series/release logic, not film core. |
| Content Calendar Generator | `skills/sub_skills/SS-233-content-calendar-generator.subskill.md` | Content cadence planning | No | Yes | Move downstream only | High | Not relevant to screenplay generation. |
| Platform Strategy Mapper | `skills/sub_skills/SS-234-platform-strategy-mapper.subskill.md` | Platform distribution strategy | No | Yes | Move downstream only | High | Important for release packaging, not film writing. |
| Hook Variation Generator | `skills/sub_skills/SS-240-hook-variation-generator.subskill.md` | Opening hook variants and retention tuning | No | Yes | Replace core use, keep content mode only | High | Strong content-hook bias. |
| Open Loop Generator | `skills/sub_skills/SS-241-open-loop-generator.subskill.md` | Open-loop design for retention | No | Yes | Replace core use, keep content mode only | High | Platform retention logic should not drive film core. |
| Story Tension Builder | `skills/sub_skills/SS-242-story-tension-builder.subskill.md` | Story tension and escalation | Partial | Some | Refactor toward cinematic tension | Medium | Good bridge capability, but still content-shaped. |
| Pacing Controller | `skills/sub_skills/SS-243-pacing-controller.subskill.md` | Pacing and retention-risk control | Partial | Some | Refactor toward cinematic pacing | Medium | Useful, but current language is platform-tuned. |
| Retention Loop Engine | `skills/sub_skills/SS-244-retention-loop-engine.subskill.md` | Retention loops and analytics attribution | No | Yes | Replace core use, keep content mode only | High | Strongly platform-retention driven. |
| Cliffhanger Designer | `skills/sub_skills/SS-245-cliffhanger-designer.subskill.md` | Cliffhanger and continuation hooks | No | Yes | Replace core use, keep content mode only | High | Good for serial content, not film-core screenplay craft. |
| Dynamic Prompt Builder | `skills/sub_skills/SS-250-dynamic-prompt-builder.subskill.md` | Prompt formatting and envelope packing | Yes | None | Keep as generic support | Low | Useful for all modes. |
| Context Window Optimizer | `skills/sub_skills/SS-251-context-window-optimizer.subskill.md` | Context length control | Yes | None | Keep as generic support | Low | Generic infrastructure skill. |
| Token Efficiency Engine | `skills/sub_skills/SS-252-token-efficiency-engine.subskill.md` | Token compression and simplification | Yes | None | Keep as generic support | Low | Generic infrastructure skill. |
| Multi-Model Consensus Engine | `skills/sub_skills/SS-253-multi-model-consensus-engine.subskill.md` | Consensus scoring and schema alignment | Yes | None | Keep as generic support | Low | Useful for validation across routes. |
| Fallback Prompt Engine | `skills/sub_skills/SS-254-fallback-prompt-engine.subskill.md` | Safe fallback prompt generation | Yes | None | Keep as generic support | Low | Good safety support. |

## 4. Subskill family classification

### Content angle and UVP

- `SS-230` and `SS-231` are content-route micro-behaviors
- they should not drive film screenplay generation

### Hook variation, open loop, retention loop, cliffhanger

- `SS-240`, `SS-241`, `SS-244`, and `SS-245` are heavily content-retention oriented
- they belong in content mode or downstream serialization, not in film-core screenplay behavior

### Pacing and story tension

- `SS-242` and `SS-243` are useful but still need cinema-first wording
- they should become cinematic tension and pacing passes rather than retention passes

### Voice, visual, media, and production support

- `SS-101` through `SS-118` include reusable production support
- most of these are downstream support or film-support, not screenplay logic

### Research, verification, and governance

- `SS-220` through `SS-224` are reusable and should remain available to both modes
- they are important for proof-backed film work and source honesty

### Prompt engineering and context efficiency

- `SS-250` through `SS-254` are generic infra skills
- they are reusable as-is and should not be treated as content-specific drift

## 5. Film-core subskill requirements

A cinema-first subskill layer needs dedicated subskills for:

- premise pressure test
- theme statement refinement
- beat calibration
- act-transition checking
- escalation checking
- character want/need contrast
- character flaw pressure
- antagonistic force calibration
- scene objective clarifier
- scene obstacle/tactic clarifier
- scene value-turn detector
- dialogue subtext pass
- dialogue voice distinctness pass
- visual motif recurrence pass
- mise-en-scene detail pass
- blocking intent pass
- camera/lens/framing pass
- sound motif recurrence pass
- silence and pause design pass
- performance beat pass
- screenplay format micro-pass
- continuity micro-pass

## 6. Non-goals

Phase 5 does not patch subskills yet.

It does not:

- delete the content engine
- create film routes
- create contracts
- create validators
- change runtime behavior
- claim any PASS state

