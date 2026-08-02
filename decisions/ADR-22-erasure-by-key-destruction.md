# ADR-22. Erasure by key destruction {#adr-22}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.7-evidence.md`

## Context

The second is an exemption claim, on the grounds that the log is retained under a legal obligation to which the erasure right yields. That argument is real and it sometimes wins. It is also a bet that the design's correctness rests on a legal opinion you do not control. When it loses you are holding an immutable store full of personal data and no mechanism for getting it out.

## Decision

Split evidence into chained metadata and encrypted content; erase by destroying the per-subject key.

Split the record. Metadata is chained and never encrypted: sequence number, the hash of the previous event, the operation, the identifiers, the envelope, the timestamps. Content is encrypted under a key held per data subject and referenced from the chain rather than embedded in it. Erasure destroys the key. Verification touches only metadata, so the chain still verifies with the content permanently unreadable. That single property is what makes the arrangement work rather than merely sound clever.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-22]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Redact in place, encrypt the whole chain, or delete bytes only.**

A competent architect reaches for this under time pressure: Redact in place, encrypt the whole chain, or delete bytes only. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Our judgement is that key destruction is defensible rather than settled. Supervisory opinion is not uniform on whether rendering data permanently unreadable amounts to erasure. Supervisory positions on key destruction as erasure vary by jurisdiction and date; confirm with counsel before treating the mechanism as settled law. Plan the fallback rather than the appeal. If your supervisor rejects key destruction, the next position is deleting the ciphertext object itself. That leaves the metadata chain intact and a dangling reference where the content was. A dangling reference is a fact about the past rather than personal data. If that is rejected too, you have a conflict between two legal obligations rather than an engineering problem. That is worth knowing before four engineers spend a quarter on it.

## Reopen when

Erasure-by-key-destruction fails a supervisory interpretation the organisation must meet.
