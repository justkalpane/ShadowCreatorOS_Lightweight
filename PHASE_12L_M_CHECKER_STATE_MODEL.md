# Phase 12L-M Checker State Model

## 1. Objective
Define validation states across the route lifecycle.

## 2. State model

| State | Registry pair exists? | Selector bound? | Correct checker | Expected status |
|---|---|---|---|---|
| Draft only | No | No | Pre-promotion checker | `PRE_PROMOTION_READY_FOR_OWNER_DECISION` |
| Active registry promoted, selector unbound | Yes | No | Post-promotion registry checker | `POST_PROMOTION_REGISTRY_VALIDATED_REPO_LEVEL` |
| Active registry promoted, selector bound | Yes | Yes | Post-selector-binding checker | `POST_SELECTOR_BINDING_VALIDATED_REPO_LEVEL` |
| Repo-level post-binding validated | Yes | Yes | Post-selector-binding checker | `POST_SELECTOR_BINDING_VALIDATED_REPO_LEVEL` |
| Governed runtime proof requested | Yes | Yes | Runtime-proof checker | `RUNTIME_PROOF_REQUIRED` |
| Governed runtime proof passed | Yes | Yes | Runtime-proof checker | `GOVERNED_RUNTIME_PROOF_RETURNED` |
| Governed runtime proof blocked | Yes | Yes | Runtime-proof checker | `RUNTIME_PROOF_BLOCKED` |

## 3. Required status names

```text
PRE_PROMOTION_READY_FOR_OWNER_DECISION
POST_PROMOTION_REGISTRY_VALIDATED_REPO_LEVEL
POST_SELECTOR_BINDING_VALIDATED_REPO_LEVEL
RUNTIME_PROOF_REQUIRED
RUNTIME_PROOF_BLOCKED
GOVERNED_RUNTIME_PROOF_RETURNED
```

## 4. No-fake-proof law

```text
repo_level_validation_must_not_claim_runtime_PASS=true
governed_runtime_proof_required_for_completion=true
```

