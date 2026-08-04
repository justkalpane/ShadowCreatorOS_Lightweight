# Phase 10: Test Fixture Route Split Plan

## 1. Objective

Phase 10 audits the test-fixture layer and designs the future fixture family for cinema-first route separation. The goal is to preserve the current content, downstream media, and governance fixtures, while adding a canonical film-route fixture set that can prove the difference between a true screenplay packet and a content-mode packet.

## 2. Relationship to Phases 1-9

Phase 1 found director-level drift.
Phase 2 found agent-level drift.
Phase 3 found subagent-level drift.
Phase 4 found skill-layer drift and missing filmcraft skills.
Phase 5 found subskill-layer drift and missing filmcraft subskills.
Phase 6 found missing film contract family.
Phase 7 found missing film route family.
Phase 8 found missing film validator family.
Phase 9 found missing film schema family.
Phase 10 now checks whether the fixture layer can prove all of that separation in practice.

## 3. Existing fixture families already present

The repo already contains useful fixture families that should be preserved:

* script/content acceptance fixtures
* content-mode gold and bad script fixtures
* route-scope and route-state fixtures
* no-fake-pass and evidence-bundle fixtures
* media-factory / visual / audio / downstream handoff fixtures
* phase0 governance / proof-plane fixtures

These are good foundations, but they are not yet organized around cinema-first film-route proof.

## 4. Fixture boundary decision

The future fixture design should separate into these lanes:

* Film route fixtures
* Content route fixtures
* Downstream distribution fixtures
* Governance / proof fixtures
* Collision and failure fixtures

That separation matters because a film packet should not be able to pass using content-mode hook or retention fixtures, and a content packet should not be able to impersonate a film screenplay packet.

## 5. Non-goals

Phase 10 does not create executable tests yet.
Phase 10 does not patch validators.
Phase 10 does not patch schemas.
Phase 10 does not patch route manifests or routes.
Phase 10 only defines the future fixture plan.
