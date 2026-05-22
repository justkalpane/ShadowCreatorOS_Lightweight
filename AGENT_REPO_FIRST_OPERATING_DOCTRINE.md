# AGENT REPO-FIRST OPERATING DOCTRINE

## Why This Lightweight Path Exists

The old ShadowEmpire full-runtime lane was quarantined because it was too heavy for immediate production intelligence work:

- n8n runtime complexity and workflow drift risk
- OpenWebUI routing/auth instability
- Gemini quota/rate-limit instability
- webhook/workflow ID drift
- mission-context and lineage degradation risk
- high debugging overhead with provider-heavy coupling

The lightweight repo exists to keep intelligence deterministic and auditable:

- GitHub repo is the constitution/brain.
- Coding agents are the reasoning/runtime operators.
- Chat output is the live product surface by default; dossier artifacts are production truth only in explicit archive/production dossier mode.
- n8n and providers are deferred execution layers, not intelligence prerequisites.

## Active Production Loop (MAC-05)

1. User content request
2. `mission_context`
3. director selection
4. agent/subagent/skill/subskill selection
5. `research_brief`
6. `script_v1`
7. `debate`
8. `critique`
9. `final_script`
10. `context_engineering_packet`
11. `provider_handoff_packet`
12. `quality_gate`
13. `lineage`
14. user review
15. commit after approval

## Mandatory Agent Behaviors

- Read repo first and obey `main` branch doctrine.
- Follow runtime contracts in `runtime_contracts/`.
- Use registry-backed selections only.
- Build chat, consolidated, or dossier outputs exactly to the active output-mode contract.
- Validate JSON packet files before commit.
- Stop on drift, missing evidence, or invalid packets.

## Work Allowed Without n8n

- topic intake normalization
- research brief
- script generation and refinement
- debate and critique
- final script
- context engineering packet
- provider handoff packet (reference mode only)
- quality gate report
- lineage
- commit/push after explicit review approval

## Work Deferred to Future Execution Layer

- voice generation
- avatar generation
- image/video generation
- publishing execution
- analytics pulls from providers
- scheduled monitoring automations
- provider orchestration
- n8n execution bus activation/import/execution
- credentialed API execution

## Branch Discipline

- Operate on `main` unless user explicitly directs otherwise.
- Do not use backup branches for active production.
- Keep backup/history branches as rollback evidence only.

## Universal Single-Agent Operation

The lightweight OS must be usable by one capable repo-aware agent. A user should not need to install every possible agent to get normal topic-to-context-engineering output.

- Single-agent operation is the primary product path.
- Multi-agent review/reasoning is an optional quality lane.
- Chat-only agents can produce Shadow Mission Packets and output bundles.
- Repo-write agents create one consolidated output file by default after approval; dossier files require explicit full dossier mode.
- n8n and providers remain future external execution layers.

## Fresh GitHub Repo Bootstrap Proof

Portable operation is proven when a fresh agent receives the GitHub repo on branch `main`, reads `START_HERE_FOR_AGENTS.md`, follows `AGENT_READ_ORDER.md`, performs registry-first selection, and returns a complete Shadow output packet without relying on old chat memory. Repo files are created only after explicit approval.

The agent must not use internet-first behavior before repo context. It must not execute n8n, providers, media, Gemini API, OpenWebUI, or old runtime by default.

## Output Consolidation and Chat Approval Gates

Default lightweight behavior must avoid file-sprawl.

- Chat-only mode is default for web/chat LLMs.
- Consolidated repo-write mode is default for coding agents with approved write access.
- Full dossier archive mode is explicit only.
- Gate failures and blocker decisions must be visible in chat.
- User approval is required before file creation, full dossier creation, commit, push, or provider handoff.

## Proof Status Honesty Rule

- Proof classification must align to the weakest required evidence layer.
- `PASS` is forbidden if mandatory evidence layers are unresolved.
- Agent mapping gaps must be surfaced as `PARTIAL` unless contracts declare that layer optional for the current proof.
- Research mode must be explicit (`repo_only`, `web_assisted`, or `real_time_web`).
- Repo-first behavior and live web research are separate claims and must not be conflated.

## Repo-First + Source-Aware Research Rule

- Repo-first sequencing is mandatory; internet-first execution is forbidden.
- Source freshness is mandatory when task scope requires current facts.
- Every output must disclose research mode, web access status, source usage, and confidence.
- No source list means no real-time-source claim.
- For default lightweight operation, chat-only output is preferred unless user approves repo-write.

## Native Tools / Connectors / Plugins Capability Routing

- Task routing must include capability assessment before execution claims.
- Capability checks must include tools, connectors, plugins, local apps, and platform-native functions.
- Required capability missing -> `NEEDS_CONFIRMATION` or `NEEDS_USER_APPROVAL` gate.
- Optional capability missing -> proceed with disclosed limitation.
- Provider/n8n/media capabilities stay execution-gated by default.

## CURRENT LIGHTWEIGHT OUTPUT MODE OVERRIDE

- `CHAT_ONLY_MODE` is default for normal user tasks.
- Normal user tasks do not create files.
- `CONSOLIDATED_REPO_WRITE_MODE` requires explicit user approval.
- `FULL_DOSSIER_ARCHIVE_MODE` requires explicit user request.
- Any older instruction saying `create one dossier per mission` applies only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
- Do not create dossier artifacts for MAC-06.1A chat-only proof.
- Do not create file sprawl by default.

## CURRENT LIGHTWEIGHT PRODUCT DOCTRINE OVERRIDE

- In current lightweight operation, chat is the primary live output surface.
- Repo is the constitution, memory, and routing brain.
- Dossier artifacts are production truth only in explicit `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
- Normal tasks must not create files by default.
- Registry-first routing must still happen in chat-only mode.
- Every output must include research mode, source disclosure, native capability assessment, tools/connectors/plugins assessment, quality gate, and lineage summary.

## ALWAYS-ON SHADOW ORCHESTRATION TRIGGER

- Normal user task language must still trigger repo-first Shadow OS.
- Do not wait for the user to say `use repo`.
- Do not wait for the user to provide the repo URL if this repo is already attached.
- Do not answer from general model knowledge first.
- For content tasks, script alone is insufficient.
- Content tasks must include content engineering output unless user asks for script-only.
- Realtime/source-aware research must be used when current facts are required.
- If web access is unavailable, disclose the limitation and gate.

## SHADOW_BOOT_CONFIRMATION REQUIRED

- Every normal task must begin with `SHADOW_BOOT_CONFIRMATION`.
- If first visible output is a script/advice/summary before boot confirmation, classify `FAIL`.
- Boot confirmation must appear before content generation.
- This applies to Codex Cloud, local Codex, Claude, ChatGPT, Gemini, Kimi, DeepSeek, Perplexity, and Antigravity when the repo is attached/readable.
- `CHAT_ONLY_MODE` remains default.
- No files are created by default.

## CANONICAL SHADOW LIGHTWEIGHT BOOT ORDER - ACTIVE LAW

Use repo-relative paths first. Absolute `/Users/apple/...` paths are local Mac references only.

1. `AGENTS.md`
2. `START_HERE_FOR_AGENTS.md`
3. `AGENT_READ_ORDER.md`
4. `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`
5. `AGENT_ANTI_DRIFT_RULES.md`
6. `runtime_contracts/ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md`
7. `runtime_contracts/LAYMAN_TASK_TRIGGER_CONTRACT.md`
8. `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md`
9. `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md`
10. `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md`
11. `runtime_contracts/NATIVE_AGENT_CAPABILITY_INVENTORY_CONTRACT.md`
12. `runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md`
13. `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`
14. `registries/native_capability_routing_matrix.yaml`
15. `registries/agent_runtime_selection_index.yaml`

## CURRENT LIGHTWEIGHT OUTPUT LAW - ACTIVE LAW

`CHAT_ONLY_MODE` is default for normal user tasks.
Normal user tasks create no files.
`CONSOLIDATED_REPO_WRITE_MODE` requires explicit user approval.
If repo-write is approved, create exactly one consolidated file by default: `outputs/missions/<mission_id>/MISSION_OUTPUT.md`.
`FULL_DOSSIER_ARCHIVE_MODE` requires explicit user request.
Older instructions saying every mission creates a dossier apply only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
For content/video/script tasks, script-only output is `PARTIAL` unless the user explicitly asks for script-only.
For content/video/script tasks, `CONTENT_ENGINEERING_OUTPUT_CONTRACT` is mandatory.

## CLAIM_EVIDENCE_STATUS LAW

Every production-sensitive claim must be expressed as:

```text
claim=
evidence=
evidence_path=
command_output_or_file_reference=
status=PASS/PARTIAL/BLOCKED/NEEDS_CONFIRMATION
```

If evidence is missing, mark `NEEDS_CONFIRMATION`. Do not convert `NEEDS_CONFIRMATION` into `PASS`.

## FRESH LAYMAN PROOF LAW

The fresh-agent proof must use a plain layman request only.
Do not use a giant forcing prompt for the primary proof.
A detailed forcing prompt is allowed only after failure as diagnostic remediation.
The proof passes only if the repo itself triggers orchestration through `AGENTS.md` and active startup docs.
