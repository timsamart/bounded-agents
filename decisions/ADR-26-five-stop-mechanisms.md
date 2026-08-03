# ADR-26. Five stop mechanisms {#adr-26}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/3.4-stopping-it.md`

**In plain terms:** Design five different stops (halt run, revoke authority, disable operation, quarantine version, cut egress). One "kill switch" is not enough.

## Context

Singular kill switches are either too narrow or so wide they take the business offline with the adversary.

## Decision

Design five distinct stop mechanisms. If underfunded, build the two widest and leave the residual visible.

## Why not the alternative

**Rejected:** Treat a single kill switch as sufficient architecture.

The stop you need at 03:00 depends on what you just learned. One reach profile cannot cover five situations.

## What changes if you follow this

Build, own, and drill five paths. Underfund honestly rather than pretend.

## Cost

Engineering and drill calendar cost - non-optional for the claim's third leg.

## Reopen when

An incident requires a sixth distinct stop the five did not cover.
