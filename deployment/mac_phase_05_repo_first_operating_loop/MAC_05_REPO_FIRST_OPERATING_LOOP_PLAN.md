# MAC-05 Repo-First Operating Loop Plan

## Objective

Convert the successful MAC-04 one-off proof into a repeatable repo-first production loop that remains execution-safe until separately approved.

## Loop Definition

1. User content request
2. `mission_context`
3. Director selection
4. Agent/subagent/skill/subskill selection
5. `research_brief`
6. `script_v1`
7. `debate`
8. `critique`
9. `final_script`
10. `context_engineering_packet`
11. `provider_handoff_packet`
12. `quality_gate`
13. `lineage`
14. User review
15. Commit after approval

## Required Inputs

- Topic
- Platform
- Audience
- Objective
- Constraints
- Approval mode
- Provider handoff needed (yes/no)
- n8n execution needed (yes/no; planning-only phase defaults to no)
- Repo contracts and registries

## Required Outputs

- One dossier folder following naming standard
- Required dossier file set
- Valid JSON packet set
- Quality gate report
- Lineage record
- Phase result report

## Allowed Files

- New dossier path under `dossiers/`
- Current phase report under `deployment/mac_phase_*`

## Forbidden Files

- `.env*`
- credential/token/cookie/key material
- runtime DB snapshots
- raw private n8n export folders
- media artifacts falsely claimed as generated

## Stop Gates

- Missing required dossier files
- Invalid JSON packets
- Invented directors/agents/skills/subskills
- Topic drift/generic output
- False media/provider execution claims

## Review Gates

- Topic adherence
- Grounding evidence in repo paths
- Script specificity and tension quality
- Provider handoff completeness (reference-only mode)
- Lineage truthfulness

## Commit Gates

- User review complete
- Safety scan pass
- JSON validation pass
- Quality gate pass
- No forbidden file staging

