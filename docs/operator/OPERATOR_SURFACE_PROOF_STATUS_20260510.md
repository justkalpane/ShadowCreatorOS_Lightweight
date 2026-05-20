# OPERATOR_SURFACE_PROOF_STATUS_20260510

## Scope
Production operator-surface proof under strict path lock (`C:/ShadowEmpire-Git_Restore_01`) only.

## Surface Matrix
| Surface | Entry | Backend Path | Current Status | Evidence |
|---|---|---|---|---|
| PowerShell Operator | `scripts/operator/new-content-job.ps1` | Operator API `:5002` -> WF chain -> skill-runtime -> packets | PROVEN_WORKFLOW_OPERATOR | Multiple dossiers with creative families |
| Operator API Direct | `POST /operator/new-content-job` | Same as above | PROVEN_WORKFLOW_OPERATOR | Timeline/packet evidence + `list-outputs` |
| n8n Runtime Chain | WF-001/010/100/200/300/400/500/600/020 | CWF -> `/operator/skill-runtime` | PROVEN | 22/22 CWF active, no fetch, no direct skill_loader import |
| Ollama Direct (`/api/generate`) | Ollama API only | Model output only | MODEL_ONLY_SMOKE_TEST | Not used as workflow proof |
| Ollama Bridge | `npm run operator:ollama -- "<prompt>"` | `operator/ollama_tool_runner.js` -> `/operator/new-content-job` -> n8n | PROVEN_WORKFLOW_OPERATOR | Dossier `DOSSIER-1778415612095-A1DPBL0YY` |
| Open WebUI Bridge | Open WebUI tool function path | `config/open_webui_tools.json` -> Operator API `:5002` | CONFIGURED_READY_FOR_MANUAL_UI_PROOF | Tool config points to `5002`; service not reachable at `:3000` in this run |
| Command Center / chat-layer | `/chat` custom UI path | chat-layer internals | QUARANTINED | Explicit policy/quarantine |

## Ollama Bridge Proof
- Command used:
  - `npm.cmd run operator:ollama -- "Create a YouTube script about AI vs Human with hook, intro, research summary, debate/critique, refined script, context engineering packet JSON, thumbnail plan, metadata."`
- Dossier ID:
  - `DOSSIER-1778415612095-A1DPBL0YY`
- Timeline/packet evidence:
  - `timeline_count: 51`
  - `packets_count: 52`
- Creative families confirmed via `scripts/operator/list-outputs.ps1`:
  - `research_packet`
  - `script_packet`
  - `debate_packet`
  - `refined_script_packet`
  - `context_packet`
  - `thumbnail_packet`
  - `metadata_packet`
- Error signal:
  - no matching dossier entry found in `data/se_error_events.json`

## Open WebUI Status
- Config file (`config/open_webui_tools.json`) points to `http://localhost:5002/operator/*` (correct).
- Runtime launcher (`scripts/windows/start_openwebui_local_runtime.ps1`) points Operator health to `5002` (correct).
- Documentation still includes legacy `5050` references in `docs/operator/OPEN_WEBUI_INTEGRATION_SETUP.md` (doc drift only).
- Open WebUI process binaries exist, but HTTP `http://localhost:3000` did not become reachable in this run.

### Manual UI Proof Steps (required)
1. Start from `C:\ShadowEmpire-Git_Restore_01` and run `scripts/windows/assert_restore01_path.ps1`.
2. Start Open WebUI runtime and verify `http://localhost:3000` responds.
3. Import/use tool definitions from `config/open_webui_tools.json`.
4. Submit content prompt from Open WebUI chat.
5. Capture returned `dossier_id`.
6. Validate with:
   - `scripts/operator/inspect-output.ps1 <DOSSIER_ID>`
   - `scripts/operator/list-outputs.ps1 <DOSSIER_ID>`
7. PASS only if creative families are visible.

## Current Production Classification
- `FULL_CREATIVE_CHAIN_PROVEN (local-only, Restore_01 path-locked)`
- `Ollama bridge: PROVEN_WORKFLOW_OPERATOR`
- `Open WebUI: CONFIGURED_READY_FOR_MANUAL_UI_PROOF`
- `Old repo: QUARANTINED`

## Next Step
- Git staging audit can be prepared next, but only for proven runtime/docs changes.

## Open WebUI Real-Time Proof Update (2026-05-10)

- Open WebUI reachable at `http://localhost:3000` (HTTP 200).
- Authenticated Open WebUI chat completions with `tool_ids=["shadow_empire"]` were executed successfully.
- Found stale installed tool payload in Open WebUI DB (`shadow_empire`) still using `localhost:5050`.
- Patched installed tool payload to `localhost:5002` via Open WebUI admin API after backup:
  - `C:\ShadowEmpire\openwebui_tool_backups\shadow_empire_tool_20260510_190245.json`

### Open WebUI Content Job Proof
- Dossier created from Open WebUI tool path:
  - `DOSSIER-1778421046157-DSZARL0K5`
- Output evidence:
  - `timeline_count=51`
  - `packets_count=52`
  - Creative families present:
    - `research_packet`
    - `script_packet`
    - `debate_packet`
    - `refined_script_packet`
    - `context_packet`
    - `thumbnail_packet`
    - `metadata_packet`

### Replay / Remodify from Open WebUI
- `request_changes` (remodify) tool path is currently partial:
  - `/operator/remodify/:id` returned `workflow_id=WF-020` in this runtime.
- `replay_stage` tool path proved replay route:
  - `/operator/replay/:id` returned `workflow_id=WF-021`.
  - Timeline/packet delta observed (`51/52` -> `59/60`).

### Updated Surface Classification
- Open WebUI bridge: `PROVEN_WORKFLOW_OPERATOR` (API-path proof complete).
- Open WebUI request_changes/remodify semantics: `PARTIAL` (WF-020 mapping behavior).
- Command Center remains `QUARANTINED`.

## Open WebUI Classification Correction (2026-05-10)

- Downgraded prior label `USER_VISIBLE_PRODUCTION_READY`.
- Corrected classification:
  - `API_VISIBLE_OPENWEBUI_TOOL_PROVEN`
  - `UI_BINDING_NOT_PROVEN`
  - `MANUAL_UI_ACTION_REQUIRED`
- Reason: backend tool execution is proven, but direct human browser click-path proof was not automated in-session.

### Binding hardening applied
- Created model preset `shadow-creator-os` with `meta.toolIds=["shadow_empire"]`.
- Created 6 visible prompt templates:
  - `shadow_full_content_job`
  - `shadow_research_packet`
  - `shadow_script_mode`
  - `shadow_thumbnail_metadata`
  - `shadow_replay_remodify`
  - `shadow_dossier_inspect`

### Tool payload drift closure
- Open WebUI installed tool payload corrected from `5050` to `5002`.
- Backup: `C:\ShadowEmpire\openwebui_tool_backups\shadow_empire_tool_20260510_190245.json`.

### Chat-history visibility truth
- Stateless `/api/chat/completions` calls without chat metadata do not create sidebar chat rows.
- DB count check remained `2 -> 2` after such call.

## UI-Binding Progress Update (2026-05-10)

- User screenshot confirms visible `Shadow Creator OS` preset + `Shadow` category + tool indicator (`1`) in Open WebUI composer.
- Classification advanced to:
  - `UI_BINDING_PARTIALLY_PROVEN`
  - `SHADOW_CREATOR_OS_MODEL_VISIBLE`
  - `TOOL_ATTACHMENT_VISIBLE`
  - `FINAL_BROWSER_CHAT_PROOF_PENDING`

Open WebUI runtime evidence:
- preset model `shadow-creator-os` present with `meta.toolIds=["shadow_empire"]`.
- six Shadow prompt templates present.
- new persistent chat rows are now created when metadata fields are included.
- latest tool-path dossiers:
  - `DOSSIER-1778424897109-C8WQ7MKO7`
  - `DOSSIER-1778424898457-WDFXVBVXX`
- both show full creative packet families and replay delta evidence.

Command Center replacement remains pending final human-visible browser chat proof.

## Direct Router Update (2026-05-10 22:10 IST)

- Browser chat failure mode confirmed from Open WebUI DB chat records:
  - model replied with advisory guidance while tool payload appeared only in `sources`.
  - classification: `TOOL_NOT_AUTO_INVOKED_FROM_BROWSER_CHAT`.
- Deterministic router created:
  - function: `shadow_creator_os_direct_pipe` (`type=pipe`)
  - preset model: `shadow-creator-os-direct`
  - install script: `scripts/operator/install-openwebui-direct-router.ps1`
  - Open WebUI DB backup: `C:\ShadowEmpire\openwebui_direct_router_backup\20260510_221026\webui.db.bak`
- Direct router execution proof:
  - dossier: `DOSSIER-1778431713532-OEAM4U6OV`
  - timeline `37` -> replay `53`
  - packets `49` -> replay `54`
  - creative families visible (`research_packet`, `script_packet`, `debate_packet`, `refined_script_packet`, `context_packet`, `thumbnail_packet`, `metadata_packet`)
- Open WebUI classification now:
  - `DIRECT_ROUTER_CREATED_BUT_MANUAL_TEST_PENDING`
  - `TOOL_CHOICE_MODE_FAILED`
  - `MANUAL_UI_ACTION_REQUIRED`

## 2026-05-11 Materialization Gate
- Previous gap (body content missing) is fixed in skill runtime.
- Fresh API dossier: DOSSIER-1778442163263-Q4SQUTJTF (timeline=51, packets=52).
- Fresh Direct Router dossier: DOSSIER-1778442208010-7GL24QGWS (timeline=51, packets=55).
- Runtime errors: 0.
- Required packet families + creator body fields present.
- Classification: SKILL_RUNTIME_GENERATION_FIXED / CREATOR_OUTPUT_MATERIALIZED.
- Timestamp: 2026-05-11 01:16:06 +05:30


## 2026-05-11 Cloud-Intelligence Audit
- Surface routing remains PASS; cloud intelligence remains UNPROVEN in no-key mode.
- Provider router now wired with explicit skip/fallback metadata.
- Latest no-key dossier: DOSSIER-1778443710533-NIPXV8FUP.
- Classification: LOCAL_MATERIALIZATION_ONLY / PROVIDER_ROUTER_READY_NO_KEYS.
- Timestamp: 2026-05-11 01:39:55 +05:30


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
