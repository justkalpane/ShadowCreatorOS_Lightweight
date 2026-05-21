# Single-Agent Capability Contract

One agent can operate Shadow Creator OS if it can satisfy these minimum capabilities.

## Required Capabilities

- Can read the GitHub repo or receive repo context.
- Can follow `START_HERE_FOR_AGENTS.md`.
- Can read `AGENT_READ_ORDER.md`.
- Can read registry/director/skill docs as needed.
- Can create a Shadow Mission Packet.
- Can select directors/agents/subagents/skills/subskills with evidence paths.
- Can assess tools/connectors/plugins as `ACTIVE`, `PLANNED`, `NOT_ACTIVE`, or `NEEDS_CONFIRMATION`.
- Can produce research, script, debate, critique, final script, and context packet.
- Can run the quality gate logically.
- Can output to chat or create files if filesystem access exists.

## Required Safety Behavior

- Must not invent missing components.
- Must mark unavailable tools/connectors/plugins as `NOT_ACTIVE` or `NEEDS_CONFIRMATION`.
- Must not claim provider, n8n, media, or old-runtime execution unless explicitly approved and actually performed.

