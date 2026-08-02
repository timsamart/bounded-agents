# ADR-11. Allow-list of typed operations {#adr-11}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.2-the-envelope.md`

## Context

The catalogue is an allow-list of typed operations. An operation that is not registered, typed and named is not callable. The platform has no generic escape hatch through which an unregistered effect can be reached.

## Decision

Allow-list callable operations; refuse anything undeclared.

The deny-list is the alternative and it deserves its strongest form, because it is what most estates run and it is not stupid. It scales with what you have learned. It never blocks a delivery. It concentrates security attention on the operations that actually frightened somebody. It loses on one property: its completeness depends on having enumerated what an adversary will think of, and the tool catalogue grows faster than the list of things anyone has thought of. An allow-list is wrong in the direction that produces a refusal and a ticket. A deny-list is wrong in the direction that produces an effect and an incident review.

## Consequences

The uncomfortable consequence is worth stating rather than burying. A new operation cannot be used on the day it ships. It has to be registered, typed, assigned a side-effect class, and admitted to a tier before any envelope can contain it. Until then a developer who built it in the morning cannot call it in the afternoon. That is a real tax on delivery. It is paid by the people whose goodwill the platform depends on. The answer to it is not a story about how security is everyone's responsibility. The answer is chapter 17, which is about making that interval short enough that nobody looks for a way around it.

Markers `[ADR-11]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Deny-list frightening operations while permitting the rest.**

Typing is the half of that decision which does the quiet work. An operation carries a declared shape for its arguments. That is what allows the tier to cap an adjustment at €5,000 rather than making a binary decision about whether posting adjustments is permitted at all. Without types, every ceiling collapses into a yes or a no, and yes is the only answer that lets the work proceed.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Untyped effect paths become dominant above the reversibility line.
