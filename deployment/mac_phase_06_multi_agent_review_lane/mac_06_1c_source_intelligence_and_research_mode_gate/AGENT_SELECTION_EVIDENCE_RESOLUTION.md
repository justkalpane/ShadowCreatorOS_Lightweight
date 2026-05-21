# Agent Selection Evidence Resolution

## Scope

This resolution checks active agent evidence for registry-first routing without inventing components.

## Evidence Sources Reviewed

- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/registries/agent_class_matrix.json`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/registries/sub_agent_matrix.json`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/registries/director_binding.yaml`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/registries/director_binding_matrix.json`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/registries/skill_registry.yaml`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/registries/subskill_runtime_registry.yaml`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/agents/`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/subagents/`
- `/Users/apple/Documents/ShadowCreatorOS_Lightweight/deployment/mac_phase_05_repo_first_operating_loop/MAC_05_DIRECTOR_AGENT_SKILL_SELECTION_STANDARD.md`

## Classification

`agent_layer_status=PROVEN_BY_FILE_DISCOVERY`

## MAC-06.1A Citation Guidance

For `directors/agents/subagents/skills/subskills` evidence in proof output:

- cite matrix/registry path(s)
- cite selected file path(s) under `agents/` and `subagents/` where applicable
- cite contract standard path for selection method

## Recommendation

Build a dedicated `AGENT_RUNTIME_SELECTION_INDEX` synthesized from current `agents/`, `subagents/`, and registry matrices before final production seal to reduce repeated `NEEDS_CONFIRMATION` churn in proof runs.
