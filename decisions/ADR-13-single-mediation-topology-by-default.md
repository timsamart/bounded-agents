# ADR-13. Single mediation topology by default {#adr-13}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.3-complete-mediation.md`

**In plain terms:** Prefer one mediation gateway topology. Federation relocates difficulty into policy freshness and double-counting.

## Context

Multiple gateways feel organisationally natural. They create signed-bundle lag and coverage sums that disagree.

## Decision

Prefer a single mediation gateway topology. Treat federation as an expensive relocation of difficulty, not the default.

## Why not the alternative

**Rejected:** Federated multi-gateway as the default shape.

Staleness becomes a security parameter in many places at once; coverage becomes a reconciled sum with double-count risk.

## What changes if you follow this

Latency and blast-radius arguments must be met with co-location and clear ownership, not with silent second gateways.

## Cost

Organisations that cannot share a gateway pay in policy distribution (chapter 13).

## Reopen when

Estate shape or protocol forces a different topology with measured benefit.
