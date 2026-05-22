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
