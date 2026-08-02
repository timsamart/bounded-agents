# ADR-34. Temporary deny-only fast path {#adr-34}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/3.2-hot-path.md`

## Context

The single-artefact answers both fail, in opposite directions, for the same reason. Put the bundle under full change control and the fastest available way to narrow authority during an incident is slower than the incident: the review, the pipeline, the staged rollout, and somewhere in the middle a run that is still permitted to do the thing you decided at 14:02 it may not do. Take the change control away and there is now an unreviewed path to widening authority in the system. That defeats the entire apparatus more cheaply than any attack in the threat model. Kai's best move against a platform like this was never an exploit. It was a plausible policy change on a Friday.

Policy ships as two things. A slow-moving bundle with the full change control a code release gets. And a fast deny list with its own signing authority and a mandatory expiry.

## Decision

Allow a temporary deny-only incident path with hard expiry; never a permit-fast path.

What makes the asymmetry safe is that the fast artefact is one-directional and temporary. The deny list can refuse and cannot permit. The worst outcome of an unreviewed entry is a self-inflicted refusal somebody notices within minutes, rather than an authority granted at speed and read by nobody. Every entry carries an expiry, capped at 24 h at Borealis. After that it is gone unless a human renews it or the change has landed in the bundle through the ordinary path. An incident-time narrowing that cannot become permanent policy is a narrowing nobody has to remember to review. The price is a second policy system with a second signing authority, a second audit trail, and a precedence rule between them. That is a real operational cost rather than a rounding error.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-34]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Add a fast permit path or make incident narrowing permanent without review.**

Conflicts resolve deny-overrides, with an explicit precedence order for the exceptional case. Evaluation is bounded by construction in the policy language rather than by a timeout.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Incident response requires a permanent narrowing that cannot wait for the ordinary bundle path.
