# ADR-38. Pinned model set per tier {#adr-38}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/3.1-agent-manifest.md`

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

Pin the allowed model set per tier in the manifest; treat routing and fallback as a safety-case change.

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[ADR-38]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- Allow unreviewed automatic per-call model routing under load, price, or latency.

## Reopen when

Vendor platforms make pinned sets impossible while still meeting residency obligations.
