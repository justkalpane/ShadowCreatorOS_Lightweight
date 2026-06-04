# M-034 Micro Cliffhanger Engine Test Definition

status: ACTIVE_SKILL_TEST_DEFINITION
skill_id: M-034
source_skill_contract: skills/script_intelligence_army/M-034-micro-cliffhanger-engine.skill.md
registry_source: registries/skill_registry.yaml
validator_scope: validators/registry_validator.cjs MISSING_SKILL_TEST_DEFINITION closure
provider_execution_allowed: false
n8n_execution_allowed: false
media_generation_allowed: false

## Purpose

This markdown file is the external test definition required for M-034 by the broad registry validator. It mirrors the deterministic tests declared in the source skill contract so registry closure can be checked without starting n8n, calling providers, or generating media.

## Contract Anchors

- skill_id: M-034
- source_skill_contract: skills/script_intelligence_army/M-034-micro-cliffhanger-engine.skill.md
- output_packet_family: m034_packet
- schema_ref: schemas/packets/m034_packet.schema.json
- producer_workflow: CWF-210
- escalation_path: WF-900
- replay_path: WF-021

## Test Matrix

| test_id | contract case | expected result |
| --- | --- | --- |
| TEST-M-034-001 | Deterministic contract case 001 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-002 | Deterministic contract case 002 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-003 | Deterministic contract case 003 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-004 | Deterministic contract case 004 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-005 | Deterministic contract case 005 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-006 | Deterministic contract case 006 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-007 | Deterministic contract case 007 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-008 | Deterministic contract case 008 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-009 | Deterministic contract case 009 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-010 | Deterministic contract case 010 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-011 | Deterministic contract case 011 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-012 | Deterministic contract case 012 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-013 | Deterministic contract case 013 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-014 | Deterministic contract case 014 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-015 | Deterministic contract case 015 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-016 | Deterministic contract case 016 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-017 | Deterministic contract case 017 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |
| TEST-M-034-018 | Deterministic contract case 018 passes with WF-900/WF-021 governance preserved. | PASS requires schema-bound packet output, append-only mutation, WF-900 error route, WF-021 replay route, and registry-consistent lineage. |

## PASS Conditions

- The source skill keeps the 12-section contract template in exact order.
- The source skill declares at least 18 deterministic TEST-M-034-### cases.
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
