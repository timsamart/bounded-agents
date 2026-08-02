# ADR-16. Pinned signed registry, no runtime discovery {#adr-16}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.4-the-seam.md`, `chapters/3.1-agent-manifest.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Remove runtime discovery; pin-and-sign from an internal registry; pin agent↔tool bindings by digest.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-16]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Runtime discovery from external registries; pointer-based tool references.

## Reopen when

External registries offer pin-and-sign semantics the internal registry monopolises.
