# REALTIME DEPLOYMENT OPERATOR TEST STATUS (2026-05-07)

## Executive Verdict
Control plane is working, but Operator API output/timeline currently reflect snapshot records, not full creative packet depth per dossier.

## Dossiers Verified
- DOSSIER-1778338210762-POK4YT1R0
- DOSSIER-1778339037237-2T49HGK88
- DOSSIER-1778339158963-ZSLONPP79

## Placeholder Error Corrected
Earlier zero results using `<NEW_DOSSIER_ID>` were invalid. Re-run was performed with real dossier IDs.

## Service Health (live)
- Operator API (`http://localhost:5002/operator/health`): PASS
- n8n (`http://localhost:5678`): PASS
- Ollama (`http://localhost:11434/api/tags`): PASS
- `check-shadow-health.ps1`: Critical checks passed 8/8

## Operator API Results (real dossier)
For `DOSSIER-1778338210762-POK4YT1R0`:
- `GET /operator/dossier/:id/timeline`: `timeline_count=3`
- `GET /operator/outputs/:id`: `packets_count=1`
- Only packet: `orchestration_status_packet`

`inspect-output.ps1` and `list-outputs.ps1` both return a valid summary for this dossier and match API results.

## Local Index Evidence
### data/se_dossier_index.json
All 3 dossiers are present and marked `approved`.

### data/se_route_runs.json
For each dossier, exactly 2 run records exist:
- WF-001 queued
- WF-010 queued
Source: `operator_api_snapshot`

### data/se_packet_index.json
For each dossier, exactly 1 linked packet exists:
- `orchestration_status_packet` (source `operator_api_snapshot`)

### data/se_approval_queue.json
No rows for these dossiers.

### data/se_error_events.json
No rows for these dossiers.

## n8n DB Execution Evidence (read-only verification)
Active DB: `C:\ShadowEmpire\n8n_user_restore_01\.n8n\database.sqlite`

All three dossiers show successful execution chain:
- WF-001 success
- WF-010 success
- WF-100 success
- WF-200 success
- WF-300 success
- WF-400 success
- WF-500 success
- WF-600 success
- WF-020 success
- WF-021 success (replay evidence found for `DOSSIER-1778339158963-ZSLONPP79`)

Conclusion: n8n workflow chain executes successfully, but dossier-scoped operator outputs remain snapshot-only.

## Root Cause Classification
- OPERATOR_API_QUEUES_BUT_DOES_NOT_TRACK_N8N
- FAKE_OR_LOCAL_EXECUTION_IDS
- OUTPUT_READER_TOO_NARROW
- PAYLOAD_CONTRACT_MISMATCH (packet dossier linkage missing in deeper packets)
- REPLAY_ONLY_QUEUES_WF021_NOT_TARGET (at API semantics layer)

## File-Level Implementation Truth
### `engine/api/operator.js`
- `/operator/new-content-job` triggers WF-001 and WF-010.
- Then writes local snapshot rows via:
  - `appendRouteRunSnapshot(...)`
  - `appendPacketSnapshot(...)`
- Response returns accepted with provider boundary note.

### `engine/chat/n8n_workflow_client.js`
- execution_id fallback:
  - `response.data.execution_id || response.data.executionId || exec-...`
- This can produce local/generated IDs when webhook does not return canonical execution id.

### `operator/output_reader.js`
- `getDossierOutputs` and timeline filter packets/runs strictly by `dossier_id|dossier_ref`.
- If deeper packets are produced without dossier linkage, they are excluded from dossier outputs/timeline.

### `operator/review_manager.js`
- replay calls WF-021 trigger only; does not directly trigger target workflow in API layer.

## Ollama/Open WebUI Reality
- Direct Ollama `/api/generate` alone = model-only smoke test.
- `operator/ollama_tool_runner.js` is a real bridge path and calls `/operator/new-content-job` for content tasks.
- `config/open_webui_tools.json` is configured to call Operator API `:5002` endpoints.
- Open WebUI path remains configured; runtime proof should be captured with dossier-linked evidence.

## Minimal Repair Plan
1. Operator API tracking patch:
   - Persist real n8n execution IDs (or mark unresolved explicitly).
   - Add completion tracking (poll/callback) for WF-010 chain and child statuses.
2. Packet linkage patch:
   - Ensure child pack packet writes include `dossier_id`/`dossier_ref` consistently.
3. Output reader enhancement:
   - Optionally surface chain packets by route/execution correlation when dossier linkage is missing.
4. Replay semantics patch:
   - Clarify and/or implement target workflow replay behavior beyond WF-021 trigger-only queue response.

## Next Test (after patch)
Single PowerShell job on one topic, then verify:
- timeline count grows beyond 3 with child workflow events
- packet count includes script/context/research/metadata families
- replay causes new output deltas tied to same dossier

## Safety
No staging, commit, push, pull, reset, or clean performed in this verification pass.

## 2026-05-09 Reconciliation Patch Pass

### Patch scope (operator layer only)
- Added `operator/n8n_execution_reconciler.js`
- Updated `operator/output_reader.js`
- Updated `engine/api/operator.js` routes to await async output/timeline readers

### Backup path
- `C:\ShadowEmpire\operator_output_reconcile_backup\20260509_221417`

### What was fixed
- Timeline no longer depends only on local route snapshot records.
- Output view no longer depends only on directly-linked packet rows.
- Added live n8n execution evidence reconciliation from SQLite for each dossier.
- Added synthetic `workflow_execution_event` packet family for operator visibility.
- Added time-window reconciliation for orphan workflow completion packets that missed `dossier_ref` linkage.

### Validation on historical dossiers (direct module validation)
- `DOSSIER-1778338210762-POK4YT1R0`
  - timeline_count: 25
  - execution_events_count: 22
  - packets_count: 24
  - families: `orchestration_status_packet`, `publishing_distribution_result`, `workflow_execution_event`
- `DOSSIER-1778339037237-2T49HGK88`
  - timeline_count: 25
  - execution_events_count: 22
  - packets_count: 24
  - families: `orchestration_status_packet`, `publishing_distribution_result`, `workflow_execution_event`
- `DOSSIER-1778339158963-ZSLONPP79`
  - timeline_count: 26
  - execution_events_count: 23
  - packets_count: 25
  - families: `orchestration_status_packet`, `publishing_distribution_result`, `workflow_execution_event`

### Creative depth evidence status
- n8n DB confirms deep workflow execution success (WF-100/200/300/400/500/600/020 and WF-021 replay).
- Operator output now exposes execution depth evidence and reconciled completion packet evidence.
- Creative payload families (script/research/debate/context/thumbnail/metadata) are still not materialized as dossier-linked packet families in operator outputs.

### Current classification
- `RUNTIME_CHAIN_WITH_OUTPUT_RECONCILIATION`
- Not yet `FULL_CREATIVE_CHAIN_PROVEN`

### Remaining gap
- Child workflow packet materialization contract is incomplete/inconsistent for dossier-linked creative families.
- WF-500 completion packets were present but missing dossier linkage until reconciliation.
- Next minimal target: standardize packet persistence for WF-100/WF-200/WF-300/WF-400/WF-600 completion outputs with required `dossier_id`/`dossier_ref` and normalized family mapping.

## 2026-05-09 Fresh Post-Patch Validation (Controlled)

### Listener Unavailable Root Cause
- Root cause: n8n listener was down after environment restart while Operator API was still running.
- Observed state:
  - `http://localhost:5002/operator/health` => `503` degraded
  - `http://127.0.0.1:5678` => unreachable
- Restoration performed:
  - restarted n8n on canonical profile (`C:\ShadowEmpire\n8n_user_restore_01`) with canonical env contract
  - verified operator health returned to `200` healthy after n8n recovery

### New Controlled Validation Run
- New dossier: `DOSSIER-1778346329330-5B9Z7C90C`
- Entry path:
  - `POST /operator/new-content-job` accepted
  - WF-001 queued HTTP 200
  - WF-010 queued HTTP 200

### Polling Result (12 cycles / 2 minutes)
- timeline_count stabilized at `25`
- execution_events_count stabilized at `22`
- packets_count stabilized at `24`
- visible families:
  - `orchestration_status_packet`
  - `publishing_distribution_result`
  - `workflow_execution_event`

### Fresh Dossier Output Scripts
- `inspect-output.ps1` PASS
- `list-outputs.ps1` PASS
- output groups remain exactly 3 families listed above

### Creative Packet Materialization Verdict
- Not proven for fresh dossier.
- Still missing dossier-materialized creative families:
  - `research_packet`
  - `script_packet`
  - `debate_packet`
  - `refined_script_packet`
  - `context_packet`
  - `thumbnail_packet`
  - `metadata_packet`

### n8n Execution Payload Evidence (Fresh Dossier)
- Deep chain executions present and successful:
  - WF-001/010/100/200/300/400/500/600/020
- Decoded execution payloads show:
  - WF-100 and WF-200 parent runs stop at first execute-workflow step (`Execute CWF-110` / `Execute CWF-210`) in runData trace.
  - CWF-110 and CWF-210 execute through append-only nodes but do not materialize creative packet outputs in operator-visible packet families.
  - WF-020 emits approval packet family (`approval_decision_packet` / `workflow_completion_packet`) in execution payload context.

### Gap Classification (Fresh)
- `PACKET_WRITER_MISSING` (for creative families in operator-visible packet index)
- `CREATIVE_CONTENT_EXISTS_BUT_UNLINKED` (some completion packets require reconciliation)
- `OUTPUT_READER_STILL_TOO_NARROW` for creative-family materialization from runData payloads
- `PAYLOAD_CONTRACT_MISMATCH` in parent/child output propagation for WF-100/WF-200 branch

### Minimal Next Repair (No Workflow Rewrite Yet)
1. Extend operator reconciliation to decode flatted n8n execution payload (`execution_data.data`) and ingest candidate `completion_packet`/`runtime_packet` families into dossier outputs.
2. Add canonical family mapper:
   - `topic_intelligence_result -> research_packet`
   - `script_intelligence_result -> script_packet`
   - `context_engineering_result -> context_packet`
   - plus pass-through for approval/replay families.
3. Add strict dossier-link reconciliation for decoded packets when `dossier_ref` is null using execution-window + execution id mapping.
4. Re-test one fresh dossier.
5. Only if creative families still absent after payload decode: patch WF-100/WF-200 and CWF-110/CWF-210 output contract to emit explicit creative packets.

### Classification Update
- Current: `RUNTIME_CHAIN_WITH_OUTPUT_RECONCILIATION`
- Not yet: `FULL_CREATIVE_CHAIN_PROVEN`


## 2026-05-09 Creative Packet Materialization Validation Update (2026-05-09T18:22:56.442Z)

### Scope
- Fresh controlled dossier run after reconciliation updates.
- Runtime-error extraction enabled from n8n execution_data to expose hidden CWF failures.

### New Validation Dossier
- DOSSIER-1778348153821-YRJ2PCLWB

### Service Health
- Operator API http://localhost:5002/operator/health => 200
- n8n http://127.0.0.1:5678 => 200
- Ollama http://localhost:11434/api/tags => 200

### Post-Patch Polling Result (12 cycles)
- timeline_count: 78 (stable)
- packets_count: 77 (stable)
- execution_events_count: 22
- runtime_errors_count: 53
- Packet families visible:
  - orchestration_status_packet
  - publishing_distribution_result
  - workflow_execution_event
  - runtime_error_packet

### Root Cause Confirmed From Execution Payloads
- Child workflows report execution_status=success at workflow level, but node-level runtime carries hard failures.
- Repeated runtime error in CWF skill nodes:
  - Module '../../../engine/skill_loader/skill_loader.js' is disallowed [line 2]
- This blocks runtime_packet emission and blocks creative packet materialization (research/script/refined/context/thumbnail/metadata families).

### Replay/Remodify Probe
- Replay request accepted (status=queued).
- Visible delta after replay wait:
  - packets: 78 -> 79
  - timeline: 79 -> 80
  - execution events: 23 -> 24
- Runtime error count unchanged (53), and no new creative families appeared.

### Classification Update
- RUNTIME_CHAIN_WITH_OUTPUT_RECONCILIATION: PASS
- CREATIVE_PACKET_MATERIALIZATION: FAIL (blocked by child skill-loader runtime error)
- Gap classification:
  - CHILD_WORKFLOWS_STUB_ONLY (effective behavior under current runtime constraints)
  - PACKET_WRITER_MISSING (creative families not emitted)
  - PAYLOAD_CONTRACT_MISMATCH (workflow success masking node-level runtime failure)

### Minimal Next Repair
1. Replace disallowed local-module require path in CWF skill nodes with an n8n-allowed execution path.
2. Ensure CWF runtime_packet is non-null and dossier-linked.
3. Ensure WF-100/WF-200 completion nodes execute and emit dossier-linked packets.
4. Revalidate required families:
   - research_packet
   - script_packet
   - refined_script_packet
   - context_packet
   - thumbnail_packet
   - metadata_packet

### Files Patched In This Update
- operator/n8n_execution_reconciler.js
- operator/output_reader.js

### Backup Path
- C:\ShadowEmpire\creative_packet_materialization_backup\20260509_225610

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

## Open WebUI Real-Time Command Surface Validation (2026-05-10)

### Service Status
- Operator API: 200 (`http://localhost:5002/operator/health`)
- n8n: 200 (`http://localhost:5678`)
- Ollama tags: 200 (`http://localhost:11434/api/tags`)
- Open WebUI: 200 (`http://localhost:3000`)

### Open WebUI Installed Tool Drift and Fix
- Open WebUI DB tool `shadow_empire` was still pointing to `localhost:5050`.
- Backup created: `C:\ShadowEmpire\openwebui_tool_backups\shadow_empire_tool_20260510_190245.json`
- Patched installed tool content to `localhost:5002` using Open WebUI admin API.

### Open WebUI Tool-Path Dossier Proof
- New dossier from Open WebUI tool call:
  - `DOSSIER-1778421046157-DSZARL0K5`
- Verified outputs:
  - `timeline_count=51`
  - `packets_count=52`
  - Required creative families present:
    - `research_packet`
    - `script_packet`
    - `debate_packet`
    - `refined_script_packet`
    - `context_packet`
    - `thumbnail_packet`
    - `metadata_packet`

### Replay/Remodify Observations from Open WebUI
- `request_changes` path currently returns WF-020 in this runtime (`PARTIAL`).
- `replay_stage` path returned WF-021 and produced visible delta.
- Dossier after replay evidence:
  - `timeline_count=59`
  - `packets_count=60`
  - WF-021 visible in timeline.

### Classification Update
- Open WebUI command surface: `PROVEN_WORKFLOW_OPERATOR` (API-path proof).
- Remodify endpoint semantics: `PARTIAL` (maps to WF-020 in this runtime).
- Overall production classification remains:
  - `FULL_CREATIVE_CHAIN_PROVEN (local-only, Restore_01 path-locked)`

## Open WebUI UI-Binding Correction (2026-05-10)

- Backend tool path remains proven (`/api/chat/completions` + `tool_ids=[shadow_empire]`).
- Human UI replacement status corrected to not-ready until visible browser proof is completed.

### Corrected classification
- `API_VISIBLE_OPENWEBUI_TOOL_PROVEN`
- `UI_BINDING_NOT_PROVEN`
- `COMMAND_CENTER_REPLACEMENT_NOT_READY`

### Binding hardening done
- Created Open WebUI preset model:
  - `shadow-creator-os` (base `llama3.2:3b`, `meta.toolIds=[shadow_empire]`).
- Created six Shadow prompt templates for visible operator shortcuts.

### Chat history explanation
- Stateless compatibility API calls do not persist chats by default (observed via chat table count check).

Reference report:
- `docs/operator/OPEN_WEBUI_REALTIME_SURFACE_TEST_20260510.md`

## Open WebUI Browser-Surface Status Correction (2026-05-10)

- Prior backend-only proof remains valid, but browser surface classification is now explicitly staged:
  - `API_VISIBLE_OPENWEBUI_TOOL_PROVEN`
  - `UI_BINDING_PARTIALLY_PROVEN`
  - `FINAL_BROWSER_CHAT_PROOF_PENDING`

Evidence:
- user screenshot shows `Shadow Creator OS` selected with tool indicator `1`.
- runtime has model binding (`shadow-creator-os` -> `toolIds=[shadow_empire]`).
- task runs generated new dossiers with creative packet families:
  - `DOSSIER-1778424897109-C8WQ7MKO7`
  - `DOSSIER-1778424898457-WDFXVBVXX`
- replay stage produced WF-021 and timeline/packet deltas.

Not yet upgraded to `USER_VISIBLE_COMMAND_SURFACE_PROVEN` until direct human browser chat output confirmation is captured.

## Open WebUI Deterministic Router Patch (2026-05-10 22:10 IST)

### Root-cause confirmation
- Browser chats under `shadow-creator-os` showed model-authored guidance instead of direct operator output.
- Open WebUI chat rows confirm tool context in `sources` while assistant `content/output` remained advisory.
- Classified as:
  - `TOOL_NOT_AUTO_INVOKED_FROM_BROWSER_CHAT`
  - `MODEL_SUMMARIZED_SOURCES_ONLY`

### Patch applied
- Added deterministic pipe:
  - `config/openwebui_shadow_creator_os_direct_pipe.py`
- Added installer:
  - `scripts/operator/install-openwebui-direct-router.ps1`
- Installed runtime objects in Open WebUI DB:
  - function `shadow_creator_os_direct_pipe`
  - model preset `shadow-creator-os-direct`
- Backup:
  - `C:\ShadowEmpire\openwebui_direct_router_backup\20260510_221026\webui.db.bak`

### Runtime proof (direct router)
- New dossier: `DOSSIER-1778431713532-OEAM4U6OV`
- Counts after creation:
  - `timeline_count=37`
  - `packets_count=49`
- Counts after replay:
  - `timeline_count=53`
  - `packets_count=54`
- Creative families present:
  - `research_packet`
  - `script_packet`
  - `debate_packet`
  - `refined_script_packet`
  - `context_packet`
  - `thumbnail_packet`
  - `metadata_packet`
- Replay route evidence:
  - `WF-021` queued and packet/timeline delta observed.

### Updated Open WebUI classification
- `DIRECT_ROUTER_CREATED_BUT_MANUAL_TEST_PENDING`
- `TOOL_CHOICE_MODE_FAILED`
- `MANUAL_UI_ACTION_REQUIRED`

## 2026-05-11 — Creator Body Materialization Fix
- Root cause: deterministic shell packets from M-001 contract path produced no creator body fields.
- Patch: operator/skill_runtime.js now materializes family-specific content + provider metadata; direct router list extraction improved.
- New validation dossier: DOSSIER-1778442163263-Q4SQUTJTF.
- timeline_count=51, packets_count=52, runtime_error_packet=0.
- Required families present: research/script/debate/refined_script/context/thumbnail/metadata.
- Outcome: CREATOR_OUTPUT_MATERIALIZED (local deterministic template mode).
- Timestamp: 2026-05-11 01:16:07 +05:30


## 2026-05-11 Provider Router Audit
- Cloud providers are wired at adapter/registry level but no live cloud calls executed.
- No-key proof dossier: DOSSIER-1778443710533-NIPXV8FUP.
- provider_used remained local_deterministic_template with explicit fallback_chain.
- Classification: CLOUD_PROVIDER_NOT_USED / PROVIDER_ROUTER_READY_NO_KEYS.
- Timestamp: 2026-05-11 01:40:07 +05:30


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
