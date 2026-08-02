# ADR-18. Approval bound to frozen call digest {#adr-18}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.5-approval-and-effect-integrity.md`

## Context

This is possible because the thing being frozen is a call at the seam – a typed operation with typed arguments, emitted at the one boundary where the non-deterministic side has to hand the deterministic side something parseable. An intention has no canonical byte representation and cannot be hashed. A call has one. That is chapter 8's contribution rather than this chapter's, and it is why the mechanism lives here and could not have lived one layer up.

Stop approving intentions. The gateway freezes the proposed call, hashes the frozen bytes, derives what the human sees from those same bytes, records the approval against the digest, and recomputes the digest immediately before execution. A payload that is not byte-for-byte the frozen call reaches execution with nothing that authorises it. It is refused because a comparison failed, not because a rule fired. Regeneration voids the approval as a mechanical fact. That is stronger than a prohibition: there is no correct implementation of *execute the regenerated call anyway*, because the object the approval points at no longer exists.

## Decision

Bind approval to a frozen call artefact via digest comparison at execution.

The alternative deserves its strongest statement. It is what most implementations do, and it arrives for free. Approve the rendered summary, keep the approval as a flag on the task, and let the orchestration layer produce the call when the flag is set. It survives retries without special handling. It lives entirely in the layer the agent team already owns. It tolerates a tool whose argument shape changes next quarter. It loses on one property, and the property is the whole point: *approved* now names a description rather than an object. The divergence between what was seen and what was done is not merely undetected. It is inexpressible. Nobody can ask the system whether the two matched, because the system never held both. Hash binding costs a durable store for frozen calls, a digest on the record, and a comparison on the execution path. It buys a question that can be asked 18 months later and answered in bytes.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-18]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Approve a rendered summary and let orchestration produce the call later.**

A competent architect reaches for this under time pressure: Approve a rendered summary and let orchestration produce the call later. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

An approval UX that cannot display a frozen artefact becomes mandatory somewhere.
