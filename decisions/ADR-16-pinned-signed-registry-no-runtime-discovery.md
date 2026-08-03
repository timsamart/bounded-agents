# ADR-16. Pinned signed registry, no runtime discovery {#adr-16}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.4-the-seam.md`, `chapters/3.1-agent-manifest.md`

**In plain terms:** Tools come from a signed internal registry at pinned versions. Runtime discovery of new servers is off.

## Context

Runtime discovery lets the callable set change without a decision - an allow-list with the adversary on the write path.

## Decision

Remove runtime discovery. Pin-and-sign from an internal registry; pin agent↔tool bindings by digest.

## Why not the alternative

**Rejected:** Discover tools at runtime from external registries; bind by mutable pointers.

Pointers move under you. Digests do not.

## What changes if you follow this

Developers lose the protocol's favourite convenience feature. Say so plainly. Promotion becomes a control.

## Cost

Registry, signing, and onboarding friction - priced against bypass in chapter 17.

## Reopen when

External registries offer pin-and-sign semantics the internal registry monopolises today.
