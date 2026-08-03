# ADR-08. Brokered token exchange {#adr-08}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

**In plain terms:** Mint and join run credentials in one broker, not as a separate grant from every tool's issuer.

## Context

Direct per-tool grants avoid a new component but multiply grant count by agents × tools and force every issuer to learn "run."

## Decision

Broker and join run credentials in one place rather than issue direct per-tool grants.

## Why not the alternative

**Rejected:** Issue direct per-tool grants from the existing identity provider for each tool.

Revocation multiplies, join semantics diverge across issuers, and "what is a run?" leaks into n systems.

## What changes if you follow this

One new component on the run-start path with its own fail posture (chapter 14). One place that understands run semantics.

## Cost

Broker availability and correctness become load-bearing. Price the fail posture before launch.

## Reopen when

The IdP gains first-class per-tool, audience-bound, run-aware grants that remove the broker.
