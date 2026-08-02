# ADR-29. Derived child envelopes {#adr-29}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/4.1-composition.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Derive attenuated child envelopes; do not propagate parent credentials or approvals.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-29]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Pass the parent client and authority to spawned sub-agents (framework default).

## Reopen when

Dynamic sub-agent composition becomes mandatory and a static delegation graph cannot express it.
