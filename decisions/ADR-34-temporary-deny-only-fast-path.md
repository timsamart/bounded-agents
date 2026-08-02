# ADR-34. Temporary deny-only fast path {#adr-34}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/3.2-hot-path.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Allow a temporary deny-only incident path with hard expiry; never a permit-fast path.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-34]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Add a fast permit path or make incident narrowing permanent without review.

## Reopen when

Incident response requires a permanent narrowing that cannot wait for the ordinary bundle path.
