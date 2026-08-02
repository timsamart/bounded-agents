# ADR-03. Frozen trusted computing base {#adr-03}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/1.3-context-and-scope.md`

## Context

Keeping the set at three components costs capability. The cost is felt as refusals. Every convenience that would like to live inside the boundary is turned away: a context assembler, a cache, a summariser that would save a round trip. Each of those, admitted, becomes a component whose compromise breaks the bound. The compensation for keeping them out is a slower path. The published price of the boundary sitting in front of everything is 20–40 ms at p99 on every mediated call. What it buys is a set of components small enough that the people who own them have read all of it. That is the only condition under which a claim about them is checkable.

The trusted computing base is three components and the key material beneath them. The list does not grow: the gateway that mediates every tool call, the path that decides whether a call is permitted, and the path that records evidence. Chapter 1 drew that boundary. Here it becomes vocabulary. The commitment attached to it is that no mechanism later in this document adds a member to the set.

## Decision

Freeze the TCB at gateway, decision path, evidence path, and keys; refuse growth.

The reason for the size is a fifty-year-old argument rather than a modern one: every access goes through one mediating point, and that point is small enough to be reasoned about in its entirety. Everything else sits outside and is assumed hostile, including the parts that feel like ours – the orchestration framework, the agent's own process, the tool implementations, the model. There is no component anywhere in the design whose job is to decide whether the model is behaving. The absence is load-bearing.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-03]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Expand the TCB to include the agent, model, framework, or tools.**

A competent architect reaches for this under time pressure: Expand the TCB to include the agent, model, framework, or tools. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

A competent design review shows the TCB must grow and remain defensible.
