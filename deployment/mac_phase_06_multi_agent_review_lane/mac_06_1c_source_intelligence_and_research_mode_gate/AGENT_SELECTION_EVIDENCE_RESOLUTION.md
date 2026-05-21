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

`agent_layer_status=PARTIAL_NEEDS_INDEX`

## MAC-06.1A Citation Guidance

For `directors/agents/subagents/skills/subskills` evidence in proof output:

- cite matrix/registry path(s)
- cite selected file path(s) under `agents/` and `subagents/` where applicable
- cite contract standard path for selection method
- cite `/Users/apple/Documents/ShadowCreatorOS_Lightweight/registries/agent_runtime_selection_index.yaml`

## Index Status

- index path: `/Users/apple/Documents/ShadowCreatorOS_Lightweight/registries/agent_runtime_selection_index.yaml`
- line_count: `728`
- non_empty: `true`

Sample entries (from current index):

1. `agent_id=agastya`, `agent_name=agastya`
2. `agent_id=agastyaagent`, `agent_name=AgastyaAgent`
3. `agent_id=named_director`, `agent_name=named_director`
4. `agent_id=agent_control_plane_001`, `agent_name=agent_control_plane_001`
5. `agent_id=agentcontrolplane001agent`, `agent_name=AgentControlPlane001Agent`

MAC-06.1A can cite this index for agent evidence paths, but classification remains `PARTIAL_NEEDS_INDEX` until entries are curated to stable runtime agent IDs and validated task-family bindings.
