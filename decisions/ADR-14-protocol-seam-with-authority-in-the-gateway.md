# ADR-14. Protocol seam with authority in the gateway {#adr-14}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.4-the-seam.md`

## Context

The gateway is a protocol server to the agent and a protocol client to the real servers. It is the only component in the path that holds a credential. The agent never sees one.

## Decision

Adopt the external tool protocol as the seam; keep authority in the gateway.

That is the chapter's entire design content. The fact that it fits in two sentences is a good sign rather than a suspicious one. Economy of mechanism is a fifty-year-old preference for control surfaces small enough to be understood completely. The gateway earns its place in the trusted computing base by refusing work rather than acquiring it. It does not derive the envelope; chapter 6 does that, and the gateway injects what it was given and cannot amend it. It does not decide; the decision path does, and the gateway asks. It does not hold the evidence chain; chapter 11 does, and the gateway blocks on the acknowledgement. What it does is translate, inject, refuse, and forward. The alternatives were a proprietary internal calling convention, which buys authority semantics on day one and costs every integration you will ever write, and waiting for the protocol to grow those semantics itself, which is a plan with a completion date owned by somebody else.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-14]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Proprietary internal calling convention, or waiting for the protocol to grow authority semantics.**

A competent architect reaches for this under time pressure: Proprietary internal calling convention, or waiting for the protocol to grow authority semantics. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Protocol gains native per-call authority the gateway can verify without re-deriving.
