# ADR-23. Fail closed on evidence {#adr-23}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.4-solution-strategy.md`, `chapters/2.7-evidence.md`, `chapters/3.3-failure-postures.md`

**In plain terms:** If evidence cannot be written, refuse the effect - every tier, no busy-hour carve-out.

## Context

Best-effort logging preserves availability and loses the claim for every unrecorded irreversible act.

## Decision

If evidence cannot write, no effects. Every tier. Every dependency.

## Why not the alternative

**Rejected:** Best-effort logging or an availability exception for peak hours.

An hour of unrecorded irreversible effects is not recoverable. A stopped queue is.

## What changes if you follow this

Evidence-store availability becomes part of agent availability. Adversaries will notice. Accept that.

## Cost

Coupled availability; storage line item for high-volume agents.

## Reopen when

An availability regime forbids fail-closed on evidence and leadership accepts the residual.
