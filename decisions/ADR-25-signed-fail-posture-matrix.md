# ADR-25. Signed fail-posture matrix {#adr-25}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/1.4-solution-strategy.md`, `chapters/3.3-failure-postures.md`

## Context

Every dependency in this system has a defined behaviour when it is unavailable. The only question is whether that behaviour was chosen in a design review or discovered at 03:40 UTC by whoever was on call. Undefined behaviour under partial outage is not an absence of a decision. It is a decision, made by the default in a library. It is usually fail-open, because fail-open is what an availability-minded engineer writes when nobody has told them that this particular call moves money.

What a user sees is part of the specification rather than a courtesy. In degraded operation a refused call returns the platform's refusal object carrying the posture, the matrix version, and the capability set currently in force. The run receives a refusal it can reason about instead of an undifferentiated failure. Marta's queue shows why an action is unavailable rather than showing it greyed out. A degraded platform that looks like a broken one produces the same phone calls as a broken one. The phone calls are a cost you can remove for the price of one field.

## Decision

Fill a dependency×tier fail-posture matrix before launch; the consequence owner signs it.

The move is a matrix with one row per dependency and one column per risk tier, filled in before launch and signed by the person who owns the consequence. Policy service unreachable: refuse, for tier one; permit within a stated staleness budget, for tier three. Evidence path unreachable: no side effects, at every tier. Model provider unavailable, or routing outside the allowed model set: terminate the run rather than continue it on a substitute. You fill these rows in a design review with the business owner in the room. That is the only setting in which the answer is a decision rather than a default.

## Consequences

What it costs: about a day per tier of argument between platform, security, and the business owner, repeated whenever a dependency is added, plus a quarterly drill that is a deliberate outage of your own making. Fail-closed rows cost availability in exactly the hour you will be asked about it. And the emergency path stops being an agent with elevated authority and becomes a human acting directly on the system of record. That is slower, and is the point.

If the evidence path cannot write, effects do not happen, at every tier and for every dependency. Chapter 11 argued this as an ordering property. The operational form is narrower and more useful than the principle: the platform does not have a posture available to it here, because the only alternative is a period of action with no record, which is the exact state this document exists to make impossible. The period is what makes it unrecoverable. A stopped queue is visible in minutes, has an owner, and ends. An hour of external effects with no record is discovered later, cannot be enumerated, and cannot be repaired, because authority is not reconstructible after the fact.

Markers `[ADR-25]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Leave posture as an unsigned platform recommendation decided on the bridge.**

Revocation belongs to the same discipline. A stop that has never been executed against a live run is a hypothesis. The interval is a number in the matrix and the quarterly drill turns it into a measurement. Chapter 13 engineers the decision path as the latency-critical component it is. Chapter 14 forces the matrix into a design review. Chapter 15 replaces the single kill switch with five distinct mechanisms.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

A dependency appears for which no declared fail posture is honest.
