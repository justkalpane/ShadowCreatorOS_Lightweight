# D-501 Platform Metadata Generator Test Definition

status: ACTIVE_SKILL_TEST_DEFINITION
skill_id: D-501
source_skill_contract: skills/publishing/D-501-platform-metadata-generator.skill.md
source_runtime_file: skills/publishing/D-501-platform-metadata-generator.py
registry_source: registries/skill_registry_wf500.yaml
validator_scope: Phase 13D_3 D-501 downstream packaging boundary coverage
provider_execution_allowed: false
n8n_execution_allowed: false
media_generation_allowed: false
runtime_proof_claimed: false
pass_claimed: false

## Purpose

This markdown file supplies focused D-501 test-definition coverage for the cinema-preproduction boundary introduced in Phase 13D_1. D-501 remains a downstream platform metadata surface and must not become a cinema-core authority for `FILM_SCREENPLAY_GENERATION`.

## Contract Anchors

- skill_id: D-501
- source_skill_contract: skills/publishing/D-501-platform-metadata-generator.skill.md
- source_runtime_file: skills/publishing/D-501-platform-metadata-generator.py
- output_packet_family: platform_metadata_packet
- producer_workflow: SE-N8N-CWF-510-Platform-Metadata-Generator
- cinema_core_authority: false
- downstream_packaging_only: true
- preserved_content_route: SCRIPT_GENERATION
- protected_film_route: FILM_SCREENPLAY_GENERATION

## Test Matrix

| test_id | contract case | expected result |
| --- | --- | --- |
| TEST-D-501-CINEMA-001 | `FILM_SCREENPLAY_GENERATION` without a ready film packet attempts to use D-501. | Blocked; D-501 reports `cinema_core_authority=false` and `downstream_packaging_only=true`. |
| TEST-D-501-CINEMA-002 | `route_mode=film_screenplay_generation` without downstream authorization attempts to use D-501. | Blocked; canonical film route boundary remains explicit. |
| TEST-D-501-CINEMA-003 | Film route invokes D-501 only after `film_packet_ready=true` and `downstream_packaging_authorized=true`. | Metadata packet may be created as downstream packaging, with `cinema_core_authority=false`. |
| TEST-D-501-CONTENT-001 | `SCRIPT_GENERATION` invokes D-501 with normal content platform targets. | Existing platform metadata behavior remains preserved. |
| TEST-D-501-CONTENT-002 | Content/social route supplies YouTube and Instagram targets. | Platform metadata remains platform-scoped and does not require filmcraft criteria. |
| TEST-D-501-BOUNDARY-001 | D-501 output is inspected for cinema authority fields. | Output must keep `cinema_core_authority=false` and `downstream_packaging_only=true`. |

## PASS Conditions

- D-501 blocks film-core use unless a film packet is ready and downstream packaging is explicitly authorized.
- D-501 never claims cinema-core authorship authority.
- D-501 preserves `SCRIPT_GENERATION` platform metadata behavior.
- D-501 does not modify the route selector, active manifests, active slices, schemas, validators, contracts, or fixtures.
- No runtime PASS or governed runtime proof is claimed.

## FAIL Conditions

- D-501 accepts `FILM_SCREENPLAY_GENERATION` as direct cinema-core authority.
- D-501 treats thumbnails, metadata, Shorts, SEO, hooks, retention loops, or platform packaging as film-core PASS criteria.
- D-501 breaks normal `SCRIPT_GENERATION` metadata output.
- D-501 performs provider, n8n, media-generation, selector, registry, schema, validator, contract, or fixture mutation.
