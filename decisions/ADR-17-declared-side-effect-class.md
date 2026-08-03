# ADR-17. Declared side-effect class {#adr-17}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.4-the-seam.md`

**In plain terms:** A human declares whether an operation is reversible, irreversible, etc. Do not infer that from the name.

## Context

`get-quote` that emails is a real failure mode. Names lie; declarations can be reviewed.

## Decision

Require a human-declared side-effect class (and idempotency where needed) for operations above the reversibility line.

## Why not the alternative

**Rejected:** Infer side-effect class from operation names.

Inference fails toward effects. The approval card and stop logic then lie.

## What changes if you follow this

One minute of thought at onboarding becomes the cheapest control in the chain.

## Cost

Onboarding ceremony per operation.

## Reopen when

Protocol standardises side-effect class and idempotency on the call itself.
