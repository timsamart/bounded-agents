# ADR-10. Attenuation by construction {#adr-10}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.2-the-envelope.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Make envelope widening unrepresentable; no widen operation exists.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-10]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Enforce non-widening only as a policy-engine rule.

## Reopen when

A legitimate widening case cannot be expressed as a new run.
