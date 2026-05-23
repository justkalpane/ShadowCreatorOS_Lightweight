# MAC-06.1L Bootstrap Persistence Failure Report

MAC_06_1L_BOOTSTRAP_PERSISTENCE_FAILURE_STATUS=FAIL

## Latest Evidence

- Preflight PASS at commit `c9d73a28da8d551639f95edd73bd18729f43b2d3`.
- Bootstrap activation PASS.
- Plain layman task still generated direct script after `SHADOW_BOOT_CONFIRMATION`.
- Self-audit returned FAIL.
- Route lock missing.
- Route manifest not read before script.
- Consumption lock missing.
- Source lock missing.
- Quality lock missing.
- Governance lock missing.
- `FINAL_VERDICT=GENERIC_OUTPUT_AFTER_BOOTSTRAP`.

## Conclusion

MAC-06.1J/K repo enforcement exists, but Codex Cloud does not reliably persist and execute the lock sequence automatically after bootstrap.

The current platform behavior proves:

- Native auto-trigger failed.
- Bootstrap activation works.
- Default post-bootstrap task persistence failed.
- Wrapper-required mode is the reliable Codex Cloud mode until platform behavior improves.

## Required Future Fix

Create a compact `SHADOW_TASK_EXECUTION_WRAPPER` prompt that users can paste before or with each task if Codex Cloud does not honor persistent bootstrap.

Keep `handoff/agent_bootstrap/SHADOW_BOOTSTRAP_OPERATING_MODE_PROMPT.md` as the session activator.

Add compatibility note:

```text
native_auto_trigger_status=FAILED
bootstrap_activation_status=PASS
post_bootstrap_task_persistence_status=FAILED
codex_cloud_reliable_mode=WRAPPER_REQUIRED_COMPATIBLE
```

## Safety Boundary

n8n_started=false
providers_called=false
media_artifacts_created=false
dossier_4_started=false
commit_performed=false
push_performed=false

safe_to_declare_lightweight_os_onboarded=false
safe_to_start_n8n_execution_bus=false

NEXT_ACTION=Design SHADOW_TASK_EXECUTION_WRAPPER and update compatibility docs before any further Test B rerun.
