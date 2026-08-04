# Phase 12F Route Selector Risk Ledger

## Risk ledger

| Risk ID | Risk | Trigger | Impact | Mitigation | Required evidence before implementation |
|---|---|---|---|---|---|
| F12F-R1 | Content scripts accidentally route into film mode | Broad film trigger terms applied without preserving `SCRIPT_GENERATION` precedence | YouTube/content tasks lose their expected route behavior | Keep `SCRIPT_GENERATION` as the baseline selector branch and require explicit collision checks | Active route registration, content-preservation regressions, selector dry-run traces |
| F12F-R2 | Short films fall back to content routes because of duration wording | Prompt mentions `YouTube`, `Shorts`, or `reel` while actually requesting a film | Film requests are misclassified and lose screenplay structure | Add intent rules that privilege screenplay language and film intent over platform packaging | Route intent matrix update, examples, and regression fixtures |
| F12F-R3 | Hook/re-hook/retention law leaks into film-core | Film selector branch inherits content cadence requirements | Film outputs get content-engine cadence as core law | Separate content cadence from film narrative law and gate it in film validators only when relevant | Film validators, film schema fields, and side-by-side fixture comparisons |
| F12F-R4 | Route selector is modified before active manifest/slice registration | Selector change happens while film route remains draft-only | Unregistered route starts influencing live routing | Require active registration prep before selector branching | Active film manifest and active film slice reviews |
| F12F-R5 | Validators are still skeleton-only | Selector tries to rely on Phase 12C skeleton validators | Film PASS becomes cosmetic instead of enforced | Do not bind selector integration until validators are enforceable | Validator binding plan and executable validator checks |
| F12F-R6 | Schemas are still skeleton-only | Selector assumes film packet fields are already enforced | Route may accept underspecified packets | Keep schema enforcement as a prerequisite, not a premise | Schema enforcement plan and packet fixture coverage |
| F12F-R7 | Contracts are still skeleton-only | Route logic assumes film governance is runtime-active | Governance is implied but not actually active | Treat contracts as design targets until binding phases are approved | Contract binding plan and route regression evidence |
| F12F-R8 | Downstream handoff confusion | Trailer, teaser, voice, or editing requests get treated as film screenplay requests | Users get the wrong route family | Keep downstream handoffs separate from film-core route intent | Downstream handoff map and route collision tests |
| F12F-R9 | Fake PASS or invented runtime artifact IDs | Route integration declares success without execution evidence | False readiness claims | Require no-fake-PASS gates and proof boundary checks | Manifested evidence bundles and no-fake-PASS fixtures |
| F12F-R10 | Real incident/docudrama request without source ledger | A factual incident is routed into film without source controls | Unsupported claims and ethics risk | Require source ledger and fact-vs-anecdote handling for real incidents | Source-ledger fields, ethics checks, and real-incident fixtures |
| F12F-R11 | Selector change without content preservation regression fixtures | Route logic changes but content baseline is not retested | `SCRIPT_GENERATION` may regress silently | Require content preservation fixtures before any selector integration | Regression fixture suite and diffable route traces |
| F12F-R12 | Active route manifest collision with `SCRIPT_GENERATION` | New film route uses overlapping aliases or trigger terms | Ambiguous routing and accidental overwrite risk | Keep canonical route IDs separate and require explicit anti-collision rules | Active film route manifest review and selector collision audit |

## Phase 12F Risk Status

`ROUTE_SELECTOR_INTEGRATION_STATUS = BLOCKED_PENDING_REGISTRATION_PREP_AND_VALIDATION`

The film route should remain draft-only until active registration prep, regression evidence, and binding-aware validators are ready.
