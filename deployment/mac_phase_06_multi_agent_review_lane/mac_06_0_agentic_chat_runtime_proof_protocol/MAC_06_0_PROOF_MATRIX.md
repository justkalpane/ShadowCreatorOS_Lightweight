# MAC-06.0 Proof Matrix

## P-01 Codex Repo-Write Proof

- Status: Partially proven.
- Evidence:
  - Production Dossier #2
  - Production Dossier #3
- Requirement: Map proof evidence to full architecture pipeline before readiness seal.
- Product implication: Successful Codex proof is enough to prove one representative single-agent repo-aware operation path.

## P-02 Cross-Agent Chat Proof

- Agents:
  - ChatGPT
  - Claude
  - Kimi
  - DeepSeek
  - Perplexity
  - Gemini chat/app
  - Antigravity
- Test:
  - User provides GitHub repo and `START_HERE_FOR_AGENTS.md` instruction.
  - Agent returns Shadow Mission Packet and output packet in chat.
  - No repo write required.

## P-03 External Reviewer Proof

- Test:
  - External reviewer returns review packet for Dossier #3.
  - Packet must follow MAC-06 review packet contract.

## P-04 Codex Finalization Proof

- Test:
  - Codex applies only user-approved reviewer changes.
  - Codex revalidates JSON, quality gate, and lineage.

## P-05 Execution Bus Boundary Proof

- Test:
  - Provider handoff packet remains reference-only until explicit approval.
  - No n8n/provider/media execution occurs during repo-first proofs.

## Readiness Implication

MAC-06.0 defines the proof requirements. It does not complete cross-agent proof by itself.

MAC-06.0B clarifies that cross-agent proof is progressive compatibility work. It must not be interpreted as a requirement to install every agent before normal lightweight OS use.
