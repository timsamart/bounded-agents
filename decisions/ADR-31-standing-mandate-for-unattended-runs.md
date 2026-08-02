# ADR-31. Standing mandate for unattended runs {#adr-31}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

## Context

Both come with the same underlying bill: key material per workload and the machinery behind it. Every workload instance holds a private key it does not share. That means issuance at start-up, an authority that issues, a rotation schedule, a revocation path, and somebody who notices when an expiry approaches. An organisation running a mesh with short-lived workload certificates has most of this and is configuring a capability it already owns. An organisation with neither competence is buying one. Capabilities arrive on a hiring and training schedule rather than an engineering one. That is slower, less predictable, and more likely to be the reason the programme slips than any line of code in this document. Price it as a quarter of someone's role indefinitely rather than as a sprint, and decide it on the estate you have.

## Decision

Resolve the unattended principal chain to a signed standing mandate (human, task class, ceiling, expiry).

A signed standing mandate occupies the principal chain. It is a durable delegation artefact naming a human principal, a task class, a ceiling, and an expiry, signed by that human. The unattended run's second chain resolves to it rather than to a live session. Attenuation survives because the mandate is itself an upper bound: it cannot carry more than its signer could reach on the day they signed it, and the authority in force for a run derived against it cannot exceed the mandate. The rejected alternatives are the two the field actually uses. Falling back to a service identity is the arrangement this whole chapter exists to abolish. Resolving the chain to a team or a queue produces a principal with no entitlements a data owner would recognise, which quietly removes the input that makes entitlement-scoped retrieval mean anything.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-31]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Fall back to a service identity or a team/queue with no recognisable entitlements.**

Read that against the attended case and the mechanism is the same mechanism. The chain is present in both. The credential has the same shape in both. The only difference is what occupies the principal slot and how far in the past the human decision was made. That last part is the price, and it is not small. A mandate is a new artefact class with a signing ceremony, a register, and an owner. Its expiry is a new thing somebody watches, because a mandate that lapses at 02:59 is an outage and a mandate that gets renewed by reflex every six months is the standing service account you removed, wearing a signature. And the approval is one step further from the action than anyone would like: Marta authorised a class of work in April and the adjustment happened in July. That is a real weakening of the second chain. It is worth saying out loud rather than describing as delegation and moving on.

## Cost

The Borealis nightly triage run starts at 03:00 with nobody present. Its second chain resolves to `mandate:claims-nightly`, signed by Marta on 2026-04-14 with an expiry of 2026-10-14, naming a task class of overnight claim triage and a ceiling below the reversibility line. The mandate was signed once, in a fifteen-minute meeting with the data owner and a record of it. It has been the second chain for roughly ninety runs a night since. Each of those runs gets its own credential and its own `sub`. Each carries `mandate:claims-nightly` in the `act` slot where an attended run carries Marta, so the record answers on whose authority the run acted without inventing a session she was never in. At 03:12 the run reaches a claim that needs a payment adjustment of €4,180, which is above the mandate's ceiling. The run does not widen, does not fall back, and does not wake anybody. It records the refusal against the run, marks the claim for the attended queue, and continues with the next one. Marta finds it at 08:00 with the reasoning already written down. Under the service identity this replaced, the same adjustment would have been inside authority, and the record afterwards would have said only that `claims-triage` did it.

## Reopen when

Unattended operation outgrows the standing-mandate artefact.
