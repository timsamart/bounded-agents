# ADR-20. Entitlement-resolved retrieval {#adr-20}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.6-data-retrieval-memory.md`

**In plain terms:** Search only what the principal may see. Do not retrieve-then-filter - filters leak via counts, ranks, and timing.

## Context

Post-filters still score forbidden partitions. Side channels remain.

## Decision

Resolve entitlements inside retrieval against a partitioned index so unreachable items never score, count, or rank.

## Why not the alternative

**Rejected:** Retrieve first, filter afterwards.

Leakage is structural, not a bug in the filter expression.

## What changes if you follow this

Index design and query planning get harder. Confidentiality gets real.

## Cost

Engineering cost in the retrieval path; worth it above sensitive tiers.

## Reopen when

A data owner requires retrieval under a non-principal identity the model cannot avoid.
