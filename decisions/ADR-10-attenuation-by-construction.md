# ADR-10. Attenuation by construction {#adr-10}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.2-the-envelope.md`

## Context

Delegation narrows because the interface that derives a child envelope from a parent offers narrowing and revocation, and offers no third operation. There is no widening call to authorise, to audit, or to get wrong.

## Decision

Make envelope widening unrepresentable; no widen operation exists.

The alternative is the one most systems have: a rule in the policy engine saying that a sub-agent's authority does not exceed its parent's. That rule is reviewable. It is testable. It is enforced by code that a competent team wrote on a Thursday. A rule that can be violated by a bug is not an invariant. It is a control with an unmeasured failure rate, sitting exactly where the blast radius is largest. Its failure mode is silent, because a widened envelope looks like a working system. Making the operation absent moves the property out of the enforcement path and into the shape of the data, where a bug produces an error rather than an escalation.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-10]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Enforce non-widening only as a policy-engine rule.**

This is the capability tradition's actual contribution, and it is older than the problem we are applying it to. Authority is held as a reference that cannot be forged or named from outside. The only thing a holder can do with it is pass on something equal or weaker. That property, rather than any quantity of exhortation, is what resolves the confused deputy. The deputy's problem was never that it was stupid. It was that authority and instruction shared one channel, so text arriving in the channel could designate authority the deputy held. Here, the run cannot name its authority. It names an operation and arguments, and the ceiling those are checked against is not addressable from inside the run. Instructions that arrive in a claim document can ask for anything they like. There is nothing for the asking to point at.

## Cost

Cost is stated in the arguing chapter. This record does not invent a figure the spine does not price.

## Reopen when

A legitimate widening case cannot be expressed as a new run.
