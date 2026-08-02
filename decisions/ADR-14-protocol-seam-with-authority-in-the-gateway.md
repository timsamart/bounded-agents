# ADR-14. Protocol seam with authority in the gateway {#adr-14}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.4-the-seam.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Adopt the external tool protocol as the seam; keep authority in the gateway.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-14]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Proprietary internal calling convention, or waiting for the protocol to grow authority semantics.

## Reopen when

Protocol gains native per-call authority the gateway can verify without re-deriving.
