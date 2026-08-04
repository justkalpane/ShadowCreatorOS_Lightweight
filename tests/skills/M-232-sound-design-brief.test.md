# SKL-PH3C-M-232-SOUND_DESIGN_BRIEF Test Definition

status: ACTIVE_SKILL_TEST_DEFINITION
skill_id: M-232
source_skill_contract: skills/media_audio/M-232-sound-design-brief.skill.md
registry_source: registries/skill_registry.yaml
validator_scope: validators/registry_validator.cjs MISSING_SKILL_TEST_DEFINITION closure
provider_execution_allowed: false
n8n_execution_allowed: false
media_generation_allowed: false

## Purpose

This markdown file is the external test definition required for M-232 by the broad registry validator. It mirrors the deterministic tests declared in the source skill contract so registry closure can be checked without starting n8n, calling providers, or generating media.

## Contract Anchors

- skill_id: M-232
- source_skill_contract: skills/media_audio/M-232-sound-design-brief.skill.md
- output_packet_family: m232_packet
- schema_ref: schemas/packets/m232_packet.schema.json
- producer_workflow: CWF-430
- escalation_path: WF-900
- replay_path: WF-021

## Test Matrix

| test_id | contract case | expected result |
| --- | --- | --- |
| TEST-M-232-001 | Deterministic registry closure case 001 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-002 | Deterministic registry closure case 002 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-003 | Deterministic registry closure case 003 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-004 | Deterministic registry closure case 004 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-005 | Deterministic registry closure case 005 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-006 | Deterministic registry closure case 006 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-007 | Deterministic registry closure case 007 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-008 | Deterministic registry closure case 008 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-009 | Deterministic registry closure case 009 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-010 | Deterministic registry closure case 010 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-011 | Deterministic registry closure case 011 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-012 | Deterministic registry closure case 012 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-013 | Deterministic registry closure case 013 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-014 | Deterministic registry closure case 014 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-015 | Deterministic registry closure case 015 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-016 | Deterministic registry closure case 016 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-017 | Deterministic registry closure case 017 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-232-018 | Deterministic registry closure case 018 must preserve WF-900/WF-021 governance. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |

## PASS Conditions

- The source skill keeps the 12-section contract template in exact order.
- The source skill declares at least 18 deterministic TEST-M-232-### cases.
- The skill emits only its schema-bound packet family and validates against the declared schema reference.
- Missing inputs, schema failures, or governance failures route to WF-900.
- Replay or remodify requests route to WF-021.
- Dossier and packet index mutation remains append-only.

## FAIL Conditions

- The source skill loses its 12-section template.
- The source skill has fewer than 18 deterministic test cases.
- The output packet family or schema reference drifts from registry parity.
- The skill bypasses WF-900 on hard failure or WF-021 on replay.
- The skill performs destructive mutation or untyped packet emission.
