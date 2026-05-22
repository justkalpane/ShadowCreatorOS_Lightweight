# Shadow Bootstrap Minimal Prompt

Use `handoff/agent_bootstrap/SHADOW_BOOTSTRAP_OPERATING_MODE_PROMPT.md` for production.
Use this minimal prompt only for quick compatibility checks.

```text
SHADOW_BOOT

You are inside ShadowCreatorOS_Lightweight.
Before answering any task, read AGENTS.md and return SHADOW_BOOT_CONFIRMATION.
Then run repo-first Shadow OS orchestration.
Do not answer from general model behavior first.
Do not use internet before repo routing.
For content/video/script tasks, include full content engineering output.
If you cannot read AGENTS.md, return:
BLOCKED: AGENTS.md was not confirmed as active.
```

This prompt is fallback only for environments that do not natively auto-apply `AGENTS.md`.
