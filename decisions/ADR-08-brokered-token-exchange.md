# ADR-08. Brokered token exchange {#adr-08}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Broker and join run credentials in one place rather than issue direct per-tool grants.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-08]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Direct per-tool grants from the existing identity provider.

## Reopen when

The IdP gains first-class per-tool, audience-bound grants that remove the broker.
