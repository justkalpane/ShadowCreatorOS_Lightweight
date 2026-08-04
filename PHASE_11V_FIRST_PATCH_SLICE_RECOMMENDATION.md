# Phase 11V First Patch Slice Recommendation

## 1. Objective

This document recommends the smallest safe first Phase 12 patch slice after the Phase 1-11U review chain.
The goal is to create repo evidence without changing runtime behavior.

## 2. Candidate slice comparison

| Slice | Scope | Runtime impact | Evidence value | Risk | Recommendation |
|---|---|---|---|---|---|
| Slice A — Fixtures-only first patch | Add non-executable canonical fixture examples, including NEET short-film, content-preservation, and no-fake-PASS examples | None | High | Lowest | Recommended |
| Slice B — Schema-skeleton first patch | Create film schema directories/files only, without wiring them | None to very low | Medium | Low to moderate | Secondary option |
| Slice C — Route-manifest draft only | Add draft film route manifest and slice entries without selector binding | Low but architectural | Medium | Higher than A | Not first choice |
| Slice D — Validator skeletons only | Create film validator skeleton files only, without enforcement binding | None to very low | Medium | Low to moderate | Not first choice |
| Slice E — Route selector integration | Update route selector / route-chain mode integration and actual routing behavior | Yes | High | Highest | Do not attempt first |

## 3. Recommended first patch slice

### Phase 12A: Fixtures-only + non-executable canonical examples

Recommended content:

- NEET short-film canonical fixture
- content preservation fixture for `SCRIPT_GENERATION`
- downstream handoff fixture for trailer/teaser/release adaptation
- no-fake-PASS fixture for incomplete film packets
- film-vs-content collision fixture
- source-led real-incident fixture that requires source ledger and fact-vs-anecdote separation

Why this is the safest first patch:

1. It creates tangible repo evidence.
2. It does not alter runtime behavior.
3. It does not require route binding, contract enforcement, or schema execution wiring.
4. It preserves the current content engine and downstream stack exactly as-is.
5. It gives the later schema/contract/validator work a concrete acceptance surface.

## 4. What should not be included in the first patch

- route selector changes
- validator enforcement changes
- schema binding changes
- contract rewrites
- implementation behavior changes
- any replacement of `SCRIPT_GENERATION`
- any claim of film-route PASS

## 5. Rollback posture

If the first patch slice creates confusion or collision, rollback should remove only the new fixture files and leave the content engine and all audit docs intact.

## 6. Final recommendation

Choose Slice A first.

This is the smallest safe patch batch that can prove the new film boundary with evidence while keeping the current runtime untouched.

## Proposed Phase 12A File Targets

The first patch batch should only create fixture/example files at paths like:

- `tests/fixtures/film_route_selection/neet_short_film.json`
- `tests/fixtures/film_route_selection/five_minute_neet_short_film.json`
- `tests/fixtures/film_route_selection/youtube_neet_script.json`
- `tests/fixtures/film_route_selection/instagram_reel_neet_script.json`
- `tests/fixtures/film_route_selection/cinematic_explainer_youtube.json`
- `tests/fixtures/film_packet_validation/valid_minimal_film_packet.json`
- `tests/fixtures/film_packet_validation/missing_beat_sheet_should_fail.json`
- `tests/fixtures/film_packet_validation/missing_character_arc_should_fail.json`
- `tests/fixtures/film_packet_validation/missing_scene_turns_should_fail.json`
- `tests/fixtures/film_packet_validation/content_packet_pretending_film_should_fail.json`
- `tests/fixtures/content_preservation/youtube_script_preserved.json`
- `tests/fixtures/content_preservation/shorts_script_preserved.json`
- `tests/fixtures/content_preservation/reel_script_preserved.json`
- `tests/fixtures/downstream_handoff/trailer_after_film_packet.json`
- `tests/fixtures/downstream_handoff/visual_plan_after_film_packet.json`
- `tests/fixtures/downstream_handoff/voice_context_after_film_packet.json`
- `tests/fixtures/no_fake_pass/github_read_not_runtime_proof.json`
- `tests/fixtures/no_fake_pass/film_packet_without_schema_should_fail.json`
- `tests/fixtures/no_fake_pass/content_validator_cannot_pass_film_packet.json`

These are design targets only. They must not be created in Phase 11V.

## Phase 12A Acceptance Gate

Phase 12A passes only if all of the following remain true:

- only fixture/example files are added
- no runtime behavior changes
- route selector is not modified
- no schemas are enforced
- no validators are enforced
- no contracts are modified
- no route manifests or slices are bound
- the existing content engine is untouched
- the NEET short-film fixture exists
- a YouTube/content preservation fixture exists
- a no-fake-PASS fixture exists
- a downstream handoff fixture exists
- no PASS/runtime proof is claimed
- rollback is simple fixture file deletion
