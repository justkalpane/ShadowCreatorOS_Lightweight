# Dialogue Subtext Contract

## Phase
12D

## Status
SKELETON_ONLY

## Scope
Future governance for the film dialogue layer. This skeleton defines the intended contract boundary without enforcement.

## Non-Binding Boundary
- This contract is not bound to runtime in Phase 12D.
- This contract does not modify runtime behavior.
- This contract does not modify route selector behavior.
- This contract does not create or bind validators.
- This contract does not create or bind schemas.
- This contract does not claim PASS.
- This contract does not claim governed runtime proof.

## Future Runtime Responsibility
This contract should govern future film dialogue decisions, keeping cinema-first behavior separate from content/platform behavior.

## Required Future Schema Links
- `schemas/film/dialogue/film_dialogue_subtext_pass.schema.json`
- `schemas/film/output_packet/film_screenplay_output_packet.schema.json`

## Required Future Validator Links
- `validators/film/dialogue/validate_dialogue_subtext.py`
- `validators/film/dialogue/validate_dialogue_voice_distinctness.py`

## Required Future Fixture Links
- `tests/fixtures/film_packet_validation/missing_dialogue_subtext_should_fail.json`

## Content Engine Preservation
Existing `SCRIPT_GENERATION` content/platform behavior remains preserved and continues to serve downstream content routes.

## Film Route Boundary
Future `FILM_SCREENPLAY_GENERATION` must be added in parallel and must not inherit content hook/re-hook/retention law as film-core PASS criteria.

## Runtime Proof Boundary
GitHub repo inspection is not governed runtime proof, and runtime IDs, PASS states, or completion certificates cannot be invented here.

## Rollback
Deletion of this skeleton contract file is sufficient rollback for Phase 12D.
