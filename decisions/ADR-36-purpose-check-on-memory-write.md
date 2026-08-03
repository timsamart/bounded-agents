# ADR-36. Purpose check on memory write {#adr-36}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.6-data-retrieval-memory.md`

**In plain terms:** Block forbidden combinations when memory is written - not later when someone reads it.

## Context

Read-time checks miss what already became a stored fact.

## Decision

Run purpose and composition checks on the memory write path for cross-context items.

## Why not the alternative

**Rejected:** Catch forbidden composites only at read or audit time.

Once stored, the composite is a durable leak and a GDPR purpose problem.

## What changes if you follow this

Write path gets stricter; some "clever" memory features die.

## Cost

Enforcement cost on writes.

## Reopen when

Product value requires write-time combinations the purpose model cannot express.
