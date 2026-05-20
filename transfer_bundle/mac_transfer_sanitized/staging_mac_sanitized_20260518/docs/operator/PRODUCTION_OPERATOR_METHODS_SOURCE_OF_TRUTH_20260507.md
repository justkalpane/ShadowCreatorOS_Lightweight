# PRODUCTION OPERATOR METHODS SOURCE OF TRUTH (2026-05-07)

## Executive Verdict
This document is built from local repo/runtime evidence only.

Current production truth:
- Canonical Operator API runtime is `http://localhost:5002` (launcher + server binding evidence).
- n8n core runtime is recovered and workflow chain is validated in recovery docs.
- Command Center/chat-layer is explicitly quarantined in recovery handoff.
- Direct flat Ollama generation is not workflow proof by itself.

Important drift note:
- Some docs still show legacy `localhost:5050` references. Canonical current runtime is `5002`.

## Canonical Runtime Anchors
- Repo: `C:\ShadowEmpire-Git_Restore_01`
- n8n profile: `C:\ShadowEmpire\n8n_user_restore_01`
- n8n UI: `http://127.0.0.1:5678/home/workflows`
- Operator API: `http://localhost:5002`
- Open WebUI: `http://localhost:3000`
- Ollama: `http://localhost:11434`

## Status Labels
- `PROVEN_WORKFLOW_OPERATOR`: Evidence shows Operator/API -> n8n workflow -> dossier/packet/approval/replay evidence.
- `MODEL_ONLY_SMOKE_TEST`: Only model text generation proof, no workflow chain evidence.
- `CONFIGURED_BUT_UNPROVEN`: wiring/config exists; no direct method-level proof evidence found.
- `PARTIAL`: some behavior proven; method still has missing acceptance evidence.
- `QUARANTINED`: unstable and excluded from production/recovery commit path.
- `FUTURE`: planned but not implemented/proven.

## Canonical Operator Surface Matrix
| Method ID | Method Name | User Entry Surface | Backend Path | Endpoint / Script | Expected n8n Workflow | Expected Evidence | Approval Path | Output Location | Status | Evidence Source |
|---|---|---|---|---|---|---|---|---|---|---|
| METHOD-01 | Ollama UI / Local Model UI Operator Bridge | Local model UI (if any) | UI -> Operator API -> n8n | Not concretely defined as a dedicated UI in repo | WF-001 -> WF-010 (+ packs) | dossier_id + wf001/wf010 + outputs | WF-020/WF-021 via operator | dossiers/data indexes | CONFIGURED_BUT_UNPROVEN | No concrete dedicated "Ollama UI" artifact found; only Ollama runtime + tool runner evidence |
| METHOD-02 | Open WebUI Shadow Tool Operator | `http://localhost:3000` | Open WebUI tools -> Operator API -> n8n | `config/open_webui_tools.json`; `scripts/windows/start_openwebui_local_runtime.ps1` | WF-001 -> WF-010 (+ packs), WF-020/WF-021 | tool call returns dossier_id/workflow state + n8n trace | `/operator/approve/:id`, `/operator/remodify/:id`, `/operator/replay/:id` | dossier/packet outputs via Operator API | CONFIGURED_BUT_UNPROVEN | Tool definitions exist and point to 5002; direct Open WebUI execution proof not found in current evidence set |
| METHOD-03 | PowerShell Operator | PowerShell scripts | Script -> Operator API -> n8n | `scripts/operator/new-content-job.ps1` | WF-001 then WF-010 | `status`, `dossier_id`, `wf001`, `wf010` in response | `approve-output.ps1`, `request-changes.ps1`, `replay-stage.ps1` -> WF-020/WF-021 | dossier files + `data/se_*` indexes | PROVEN_WORKFLOW_OPERATOR | Script code + operator acceptance report PASS with dossier/workflow evidence |
| METHOD-04 | Operator API Direct | REST/curl/Invoke-RestMethod | API -> n8n webhooks | `POST /operator/new-content-job`, related endpoints | WF-001 -> WF-010 (+ child packs), WF-020, WF-021 | dossier_id, wf001/wf010 status, timeline, outputs, error events | `/operator/approve/:id`, `/operator/remodify/:id`, `/operator/replay/:id` | `dossiers/`, `data/se_dossier_index.json`, `data/se_packet_index.json`, `data/se_route_runs.json`, `data/se_error_events.json` | PROVEN_WORKFLOW_OPERATOR | `engine/api/operator.js` flow + operator acceptance report PASS |
| METHOD-05 | Git Bash / Repo CLI Operator | Git Bash / terminal | CLI -> operator runner/API -> n8n | `npm run operator:ollama`, REST calls, scripts | WF-001 -> WF-010 for content jobs | dossier_id + workflow status when routed via operator API | Same operator API approval endpoints | same dossier/index outputs | PARTIAL | CLI routes exist (`operator/ollama_tool_runner.js`, package scripts) but Git Bash-specific proof trace not explicitly captured |
| METHOD-06 | n8n Manual UI Operator | n8n UI | Manual webhook/workflow execution in n8n | n8n UI + ingress webhooks | WF-001, WF-010, WF-100..WF-600, WF-020, WF-021, WF-900 | n8n execution IDs, workflow status, dossier/packet updates | WF-020/WF-021 via workflow/UI | n8n executions + dossier/index files | PROVEN_WORKFLOW_OPERATOR | recovery docs + graph parity + runtime recovery handoff evidence |
| METHOD-07 | n8n Chat / Default Agents Operator | n8n-native chat/agent UI | n8n chat/agent nodes -> workflow/tooling | Not found in current workflow JSON set | N/A | Would need chat trigger + agent execution traces | N/A | N/A | FUTURE | No `chatTrigger` / AI Agent node evidence in `n8n/workflows/*.json`; docs mark n8n chat hub future/not production-approved |
| METHOD-08 | Command Center / Chat API / Future GUI | `http://localhost:5002/chat` | Chat API layer -> operator/n8n orchestration | `server.js`, `engine/api/chat.js`, chat services | Intended WF-010 parent routing | Would require stable browser UX + dossier/packet/approval evidence | via operator endpoints | chat session + dossier outputs | QUARANTINED | `docs/recovery/FINAL_RECOVERY_BRANCH_STATUS_20260507.md` explicitly quarantines chat-layer files |

## What Is Actually Built vs Assumed
1. Built and evidenced strongly:
- Operator API direct workflow path.
- PowerShell script path through Operator API.
- n8n manual workflow path.

2. Built/configured but method-level proof incomplete in current evidence set:
- Open WebUI tool-bridge path (configured, but no direct proof record here that a full run was executed end-to-end from Open WebUI chat in this checkpoint set).
- Git Bash-specific path (commands exist; no explicit Git Bash proof transcript in this evidence bundle).

3. Not equivalent to workflow proof:
- Raw `POST /api/generate` to Ollama alone.

4. Explicitly not production-approved now:
- Command Center/chat-layer (quarantined).

## PASS Criteria Per Method
A method is PASS only if evidence includes at least one of:
- `dossier_id`
- workflow execution status (`wf001/wf010` and/or n8n execution trace)
- packet/index linkage (`se_packet_index`, `se_route_runs`)
- approval/replay state (`WF-020` / `WF-021` path)

## FAIL Criteria Per Method
- Only model text output with no workflow evidence.
- No dossier_id.
- No workflow trace.
- No packet/approval/replay state evidence.

## Where To Verify Evidence
- n8n execution trace: `http://127.0.0.1:5678/home/workflows` (Executions)
- Dossier index: `C:\ShadowEmpire-Git_Restore_01\data\se_dossier_index.json`
- Packet index: `C:\ShadowEmpire-Git_Restore_01\data\se_packet_index.json`
- Route runs: `C:\ShadowEmpire-Git_Restore_01\data\se_route_runs.json`
- Approval queue: `C:\ShadowEmpire-Git_Restore_01\data\se_approval_queue.json`
- Error events: `C:\ShadowEmpire-Git_Restore_01\data\se_error_events.json`
- Dossier files: `C:\ShadowEmpire-Git_Restore_01\dossiers\`

## Correct Testing Order (Production Truth-Oriented)
1. METHOD-03 PowerShell Operator (fastest governed proof)
2. METHOD-04 Operator API Direct
3. METHOD-06 n8n Manual UI trace correlation
4. METHOD-02 Open WebUI tool bridge
5. METHOD-05 Git Bash/CLI operator path
6. METHOD-01 Ollama UI bridge (only if concrete UI surface is identified and wired)
7. METHOD-07 n8n chat/default agents (future)
8. METHOD-08 Command Center (quarantined until formal reactivation)

## Do-Not-Confuse Rules
- Direct Ollama generation (`/api/generate`) = model smoke only.
- Open WebUI/Ollama becomes workflow-operator proof only when tool/API calls route to Operator API and trigger n8n chain.
- Command Center is currently quarantined unless an explicit de-quarantine decision and successful browser QA are documented.

## Evidence Files Used (Primary)
- `docs/recovery/FINAL_RECOVERY_BRANCH_STATUS_20260507.md`
- `docs/operator/OPERATOR_ACCEPTANCE_TEST_REPORT.md`
- `engine/api/operator.js`
- `operator/ollama_tool_runner.js`
- `config/open_webui_tools.json`
- `scripts/operator/new-content-job.ps1`
- `scripts/windows/start_shadow_operator_api.ps1`
- `scripts/windows/start_openwebui_local_runtime.ps1`
- `server.js`
- `operator/config.js`
- `docs/PROD-01_OPERATING_METHODS_6_SURFACES.md`
- `docs/operator/OPERATOR_USAGE_GUIDE.md`
- `docs/operator/OPERATOR_API_REFERENCE.md`
- `n8n/workflows/WF-001.json`, `WF-010.json`, `WF-020.json`, `WF-021.json`, `WF-900.json`, `WF-100..WF-600.json`

## Final Architecture Reminder
Production operator truth is workflow-governed flow:
`Operator Surface -> Operator API / bridge -> n8n workflows -> dossier/packet/approval/replay evidence -> returned status/output`

Not model-only text generation.
