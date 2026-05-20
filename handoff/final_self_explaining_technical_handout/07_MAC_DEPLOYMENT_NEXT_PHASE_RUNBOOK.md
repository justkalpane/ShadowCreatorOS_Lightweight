# Mac Deployment Next Phase Runbook

## Phase 0
- objective: Mac baseline audit
- input docs: deployment/mac_phase_00_baseline/MAC_00_BASELINE_AUDIT.md
- allowed: host/tool checks
- forbidden: install/runtime/workflow actions
- pass: baseline report complete
- stop: missing critical prerequisites
- next gate: Phase 1

## Phase 1
- objective: repo transfer integrity
- input docs: deployment/mac_phase_01_repo_transfer/MAC_01_REPO_TRANSFER_AND_INTEGRITY.md
- allowed: transfer + checksum verification
- forbidden: runtime execution
- pass: counts/checksums match
- stop: mismatch/forbidden artifact
- next gate: Phase 2

## Phase 2
- objective: install required dependencies
- input docs: deployment/mac_phase_02_dependency_install/MAC_02_DEPENDENCY_INSTALL_PLAN.md
- allowed: install-now stack only
- forbidden: n8n/provider execution
- pass: toolchain verified
- stop: unresolved install gaps
- next gate: Phase 3

## Phase 3
- objective: Codex/Claude/Kimi setup
- input docs: deployment/mac_phase_03_agent_setup/MAC_03_CODEX_CLAUDE_KIMI_AGENT_SETUP.md
- allowed: CLI/auth readiness checks
- forbidden: first proof execution
- pass: agent readiness confirmed
- stop: auth/session issues
- next gate: Phase 4

## Phase 4
- objective: first repo-first dossier proof
- input docs: deployment/mac_phase_04_first_repo_proof/FIRST_MAC_REPO_FIRST_PROOF_PROMPT.md
- allowed: local repo-first generation only
- forbidden: n8n/Gemini/provider/OpenWebUI
- pass: quality gate + lineage pass
- stop: topic drift/generic output
- next gate: Phase 5

## Phase 5
- objective: future n8n execution bus design
- input docs: deployment/mac_phase_05_future_n8n_bus/FUTURE_N8N_EXECUTION_BUS_DESIGN.md
- forbidden: workflow import/execution
- next gate: Phase 6

## Phase 6
- objective: provider execution later under governance gates
- forbidden: unapproved provider execution

## Critical order rules
- Do MAC-0 only first.
- Do not run first proof until MAC-0..MAC-3 pass.
- Do not install n8n until later phase.
- Do not import workflows.
