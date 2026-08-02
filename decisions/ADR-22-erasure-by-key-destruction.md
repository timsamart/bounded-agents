# ADR-22. Erasure by key destruction {#adr-22}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.7-evidence.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Split evidence into chained metadata and encrypted content; erase by destroying the per-subject key.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-22]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Redact in place, encrypt the whole chain, or delete bytes only.

## Reopen when

Erasure-by-key-destruction fails a supervisory interpretation the organisation must meet.
