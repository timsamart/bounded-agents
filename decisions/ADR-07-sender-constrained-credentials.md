# ADR-07. Sender-constrained credentials {#adr-07}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

**In plain terms:** A stolen run token must not be usable from another machine. Bind the credential to the workload's key.

## Context

Bearer tokens stolen from agent or CI contexts can be replayed immediately. Short TTL alone does not stop same-second reuse.

## Decision

Require holder-of-key proof (sender constraint) for run credentials.

## Why not the alternative

**Rejected:** Rely on short-lived bearer tokens alone.

Theft-to-use can be faster than expiry. Without proof-of-possession, presentation anywhere succeeds.

## What changes if you follow this

Every workload instance needs key material, rotation, and revocation. Mesh estates already have most of this; others buy an operations skill.

## Cost

Ongoing key-management cost for every runtime that holds a run credential.

## Reopen when

Bearer-only becomes unacceptable to every system of record in the estate - or proof-of-possession becomes universal free infrastructure.
