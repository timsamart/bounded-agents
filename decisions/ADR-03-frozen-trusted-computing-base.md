# ADR-03. Frozen trusted computing base {#adr-03}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.3-context-and-scope.md`

**In plain terms:** Only three things plus keys are trusted: gateway, decision path, evidence path. Everything else - model, agent, tools - sits outside.

## Context

Every new "trusted" component is a place the claim can fail silently. Teams grow the trusted set whenever something is hard to mediate.

## Decision

Freeze the trusted computing base at the gateway, the decision path, the evidence path, and the key material beneath them. Refuse growth without reopening this record.

## Why not the alternative

**Rejected:** Treat the model, framework, tools, or orchestration as part of the trusted computing base.

Those components take attacker-shaped input or change without your version string. Putting them inside the TCB imports their failure modes into the claim.

## What changes if you follow this

Later chapters may not add TCB members by stealth. If a design needs a fourth trusted component, it needs a new decision with an explicit cost.

## Cost

Some features become harder: anything that requires trusting model output for authority is out of scope by construction.

## Reopen when

A competent design review shows the TCB must grow and can still be defended.
