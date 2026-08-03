# ADR-22. Erasure by key destruction {#adr-22}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.7-evidence.md`

**In plain terms:** Evidence content is encrypted per subject. Erasure destroys the key. The hash chain still verifies; content becomes unreadable.

## Context

Tamper-evident logs fight erasure. Redacting bytes in place fights tamper-evidence.

## Decision

Split chained metadata from encrypted content. Erase by destroying the per-subject key.

## Why not the alternative

**Rejected:** Redact in place, delete bytes only, or encrypt the entire chain as one blob.

In-place redact breaks integrity stories; whole-chain encryption makes selective erasure clumsy or impossible.

## What changes if you follow this

Key-management estate; witnessed destruction; backup/replica regimes in Appendix A.

## Cost

Real key-management cost - the price of both integrity and erasure.

## Reopen when

A supervisory interpretation rejects key destruction as erasure and the organisation must comply another way.
