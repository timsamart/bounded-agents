# ADR-07. Sender-constrained credentials {#adr-07}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Require holder-of-key / confirmation (sender constraint) for run credentials.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-07]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Rely on short-lived bearer tokens alone.

## Reopen when

Bearer-only becomes unacceptable to every system of record in the estate.
