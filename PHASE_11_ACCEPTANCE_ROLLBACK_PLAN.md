# Phase 11 Acceptance Rollback Plan

This document defines the rollback logic for the first implementation phase after the audits.
It is intentionally conservative.

## Acceptance philosophy

Phase 11 should only be considered successful if the new film-first layers can exist in parallel with the current content engine.
Success means:

- the film route is real
- the content route still works
- downstream adaptation still works
- fake film PASS states are blocked
- no invented runtime proof is claimed

## Proof boundary

The following are not enough on their own:

- repository inspection
- documentation completion
- route labels without validators
- validator names without film packet fields
- content-route success used as proof of film-route success
- downstream media success used as proof of screenplay success

The film route must be proved with film-specific schema and validation support.

## Acceptance gates

### Gate A: Schema gate

The film packet shape must be expressible.
If the schema cannot represent the required film fields, stop before validators or routes are wired.

### Gate B: Contract gate

The repo must clearly distinguish:

- content script behavior
- cinema screenplay behavior
- downstream adaptation behavior

If the distinction is unclear, stop before route work.

### Gate C: Validator gate

The film validators must reject:

- missing beat sheets
- missing character arc / scene structure
- content packets pretending to be film packets
- unsupported claims of PASS

If validators are not fail-closed, stop.

### Gate D: Route gate

`FILM_SCREENPLAY_GENERATION` and its companion route family must be selectable without replacing `SCRIPT_GENERATION`.

If the route split would break content routing, stop.

### Gate E: Wiring gate

Directors, agents, subagents, skills, and subskills must be consumed in the correct mode.
If the wiring still behaves as content-only for film prompts, stop and inspect the route split.

### Gate F: Fixture gate

The Phase 10 fixture matrix must cover:

- route selection
- film packet validation
- content preservation
- downstream handoff
- no-fake-PASS rejection

If fixture coverage is incomplete, stop before implementation patches.

## Required future test cases

The next implementation phase should eventually cover these cases:

- canonical film prompt routes to the film route
- canonical YouTube prompt remains in the content route
- trailer request goes downstream, not into screenplay generation
- incomplete film packet fails
- content packet pretending to be film packet fails
- source-bound film claim requires source-ledger support
- no-fake-PASS gate blocks invented runtime proof
- downstream handoff remains intact after film route introduction
- film route cannot silently replace `SCRIPT_GENERATION`
- regression check for preserved downstream visual/voice/editing routes

## Rollback rules

If any acceptance gate fails, rollback only the newest affected unit.

Rollback order:

1. Remove implementation wiring
2. Remove route additions
3. Remove validator additions
4. Remove contract additions
5. Remove schema additions

Do not touch unrelated repository work.
Do not remove the content engine unless it is directly implicated.

## What must not be rolled back lightly

The following are reusable and should be preserved unless they are the direct cause of failure:

- route state discipline
- route dependency expansion
- source honesty / evidence discipline
- no-fake-pass governance
- downstream media pipeline
- visual planning stack
- voice context stack
- editing and packaging stack

These are part of the long-term architecture.

## Failure classification

When a gate fails, classify the issue as one of:

- missing schema
- missing contract
- missing validator
- route collision
- wiring drift
- content-vs-film ambiguity
- downstream regression
- invented proof risk

This keeps rollback decisions readable and avoids overcorrecting.

## Safe recovery sequence

If the film route fails during implementation:

1. Freeze the broken unit
2. Revert only the last film-specific patch
3. Re-check whether the content engine still works
4. Re-check the route manifests and slices
5. Re-check the validators
6. Resume only after the film/data boundary is clean again

## No-go conditions

Do not continue implementation if any of the following are true:

- the film packet cannot be represented
- the film route collides with content routing
- validators can pass incomplete film packets
- the content engine becomes unavailable
- downstream media routes are broken
- proof is invented instead of measured

## Go / no-go checklist

### Go

- Phase 11 docs are complete
- patch units are clearly ordered
- minimum viable film slice is defined
- acceptance gates are explicit
- rollback order is clear

### No-go

- missing schema plan
- missing contract plan
- missing validator plan
- unclear route split
- incomplete fixture coverage
- any claim of PASS without film validation support

## Final safety statement

Phase 11 is a bridge from audit to implementation, not a leap.
The safest path is to add the film-first layer one boundary at a time and preserve the existing content and downstream systems throughout.
