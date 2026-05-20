# OPENWEBUI_DIRECT_COMMAND_SURFACE_20260510

## Purpose
Convert Open WebUI from probabilistic tool-choice behavior into a deterministic Shadow Creator OS operator surface.

## Failure Pattern Confirmed
- `shadow-creator-os` (tool-choice preset) often returned advisory text.
- Chat evidence showed tool payloads in `sources` while assistant content did not return operator-grade dossier summaries.

Classification before patch:
- `TOOL_NOT_AUTO_INVOKED_FROM_BROWSER_CHAT`
- `OPENWEBUI_API_TOOL_PROVEN_BUT_BROWSER_UX_NOT_PROVEN`

## Direct Router Implementation
- Pipe file:
  - `config/openwebui_shadow_creator_os_direct_pipe.py`
- Installer:
  - `scripts/operator/install-openwebui-direct-router.ps1`
- Open WebUI runtime entities:
  - function: `shadow_creator_os_direct_pipe` (`type=pipe`)
  - model: `shadow-creator-os-direct`

## Routing Contract
`Shadow Creator OS Direct` model behavior:
1. health prompts -> `GET /operator/health`
2. content-generation prompts -> `POST /operator/new-content-job`
3. inspect prompts -> `GET /operator/dossier/:id/timeline` + `GET /operator/outputs/:id`
4. replay/remodify prompts -> `POST /operator/replay/:id` (WF-021 proven path)
5. response formatting always returns dossier-oriented operator output:
   - `dossier_id`
   - workflow summary
   - timeline/packet counts
   - packet families
   - next actions

## Proof Run
- Dossier: `DOSSIER-1778431713532-OEAM4U6OV`
- Creation counts:
  - `timeline_count=37`
  - `packets_count=49`
- Replay counts:
  - `timeline_count=53`
  - `packets_count=54`
- Visible creative families:
  - `research_packet`
  - `script_packet`
  - `debate_packet`
  - `refined_script_packet`
  - `context_packet`
  - `thumbnail_packet`
  - `metadata_packet`

## Limits
- Browser-side visible confirmation is still required from manual UI chat under `shadow-creator-os-direct`.
- Refined-script body and detailed thumbnail/metadata text are not yet consistently materialized in packet payload fields.

## Current Classification
- `DIRECT_ROUTER_CREATED_BUT_MANUAL_TEST_PENDING`
- `TOOL_CHOICE_MODE_FAILED`
- `MANUAL_UI_ACTION_REQUIRED`

## 2026-05-11 Materialization Update
- Direct router now returns body content (script/thumbnail/metadata) after skill runtime content materialization patch.
- Validation dossier: DOSSIER-1778442208010-7GL24QGWS.
- Status: CREATOR_OUTPUT_MATERIALIZED (local deterministic template mode).
- Timestamp: 2026-05-11 01:16:07 +05:30

