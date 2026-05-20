# AGENT REPO-FIRST OPERATING DOCTRINE

## Why This Lightweight Path Exists

The old ShadowEmpire full-runtime lane was quarantined because it was too heavy for immediate production intelligence work:

- n8n runtime complexity and workflow drift risk
- OpenWebUI routing/auth instability
- Gemini quota/rate-limit instability
- webhook/workflow ID drift
- mission-context and lineage degradation risk
- high debugging overhead with provider-heavy coupling

The lightweight repo exists to keep intelligence deterministic and auditable:

- GitHub repo is the constitution/brain.
- Coding agents are the reasoning/runtime operators.
- Dossier artifacts are the production truth.
- n8n and providers are deferred execution layers, not intelligence prerequisites.

## Active Production Loop (MAC-05)

1. User content request
2. `mission_context`
3. director selection
4. agent/subagent/skill/subskill selection
5. `research_brief`
6. `script_v1`
7. `debate`
8. `critique`
9. `final_script`
10. `context_engineering_packet`
11. `provider_handoff_packet`
12. `quality_gate`
13. `lineage`
14. user review
15. commit after approval

## Mandatory Agent Behaviors

- Read repo first and obey `main` branch doctrine.
- Follow runtime contracts in `runtime_contracts/`.
- Use registry-backed selections only.
- Build dossier outputs exactly to contract.
- Validate JSON packet files before commit.
- Stop on drift, missing evidence, or invalid packets.

## Work Allowed Without n8n

- topic intake normalization
- research brief
- script generation and refinement
- debate and critique
- final script
- context engineering packet
- provider handoff packet (reference mode only)
- quality gate report
- lineage
- commit/push after explicit review approval

## Work Deferred to Future Execution Layer

- voice generation
- avatar generation
- image/video generation
- publishing execution
- analytics pulls from providers
- scheduled monitoring automations
- provider orchestration
- n8n execution bus activation/import/execution
- credentialed API execution

## Branch Discipline

- Operate on `main` unless user explicitly directs otherwise.
- Do not use backup branches for active production.
- Keep backup/history branches as rollback evidence only.

