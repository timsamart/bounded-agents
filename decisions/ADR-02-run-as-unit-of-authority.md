# ADR-02. Run as unit of authority {#adr-02}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/1.3-context-and-scope.md`, `chapters/1.4-solution-strategy.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Make the run the unit of authority, budget, evidence, and revocation; derive at start and expire with the run.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-02]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Inherit authority from an accumulated agent service principal.

## Reopen when

Long-running agents force a unit larger than a run without a security-parameter duration.
