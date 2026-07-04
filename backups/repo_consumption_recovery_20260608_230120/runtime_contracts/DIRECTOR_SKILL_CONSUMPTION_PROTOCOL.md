# Director Skill Consumption Protocol

Selecting is not enough.
Citing is not enough.

A director, agent, subagent, skill, or subskill is `USED` only if:

1. Its file or registry entry was read before output generation.
2. At least 3 concrete rules were extracted.
3. Those rules changed an output decision.
4. The output includes a consumption ledger.
5. Missed rules are listed.

## Required Output Sections

Every routed task must include:

```text
DIRECTOR_CONSUMPTION_LEDGER
AGENT_CONSUMPTION_LEDGER
SUBAGENT_CONSUMPTION_LEDGER
SKILL_CONSUMPTION_LEDGER
SUBSKILL_CONSUMPTION_LEDGER
MISSED_REPO_RULES
LINE_BY_LINE_INFLUENCE_MAP
```

## Ledger Fields

Each ledger item must include:

```text
asset_name=
asset_path=
read_before_output=true/false
rules_extracted=
- <rule 1>
- <rule 2>
- <rule 3>
output_decisions_changed=
- <decision>
missed_rules=
status=USED/NEEDS_CONFIRMATION/BLOCKED
```

## Fail Law

- `NONE_SELECTED` is a fail state for any mandatory ledger.
- `NAMED_NOT_OPENED` is a fail state for selected assets.
- `READ_BUT_NO_RULES_EXTRACTED` is partial at best.
- `READ_BUT_NO_OUTPUT_INFLUENCE` is partial at best.
- Script/content output before consumption ledger is `FAIL`.
- Manifest or registry proxy binding alone is not consumption proof for a
  mandatory director, agent, subagent, skill, or subskill.

## Route Manifest Driven Consumption Law

- Consumption must be driven by the selected `route_manifest_path`.
- Every selected director, agent, subagent, skill, and subskill must have:
  - `source_path=`
  - `read_before_output=true`
  - `exact_rules_extracted>=3` unless the file is too small to contain three rules
  - `output_decisions_changed_by_rules=`
  - `missed_rules=`
- A ledger is invalid if `exact_rules_extracted` is blank.
- A ledger is invalid if `output_decisions_changed_by_rules` is blank.
- Selected-but-not-read component evidence is `FAIL` or `PARTIAL` according to route criticality.
- Missing subskill evidence is `PARTIAL` unless the route manifest declares the subskill optional.
- Missing governance director evidence is `FAIL` for production content tasks.
- `loaded=true` without route-scoped consumption evidence is not proof of use.
- `evaluated internally`, `marked as USED`, `assumed consumed`, `selected`, or
  `loaded` without a repo-relative file path and exact extracted rule evidence
  is invalid consumption evidence.
- Time limit, context pressure, or approval pressure cannot downgrade mandatory
  route actor reads into synthetic ledgers. Stop before output instead.
- `manifest proxy`, `proxy binding`, `route-manifest registry binding`, and
  `ROLE_SUMMARY only` are not enough for mandatory script-generation route
  components.
- For `SCRIPT_GENERATION`, the mandatory directors, agents, and subagents named
  in the route manifest must be individually opened before output. If any of
  them remain proxy-only, final status cannot exceed `NEEDS_CONFIRMATION`.
- For `MEDIA_FACTORY_HANDOFF`, the mandatory directors, agents, subagents,
  bridge contracts, and media-method subskills named in the route manifest must
  be individually opened before output. If any of them remain proxy-only, full
  production readiness is blocked.

## Exact Rule Evidence Law

- `consumed=true` is invalid unless exact rule evidence is present.
- `evidence_depth` must be one of:
  - `EXACT_RULE`
  - `SECTION_LEVEL`
  - `ROLE_SUMMARY`
  - `MISSING`
- Production content full `PASS` requires key route components to be `EXACT_RULE` or `SECTION_LEVEL`.
- `ROLE_SUMMARY` only allows `NEEDS_CONFIRMATION` or `PARTIAL`.
- Every selected component must feed `RULE_CONSUMPTION_EVIDENCE_LEDGER`.
- Every critical output line must feed `EXACT_RULE_LINEAGE_MAP`.
- If a mandatory route actor is represented only by `ROLE_SUMMARY`, classify the
  actor as `NEEDS_CONFIRMATION` in chat-safe output and cap final proof at
  `NEEDS_CONFIRMATION`.
- `MEDIA_FACTORY_HANDOFF` full `PASS` additionally requires
  `RULE_CONSUMPTION_EVIDENCE_LEDGER` and `EXACT_RULE_LINEAGE_MAP` to be present
  in the chat output itself, not merely implied by a validator or route lock.
