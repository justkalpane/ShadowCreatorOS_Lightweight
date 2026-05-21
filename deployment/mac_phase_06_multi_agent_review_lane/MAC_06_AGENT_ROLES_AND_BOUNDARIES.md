# MAC-06 Agent Roles and Boundaries

## Primary Operator

### Codex

- Owns dossier production under MAC-05 loop.
- Owns final integration of approved reviewer feedback.
- Owns final JSON validation and quality-gate truth.
- Owns commit preparation after user approval.

## Optional Reviewer Agents

### Claude

- Architecture, reasoning quality, doctrine compliance review.
- Finds logical gaps, weak claims, and strategy inconsistency.

### Kimi

- Creativity, hook strength, audience resonance review.
- Improves clarity, pacing, emotional pull, memorability.

### DeepSeek

- Structure, schema, consistency, and JSON/contract review.
- Verifies internal coherence across dossier artifacts.

### Other Coding Agents

- Allowed only if they follow `/Users/apple/Documents/ShadowCreatorOS_Lightweight/START_HERE_FOR_AGENTS.md`.
- Must use review packet contract and scorecard format.

## Role Boundaries

- Reviewers do not execute providers.
- Reviewers do not run n8n.
- Reviewers do not invent directors/skills/subskills.
- Reviewers propose; Codex applies approved changes.
- User approval is required before finalization commit.

