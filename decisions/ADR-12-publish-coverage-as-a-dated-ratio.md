# ADR-12. Publish coverage as a dated ratio {#adr-12}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/1.4-solution-strategy.md`, `chapters/2.3-complete-mediation.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Publish mediated-path coverage as a dated ratio; separate discovery ownership from closure ownership.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-12]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Assert complete mediation with an adjective and no denominator.

## Reopen when

Discovery finds a path class mediation cannot cover without a different primitive.
