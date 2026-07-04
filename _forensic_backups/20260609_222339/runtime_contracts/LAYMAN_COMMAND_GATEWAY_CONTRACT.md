# MAC-06.1O Layman Command Gateway Contract

## Purpose

The Layman Command Gateway lets a user give simple Shadow commands while the repo internally enforces the full Shadow Task Execution Wrapper.

The long wrapper prompt remains the execution engine. The layman command is the user-facing trigger.

## Compatibility Status

```text
native_auto_trigger_status=FAILED
bootstrap_activation_status=PASS
post_bootstrap_task_persistence_status=FAILED
codex_cloud_reliable_mode=WRAPPER_REQUIRED_COMPATIBLE
raw_plain_task_default_production_proof=false
shadow_command_gateway_required=true
```

## Command Families

### Shadow Task

```text
command_family=Shadow task
prefixes=Shadow task:, Shadow:, Run Shadow:
route_mode=AUTO_CLASSIFY
internal_wrapper_required=true
```

Use this for generic route detection across all supported Shadow OS routes.

### Shadow Script

```text
command_family=Shadow script
prefixes=Shadow script:, Script:, Write script:
route_id=SCRIPT_GENERATION
internal_wrapper_required=true
```

Routes to script generation with task route lock, route manifest, source breadth when needed, exact rule evidence, quality gate, governance gate, and content engineering.

### Shadow Topic

```text
command_family=Shadow topic
prefixes=Shadow topic:, Topic:, Find topic:, Pick topic:
route_id=TOPIC_DISCOVERY
internal_wrapper_required=true
```

Routes to topic discovery with trend/research qualification, scoring, and approval gate.

### Shadow Refine

```text
command_family=Shadow refine
prefixes=Shadow refine:, Refine script:, Improve script:
route_id=SCRIPT_REFINEMENT
internal_wrapper_required=true
```

Routes to script refinement, critique, debate, retention, and quality governance.

### Shadow Context

```text
command_family=Shadow context
prefixes=Shadow context:, Context engineering:, Create production packet:
route_id=CONTEXT_ENGINEERING
internal_wrapper_required=true
```

Routes to context engineering and production packet creation without provider execution.

### Shadow Voice

```text
command_family=Shadow voice
prefixes=Shadow voice:, ElevenLabs context:, Voice prompt:
route_id=VOICE_CONTEXT
internal_wrapper_required=true
```

Routes to voice context, emotion, prosody, SSML, and provider boundary.

### Shadow Video

```text
command_family=Shadow video
prefixes=Shadow video:, Avatar video:, Video prompt:, Sora prompt:, Runway prompt:, Kling prompt:, Pika prompt:
route_id=AVATAR_VIDEO_CONTEXT
internal_wrapper_required=true
```

Routes to avatar/video context, scene planning, gesture, visual consistency, and provider boundary.

### Shadow Package

```text
command_family=Shadow package
prefixes=Shadow package:, Packaging:, Thumbnail:, Metadata:
route_id=EDITING_PACKAGING
internal_wrapper_required=true
```

Routes to editing, packaging, thumbnail, title, description, hashtags, and retention packaging.

### Shadow Full

```text
command_family=Shadow full
prefixes=Shadow full:, Full pipeline:, Complete content package:
route_id=FULL_VIDEO_PIPELINE
internal_wrapper_required=true
execution_boundary=planning_only_no_provider_execution
```

Routes to full pipeline planning only. It must not start n8n, call providers, create media, or execute workflows without explicit approval.

## Required Law

- Any command beginning with `Shadow task:` or a specific `Shadow <route>:` alias must internally apply `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md`.
- User does not need to paste the long wrapper manually.
- Raw plain messages without Shadow prefix remain not production-proof in Codex Cloud until future platform behavior proves otherwise.
- If the assistant skips locks after a Shadow command, final status must be `FAIL`.
- If user asks for `proof mode`, show all locks, ledgers, source maps, exact rule evidence, quality gates, and final proof.
- If user does not ask for proof mode, use compact operator output but still execute locks internally.

## Required Gateway Proof

```text
layman_command_gateway_used=true/false
shadow_command_alias_detected=true/false
shadow_command_alias=
raw_user_task_preserved=true/false
internal_wrapper_applied=true/false
output_mode=PROOF_MODE/OPERATOR_MODE/DEBUG_MODE
operator_mode_used=true/false
proof_mode_requested=true/false
```

## Deterministic Command Expansion Block

For every detected Shadow command, output mode may be compact, but the internal expansion proof must exist before final content:

```text
SHADOW_COMMAND_EXPANSION_REQUIRED_OUTPUT
shadow_command_alias_detected=true
raw_user_task_preserved=true
alias_matrix_entry_used=true
route_id_resolved=true
route_manifest_loaded=true
internal_wrapper_applied=true
output_mode_resolved=true
compact_or_proof_output_allowed_only_after_locks=true
```

Required expansion sequence:

1. Detect the alias from `registries/layman_command_alias_matrix.yaml`.
2. Preserve the raw user task exactly.
3. Resolve `route_id` or `route_mode`.
4. Load the selected route manifest.
5. Internally apply `handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md`.
6. Resolve output mode from `runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md`.
7. Execute all locks before final output.

If any required expansion field is false or missing:

```text
final_status=FAIL
BLOCKED_BEFORE_OUTPUT
failed_lock=SHADOW_COMMAND_EXPANSION
reason=Shadow command alias did not expand through the internal wrapper.
```

Normal final content is forbidden when command expansion is incomplete.

## Fail Conditions

- `shadow_command_alias_detected=true` and `internal_wrapper_applied=false`
- `shadow_command_alias_detected=true` and `alias_matrix_entry_used=false`
- `shadow_command_alias_detected=true` and `route_manifest_loaded=false`
- `shadow_command_alias_detected=true` and `output_mode_resolved=false`
- `shadow_command_alias_detected=true` and `compact_or_proof_output_allowed_only_after_locks=false`
- `operator_mode_used=true` and no compact lock summary exists
- raw plain post-bootstrap task is claimed as production proof without automatic locks
- Shadow command output claims `PASS` while route lock, dependency expansion, consumption, source breadth, rule evidence, quality, or governance lock is missing


## MAC-06.2D ARTICLE PIPELINE ROUTE CONNECTION

- Output may claim media-pipeline readiness only when route manifests cite `mac_06_2d_article_pipeline_connections`.
- Provider execution remains disabled unless an explicit `approval_packet` authorizes execution scope.
- Contract-only media packet references are insufficient; route-level validator bindings must be present.
