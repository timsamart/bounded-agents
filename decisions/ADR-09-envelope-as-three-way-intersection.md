# ADR-09. Envelope as three-way intersection {#adr-09}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.2-the-envelope.md`

## Context

Three parties decide what a run may do, and the run receives only what all three permit. The team that owns the agent declares what the task needs. The identity estate supplies what the human principal can reach. The risk tier supplies the ceiling for work of this kind. The envelope is the intersection, computed at run start. It is empty if any of the three is empty.

## Decision

Derive the envelope as declared need ∩ principal reach ∩ tier ceiling at run start.

Each input answers a question the other two cannot. Declared need knows what the task does and knows nothing about who is asking. Principal reach knows Marta's entitlements and has no opinion about claims triage. The tier knows what a category of work is allowed to cost when it goes wrong and knows nothing about either. Take any one of them alone and you have a familiar failure. Need alone is the agent team granting itself authority. Reach alone is the agent inheriting a human's whole working life. The ceiling alone is a policy that permits everything the worst case permits. Least privilege has been the settled answer for fifty years. The intersection is what that principle looks like when it stops being an aspiration and becomes a computation performed by a machine at a specific moment, on inputs that have owners and can be produced in an incident review.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-09]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Treat any single input as sufficient authority.**

A competent architect reaches for this under time pressure: Treat any single input as sufficient authority. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Production measurements show one input dominates the intersection.
