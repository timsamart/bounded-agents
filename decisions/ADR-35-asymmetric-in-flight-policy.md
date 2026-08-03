# ADR-35. Asymmetric in-flight policy {#adr-35}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.2-the-envelope.md`

**In plain terms:** If policy narrows mid-run, the next call sees it. If policy widens, the current run keeps its birth ceiling.

## Context

An envelope that tracks live policy in both directions is a cache with staleness, not a ceiling.

## Decision

Narrowing mid-run takes effect on the next call. Widening applies only to the next derivation.

## Why not the alternative

**Rejected:** Let the envelope track live policy upward and downward.

Upward tracking destroys the meaning of a ceiling derived at start.

## What changes if you follow this

Runs in flight may finish under a withdrawn ceiling for at most max-run-duration. Revoke if that window is too long.

## Cost

Max run duration becomes a security parameter.

## Reopen when

A legitimate mid-run ceiling raise cannot wait for a new run.
