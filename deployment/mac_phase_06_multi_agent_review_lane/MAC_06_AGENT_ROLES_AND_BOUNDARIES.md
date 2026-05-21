# MAC-06 Agent Roles and Boundaries

## Primary Operator

### Codex

- Owns dossier production under MAC-05 loop.
- Owns final integration of approved reviewer feedback.
- Owns final JSON validation and quality-gate truth.
- Owns commit preparation after user approval.

## Optional Reviewer Agents

### Codex Self-Review / Internal QA

- Can run a self-audit against the review scorecard.
- Useful for catching obvious doctrine, JSON, lineage, and quality-gate gaps.
- Does not count as external multi-agent proof by itself.

### Claude

- Architecture, reasoning quality, doctrine compliance review.
- Finds logical gaps, weak claims, and strategy inconsistency.

### Kimi

- Creativity, hook strength, audience resonance review.
- Improves clarity, pacing, emotional pull, memorability.

### DeepSeek

- Structure, schema, consistency, and JSON/contract review.
- Verifies internal coherence across dossier artifacts.

### ChatGPT

- Strategy, critique, prompt, and operating-model review.
- Can produce chat-only packets when local repo write access is unavailable.

### Perplexity

- Research/source-validation reviewer lane.
- Used for freshness, source confidence, fact risk, and claim verification.
- Does not modify dossier directly.

### Gemini Chat/App

- Optional chat/app reasoning lane if user chooses it.
- Gemini API calls remain forbidden unless separately approved.

### Antigravity

- Optional repo-aware coding/operator lane if installed and user-approved.
- Must return MAC-06 review packets or contract outputs.

### Other Coding Agents

- Allowed only if they follow `/Users/apple/Documents/ShadowCreatorOS_Lightweight/START_HERE_FOR_AGENTS.md`.
- Must use review packet contract and scorecard format.

### Generic Future Repo-Aware Agent Lane

- Any future coding/reasoning agent is allowed only if it can read the repo and follow `START_HERE_FOR_AGENTS.md`, `AGENT_READ_ORDER.md`, MAC-05, and MAC-06 contracts.

## Role Boundaries

- Reviewers do not execute providers.
- Reviewers do not run n8n.
- Reviewers do not invent directors/skills/subskills.
- Reviewers propose; Codex applies approved changes.
- User approval is required before finalization commit.
- Chat-only agents may return packets without local repo writes.
- External agents must not fake repo access, provider execution, or media artifacts.
