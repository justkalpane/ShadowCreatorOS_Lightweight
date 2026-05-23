# Script Quality Enforcement Contract

Every script/content task must include these gates before final verdict.

## TOPIC_QUALITY_GATE

```text
relevance_score=
trend_source_score=
audience_fit_score=
novelty_score=
production_feasibility_score=
approved=true/false
reason=
```

## HOOK_GENERATION_GATE

```text
hook_variant_1=
hook_variant_2=
hook_variant_3=
score_each=
selected_hook=
selection_reason=
```

## SCRIPT_QUALITY_GATE

```text
emotional_strength_score=
clarity_score=
novelty_score=
retention_score=
creator_specificity_score=
visualizability_score=
CTA_strength_score=
overall_score=
pass_threshold=
passed=true/false
```

## Rewrite Law

- If `overall_score < pass_threshold`, rewrite before final.
- If hook score is weak, generate new hooks.
- If visualizability is weak, route to visual/context skill.
- If emotional strength is weak, route to emotion rewrite.
- If creator specificity is weak, route to audience/persona skill.
- Do not label script output final until the gate passes or the user explicitly approves limited mode.
- Hook variants require scores and rejection reasons.
- Quality gate requires scores plus `pass_threshold`.
- Rewrite is required if `overall_score < pass_threshold`.
- Governance lock must approve the final script.
- Final output cannot classify as `PASS` if `SCRIPT_QUALITY_GATE` is missing.
- Manual structured output without a quality scorecard is `PARTIAL`, not `PASS`.
