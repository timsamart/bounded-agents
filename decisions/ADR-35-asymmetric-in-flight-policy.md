# ADR-35. Asymmetric in-flight policy {#adr-35}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.2-the-envelope.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Narrowing mid-run takes effect on the next call; widening applies only to the next derivation.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-35]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Let the envelope track live policy in both directions.

## Reopen when

A legitimate mid-run ceiling raise cannot wait for a new run.
