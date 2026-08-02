# ADR-05. Discrete risk tiers {#adr-05}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/1.2-constraints.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Use discrete risk tiers; assign gap cases to the higher tier.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-05]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Use continuous risk scores as the primary scheme.

## Reopen when

Continuous scores become a supervisory expectation discrete tiers cannot map.
