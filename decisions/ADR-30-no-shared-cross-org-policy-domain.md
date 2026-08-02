# ADR-30. No shared cross-org policy domain {#adr-30}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/4.2-across-the-boundary.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Keep the organisational boundary; use bilateral credentials, checkable claims, and contractual attestations.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-30]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Dissolve the boundary into one shared policy domain or a federated broker both sides trust.

## Reopen when

A counterparty demands a shared policy domain the attenuated-credential model cannot satisfy.
