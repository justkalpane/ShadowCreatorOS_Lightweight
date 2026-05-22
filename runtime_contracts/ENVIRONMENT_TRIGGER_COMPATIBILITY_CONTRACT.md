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
