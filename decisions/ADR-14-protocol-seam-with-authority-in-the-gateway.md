# ADR-14. Protocol seam with authority in the gateway {#adr-14}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.4-the-seam.md`

**In plain terms:** Speak the shared tool protocol at the seam, but keep credentials and authority decisions in the platform gateway - never in the agent.

## Context

The gateway is a protocol server to the agent and a protocol client to real tools. It is the only component on the path that holds a credential. A proprietary calling convention buys semantics early and costs every integration. Waiting for the protocol to grow authority semantics waits on someone else's roadmap.

## Decision

Adopt the external tool protocol (e.g. MCP) as the seam. Keep authority in the gateway: translate, inject, refuse, forward.

## Why not the alternative

**Rejected:** Proprietary internal calling convention - or wait until the protocol carries full authority semantics.

Proprietary locks you in. Waiting leaves mediation unmeasurable until a date you do not own.

## What changes if you follow this

Extra hop on every tool call; registry and pinning required (ADR-16). Agent never sees a credential.

## Cost

Single-digit milliseconds if co-located; worse if not. Additive to the decision path.

## Reopen when

Protocol gains native per-call authority the gateway can verify without re-deriving.
