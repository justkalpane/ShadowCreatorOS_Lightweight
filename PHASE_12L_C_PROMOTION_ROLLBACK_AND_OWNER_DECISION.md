# Phase 12L-C Promotion Rollback And Owner Decision

## 1. Objective
Define rollback and owner decision rules for future promotion.

## 2. Rollback plan
Future rollback must include:
- delete promoted active manifest/slice files
- verify route selector unchanged
- verify content route remains active
- verify no film route binding happened
- rerun or inspect content preservation fixtures
- leave inactive drafts untouched
- no force push
- no runtime proof claims

## 3. Owner decision options

| Option | Meaning | Allowed later work | Forbidden work | Recommendation |
|---|---|---|---|---|
| Pause | Hold the promotion stream | No new active files | Any registry creation | Safe default |
| Repair inactive drafts | Fix draft artifacts before promotion | Draft-only fixes | Active registry creation | Useful if draft content is incomplete |
| Build promotion validator/checker | Add a gate that verifies promotion safety | Checker/validator design | Active registry creation | Recommended next step |
| Promote active manifest/slice files without selector binding | Move drafts into active registry paths only after gating | Active file creation only if gated | Selector binding | Not recommended until promotion gate exists |
| Bind selector | Connect live selector to film route | Selector edit work | Premature activation | Too early for this phase |

## 4. Recommended next phase
`Phase 12L-D: build promotion checker/validator only`

The conservative choice is to build the checker first because active registry auto-discovery risk is confirmed.

## 5. Future approval phrase
`Approved: proceed with Phase 12L-D promotion checker only.`

This phrase is recorded for later review only. It is not approved here.
