# Component Readiness Matrix

| Component | Readiness Status | Mode | Transfer Status | Mac Action | Risk | Notes |
|---|---|---|---|---|---|---|
| lightweight repo constitution | ready | active | transfer-safe | use as root | low | command center established |
| directors | ready | active | transfer-safe | use after MAC-3 | medium | verify role presence |
| agents | ready | active | transfer-safe | use after MAC-3 | medium | phase-gated |
| subagents | ready | active | transfer-safe | use after MAC-3 | medium | phase-gated |
| skills | ready | active | transfer-safe | use by phase | medium | avoid drift |
| registries | ready | active | transfer-safe | validate pre-proof | low | source-of-truth |
| schemas | ready | active | transfer-safe | validation support | low | |
| validators | ready | active | transfer-safe | run post-gates | medium | no blind execution |
| runtime contracts | ready | active | transfer-safe | enforce in proof | low | |
| dossier template | ready | active | transfer-safe | use in MAC-4 | low | |
| first-proof prompt | ready | active | transfer-safe | use in MAC-4 | low | |
| n8n sanitized workflow archive | ready | reference | transfer-safe | review only | low | 71 files |
| n8n raw private archive | ready | private/forensic | not transfer-safe default | keep windows-only default | high | do not commit/transfer by default |
| current Windows handoff docs | ready | reference | transfer-safe | read for context | low | |
| Mac phase docs | ready | active | transfer-safe | execute in order | low | |
| transfer manifest | ready | active | transfer-safe | enforce include/exclude | low | |
| checksum plan | ready | active | transfer-safe | use at packaging time | low | |
| future n8n bus design | ready | deferred | transfer-safe | design stage only | medium | no live import now |
| provider handoff packet contract | partial | deferred | transfer-safe | finalize before provider phase | medium | remains gated |
| OpenWebUI reference | deferred | reference | transfer-safe | optional later | medium | not required first proof |
| Operator API reference | deferred | reference | transfer-safe | optional later | medium | not required first proof |
| old DB/profile | preserved | private/reference | not transfer-safe active | keep excluded | high | never active on Mac |
| provider credentials | not configured | private/deferred | do not transfer | configure later with gates | high | no secrets in repo |
