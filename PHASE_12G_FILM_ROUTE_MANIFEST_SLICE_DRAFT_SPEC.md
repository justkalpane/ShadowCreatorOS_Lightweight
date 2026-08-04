# Phase 12G Film Route Manifest Slice Draft Spec

## 1. Objective
Define the proposed future `FILM_SCREENPLAY_GENERATION` manifest and slice shape.

## 2. Proposed future files

| Future file | Purpose | Active in Phase 12G? | Required before creation | Risk |
|---|---|---|---|---|
| `registries/route_manifests/film_screenplay_generation.yaml` | Active film route manifest for screenplay generation | Active in Phase 12G? no | Active route prep, collision analysis, regression coverage, owner approval | High until all prep evidence exists |
| `registries/route_slices/film_screenplay_generation.registry_slice.yaml` | Active film route slice for dependency consumption and route scope | Active in Phase 12G? no | Active manifest, dependencies, fixtures, validators, contracts, and selector prep | High until manifest and proofs exist |

## 3. Proposed future route identity
```yaml
route_id: FILM_SCREENPLAY_GENERATION
route_family: cinema_core
route_mode: film_screenplay_generation
preserves_content_route: SCRIPT_GENERATION
downstream_routes:
  - VISUAL_MEDIA_PLAN
  - VOICE_CONTEXT
  - EDITING_PACKAGING
  - MEDIA_FACTORY_HANDOFF
  - FULL_VIDEO_PIPELINE
```

## 4. Proposed future manifest sections
- route identity
- triggers
- non-triggers
- mandatory contracts
- mandatory schemas
- mandatory validators
- directors
- agents
- subagents
- skills
- subskills
- source requirements
- style/canon requirements
- animation mode requirements
- real incident/docudrama requirements
- no-fake-PASS gates
- downstream handoff rules
- output packet requirements
- acceptance gates

## 5. Proposed future slice sections
- slice identity
- consumed contracts
- consumed schemas
- consumed validators
- dependency expansion
- fixture references
- route scope requirements
- proof/lineage requirements
- route collision rules
- downstream allowed routes
- prohibited content-core leakage

## 6. Content preservation rule
`SCRIPT_GENERATION` remains the content/platform script route and must not be replaced.
