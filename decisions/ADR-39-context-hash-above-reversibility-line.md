# ADR-39. Context hash above reversibility line {#adr-39}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.7-evidence.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Require a hash of the full assembled context above the reversibility line; references suffice below.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-39]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Always store full context, or never commit context content.

## Reopen when

Reconstruction obligations require full context retention above what hashing provides.
