# ADR-27. Unexercised controls are absent {#adr-27}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/1.4-solution-strategy.md`, `chapters/3.4-stopping-it.md`, `chapters/3.5-decay.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

A control or switch unexercised against a live run in a quarter is absent; the drill calendar is load-bearing architecture.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-27]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Treat drills as optional SRE hygiene demoted out of architecture.

## Reopen when

An auditor rejects exercised-set evidence and the organisation cannot meet the alternative.
