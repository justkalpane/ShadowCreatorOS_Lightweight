# MAC-06.1A Fresh GitHub Repo Bootstrap Proof Plan

## Purpose

Prove that a fresh repo-aware agent can operate Shadow Creator OS directly from GitHub `main` without relying on this current Mac Codex chat memory.

## Proof Model

The agent receives:

- GitHub repo: `https://github.com/justkalpane/ShadowCreatorOS_Lightweight`
- Branch: `main`
- Instruction: detect/read `AGENTS.md` first if available, then read `START_HERE_FOR_AGENTS.md`
- Simple user task: create a YouTube Shorts script on the requested topic

## What The Agent Must Prove

- The first visible output is `SHADOW_BOOT_CONFIRMATION`, before any script/summary/advice.
- It reports `shadow_boot_confirmation_present=true` and `first_visible_output_is_boot_confirmation=true`.
- It starts from the repo, not internet-first behavior.
- It follows `START_HERE_FOR_AGENTS.md` and `AGENT_READ_ORDER.md`.
- It detects and reads `AGENTS.md` before all other repo instructions when available.
- It uses the canonical startup order from `AGENTS.md`.
- It cites `registries/native_capability_routing_matrix.yaml`.
- It cites `registries/agent_runtime_selection_index.yaml`.
- For content/script/video tasks, it follows `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`.
- It remains `CHAT_ONLY_MODE`; `files_created=false` and `dossier_artifacts_created=false`.
- It creates a Shadow Mission Packet.
- It loads repo context.
- It routes registry-first.
- It classifies task intent using `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`.
- It selects `route_id` from `registries/task_intent_routing_matrix.yaml`.
- It reads `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md`.
- It reads `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`.
- It reads `runtime_contracts/GUMLOOP_BENCHMARK_OUTPUT_STANDARD.md`.
- It selects directors, agents, subagents, skills, and subskills with real evidence paths.
- It includes director, agent, subagent, skill, and subskill consumption ledgers.
- It includes `MISSED_REPO_RULES` and `LINE_BY_LINE_INFLUENCE_MAP`.
- For script/content tasks, it includes topic quality gate, 3 hook variants, hook generation gate, script quality gate, and rewrite if needed.
- It reports `shallow_repo_routing_detected=false`.
- It reads `runtime_contracts/ROUTE_DEPENDENCY_EXPANSION_PROTOCOL.md`.
- It reads `runtime_contracts/TASK_EXECUTION_STATE_MACHINE_CONTRACT.md`.
- It reports `route_manifest_path=`.
- It reports `route_manifest_read=true`.
- It includes `TASK_ROUTE_LOCK`, `ROUTE_DEPENDENCY_EXPANSION_LOCK`, `CONSUMPTION_LOCK`, `SOURCE_RESEARCH_LOCK` when required, `QUALITY_LOCK`, and `GOVERNANCE_LOCK`.
- It reports `route_scope_complete=true`.
- It reports `mandatory_files_read_before_output=true`.
- It reports `script_generated_after_all_locks=true`.
- It reports `loaded_true_but_not_consumed_detected=false`.
- It reports `manual_rerun_structured_but_partial_detected=false` for any PASS claim.
- It assesses tools/connectors/plugins honestly as `ACTIVE`, `PLANNED`, `NOT_ACTIVE`, or `NEEDS_CONFIRMATION`.
- It produces research, script, debate, critique, final script, and context engineering packet.
- It runs a quality gate.
- It returns output to chat or repo depending on access.
- It does not execute n8n, providers, media, Gemini API, OpenWebUI, or old runtime.

## Fail-Fast Rule

If a plain content task returns any final answer/script/summary/outline/advice before `SHADOW_BOOT_CONFIRMATION`, classify `FAIL`.

If a script/content task routes shallowly by naming directors or skills without reading and consuming their files, classify `FAIL`.

PASS is impossible if:

- no task route is selected
- `registries/task_intent_routing_matrix.yaml` is not cited
- no consumption ledger is present
- no 3 hook variants are present for script/content tasks
- no quality scores are present
- no line-by-line influence map is present
- shallow repo routing only is detected
- script is generated before director/skill consumption
- route manifest is not read
- mandatory route files are not read before output
- route scope is incomplete
- output appears before task route, route dependency expansion, consumption, quality, or governance locks
- governance lock is missing
- source/current claims appear before source lock
- content engineering is present but consumption, influence, or quality proof is missing

## Environment Compatibility Split

Test A - Native Auto Trigger:

- Plain layman task must produce `SHADOW_BOOT_CONFIRMATION` as the first visible output.
- PASS means platform classification may be `NATIVE_AUTO_TRIGGER_COMPATIBLE`.

Test B - Bootstrap Required:

- Run only if Test A fails.
- Use `handoff/agent_bootstrap/SHADOW_BOOTSTRAP_MINIMAL_PROMPT.md`.
- PASS means platform classification is `BOOTSTRAP_REQUIRED_COMPATIBLE`, not `NATIVE_AUTO_TRIGGER_COMPATIBLE`.

If Test A and Test B both fail, classify the platform as `REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE` or `NOT_COMPATIBLE`.

## Supported Agent Types

The proof may be run with Codex, Claude, ChatGPT, Kimi, DeepSeek, Gemini, Perplexity, Antigravity, local LLM apps, or other repo-aware LLM/coding agents.

A successful Codex proof is the first representative proof, not the only possible future proof. Other agents can be progressively tested later. Users must not be forced to install all agents.
