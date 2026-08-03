# ADR-07. Sender-constrained credentials {#adr-07}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

## Context

Certificate-bound credentials where your estate already terminates TLS with client certificates and the tools are internal. Application-layer proof of possession where the caller is HTTP-only, where there is no certificate lifecycle to attach the binding to, or where the call crosses an organisational boundary. That is a condition rather than a preference. A document that stated a favourite here would be describing its author's last estate rather than your current one.

Mutual TLS with certificate-bound tokens puts the binding in the transport. The credential carries a thumbprint of the client certificate. The gateway compares it against the certificate on the connection that presented it. It costs nothing per request once the connection is established, which matters for a chatty run. It is close to free for an organisation already running a service mesh that issues workload certificates. DPoP puts the binding in the application layer. The client signs a proof for each request with a key whose thumbprint the credential carries. The gateway verifies the signature, the target, and the freshness. It survives intermediaries that terminate TLS. It works where you have no certificate authority to lean on. It costs a signature per request plus clock and replay discipline you now own.

## Decision

Require holder-of-key / confirmation (sender constraint) for run credentials.

Both come with the same underlying bill: key material per workload and the machinery behind it. Every workload instance holds a private key it does not share. That means issuance at start-up, an authority that issues, a rotation schedule, a revocation path, and somebody who notices when an expiry approaches. An organisation running a mesh with short-lived workload certificates has most of this and is configuring a capability it already owns. An organisation with neither competence is buying one. Capabilities arrive on a hiring and training schedule rather than an engineering one. That is slower, less predictable, and more likely to be the reason the programme slips than any line of code in this document. Price it as a quarter of someone's role indefinitely rather than as a sprint, and decide it on the estate you have.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-07]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Rely on short-lived bearer tokens alone.**

A signed standing mandate occupies the principal chain. It is a durable delegation artefact naming a human principal, a task class, a ceiling, and an expiry, signed by that human. The unattended run's second chain resolves to it rather than to a live session. Attenuation survives because the mandate is itself an upper bound: it cannot carry more than its signer could reach on the day they signed it, and the authority in force for a run derived against it cannot exceed the mandate. The rejected alternatives are the two the field actually uses. Falling back to a service identity is the arrangement this whole chapter exists to abolish. Resolving the chain to a team or a queue produces a principal with no entitlements a data owner would recognise, which quietly removes the input that makes entitlement-scoped retrieval mean anything.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Bearer-only becomes unacceptable to every system of record in the estate.
