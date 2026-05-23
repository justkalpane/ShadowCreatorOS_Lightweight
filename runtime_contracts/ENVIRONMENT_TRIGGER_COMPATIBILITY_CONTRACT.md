# Environment Trigger Compatibility Contract

This contract classifies whether a host environment actually applies Shadow Creator OS startup law before generating a response.

Repo visibility is not the same as active behavioral control. `AGENTS.md` can be present while the platform still answers from generic chat or internet-first behavior.

## Compatibility Levels

### NATIVE_AUTO_TRIGGER_COMPATIBLE

- Plain layman task triggers `SHADOW_BOOT_CONFIRMATION` first.
- `AGENTS.md` is read before answer.
- Repo-first route starts before any script, advice, summary, source, or web output.
- No explicit `use repo` prompt is needed.

### BOOTSTRAP_REQUIRED_COMPATIBLE

- Plain layman task does not auto-trigger.
- A one-time bootstrap instruction is required.
- After bootstrap, repo-first behavior can be enforced in-session.
- This is acceptable only if disclosed to the user.

### WRAPPER_REQUIRED_COMPATIBLE

- Native auto-trigger failed.
- Bootstrap activation succeeds.
- Default post-bootstrap task persistence fails.
- A compact per-task execution wrapper is required before or with each task.
- This is the reliable Codex Cloud mode until platform behavior improves.

### REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE

- Repo files are visible.
- `AGENTS.md` exists.
- Plain message bypasses repo instructions.
- This is not acceptable for native onboarding.

### NOT_COMPATIBLE

- Repo cannot be read or used.
- No valid Shadow routing can occur.

## Onboarding Rule

Do not declare `ShadowCreatorOS_Lightweight` onboarded on any platform until that platform is classified as either:

- `NATIVE_AUTO_TRIGGER_COMPATIBLE`, or
- `BOOTSTRAP_REQUIRED_COMPATIBLE` with user-approved bootstrap workflow.

If a platform is `REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE`, classify native auto-trigger as failed and run the bootstrap-required compatibility test before any onboarding claim.

## Codex Cloud MAC-06.1M Compatibility Note

```text
native_auto_trigger_status=FAILED
bootstrap_activation_status=PASS
post_bootstrap_task_persistence_status=FAILED
recovery_route_scope_lock_run_status=PASS
codex_cloud_reliable_mode=WRAPPER_REQUIRED_COMPATIBLE
wrapper_required_live_test_status=PASS_WITH_NOTICE
wrapper_required_mode_chat_only_content_tasks_usable=true
default_bootstrap_mode_onboarded=false
lightweight_os_onboarded=false
```

Do not declare default bootstrap mode onboarded for Codex Cloud while post-bootstrap layman tasks can still skip route locks, route manifests, consumption ledgers, source lock, quality lock, or governance lock.

Wrapper-required mode is usable for chat-only content tasks with notice: the route-lock structure passed, source breadth was repaired, and exact rule-consumption evidence still needs MAC-06.1N hardening.
