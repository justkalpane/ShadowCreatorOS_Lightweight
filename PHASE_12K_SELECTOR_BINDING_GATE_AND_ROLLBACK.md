# Phase 12K Selector Binding Gate and Rollback

## 1. Objective
Define the gate for a future selector-binding phase.

## 2. Future binding prerequisites

| Gate | Required evidence | Current status | Blocker if missing |
|---|---|---|---|
| Active manifest/slice registration decision | Owner-approved decision to create active film route files | Not yet approved | Binding should not start without a clear activation decision |
| Selector edit plan | A concrete selector patch plan | Prep-only in this phase | No safe selector edit path without a patch plan |
| Fixture coverage | Phase 12A route, film-packet, content-preservation, downstream, and no-fake-PASS fixtures | Present | Missing coverage leaves collisions untested |
| Schema skeletons available | Phase 12B schema skeletons | Present | Selector should not move ahead of schema prep |
| Validator skeletons available | Phase 12C validator skeletons | Present | Binding without validators creates false PASS risk |
| Contract prep available | Phase 12D contract prep | Present | Binding without contract prep weakens governance |
| No-fake-PASS validation plan | Explicit no-fake-PASS gate plan | Present in prep chain | Selector changes need explicit proof boundaries |
| Content preservation regression plan | Regression coverage for `SCRIPT_GENERATION` preservation | Present in fixture set, but not executable yet | Content route must stay protected |
| Downstream route preservation plan | Explicit downstream-only routing for trailers, teasers, packaging, and handoffs | Present in prep chain | Prevents overreach into film-core |
| Rollback plan | Revert path for selector and any future active files | Present here | No safe binding without a clear rollback |
| Owner approval | Explicit owner approval for the next phase | Required | No binding without approval |

## 3. Rollback plan
Future rollback must include:
- revert selector edit
- keep content route unchanged
- keep fixtures/schemas/validators/contracts as harmless prep artifacts if unbound
- rerun content preservation fixtures/tests
- remove active route files only if registration happened in the same patch

## 4. Future approval phrase
`Approved: proceed with Phase 12L active manifest/slice files only, no selector binding.`

Phase 12L must not start until Phase 12K is reviewed and approved.
Phase 12L must not modify the route selector.
Phase 12L must not bind `FILM_SCREENPLAY_GENERATION`.
Phase 12L may only create active manifest/slice files if repo evidence proves they remain unselector-bound until a later selector patch.
Selector binding remains a later phase after Phase 12L review.
No runtime PASS or governed proof is claimed.

## 5. Phase 12L recommendation
`Phase 12L: active manifest/slice files only, no selector binding`

That is the safer next step because it creates the active route artifacts first while keeping the live selector untouched.
