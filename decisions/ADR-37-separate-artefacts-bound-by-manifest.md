# ADR-37. Separate artefacts bound by manifest {#adr-37}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/3.1-agent-manifest.md`

## Context

Three mechanisms already assume that composition exists as a nameable thing. Chapter 6 derives a run's authority from a declared need that somebody wrote, reviewed and keeps true. It treats that need as a static field of a signed artefact, not a computation. Chapter 8 pins and signs tool manifests in an internal registry so a server cannot rewrite its own description under a running estate. Chapter 15 quarantines a version. Each reaches for a different half of the same object. None defines it. That is how a document can govern what an agent does at runtime and say nothing about how an agent comes to exist.

The gap is not inside any of the three. It is in the join. The moment somebody asks what combination was in force, the gap opens. A prompt revision on Monday, a policy bundle on Wednesday, and a tool manifest on Thursday produce Friday's behaviour. Each part has a history. The composition has none. The composition is what ran.

## Decision

Keep owned artefacts separate and bind them with a signed manifest.

The alternative is worth arguing. Put instructions, policy and tool bindings in one repository. Deploy them as a unit. One atomic diff. One review. A competent architect would choose it. On integrity grounds it is stronger: there is no join to get wrong. It loses on the thing that decides whether a control survives contact with the organisation. It forces a claims specialist editing a sentence of guidance into a deployment pipeline they cannot use. The observable result is not better review. It is a shadow copy of the text somewhere the pipeline cannot see. The manifest keeps each artefact where its owner can reach it. The binding between them is the security object. That is a weaker guarantee honestly held, rather than a stronger one that quietly stops being true in month four.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-37]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Force instructions, policy, and tool bindings into one atomic monorepo deploy unit.**

A competent architect reaches for this under time pressure: Force instructions, policy, and tool bindings into one atomic monorepo deploy unit. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Cost is stated in the arguing chapter. This record does not invent a figure the spine does not price.

## Reopen when

A deployment model that cannot join separately owned artefacts becomes mandatory.
