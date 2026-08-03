# ADR-09. Envelope as three-way intersection {#adr-09}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.2-the-envelope.md`

**In plain terms:** A run may only do what the task needs AND the human can reach AND the risk tier allows - all three.

## Context

Three parties decide what a run may do. The agent team declares need; the identity estate supplies the human's reach; risk supplies the tier ceiling. Need alone is self-grant. Reach alone inherits a human's whole working life. Ceiling alone permits the worst case.

## Decision

Derive the envelope as declared need AND principal reach AND tier ceiling at run start.

## Why not the alternative

**Rejected:** Treat any single input as sufficient authority.

Each alone recreates a familiar enterprise failure mode with a new blast radius.

## What changes if you follow this

Three owners will disagree; that disagreement is the control. Derivation removes operations without a meeting.

## Cost

Manifests must declare need; identity and risk must supply the other two on time at run start.

## Reopen when

Production measurements show one input always dominates so the other two are decorative.
