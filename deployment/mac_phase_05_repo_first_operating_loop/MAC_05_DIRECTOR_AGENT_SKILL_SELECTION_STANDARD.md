# MAC-05 Director/Agent/Skill Selection Standard

## Selection Method

- Registry-first always.
- Never invent directors, agents, subagents, skills, or subskills.
- Every selected item must include repo evidence path in lineage.

## Missing Item Rule

- If requested item is absent:
  - mark `NEEDS_CONFIRMATION`
  - continue with available grounded alternatives
  - do not fabricate

## Recommended Scope for First Loop Repeats

- Directors:
  - Recommended max: 4
  - Default set when present: Narada, Chanakya, Valmiki, Krishna
- Skills:
  - Recommended max: 12-20
  - Use focused cross-pack subset (topic + script + context), not full registry

## Generic Output Avoidance

- Enforce explicit conflict architecture
- Require concrete audience context
- Require position-counterposition-synthesis in debate
- Require critique delta from `script_v1` to `final_script`

## Grounding Requirements

- Directors: `directors/*` and `registries/director_contracts/*`
- Agents: `agents/AGENT_RUNTIME_REGISTRY.yaml` + file existence
- Skills: `registries/skill_registry*` + skill file existence
- Subskills: `registries/subskill_runtime_registry.yaml`

