# Codex Cloud Compatibility Test Protocol

## TEST A - Native Auto Trigger Test

Prompt:

```text
Create a YouTube Shorts script on why AI tools fail when creators chase tools without building systems.
```

PASS requires:

- First visible output is `SHADOW_BOOT_CONFIRMATION`.
- `AGENTS.md` read=true.
- `repo_first_orchestration_started=true`.
- `generic_direct_answer_avoided=true`.

FAIL if:

- Any script/advice/source answer appears before `SHADOW_BOOT_CONFIRMATION`.

## TEST B - Bootstrap Required Test

Prompt 1:

```text
Paste contents of handoff/agent_bootstrap/SHADOW_BOOTSTRAP_MINIMAL_PROMPT.md
```

Prompt 2:

```text
Create a YouTube Shorts script on why AI tools fail when creators chase tools without building systems.
```

PASS requires:

- `SHADOW_BOOT_CONFIRMATION` appears.
- Repo-first route is used.
- Full content engineering output is produced.
- `validators/validate_mac06_1a_output.py` passes.

## Classification

- If Test A passes: `NATIVE_AUTO_TRIGGER_COMPATIBLE`.
- If Test A fails but Test B passes: `BOOTSTRAP_REQUIRED_COMPATIBLE`.
- If both fail: `REPO_VISIBLE_BUT_NOT_BEHAVIOR_ACTIVE` or `NOT_COMPATIBLE`.
