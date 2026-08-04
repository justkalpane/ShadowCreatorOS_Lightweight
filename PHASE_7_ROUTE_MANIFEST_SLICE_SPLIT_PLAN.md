# Phase 7 Route Manifest and Route Slice Split Plan

## 1. Objective
Phase 7 audits the route manifest and route slice layer so we can separate cinema-first routing from the existing content-first `SCRIPT_GENERATION` path without breaking the current content engine or downstream media stack. This is still documentation-only. No route files are being patched in this phase.

## 2. Relationship to Phases 1-6
Phase 1 found director-level platform drift.
Phase 2 found agent-level content and platform drift.
Phase 3 found subagent-level hook, trend, and retention drift.
Phase 4 found skill-level content-hook and retention drift plus missing filmcraft skills.
Phase 5 found subskill-level micro-behavior drift plus missing filmcraft subskills.
Phase 6 found contract-layer content bias plus missing film contract families.
Phase 7 now checks whether the route manifests and route slices can cleanly split film mode away from `SCRIPT_GENERATION`.

## 3. Route inventory

| Route | File path | Current role | Cinema-core ready? | Platform/content drift? | Recommended mode split | Patch priority | Notes |
|---|---|---:|---:|---:|---|---:|---|
| `SCRIPT_GENERATION` | `registries/route_manifests/script_generation.yaml` | Core script route | Partial | Yes | Add parallel film route family | P0 | Triggered by YouTube/Shorts/reel/voiceover terms |
| `SCRIPT_GENERATION` slice | `registries/route_slices/script_generation.registry_slice.yaml` | Active script route scope | Partial | Yes | Keep content path, duplicate film path later | P0 | Mandatory skills/subskills are still retention-first |
| `ROUTE_CHAIN_MODE_SELECTOR` | `runtime/state/route_chain_mode_selector.yaml` | Mode-to-route gate | Partial | Yes | Add film mode branch | P0 | Only content routes are currently defined |
| `MEDIA_FACTORY_HANDOFF` | `registries/route_manifests/media_factory_handoff.yaml` | Downstream media handoff | Yes, downstream only | No | Keep downstream | P1 | Strong media support, not screenplay core |
| `visual_media_plan` slice | `registries/route_slices/visual_media_plan.registry_slice.yaml` | Visual planning branch | Yes, downstream only | No | Keep downstream | P1 | Good for adaptation, not film writing |
| `visual_media_generation_draft` slice | `registries/route_slices/visual_media_generation_draft.registry_slice.yaml` | Visual generation draft branch | Yes, downstream only | No | Keep downstream | P1 | Execution-facing media prep |
| `full_video_pipeline` | `registries/route_manifests/full_video_pipeline.yaml` | End-to-end content pipeline | Partial | Yes | Preserve as downstream distribution route | P1 | Still content/video oriented |
| `full_video_pipeline` slice | `registries/route_slices/full_video_pipeline.registry_slice.yaml` | End-to-end pipeline scope | Partial | Yes | Keep downstream | P1 | Includes content orchestration and platform behavior |
| `CONTEXT_ENGINEERING` | `registries/route_manifests/context_engineering.yaml` | Script-to-context bridge | Partial | Yes | Keep as downstream bridge | P2 | Useful after screenplay lock |
| `context_engineering` slice | `registries/route_slices/context_engineering.registry_slice.yaml` | Context bridge scope | Partial | Yes | Keep as downstream bridge | P2 | Voice/image/video/editing context only |
| `VOICE_CONTEXT` | `registries/route_manifests/voice_context.yaml` | Voiceover and narration context | Yes, downstream only | No | Keep downstream | P2 | Narration support, not film core |
| `voice_context` slice | `registries/route_slices/voice_context.registry_slice.yaml` | Voice context scope | Yes, downstream only | No | Keep downstream | P2 | Audio delivery branch |
| `EDITING_PACKAGING` | `registries/route_manifests/editing_packaging.yaml` | Packaging, captions, metadata | Yes, downstream only | No | Keep downstream | P2 | Valid release/support path |
| `editing_packaging` slice | `registries/route_slices/editing_packaging.registry_slice.yaml` | Editing package scope | Yes, downstream only | No | Keep downstream | P2 | Platform packaging and SEO path |
| `SCRIPT_REFINEMENT` | `registries/route_manifests/script_refinement.yaml` | Rewrite/refine content route | Partial | Yes | Keep content mode, mirror film refinement later | P1 | Retention and emotional rhythm logic dominate |
| `script_refinement` slice | `registries/route_slices/script_refinement.registry_slice.yaml` | Refinement route scope | Partial | Yes | Duplicate with film mode later | P1 | Still script/content-centric |
| `TOPIC_DISCOVERY` | `registries/route_manifests/topic_discovery.yaml` | Topic and trend discovery | Partial | Yes | Keep upstream discovery, not film core | P2 | Works as a prewriting helper |
| `topic_discovery` slice | `registries/route_slices/topic_discovery.registry_slice.yaml` | Topic discovery scope | Partial | Yes | Keep upstream | P2 | Good for topic selection only |
| `AVATAR_VIDEO_CONTEXT` | `registries/route_manifests/avatar_video_context.yaml` | Avatar/video context route | Yes, downstream only | No | Keep downstream | P2 | Production/visual handoff, not screenplay core |
| `avatar_video_context` slice | `registries/route_slices/avatar_video_context.registry_slice.yaml` | Avatar/video scope | Yes, downstream only | No | Keep downstream | P2 | Video execution branch |

## 4. Route family classification

### Core film compatible
- `ROUTE_DEPENDENCY_EXPANSION` style route governance
- route state and route scope discipline
- downstream bridge routes that can be reused after screenplay lock

### Content-route only
- `SCRIPT_GENERATION`
- `SCRIPT_REFINEMENT`
- content-focused trigger terms
- hook / re-hook / retention / viral logic

### Downstream distribution only
- `CONTEXT_ENGINEERING`
- `VOICE_CONTEXT`
- `EDITING_PACKAGING`
- `MEDIA_FACTORY_HANDOFF`
- `AVATAR_VIDEO_CONTEXT`
- `full_video_pipeline` as a downstream production route

### Needs film mirror
- `SCRIPT_GENERATION`
- `SCRIPT_REFINEMENT`
- `SCRIPT_GENERATION` slice
- `SCRIPT_REFINEMENT` slice
- `full_video_pipeline` slice only where it carries content-first defaults

## 5. Film-core route requirements
The route layer still does not contain a dedicated cinema-first route family. The missing route family should own:
- film route intent
- screenplay generation
- film story development
- cinematic director plan
- feature film production pipeline
- film release distribution
- route separation between film and content modes

## 6. Non-goals
Phase 7 does not patch any route manifest or route slice yet.
Phase 7 does not add `FILM_SCREENPLAY_GENERATION` yet.
Phase 7 does not change the current content engine or downstream media stack.

