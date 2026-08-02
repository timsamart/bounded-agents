# ADR-20. Entitlement-resolved retrieval {#adr-20}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.6-data-retrieval-memory.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Resolve entitlements inside retrieval against a partitioned index so unreachable items never score, count, or rank.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-20]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Retrieve first, filter afterwards.

## Reopen when

A data owner requires retrieval under a non-principal identity the model cannot avoid.
