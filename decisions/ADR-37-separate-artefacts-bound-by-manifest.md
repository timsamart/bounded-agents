# ADR-37. Separate artefacts bound by manifest {#adr-37}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/3.1-agent-manifest.md`

**In plain terms:** Instructions, policy, and tools stay separately owned. A signed manifest binds the versions that may run together.

## Context

Monorepo atomic deploy is stronger on join integrity and forces specialists into pipelines they will bypass with shadow text.

## Decision

Keep owned artefacts separate; bind them with a signed manifest.

## Why not the alternative

**Rejected:** Force instructions, policy, and tool bindings into one atomic repository deploy unit.

Shadow instructions appear when claims people cannot reach the only pipeline.

## What changes if you follow this

Manifest is the security object. Promotion gates apply to the binding.

## Cost

Join complexity; human-reachable ownership.

## Reopen when

A deployment model that cannot join separately owned artefacts becomes mandatory.
