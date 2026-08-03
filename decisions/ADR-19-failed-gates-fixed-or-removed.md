# ADR-19. Failed gates fixed or removed {#adr-19}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.5-approval-and-effect-integrity.md`

## Context

The distribution of time to decision, never its mean. A mean of 45 s can be a room full of careful reviewers, or a mass at 3 s with a thin tail at 4 min. Those are two behaviours wearing one number. The approval rate per gate, read against its own history: a gate that has refused nothing in 60 days is either protecting a population of proposals that are all correct, which is possible and worth knowing, or it has stopped being a decision. And whether the detail view was ever opened, which is the cheapest of the three and the most damning. A gate approved 900 times with the diff expanded twice is not a gate that needs improving.

## Decision

A human gate that fails its measurement is fixed or removed with tier demotion; keeping a known-failing gate is not an option.

A gate that fails its measurement is fixed or it is removed. When it is removed, the action is demoted to a tier that does not call for it. There is no third option in which the gate stays and its failure is known. That option is the one most organisations choose. It survives because it is comfortable: the gate is in the control register, it was described to a supervisor in a sentence still true in form, and taking it out means a conversation with the person who asked for it. Keeping it is cheap on the day and costs the safety case its integrity. The organisation is then carrying a control whose failure rate it has measured and not acted on, at exactly the point where it decided proof was owed to somebody else. It also moves the accountability onto whoever is clicking, for behaviour the system produced in them.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-19]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Leave a failing gate in place because it looks good in the control register.**

Demotion is a real loss. Pretending otherwise would be dishonest. An action below the reversibility line carries a lower cap, or becomes unavailable to unattended runs, or returns to the queue a person works directly. Somebody's throughput falls, usually the team whose delivery target depended on the automation. That argument is the honest version of one you were previously having with the record. The alternative is a control load-bearing in a document and absent in operation. The first person to find the difference will do so under conditions you did not choose. The conformance test for I5 is mechanical – a call whose payload is altered after approval is refused at execution – and it says nothing about whether anybody read the card. That is why the measurement sits beside the test rather than inside it.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Every remaining gate is unread for a quarter with no safe demotion path.
