# Phase 12I Route Collision Review

## 1. Objective
Review likely collisions before any active film route registration or selector binding.

## 2. Active surfaces inspected

| Active surface | Inspected? | Collision relevance | Notes |
|---|---:|---|---|
| `runtime/state/route_chain_mode_selector.yaml` | Yes | High | Default routing still centers `script_only` / `SCRIPT_GENERATION` |
| `registries/route_manifests/script_generation.yaml` | Yes | High | Content trigger terms still route here today |
| `registries/route_slices/script_generation.registry_slice.yaml` | Yes | High | Content scope and enforcement contracts remain content-oriented |
| `registries/route_manifests/full_video_pipeline.yaml` | Yes | Medium | Downstream pipeline route must stay downstream |
| `registries/route_slices/full_video_pipeline.registry_slice.yaml` | Yes | Medium | Pipeline should not be mistaken for screenplay routing |
| `registries/route_manifests/media_factory_handoff.yaml` | Yes | Medium | Packaging/handoff remains a separate downstream family |
| `registries/route_slices/media_factory_handoff.registry_slice.yaml` | Yes | Medium | Handoff scope must not absorb film-core screenplay intent |

## 3. Collision table

| Collision ID | Scenario | Current expected route | Future desired behavior | Risk level | Required fixture/schema/validator support | Activation blocker? |
|---|---|---|---|---|---|---|
| C-12I-01 | Short film prompt routed to content script | `SCRIPT_GENERATION` today for existing content phrasing; future film route only for explicit screenplay intent | `FILM_SCREENPLAY_GENERATION` later, when active | High | Route-selection fixtures + route selector branch + film route validator | Yes |
| C-12I-02 | YouTube script prompt routed to film route | `SCRIPT_GENERATION` | Stay on content route | High | Content-preservation fixtures + selector precedence rules | Yes |
| C-12I-03 | Instagram reel prompt routed to film route | `SCRIPT_GENERATION` | Stay on content/social route | High | Content-preservation fixtures + route classification rules | Yes |
| C-12I-04 | Voiceover script prompt routed to film route | `SCRIPT_GENERATION` | Stay on content route | High | Content-preservation fixtures + route classification rules | Yes |
| C-12I-05 | Cinematic explainer for YouTube is ambiguous | `SCRIPT_GENERATION` | Stay content route unless explicit screenplay request appears | Medium | Ambiguity fixtures + explicit intent handling | Yes |
| C-12I-06 | Trailer prompt routed to film core instead of downstream packaging | Downstream route family, not screenplay core | Keep trailer/teaser packaging downstream-only | High | Downstream handoff fixtures | Yes |
| C-12I-07 | Thumbnail/title prompt routed to film core | Downstream packaging route family | Keep packaging downstream-only | High | Downstream handoff fixtures | Yes |
| C-12I-08 | Full video pipeline prompt treated as screenplay | `FULL_VIDEO_PIPELINE` / downstream production family | Keep pipeline separate from screenplay intent | High | Downstream pipeline fixtures + route family gating | Yes |
| C-12I-09 | Content validators reused for film packet | Content validation only | Film validators must be separate and later bound | High | Film validator skeletons + no-fake-PASS fixtures | Yes |
| C-12I-10 | Film schemas treated as active enforcement before binding | Skeleton-only prep today | No enforcement until later activation | High | Schema skeletons + activation gate | Yes |
| C-12I-11 | Draft manifest without active slice | Inactive draft only | Pair active manifest and slice later | High | Active registration prep docs | Yes |
| C-12I-12 | Draft slice without active manifest | Inactive draft only | Pair active manifest and slice later | High | Active registration prep docs | Yes |
| C-12I-13 | Route selector defaults override film intent | `script_only` default still active | Selector branch later, after readiness | High | Selector integration plan + regression fixtures | Yes |
| C-12I-14 | Real incident film without source ledger | Blocked by source ethics later | Require source ledger and fact-vs-anecdote separation | High | Source ledger fixtures/schema/validator support | Yes |
| C-12I-15 | Animation film without animation style bible | Blocked by style prep later | Require animation canon/style support | Medium | Animation style schema/validator support | Yes |
| C-12I-16 | No-fake-PASS gaps | None of the current prep artifacts claims PASS | Keep proof gates explicit and later executable | High | No-fake-PASS fixtures + validators + contracts | Yes |

## 4. Content preservation conclusion
`SCRIPT_GENERATION` preservation remains protected by the draft plan. The active content route still owns YouTube, Shorts, reel, voiceover, and similar content wording, while the film route stays future-only and explicitly parallel.

## 5. Collision verdict
`COLLISION_REVIEW_PASS_FOR_INACTIVE_DRAFT`

