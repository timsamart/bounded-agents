# ADR-15. Server-originated content untrusted {#adr-15}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.4-the-seam.md`

**In plain terms:** Tool descriptions, resources, and prompt templates are untrusted data with provenance - never a source of authority.

## Context

Registered catalogue text feels like "our metadata." It reaches the model like an instruction and has a supply chain behind it.

## Decision

Treat all server-originated content as untrusted data requiring provenance. Never derive authority from it.

## Why not the alternative

**Rejected:** Trust registered tool descriptions as safe configuration.

Description injection and malicious servers are demonstrated classes of attack. Trusting the text is trusting the attacker's channel.

## What changes if you follow this

Onboarding records hashes; runs re-verify. Authority stays in envelope and policy.

## Cost

Provenance and pin discipline on every tool artefact.

## Reopen when

Protocol carries signed provenance for every server-originated payload as a required field.
