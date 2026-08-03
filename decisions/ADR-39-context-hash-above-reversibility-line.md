# ADR-39. Context hash above reversibility line {#adr-39}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.7-evidence.md`

**In plain terms:** For irreversible effects, evidence includes a hash of the assembled context. Below that line, references can suffice.

## Context

Always storing full context is expensive. Never committing context makes reconstruction theatre.

## Decision

Require a content hash of the full assembled context above the reversibility line; references suffice below.

## Why not the alternative

**Rejected:** Always store full context, or never commit context content.

All-or-nothing misses the reversibility distinction the rest of the design uses.

## What changes if you follow this

Canonical serialisation ownership required so hashes are stable.

## Cost

Storage and CPU for hashing above the line.

## Reopen when

Reconstruction obligations require full context retention beyond hashing.
