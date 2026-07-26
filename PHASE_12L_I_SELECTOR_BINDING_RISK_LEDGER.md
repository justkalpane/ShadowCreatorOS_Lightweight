# Phase 12L-I Selector Binding Risk Ledger

## 1. Objective
Record the risks that still matter before any selector binding work begins.

## 2. Risk Table

| Risk ID | Risk | Evidence/source | Impact | Mitigation | Stop condition |
|---|---|---|---|---|---|
| R-12LI-01 | Selector binding activates film route path | Phase 12L-G and current active registry pair | Film route becomes live through the selector | Keep binding separate from registry promotion | Stop if selector binding is attempted without explicit owner approval |
| R-12LI-02 | Content route collision | `runtime/state/route_chain_mode_selector.yaml` and `registries/route_manifests/script_generation.yaml` | `SCRIPT_GENERATION` could be displaced or blurred | Preserve `SCRIPT_GENERATION` as the content route boundary | Stop if any selector change removes or weakens `SCRIPT_GENERATION` |
| R-12LI-03 | Accidental replacement of `SCRIPT_GENERATION` | Live selector and content route law | Existing content scripts could be misrouted | Require additive binding only | Stop if any new selector rule overrides `SCRIPT_GENERATION` |
| R-12LI-04 | Untested runtime invocation path | Selector binding has not yet happened | Runtime behavior may diverge from repo evidence | Require post-binding validation | Stop if binding is attempted without a validation plan |
| R-12LI-05 | False PASS claim | Prior phase boundaries and checker law | Repo changes could be overstated as runtime completion | Never claim PASS from selector edits alone | Stop if any PASS or governed proof appears |
| R-12LI-06 | Rollback complexity | Active registry promotion history | Selector changes are harder to unwind than docs | Keep rollback explicit and separate | Stop if rollback plan is missing |
| R-12LI-07 | Active registry visibility already present | Phase 12L-H static lint report and active registry files | The promoted film pair is already visible to repo tooling | Treat selector binding as a distinct step | Stop if anyone conflates registry presence with selector binding |
| R-12LI-08 | Need for post-binding validation | Phase 12L-F next-phase recommendation | Bound selector may need additional lint after binding | Require a post-binding validation phase | Stop if binding is proposed without post-binding checks |

## 3. Non-Negotiable Constraints

```text
SCRIPT_GENERATION_must_remain_available=true
FILM_SCREENPLAY_GENERATION_binding_must_be_additive=true
runtime_PASS_must_not_be_claimed_from_selector_edit=true
post_binding_validation_required=true
rollback_plan_required=true
```

