# ADR-01. Containment over prevention-as-claim {#adr-01}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/1.1-introduction.md`, `chapters/1.4-solution-strategy.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Prefer containment bounds the organisation sets over prevention rates an adversary selects.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-01]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Treat filter/prompt false-negative rate as a design parameter in the safety claim.

## Reopen when

Prevention shows measured FN rate of zero against adaptive adversaries.
