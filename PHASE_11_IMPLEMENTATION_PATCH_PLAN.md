# Phase 11 Implementation Patch Plan

## Objective

Phase 11 converts the full audit chain into a safe implementation order.
The goal is to introduce cinema-first filmmaking support without breaking the existing
content-first engine, downstream media routes, or the governance spine.

This is a staged patch plan only. It does not implement code.

## Audit chain summary

The implementation plan is based on the completed audit chain:

1. Phase 1: Directors
2. Phase 2: Agents
3. Phase 3: Subagents
4. Phase 4: Skills
5. Phase 5: Subskills
6. Phase 6: Runtime Contracts
7. Phase 7: Route Manifests and Route Slices
8. Phase 8: Validators
9. Phase 9: Schemas
10. Phase 10: Test Fixtures

Across those phases, the repo was found to be strong in governance and downstream media support, while the screenplay core remained content-first. Phase 11 turns that audit into an implementation sequence.

## Core design rule

Preserve the current `SCRIPT_GENERATION` / content engine.
Add a parallel cinema-first route family.
Move platform adaptation, packaging, and release logic downstream.
Do not allow downstream logic to control core screenplay generation.

## Required sequencing

The safe order is:

1. Film schemas
2. Film contracts
3. Film validators
4. Film route manifests and slices
5. Fixture and acceptance wiring
6. Implementation patches

This sequence keeps data shape, legal rules, and validation ahead of route behavior.

## Minimal viable implementation slice

The smallest safe first slice is:

1. Film route state schema
2. Film screenplay output packet schema
3. Film route intent contract
4. Film screenplay structure contract
5. Film route selection validator
6. Film screenplay packet validator
7. Film route manifest entry
8. Film route slice entry

This minimal slice proves the cinema-first route can exist without displacing `SCRIPT_GENERATION`.

## Full implementation roadmap

After the minimal slice lands, expand in this order:

1. Character and scene family
2. Dialogue and subtext family
3. Visual language and composition family
4. Sound and performance family
5. Downstream handoff family
6. Film validation scorecard family
7. Wiring of directors, agents, subagents, skills, and subskills
8. Fixture-backed acceptance coverage
9. Runtime integration hardening

## Patch phases

### Patch Unit 1: Film schema family

Create cinema-first schemas for:

- route state capsule
- screenplay output packet
- source ledger and fact map
- beat sheet and structure maps
- character arc and web
- scene dramaturgy
- dialogue subtext
- visual motif and image system
- mise-en-scene, blocking, composition
- camera language
- sound motif and performance
- screenplay format status
- downstream handoff
- validation scorecard
- no-fake-pass gate

Dependency: none beyond the current governance spine.

### Patch Unit 2: Film contract family

Create contracts that define the legal meaning of the film packet:

- film route intent
- screenplay structure
- Save the Cat and alternate canon mappings
- three-act and eight-sequence mappings
- character arc and opposing force
- scene dramaturgy
- dialogue subtext
- visual language
- directorial style
- performance direction
- screenplay format
- film validation
- route separation between content and film

Dependency: film schemas must exist first.

### Patch Unit 3: Film validator family

Create validators that can reject fake film PASS states.
They must distinguish:

- content-mode script packets
- cinematic screenplay packets
- downstream adaptation packets
- incomplete film packets
- unsupported claims about runtime proof

Dependency: film contracts and schemas must exist first.

### Patch Unit 4: Film route manifests and slices

Add route manifests and slices for:

- `FILM_SCREENPLAY_GENERATION`
- `FILM_STORY_DEVELOPMENT`
- `CINEMATIC_DIRECTOR_PLAN`
- `FEATURE_FILM_PRODUCTION_PIPELINE`
- `FILM_RELEASE_DISTRIBUTION`

Keep `SCRIPT_GENERATION` intact for content-first work.
Do not collapse film and content routes into a single default route.

Dependency: validators and contracts should already define the split.

### Patch Unit 5: Fixture wiring

Convert Phase 10 fixtures into the first acceptance harness for the new route split.
Use them to verify:

- route selection
- packet completeness
- content preservation
- downstream handoff
- no-fake-pass rejection

Dependency: route, contract, and validator layers must already exist.

### Patch Unit 6: Implementation patches

Only after the above layers exist should actual implementation changes be applied to:

- routing logic
- director consumption
- agent/subagent consumption
- skill/subskill selection
- schema serialization
- validator enforcement

This is the first point where runtime behavior may change.

## Non-goals

Phase 11 does not:

- remove the current content engine
- delete YouTube or social distribution behavior
- claim governed runtime proof
- claim completion certificates
- create executable tests yet
- create `FILM_SCREENPLAY_GENERATION` yet
- rewrite the whole repo at once

## Implementation constraints

- Do not convert the content engine into the film engine.
- Do not hide film logic inside content routes.
- Do not add runtime behavior before the schema, contract, and validator layers exist.
- Do not loosen the current downstream adaptation stack.
- Do not claim PASS without validator and schema support.

## Implementation guardrails

- Every patch unit must preserve existing downstream behavior unless a later unit explicitly changes it.
- Every new film artifact must be parallel to, not hidden inside, the content engine.
- Validators must fail closed when a film packet is incomplete.
- Route changes must remain explainable from the audit chain.

## Rollout principle

Implement the smallest safe film-first layer first, then expand outward.
The governance spine is reusable.
The content engine is reusable.
The new film route family is additive.
