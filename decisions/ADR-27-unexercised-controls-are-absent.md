# ADR-27. Unexercised controls are absent {#adr-27}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.4-solution-strategy.md`, `chapters/3.4-stopping-it.md`, `chapters/3.5-decay.md`

## Context

The other direction was exercised on 2026-07-06 at 22:40, when a storm claim needed an emergency payment and no envelope in force permitted one at that hour. There is no emergency run, no widened envelope and no break-glass derivation, which chapter 14 settled rather than this one. Marta signed into Guidewire and posted the adjustment herself. The platform's contribution was that the movement did not surface as an unexplained effect: the manual path writes into the same evidence chain, marked as a human action on the system of record with no run behind it, and the reconciliation job matched it without anyone being asked to explain it. The agent was not widened, that night or afterwards.

Every control in the previous four moves degrades, most of them silently. The difference between an architecture and a diagram of one is whether that degradation has a budget line. The coverage fraction falls when a team ships an integration in a hurry. The envelope widens one declared-need review at a time. The policy bundle accumulates rules that have not fired in 90 days and nobody can now delete safely. The stop mechanism works, presumably, since the last time anyone ran it.

## Decision

A control or switch unexercised against a live run in a quarter is absent; the drill calendar is load-bearing architecture.

A reviewer will say that this is operational discipline rather than architecture and belongs in Part III with the other things an SRE inherits. The objection is fair. The answer is narrow: move five is the only move that decides whether the other four are still true in month fourteen. Demoting it to an operations chapter is precisely the mistake the field keeps making. The unit that makes it tractable is the signed agent manifest of chapter 12, because recertification needs an object it can diff. Chapter 16 derives the measurements and the calendar that use it. Chapter 17 prices the sanctioned path against the shortcut in minutes, which is the only unit that decides adoption. A control that has not been exercised in a quarter is not a control you have. It is a control you had. The distinction is invisible from the inside until the quarter you need it.

## Consequences

What it costs: roughly one engineer-day a week, permanently. It is the first line cut in a bad quarter because it is the only one whose removal produces no immediate symptom. You are buying an alarm on a slope, and slopes are politically difficult to fund.

The rule is severe on purpose, and it is severe in one specific direction. It costs nothing to write a stop procedure and it costs a morning to run one. An organisation with a procedure and no execution has bought the appearance of the capability for an afternoon of writing and has declined the drill morning four times a year that the capability itself costs. That is not a moral failing. It is an accurate response to the incentives. The only correction that works is to make the absence visible in the same place the capability would have been.

Markers `[ADR-27]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Treat drills as optional SRE hygiene demoted out of architecture.**

That distinction also bounds the cost rather than waving it away, which is the honest half of the argument. The obligation attaches to the mechanisms with no organic exercise. That set is enumerable rather than open-ended: the five stop mechanisms, deliberate entry into degraded mode, end-to-end verification of the evidence chain, the manual path on the system of record that exists because there is no agent break-glass, and the refusal paths the canary suite covers. Everything the estate exercises on its own keeps the ordinary evidence it already has. Nothing here asks for a drill of the payroll run.

## Cost

The objection to that is strong and comes from experienced people, so take it at full strength. Documentation plus competent staff is how every other operational capability in the enterprise is evidenced. Nobody executes the disaster-recovery plan quarterly to prove it exists. Nobody rehearses the certificate renewal. An organisation that made quarterly execution the price of counting a capability would spend more on exercises than on the operations they protect. Regulated organisations already generate more evidence than anyone reads. One more standing obligation is a real cost argued by people who have watched several such obligations decay into a signature on a form.

## Reopen when

An auditor rejects exercised-set evidence and the organisation cannot meet the alternative.
