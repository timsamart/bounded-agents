# ADR-06. Two identity chains joined per run {#adr-06}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Keep principal and workload chains distinct; join them once per run in the credential.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-06]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Collapse both questions into one agent identity.

## Reopen when

Unattended operation outgrows the standing-mandate artefact.
