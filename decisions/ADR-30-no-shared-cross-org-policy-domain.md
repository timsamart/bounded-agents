# ADR-30. No shared cross-org policy domain {#adr-30}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/4.2-across-the-boundary.md`

**In plain terms:** Across organisations, use bilateral checkable claims - not one shared policy domain or shared broker TCB.

## Context

Shared domains make Parts II - III easy and concentrate secrets and shared incident appetite you may not want.

## Decision

Keep the organisational boundary. Use verifiable credentials, checkable claims, and contracts. List what remains unbuildable.

## Why not the alternative

**Rejected:** Dissolve into one policy domain or a federated broker both sides trust with full envelope semantics.

You inherit another organisation's failure modes and politics.

## What changes if you follow this

Narrower claims; visible unbuildable list (Appendix B). Honesty over portable fantasy.

## Cost

Contract and credential operations cost; less engineering fantasy cost.

## Reopen when

A counterparty demands a shared policy domain this model cannot satisfy.
