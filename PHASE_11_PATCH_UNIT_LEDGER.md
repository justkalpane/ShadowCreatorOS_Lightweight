# Phase 11 Patch Unit Ledger

This ledger turns the audit findings into discrete implementation units.
It is a planning artifact only.

| Patch Unit | Scope | Primary files / areas | Dependency order | Risk | Rollback strategy | Acceptance gate |
|---|---|---|---|---|---|---|
| PU-11-01 | Film schema family | `schemas/film/**` | 1 | Medium | Remove new film schemas only | Film packet shape is expressible |
| PU-11-02 | Film contract family | `runtime_contracts/film/**` | 2 | Medium | Remove film contracts only | Film rules are explicit and parallel |
| PU-11-03 | Film validator family | `validators/film/**` | 3 | High | Remove film validators only | Fake film PASS is blocked |
| PU-11-04 | Film route manifests | `registries/route_manifests/**` | 4 | High | Remove film route entries only | Film route is selectable without replacing content route |
| PU-11-05 | Film route slices | `registries/route_slices/**` | 4 | High | Remove film slice entries only | Film route has a concrete consumption path |
| PU-11-06 | Content-vs-film separation rules | routing contracts and registries | 2-4 | High | Restore prior routing precedence | Content route still handles YouTube/social work |
| PU-11-07 | Downstream adaptation retention | visual / voice / editing / media factory routes | 4 | Medium | Revert only new film bindings | Existing downstream routes remain intact |
| PU-11-08 | Fixture harness binding | `PHASE_10_*` docs and future test data | 5 | Medium | Drop harness bindings only | Fixture coverage spans route selection and failure cases |
| PU-11-09 | Director / agent / skill / subskill wiring | consumer registries and route selection logic | 6 | High | Restore previous consumer selection | Film route can consume the right layers without content drift |
| PU-11-10 | Acceptance reporting | output contract / scorecard reporting | 6 | Medium | Disable film-specific reporting only | Film acceptance can be explained and audited |
| PU-11-11 | Film route state capsule | route state schema and persistence | 1 | Medium | Remove film state additions only | Film mode can be tracked distinctly |
| PU-11-12 | Film source ledger / fact map | source ledger and source-bound output fields | 1 | Medium | Remove source packet additions only | Film claims remain source-aware |
| PU-11-13 | Beat-sheet family | beat sheet and structure maps | 1-2 | Medium | Remove structure fields only | Cinema structure is expressible |
| PU-11-14 | Character arc family | character arc and web | 1-2 | Medium | Remove character fields only | Character transformation can be enforced |
| PU-11-15 | Scene dramaturgy family | objective / conflict / turn fields | 1-2 | Medium | Remove scene fields only | Scene-level drama is explicit |
| PU-11-16 | Dialogue subtext family | dialogue pass fields | 1-2 | Medium | Remove dialogue film fields only | Dialogue can be judged beyond surface text |
| PU-11-17 | Visual motif family | motif / image-system fields | 1-2 | Medium | Remove visual motif fields only | Visual repetition can be tracked |
| PU-11-18 | Mise-en-scene family | blocking / composition fields | 1-2 | Medium | Remove mise-en-scene fields only | Stagecraft is representable |
| PU-11-19 | Camera language family | lens / framing / movement fields | 1-2 | Medium | Remove camera fields only | Directorial framing is explicit |
| PU-11-20 | Sound / silence / performance family | sound motif and performance fields | 1-2 | Medium | Remove sound/performance fields only | Auditory and acting direction are representable |
| PU-11-21 | Film screenplay format status | screenplay formatting flags | 1-2 | Low | Remove format status fields only | Film packet formatting can be verified |
| PU-11-22 | Film downstream handoff packet | downstream handoff fields | 1-2 | Medium | Remove handoff additions only | Film packet can feed later stages |
| PU-11-23 | No-fake-pass gate | validation scorecard and gate results | 2-3 | High | Remove new gate logic only | Fake PASS states are blocked |
| PU-11-24 | Film-vs-content collision rules | route precedence and packet classification | 2-4 | High | Restore content precedence rules | Content and film outputs stay separable |
| PU-11-25 | Film acceptance harness | fixture-to-validator mapping | 5 | Medium | Drop harness mapping only | The plan remains measurable |
| PU-11-26 | Film reporting summary | owner-readable implementation summary | 6 | Low | Remove film summary only | Auditability stays intact |
| PU-11-27 | Runtime integration boundary | adapter and provider handoff | 6 | High | Revert integration boundary only | Runtime stays honest |
| PU-11-28 | Preservation of downstream routes | visual / voice / editing / media factory routes | 4-6 | Medium | Revert new film bindings only | Existing downstream tooling remains usable |
| PU-11-29 | Route selection dispatch | task-to-route choice logic | 4-6 | High | Restore old dispatch order | Film prompts can route without hijacking content prompts |
| PU-11-30 | Implementation telemetry | patch provenance and acceptance telemetry | 6 | Low | Disable film telemetry only | The rollout can still be audited |

## Patch unit notes

### PU-11-01

Adds the data model that can describe a cinema-first packet.
Without this, later validators would have no stable shape to enforce.

### PU-11-02

Defines the legal spine of film-mode behavior.
These contracts should explain the difference between content scripts and film scripts.

### PU-11-03

Ensures incomplete film packets fail closed.
This is the main protection against fake PASS states.

### PU-11-04

Introduces a separate film route family in parallel with `SCRIPT_GENERATION`.
This is the first visible route split.

### PU-11-05

Adds route slices so the film route has a concrete consumption path.
This keeps route selection from becoming a label-only change.

### PU-11-06

Makes the route split enforceable in both the content and film directions.
Content routes remain valid downstream behavior.

### PU-11-07

Preserves the current visual, voice, editing, and media factory layers.
These are downstream adaptation assets, not core screenplay writers.

### PU-11-08

Connects Phase 10 fixtures to the future implementation path.
Fixture coverage should remain documentation-backed until implementation is ready.

### PU-11-09

Aligns directors, agents, subagents, skills, and subskills with the new film route.
This should happen after the film route exists so the wiring has a target.

### PU-11-10

Provides readable reporting so the owner can audit film-mode readiness.
No PASS claims should be made without schema and validator backing.

## Rollback ordering

If a later patch unit fails, rollback in this order:

1. Remove the newest implementation wiring
2. Remove the newest route entries
3. Remove the newest validators
4. Remove the newest contracts
5. Remove the newest schemas

Do not roll back the content engine unless it was explicitly modified by the failed patch unit.

## Success criteria by layer

- Schema success: packet fields are representable
- Contract success: film-vs-content separation is explicit
- Validator success: incomplete or fake film packets fail
- Route success: film prompts resolve to a film route
- Wiring success: the correct directors / agents / skills are consumed
- Reporting success: the implementation can be explained without invented proof

## Patch budget

The first implementation batch should be as small as possible while still proving the route split:

- one schema slice
- one contract slice
- one validator slice
- one route slice
- one fixture slice

Everything else should wait until that slice is stable.

## Notes on preserved behavior

The following must remain available unless later work explicitly changes them:

- `SCRIPT_GENERATION`
- content engineering routes
- visual media planning routes
- voice context routes
- editing and packaging routes
- media factory handoff routes
- downstream release and distribution routes

The film route is additive, not destructive.
