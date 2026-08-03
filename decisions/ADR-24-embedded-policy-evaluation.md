# ADR-24. Embedded policy evaluation {#adr-24}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/3.2-hot-path.md`

**In plain terms:** Evaluate policy locally from signed, versioned bundles on the hot path - not a remote call on every tool call.

## Context

Central synchronous decision adds network to p99 and correlates outage across every agent.

## Decision

Embed local policy evaluation from signed bundles with a declared staleness budget.

## Why not the alternative

**Rejected:** Remote central decision service call on every call.

Governance outage becomes estate outage; latency budget dies.

## What changes if you follow this

Freshness becomes the security parameter. Stale bundles fail closed (see chapter 13).

## Cost

Bundle distribution and signing; local CPU on the enforcement path.

## Reopen when

Measured p99 of embedded evaluation exceeds a staleness budget a central call can meet.
