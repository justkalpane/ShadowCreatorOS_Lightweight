# PRODUCTION_REPO_DRIFT_AUDIT_20260510

## Incident Summary
- Drift incident confirmed: work was executed from `C:\ShadowEmpire-Git` while production baseline is `C:\ShadowEmpire-Git_Restore_01`.
- Runtime services are still aligned to production profile evidence (`C:\ShadowEmpire\n8n_user_restore_01`), but wrong-repo patch activity did occur.

## Canonical Production Paths
- Production repo: `C:\ShadowEmpire-Git_Restore_01`
- Stale/forensic repo: `C:\ShadowEmpire-Git`
- Production n8n profile: `C:\ShadowEmpire\n8n_user_restore_01`
- Old profile: `C:\ShadowEmpire\n8n_user` (absent on disk)

## Active Runtime Evidence
- Port listeners:
  - `5002` -> PID `19744` (`node.exe`)
  - `5678` -> PID `19636` (`node.exe`)
  - `11434` -> PID `7752` (`ollama.exe`)
- Windows process command-line introspection (`Get-CimInstance`, `Get-WmiObject`) returned access denied in this session.
- Operator API route verification:
  - `POST /operator/skill-runtime` returns `SUCCESS` with `runtime_packet`.
  - This route exists in `Restore_01` operator API implementation and is absent in old repo `engine/api/operator.js`.
- Live n8n DB verification (`C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite`):
  - 22/22 CWF workflows active.
  - 22/22 CWF workflows have non-null `activeVersionId`.
  - 22/22 CWF workflow JSON payloads include `/operator/skill-runtime` and `axios`.
  - 0 workflows include `fetch(`.
  - 0 workflows include direct `skill_loader` import.

## Git Root Comparison
| Repo Path | Branch | HEAD | Dirty Files Count | Classification |
|---|---|---|---:|---|
| `C:\ShadowEmpire-Git_Restore_01` | `recovery/runtime-lock-20260506` | `aca5c63 docs: add final recovery branch status handoff` | high (runtime + workflow + docs + untracked) | `PRODUCTION_RESTORE_01` |
| `C:\ShadowEmpire-Git` | `main` | `0447c2f docs: add comprehensive dossier propagation fix guide for Phase 9` | high (legacy + runtime + untracked) | `OLD_REPO_DRIFT` |

## Critical File Comparison (Old vs Production)
| File | Same/Different | Production Has Latest Fix? | Old Repo Has Unreviewed/Drifted State? | Action Needed |
|---|---|---|---|---|
| `engine/api/operator.js` | Different | Yes (`/operator/skill-runtime` present) | Yes | Keep production; quarantine old |
| `operator/output_reader.js` | Different | Yes | Yes | Keep production; quarantine old |
| `operator/n8n_execution_reconciler.js` | Different (old missing) | Yes | Yes | Keep production |
| `operator/skill_runtime.js` | Different (old missing) | Yes | Yes | Keep production |
| `operator/ollama_tool_runner.js` | Different | Yes | Yes (wrong-repo edited during incident) | Do not trust old repo |
| `config/open_webui_tools.json` | Different | Yes (`5002`) | Yes (wrong-repo edited during incident) | Keep production only |
| `scripts/windows/start_n8n_shadow_phase1.ps1` | Different | Yes (`restore_01` profile + `NODE_FUNCTION_ALLOW_EXTERNAL=axios`) | Yes | Keep production only |
| `scripts/windows/start_shadow_operator_api.ps1` | Different | Yes (`5002` canonical) | Yes | Keep production only |
| `scripts/windows/start_openwebui_local_runtime.ps1` | Different | Yes | Yes | Keep production only |
| `docs/operator/REALTIME_DEPLOYMENT_OPERATOR_TEST_STATUS_20260507.md` | Different (old missing) | Yes | Yes | Keep production only |

## Legacy Port/Path Drift Findings
- Production repo still contains some legacy `5050` references in non-canonical helper files:
  - `config/openwebui_shadow_operator_tools*.py`
  - `operator/mcp/shadow_operator_mcp_server.js`
  - `scripts/windows/start_open_webui.ps1`
- Canonical production files already aligned to `5002`:
  - `config/open_webui_tools.json`
  - `scripts/windows/start_shadow_operator_api.ps1`
  - `scripts/windows/start_openwebui_local_runtime.ps1`
  - `scripts/windows/start_n8n_shadow_phase1.ps1`

## Drift Classification
- **Primary classification:** `WRONG_REPO_PATCH_ONLY`
- Runtime proof remains tied to production profile DB and active workflow content.
- Additional process-path certainty is limited by local permission denial for command-line inspection.

## Validity of FULL_CREATIVE_CHAIN Proof
- `FULL_CREATIVE_CHAIN_PROVEN (local-only)` remains valid against production runtime evidence because:
  - Live DB in `n8n_user_restore_01` contains patched CWF state.
  - Active workflows show boundary fix (`/operator/skill-runtime`) and no blocked import/fetch pattern.
  - Operator API currently serves `POST /operator/skill-runtime` successfully.

## Safe Correction Plan
1. Freeze non-production repo (`C:\ShadowEmpire-Git`) for runtime work.
2. Treat all old-repo modified files as quarantined and non-deployable.
3. Continue all runtime commands only from `C:\ShadowEmpire-Git_Restore_01`.
4. Perform any future endpoint/script/doc patching in `Restore_01` only.
5. Add a short repo guard step to every runbook:
   - verify `git rev-parse --show-toplevel` equals `C:/ShadowEmpire-Git_Restore_01` before execution.
6. Re-run one controlled production proof from `Restore_01` before Open WebUI/Ollama bridge expansion.

## Next Allowed Step
- Resume operator-surface testing only after explicit confirmation that terminal working directory and git root are `C:\ShadowEmpire-Git_Restore_01`.

## Path-Lock Revalidation (2026-05-10 17:22:53 +05:30)

- Preflight root lock: C:/ShadowEmpire-Git_Restore_01 (PASS)
- Branch: ecovery/runtime-lock-20260506
- HEAD: ca5c63 docs: add final recovery branch status handoff
- Canonical health: Operator API 200, n8n 200, Ollama 200 (PASS)
- Direct skill-runtime probe: PASS (POST /operator/skill-runtime returns SUCCESS)
- Live n8n DB (C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite) CWF check:
  - total=22, active=22, activeVersion=22
  - uses /operator/skill-runtime=22
  - uses axios=22
  - contains etch(=0
  - contains direct skill_loader import=0
- Fresh Restore_01 validation dossier: $did
  - timeline_count=51
  - packets_count=52
  - runtime_error_packet observed: 0 (no new runtime error evidence in inspect/list output)
  - required creative families visible: esearch_packet, script_packet, debate_packet, efined_script_packet, context_packet, 	humbnail_packet, metadata_packet

### Drift Verdict Update

- Drift incident remains: old repo C:\ShadowEmpire-Git was touched accidentally.
- Production runtime evidence remains Restore_01-aligned.
- Full proof classification retained as:
  - FULL_CREATIVE_CHAIN_PROVEN (local-only, Restore_01 path-locked)
- Next allowed step: Ollama bridge proof from C:\ShadowEmpire-Git_Restore_01 only.

## Repo Reconciliation Closure (2026-05-10)

- Reconciliation mission completed under path-lock.
- Old repo `C:\ShadowEmpire-Git` remains quarantined.
- No old-only runtime-critical files were required for production continuity.
- Migrated old-only reference evidence bundle:
  - `docs/recovery/GRAPH_PARITY_AUDIT_20260506_CURRENT/*`
- Added path-lock controls in production repo:
  - `scripts/windows/assert_restore01_path.ps1`
  - startup scripts now invoke the guard.
- Post-change validation PASS:
  - path-lock guard PASS
  - Operator API 200, n8n 200, Ollama 200
  - direct `/operator/skill-runtime` PASS
  - fresh proof dossier: `DOSSIER-1778414996783-0NSODRPXU`
  - timeline_count=51, packets_count=52
  - creative families visible (`research_packet`, `script_packet`, `debate_packet`, `refined_script_packet`, `context_packet`, `thumbnail_packet`, `metadata_packet`)

Final drift status:
- `C:\ShadowEmpire-Git_Restore_01` = production source of truth
- `C:\ShadowEmpire-Git` = forensic/stale only

## Operator Surface Proof Update (2026-05-10)

- Path lock preflight: PASS (`C:/ShadowEmpire-Git_Restore_01`)
- Health: Operator API 200, n8n 200, Ollama 200
- Ollama bridge command executed from Restore_01:
  - `npm.cmd run operator:ollama -- "Create a YouTube script about AI vs Human with hook, intro, research summary, debate/critique, refined script, context engineering packet JSON, thumbnail plan, metadata."`
- Bridge dossier: `DOSSIER-1778415612095-A1DPBL0YY`
- Evidence:
  - `timeline_count=51`
  - `packets_count=52`
  - creative families confirmed (`research_packet`, `script_packet`, `debate_packet`, `refined_script_packet`, `context_packet`, `thumbnail_packet`, `metadata_packet`)
- Ollama bridge classification: `PROVEN_WORKFLOW_OPERATOR`
- Open WebUI:
  - config path to `5002`: PASS
  - service reachability (`http://localhost:3000`): not reachable in this run
  - classification: `CONFIGURED_READY_FOR_MANUAL_UI_PROOF`
- Command Center/chat-layer remains quarantined.

## Open WebUI Surface Drift Closure (2026-05-10)

- Verified Open WebUI service is reachable at `http://localhost:3000`.
- Verified Open WebUI installed tool bundle `shadow_empire` had stale endpoint drift (`localhost:5050`) despite repo config already at `5002`.
- Applied in-place Open WebUI tool payload correction via admin API after backup:
  - `C:\ShadowEmpire\openwebui_tool_backups\shadow_empire_tool_20260510_190245.json`
- Re-validated Open WebUI command path by executing chat-completions with tool calls and producing a new dossier:
  - `DOSSIER-1778421046157-DSZARL0K5`
  - `timeline_count=51`, `packets_count=52`, required creative families visible.

Drift status remains controlled:
- Production repo: `C:\ShadowEmpire-Git_Restore_01`
- Old repo: `C:\ShadowEmpire-Git` quarantined
- Open WebUI runtime now aligned to production `:5002` endpoint path.

## Open WebUI Runtime Binding Addendum (2026-05-10)

- Runtime store and UI-binding were hardened in production profile:
  - Installed `shadow_empire` tool payload endpoint corrected to `localhost:5002`.
  - New Open WebUI preset model `shadow-creator-os` created with `meta.toolIds=["shadow_empire"]`.
  - Six Shadow operator prompt templates created for visible user shortcuts.
- This does not alter repo-path drift classification; old repo remains quarantined.

## Open WebUI UI-Binding Drift Follow-up (2026-05-10)

- Confirmed browser-visible `Shadow Creator OS` preset and tool indicator after runtime binding fixes.
- Added runtime preset model (`shadow-creator-os`) and prompt templates in Open WebUI store.
- Old repo quarantine unchanged; production path-lock unchanged.
- Remaining gate is final user-visible browser-chat output confirmation.

## Open WebUI Direct Router Hardening (2026-05-10 22:10 IST)

- Applied from path-locked production repo only:
  - `C:/ShadowEmpire-Git_Restore_01`
- Added deterministic Open WebUI pipe runtime artifact:
  - `config/openwebui_shadow_creator_os_direct_pipe.py`
- Added installer:
  - `scripts/operator/install-openwebui-direct-router.ps1`
- Installed Open WebUI runtime entries with DB backup:
  - backup: `C:\ShadowEmpire\openwebui_direct_router_backup\20260510_221026\webui.db.bak`
  - function: `shadow_creator_os_direct_pipe` (`type=pipe`, active)
  - model: `shadow-creator-os-direct` (base model id points to direct pipe)

Validation snapshot:
- Direct router produced dossier `DOSSIER-1778431713532-OEAM4U6OV`
- replay against same dossier produced `WF-021` evidence and packet/timeline delta
- required creative packet families remained visible

Drift status unchanged:
- production repo remains `C:\ShadowEmpire-Git_Restore_01`
- old repo `C:\ShadowEmpire-Git` remains quarantined

## 2026-05-11 Follow-up (Materialization Fix)
- Patch executed under path-lock (C:/ShadowEmpire-Git_Restore_01) only.
- No old-repo mutation.
- Verified creator body fields now materialize in fresh dossiers.
- Timestamp: 2026-05-11 01:16:19 +05:30


## 2026-05-11 n8n Gemini Credential + WF-950 Proof Update
- timestamp: 2026-05-11 13:51:21
- repo_root: C:/ShadowEmpire-Git_Restore_01
- n8n_profile: C:/ShadowEmpire/n8n_user_restore_01/.n8n/database.sqlite
- credential_saved: true
- credential_meta: id=xgzfFBdjjmxYxLnW, name=Google Gemini(PaLM) Api account, type=googlePalmApi
- wf950_import: success (workflow id WF950GemSmkTst01)
- wf950_execution: success (execution id 1568, mode=cli)
- wf950_provider_path: n8n credential (googlePalmApi)
- secret_exposure: false
- note: Gemini node response was truncated by max tokens in smoke test, but credential-backed call and token usage succeeded.

### Production route re-check
- dossier_id: DOSSIER-1778487364691-DLODCL7BJ
- timeline_count: 51
- packets_count: 52
- required_families_present: true
- packet metadata sample shows: provider_used=gemini, model_used=gemini-2.5-flash, cloud_provider_used=true
- runtime_error_packet_count: 0
