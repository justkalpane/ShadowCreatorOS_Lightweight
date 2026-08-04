# Phase 12L-F Next Phase Recommendation

## 1. Objective
Recommend the next phase after owner decision packet creation.

## 2. Recommended Path

If the owner wants to continue toward film-engine activation, recommend:

```text
Phase 12L-G: controlled active manifest/slice promotion only, no selector binding
```

## 3. Why Not Selector Binding Yet

- Active files have not yet been promoted.
- Promoted files need post-promotion static lint.
- Selector binding should remain separate.
- Runtime proof cannot be claimed from repo files alone.

## 4. Required Approval Phrase

Use exactly:

```text
Approved: proceed with Phase 12L-G controlled active manifest/slice promotion only, no selector binding.
```

Do not approve this phrase yourself.

## 5. Stop Conditions

Phase 12L-G must stop if:

- checker does not return `PROMOTION_GATE_READY_FOR_OWNER_DECISION`
- active target files already exist unexpectedly
- route selector references `FILM_SCREENPLAY_GENERATION`
- inactive drafts fail parsing
- required prep artifacts are missing
- owner approval phrase is absent
- unrelated dirty files would be staged
- any runtime PASS/proof claim appears

