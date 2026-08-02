# ADR-19. Failed gates fixed or removed {#adr-19}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.5-approval-and-effect-integrity.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

A human gate that fails its measurement is fixed or removed with tier demotion; keeping a known-failing gate is not an option.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-19]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Leave a failing gate in place because it looks good in the control register.

## Reopen when

Every remaining gate is unread for a quarter with no safe demotion path.
