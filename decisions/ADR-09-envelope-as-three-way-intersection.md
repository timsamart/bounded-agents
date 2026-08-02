# ADR-09. Envelope as three-way intersection {#adr-09}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.2-the-envelope.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Derive the envelope as declared need ∩ principal reach ∩ tier ceiling at run start.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-09]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Treat any single input as sufficient authority.

## Reopen when

Production measurements show one input dominates the intersection.
