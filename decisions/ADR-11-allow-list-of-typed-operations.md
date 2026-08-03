# ADR-11. Allow-list of typed operations {#adr-11}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.2-the-envelope.md`

**In plain terms:** Only named, registered operations may run. Everything else is refused.

## Context

Deny-lists grow with fear and never finish. Failure mode is an effect. Allow-lists fail closed.

## Decision

Allow-list callable operations; refuse anything undeclared.

## Why not the alternative

**Rejected:** Deny-list frightening operations and permit the rest by default.

Completeness depends on enumerating adversary ideas while catalogues grow faster than reviews.

## What changes if you follow this

New operations cannot ship the day they are written - they need registration and side-effect class (ADR-17). Chapter 17 is about making that friction small.

## Cost

Onboarding cost per operation; security gain on every unknown call.

## Reopen when

Untyped effect paths become dominant above the reversibility line.
