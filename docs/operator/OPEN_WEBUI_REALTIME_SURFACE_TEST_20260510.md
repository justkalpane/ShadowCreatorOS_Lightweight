# OPEN_WEBUI_REALTIME_SURFACE_TEST_20260510

## Corrected Executive Classification
- `API_VISIBLE_OPENWEBUI_TOOL_PROVEN`
- `UI_BINDING_NOT_PROVEN` (direct browser click-path not automated in this session)
- `COMMAND_CENTER_REPLACEMENT_NOT_READY` (pending explicit human-UI proof)

## Path Lock
- Repo root: `C:/ShadowEmpire-Git_Restore_01`
- Branch: `recovery/runtime-lock-20260506`
- HEAD: `aca5c63 docs: add final recovery branch status handoff`

## Service Reachability
- Operator API: `200` (`http://localhost:5002/operator/health`)
- n8n: `200` (`http://localhost:5678`)
- Ollama tags: `200` (`http://localhost:11434/api/tags`)
- Open WebUI: `200` (`http://localhost:3000`)

## UI-Binding Root Cause and Fixes

### Root Cause Found
Open WebUI-installed tool payload (`shadow_empire`) still pointed to `localhost:5050` in runtime DB, even though repo config was on `5002`.

### Runtime Fix Applied
- Backup of installed tool payload:
  - `C:\ShadowEmpire\openwebui_tool_backups\shadow_empire_tool_20260510_190245.json`
- Updated installed Open WebUI tool payload via admin API:
  - `http://localhost:5050` -> `http://localhost:5002`

### Visibility/Binder Fix Applied
Created visible Open WebUI model preset and prompt templates to make Shadow operations explicit in UI:

1. Model preset created:
- `shadow-creator-os` (display name: **Shadow Creator OS**)
- `base_model_id`: `llama3.2:3b`
- `meta.toolIds`: `["shadow_empire"]`
- `meta.capabilities.tools`: `true`

2. Prompt templates created:
- `shadow_full_content_job`
- `shadow_research_packet`
- `shadow_script_mode`
- `shadow_thumbnail_metadata`
- `shadow_replay_remodify`
- `shadow_dossier_inspect`

### Repo Consistency Patches (for future imports)
- `config/openwebui_shadow_operator_tools.py` -> `5002`
- `config/openwebui_shadow_operator_tools_v2.py` -> `5002`
- `config/openwebui_shadow_operator_tools_v3.py` -> `5002`
- `docs/operator/OPEN_WEBUI_INTEGRATION_SETUP.md` legacy runtime map corrected to `5002`

## Tool / Binding Inventory

| Tool/Function | Installed | Enabled | Visible to User (API evidence) | Attached to Model | Endpoint | Status |
|---|---|---|---|---|---|---|
| shadow_empire | YES | YES | YES (`/api/v1/tools`) | YES (`shadow-creator-os.meta.toolIds`) | `http://localhost:5002/operator/*` | READY |

## Backend-Proven Task Matrix (Open WebUI Chat API)

| Test | Evidence Path | Dossier ID | Timeline | Packets | Result |
|---|---|---|---:|---:|---|
| health_check tool | `/api/chat/completions` with `tool_ids=[shadow_empire]` | n/a | n/a | n/a | PASS after 5002 fix |
| full content job | `/api/chat/completions` with `tool_ids=[shadow_empire]` | `DOSSIER-1778421046157-DSZARL0K5` | 51 | 52 | PASS |
| replay stage | `/api/chat/completions` with `tool_ids=[shadow_empire]` | same dossier | 59 | 60 | PASS (WF-021 seen) |
| remodify/request_changes | `/api/chat/completions` with `tool_ids=[shadow_empire]` | same dossier | 53 | 54 | PARTIAL (mapped to WF-020 in current backend semantics) |

Creative packet families verified on dossier `DOSSIER-1778421046157-DSZARL0K5`:
- `research_packet`
- `script_packet`
- `debate_packet`
- `refined_script_packet`
- `context_packet`
- `thumbnail_packet`
- `metadata_packet`

## Chat History Visibility Finding

Why earlier API tests were not visible as new sidebar chats:
- `/api/chat/completions` without chat metadata does not persist new chat rows.
- Verified by DB count test on `chat` table: remained `2 -> 2` after stateless API call.

Implication:
- Browser-visible chat history requires UI-driven chat flow (or explicit chat persistence endpoints/metadata), not bare stateless compatibility calls.

## UI Proof Status (Human UI)
- Browser automation was not available in this session.
- Therefore direct click-path proof (tool picker visibility + chat composer behavior on your exact screen) is still pending.

Current status remains:
- `API_VISIBLE_OPENWEBUI_TOOL_PROVEN`
- `MANUAL_UI_ACTION_REQUIRED` for final user-visible certification

## Exact Manual UI Steps (next)
1. Open `http://localhost:3000` and ensure logged in as `Chethan`.
2. Select model **Shadow Creator OS** (not plain `llama3.2:3b`).
3. In a new chat, run:
   - `Use Shadow Creator OS tools. Create a YouTube script about AI vs Human with hook, intro, research summary, debate/critique, refined script, context engineering packet JSON, thumbnail plan, and metadata. Return dossier_id and packet families.`
4. Confirm response contains `dossier_id`.
5. Then run:
   - `Inspect the latest dossier outputs and show script, thumbnail ideas, and metadata.`
6. Optional replay:
   - `Improve the hook and make the intro sharper for the latest dossier using replay stage WF-200.`

PASS to upgrade classification to `USER_VISIBLE_COMMAND_SURFACE_PROVEN` requires the above to be visibly confirmed in browser UI.
## Browser UI Progress Update (2026-05-10, user screenshot + runtime verification)

### Screenshot-backed status
User-provided browser screenshot confirms:
- `Shadow Creator OS` preset is visible in model picker.
- `Shadow` category is visible.
- tool indicator shows `1` tool attached/available.

### Corrected classification
- `UI_BINDING_PARTIALLY_PROVEN`
- `SHADOW_CREATOR_OS_MODEL_VISIBLE`
- `TOOL_ATTACHMENT_VISIBLE`
- `FINAL_BROWSER_CHAT_PROOF_PENDING`

### Additional binding hardening completed
- Created Open WebUI preset model `shadow-creator-os` (base `llama3.2:3b`) with `meta.toolIds=["shadow_empire"]`.
- Created six prompt templates for visible operator UX shortcuts.

### Persistence and session findings
- API calls without chat metadata are stateless and do not create sidebar chats.
- Calls including `parent_id`, `id`, and `user_message` now create persistent Open WebUI chat rows.
- Chat table now shows new recent chats:
  - `63f0c6b5-8e9b-4c21-9a1f-3744751ad406`
  - `e3a4aa69-8ca9-4b81-ac44-167625a4fbfc`
  - `e7743943-474c-4c4a-b84f-b3e6c83840c7`

### Latest verified Open WebUI task run (tool path)
- Dossiers created:
  - `DOSSIER-1778424897109-C8WQ7MKO7`
  - `DOSSIER-1778424898457-WDFXVBVXX`
- For each dossier:
  - `timeline_count=51`
  - `packets_count=55`
  - required creative families present:
    - `research_packet`
    - `script_packet`
    - `debate_packet`
    - `refined_script_packet`
    - `context_packet`
    - `thumbnail_packet`
    - `metadata_packet`

### Replay from Open WebUI tool path
- `replay_stage` on `DOSSIER-1778424898457-WDFXVBVXX` returned `WF-021` queued.
- Post-replay evidence:
  - `timeline_count=53`
  - `packets_count=57`
  - WF-021 present in timeline.

### Remaining gate
Direct human browser-chat visual confirmation of dossier/output text is still required to upgrade to:
- `USER_VISIBLE_COMMAND_SURFACE_PROVEN`

## Direct Router Upgrade (2026-05-10 22:10 IST)

### Why tool-choice mode failed in browser
- Browser chats for `shadow-creator-os` were persisted but responses were generic model guidance.
- Chat records show `sources` carrying tool payload context, while assistant `content/output` still rendered advisory text.
- Failure classification:
  - `TOOL_NOT_AUTO_INVOKED_FROM_BROWSER_CHAT`
  - `MODEL_SUMMARIZED_SOURCES_ONLY`
  - `OPENWEBUI_API_TOOL_PROVEN_BUT_BROWSER_UX_NOT_PROVEN`

### Deterministic fix applied
- Added direct Open WebUI pipe file:
  - `config/openwebui_shadow_creator_os_direct_pipe.py`
- Added installer:
  - `scripts/operator/install-openwebui-direct-router.ps1`
- Installed into Open WebUI DB with backup:
  - `C:\ShadowEmpire\openwebui_direct_router_backup\20260510_221026\webui.db.bak`
- Created runtime objects:
  - Function: `shadow_creator_os_direct_pipe` (`type=pipe`, active)
  - Model preset: `shadow-creator-os-direct` (base model = direct pipe)

### Direct router runtime proof (deterministic)
- Fresh run through pipe runtime:
  - Dossier: `DOSSIER-1778431713532-OEAM4U6OV`
  - `timeline_count=37`
  - `packets_count=49`
  - families present:
    - `research_packet`
    - `script_packet`
    - `debate_packet`
    - `refined_script_packet`
    - `context_packet`
    - `thumbnail_packet`
    - `metadata_packet`
- Replay proof through same direct pipe:
  - `POST /operator/replay/:id` -> `WF-021` queued
  - post replay counts: `timeline_count=53`, `packets_count=54`

### Current Open WebUI classification
- `DIRECT_ROUTER_CREATED_BUT_MANUAL_TEST_PENDING`
- `TOOL_CHOICE_MODE_FAILED` (legacy preset behavior)
- `MANUAL_UI_ACTION_REQUIRED` (final browser-visible validation pending)
