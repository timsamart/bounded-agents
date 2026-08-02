# ADR-26. Five stop mechanisms {#adr-26}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/3.4-stopping-it.md`

## Context

There is a second thing no switch undoes, and it is quieter. A stop leaves the organisation in a state where the agent is not running. That is a state somebody has to decide to leave. The exit authority is a named person and the entry authority is not the same person, which is chapter 14's machinery reused rather than rebuilt.

## Decision

Design five distinct stop mechanisms; if underfunded, build the two widest and leave the residual visible.

Five mechanisms is five things to build, own, document, and drill. The temptation to build one is a resourcing argument dressed as a design argument. Naming it correctly is most of the answer: an organisation that cannot fund five stop mechanisms has a budget position, which is respectable and arguable, and not an architecture in which one switch is sufficient. The honest form of that position is to build the two with the widest coverage per unit of effort – halting a run and revoking an authority – write the interval column for the other three as absent, and let the residual be visible to whoever signs the risk acceptance.

## Consequences

The item most likely to be underestimated is not engineering at all. Five switches means five named owners. Each is a person who is still at the company next year, has the credential, has pulled the thing at least once, and can be reached at 03:00. At an annual turnover of 15%, the probability that all five are still in post twelve months from now is about 44%. The more likely state of the world is that at least one switch has no owner. The second most likely is that nobody has noticed. This is an attrition problem wearing an architecture problem's clothes. The only mechanism that addresses it is the one thing an architecture document can do about staffing: make each owner a named row rather than a team, put the date of their last execution beside their name, and let the blank date be the alarm.

Markers `[ADR-26]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Treat a single kill switch as sufficient architecture.**

Priced properly, what you are buying is five runbooks and four drills a year each, which is 20 executions a year. At Borealis they run as one drill morning a quarter, two engineers, roughly half a day including the write-up, so about 8 engineer-days a year plus the initial cost of five runbooks nobody enjoys writing. The runs consumed are real runs and the drill is executed in production, because a drill against a staging run measures a staging system, which is the whole content of the last row of Table 15.1. There is no measurable latency cost: the revocation-state check is already inside chapter 13's 20–40 ms at p99, and this chapter adds a tighter staleness budget on one input rather than a new call on the path.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

An incident requires a sixth distinct stop the five did not cover.
