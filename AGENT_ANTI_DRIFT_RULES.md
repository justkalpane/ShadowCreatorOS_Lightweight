# AGENT ANTI-DRIFT RULES

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
- `recurring_rehook_required=true` for 3-10 minute YouTube scripts
- `max_gap_without_rehook_seconds<=90` unless justified
- `five_minute_minimum_internal_rehooks>=3`
- `script_quality_gate_present=true`

Shallow repo routing is `FAIL`.
Generic output after bootstrap is `FAIL`.
Selected-but-not-read director/skill/subskill is `FAIL` or `PARTIAL` according to validator.
If route evidence is missing, mark `NEEDS_CONFIRMATION` and ask whether to continue limited mode.

`HOOK_VARIANTS` chooses the opening hook only. A one-hook-only 3-10 minute
YouTube script cannot pass. Missing selected-layer propagation, missing
recurring re-hooks, or an unexplained re-hook gap above 90 seconds prevents
`PASS`.

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

## Rule 1: No Generic Chatbot Mode

- Do not answer with broad generic advice when production artifacts are requested.
- Convert requests into contract outputs. Use chat output by default; file-backed artifacts require explicit approval.

## CANONICAL SHADOW LIGHTWEIGHT BOOT ORDER - ACTIVE LAW

Use repo-relative paths first. Absolute `/Users/apple/...` paths are local Mac references only.

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

## CURRENT LIGHTWEIGHT OUTPUT LAW

- `CHAT_ONLY_MODE` is default for normal tasks.
- Normal tasks create no files.
- `CONSOLIDATED_REPO_WRITE_MODE` requires explicit user approval.
- If repo-write is approved, create exactly one consolidated file by default: `outputs/missions/<mission_id>/MISSION_OUTPUT.md`.
- `FULL_DOSSIER_ARCHIVE_MODE` requires explicit user request.
- Older lines about every mission creating a dossier apply only to `FULL_DOSSIER_ARCHIVE_MODE` or approved MAC-05 production dossier mode.
- For content/video/script tasks, script-only output is `PARTIAL` unless user explicitly asks script-only.
- For content/video/script tasks, `CONTENT_ENGINEERING_OUTPUT_CONTRACT.md` is mandatory.

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

## SHADOW_BOOT_CONFIRMATION REQUIRED

- Every normal task must begin with `SHADOW_BOOT_CONFIRMATION`.
- If first visible output is a script/advice/summary before boot confirmation, classify `FAIL`.
- Boot confirmation must appear before content generation.
- This applies to Codex Cloud, local Codex, Claude, ChatGPT, Gemini, Kimi, DeepSeek, Perplexity, and Antigravity when the repo is attached/readable.
- `CHAT_ONLY_MODE` remains default.
- No files are created by default.


## Rule 2: Registry-Only Selection

- Directors/agents/subagents/skills/subskills must be selected from repo registries/files.
- If missing, mark `NEEDS_CONFIRMATION` and continue with grounded alternatives.
- Never fabricate capability names or invocation claims.

## Rule 3: Contracts Are Law

Always enforce:

- `runtime_contracts/MISSION_CONTEXT_CONTRACT.md`
- `runtime_contracts/DIRECTOR_SELECTION_CONTRACT.md`
- `runtime_contracts/SKILL_SELECTION_CONTRACT.md`
- `runtime_contracts/DOSSIER_OUTPUT_CONTRACT.md` only in `FULL_DOSSIER_ARCHIVE_MODE ONLY` or approved MAC-05 production dossier mode.
- `runtime_contracts/QUALITY_GATE_CONTRACT.md`
- `runtime_contracts/PROVIDER_HANDOFF_CONTRACT.md` as planning/reference only unless provider execution is explicitly approved.
- `runtime_contracts/LINEAGE_CONTRACT.md`

Normal `CHAT_ONLY_MODE` tasks create no files, no dossier artifacts, and no provider execution.

## Rule 4: n8n/Provider Execution Is Off by Default

- No n8n start/install/import/execution unless explicitly approved.
- No provider or Gemini calls unless explicitly approved.
- No OpenWebUI dependency for intelligence lane.

## Rule 5: Old Runtime Is Quarantined

- Old Windows environment is reference-only.
- Do not treat old DB/profile/binaryData/workflow IDs/webhooks as active runtime truth.
- Raw private workflow exports are forensic/reference only.

## Rule 6: Truthful Artifact Claims

- Do not claim voice/video/image/avatar generation unless actually executed in approved phase.
- Provider handoff packet is planning/reference output unless execution approval exists.

## Rule 7: Quality Gate Before Commit

Hard stop if any of these fail:

- topic adherence
- generic-output detector
- grounded selection evidence
- JSON validity
- lineage completeness

## Rule 8: Commit Discipline

- Commit only after user review approval.
- Keep commits scoped and audit-friendly.
- Do not mix unrelated artifacts into the same commit.

## Rule 9: Branch Clarity

- Active production branch is `main`.
- Backup branches are rollback references only.
- Avoid branch confusion in instructions and outputs.

## Layman Command Gateway Law

Codex Cloud reliable production usage:

1. Activate bootstrap once.
2. Use `Shadow <command>:` aliases for each production task.
3. Alias internally applies wrapper-required route locks.
4. Raw plain messages remain non-production proof until native persistence is proven.
5. Operator mode may hide details, but execution locks remain mandatory.

## VISUAL_CREATION_DNA_LAW — Anti-Drift Reminder

Every image prompt in a MEDIA_FACTORY_HANDOFF output must include all 15 fields.
No prompt is complete with fewer than 15. This is repo law, not a recommendation.

Required fields (all 15 must be present per scene):

1. `subject` — who or what is in frame
2. `environment` — location, era, time of day, set dressing
3. `camera_framing` — shot type (wide/medium/close_up/etc.)
4. `lens_focal_logic` — wide_angle / standard / telephoto / macro
5. `lighting_setup` — key light direction, fill ratio, color temperature
6. `emotional_tone` — the feeling the scene must produce
7. `color_palette` — named palette with Rec.709 note
8. `cinematic_delivery_standard` — default Rec.709 unless HDR explicitly requested
9. `style_lock` — cinematic_realism / stylized_animation / etc.
10. `movement_intent` — static / slow_drift / dolly_push / pull_back / etc.
11. `negative_prompt` — must include: blurry, watermark, face_deformation
12. `drift_prevention` — IP-Adapter ref, previous frame ID, or color card ID
13. `continuity_constraints` — what must match adjacent scenes
14. `brand_persona_consistency` — identity rules preserved across all scenes
15. `safety_real_person_handling` — use_side_profile / use_silhouette / use_shadow / use_animated_inspired / no_face_generation / not_applicable

Source of truth: `runtime_contracts/MEDIA_FACTORY_FINAL_DRAFT_CONTRACT.md`
Schema enforcement: `schemas/media_factory/scene_prompt_packet.schema.json`

Missing any field → prompt cannot reach PASS → entire Media Factory draft cannot reach PASS.

## PROVIDER_HONESTY_GATE — Anti-Drift Reminder

Every Media Factory output must explicitly declare:

```text
PROVIDER_HONESTY_GATE
providers_called=true/false
n8n_used=true/false
local_media_generation_engine_used=true/false
media_artifacts_claimed=true/false
provider_execution_allowed=false
```

Do not omit this block. Do not set providers_called=true unless a provider was actually called.
Do not set local_media_generation_engine_used=true unless a local engine produced output with evidence.
Missing gate when artifacts are claimed → status downgrades from PASS to BLOCKED.

Source of truth: `runtime_contracts/PROVIDER_HANDOFF_CONTRACT.md`
