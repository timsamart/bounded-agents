# ADR-18. Approval bound to frozen call digest {#adr-18}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.5-approval-and-effect-integrity.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Bind approval to a frozen call artefact via digest comparison at execution.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-18]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Approve a rendered summary and let orchestration produce the call later.

## Reopen when

An approval UX that cannot display a frozen artefact becomes mandatory somewhere.
