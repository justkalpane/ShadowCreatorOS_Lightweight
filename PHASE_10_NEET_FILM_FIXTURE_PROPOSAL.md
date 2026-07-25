# Phase 10 NEET Film Fixture Proposal

## 1. Purpose

The NEET short-film case should become the canonical film-route fixture because it is a concrete screenplay-like request that can prove the difference between a cinema-first route and a content-first route.

The fixture must show that:

* the request is routed to film mode, not YouTube/script-content mode
* the resulting packet contains filmcraft structure
* the packet fails if mandatory film fields are missing
* the packet fails if a content-mode packet is disguised as a film packet
* repo reading alone does not count as governed runtime proof

## 2. Canonical fixture concept

Recommended fixture name:

```text
neet_short_film_canonical_film_route.json
```

Optional companion text fixture:

```text
neet_short_film_canonical_film_route.md
```

## 3. Fixture intent

The fixture should encode a request like:

* short film
* screenplay
* cinematic story
* feature-film style not required
* film-first route required
* downstream distribution optional

The route expectation should be `FILM_SCREENPLAY_GENERATION` once that route exists.

## 4. Required fields in the canonical film fixture

At minimum, the canonical NEET film fixture should expect:

* route state capsule
* route ID and route mode
* film intent lock
* source research status
* source ledger
* fact vs anecdote map
* logline
* theme
* premise
* genre
* tone
* cinematic world
* protagonist want
* protagonist need
* protagonist flaw
* protagonist arc
* antagonist or opposing force
* character web
* beat sheet
* three-act map
* eight-sequence map
* scene list
* scene objective / obstacle / tactic
* scene conflict and turn
* dialogue subtext pass
* dialogue voice distinctness pass
* visual motif / image system
* mise-en-scène notes
* blocking and composition notes
* camera language / lens / framing notes
* sound motif / silence design
* performance direction
* screenplay body
* screenplay formatting status
* director’s notes
* production notes
* downstream handoff recommendations
* film validation scorecard
* no-fake-PASS gate result
* unsupported claims ledger
* lineage / consumption ledger
* final status

## 5. Success and failure modes

The NEET fixture should pass only when the film packet is complete and the film route is chosen.

It should fail when:

* beat sheet is missing
* character arc is missing
* scene turns are missing
* a content-only packet is supplied
* a downstream media packet is mistaken for a screenplay packet
* repo inspection is mistaken for runtime proof

## 6. Relation to existing fixture families

The NEET fixture should sit beside, not replace:

* the current script/content fixtures
* the current route-state and evidence fixtures
* the current downstream visual/media fixtures
* the current governance and no-fake-pass fixtures

## 7. Non-goals

This is not an executable test yet. It is the design target for the future Phase 11 implementation patch plan and the eventual film-route test suite.
