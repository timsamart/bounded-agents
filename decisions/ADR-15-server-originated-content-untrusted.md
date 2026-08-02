# ADR-15. Server-originated content untrusted {#adr-15}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.4-the-seam.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Treat tool descriptions, resources, and prompt templates as untrusted data with provenance requirements.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-15]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Treat registered tool descriptions as trusted configuration.

## Reopen when

Protocol carries signed provenance for every server-originated payload as a required field.
