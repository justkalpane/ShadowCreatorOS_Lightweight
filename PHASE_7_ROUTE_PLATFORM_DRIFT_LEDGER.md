# Phase 7 Route Platform Drift Ledger

| Route/File | Line or evidence reference | Term/finding | Current context | Classification | Reason | Proposed film-mode equivalent | Keep downstream? | Risk if ignored |
|---|---|---|---|---|---|---|---|---|
| `registries/route_manifests/script_generation.yaml` | 1-24 | `SCRIPT_GENERATION` route name, allowed modes, and trigger terms are all script/content-first | Root script route | REPLACE | The route is explicitly anchored to YouTube/Shorts/reel/voiceover | `FILM_SCREENPLAY_GENERATION` route family | No | Film prompts will continue to be routed as creator scripts |
| `registries/route_manifests/script_generation.yaml` | 43-58 | Mandatory contracts include content engineering, story engine, language control, research, and timed beat map | Content-script governance stack | REPLACE | Contracts still encode content cadence and retention logic | Film screenplay contract family | No | Film writing will be judged by content cadence laws |
| `registries/route_manifests/script_generation.yaml` | 92-111 | Mandatory skills/subskills are hook, retention, pacing, cliffhanger, and content angle oriented | Content optimization stack | REPLACE | The core route still prefers creator-retention mechanics | Film craft skill family | No | Film route will inherit hook-first behavior |
| `registries/route_manifests/script_generation.yaml` | 113-124 | Required output blocks include hook, cadence, scorecards, influence maps, and Bengaluru hardening | Script-content proof stack | REPLACE | Output proof is still built around content generation | Film screenplay output packet | No | Screenplay output will remain content proof shaped |
| `registries/route_slices/script_generation.registry_slice.yaml` | 5-44 | Directors, agents, subagents, skills, subskills are the content-oriented lineage | Script route scope | REPLACE | The slice is the actual executable scope for content scripts | Film route slice equivalent | No | A new film route would still point into content-first components |
| `runtime/state/route_chain_mode_selector.yaml` | 5-24 | `script_only` only allows `SCRIPT_GENERATION` and blocks media branches until after final script | Route gate | KEEP | Strong separation is already present | Reuse as a new film selector branch | Yes | Good guardrail, but no film branch exists |
| `runtime/state/route_chain_mode_selector.yaml` | 26-42 | `script_plus_visual_plan` adds `MEDIA_FACTORY_HANDOFF` after final script | Downstream visual branch | KEEP | Valid downstream support, not film-core routing | Reuse as post-film adaptation branch | Yes | This should stay downstream of film writing |
| `runtime/state/route_chain_mode_selector.yaml` | 44-62 | `script_plus_visual_generation_draft` bundles voice/image/video/media batch plans | Content-to-media handoff | MOVE | Useful after screenplay lock, not during screenplay generation | Film media-adaptation branch | Yes | Media bundle logic should not become screenplay authority |
| `runtime/state/route_chain_mode_selector.yaml` | 64-77 | `script_plus_media_factory_handoff` depends on `SCENE_SYNC_MATRIX` and production proof | Downstream production handoff | KEEP | Good downstream execution gate | Film release/adaptation handoff | Yes | Safe to preserve as a downstream lane |
| `runtime/state/route_chain_mode_selector.yaml` | 79-96 | `full_content_packet` still belongs to script/content plus context and packaging | Content packet route | REPLACE | It is broad but still content-centered | Film full packet family | Yes, downstream only | Broad content packets can swallow a film prompt |
| `registries/route_manifests/media_factory_handoff.yaml` | 1-16 | Trigger terms and mandatory components are storyboard, B-roll, render packet, and visual generation | Media handoff route | KEEP | Valid downstream media-production route | Film adaptation output branch | Yes | Should not be promoted into film screenplay core |
| `registries/route_manifests/media_factory_handoff.yaml` | 17-28 | Depth branches define visual plan, final draft, and generator draft | Media production depth lanes | KEEP | Strong downstream branching discipline | Reuse after screenplay lock | Yes | Good model for route layering, not screenplay logic |
| `registries/route_slices/visual_media_plan.registry_slice.yaml` | 1-20 | Visual plan scope is route_id `MEDIA_FACTORY_HANDOFF` with visual directors/agents | Visual planning branch | KEEP | Explicitly downstream | Film adaptation branch | Yes | Fine as a post-script route |
| `registries/route_slices/visual_media_plan.registry_slice.yaml` | 21-57 | Required skills and output contracts are shot list, b-roll, storyboard, visual asset planning | Visual production branch | KEEP | Useful after screenplay exists | Film visual handoff equivalent | Yes | Safe downstream support |
| `registries/route_slices/visual_media_generation_draft.registry_slice.yaml` | 1-20 | Draft branch adds media output bundle, voice/image/video batch plans | Execution-facing media draft | KEEP | Still downstream execution | Film visual execution branch | Yes | Needs screenplay input, not screenplay authority |
| `registries/route_slices/full_video_pipeline.registry_slice.yaml` | 1-39 | Full pipeline includes content/operations skills and broader output scopes | End-to-end pipeline | REPLACE | The route is still content production heavy | Film production pipeline route | Yes, downstream only | Film core would be misrouted into content operations |
| `registries/route_manifests/context_engineering.yaml` | 1-13, 36-49 | Context engineering is script-to-context conversion with voice/image/video/editing outputs | Downstream bridge route | MOVE | Useful after screenplay lock | Film context bridge | Yes | Good bridge, wrong place for screenplay generation |
| `registries/route_slices/context_engineering.registry_slice.yaml` | 1-13, 41-59 | Context bridge includes asset briefs, voice/video/image packets, provider boundary | Downstream bridge scope | MOVE | Useful as adaptation layer | Film context bridge | Yes | Keep downstream |
| `registries/route_manifests/editing_packaging.yaml` | 1-24 | Editing, captions, thumbnail, title, description, hashtags, platform packaging | Release/distribution route | KEEP | Valid downstream distribution logic | Film release distribution | Yes | Should stay downstream |
| `registries/route_slices/editing_packaging.registry_slice.yaml` | 1-34, 49-56 | Platform metadata and SEO-specific skills/blocks | Release/distribution route | KEEP | Good for packaging and publication | Film release distribution | Yes | Do not move into screenplay core |
| `registries/route_manifests/voice_context.yaml` | 1-24 | Voice generation and SSML context | Audio delivery route | KEEP | Downstream narration support | Film voice handoff | Yes | Safe to preserve downstream |
| `registries/route_slices/voice_context.registry_slice.yaml` | 1-44 | Voice skills and output blocks are provider-bounded | Audio delivery route | KEEP | Strong voice handoff lane | Film voice handoff | Yes | Not screenplay core |
| `registries/route_manifests/script_refinement.yaml` | 1-24 | Rewrite, make it emotional, make it viral, make it cinematic | Content refinement route | REPLACE | “viral” and “retention” remain the center of gravity | Film script refinement route | No | This route can drag film writing back into platform cadence |
| `registries/route_slices/script_refinement.registry_slice.yaml` | 1-24, 41-56 | Hook structure audit, clarity, emotional rhythm, re-hook system | Content refinement scope | REPLACE | Script rewrite path still depends on retention mechanics | Film refinement slice | No | Film scenes would be optimized like YouTube hooks |
| `registries/route_manifests/topic_discovery.yaml` | 1-13, 52-63 | Trending topic and viral idea discovery with source research | Prewriting discovery | MOVE | Useful upstream, but not film core | Film story discovery route | Yes, upstream only | Keep as topic intelligence, not screenplay authority |
| `registries/route_slices/topic_discovery.registry_slice.yaml` | 1-21, 40-73 | Trend scanners, topic viability, deep research, fact verification | Discovery route | MOVE | Best as upstream research | Film story discovery slice | Yes, upstream only | Safe if not used as screenplay engine |
| `registries/route_manifests/avatar_video_context.yaml` | 1-24 | Avatar/video prompt terms and provider boundary | Video execution route | KEEP | Valid downstream production support | Film avatar/video adaptation branch | Yes | Not film screenplay core |
| `registries/route_slices/avatar_video_context.registry_slice.yaml` | 1-45, 56-72 | Video prompt and image/video context packets | Video execution route | KEEP | Good downstream media lane | Film adaptation branch | Yes | Do not use as screenplay route |

## Route drift summary
- KEEP: 9
- REFACTOR: 0
- MOVE: 5
- REPLACE: 6
- DUPLICATE: 0
- DELETE: 0
- NEEDS_DESIGN_DECISION: 0
- MISSING_FILM_ROUTE: 16
- REGISTRY_FILE_MISMATCH: 0 observed in this audit set
- READ_BLOCKED: 0

## Highest-risk drift pattern
The highest-risk drift is that the current route family uses content-retention logic and platform-specific sequencing as the root route for any script request. That is fine for creator scripts, but it is the wrong default for short-film and feature-film prompts.

## Film-mode equivalent direction
The film-mode route should be a parallel family, not a replacement of the current content stack. It should own screenplay intent, structure, character arc, scene dramaturgy, and production-ready cinematic outputs, while the existing routes continue to serve downstream visual, voice, editing, and distribution work.

