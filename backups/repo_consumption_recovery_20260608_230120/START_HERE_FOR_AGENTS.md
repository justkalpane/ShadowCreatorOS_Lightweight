# START HERE FOR AGENTS

## ROOT INSTRUCTION WARNING - ACTIVE

`AGENTS.md` is the canonical root instruction.

If this file is read first, immediately return to `AGENTS.md`, apply `SHADOW_BOOT_CONFIRMATION`, and only then continue.

Do not produce scripts, advice, summaries, plans, or web-sourced answers before `SHADOW_BOOT_CONFIRMATION`.

Absolute `/Users/apple/...` paths are `LOCAL_MAC_REFERENCE_ONLY`, not portable startup law.

Normal tasks use `CHAT_ONLY_MODE` by default and create no files.

Full dossier mode requires explicit user request.

## ENVIRONMENT TRIGGER COMPATIBILITY LAW

Repo presence is not equal to active behavioral control.

If a platform sees the repo but does not output `SHADOW_BOOT_CONFIRMATION` before the first answer, classify:

```text
platform_current_classification=REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE
```

Do not continue producing scripts, advice, summaries, or web-sourced answers after this failure.

Compatibility levels:

- `NATIVE_AUTO_TRIGGER_COMPATIBLE`
- `BOOTSTRAP_REQUIRED_COMPATIBLE`
- `REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE`
- `NOT_COMPATIBLE`

Native onboarding requires either:

- `NATIVE_AUTO_TRIGGER_COMPATIBLE`, or
- `BOOTSTRAP_REQUIRED_COMPATIBLE` with user-approved bootstrap workflow.

Codex Cloud currently requires compatibility validation before onboarding.

## TASK ROUTING + CONSUMPTION LAW

Every task after `SHADOW_BOOT_CONFIRMATION` must be classified through:

- `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`
- `registries/task_intent_routing_matrix.yaml`

Every selected director, agent, subagent, skill, and subskill must be consumed through:

- `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md`

For script/content tasks, output must satisfy:

- `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`
- `runtime_contracts/GUMLOOP_BENCHMARK_OUTPUT_STANDARD.md`
- `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`

Selecting is not enough.
Citing is not enough.
A script cannot be generated until consumption ledgers are complete.

Required before final output:

- `task_intent_classified=true`
- `route_id=`
- `task_intent_routing_matrix_cited=true`
- `director_consumption_ledger_present=true`
- `agent_consumption_ledger_present=true`
- `subagent_consumption_ledger_present=true`
- `skill_consumption_ledger_present=true`
- `subskill_consumption_ledger_present=true`
- `line_by_line_influence_map_present=true`
- `topic_quality_gate_present=true`
- `hook_generation_gate_present=true`
- `hook_variants_count>=3`
- `SCRIPT_BODY_DEPTH_LOCK` present for 3-10 minute YouTube scripts
- `script_quality_gate_present=true`

Shallow repo routing is `FAIL`.
Generic output after bootstrap is `FAIL`.
Selected-but-not-read director/skill/subskill is `FAIL` or `PARTIAL` according to validator.
If route evidence is missing, mark `NEEDS_CONFIRMATION` and ask whether to continue limited mode.

## COMPLETE REQUIRED REPO SCOPE LAW

Every task must use the complete required repo scope for its selected route.

Complete required repo scope is determined by:

- `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`
- `registries/task_intent_routing_matrix.yaml`
- selected `route_manifest_path`
- `runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md`
- `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md`

Do not read only startup docs.
Do not read only bootstrap docs.
Do not read only `.agents` skills.
Do not copy Gumloop route names as source truth.
Do not generate content until route manifest and mandatory files are consumed.

Never replace missing repo reads with synthesized ledgers. If a model cannot
read the full selected route scope inside the current context or time budget,
it must stop before content generation and return `BLOCKED_BEFORE_OUTPUT` with
the missing repo-relative paths. "Evaluated internally", "marked as USED", or
role-summary-only ledgers are shallow routing, not production consumption.

If complete required repo scope is not consumed:

- `route_scope_status=FAIL`
- `shallow_repo_routing_detected=true`
- final proof cannot be PASS.

For `SCRIPT_GENERATION`, PASS requires a visible `ROUTE_SCOPE_FILE_AUDIT` before
the script: canonical route id `SCRIPT_GENERATION`, route manifest read, at
least 68 total route-scope files read, and layer counts covering startup docs,
runtime contracts, registries, directors, agents, subagents, skills, and
subskills. If that audit is missing, return `BLOCKED_BEFORE_OUTPUT`.

## WRAPPER REQUIRED COMPATIBILITY LAW

Codex Cloud reliable mode is currently `WRAPPER_REQUIRED_COMPATIBLE`.

- Native auto-trigger failed.
- Bootstrap activation passed.
- Default post-bootstrap task persistence failed.
- Recovery route-scope-lock run passed.

When operating in Codex Cloud, use `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md` or `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER_COMPACT.md` before or with each task until platform persistence improves.

Required proof fields:

- `shadow_task_execution_wrapper_read=true`
- `wrapper_required_mode_used=true`
- `codex_cloud_reliable_mode=WRAPPER_REQUIRED_COMPATIBLE`
- `post_bootstrap_task_persistence_status=FAILED`

If you are a coding agent working in this repository, start here before any production action.

## Mandatory Startup Steps

1. First authority is `AGENTS.md`.
2. Output `SHADOW_BOOT_CONFIRMATION` before task output.
3. Read `START_HERE_FOR_AGENTS.md`.
4. Read `AGENT_READ_ORDER.md`.
5. Read `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`.
6. Read `AGENT_ANTI_DRIFT_RULES.md`.
7. Read `runtime_contracts/ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md`.
8. Read `runtime_contracts/LAYMAN_COMMAND_GATEWAY_CONTRACT.md`.
9. Read `registries/layman_command_alias_matrix.yaml`.
10. Read `runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md`.
11. Read `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md`.
12. Read `registries/task_intent_routing_matrix.yaml`.
13. Read selected `route_manifest_path`.
14. Operate on branch `main`.
15. Follow repo-first Shadow orchestration before answering.
16. Enforce quality gate and lineage for every output.

Repo-relative paths are authoritative. Absolute `/Users/apple/...` paths are `LOCAL_MAC_REFERENCE_ONLY`.
Any old absolute Mac startup path is `LOCAL_REFERENCE_ONLY`, not portable startup law.
Any production dossier language applies only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 dossier mode.

No Shadow command may be answered until the Layman Command Gateway contract, alias matrix, output mode contract, and Shadow Task Execution Wrapper are loaded.

If a `Shadow <command>:` alias is detected, preserve the raw task, resolve the alias through `registries/layman_command_alias_matrix.yaml`, and internally apply `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md`. If that expansion cannot be proven, return `BLOCKED_BEFORE_OUTPUT` instead of normal content.

## Hard Boundaries

- Do not use backup branches for active production.
- Do not run n8n or provider execution unless explicitly approved.
- Do not import workflows unless explicitly approved.
- Do not call Gemini/providers unless explicitly approved.
- Do not use old Windows runtime as active truth.
- Do not claim media artifacts unless genuinely generated in approved execution phase.

## Mission Model

Repo-first intelligence is the active path:

- topic -> research -> debate -> critique -> script -> refinement -> context packet -> provider handoff packet

n8n/provider layers are deferred execution infrastructure, not required for topic-to-context engineering.

## Local Media Factory Bridge

When a task involves storyboard, B-roll, visual media draft, local render,
ComfyUI, AnimateDiff, Wan, FFmpeg, DaVinci, or the ShadowMediaFactory control
panel, agents must load:

- `registries/local_media_factory_bridge.yaml`
- `runtime_contracts/LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT.md`
- `registries/route_manifests/media_factory_handoff.yaml`

Active local Mac Media Factory root:

```text
/Users/apple/ShadowMediaFactory
```

The local Media Factory is the media worker, not the brain. ShadowCreatorOS
produces scene/prompt/route packets; ShadowMediaFactory performs approved
preflight, generation, assembly, proof, registry, and export tasks.

After any Media Factory runtime change, run the bridge drift audit:

```text
python3 tools/shadow_runtime/media_factory_bridge_sync.py --runtime-check
```

If repo-write is explicitly approved, synchronize the bridge registry state:

```text
python3 tools/shadow_runtime/media_factory_bridge_sync.py --runtime-check --apply
```

## Historical Context References

Future agents should read historical source docs when deeper background is needed on PRD intent, quarantine decisions, and migration history.

- Historical docs are reference context, not active runtime commands.
- MAC-05 operating loop and runtime contracts remain active production law.
- Old full Shadow OS remains quarantined unless explicitly approved for a separate execution phase.

## Universal Single-Agent Operation

One capable repo-aware agent can operate the intelligence layer alone. Multi-agent review is optional quality enhancement, not mandatory for basic operation.

- Chat-only agents can return complete Shadow Mission Packet and output bundles.
- Repo-write agents create one consolidated output file by default after approval; dossier files require explicit full dossier mode.
- n8n/provider layers remain deferred external execution infrastructure.
- Do not force users to install every agent before operating the lightweight OS.

## Fresh GitHub Repo Bootstrap Proof

Future agents must start from GitHub repo `main` and read this file before doing the task. The agent must use repo-first behavior before internet-first behavior.

- Start with `AGENTS.md`, then `START_HERE_FOR_AGENTS.md`.
- Follow `AGENT_READ_ORDER.md`.
- Use registry-first selection with evidence paths.
- Produce a chat-only Shadow output packet by default. Create repo files only after explicit approval.
- Do not execute n8n/providers/media by default.

## Output Consolidation and Chat Approval Gates

The chat is the user-facing control UI.

- Agents must show blockers, gates, recommendations, and approval options in chat.
- Do not hide gate failures inside backend files.
- Default output is chat-only.
- Default repo-write creates one consolidated mission file.
- Full multi-file dossier mode is explicit archive/production mode only.
- Do not create per-subtask files by default.
- Do not create director/agent/skill scratch files by default.
- User must approve before file creation, full dossier creation, commit, push, or n8n/provider handoff.

## Proof Status Honesty Rule

- Final proof status must match the weakest required evidence layer.
- Do not mark `PASS` if any mandatory evidence is missing.
- If agent mapping is not proven and agent mapping is required, mark `PARTIAL`.
- Research mode must be disclosed.
- Repo-first behavior does not imply real-time web research was used.
- Internet access must be explicitly confirmed before claiming current/live research.

## Repo-First + Source-Aware Research Rule

- Repo-first startup is mandatory.
- Internet-first behavior is forbidden.
- Real-time web research is required when freshness-critical tasks demand it.
- Agent must disclose whether web access was available and whether it was used.
- Agent must not claim source-backed current research unless sources were actually retrieved and listed.
- Normal default output is chat-only.
- Consolidated repo-write output requires user approval.
- Full dossier mode is explicit-only.

## Native Tools / Connectors / Plugins Capability Routing

- Every agent must declare capabilities available in the current environment.
- Do not assume Codex/Claude/ChatGPT/Gemini/Perplexity/Kimi/DeepSeek/Antigravity have identical tools.
- Confirm repo read before mission routing.
- Confirm web research availability before claiming current data.
- Repo write/file creation requires user approval.
- Git commit/push requires user approval.
- n8n/provider/media execution requires explicit approval.
- Map task route to required capabilities before execution.
- If required capability is missing, show chat gate and user options.

## CURRENT LIGHTWEIGHT OUTPUT MODE OVERRIDE

- `CHAT_ONLY_MODE` is default for normal user tasks.
- Normal user tasks do not create files.
- `CONSOLIDATED_REPO_WRITE_MODE` requires explicit user approval.
- `FULL_DOSSIER_ARCHIVE_MODE` requires explicit user request.
- Any older instruction saying `create one dossier per mission` applies only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
- Do not create dossier artifacts for MAC-06.1A chat-only proof.
- Do not create file sprawl by default.

## ACTIVE PRECEDENCE WARNING FOR FRESH AGENTS

If any document conflicts, apply this order:

1. User explicit instruction
2. Runtime safety boundaries
3. Current Lightweight Output Mode Override
4. Native Capability Routing Contract
5. Source-Aware Runtime Decision Protocol
6. Chat Approval Gate Contract
7. Proof Status Honesty Law
8. MAC-06.1A Expected Output Contract
9. MAC-05 full dossier contracts only when full dossier mode is explicitly approved
10. Historical handoff docs are reference only

Do not follow older dossier-first text for normal chat tasks.

## ALWAYS-ON SHADOW ORCHESTRATION TRIGGER

- Normal user task language must still trigger repo-first Shadow OS.
- Do not wait for the user to say `use repo`.
- Do not wait for the user to provide the repo URL if this repo is already attached.
- Do not answer from general model knowledge first.
- For content tasks, script alone is insufficient.

## SHADOW_BOOT_CONFIRMATION REQUIRED

- Every normal task must begin with `SHADOW_BOOT_CONFIRMATION`.
- If first visible output is a script/advice/summary before boot confirmation, classify `FAIL`.
- Boot confirmation must appear before content generation.
- This applies to Codex Cloud, local Codex, Claude, ChatGPT, Gemini, Kimi, DeepSeek, Perplexity, and Antigravity when the repo is attached/readable.
- `CHAT_ONLY_MODE` remains default.
- No files are created by default.

- Content tasks must include content engineering output unless user asks for script-only.
- Realtime/source-aware research must be used when current facts are required.
- If web access is unavailable, disclose the limitation and gate.
- Every 3-10 minute YouTube script must include a 45-75 second
  `CINEMATIC_SHORT_STORY_BLOCK` with character, conflict, turning point,
  cinematic visuals, emotional peak, and a bridge back to the topic.
- Real-person, real-incident, brand, company, factual case-study, and
  biographical proof claims require web-assisted research when web access is
  available. Unsupported claims prevent `SOURCE_RESEARCH_LOCK=PASS`.

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

For script routes, also load:

- `runtime_contracts/SCRIPT_LANGUAGE_CONTROL_CONTRACT.md`
- `runtime_contracts/REAL_TIME_RESEARCH_ENFORCEMENT_CONTRACT.md`
- `runtime_contracts/SOURCE_QUALITY_CLASSIFICATION_CONTRACT.md`
- `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md`
- `runtime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md`
- `runtime_contracts/LOCAL_CLOUD_HYBRID_MEDIA_EXECUTION_CONTRACT.md`
- `runtime_contracts/PROVIDER_HANDOFF_CONTRACT.md`

For Media Factory / storyboard / B-roll / visual plan / local engine handoff routes, also load:

- `runtime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md`
- `runtime_contracts/LOCAL_CLOUD_HYBRID_MEDIA_EXECUTION_CONTRACT.md`
- `runtime_contracts/DYNAMIC_TIMED_BEAT_MAP_CONTRACT.md`
- `runtime_contracts/PROVIDER_HANDOFF_CONTRACT.md`
- `runtime_contracts/LOCAL_MEDIA_FACTORY_BRIDGE_CONTRACT.md`
- `registries/route_manifests/media_factory_handoff.yaml`
- `registries/local_media_factory_bridge.yaml`
- `schemas/media_factory/scene_sync_matrix.schema.json`
- `schemas/media_factory/scene_prompt_packet.schema.json`
- `schemas/media_factory/media_factory_packet.schema.json`
- `.agents/skills/shadow-media-factory/SKILL.md`
- `skills/sub_skills/SS-116-notebooklm-visual-style-orchestrator.subskill.md`
- `skills/sub_skills/SS-117-depth-anything-v2-depth-map-generator.subskill.md`
- `skills/sub_skills/SS-118-hyperframes-html-renderer.subskill.md`

The English master draft, honest source sufficiency, dynamic timing, and
scene-synchronized Media Factory handoff are mandatory production gates.

Locked Media Factory visual laws:

- `NOTEBOOKLM_VISUAL_METHOD` uses HyperFrames CLI through SS-116/SS-118.
- `PROGRAMMATIC_SLIDE_VISUAL_METHOD`, `HTML_CSS_GSAP_VISUAL_METHOD`, and WebM
  alpha overlays use HyperFrames CLI through SS-118.
- `IMAGE_MOTION_GRAPHICS_BROLL_METHOD` uses Depth Anything V2 as a mask source
  and DaVinci Resolve Fusion for 2.5D parallax.
- `CINEMATIC_BROLL_VIDEO` must be at least 12% of total runtime in 3-10 minute
  production visual plans.
- Storyboards use the locked multi-arc table with 10 production columns plus
  the Reasoning column.
- Do not substitute tools across these methods without an explicit route
  downgrade and user approval.

Contract creation alone is not runtime propagation. Selected directors,
agents, subagents, skills, and subskills must consume the relevant script laws.
For 3-10 minute YouTube scripts, `HOOK_VARIANTS` chooses the opening hook only.
Recurring re-hooks default to a dynamic 70-90 second interval, no unexplained
gap may exceed 90 seconds, and a 5-minute script requires at least three
internal re-hooks plus a CTA hook.

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

## Layman Command Gateway Law

Codex Cloud reliable production usage:

1. Activate bootstrap once.
2. Use `Shadow <command>:` aliases for each production task.
3. Alias internally applies wrapper-required route locks.
4. Raw plain messages remain non-production proof until native persistence is proven.
5. Operator mode may hide details, but execution locks remain mandatory.

## KNOWLEDGE BASE LAW — ACTIVE

The repo contains a live knowledge base synthesized from the 3 canonical source documents.
Every agent MUST read this file before performing structural work:

- `docs/SHADOW_OS_KNOWLEDGE_BASE.md`

This knowledge base contains:
- Canonical Director Population (32 directors, all DIR IDs)
- Codex Wave build history and completion status
- Claude session history and gap inventory
- PRD v34 zero-loss laws and harness architecture
- Skill range map (M-001 through M-221+)
- Current repo state (as of 2026-06-03)
- Open gaps by priority (P1/P2/P3)
- Anti-drift rules and provider boundary law

Source documents (also in repo root — canonical):
- `Detailed_PRD_MASTERPIECE_v34_ZERO_LOSS_HARNESS_RESTRUCTURED.txt` (2.2MB — HIGHEST authority)
- `latest Claude entire Build status.txt` (158KB)
- `latest Codex entire Build status.txt` (131KB)

**Knowledge base must be read before any structural change, gap closure, or new component creation.**
