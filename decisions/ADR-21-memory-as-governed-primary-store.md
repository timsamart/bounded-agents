# ADR-21. Memory as governed primary store {#adr-21}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.6-data-retrieval-memory.md`

**In plain terms:** Agent memory is a governed store with provenance, purpose, and retention - not an unmanaged vector "cache."

## Context

Framework memory accumulates personal data with no ceremony and surfaces in subject-access requests.

## Decision

Treat agent memory as a governed primary store.

## Why not the alternative

**Rejected:** Treat framework vector stores as droppable caches.

Caches that hold personal data are primary stores whether you named them that or not.

## What changes if you follow this

Write-time purpose checks (ADR-36); retention jobs; provenance fields.

## Cost

Platform ownership of memory lifecycle.

## Reopen when

Product value requires memory shared across principals in a way this model forbids.
