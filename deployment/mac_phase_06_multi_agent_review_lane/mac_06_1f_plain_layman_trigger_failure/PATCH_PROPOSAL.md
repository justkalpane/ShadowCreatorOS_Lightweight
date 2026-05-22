# MAC-06.1F Hardening Patch Proposal (No Patch Applied Yet)

This file proposes exact patch blocks to harden auto-trigger behavior. It does NOT apply them.

## Goal

Force a visible, machine-checkable boot signature so a plain layman request cannot silently bypass repo-first orchestration.

## A) AGENTS.md (Top Injection)

Add at the very top of `AGENTS.md`:

```text
SHADOW_BOOT_CONFIRMATION LAW

For every user task in this repo, before giving any final answer, the first visible output MUST include:

SHADOW_BOOT_CONFIRMATION
agents_md_detected=true/false
agents_md_read=true/false
repo_first_orchestration_started=true/false
generic_direct_answer_avoided=true/false
shadow_mode=CHAT_ONLY_MODE
next_stage=Native Capability Assessment

If you cannot confirm AGENTS.md was read, do not answer the task.
Return: BLOCKED: AGENTS.md was not confirmed as active.
```

## B) shadow-content-orchestration SKILL.md (Description Strength)

Update `description:` to be front-loaded and explicit:

```yaml
description: "Automatically use this skill for any plain user request to write a script, YouTube video, Shorts, reel, content idea, topic, storytelling, debate, critique, or context engineering output. This skill prevents generic answers and forces repo-first Shadow Creator OS orchestration, registry routing, and full content engineering."
```

## C) shadow-context-engineering SKILL.md (Description Strength)

Update `description:`:

```yaml
description: "Automatically use this skill whenever a script, video, audio, image, music, media, voiceover, provider handoff, or context packet is requested. Requires timed beat map, voice context, image prompts, video prompts, music/SFX, editing plan, platform packaging, and provider boundary."
```

## D) MAC-06.1A Proof Docs (Fail Rule)

Patch these to add an explicit fail rule:

- `deployment/mac_phase_06_multi_agent_review_lane/mac_06_1a_fresh_github_repo_bootstrap_proof/MAC_06_1A_UNIVERSAL_AGENT_STARTER_PROMPT.md`
- `deployment/mac_phase_06_multi_agent_review_lane/mac_06_1a_fresh_github_repo_bootstrap_proof/MAC_06_1A_EXPECTED_OUTPUT_CONTRACT.md`
- `deployment/mac_phase_06_multi_agent_review_lane/mac_06_1a_fresh_github_repo_bootstrap_proof/MAC_06_1A_VERIFICATION_CHECKLIST.md`

Rule:

```text
If a plain content task returns a script before SHADOW_BOOT_CONFIRMATION, classify FAIL.
```

## E) Validator (Optional Tightening)

Optionally require `SHADOW_BOOT_CONFIRMATION` literal string to appear, not only the boolean fields, so the signature is unambiguous and easy to spot.

## Risk / Tradeoff

This makes every answer begin with a structured boot signature. That is intentional: the product goal is to prevent silent generic answers.

