# ADR-37. Separate artefacts bound by manifest {#adr-37}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/3.1-agent-manifest.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Keep owned artefacts separate and bind them with a signed manifest.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-37]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Force instructions, policy, and tool bindings into one atomic monorepo deploy unit.

## Reopen when

A deployment model that cannot join separately owned artefacts becomes mandatory.
