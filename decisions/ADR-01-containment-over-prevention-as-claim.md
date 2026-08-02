# ADR-01. Containment over prevention-as-claim {#adr-01}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/1.1-introduction.md`, `chapters/1.4-solution-strategy.md`

## Context

Borealis Mutual held its post-incident review on 2026-03-12, 11 days after a claim document containing an instruction in a free-text note caused `claims-triage` to attempt an adjustment posting against a claim it had never been asked to touch. The attempt was caught by a reconciliation report the following morning, not by the classifier, which had scored the note below threshold. The review was competent and it was fast: 11 action items, owners against all of them, dates against nine. Two of the 11 were the wrong kind of item. One raised the classifier threshold. One added four paragraphs to the system prompt instructing the agent to disregard instructions found inside claim documents.

## Decision

Prefer containment bounds the organisation sets over prevention rates an adversary selects.

Notice what the claim does *not* say. Nothing about the agent behaving well. Nothing about the model being trustworthy. Nothing about perfect prevention. Everything in this document follows one preference: prevention has a miss rate we do not control; containment has a bound we do.

Nobody in that room was wrong about the value of a better prompt. They were wrong about which column of the slide it belonged in. That is a documentation error with a specific consequence: a false-negative rate the adversary selects, presented as though it were a design parameter the organisation selected. The two hygiene items belonged under *reduces frequency*, where they are honest and useful. The nine containment items belonged under *bounds the consequence*, where they can be tested. This is the whole of the decision: keep the filter, keep the prompt, and keep them out of the column that carries the claim. The bound has to hold on the run where the filter was wrong.

## Consequences

The honest limit of the preference is worth stating in the same breath. Containment's bound is only as good as the enumeration behind it and the coverage fraction underneath it. Both of those are quantities the organisation has to measure and keep measuring. That is a materially better position than a rate somebody else controls. It is a position with maintenance, not a position with a guarantee.

Markers `[ADR-01]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Treat filter/prompt false-negative rate as a design parameter in the safety claim.**

A competent architect reaches for this under time pressure: Treat filter/prompt false-negative rate as a design parameter in the safety claim. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Neither was a bad thing to do. The threshold change plausibly stops the next copy of this attack. The prompt change costs almost nothing. The problem appeared three weeks later, in the assurance pack that went to the risk committee, where both items were listed in the controls column alongside the other nine. In that column they carry a claim neither can support. The threshold change had an operational tail: `claims-triage` handles about 4,000 runs a day; the tightened threshold held roughly 3% for human review; by the sixth week a queue of about 120 runs a day was being cleared in batches by people who had stopped reading them individually.

## Reopen when

Prevention shows measured FN rate of zero against adaptive adversaries.
