# Phase 13E_33 Governed Film Route Runtime Proof Harness Plan

## 1. Objective

Phase 13E_33 designs the governed runtime proof harness for `FILM_SCREENPLAY_GENERATION`.

This phase is planning-only. It does not execute runtime, does not generate a film screenplay packet, does not modify the route selector, does not modify active route registries, does not bind validators, does not modify schemas, does not change runtime behavior, and does not claim PASS or governed runtime proof.

The plan converts Phase 13E_32 readiness findings into a bounded future harness shape.

## 2. Current State Evidence

```text
phase=13E_33
base_head=6c90510bc270a0e92b6fd76d368bad4b1c871f81
phase_13e_32_completed=true
static_route_state_ready_for_proof_planning=true
post_binding_checker_ready_status_confirmed=true
governed_runtime_invocation_identified=false
runtime_proof_execution_ready=false
runtime_execution_performed=false
film_output_generated=false
runtime_behavior_changed=false
selector_modified=false
active_route_manifest_modified=false
active_route_slice_modified=false
validators_modified=false
schemas_modified=false
tests_modified=false
pass_claimed=false
governed_runtime_proof_claimed=false
worktree_dirty=true
```

Evidence inspected:

| Evidence | Path or command | Finding | Harness implication |
| --- | --- | --- | --- |
| Phase 13E_32 readiness gate | `PHASE_13E_32_FILM_ROUTE_RUNTIME_PROOF_READINESS_GATE.md` | `GOVERNED_RUNTIME_INVOCATION_IDENTIFIED=false`; `RUNTIME_PROOF_EXECUTION_READY=false` | Harness must be designed before proof execution |
| Post-binding checker | `python3 validators/film/validate_film_route_post_binding_state.py` | `POST_BINDING_FILM_ROUTE_STATE_READY` | Harness can rely on static route metadata as preflight input |
| Phase 13E_30 checker test | `python3 tests/test_phase_13e30_film_route_post_binding_state_checker.py` | Passed | Existing checker remains a pre-proof guard |
| Phase 13E_29 metadata test | `python3 tests/test_phase_13e29_active_film_route_binding_metadata.py` | Passed | Active metadata is internally coherent |
| Selector | `runtime/state/route_chain_mode_selector.yaml` | `default_mode=script_only`; film mode allows `FILM_SCREENPLAY_GENERATION` | Harness must preserve default mode and route boundaries |
| Active manifest | `registries/route_manifests/film_screenplay_generation.yaml` | Active, registered, selector-bound metadata | Harness must not edit registry metadata during proof |
| Active slice | `registries/route_slices/film_screenplay_generation.registry_slice.yaml` | Active, registered, selector-bound metadata; route state requirements present | Harness must emit route-state evidence matching slice expectations |
| Route state contract | `runtime/state/route_state_contract.md` | Requires route state capsule, file hashes, read ledger, validator ledger, and no-fake-PASS controls | Harness must produce a capsule before any proof claim |
| Route state schema | `runtime/state/route_state.schema.json` | Does not yet include `film_screenplay_generation` in `task_mode` enum | Harness implementation must avoid claiming schema-valid route state until this is reconciled |
| Film output schema | `schemas/film/output_packet/film_screenplay_output_packet.schema.json` | Skeleton schema with no required fields | Cannot be used alone as proof of film output quality |
| Key film validators | `validators/film/...` | Relevant validators return `SKELETON_ONLY`, `passed=false`, `enforced=false` | Runtime proof remains blocked until enforceable validators exist |

## 3. Harness Design Boundary

The future harness must be proof infrastructure, not proof itself.

Allowed future harness responsibilities:

- run static route preflight through the Phase 13E_30 post-binding checker,
- load selector, manifest, slice, route state contract, output schema, and validator manifest,
- create a dry-run route state capsule template,
- create an evidence bundle template,
- define a controlled film-screenplay invocation payload,
- record before/after dirty-worktree and default-mode evidence,
- run script route preservation checks,
- run available validators and record whether they are skeleton-only, blocked, or enforceable,
- stop with a blocked status when enforceable film runtime validation is not available.

Prohibited future harness behavior:

- do not claim `PASS` from static metadata,
- do not claim governed runtime proof from checker readiness,
- do not invent runtime artifact IDs,
- do not invent completion certificates,
- do not route YouTube/content prompts into film-core,
- do not activate downstream media, thumbnail, shorts, publishing, or platform metadata surfaces as film-core authorities,
- do not modify unrelated dirty files,
- do not modify selector or active route registry files during proof.

## 4. Proposed Harness File Scope

Future Phase 13E_34 may create implementation files only if approved separately.

Proposed bounded files:

| Future file | Purpose | Runtime behavior changed? | Proof claim allowed? |
| --- | --- | --- | --- |
| `tools/film_runtime/film_route_runtime_proof_harness.py` | Read-only harness entrypoint for preflight, route-state template, evidence bundle template, and controlled blocked proof status | false | false |
| `tests/test_phase_13e34_film_route_runtime_proof_harness.py` | Unit tests for harness status, boundary preservation, skeleton-validator blocking, and no fake proof claims | false | false |
| `PHASE_13E_34_GOVERNED_FILM_ROUTE_RUNTIME_PROOF_HARNESS_IMPLEMENTATION_REPORT.md` | Implementation report if a harness patch is later approved | false | false |

The proposed harness should write no proof artifacts by default. If it needs an output path later, it must write only under a dedicated phase-scoped evidence directory approved in that later phase.

## 5. Proposed Harness Status Model

The harness must return one of these statuses:

```text
FILM_RUNTIME_PROOF_HARNESS_PREFLIGHT_READY
FILM_RUNTIME_PROOF_BLOCKED_NO_GOVERNED_INVOCATION
FILM_RUNTIME_PROOF_BLOCKED_ROUTE_STATE_SCHEMA_GAP
FILM_RUNTIME_PROOF_BLOCKED_SKELETON_VALIDATORS
FILM_RUNTIME_PROOF_BLOCKED_OUTPUT_SCHEMA_SKELETON
FILM_RUNTIME_PROOF_BLOCKED_SCRIPT_ROUTE_REGRESSION
FILM_RUNTIME_PROOF_BLOCKED_DIRTY_WORKTREE_SCOPE
FILM_RUNTIME_PROOF_BLOCKED_FAKE_PASS_ATTEMPT
```

`FILM_RUNTIME_PROOF_HARNESS_PREFLIGHT_READY` may only mean the harness can run preflight checks. It must not mean runtime proof passed.

## 6. Required Harness Output Fields

A future harness report must include:

```text
FILM_RUNTIME_PROOF_HARNESS_REPORT
phase=
status=
repo_root=
head_sha=
route_mode=film_screenplay_generation
route_id=FILM_SCREENPLAY_GENERATION
default_mode_before=
default_mode_after=
selector_mode_resolved=
manifest_path=
manifest_hash=
slice_path=
slice_hash=
script_generation_preserved=
post_binding_checker_status=
route_state_capsule_template_created=
route_state_schema_compatible=
film_output_schema_enforceable=
film_validators_enforceable=
film_output_generated=false
runtime_execution_performed=false
runtime_behavior_changed=false
pass_claimed=false
governed_runtime_proof_claimed=false
first_blocker=
```

## 7. Required Route State Capsule Template

The harness should prepare a template matching `runtime/state/route_state_contract.md`:

```text
route_id=FILM_SCREENPLAY_GENERATION
route_manifest_path=registries/route_manifests/film_screenplay_generation.yaml
route_manifest_hash=<computed>
task_mode=film_screenplay_generation
route_phase=BLOCKED
files_consumed=<selected route scope>
file_hashes=<selected route scope hashes>
evidence_bundle_id=<none until proof execution is allowed>
evidence_bundle_schema_path=<future approved path>
validator_ledger=<validator names and enforceability statuses>
validator_results=<blocked/skeleton/enforced>
bridge_job_packet_path=<not applicable unless downstream handoff approved>
bridge_job_packet_hash=<not applicable unless downstream handoff approved>
patch_transaction_id=<not applicable for read-only proof>
dependencies_complete=false
output_phase_started=false
last_completed_step=POST_BINDING_STATIC_PREFLIGHT
next_required_step=RECONCILE_FILM_TASK_MODE_SCHEMA_AND_ENFORCE_VALIDATORS
compaction_recovery_ready=true
historical_files_allowed=false
active_runtime_scope=FILM_SCREENPLAY_GENERATION_ONLY
```

Current caveat: `runtime/state/route_state.schema.json` does not list `film_screenplay_generation` in its `task_mode` enum. A future harness may create a route state contract template, but it must not claim schema-valid route state until that schema gap is explicitly handled in an approved phase.

## 8. Validator Enforcement Reality

The following validators were inspected as proof-critical examples:

| Validator | Current result | Proof implication |
| --- | --- | --- |
| `validators/film/output_packet/validate_film_screenplay_packet.py` | `SKELETON_ONLY`, `passed=false`, `enforced=false` | Cannot validate runtime output as PASS |
| `validators/film/validation/validate_no_fake_film_pass.py` | `SKELETON_ONLY`, `passed=false`, `enforced=false` | Cannot enforce no-fake-PASS on generated output yet |
| `validators/film/validation/validate_film_content_packet_separation.py` | `SKELETON_ONLY`, `passed=false`, `enforced=false` | Cannot enforce content-vs-film packet separation yet |
| `validators/film/route/validate_film_route_selection.py` | `SKELETON_ONLY`, `passed=false`, `enforced=false` | Cannot prove selector behavior through film validator enforcement yet |

Therefore:

```text
film_validators_enforceable=false
film_output_schema_enforceable=false
runtime_proof_claim_allowed=false
```

## 9. Script Route And Downstream Preservation Requirements

The future harness must prove these are preserved before and after any runtime attempt:

| Boundary | Required future check |
| --- | --- |
| `SCRIPT_GENERATION` default route | Selector `default_mode` remains `script_only` |
| YouTube/content prompts | Negative trigger fixtures continue to avoid film-core |
| Shorts/reels/TikTok prompts | Must remain content/social route, not film-core |
| Voiceover prompts | Must remain content/voice route unless attached to an already approved film packet |
| Trailer/teaser/title/thumbnail prompts | Must remain downstream packaging, not film-core screenplay generation |
| Media Factory handoff | Must remain downstream and cannot become cinema-core proof authority |
| Full video pipeline | Must remain downstream and cannot replace screenplay proof |

## 10. Dirty Worktree Containment

The future harness must record:

```bash
git status --porcelain=v2
git diff --name-only
git diff --cached --name-only
```

It must fail if it writes, stages, or modifies any unrelated dirty file. If evidence artifacts are later approved, they must be phase-scoped and must not touch existing dirty hunks.

## 11. Acceptance Tests For Future Harness Patch

| Test | Required assertion |
| --- | --- |
| Harness CLI exists | CLI prints `FILM_RUNTIME_PROOF_HARNESS_REPORT` |
| Static preflight runs | Post-binding checker status is consumed |
| No proof claim | CLI prints `pass_claimed=false` and `governed_runtime_proof_claimed=false` |
| Skeleton validator block | CLI returns blocked status when film validators are still skeleton-only |
| Route-state schema caveat | CLI records schema gap for `film_screenplay_generation` task mode if unreconciled |
| Default mode preserved | CLI records `default_mode_before=script_only` and `default_mode_after=script_only` |
| Script route preserved | CLI records `script_generation_preserved=true` |
| No downstream drift | CLI records media/publishing downstream-only boundary |
| Dirty worktree protected | Test verifies harness does not stage or alter unrelated files |

## 12. Failure Containment

The future harness must stop at the first blocker and return:

```text
first_blocker_id=
first_blocker_summary=
responsible_path=
minimum_repair_scope=
runtime_execution_performed=false
film_output_generated=false
pass_claimed=false
governed_runtime_proof_claimed=false
next_safe_action=
```

If the first blocker is the current skeleton-validator state, the next safe action is validator enforcement planning, not runtime execution.

## 13. Final Verdict

```text
PHASE_13E_33_STATUS=GOVERNED_FILM_ROUTE_RUNTIME_PROOF_HARNESS_PLAN_COMPLETE
HARNESS_IMPLEMENTED=false
RUNTIME_EXECUTION_PERFORMED=false
FILM_OUTPUT_GENERATED=false
STATIC_POST_BINDING_PREFLIGHT_READY=true
GOVERNED_RUNTIME_INVOCATION_DEFINED=false
ROUTE_STATE_CAPSULE_TEMPLATE_DEFINED=true
EVIDENCE_BUNDLE_SHAPE_DEFINED=true
FILM_VALIDATORS_ENFORCEABLE=false
FILM_OUTPUT_SCHEMA_ENFORCEABLE=false
ROUTE_STATE_SCHEMA_GAP_IDENTIFIED=true
SCRIPT_GENERATION_PRESERVATION_REQUIRED=true
DOWNSTREAM_BOUNDARY_PRESERVATION_REQUIRED=true
DIRTY_WORKTREE_CONTAINMENT_REQUIRED=true
RUNTIME_BEHAVIOR_CHANGED=false
SELECTOR_MODIFIED=false
ACTIVE_ROUTE_MANIFESTS_MODIFIED=false
ACTIVE_ROUTE_SLICES_MODIFIED=false
VALIDATORS_MODIFIED=false
SCHEMAS_MODIFIED=false
TESTS_MODIFIED=false
PASS_CLAIMED=false
RUNTIME_PROOF_CLAIMED=false
GOVERNED_RUNTIME_PROOF_CLAIMED=false
FINAL_VERDICT=READY_FOR_BOUNDED_HARNESS_IMPLEMENTATION_NOT_RUNTIME_PROOF
```

## 14. Recommended Next Phase

Phase 13E_34: bounded governed film route proof harness implementation patch

Phase 13E_34 should implement only the read-only harness and its focused tests. It must not execute runtime proof, must not claim PASS, and must return a blocked status while film validators remain skeleton-only or the route state schema cannot represent `film_screenplay_generation`.
