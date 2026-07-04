# Shadow Creator OS - Agent Startup Law

## SHADOW_BOOT_CONFIRMATION LAW

For every user task in this repo, including simple layman requests, before giving any final answer, the first visible output MUST include:

```text
SHADOW_BOOT_CONFIRMATION
agents_md_detected=true/false
agents_md_read=true/false
repo_first_orchestration_started=true/false
generic_direct_answer_avoided=true/false
shadow_mode=CHAT_ONLY_MODE
next_stage=Native Capability Assessment
```

If you cannot confirm `AGENTS.md` was read, do not answer the task. Return exactly:

```text
BLOCKED: AGENTS.md was not confirmed as active.
```

A plain user request is enough to trigger Shadow OS.
Do not wait for the user to say `use repo`.
Do not answer with a script, summary, plan, advice, or web-sourced answer before `SHADOW_BOOT_CONFIRMATION`.

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
- `runtime/state/route_state_contract.md`
- selected `registries/route_slices/*.registry_slice.yaml`

Do not read only startup docs.
Do not read only bootstrap docs.
Do not read only `.agents` skills.
Do not copy Gumloop route names as source truth.
Do not generate content until route manifest and mandatory files are consumed.
Do not solve token drain by making the repo shallow. Solve it by making route
state explicit, blocking repeated unchanged reads without a reason, and
entering output phase after selected-route dependencies are complete.

For supported production routes, the selected route slice is mandatory. If the
route slice is missing, block before output. Do not fall back to a full registry
scan unless `audit_mode=true` or `rebuild_mode=true`.

Boot stage runs once per task, but boot files may be reread when there is a
real route or validation reason. After `ROUTE_LOCKED`, rereads require a visible
`reread_reason` such as `file_hash_changed`, `audit_mode`, `validator_mode`,
`explicit_user_requested_compare`, `route_manifest_changed`,
`krishna_directive_dependency_trace`, `semantic_influence_verification`, or
`compaction_recovery_validation`:

- `AGENTS.md`
- `START_HERE_FOR_AGENTS.md`
- `AGENT_READ_ORDER.md`
- `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`
- `AGENT_ANTI_DRIFT_RULES.md`

After `DEPENDENCIES_CONSUMED`, immediately set `output_phase_started=true` and
produce the deliverable. Additional repo expansion is drift unless the selected
route manifest explicitly authorizes it.

Historical files are dormant by default. `outputs/missions/**` requires
`continue_previous_mission=true`, `regression_mode=true`, or explicit user
reference. `downloads/chat_transcript.txt` requires `drift_audit_mode=true` or
explicit user reference.

Time, token, context, compaction, or approval pressure does not permit synthetic
repo consumption.

Forbidden shallow substitutes:

- "I cannot read all required files, so I will synthesize the ledger"
- "Additional ledgers were evaluated internally"
- "marked as USED" without file-specific read evidence
- role-summary-only director, agent, subagent, skill, or subskill consumption
- route matrix citation without selected route manifest consumption

If any required route manifest, mandatory contract, director, agent, subagent,
skill, or subskill cannot be read before content generation, return:

```text
BLOCKED_BEFORE_OUTPUT
route_scope_status=FAIL
shallow_repo_routing_detected=true
missing_required_repo_scope=<comma-separated repo-relative paths>
synthetic_consumption_attempted=false
next_stage=Read missing route scope before generating content
```

If complete required repo scope is not consumed:

- `route_scope_status=FAIL`
- `shallow_repo_routing_detected=true`
- final proof cannot be PASS.

## SCRIPT_GENERATION ROUTE SCOPE PASS LAW

For `SCRIPT_GENERATION`, `route_scope_status=PASS` is forbidden unless the
output contains a `ROUTE_SCOPE_FILE_AUDIT` before `FINAL_SCRIPT`.

Minimum proof fields:

```text
ROUTE_SCOPE_FILE_AUDIT
canonical_route_id=SCRIPT_GENERATION
route_manifest_read=true
selected_route_slice_read=true
mandatory_route_slice_paths_consumed=true
semantic_influence_map_present=true
dependencies_complete=true
output_phase_started=true
final_deliverable_generated=true
missing_required_repo_scope=None
```

The file audit must list repo-relative paths, not role names. A script output
that skips mandatory route-slice paths, omits semantic influence, or never
enters output phase is still shallow and must be blocked. Using
`route_id=route_script_generation_001` or any non-canonical route id is shallow
routing; use exactly `route_id=SCRIPT_GENERATION`.

File counts such as `total_route_scope_files_read` are telemetry only. They are
useful for audits, but they are not PASS authority and must never replace
selected route-slice completion plus semantic influence.

For real-person proof scripts, `SOURCE_RESEARCH_LOCK=PASS` or
`SOURCE_BREADTH_LOCK=PASS` requires structured `SOURCE_LEDGER` and
`FACT_VS_ANECDOTE_MAP` rows with actual page/article/interview URLs. Labels
such as `Wikipedia - Yash` or `Hindustan Times - Yash Interview` without real
URLs are not source evidence.

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

You are operating inside ShadowCreatorOS_Lightweight.

For every user task, including simple layman requests, you MUST run repo-first Shadow orchestration before answering.

Never answer directly as a generic chatbot unless the user explicitly says:

- `bypass Shadow OS`
- `answer normally without repo`

## CANONICAL SHADOW LIGHTWEIGHT BOOT ORDER - ACTIVE LAW

1. Read `AGENTS.md`.
2. Read `START_HERE_FOR_AGENTS.md`.
3. Read `AGENT_READ_ORDER.md`.
4. Read `AGENT_REPO_FIRST_OPERATING_DOCTRINE.md`.
5. Read `AGENT_ANTI_DRIFT_RULES.md`.
6. Read `runtime_contracts/ACTIVE_RUNTIME_PRECEDENCE_CONTRACT.md`.
7. Read `runtime_contracts/LAYMAN_COMMAND_GATEWAY_CONTRACT.md`.
8. Read `registries/layman_command_alias_matrix.yaml`.
9. Read `runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md`.
10. Read `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md`.
11. Read `registries/task_intent_routing_matrix.yaml`.
12. Read selected `route_manifest_path`.
13. Read `runtime_contracts/ENVIRONMENT_TRIGGER_COMPATIBILITY_CONTRACT.md`.
14. Read `runtime_contracts/TASK_INTENT_ROUTING_CONTRACT.md`.
15. Read `runtime_contracts/DIRECTOR_SKILL_CONSUMPTION_PROTOCOL.md`.
16. Read `runtime_contracts/SCRIPT_QUALITY_ENFORCEMENT_CONTRACT.md`.
17. Read `runtime_contracts/GUMLOOP_BENCHMARK_OUTPUT_STANDARD.md`.
18. Read `runtime_contracts/BOOTSTRAP_SYNC_PROTOCOL.md`.
19. Read `runtime_contracts/LAYMAN_TASK_TRIGGER_CONTRACT.md`.
20. Read `runtime_contracts/CONSOLIDATED_OUTPUT_CONTRACT.md`.
21. Read `runtime_contracts/CHAT_APPROVAL_GATE_CONTRACT.md`.
22. Read `runtime_contracts/SOURCE_AWARE_RUNTIME_DECISION_PROTOCOL.md`.
23. Read `runtime_contracts/NATIVE_AGENT_CAPABILITY_INVENTORY_CONTRACT.md`.
24. Read `runtime_contracts/TOOLS_CONNECTORS_PLUGINS_ASSESSMENT_CONTRACT.md`.
25. Read `runtime_contracts/CONTENT_ENGINEERING_OUTPUT_CONTRACT.md`.
26. Read `registries/native_capability_routing_matrix.yaml`.
27. Read `registries/agent_runtime_selection_index.yaml`.
28. If task involves storyboard, B-roll, scene prompt, visual plan, local engine handoff, or Media Factory output, read `.agents/skills/shadow-media-factory/SKILL.md`.

Repo-relative paths are authoritative. Absolute Mac paths are `LOCAL_MAC_REFERENCE_ONLY`.

No Shadow command may be answered until `runtime_contracts/LAYMAN_COMMAND_GATEWAY_CONTRACT.md`, `registries/layman_command_alias_matrix.yaml`, `runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md`, and `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md` have been loaded.

If `Shadow script:`, `Shadow task:`, or any alias in `registries/layman_command_alias_matrix.yaml` is detected, internally expand the command through `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md` before final output. If expansion cannot be proven, return `BLOCKED_BEFORE_OUTPUT`.

## Default Behavior

1. Confirm `AGENTS.md` is active.
2. Output `SHADOW_BOOT_CONFIRMATION`.
3. Read `START_HERE_FOR_AGENTS.md`.
4. Read `AGENT_READ_ORDER.md`.
5. Continue canonical boot order.
6. Run Native Agent Capability Assessment.
7. Run Task Freshness Classification.
8. Run Research Mode Decision.
9. Run registry-first routing.
10. Select directors / agents / subagents / skills / subskills with evidence.
11. Assess tools / connectors / plugins.
12. If the task is content/script/video/media related, run the Shadow Content Engineering Output Standard.
13. Output to chat by default.

## Mandatory Mode

- `CHAT_ONLY_MODE` is default.
- No files are created by default.
- Repo-write requires explicit user approval.
- Full dossier requires explicit user request.
- n8n/providers/media execution require explicit approval.

## CURRENT LIGHTWEIGHT OUTPUT LAW - ACTIVE LAW

`CHAT_ONLY_MODE` is default for normal user tasks.
Normal user tasks create no files.
`CONSOLIDATED_REPO_WRITE_MODE` requires explicit user approval.
If repo-write is approved, create exactly one consolidated file by default: `outputs/missions/<mission_id>/MISSION_OUTPUT.md`.
`FULL_DOSSIER_ARCHIVE_MODE` requires explicit user request.
Older instructions saying every mission creates a dossier apply only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
For content/video/script tasks, script-only output is `PARTIAL` unless the user explicitly asks for script-only.
For content/video/script tasks, `CONTENT_ENGINEERING_OUTPUT_CONTRACT` is mandatory.

For script/content tasks:

- The first master script is English unless the user explicitly requests
  another language or translation/localization.
- Source presence is not source sufficiency. Real-person proof scripts require
  source-quality classification and fact-versus-anecdote mapping.
- Timed beats are dynamic. Do not hard-lock output to uniform 15-second blocks
  without production justification.
- Final Media Factory drafts require scene-level synchronization and a
  local/cloud/hybrid execution plan.
- Contract creation alone is not enough. The selected directors, agents,
  subagents, skills, and subskills must consume the script behavior laws.
- Manifest or route-registry proxy binding alone is not enough for mandatory
  script-generation directors, agents, subagents, skills, or subskills.
- A named public figure or known real-world identity used as proof defaults to
  real-person treatment and cannot be silently downgraded to a composite or
  mythology anchor unless the user explicitly approves fictionalization.
- `HOOK_VARIANTS` chooses an opening hook only. Every 3-10 minute YouTube
  script requires topic-relevant recurring re-hooks at a dynamic 70-90 second
  default interval, with no unexplained gap above 90 seconds.
- A 5-minute script requires at least three internal re-hooks plus a CTA hook.
- A 3-10 minute YouTube script requires `SCRIPT_BODY_DEPTH_LOCK`; for a
  5-minute script, shallow short-form-length bodies cannot declare `PASS`.
- Missing active-layer propagation or recurring re-hook evidence prevents
  `PASS`.
- If the output claims production-ready Media Factory context, `SCENE_SYNC_MATRIX`
  is required even when provider execution remains planning-only.
- For real-person proof scripts, fact-like spoken lines must align to
  `SOURCE_LEDGER` and `FACT_VS_ANECDOTE_MAP`; a nearby source cannot justify a
  stronger rewritten claim.
- Unsupported biographical absolutes such as `every`, `always`, `never`, or
  `only` must be downgraded unless the exact strength is source-backed.
- Off-topic teaser, trailer, release, or cross-sell promotion is forbidden
  inside the spoken script unless the user explicitly requested the tie-in.

For Media Factory / storyboard / B-roll / visual plan tasks:

- HyperFrames is kept and has locked roles: NotebookLM-style dual-panel slides,
  programmatic slide/data-card/kinetic text rendering, and WebM alpha overlays.
- Depth Anything V2 is a local depth-map masking tool only; it does not generate
  images and does not replace DaVinci Resolve.
- `CINEMATIC_BROLL_VIDEO` must be at least 12% of total runtime for 3-10 minute
  production visual plans unless the user explicitly approves a downgrade.
- The storyboard format is locked to multi-arc tables with 10 production columns
  plus a Reasoning column.
- For any 3-10 minute visual plan with a cinematic real-person, real-incident,
  or backstory opening, the establishing story beats must remain
  `CINEMATIC_BROLL_VIDEO` unless the user explicitly approves a downgrade.
- A 5-minute visual plan must preserve four re-hooks at no unexplained gap above
  90 seconds and must keep A-Roll batches A through D.
- `NOTEBOOKLM_VISUAL_METHOD` consumes SS-116 and SS-118.
- `IMAGE_MOTION_GRAPHICS_BROLL_METHOD` consumes SS-117 and DaVinci Resolve
  Fusion for parallax.
- `PROGRAMMATIC_SLIDE_VISUAL_METHOD`, `HTML_CSS_GSAP_VISUAL_METHOD`, and WebM
  alpha overlays consume SS-118.

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

## SCRIPT STORY + REAL-WORLD SOURCE LAW

For every 3-10 minute YouTube script, the script-generation route must include a
`CINEMATIC_SHORT_STORY_BLOCK` before the main teaching section.

The story must run for 45-75 seconds and include:

- character
- setting
- conflict
- turning point
- cinematic visuals
- emotional peak
- lesson bridge back to the topic

The story basis must be one of:

- `real_person`
- `real_incident`
- `realistic_composite`
- `mythological_parallel`

When a script uses a real person, celebrity, brand, company, factual case study,
biographical claim, or real incident as proof, web-assisted source research is
mandatory when web access is available.

If unsupported claims remain, `SOURCE_RESEARCH_LOCK` cannot be `PASS`.
If web evidence is required but unused, final proof cannot be `PASS` unless the
user explicitly approved repo-only limited continuation.
Script-only output is `PARTIAL` unless the user explicitly requested script-only.

## FRESH LAYMAN PROOF LAW

The fresh-agent proof must use a plain layman request only.
Do not use a giant forcing prompt for the primary proof.
A detailed forcing prompt is allowed only after failure as diagnostic remediation.
The proof passes only if the repo itself triggers orchestration through `AGENTS.md` and active startup docs.

## Forbidden

- Do not produce generic LLM output before repo routing.
- Do not skip registry-first selection.
- Do not claim realtime web research unless sources were actually used.
- Do not use invalid gate statuses.
- Do not create files unless approved.
- Do not claim n8n/provider/media execution unless actually executed with approval.

Allowed gate statuses only:

- `PASS`
- `BLOCKED`
- `NEEDS_USER_APPROVAL`
- `NEEDS_CONFIRMATION`

## Layman Command Gateway Law

Codex Cloud reliable production usage:

1. Activate bootstrap once.
2. Use `Shadow <command>:` aliases for each production task.
3. Alias internally applies wrapper-required route locks.
4. Raw plain messages remain non-production proof until native persistence is proven.
5. Operator mode may hide details, but execution locks remain mandatory.
