# PATH AND REFERENCE AUDIT

audit_date=2026-05-22
operator_mode=OLD_LOCAL_MAC_CODEX_CHAT
repo_path=/Users/apple/Documents/ShadowCreatorOS_Lightweight

## Command Evidence

```text
command=rg -n "/Users/apple/Documents/ShadowCreatorOS_Lightweight" . --glob '*.md' --glob '*.yaml' --glob '*.json' | wc -l
absolute_path_count=121

command=rg -n "[A-Za-z]:\\\\" . --glob '*.md' --glob '*.yaml' --glob '*.json' | wc -l
old_windows_path_count=1963

command=rg -n "OpenWebUI|old Windows|Windows runtime|n8n_user_restore|ShadowEmpire-Git_Restore|FULL_DOSSIER_ARCHIVE_MODE|DOSSIER" . --glob '*.md' --glob '*.yaml' --glob '*.json' | wc -l
old_runtime_reference_count=2421

command=rg active startup/proof/runtime paths for absolute Mac path, invalid status, and dossier-first conflict strings
active_absolute_path_count=2
active_invalid_status_count=6
active_dossier_first_conflict_count=5
```

## Active Match Line Classification

| Match | File:Line | Classification | Reason |
| --- | --- | --- | --- |
| `/Users/apple/Documents/ShadowCreatorOS_Lightweight` | `AGENT_STARTUP_PROMPT.md:9` | LOCAL_REFERENCE_ONLY | Explicitly marked as `LOCAL_MAC_REFERENCE_ONLY`; active path remains `$SHADOW_REPO_ROOT`. |
| `/Users/apple/Documents/ShadowCreatorOS_Lightweight` | `MAC_06_1A_PREPARATION_RESULT.md:5` | HISTORICAL_REFERENCE | Historical proof result field, not active startup/runtime instruction. |
| `PASS_WITH_NOTICE` | `validators/validate_mac06_1a_output.py:57` | FORBIDDEN_EXAMPLE | Validator rejects this invalid gate status. |
| `PASS_WITH_REFINEMENT` | `validators/validate_mac06_1a_output.py:58` | FORBIDDEN_EXAMPLE | Validator rejects this invalid gate status. |
| `READY_FOR_USER_DECISION` | `validators/validate_mac06_1a_output.py:59` | FORBIDDEN_EXAMPLE | Validator rejects this invalid gate status. |
| `READY_FOR_USER_DECISION` | `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md:49` | FORBIDDEN_EXAMPLE | Contract maps this invalid status to `NEEDS_USER_APPROVAL`. |
| `PASS_WITH_NOTICE` | `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md:50` | FORBIDDEN_EXAMPLE | Contract maps this invalid status to canonical status handling. |
| `PASS_WITH_REFINEMENT` | `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md:51` | FORBIDDEN_EXAMPLE | Contract maps this invalid status to canonical status handling. |
| `Do not create dossier artifacts` | `AGENT_READ_ORDER.md:181` | FORBIDDEN_EXAMPLE | Prohibition, not dossier-first instruction. |
| `Do not create dossier artifacts` | `START_HERE_FOR_AGENTS.md:114` | FORBIDDEN_EXAMPLE | Prohibition, not dossier-first instruction. |
| `Do not create dossier artifacts` | `AGENT_STARTUP_PROMPT.md:98` | FORBIDDEN_EXAMPLE | Prohibition, not dossier-first instruction. |
| `Do not create dossier artifacts` | `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md:136` | FORBIDDEN_EXAMPLE | Prohibition, not dossier-first instruction. |
| `Do not create dossier artifacts` | `MAC_06_1A_UNIVERSAL_AGENT_STARTER_PROMPT.md:38` | FORBIDDEN_EXAMPLE | Prohibition, not dossier-first instruction. |

active_defects_remaining=false

## Classification

missing_reference_count=NEEDS_CONFIRMATION
absolute_path_count=121
old_windows_path_count=1963
old_runtime_reference_count=2421
critical_missing_paths=[]

active_docs_repo_relative=true
historical_absolute_paths_present=true
historical_windows_paths_present=true

## Active Findings

- Active startup docs now use repo-relative paths for the canonical boot order.
- `AGENT_READ_ORDER.md` was converted from absolute Mac paths to repo-relative paths for active read-order entries.
- `registries/agent_runtime_selection_index.yaml` was converted from absolute Mac evidence paths to repo-relative evidence paths.
- Remaining active absolute path references are local-reference disclosures or historical result fields, not runtime commands.
- Invalid gate status strings remain only as forbidden/mapped examples in `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md` and as blocked values in `validators/validate_mac06_1a_output.py`.
- "Do not create dossier artifacts" occurrences are prohibitions, not active dossier-first instructions.

## Critical Missing Paths

critical_missing_paths=none_detected_for_required_active_startup_contract_registry_validator_files

## Status

path_reference_audit_completed=true
active_docs_repo_relative=true
historical_absolute_paths_present=true
path_reference_status=PARTIAL
proof_classification=PARTIAL
reason=Historical absolute paths and old-runtime references remain but active startup docs are repo-relative.
