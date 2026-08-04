# Phase 5 Subskill Film Mode Proposal

This proposal defines the target subskill architecture for cinema mode while preserving the existing content and distribution subskills.

## 1. Proposed film-mode subskill families

Recommended new families:

- `skills/film_subskills/story_structure/`
- `skills/film_subskills/character_arc/`
- `skills/film_subskills/scene_dramaturgy/`
- `skills/film_subskills/dialogue_subtext/`
- `skills/film_subskills/visual_language/`
- `skills/film_subskills/directorial_composition/`
- `skills/film_subskills/sound_performance/`
- `skills/film_subskills/screenplay_validation/`

These should be parallel to, not nested inside, the existing content-retention micro-behavior families.

## 2. Proposed film-mode subskills

Recommended new subskills:

- `FS-401-premise-pressure-test.subskill.md`
- `FS-402-theme-statement-refiner.subskill.md`
- `FS-403-save-the-cat-beat-calibrator.subskill.md`
- `FS-404-three-act-transition-checker.subskill.md`
- `FS-405-eight-sequence-escalation-checker.subskill.md`
- `FS-406-character-want-need-contrast-builder.subskill.md`
- `FS-407-character-flaw-pressure-engine.subskill.md`
- `FS-408-antagonistic-force-calibrator.subskill.md`
- `FS-409-scene-objective-clarifier.subskill.md`
- `FS-410-scene-obstacle-tactic-mapper.subskill.md`
- `FS-411-scene-value-turn-detector.subskill.md`
- `FS-412-dialogue-subtext-pass.subskill.md`
- `FS-413-dialogue-voice-distinctness-pass.subskill.md`
- `FS-414-visual-motif-recurrence-pass.subskill.md`
- `FS-415-mise-en-scene-detail-pass.subskill.md`
- `FS-416-blocking-intent-pass.subskill.md`
- `FS-417-camera-lens-framing-pass.subskill.md`
- `FS-418-sound-motif-recurrence-pass.subskill.md`
- `FS-419-silence-pause-design-pass.subskill.md`
- `FS-420-performance-beat-pass.subskill.md`
- `FS-421-screenplay-format-micro-pass.subskill.md`
- `FS-422-continuity-micro-pass.subskill.md`

## 3. Reuse map

| Existing subskill/family | Current bias | Film-mode use | Downstream retained? | Recommendation |
|---|---|---|---|---|
| `SS-101-elevenlabs-voice-generation-optimizer` | Voice generation | Film narration and trailer voice support | Yes | Reuse with film mode. |
| `SS-102-heygen-avatar-render-orchestrator` | Avatar rendering | Presenter/overlay support | Yes | Reuse downstream only. |
| `SS-103-nanobanana-visual-generation-optimizer` | Visual generation | Film visual concept support | Yes | Reuse with film mode. |
| `SS-104-sora-video-generation-orchestrator` | Video generation | Shot/scene production support | Yes | Reuse with film mode. |
| `SS-105-higgsfield-cinematic-motion-director` | Cinematic motion | Direct film-support fit | Yes | Reuse as-is. |
| `SS-106-kling-video-prompt-optimizer` | Video prompt shaping | Film visual prompt support | Yes | Reuse with film mode. |
| `SS-107-suno-music-generation-optimizer` | Music generation | Film sound motif support | Yes | Reuse with film mode. |
| `SS-108-youtube-publish-oauth-guard` | YouTube release guard | Release adaptation only | Yes | Move downstream. |
| `SS-109-youtube-analytics-ingestion-governor` | YouTube analytics | Release analytics only | Yes | Move downstream. |
| `SS-110-openrouter-llm-route-governor` | LLM routing | Governance support | Yes | Reuse as-is. |
| `SS-111-ollama-local-inference-optimizer` | Local inference | Infra support | Yes | Reuse as-is. |
| `SS-112-ffmpeg-render-assembly-guard` | Render assembly | Film render support | Yes | Reuse downstream. |
| `SS-113-wav2lip-lipsync-quality-guard` | Lip-sync QA | Performance/overlay QA | Yes | Reuse downstream. |
| `SS-114-yt-dlp-ingestion-compliance-guard` | Ingestion compliance | Release gating only | Yes | Move downstream. |
| `SS-115-gemini-multimodal-research-optimizer` | Research support | Film research support | Yes | Reuse as-is. |
| `SS-116-notebooklm-visual-style-orchestrator` | Visual rendering | Reference and presentation support | Yes | Reuse downstream. |
| `SS-117-depth-anything-v2-depth-map-generator` | Depth map generation | Motion-graphics support | Yes | Reuse downstream. |
| `SS-118-hyperframes-html-renderer` | HTML/GSAP render | Motion-graphics support | Yes | Reuse downstream. |
| `SS-220` to `SS-224` | Research, credibility, verification, synthesis, contradiction | Evidence and safety support | Yes | Reuse as-is. |
| `SS-230` to `SS-245` | Content angle, UVP, hooks, loops, retention, pacing | Content-mode only, with film mirrors | Yes | Duplicate or refactor into filmcraft family. |
| `SS-250` to `SS-254` | Prompt engineering | Generic infra | Yes | Reuse as-is. |

## 4. Old-to-new responsibility map

| Existing subskill responsibility | Current bias | Film-mode replacement | Downstream retained? | Notes |
|---|---|---|---|---|
| Content angle selection | Creator/content fit | Premise pressure test | No | Film mode should judge dramatic promise, not creator angle. |
| UVP selection | Audience/market fit | Theme and premise refinement | No | Keep market logic downstream if needed. |
| Hook variation | Retention / curiosity gap | Cinematic opening tension | Yes | Film opening should not behave like a YouTube hook. |
| Open loop generation | Retention loop | Dramatic question and payoff design | Yes | Useful conceptually, wrong default label. |
| Cliffhanger design | Series continuation | Act-button and scene-turn promise | Yes | Good for serialization, not every film scene. |
| Pacing control | Retention risk and platform form factor | Cinematic pacing and act rhythm | Yes | Needs film-native terms. |
| Retention loop design | Analytics-driven retention | Scene momentum and payoff pacing | Yes | Strongly content-specific today. |
| Content calendar planning | Publishing cadence | Release calendar planning | Yes | Downstream only. |
| Platform strategy mapping | Platform metrics | Distribution strategy mapping | Yes | Downstream only. |
| Voice generation | Platform narration and persona consistency | Film narration and dialogue voice direction | Yes | Film mode should preserve performance intent. |
| Visual generation | Platform style constraints | Film visual language concepting | Yes | Reusable with film-mode terminology. |
| Research and fact checking | Evidence support | Film research and source grounding | Yes | Already reusable. |
| Prompt formatting | Generic prompt support | Film prompt package assembly | Yes | Generic infra. |

## 5. Interface to Phase 6 Contracts

Phase 6 should inspect and propose contracts for:

- film route intent
- screenplay structure
- Save the Cat and beat-sheet logic
- three-act and eight-sequence logic
- character arc
- scene dramaturgy
- dialogue subtext
- visual motif
- mise-en-scene and composition
- camera language
- sound motif
- performance direction
- screenplay format
- film validation
- content-vs-film route separation

## 6. Future patch plan

Phase 6 should inspect the runtime contracts that currently enforce prompt generation, route selection, content gates, and output packaging, then determine how to add cinema contracts without breaking the existing content and distribution lanes.

## 7. Non-goals

This phase does not create or patch any subskills yet.

It does not alter routes, skills, contracts, validators, schemas, or runtime behavior.

## Phase 11U Canon/Style Supplement Linkage Addendum

This is a later linkage update and does not rewrite the original Phase 5 finding.
Future film subskills must now align to the supplement pack:

- `FILMCRAFT_CANON_SOURCE_LEDGER.md`
- `CINEMA_STYLE_BIBLE_REQUIREMENTS.md`
- `ANIMATION_CANON_REQUIREMENTS.md`
- `FILM_ROUTE_PLATFORM_SEPARATION_LAW.md`
- `FILM_OUTPUT_STYLE_PALETTE_SCHEMA_REQUIREMENTS.md`
- `REAL_INCIDENT_DOCUDRAMA_ETHICS_REQUIREMENTS.md`

Future film subskills must include canon-aware structure checks, style/palette micro-rules, animation branching, source-vs-render checks, and ethics-aware real-incident handling.
`SCRIPT_GENERATION` remains preserved for content/platform use, and `FILM_SCREENPLAY_GENERATION` remains a parallel future route.
Hook, retention, pacing, and creator-fit micro-behavior may stay in content subskills, but they must not become film-core PASS criteria.
Phase 12 remains blocked until the supplement layer is reviewed.
