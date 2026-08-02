# ADR-21. Memory as governed primary store {#adr-21}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.6-data-retrieval-memory.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Treat agent memory as a governed primary store with provenance, retention, and scopes.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-21]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Treat framework vector stores as unmanaged caches.

## Reopen when

Memory must be shared across principals to deliver funded product value.
