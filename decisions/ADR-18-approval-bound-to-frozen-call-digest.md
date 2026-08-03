# ADR-18. Approval bound to frozen call digest {#adr-18}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.5-approval-and-effect-integrity.md`

**In plain terms:** Humans approve a frozen call artefact. Execution checks the digest. A regenerated call voids the approval.

## Context

Approving a rendered summary and letting orchestration produce the call later makes "approved" name a description, not bytes.

## Decision

Bind approval to a frozen call via digest comparison at execution.

## Why not the alternative

**Rejected:** Approve a summary or UI view and allow the system to build the call afterwards.

Seen-versus-done divergence becomes inexpressible eighteen months later.

## What changes if you follow this

Approval UX must show the frozen artefact (effect class, irreversibility, diff, budget) - not the prompt or the model's story about itself.

## Cost

Engineering for hash binding and UI that can display it.

## Reopen when

An approval UX that cannot display a frozen artefact becomes mandatory somewhere.
