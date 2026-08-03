# ADR-06. Two identity chains joined per run {#adr-06}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

**In plain terms:** Keep "who authorised this?" and "which workload is presenting?" as separate chains, joined once at run start.

## Context

Collapsing both into one agent identity makes intersection arithmetic impossible and hides which human or mandate stands behind the run.

## Decision

Keep principal and workload chains distinct. Join them once per run in the credential.

## Why not the alternative

**Rejected:** Collapse both questions into one agent identity.

You can no longer tell whether authority came from a person (or mandate) or from a machine identity with broad reach.

## What changes if you follow this

Credentials carry `sub` (run) and `act` (workload + principal). Envelope derivation reads both. Complexity rises; accountability rises with it.

## Cost

Issuer and broker must understand two chains. See ADR-08.

## Reopen when

Unattended operation outgrows the standing-mandate artefact (ADR-31).
