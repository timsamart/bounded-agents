# ADR-38. Pinned model set per tier {#adr-38}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/3.1-agent-manifest.md`

**In plain terms:** The manifest lists which models may run for this tier. Auto-routing to a cheaper or other-region model is a safety-case change.

## Context

Routers change refusal profile and residency without touching the envelope.

## Decision

Pin the allowed model set per tier in the manifest. Treat routing and fallback as a safety-case change.

## Why not the alternative

**Rejected:** Allow unreviewed automatic per-call model routing under load, price, or latency.

Different model, different residual. Silently.

## What changes if you follow this

Deprecation calendars become standing jobs. Fallbacks need review.

## Cost

Less automatic cost optimisation; more honest evaluation.

## Reopen when

Vendor platforms make pinned sets impossible while still meeting residency obligations.
