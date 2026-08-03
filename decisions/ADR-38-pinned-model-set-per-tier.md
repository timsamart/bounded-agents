# ADR-38. Pinned model set per tier {#adr-38}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/3.1-agent-manifest.md`

## Context

The set of models a version is permitted to run on is a property of the tier. It is carried in the envelope alongside everything else the run is bounded by. A route to a model outside the set terminates the run rather than completing it on the substitute. Model routing is an authority decision wearing an optimisation's clothes.

## Decision

Pin the allowed model set per tier in the manifest; treat routing and fallback as a safety-case change.

A router selects between models per call, automatically, under load, optimising for latency and price. A platform team changes it without a security review because on its face it alters nothing about what the agent is allowed to do. It touches neither the envelope nor the declared need. It changes which model reads the attacker-shaped document. A model with a different refusal profile is a different safety case. A fallback route during a vendor outage is a silent amendment to that case, made by an availability mechanism, in precisely the degraded conditions where nobody is reading change tickets. A route to a differently located model can move inference across a boundary the organisation has made residency claims about without a single data control firing, because nothing was retrieved. And a cheaper model at the same tier invalidates the evaluation that authorised the version, because the number was measured against the frontier model the tier permits and the run is executing on something else.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-38]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Allow unreviewed automatic per-call model routing under load, price, or latency.**

Terminating the run is fail-closed and it costs availability at the worst moment. During a vendor incident, an estate that terminates stops doing work while one that degrades carries on with a substitute model and, in most cases, gets away with it. That trade belongs in the fail-posture matrix signed before the outage rather than in a decision taken during one. The row it occupies is model unavailability, which chapter 14 decides in advance like every other dependency. The reason to prefer termination is not that degradation is always wrong. It is that a degraded run is indistinguishable in the evidence record from a normal one unless model identity is part of what the run is bounded by. A safety case that cannot see its own substrate is not one.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Vendor platforms make pinned sets impossible while still meeting residency obligations.
