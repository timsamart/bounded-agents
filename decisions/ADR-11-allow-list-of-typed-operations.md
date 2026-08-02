# ADR-11. Allow-list of typed operations {#adr-11}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.2-the-envelope.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Allow-list callable operations; refuse anything undeclared.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-11]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Deny-list frightening operations while permitting the rest.

## Reopen when

Untyped effect paths become dominant above the reversibility line.
