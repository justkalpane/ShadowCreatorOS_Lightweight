# Save The Cat Beat Sheet Contract

## Phase
12D

## Status
SKELETON_ONLY

## Scope
Future governance for the film story_structure layer. This skeleton defines the intended contract boundary without enforcement.

## Non-Binding Boundary
- This contract is not bound to runtime in Phase 12D.
- This contract does not modify runtime behavior.
- This contract does not modify route selector behavior.
- This contract does not create or bind validators.
- This contract does not create or bind schemas.
- This contract does not claim PASS.
- This contract does not claim governed runtime proof.

## Future Runtime Responsibility
This contract should govern future film story_structure decisions, keeping cinema-first behavior separate from content/platform behavior.

## Required Future Schema Links
- `schemas/film/story_structure/film_beat_sheet.schema.json`
- `schemas/film/story_structure/film_validation_scorecard.schema.json`

## Required Future Validator Links
- `validators/film/story_structure/validate_save_the_cat_beat_sheet.py`
- `validators/film/validation/validate_film_scorecard_no_fake_pass.py`

## Required Future Fixture Links
- `tests/fixtures/film_packet_validation/missing_beat_sheet_should_fail.json`
- `tests/fixtures/film_packet_validation/valid_minimal_film_packet.json`

## Content Engine Preservation
Existing `SCRIPT_GENERATION` content/platform behavior remains preserved and continues to serve downstream content routes.

## Film Route Boundary
Future `FILM_SCREENPLAY_GENERATION` must be added in parallel and must not inherit content hook/re-hook/retention law as film-core PASS criteria.

## Runtime Proof Boundary
GitHub repo inspection is not governed runtime proof, and runtime IDs, PASS states, or completion certificates cannot be invented here.

## Rollback
Deletion of this skeleton contract file is sufficient rollback for Phase 12D.
