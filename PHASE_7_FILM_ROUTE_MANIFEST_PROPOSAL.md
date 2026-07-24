# Phase 7 Film Route Manifest Proposal

## 1. Proposed film route families
```text
registries/route_manifests/film_screenplay_generation.yaml
registries/route_slices/film_screenplay_generation.registry_slice.yaml
registries/route_manifests/film_story_development.yaml
registries/route_slices/film_story_development.registry_slice.yaml
registries/route_manifests/cinematic_director_plan.yaml
registries/route_slices/cinematic_director_plan.registry_slice.yaml
registries/route_manifests/feature_film_production_pipeline.yaml
registries/route_slices/feature_film_production_pipeline.registry_slice.yaml
registries/route_manifests/film_release_distribution.yaml
registries/route_slices/film_release_distribution.registry_slice.yaml
```

## 2. Proposed film route triggers
```text
short film
screenplay
film script
cinematic script
feature film
shooting script
scene script
director's script
narrative film
cinematic screenplay
dramatic short
character-driven film
film story
story development
director plan
production pipeline
release distribution
```

## 3. Reuse map

| Existing route/family | Current bias | Film-mode use | Downstream retained? | Recommendation |
|---|---|---|---|---|
| `SCRIPT_GENERATION` | YouTube/content-first | Use as content route only | Yes | Reuse as-is for content mode |
| `SCRIPT_REFINEMENT` | Hook/retention refinement | Create film refinement twin later | Yes | Duplicate for film mode |
| `CONTEXT_ENGINEERING` | Script-to-media context bridge | Use after screenplay lock | Yes | Move downstream |
| `VOICE_CONTEXT` | Narration/audio context | Use after screenplay lock | Yes | Move downstream |
| `EDITING_PACKAGING` | Platform packaging/release | Use after screenplay lock | Yes | Move downstream |
| `MEDIA_FACTORY_HANDOFF` | Visual production handoff | Use after screenplay lock | Yes | Move downstream |
| `AVATAR_VIDEO_CONTEXT` | Video/renderer context | Use after screenplay lock | Yes | Move downstream |
| `FULL_VIDEO_PIPELINE` | End-to-end content production | Keep as downstream production route | Yes | Reuse with film mode only after screenplay is done |
| `TOPIC_DISCOVERY` | Trend/topic discovery | Use as upstream research only | Yes | Reuse as upstream discovery |

## 4. Old-to-new responsibility map

| Existing route responsibility | Current bias | Film-mode replacement | Downstream retained? | Notes |
|---|---|---|---|---|
| Script generation for YouTube/Shorts/reels | Platform/content-first | `FILM_SCREENPLAY_GENERATION` | Yes, content route remains | Film prompts need a separate root route |
| Hook, re-hook, retention cadence | Creator optimization | Scene escalation and act/sequence pacing | Yes | Keep only in content mode |
| Script refinement for viral/emotional rewrite | Content rewrite | Film script refinement and dramaturgy | Yes | Duplicate into film mode |
| Script-to-context output | Media prep bridge | Film context handoff | Yes | Downstream only |
| Voice/video/editing packaging | Platform release prep | Film release-adaptation handoff | Yes | Downstream only |

## 5. Missing film route capability check
The audited route layer does not yet contain dedicated route artifacts for:
- film route intent
- film screenplay generation
- film story development
- cinematic director plan
- feature film production pipeline
- film release distribution
- film-vs-content separation
- screenplay structure route
- beat sheet route
- character arc route
- scene dramaturgy route
- dialogue subtext route
- visual motif route
- blocking / composition route
- camera language route
- sound motif route
- performance direction route
- film validation route

## 6. Interface to Phase 8 validators
Phase 8 should inspect and propose validators for:
- film route selection
- screenplay structure output
- beat sheet output
- character arc output
- scene dramaturgy output
- dialogue subtext output
- visual motif output
- composition / blocking output
- camera language output
- sound motif output
- performance direction output
- film validation scorecard
- route separation between content and film
- no-bypass route proof

## 7. Future patch plan
Phase 8 should inspect validator coverage only after the film route manifests and slices are defined. The validator layer is where the future film route gets guarded against fake PASS claims, but that guardrail should be built on top of a clear route split, not before it.

