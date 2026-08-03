# ADR-04. Obligation-derived requirements {#adr-04}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.2-constraints.md`

## Context

Regulation (EU) 2024/1689 (the AI Act) needs a preliminary honesty. Most agent deployments are not high-risk systems under the classification. A chapter that implies otherwise is doing a vendor's marketing without being paid for it. Where the classification does bite, the two obligations that touch this design are record-keeping across the system's lifetime and human oversight. Both are demonstration obligations. Neither describes what oversight looks like for a system taking four thousand actions between 03:00 and 09:00 with nobody awake. The field does not currently have an answer to that question. Stating it as unsolved is more useful than a control that names a reviewer who cannot possibly read what they are reviewing.

Regulation (EU) 2016/679 (GDPR) binds hardest in two places, and they pull against each other. Purpose limitation constrains memory: content gathered to triage a claim acquires a purpose when it is written, and reusing it for underwriting is a new purpose, not a query. Erasure constrains evidence: a record designed to be tamper-evident is a record designed to resist exactly the operation a data subject is entitled to demand. The contradiction is real. It has an answer. The answer costs a key-management estate, not a policy exception.

## Decision

Derive every requirement from a named obligation, never from a vendor control catalogue.

The move that follows is to derive every requirement from an obligation, never from a vendor's control catalogue. The catalogue route is attractive, and it is what a competent, time-poor team will choose: it is fast, the labels are ones an auditor recognises, and it produces a mapping matrix in two weeks rather than two months. It loses on one point. A control catalogue is a set of answers to questions somebody else was asked. Mapping an obligation onto it produces controls that satisfy the citation and stop nothing. That is worse than having no control, because the gap is now documented as closed. The slower route costs about 15 engineer-days plus the risk function's attention. Every requirement then carries an argument somebody can contest. That is slower in the design review and cheaper in the audit.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-04]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Map obligations onto a vendor catalogue for speed and auditor-familiar labels.**

A competent architect reaches for this under time pressure: Map obligations onto a vendor catalogue for speed and auditor-familiar labels. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Where a mechanism exists only because of an obligation, say so in the same sentence. Price it as compliance cost. Do not dress it as security. Evidence retention is the clean example. Operationally, 90 d covers every incident investigation anyone at Borealis has run. The obligation implies years. The difference is a storage line of roughly €5,000 a year at current volumes, which is nothing, plus the cost of showing that a hash chain written in 2026 still verifies in 2031 under a key rotation regime nobody has exercised. That second cost is not nothing. It belongs in the operational budget, not the security one.

## Reopen when

A regulation is shown to require a named control rather than evidence of an outcome.
