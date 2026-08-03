# ADR-31. Standing mandate for unattended runs {#adr-31}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

**In plain terms:** Overnight runs resolve the principal chain to a signed standing mandate (who, task class, ceiling, expiry) - not to a naked service account.

## Context

Service identities have no human entitlements story. Team queues have no recognisable principal.

## Decision

Unattended principal chain resolves to a signed standing mandate.

## Why not the alternative

**Rejected:** Fall back to a service identity or an undifferentiated team queue.

Intersection with reach becomes fiction; accountability dissolves.

## What changes if you follow this

Mandate is an upper bound; attenuation still applies. Expiry and recertification required.

## Cost

Mandate lifecycle operations.

## Reopen when

Unattended work outgrows what a mandate can honestly express.
