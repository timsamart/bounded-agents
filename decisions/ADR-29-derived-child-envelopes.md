# ADR-29. Derived child envelopes {#adr-29}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/4.1-composition.md`

**In plain terms:** Sub-agents get their own attenuated envelope. Do not pass the parent's credentials or approvals.

## Context

Framework default is to hand the child the parent's client. Under hostile input that is widening with extra steps.

## Decision

Derive attenuated child envelopes from the parent envelope and the manifest's delegation graph. Do not propagate parent credentials or approvals.

## Why not the alternative

**Rejected:** Pass parent authority and approval to spawned sub-agents.

Child calls become indistinguishable from parent calls with full reach.

## What changes if you follow this

Dynamic free-form composition dies; static delegation graphs live. Shared budget counters across the tree.

## Cost

Less "magic" composition; more predictable blast radius.

## Reopen when

Dynamic sub-agent composition becomes mandatory and a static graph cannot express it.
