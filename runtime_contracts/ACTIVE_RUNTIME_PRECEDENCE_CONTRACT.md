# Active Runtime Precedence Contract

Current runtime precedence order:

1. User explicit instruction
2. Runtime safety boundaries
3. Output consolidation and chat approval gates
4. Source-aware research gate
5. Proof status honesty
6. MAC-06.1A proof contract
7. MAC-05 full dossier contract only when full dossier mode is explicitly approved
8. Historical handoff/migration/build docs are reference only

## Mode Clarification

- Old handoff rules that say one dossier per mission are historical unless `FULL_DOSSIER_ARCHIVE_MODE` is explicitly requested.
- `CHAT_ONLY_MODE` creates no files by default.
- `CONSOLIDATED_REPO_WRITE_MODE` creates one consolidated output file only after user approval.
- `FULL_DOSSIER_ARCHIVE_MODE` is explicit-only.

## ACTIVE RUNTIME TRUTH MAP

MAC-06.1P-C active runtime truth is limited to the files and registries below. These files may define current runtime behavior when read through the canonical boot order:

```text
ACTIVE_RUNTIME_TRUTH:
- AGENTS.md
- START_HERE_FOR_AGENTS.md
- AGENT_READ_ORDER.md
- AGENT_STARTUP_PROMPT.md
- AGENT_REPO_FIRST_OPERATING_DOCTRINE.md
- AGENT_ANTI_DRIFT_RULES.md
- handoff/agent_bootstrap/SHADOW_BOOTSTRAP_OPERATING_MODE_PROMPT.md
- handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER.md
- handoff/agent_bootstrap/SHADOW_TASK_EXECUTION_WRAPPER_COMPACT.md
- runtime_contracts/LAYMAN_COMMAND_GATEWAY_CONTRACT.md
- runtime_contracts/SHADOW_OUTPUT_MODE_CONTRACT.md
- runtime_contracts/SOURCE_BREADTH_AND_RULE_EVIDENCE_CONTRACT.md
- registries/layman_command_alias_matrix.yaml
- registries/task_intent_routing_matrix.yaml
- registries/route_manifests/*.yaml
- validators/validate_mac06_1a_output.py
```

## Historical And Future Reference Classes

The following are not active runtime law unless a later active runtime truth file explicitly connects and activates them:

```text
HISTORICAL_REFERENCE_ONLY:
- old Windows repo paths
- old n8n profile paths
- prior proof reports
- deprecated restore paths
- archive_reference/*
- handoff/historical_source_docs/*

FUTURE_EXECUTION_ONLY:
- provider/media future docs unless explicitly activated
- n8n execution bus docs unless explicitly activated
- workflow import/run instructions unless explicitly approved

PROOF_ONLY:
- proofs/*
- deployment/mac_phase_* proof reports unless cited by an active runtime truth file as a current gate
```

## Active-Language Quarantine Rule

If a file contains active-looking instructions but is not referenced by `ACTIVE_RUNTIME_TRUTH`, it must not be treated as runtime law until one of these happens:

- it is connected by an active runtime truth file;
- it is explicitly marked `ACTIVE_SUPPORTING_CONTRACT`;
- it is explicitly moved into the canonical boot order.

If a pointer scanner finds old Windows, n8n, provider, archive, proof, or historical references, those rows must be classified as historical/future/proof noise unless an active runtime truth file explicitly promotes them.
