# ADR-28. Paved road as product {#adr-28}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/3.6-the-paved-road.md`

## Context

The rejected option deserves its strongest form, because it is how almost every organisation does this and the reasons are not bad ones. A project has a budget, a deadline and an executive sponsor. That combination is what gets a platform built at all. A product with a roadmap and no date gets built in year three, by which time the estate has grown its own answer. Security ownership puts the tooling next to the people who hold the threat model, which is where the judgement lives about which steps can be shortened and which cannot. The gateway at Borealis exists because somebody wrote a charter with a date on it. No product proposal would have survived the same funding round.

The paved road is funded as a product with a named owner and a standing team, in the same quarter as the gateway rather than the one after it, and not as security-owned tooling delivered by a project.

## Decision

Own the paved road as a product with an adoption objective measured in days, not as a time-boxed security project.

What the project form cannot do is outlive itself. A project ends. The team disperses into the next charter. The road stops being paved on the day the last ticket closes, while the estate it was paved for keeps changing weekly. The second failure is worse. A project is measured on scope delivered and a security-owned project on control coverage. Neither of those is a duration. Nobody in the funding structure is accountable for the number that decides whether the control is used. The number is therefore not collected. A road with no owner degrades in the direction of whoever files the most tickets rather than whoever quietly left. A product has an owner whose objective is adoption, a backlog fed by the engineers on the road, and a headline metric measured in days.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-28]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Fund a project that ends when the last ticket closes.**

A competent architect reaches for this under time pressure: Fund a project that ends when the last ticket closes. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

The paved road loses adoption for a quarter despite funded ownership.
