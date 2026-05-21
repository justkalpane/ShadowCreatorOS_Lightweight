# Director Skill Selector Proof Standard

## Proof Requirement

Every agentic runtime proof must show that selection came from repo evidence.

## Required Selection Evidence

- Directors selected from real registry/contract files.
- Agents selected from real repo files or registries.
- Subagents selected from real repo files or registries.
- Skills selected from real repo files or registries.
- Subskills selected from real repo files or registries.

## Required Fields

- selected item name
- selection reason
- evidence path
- confidence
- role in output

## Missing Component Rule

If a requested director/agent/skill/subskill is not present in repo evidence, mark it `NEEDS_CONFIRMATION`.

## Hard Fail

Invented directors, agents, skills, subskills, workflow IDs, provider executions, or media artifacts fail the proof.

