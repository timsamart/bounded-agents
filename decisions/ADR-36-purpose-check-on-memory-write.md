# ADR-36. Purpose check on memory write {#adr-36}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.6-data-retrieval-memory.md`

## Context

Each of the three obvious scopes fails somewhere. The failures are worth naming rather than ranking. Agent-scoped memory lets one principal's content shape another principal's run. That defeats entitlement-resolved retrieval on the write side, where no amount of care at read time repairs it. Principal-scoped memory preserves the entitlement model exactly and destroys most of the value, because the organisational learning an agent estate is bought for is the cross-principal part. Organisation-scoped memory is the aggregation problem adopted as a design goal. The tiered arrangement keeps the first tier honest by making its admission criterion mechanical: an item enters organisation scope only if its provenance chain contains no principal-derived input. That is a query rather than a judgement.

Aggregation is the failure that hides behind a set of individually correct decisions. An agent reads claims history under a valid entitlement, reads underwriting history under a valid entitlement, writes the joined inference to memory, and has produced a fact that neither data owner released and no policy evaluated. Entitlement checks are per item and per principal. They are blind to composition. That is how a governed agent estate becomes a data warehouse with no schema and no owner, discovered eventually by whoever is asked to answer for it. Purpose limitation is the obligation that bites here, and it bites at the moment of composition rather than at the moment of reading.

## Decision

Run purpose and composition checks on the memory write path for cross-context items.

So content that crosses a bounded context is carried with derived provenance and a purpose check performed at write time. Write time is the only moment at which the composition is visible: the item knows which contexts contributed to it, the purposes attached to each are available, and the check evaluates whether the composite is permitted under both. At read time that information is gone, because a read sees a stored fact and cannot tell what was joined to make it. The cost is a policy evaluation on the memory write path. That is a second place where the decision path sits in a latency-sensitive route. The benefit is that a forbidden composite never becomes a stored fact rather than being caught at some later point by an audit.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-36]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Catch forbidden composites later at read or audit time.**

A competent architect reaches for this under time pressure: Catch forbidden composites later at read or audit time. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

The coincidence deserves an honest sentence. Purpose binding arrived from chapter 2 as an imposed data-protection obligation. It turns out to be the control that limits blast radius across tasks. That is a nicer outcome than the project earned. It did not come from foresight, and the argument for it here does not rest on the regulation. If the obligation were withdrawn tomorrow, this mechanism would stay. The part of it that exists only because the article exists is the documentation burden, which is priced as compliance cost and not as security.

## Reopen when

Product value requires write-time combinations the purpose model cannot express.
