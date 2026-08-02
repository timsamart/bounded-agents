# ADR-32. Recertify ceiling, need, and exercised set {#adr-32}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/3.5-decay.md`

## Context

Recertification produces two reports with two owners. The question an access review is built to ask has no answer in this architecture. The question that does have an answer is one only the platform can answer.

## Decision

Recertify via tier ceiling and declared need plus the platform's exercised-set report.

The data owner recertifies the tier ceiling and the declared need. Both are static artefacts. Both fit on a page. Both ask a question a data owner is competent to judge: is this the work, and is this the reach the work needs. The platform reports the exercised set from last quarter – the list of operations actually called, against which systems, under whose authority. That report is only possible because chapter 11 wrote every effect down before it happened. The two views answer different questions and disagree usefully. The ceiling says what was permitted. The exercised set says what was used. The gap between them is the over-declaration list that keeps the intersection from becoming a constant.

## Consequences

What the identity governance platform can be told is worth stating plainly, because somebody will have to type it into one. It can be told that the agent identity exists, that a named person owns it, that it carries a tier, a declared need, and a ceiling. It can hold those as the static entitlement of record. What it cannot be told is what the identity can reach, because between runs the honest answer is nothing: authority does not exist until a run derives it. A governance tool handed *nothing* records an orphan, or refuses the import, or invents a zero that a reviewer reads as an error. This is a deliberate architectural property colliding with a mandatory, audited process. The collision is far cheaper to prepare for than to discover during an access-review cycle three weeks before an examination. The preparation is one page in the recertification pack: the ceiling as the static figure the tool holds, the exercised set attached as evidence that the static figure overstates reality, and a named person who will say both sentences out loud to an auditor.

Markers `[ADR-32]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Recertify only static entitlement lists and ignore what was exercised.**

The cost is two processes on two calendars. That roughly doubles the load and puts part of it on a team that has never carried a recertification obligation before. It buys what a conventional entitlement review cannot buy at any price: an answer grounded in what happened rather than in what was granted.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

An auditor rejects exercised-set recertification and requires an alternative the org must meet.
