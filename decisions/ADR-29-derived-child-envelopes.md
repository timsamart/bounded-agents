# ADR-29. Derived child envelopes {#adr-29}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/4.1-composition.md`

## Context

Intent fails in the same shape and one step earlier. Intent is not an object with a hash. It is what Marta wanted at 09:04. The only moment the platform ever binds it to something checkable is the moment she approves a specific payload. Away from that moment it is a natural-language proposition. The thing the callee has to decide is whether a typed operation with typed arguments falls inside it. That decision is an interpretation. The only component available to perform it is a model. A model in the decision path is the one thing this document has refused since chapter 1.

Chapter 9 made an approval a decision about one frozen artefact identified by its hash. It made approval consume authority rather than grant it. I5 states the consequence: the object approved and the object executed are the same object. A child's calls are different objects, constructed by a different run, with different arguments and different hashes. There is nothing for the parent's approval to bind to. Propagating an approval down a hop is therefore not a relaxation of I5 in the interest of throughput. It is a direct contradiction of it, dressed as a convenience. The artefact it produces is an approval record pointing at a hash that was never executed, and an execution pointing at no approval at all.

## Decision

Derive attenuated child envelopes; do not propagate parent credentials or approvals.

Propagating the parent's authority and approval to the child is what every framework does by default. It is the obvious design rather than a careless one Framework defaults change monthly; treat parent-authority propagation as the observed default on your pinned versions and re-check on upgrade rather than citing a survey that will be stale on arrival.. The child is doing the parent's work, on the parent's behalf, usually inside the same process. The parent already holds a client with credentials attached. Passing them costs one line. Passing nothing costs none. Under a benign model that design is correct. It is how every delegation pattern in ordinary software has worked for thirty years. Under this document's assumption it turns the child into a widening operation with extra steps. Any content that reaches the parent can determine what the child does with the parent's full authority. The child's calls arrive at the gateway indistinguishable from the parent's. What replaces it is the derived envelope. That costs the dynamic composition that makes frameworks pleasant to use. It buys a tree in which no node holds more than the node above it.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-29]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Pass the parent client and authority to spawned sub-agents (framework default).**

A competent architect reaches for this under time pressure: Pass the parent client and authority to spawned sub-agents (framework default). It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Dynamic sub-agent composition becomes mandatory and a static delegation graph cannot express it.
