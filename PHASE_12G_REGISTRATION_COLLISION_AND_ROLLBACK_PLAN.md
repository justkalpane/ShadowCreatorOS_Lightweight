# Phase 12G Registration Collision and Rollback Plan

## 1. Objective
Identify collision risks and rollback strategy before active route registration.

## 2. Collision risk table

| Risk ID | Collision risk | Affected surface | Why it matters | Mitigation | Must be tested before binding? |
|---|---|---|---|---|---|
| C-12G-01 | Short film prompt routed to content script | Route selector and trigger terms | Film prompts must not be flattened into content scripting | Preserve screenplay intent rules and route-intent precedence | Yes |
| C-12G-02 | YouTube script prompt routed to film route | Route selector and content trigger terms | Content tasks should keep `SCRIPT_GENERATION` | Require explicit screenplay intent for film routing | Yes |
| C-12G-03 | Cinematic explainer ambiguity | Route selector / manifest triggers | Cinematic style does not always mean screenplay route | Distinguish style from route intent | Yes |
| C-12G-04 | Trailer prompt incorrectly routed to film core instead of downstream packaging | Downstream handoff routing | Trailer work is not screenplay generation | Keep trailer/teaser packaging downstream-only | Yes |
| C-12G-05 | Full video pipeline prompt incorrectly treated as screenplay | Route selector | Production pipeline is not screenplay intent | Preserve downstream pipeline route family | Yes |
| C-12G-06 | Route selector uses content mode defaults | Selector baseline | Default routing still favors `script_only` | Add a film branch only after registration prep | Yes |
| C-12G-07 | Content validators used for film packet | Validation layer | Content PASS cannot stand in for film validation | Bind film validators separately before any PASS claims | Yes |
| C-12G-08 | Film schemas treated as enforced before validators are bound | Schema/validation boundary | Skeleton schemas should not imply enforcement | Keep schemas as prep artifacts until binding phase | Yes |
| C-12G-09 | Route manifest active without slice | Manifest/slice lifecycle | Active manifests without slices create partial route scope | Require pairwise registration and dependency checks | Yes |
| C-12G-10 | Slice active without manifest | Manifest/slice lifecycle | Slice-only activation creates undefined route scope | Require manifest-first registration gating | Yes |
| C-12G-11 | No-fake-PASS gaps | Proof boundary | False approval becomes easy if proof gates are skipped | Require explicit no-fake-PASS evidence and rollback path | Yes |
| C-12G-12 | Real incident film without source ledger | Source/ethics boundary | Fact claims need source discipline | Require source ledger and fact-vs-anecdote separation | Yes |
| C-12G-13 | Animation film without animation style bible | Style/canon boundary | Animation defaults can silently drift into live-action assumptions | Require animation style bible and motion-canon evidence | Yes |

## 3. Rollback plan
- delete or revert film manifest/slice files
- revert route selector change
- keep fixtures/schemas/validators/contracts as harmless prep artifacts if unbound
- restore previous route selector behavior
- run content preservation fixtures/tests

## 4. Phase 12H readiness gate
`Phase 12H: inactive film route manifest/slice draft files only`

This is the next safe step only if Phase 12G stays preparation-only and the registration prep evidence remains intact.
