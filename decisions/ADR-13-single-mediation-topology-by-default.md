# ADR-13. Single mediation topology by default {#adr-13}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.3-complete-mediation.md`

## Context

It loses on three properties that arrive together as the estate grows. Latency: every call crosses the network to one location, which for a domain whose system of record sits in another region is tens of milliseconds at p99 before the decision path has done anything, on top of the 20–40 ms at p99 the decision itself already costs. Blast radius: the component that mediates everything is the component whose failure stops everything, and its fail posture stops being a per-domain risk decision and becomes one decision taken centrally by people who cannot hold every domain's tolerance in their heads. Organisational reality: one gateway needs one team holding change control over every integration in the company, and the claims platform's release train is not the treaty system's, so the first domain that cannot take an upgrade holds everybody else's.

The single central gateway is the stronger design on the property this chapter cares about most. Conceding that is cheaper than pretending otherwise. One place to count turns coverage into a query rather than a reconciliation. One policy version removes the distribution problem entirely. One deployment means one upgrade, one key rotation, and one rotation of people who know how the thing behaves at three in the morning. An organisation in a position to have that is better off with it. A small estate with one network and one change window is in that position.

## Decision

Prefer a single mediation gateway topology; treat federation as an expensive relocation of difficulty.

Federating moves the difficulty rather than removing it, and the place it moves to is expensive. With one gateway the policy bundle sits where the decisions are made. With several, one signed bundle reaches several places at slightly different moments. Bundle staleness acquires a number. That number becomes a security parameter. The hot path acquires a distribution dependency it did not have before. Chapter 13 pays that bill and it is not a rounding error. Coverage measurement gets dearer too, because the number becomes a sum across deployments with a reconciliation underneath it and more places for a path to be counted twice or not at all.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-13]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Federated multi-gateway as the default.**

A competent architect reaches for this under time pressure: Federated multi-gateway as the default. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Estate shape or protocol forces a different topology with measured benefit.
