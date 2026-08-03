# ADR-10. Attenuation by construction {#adr-10}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.2-the-envelope.md`

**In plain terms:** There is no "widen authority" operation. Child runs can only get less, never more.

## Context

A policy rule "child ≤ parent" is reviewable and still violable by a bug. A widened envelope looks like a working system.

## Decision

Make envelope widening unrepresentable. The interface offers narrowing and revocation only.

## Why not the alternative

**Rejected:** Enforce non-widening only as a policy-engine rule.

Rules fail open into escalation. Absent operations fail into errors.

## What changes if you follow this

Dynamic "just give the child what it needs" composition dies. Spawns go through derivation (ADR-29).

## Cost

Some product fantasies become unexpressible. That is intentional.

## Reopen when

A legitimate widening case cannot be expressed as a new run.
