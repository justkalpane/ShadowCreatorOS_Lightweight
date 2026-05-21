# MAC-06 Review Scorecard Standard

Use 0-10 scoring (10 = best). Reviewers must score each item.

## Score Dimensions

1. Topic adherence
2. Strategic depth
3. Hook strength
4. Script specificity
5. Audience fit
6. Platform fit
7. Non-generic quality
8. Lineage truth
9. Provider handoff usefulness
10. Production readiness

## Pass Threshold

- `overall_score >= 8.0`
- No critical grounding failures
- No false execution/media claims
- No n8n/provider drift

## Critical Fail Conditions

- Invented directors/agents/skills/subskills
- JSON/contract contradictions
- Topic drift to unrelated angle
- Fake claims about generated media or executed providers

## Scoring Output

- Provide per-dimension scores.
- Provide calculated `overall_score`.
- Provide verdict:
  - `PASS`
  - `PASS_WITH_MUST_FIX`
  - `FAIL`

