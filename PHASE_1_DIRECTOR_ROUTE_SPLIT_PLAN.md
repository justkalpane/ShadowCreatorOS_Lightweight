# Phase 1 Director + Route Split Plan

## Objective

Phase 1 exists to split cinema-first screenplay generation away from the current YouTube/content-first `SCRIPT_GENERATION` path, while preserving the existing content engine and all downstream distribution layers.

This phase is intentionally narrow. It does **not** rewrite the whole repo. It creates a clean architectural seam so film prompts can be routed into a cinema-first core without breaking the current creator/content stack.

## Source Grounding

This plan is grounded in the current route manifest and route slice for `SCRIPT_GENERATION`:

- `registries/route_manifests/script_generation.yaml:1-25`
- `registries/route_manifests/script_generation.yaml:43-124`
- `registries/route_manifests/script_generation.yaml:139-207`
- `registries/route_slices/script_generation.registry_slice.yaml:1-60`

Those files still define `SCRIPT_GENERATION` as the canonical route, with trigger terms like `YouTube script`, `Shorts script`, `reel script`, and `voiceover script`, plus recurring-hook and retention rules that are explicitly YouTube-oriented.

## Architecture Decision

### Recommended default: Option A

**Option A: Add a new `FILM_SCREENPLAY_GENERATION` route in parallel.**

This is the safest and most reviewable approach because it:

- preserves existing `SCRIPT_GENERATION` behavior
- avoids destructive rewrite of proven creator/content routes
- makes the cinema-first contract explicit
- gives reviewers a separate route boundary to validate
- reduces regression risk in downstream packaging and distribution

### Why not Option B first

Replacing `SCRIPT_GENERATION` default behavior would be too risky in Phase 1 because the current route still powers valid YouTube/content workflows, recurring hooks, and platform packaging. Removing that behavior before the film path is proven would create avoidable drift.

### Why not Option C first

Mode separation inside `SCRIPT_GENERATION` can become a later refinement, but it is too easy to blur the boundary in a first pass. Phase 1 needs a crisp architectural split, not a hidden fork inside one overloaded route.

## Route Boundary

### Film-core route should own

- short film
- screenplay
- film script
- cinematic script
- feature film
- shooting script
- scene script
- director’s script
- narrative film
- character-driven film
- dramatic short

### Existing script/content route should retain

- YouTube script
- Shorts script
- reels script
- voiceover script
- creator video
- explainer video
- social video
- retention-optimized video
- platform-first content

### Downstream routes should retain

- trailer adaptation
- teaser cutdowns
- YouTube trailer
- Instagram promo
- TikTok cutdown
- metadata
- packaging
- release distribution
- platform analytics

## Required Director Mode Separation

The Phase 1 director boundary should be explicit for each major director family.

| Director | Current behavior | Film-mode responsibility | Content/social-mode responsibility | Downstream distribution responsibility | Repo path | Patch risk |
|---|---|---|---|---|---|---|
| Krishna | Core script orchestration still leans on `SCRIPT_GENERATION`, recurring hooks, and YouTube-specific cadence | Become the entry director for cinema-first screenplay routing and story authority | Keep current content-script routing for YouTube/creator work | None directly; downstream only | `directors/supreme_vision/krishna.md` | High |
| Shakti | Amplifies engagement, audience force, viral velocity | Recast as emotional-force amplification for dramatic tension, not just virality | Preserve engagement support for creator work | None directly | `directors/supreme_vision/shakti.md` | High |
| Chanakya | Creator fit / platform fit / viral or monetization goals | Replace with film opportunity scoring and story-market fit | Keep audience-fit support for creator packaging | None directly | `directors/strategy/chanakya.md` | High |
| Narada | Trend, platform analytics, distribution optimization | Move trend signals into film research intake only | Keep platform/distribution intelligence for creator routes | Owns distribution signal intake | `directors/strategy/narada.md` | High |
| Vishnu | Cross-platform sync and resilience | Add a film-mode sync layer for screenplay, scene, and production continuity | Preserve fallback orchestration for content workflows | Keep platform resilience logic downstream | `directors/supreme_vision/vishnu.md` | Medium |
| Saraswati | Audience expansion and multi-channel repurposing | Keep as downstream adaptation and release packaging, not screenplay core | Preserve channel adaptation and content multiplication | Yes, this is a downstream owner | `directors/distribution/saraswati.md` | Low |
| Garuda | Rapid publishing and multi-platform deployment | Keep as downstream distribution dispatcher | Preserve publication velocity logic | Yes, downstream only | `directors/cinematic/garuda.md` | Low |
| Varuna | Format adaptation, audience segment flow | Add film-format adaptation and delivery rhythm checks | Preserve platform-format constraints for content routes | Yes, downstream or adapter layer | `directors/cinematic/varuna.md` | Medium |
| Maya | Visual style / creator brand alignment | Become film visual-discipline support | Preserve creator visual brand support | Only after core film packet exists | `directors/production/maya.md` | Low |
| Vishwakarma | Production coordination and asset build support | Support film production packet generation | Preserve current production fabrication roles | Downstream production only | `directors/production/vishwakarma.md` | Low |
| Nataraja | Pacing and editing consistency | Convert pacing into scene rhythm, shot rhythm, and cut rhythm | Preserve content pacing support | Downstream finishing support | `directors/cinematic/nataraja.md` | Medium |
| Tumburu | Voice and audio style alignment | Support cinematic sound motif and performance texture | Preserve voiceover/audio support for content routes | Downstream audio shaping | `directors/production/tumburu.md` | Low |
| Arjuna | Production execution and scoring | Support shoot-planning and execution control | Preserve existing production scoring | Downstream production support | `directors/production/arjuna.md` | Low |
| Agni | Trend acceleration and speed decisions | Recast as urgency / opportunity scoring for film development, not trend-chasing | Preserve fast-track content when explicitly asked | Downstream content acceleration only | `directors/production/agni.md` | Medium |
| Indra | Premium distribution / high-value audience conversion | Support premium finish and release readiness | Preserve premium finishing for content | Downstream finishing/distribution | `directors/cinematic/indra.md` | Low |

## Non-goals

Phase 1 does **not**:

- delete the old YouTube route
- rewrite all skills
- rewrite all contracts
- patch validators
- patch schemas
- run governed runtime
- claim completion certificate
- remove downstream distribution behavior that is currently valid

## Proposed Next Phases

1. Phase 2: Agents
2. Phase 3: Subagents
3. Phase 4: Skills
4. Phase 5: Subskills
5. Phase 6: Runtime contracts
6. Phase 7: Route manifests and route slices
7. Phase 8: Validators
8. Phase 9: Output schemas
9. Phase 10: NEET short-film test fixture

## Phase 1 Exit Criteria

This phase is complete when:

- the film route boundary is documented
- the director drift map is explicit
- the current content route remains intact
- the downstream routes are preserved
- the next patch phase can safely begin from a film-first design

