# ADR-24. Embedded policy evaluation {#adr-24}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/3.2-hot-path.md`

## Context

The rejected alternative is a network call to a central policy decision point for every decision. It is genuinely better on the property that matters most here. Freshness is exact. A rule narrowed at 14:02 is in force at 14:02 everywhere. There is no propagation to measure, no staleness table to write, and no class of incident in which two enforcement points disagree about what the policy says. It is also easier to operate: one deployment, one version, one place to look when a decision surprises somebody. Anyone who has run an estate with a central authorisation service knows it works. The reason teams reach for it is not naivety.

Policy is authored centrally. It is compiled into a versioned and signed bundle. It is distributed to every enforcement point in advance. It is evaluated as a local function call. There is no synchronous call to a policy service on the decision path.

## Decision

Evaluate policy locally from signed, versioned bundles on the hot path.

It loses on two properties, both about a bad day rather than a good one. The first is arithmetic. A synchronous round trip inside every decision adds a network to a path that had none. The p99 of a remote call under load is not the p99 of a local one. The second is correlation. A central decision point is a component whose degradation is a governance outage across every agent at once. The fail posture for one dependency decides whether the whole platform refuses or permits. Kai does not need to defeat the policy to reach that state. He needs the platform loaded enough that its operators are choosing between refusing everything and turning the check off. Local evaluation removes the round trip and decomposes the failure. It pays for both in freshness.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-24]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Synchronous remote call to a central decision service on every call.**

A competent architect reaches for this under time pressure: Synchronous remote call to a central decision service on every call. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Measured p99 of embedded evaluation exceeds a staleness budget a central call can meet.
