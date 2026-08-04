# Phase 13C Repo Redesign Implementation Waves

## 1. Objective
Define how to safely redesign the repo without random mass patching.

## 2. Wave table
| Wave | Purpose | Target surfaces | Allowed changes | Forbidden changes | Validation gate | Rollback |
| --- | --- | --- | --- | --- | --- | --- |
| Wave 1 | P0 mythology and content drift blockers | Selected directors and content-heavy skills | Narrow behavior rewrites for the worst drift surfaces | Selector, registry files, schemas, validators, contracts | Diff review against P0 list | Revert Wave 1 commits only |
| Wave 2 | 24-craft director ownership files | directors/ | Reassign craft ownership and role language | Runtime selector, route manifests, route slices | Craft-to-owner coverage review | Revert director docs/logic changes |
| Wave 3 | Agent producer alignment | agents/ | Reframe agent duties to production-house logic | Direct selector or route changes | Agent-to-craft alignment ledger | Revert agent changes only |
| Wave 4 | Subagent department crew alignment | subagents/ | Reassign support roles to department-specific work | Broad content-engine rewrites | Department handoff review | Revert subagent changes only |
| Wave 5 | Skill and subskill execution alignment | skills/, subskills/, .agents/skills/ | Refactor execution techniques to cinema craft | Registry writes, runtime proof claims | Skill-to-craft traceability gate | Revert skill/subskill changes only |
| Wave 6 | Registry, contract, and schema alignment | registries/, runtime_contracts/, schemas/ | Update canonical truth surfaces for cinema core | Unscoped worker rewrites | Registry-contract-schema consistency audit | Revert registry/contract/schema changes |
| Wave 7 | Validation and no-fake-proof alignment | validators/ | Strengthen evidence, PASS, and proof boundaries | Invented runtime proof | Validator coverage gate | Revert validator changes only |
| Wave 8 | Downstream packaging isolation | route packaging surfaces | Separate packaging from cinema core | Film-core authorship leakage | Downstream isolation audit | Revert packaging changes only |

## 3. Scoped patch rule
```text
patches_must_be_wave_scoped=true
unrelated_dirty_files_must_not_be_staged=true
no_mass_rewrite_without_inventory=true
```

## 4. Operating rule
Future implementation must begin from an inventory, a craft ownership map, and a wave gate. No phase should try to rewrite the full repo in one pass.
