# ADR-23. Fail closed on evidence {#adr-23}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.4-solution-strategy.md`, `chapters/2.7-evidence.md`, `chapters/3.3-failure-postures.md`

## Context

Price it in the right budget. Chapter 1's 20–40 ms at p99 is the decision path. That tax lands on every mediated call. This write is additive and lands only on calls that carry an effect, which at Borealis is a low single-digit number per run rather than on every call. Our judgement, and it is judgement rather than measurement, is that a quorum-durable append inside one availability domain belongs in a budget of 5–15 ms at p99, and that a quorum spanning regions moves it to 40–80 ms at p99, which residency requirements sometimes force. An effect-bearing call above the reversibility line therefore sits at 25–55 ms at p99 in the good case. This is the largest latency item in the document after the decision path itself. Volume is not the problem at this scale: 4,000 claims a day and roughly 1,900 runs a night produce a few thousand durable appends across the batch window, about one per second at the peak. The expense is the coupling, not the rate.

## Decision

If evidence cannot write, refuse effects – every tier, every dependency.

What it costs: your effect path is now no more available than your evidence path. This is the trade people try to carve out first, usually as a proposal for best-effort logging with an availability exception for the busy hours. The durable write sits on the critical path and is the remainder of the 20–40 ms. The retention volume for a 4,000-run-a-day agent is a storage line item somebody has to sign. Refusing the carve-out is the one posture in this document that is not negotiable. A platform that can act without recording holds, for the duration of that interval, none of the three claims made in chapter 1.

## Consequences

Every dependency in this system has a defined behaviour when it is unavailable. The only question is whether that behaviour was chosen in a design review or discovered at 03:40 UTC by whoever was on call. Undefined behaviour under partial outage is not an absence of a decision. It is a decision, made by the default in a library. It is usually fail-open, because fail-open is what an availability-minded engineer writes when nobody has told them that this particular call moves money.

Markers `[ADR-23]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Best-effort logging or an availability carve-out for busy hours.**

Ordering is the whole of this move. The evidence record is written and acknowledged before the effect is executed. The absence of a record is then evidence of the absence of an effect, rather than evidence that logging was down. A log is a description of what happened. A precondition is a constraint on what can happen. Only the second survives contact with someone who benefits from the record being incomplete.

## Cost

The matrix is not the deliverable. The signature is. This is the political content of the decision rather than a flourish attached to it. An unsigned matrix is a recommendation from the platform team. A recommendation loses to a phone call from someone whose queue has stopped, every time, and correctly, because nobody in that call has been given the authority to hold the line. A signed row is a decision with a person's name on it, taken with time to think. That changes what happens on the bridge: the conversation moves from *what do we do* to *do we override Marta's June decision*, and those are conversations with different outcomes and different records. The purpose of the whole exercise is to make the decision attributable before it is urgent. Everything else the matrix does is secondary to that. This is also why the signer is the person who owns the consequence of the outage rather than the person who owns the platform, and why a refusal to sign is a useful outcome rather than a failed meeting. A row nobody will sign is a row whose cost the business has not accepted. Finding that out in June is cheap.

## Reopen when

An availability regime forbids fail-closed on evidence and the organisation accepts the trade.
