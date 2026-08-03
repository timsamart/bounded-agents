# ADR-30. No shared cross-org policy domain {#adr-30}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/4.2-across-the-boundary.md`

## Context

That is a commercial motive for chapter 11's discipline rather than a compliance one. The estate that can produce a tamper-evident account of its own side settles faster than the estate that offers a reconstructed narrative. The difference is visible to people who never read an evidence schema.

## Decision

Keep the organisational boundary; use bilateral credentials, checkable claims, and contractual attestations.

The recurring proposal is to dissolve the boundary: put both organisations in one policy domain, or put a broker between them that both treat as an extension of their own TCB. Either proposal is attractive because it would let the instruments of Parts II and III apply unchanged. Both fail for the same reason they are attractive. A shared policy domain presupposes shared inputs, shared fail postures and a shared appetite for the other's incidents. A federated broker presupposes a third computing base both sides will treat as trusted for mediation and evidence. That concentrates the richest secrets of two estates in one place and replaces bilateral distrust with a single compromise story neither side controls. The construction that survives is the narrower one: credentials the recipient can verify, claims the recipient can check, and attestations the contract can demand – with the unbuildable list kept visible so that nobody fills the gaps with hope.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-30]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Dissolve the boundary into one shared policy domain or a federated broker both sides trust.**

A competent architect reaches for this under time pressure: Dissolve the boundary into one shared policy domain or a federated broker both sides trust. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

What this costs, in total, is not primarily engineering. It is bilateral agreements, per-counterparty onboarding, and an attestation register with expiry dates that a named owner watches. Teams that price only the credential format discover the legal and commercial half about two quarters late, usually when the first schedule expires and the integration is still live.

## Reopen when

A counterparty demands a shared policy domain the attenuated-credential model cannot satisfy.
