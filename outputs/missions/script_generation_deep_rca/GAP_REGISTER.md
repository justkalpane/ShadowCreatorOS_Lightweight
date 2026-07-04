# Gap Register

This file collects the missing details that were identified across the conversation and the repo audit.

## Gap 1: Debate / Critique / Refinement Was Not Visible Enough

- **what the user expected:** a mandatory audit layer that actively critiques and refines every task
- **what the repo shows:** critique/refinement and governance are required surfaces
- **what failed:** the earlier output did not visibly prove that critique was actually run as a gate
- **why it matters:** without visible critique delta, the script can look polished while still being retention-weak
- **upgrade needed:** expose a critique pass block before final script approval

## Gap 2: Approval Gate Was Not Surfaced as a Real Decision Point

- **what the user expected:** clear approval, rejection, or repair trail
- **what the repo shows:** approval gates and governance lock are required
- **what failed:** the previous output did not present an auditable approval chain
- **why it matters:** the script can be accepted without proving it survived quality review
- **upgrade needed:** show visible gate statuses in chat

## Gap 3: The Script Was Article-Like Instead of Spoken

- **what the user expected:** crisp, fascinating, spoken-for-camera writing
- **what the repo shows:** spoken runtime fit and script structure are mandatory
- **what failed:** the script stayed too explanatory and even-paced
- **why it matters:** viewers hear fatigue before they feel the hook
- **upgrade needed:** shorter lines, more interrupts, more spoken cadence

## Gap 4: Beat Map Was Not Operational Enough

- **what the user expected:** a production-grade dynamic timeline
- **what the repo shows:** 3-20 second blocks with duration reason, purpose, and retention reset goal
- **what failed:** the beat map behaved like an outline
- **why it matters:** editors and retention systems cannot work from a summary
- **upgrade needed:** beat-by-beat control with timing reasons

## Gap 5: Re-hook Rhythm Was Too Soft

- **what the user expected:** attention-grabbing resets every relevant interval
- **what the repo shows:** recurring re-hooks are mandatory, with a default 70-90 second interval
- **what failed:** the re-hooks did not feel like real attention pivots
- **why it matters:** retention decays when the viewer does not feel movement
- **upgrade needed:** stronger hooks, sharper transitions, more emotional pressure

## Gap 6: Real-Person Proof Was Not Ledgered

- **what the user expected:** source-backed claims for Yash
- **what the repo shows:** source ledger and fact-vs-anecdote map are required
- **what failed:** facts were used but not visibly mapped
- **why it matters:** source integrity becomes hard to audit
- **upgrade needed:** structured source rows plus claim rows

## Gap 7: Story Arc Was Too Thin

- **what the user expected:** a cinematic Yash arc that pulls the viewer in
- **what the repo shows:** 45-75 second cinematic story block
- **what failed:** the story was too compressed
- **why it matters:** the story should create emotional momentum, not just context
- **upgrade needed:** setup, conflict, turning point, payoff, bridge

## Gap 8: Validation Evidence Was Missing

- **what the user expected:** proof that the draft passed or failed on each gate
- **what the repo shows:** weakest-gate validation scorecard is mandatory
- **what failed:** the output did not display a real scorecard
- **why it matters:** without the scorecard, the final state is hard to trust
- **upgrade needed:** visible gate-by-gate scoring

## Gap 9: Line-Level Traceability Was Missing

- **what the user expected:** detailed RCA and influence tracing
- **what the repo shows:** line-by-line influence map is required
- **what failed:** no traceability from line to gate or source
- **why it matters:** a polished output can hide weak construction
- **upgrade needed:** map major lines to source or retention logic

## Gap 10: Governance State Was Not Explicit

- **what the user expected:** the system should behave like a quality board
- **what the repo shows:** governance lock is a formal part of the route
- **what failed:** the earlier output did not show the governance record
- **why it matters:** governance without visibility cannot be audited
- **upgrade needed:** explicit governance block with status and repair route

## Gap 11: Route-State Evidence Was Missing

- **what the user expected:** proof that the route was actually followed
- **what the repo shows:** route-state capsule and audit-event evidence are part of the execution model
- **what failed:** route-state evidence was not surfaced
- **why it matters:** the task can appear solved while the underlying process is unverified
- **upgrade needed:** route-state capsule fields in the audit pack

## Gap 12: Re-hook Timing Change Will Need Repo-Wide Cleanup

- **what the user requested for later:** change the re-hook default from 90 seconds to 25 seconds
- **what the repo shows:** the same interval appears in multiple contracts and manifests
- **what failed:** nothing yet, but the change cannot be safely local-only
- **why it matters:** partial updates will create internal inconsistency
- **upgrade needed:** patch all timing references together later

## Missing Details Collected from the Conversation

- The user repeatedly asked for a forensic RCA, not a polished summary.
- The user wanted explicit separation between repo defect and model/module defect.
- The user wanted proof that the audit/debate/approval process was actually followed.
- The user wanted every missing gap captured before blueprinting or patching.
- The user wants the re-hook interval tightened later, but only after the RCA is approved.

## Final Note

This register is intentionally gap-first, not solution-first.

The repair work should begin only after the stricter RCA table is approved.
