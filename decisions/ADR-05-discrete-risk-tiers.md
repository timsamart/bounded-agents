# ADR-05. Discrete risk tiers {#adr-05}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/1.2-constraints.md`

## Context

The failure mode of scoring is specific. An agent scoring 6.8 against a threshold of 7.0 produces a conversation about the 0.2. A competent person under delivery pressure can always find 0.2, because the inputs to the score are estimates and the estimates carry ranges. Nobody involved is behaving badly. The arithmetic offers a lever, and levers get pulled. A discrete boundary offers no lever of that kind. Whether an operation can be undone by one person in ten minutes is a question about the operation. A spreadsheet cannot move it.

Risk tiers are discrete. The boundary that matters most is reversibility. A continuous score invites a negotiation at the boundary. A tier invites an argument about which tier. That is a better argument to have in front of an auditor, and a better one to lose.

## Decision

Use discrete risk tiers; assign gap cases to the higher tier.

The cost of tiers is expressiveness, and it is paid by the agents that fall between them. An agent whose risk profile sits genuinely in the gap is assigned the higher tier and carries controls heavier than its own assessment would have chosen. Our judgement is that this is the right trade, and here is the cost of being wrong: at Borealis roughly 15% of agent versions ended up one step above where their owners would have placed them. Over-control is not free. A team that finds the sanctioned path disproportionate to their risk goes around it, and coverage falls without anyone filing a ticket. If the tier definitions are drawn badly, that is the number that moves first.

## Consequences

The inventory has five columns. The column that does the work is the last one: Constraint, class, source with a named owner, negotiable, and what changes if it moves. Teams reliably fill the first four and leave the fifth blank. That turns an instrument back into documentation. A row without a consequence has not been thought about and cannot be prioritised against anything. A blank template, with the three class tests printed beside it, is in Appendix E.

Markers `[ADR-05]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Use continuous risk scores as the primary scheme.**

A competent architect reaches for this under time pressure: Use continuous risk scores as the primary scheme. It is familiar, often already funded, and easy to defend in a review that never asks what happens when the optimistic assumption fails. It loses here because the safety claim would then rest on a quantity the organisation does not control, or on an unbounded object.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Continuous scores become a supervisory expectation discrete tiers cannot map.
