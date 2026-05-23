# AGENT READ ORDER

All future coding-agent sessions must read in this order before production work.

Repo root: `$SHADOW_REPO_ROOT`

Use repo-relative paths first. Absolute `/Users/apple/...` paths are `LOCAL_MAC_REFERENCE_ONLY`.

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

If complete required repo scope is not consumed:

- `route_scope_status=FAIL`
- `shallow_repo_routing_detected=true`
- final proof cannot be PASS.

## CANONICAL SHADOW LIGHTWEIGHT BOOT ORDER - ACTIVE LAW

1. `AGENTS.md`
2. `START_HERE_FOR_AGENTS.md`
3. `AGENT_READ_ORDER.md`
4. `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`
5. `AGENT_ANTI_DRIFT_RULES.md`
6. `runtime_contracts/ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md`
7. `runtime_contracts/ENVIRONMENT_TRIGGER_COMPATIBILITY_CONTRACT.md`
8. `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`
9. `registries/task_intent_routing_matrix.yaml`
10. `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md`
11. `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`
12. `runtime_contracts/GUMLOOP_BENCHMARK_OUTPUT_STANDARD.md`
13. `runtime_contracts/BOOTSTRAP_SYNC_PROTOCOL.md`
14. `runtime_contracts/LAYMAN_TASK_TRIGGER_CONTRACT.md`
15. `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md`
16. `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md`
17. `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md`
18. `runtime_contracts/NATIVE_AGENT_CAPABILITY_INVENTORY_CONTRACT.md`
19. `runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md`
20. `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`
21. `registries/native_capability_routing_matrix.yaml`
22. `registries/agent_runtime_selection_index.yaml`

Repo-relative paths are authoritative.
Absolute `/Users/apple/...` paths are `LOCAL_MAC_REFERENCE_ONLY`.

## SHADOW_BOOT_CONFIRMATION REQUIRED

Before any task output, the first visible output must be:

```text
SHADOW_BOOT_CONFIRMATION
agents_md_detected=true/false
agents_md_read=true/false
repo_first_orchestration_started=true/false
generic_direct_answer_avoided=true/false
shadow_mode=CHAT_ONLY_MODE
next_stage=Native Capability Assessment
```

If `AGENTS.md` is not confirmed active, return:

```text
BLOCKED: AGENTS.md was not confirmed as active.
```

## Phase A: Startup Doctrine

1. `AGENTS.md`
2. `START_HERE_FOR_AGENTS.md`
3. `AGENT_STARTUP_PROMPT.md`
4. `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`
5. `AGENT_ANTI_DRIFT_RULES.md`

## Phase B: Legacy Local Mac Runtime Context - LOCAL_REFERENCE_ONLY

5. `START_HERE_FOR_MAC_CODEX.md`
6. `MAC_CODEX_READ_ORDER_ON_FIRST_OPEN.md`
7. `SHADOW_LIGHTWEIGHT_RUNTIME.md`
8. `AGENT_OPERATING_GUIDE.md`
9. `00_READ_ME_FIRST_FOR_MAC_MIGRATION.md`

## Phase C: Operating Loop Standards

10. `deployment/mac_phase_05_repo_first_operating_loop/MAC_05_REPO_FIRST_OPERATING_LOOP_PLAN.md`
11. `deployment/mac_phase_05_repo_first_operating_loop/MAC_05_DOSSIER_FACTORY_STANDARD.md`
12. `deployment/mac_phase_05_repo_first_operating_loop/MAC_05_CONTENT_REQUEST_INTAKE_CONTRACT.md`
13. `deployment/mac_phase_05_repo_first_operating_loop/MAC_05_DIRECTOR_AGENT_SKILL_SELECTION_STANDARD.md`
14. `deployment/mac_phase_05_repo_first_operating_loop/MAC_05_QUALITY_GATE_STANDARD.md`
15. `deployment/mac_phase_05_repo_first_operating_loop/MAC_05_PROVIDER_HANDOFF_BOUNDARY.md`
16. `deployment/mac_phase_05_repo_first_operating_loop/MAC_05_FUTURE_N8N_BUS_BOUNDARY.md`
17. `deployment/mac_phase_05_repo_first_operating_loop/MAC_05_EXECUTION_NOT_ALLOWED_YET.md`

## Phase D: Contracts and Grounding

18. `runtime_contracts/MISSION_CONTEXT_CONTRACT.md`
19. `runtime_contracts/DIRECTOR_SELECTION_CONTRACT.md`
20. `runtime_contracts/SKILL_SELECTION_CONTRACT.md`
21. `runtime_contracts/DOSSIER_OUTPUT_CONTRACT.md` - `FULL_DOSSIER_ARCHIVE_MODE ONLY` or approved MAC-05 dossier mode.
22. `runtime_contracts/QUALITY_GATE_CONTRACT.md`
23. `runtime_contracts/PROVIDER_HANDOFF_CONTRACT.md` - planning/reference only unless provider execution is explicitly approved.
24. `runtime_contracts/LINEAGE_CONTRACT.md`

## Phase E: Mission Execution Rule - FULL_DOSSIER_ARCHIVE_MODE ONLY

For approved `FULL_DOSSIER_ARCHIVE_MODE ONLY` or explicit MAC-05 production dossier mode only, output one dossier containing:

- `mission.md`
- `mission_context.json`
- `selected_directors.json`
- `selected_agents.json`
- `selected_subagents.json`
- `selected_skills.json`
- `selected_subskills.json`
- `research_brief.md`
- `script_v1.md`
- `debate.md`
- `critique.md`
- `final_script.md`
- `context_engineering_packet.json`
- `provider_handoff_packet.json`
- `quality_gate_report.md`
- `lineage.json`
- `DOSSIER_README.md`

Phase E applies only to approved `FULL_DOSSIER_ARCHIVE_MODE ONLY` or explicit production dossier mode. It is not default chat mode. For normal lightweight tasks, output-consolidation rules override Phase E: chat-only creates no files, and consolidated repo-write creates one mission output file unless full dossier mode is explicitly requested.

## PHASE E OVERRIDE FOR CURRENT LIGHTWEIGHT DEFAULT

- Phase E full dossier file list applies only to approved `FULL_DOSSIER_ARCHIVE_MODE` or explicit MAC-05 production dossier mode.
- For normal lightweight tasks, `CHAT_ONLY_MODE` is default and creates no files.
- For approved repo-write tasks, `CONSOLIDATED_REPO_WRITE_MODE` creates one consolidated file only.
- MAC-06.1A proof must not create files.
- Output consolidation, chat approval gates, source-aware routing, and native capability routing override old dossier-first behavior for normal tasks.

## Phase F: Historical Source References

Use these for deeper historical context only (not as active runtime commands):

1. `Detailed_PRD_MASTERPIECE_v34_ZERO_LOSS_HARNESS_RESTRUCTURED.txt`
2. `latest Codex entire Build status.txt`
3. `latest Claude entire Build status.txt`
4. `handoff/current_windows_environment/CURRENT_WINDOWS_ENVIRONMENT_HANDOFF_INDEX.md`
5. `handoff/mac_migration/MAC_MIGRATION_ZERO_GAP_TECHNICAL_HANDOFF_V4_COMBINED_MASTER.md`
6. `archive_reference/old_quarantine_manifest/FREEZE_MANIFEST.md`
7. `archive_reference/old_quarantine_manifest/QUARANTINE_STATUS.md`
8. `handoff/historical_source_docs/HISTORICAL_SOURCE_DOCS_INDEX.md`

## Phase G: Universal Single-Agent Runtime Doctrine

Use these to understand the primary lightweight operating model:

1. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_0b_universal_single_agent_runtime_doctrine/UNIVERSAL_SINGLE_AGENT_RUNTIME_MODEL.md`
2. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_0b_universal_single_agent_runtime_doctrine/SINGLE_AGENT_CAPABILITY_CONTRACT.md`
3. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_0b_universal_single_agent_runtime_doctrine/CHAT_ONLY_OPERATION_CONTRACT.md`
4. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_0b_universal_single_agent_runtime_doctrine/REPO_WRITE_OPERATION_CONTRACT.md`
5. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_0b_universal_single_agent_runtime_doctrine/MULTI_AGENT_REVIEW_IS_OPTIONAL.md`

## Phase H: Fresh GitHub Repo Bootstrap Proof

Use these when testing whether a fresh agent can operate from GitHub `main`:

1. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_1a_fresh_github_repo_bootstrap_proof/MAC_06_1A_FRESH_GITHUB_REPO_BOOTSTRAP_PROOF_PLAN.md`
2. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_1a_fresh_github_repo_bootstrap_proof/MAC_06_1A_UNIVERSAL_AGENT_STARTER_PROMPT.md`
3. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_1a_fresh_github_repo_bootstrap_proof/MAC_06_1A_EXPECTED_OUTPUT_CONTRACT.md`
4. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_1a_fresh_github_repo_bootstrap_proof/MAC_06_1A_VERIFICATION_CHECKLIST.md`

## Phase I: Output Consolidation and Chat Approval Gates

Use these to enforce output governance:

1. `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md`
2. `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md`
3. `runtime_contracts/OUTPUT_RETENTION_AND_CLEANUP_POLICY.md`

## Phase J: Proof Status Honesty

Use these before classifying any bootstrap/review proof:

1. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_1a_fresh_github_repo_bootstrap_proof/MAC_06_1A_EXPECTED_OUTPUT_CONTRACT.md`
2. `deployment/mac_phase_06_multi_agent_review_lane/mac_06_1a_fresh_github_repo_bootstrap_proof/MAC_06_1A_VERIFICATION_CHECKLIST.md`
3. `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md`

## Phase K: Source Intelligence and Research Mode Gate

Use these to enforce source-aware repo-first behavior:

1. `runtime_contracts/SOURCE_INTELLIGENCE_AND_WEB_RESEARCH_CONTRACT.md`
2. `runtime_contracts/RESEARCH_GATE_CONTRACT.md`
3. `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md`
4. `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md`

## Phase L: Native Capability Routing

Use these to bind task routing to actual environment capabilities:

1. `runtime_contracts/NATIVE_AGENT_CAPABILITY_INVENTORY_CONTRACT.md`
2. `runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md`
3. `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md`
4. `runtime_contracts/ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md`
5. `registries/native_capability_routing_matrix.yaml`

## Phase M: Always-On Task Trigger and Content Engineering

Use these for normal layman content/script/video tasks:

1. `runtime_contracts/LAYMAN_TASK_TRIGGER_CONTRACT.md`
2. `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`
3. `.agents/skills/shadow-content-orchestration/SKILL.md`
4. `.agents/skills/shadow-research-gate/SKILL.md`
5. `.agents/skills/shadow-context-engineering/SKILL.md`

## CURRENT LIGHTWEIGHT OUTPUT LAW - ACTIVE LAW

- `CHAT_ONLY_MODE` is default for normal user tasks.
- Normal user tasks do not create files.
- `CONSOLIDATED_REPO_WRITE_MODE` requires explicit user approval.
- If repo-write is approved, create exactly one consolidated file by default: `outputs/missions/<mission_id>/MISSION_OUTPUT.md`.
- `FULL_DOSSIER_ARCHIVE_MODE` requires explicit user request.
- Any older instruction saying `create one dossier per mission` applies only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
- Do not create dossier artifacts for MAC-06.1A chat-only proof.
- Do not create file sprawl by default.
- For content/video/script tasks, script-only output is `PARTIAL` unless the user explicitly asks for script-only.
- For content/video/script tasks, `CONTENT_ENGINEERING_OUTPUT_CONTRACT` is mandatory.

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
