# ADR-04. Obligation-derived requirements {#adr-04}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/1.2-constraints.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Derive every requirement from a named obligation, never from a vendor control catalogue.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-04]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Map obligations onto a vendor catalogue for speed and auditor-familiar labels.

## Reopen when

A regulation is shown to require a named control rather than evidence of an outcome.
