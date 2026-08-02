# ADR-24. Embedded policy evaluation {#adr-24}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/3.2-hot-path.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Evaluate policy locally from signed, versioned bundles on the hot path.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-24]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Synchronous remote call to a central decision service on every call.

## Reopen when

Measured p99 of embedded evaluation exceeds a staleness budget a central call can meet.
