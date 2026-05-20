# Drift/Failure/Recovery Ledger

| Issue | Why It Mattered | Current Status | Mitigation | Mac Prevention Rule |
|---|---|---|---|---|
| n8n profile drift | Wrong runtime state and workflow mismatch risk | mitigated | profile path lock + quarantine docs | Never reuse old profile as active runtime |
| wrong old n8n profile risk | Could trigger wrong workflows/data | mitigated | explicit forbidden path docs | Enforce path audit in MAC-0/MAC-1 |
| workflow ID drift | Broken cross-reference/parity | mitigated | full DB export + diff | Rebuild IDs on fresh Mac runtime only |
| webhook path drift | Trigger failures | mitigated | registry-driven mapping docs | No direct path guessing |
| WF-000 simple path 404 vs registry pass | False failure interpretation | documented | use registry-routed checks | Always validate routed endpoints |
| OpenWebUI auth/model detection 401 | Misleading runtime readiness | documented | separated from core migration lane | OpenWebUI optional and later |
| Gemini 429 | Cloud rate-limit instability | documented | local-first doctrine | No provider dependency in first proof |
| generic output drift | Topic mismatch risk | mitigated | first-proof quality gate | Enforce AI-vs-Human topic gate |
| Chanakya/director activation drift | Role selection inconsistency | open (controlled) | explicit role-if-present rule | Do not invent missing roles |
| mission_context propagation drift | Packet lineage inconsistencies | open (controlled) | lineage contract docs | Validate lineage in proof report |
| repo-completion mistaken for runtime-completion | False readiness claims | mitigated | hard truth status docs | Require evidence-gated phase exits |
| Wave 2 had only 38 workflow refs | Missing template universe | repaired | full 71-workflow export | Always compare repo refs vs DB export |
| Codex V4/V5 single-file drift | Hard-to-execute handoff | repaired | command-center structure + indexes | Keep phase docs separated |
| missing handout/folder organization | Migration confusion risk | repaired | master index + runbooks | Use read-order file first |
| raw private export safety risk | Potential sensitive leakage | controlled | raw-private handling rules | Exclude raw private by default |
| 2 unknown DB-only workflows | Reuse/import ambiguity | open | classification lock marked NEEDS_CONFIRMATION | Manual review before any import/reuse |
