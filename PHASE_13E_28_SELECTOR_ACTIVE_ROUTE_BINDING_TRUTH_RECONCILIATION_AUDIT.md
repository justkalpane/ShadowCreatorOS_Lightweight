# Phase 13E_28 Selector and Active Route Binding Truth Reconciliation Audit

## 1. Objective

Phase 13E_28 reconciles repo evidence about `FILM_SCREENPLAY_GENERATION` selector binding versus the active film route manifest and slice metadata.

This is an audit-only phase. It does not modify the route selector, active route manifests, active route slices, schemas, validators, contracts, fixtures, directors, agents, subagents, skills, subskills, or runtime behavior.

## 2. Current State

```text
phase=13E_28
base_head=6d9a79425b1aa99a2bb1d4747ff53e1fc4b19c09
phase_13e_27_completed=true
selector_truth_reconciliation_audit_started=true
runtime_behavior_changed=false
selector_modified=false
active_route_manifest_modified=false
active_route_slice_modified=false
pass_claimed=false
runtime_proof_claimed=false
governed_runtime_proof_claimed=false
worktree_dirty=true
```

The worktree contains pre-existing unrelated dirty and untracked files. This audit preserves them and stages only this report.

## 3. Evidence Inspected

| Surface | Path or command | Evidence | Interpretation |
| --- | --- | --- | --- |
| Route selector | `runtime/state/route_chain_mode_selector.yaml` | `default_mode=script_only`; `film_screenplay_generation` mode exists; allowed route ID is `FILM_SCREENPLAY_GENERATION`. | Repo selector binding exists from Phase 12L-K while the default content route remains preserved. |
| Selector binding patch | `git diff --name-only 233b774^..233b774`; `git diff 233b774^..233b774 -- runtime/state/route_chain_mode_selector.yaml` | Phase 12L-K added only `PHASE_12L_K_SELECTOR_BINDING_PATCH_REPORT.md` and `runtime/state/route_chain_mode_selector.yaml`; the new mode allows `FILM_SCREENPLAY_GENERATION`. | Selector binding was intentional and additive. |
| Phase 12L-K report | `PHASE_12L_K_SELECTOR_BINDING_PATCH_REPORT.md` | Declares `added_selector_mode=film_screenplay_generation`, `added_route_id=FILM_SCREENPLAY_GENERATION`, and `default_mode_unchanged=script_only`. | Confirms repo-level selector binding, not runtime PASS. |
| Phase 12L-L report | `PHASE_12L_L_POST_SELECTOR_BINDING_VALIDATION_REPORT.md` | Declares `POST_SELECTOR_BINDING_VALIDATION_NEEDS_CHECKER_UPDATE` and `runtime_behavior_changed=repo_selector_binding_exists`. | Confirms selector binding exists and that the old promotion checker is stale after binding. |
| Phase 12L-M plan | `PHASE_12L_M_POST_BINDING_CHECKER_UPDATE_PLAN.md` | Recommends a separate post-binding checker instead of weakening the pre-promotion checker. | Checker model remains incomplete after selector binding. |
| Active film manifest | `registries/route_manifests/film_screenplay_generation.yaml` | `active_route=true`, `registered=true`, `bound_to_route_selector=false`, `runtime_behavior_changed=false`, `pass_claimed=false`. | Active registry file exists but binding metadata is stale or unreconciled after Phase 12L-K. |
| Active film slice | `registries/route_slices/film_screenplay_generation.registry_slice.yaml` | `active_slice=true`, `registered=true`, `bound_to_route_selector=false`, `selector_binding_required=false`, `route_activation_requires_later_selector_patch=true`, `FILM_SCREENPLAY_GENERATION_NOT_SELECTOR_BOUND=true`. | Slice still carries pre-selector-binding metadata/law even though selector mode now exists. |
| Script route preservation | `registries/route_slices/script_generation.registry_slice.yaml`; selector | `route_id=SCRIPT_GENERATION`; selector default remains `script_only`. | Existing `SCRIPT_GENERATION` route remains preserved. |
| Pre-promotion checker | `python3 validators/film/validate_film_route_promotion_gate.py` | `PROMOTION_GATE_BLOCKED_ACTIVE_FILE_ALREADY_EXISTS`. | Expected stale result for pre-binding checker after active files and selector mode exist. |

## 4. Parse and Static Validation Results

| File | Parser command | Result |
| --- | --- | --- |
| `runtime/state/route_chain_mode_selector.yaml` | `ruby -rpsych -e 'Psych.load_file("runtime/state/route_chain_mode_selector.yaml")'` | `selector_yaml_valid` |
| `registries/route_manifests/film_screenplay_generation.yaml` | `ruby -rpsych -e 'Psych.load_file("registries/route_manifests/film_screenplay_generation.yaml")'` | `film_manifest_yaml_valid` |
| `registries/route_slices/film_screenplay_generation.registry_slice.yaml` | `ruby -rpsych -e 'Psych.load_file("registries/route_slices/film_screenplay_generation.registry_slice.yaml")'` | `film_slice_yaml_valid` |
| `registries/route_manifests/script_generation.yaml` | `ruby -rpsych -e 'Psych.load_file("registries/route_manifests/script_generation.yaml")'` | `script_manifest_yaml_valid` |
| `registries/route_slices/script_generation.registry_slice.yaml` | `ruby -rpsych -e 'Psych.load_file("registries/route_slices/script_generation.registry_slice.yaml")'` | `script_slice_yaml_valid` |

## 5. Reconciliation Matrix

| Truth claim | Selector evidence | Manifest evidence | Slice evidence | Reconciled status |
| --- | --- | --- | --- | --- |
| `FILM_SCREENPLAY_GENERATION` selector mode exists | Present: `film_screenplay_generation` mode allows `FILM_SCREENPLAY_GENERATION`. | Not the selector source. | Not the selector source. | True at selector layer. |
| Default content route remains preserved | `default_mode=script_only`; `SCRIPT_GENERATION` still allowed in script mode. | `preserves_content_route=SCRIPT_GENERATION`. | `SCRIPT_GENERATION_PRESERVED=true`. | True. |
| Active film registry files exist | Not registry source. | `active_route=true`, `registered=true`. | `active_slice=true`, `registered=true`. | True at registry layer. |
| Film manifest/slice say selector-bound | Selector says mode exists. | `bound_to_route_selector=false`. | `bound_to_route_selector=false`. | False at route metadata layer. |
| Film slice says selector patch still needed | Selector already has the mode. | Not present. | `route_activation_requires_later_selector_patch=true`; `FILM_SCREENPLAY_GENERATION_NOT_SELECTOR_BOUND=true`. | Stale/unreconciled after Phase 12L-K. |
| Governed runtime proof exists | Not proven by selector file. | `governed_runtime_proof_claimed=false`. | `governed_runtime_proof_claimed=false`. | False. |

## 6. Root Cause Classification

```text
selector_layer_state=BOUND_AT_REPO_SELECTOR_LEVEL
active_manifest_state=ACTIVE_REGISTERED_BUT_BINDING_METADATA_STALE
active_slice_state=ACTIVE_REGISTERED_BUT_BINDING_METADATA_STALE
checker_state=PRE_BINDING_PROMOTION_CHECKER_STALE_FOR_POST_BINDING_STATE
script_generation_state=PRESERVED
runtime_proof_state=NOT_CLAIMED
```

The evidence does not show a selector-binding failure. It shows that Phase 12L-K added the selector mode, while the active film manifest and slice retained pre-selector-binding metadata from earlier active-registry-only phases. The old promotion checker also remains pre-binding and therefore reports an expected blocker once active files already exist.

## 7. Risks If Left Unreconciled

| Risk ID | Risk | Impact | Required handling |
| --- | --- | --- | --- |
| R-001 | Manifest/slice metadata says unbound while selector contains bound mode. | Future audits can disagree about whether `FILM_SCREENPLAY_GENERATION` is repo selector-bound. | Bounded metadata reconciliation patch. |
| R-002 | Slice still says `route_activation_requires_later_selector_patch=true`. | Later phases may try to repeat selector work or block incorrectly. | Update active slice metadata only after owner approval. |
| R-003 | Slice law still says `FILM_SCREENPLAY_GENERATION_NOT_SELECTOR_BOUND=true`. | Route truth is internally inconsistent after Phase 12L-K. | Replace or retire stale law carefully without claiming runtime proof. |
| R-004 | Pre-promotion checker remains the only checker. | Checker output remains stale after active files exist and selector binding exists. | Add post-binding state checker in a separate bounded phase. |
| R-005 | Runtime proof could be confused with repo selector truth. | False PASS or governed completion claim risk. | Keep `runtime_proof_claimed=false` until governed runtime surface returns proof. |

## 8. Non-Actions in Phase 13E_28

```text
route_selector_modified=false
active_route_manifest_modified=false
active_route_slice_modified=false
schemas_modified=false
validators_modified=false
contracts_modified=false
fixtures_modified=false
directors_modified=false
agents_modified=false
subagents_modified=false
skills_modified=false
subskills_modified=false
runtime_behavior_changed=false
pass_claimed=false
runtime_proof_claimed=false
governed_runtime_proof_claimed=false
```

## 9. Recommended Repair Scope

A later bounded patch should update only active film route metadata and, if approved separately, add a post-binding checker. It should not touch selector logic unless new evidence proves the selector itself is wrong.

Candidate metadata-only repair fields:

```text
registries/route_manifests/film_screenplay_generation.yaml:
  bound_to_route_selector: true
  runtime_behavior_changed: false
  governed_runtime_proof_claimed: false
  pass_claimed: false

registries/route_slices/film_screenplay_generation.registry_slice.yaml:
  bound_to_route_selector: true
  runtime_state_requirements.selector_binding_required: true
  runtime_state_requirements.route_activation_requires_later_selector_patch: false
  laws.FILM_SCREENPLAY_GENERATION_NOT_SELECTOR_BOUND: false
  runtime_behavior_changed: false
  governed_runtime_proof_claimed: false
  pass_claimed: false
```

Candidate checker-only repair:

```text
validators/film/validate_film_route_post_binding_state.py
```

The checker should verify selector mode, active manifest, active slice, script route preservation, no-PASS boundary, no governed proof claim, and downstream/content separation without weakening `validators/film/validate_film_route_promotion_gate.py`.

## 10. Final Verdict

```text
PHASE_13E_28_STATUS=SELECTOR_ACTIVE_ROUTE_BINDING_TRUTH_RECONCILIATION_AUDIT_COMPLETE
SELECTOR_FILM_MODE_PRESENT=true
SELECTOR_ALLOWED_ROUTE_ID_FILM_SCREENPLAY_GENERATION=true
DEFAULT_MODE_SCRIPT_ONLY_PRESERVED=true
SCRIPT_GENERATION_PRESERVED=true
ACTIVE_FILM_MANIFEST_EXISTS=true
ACTIVE_FILM_SLICE_EXISTS=true
ACTIVE_FILM_MANIFEST_REGISTERED=true
ACTIVE_FILM_SLICE_REGISTERED=true
ACTIVE_FILM_MANIFEST_BINDING_METADATA_RECONCILED=false
ACTIVE_FILM_SLICE_BINDING_METADATA_RECONCILED=false
PRE_PROMOTION_CHECKER_STALE_FOR_POST_BINDING_STATE=true
POST_BINDING_CHECKER_EXISTS=false
RUNTIME_BEHAVIOR_CHANGED=false
SELECTOR_MODIFIED=false
ACTIVE_ROUTE_MANIFESTS_MODIFIED=false
ACTIVE_ROUTE_SLICES_MODIFIED=false
SCHEMAS_MODIFIED=false
VALIDATORS_MODIFIED=false
CONTRACTS_MODIFIED=false
FIXTURES_MODIFIED=false
DIRECTORS_MODIFIED=false
AGENTS_MODIFIED=false
SUBAGENTS_MODIFIED=false
SKILLS_MODIFIED=false
SUBSKILLS_MODIFIED=false
PASS_CLAIMED=false
RUNTIME_PROOF_CLAIMED=false
GOVERNED_RUNTIME_PROOF_CLAIMED=false
```

## 11. Recommended Next Phase

```text
Phase 13E_29: bounded active film route binding metadata reconciliation patch
```

Phase 13E_29 should update only the stale active film manifest/slice binding metadata to match the repo selector binding created in Phase 12L-K, while preserving `SCRIPT_GENERATION`, preserving `default_mode=script_only`, and continuing to claim no runtime PASS or governed runtime proof.
