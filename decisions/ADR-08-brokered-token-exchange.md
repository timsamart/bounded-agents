# ADR-08. Brokered token exchange {#adr-08}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

## Context

One broker performs the exchange, rather than each tool's identity provider issuing the run a grant of its own. The broker takes the workload's proof and the principal's assertion, checks both, and mints the run credential. Token exchange is a settled mechanism with a specification behind it. This is an ordinary use of it rather than an invention.

## Decision

Broker and join run credentials in one place rather than issue direct per-tool grants.

The alternative deserves its strongest statement, because it is what a competent estate already does. Direct per-tool grants add no component. They introduce no new failure domain on the run-start path. They reuse the issuance machinery your identity provider has been operating correctly for years. It loses on arithmetic rather than on principle. The number of grant relationships grows with agents multiplied by tools rather than with either. Every one of those issuers has to learn what a run is and how to audience-bind to a gateway it does not own. Revocation acquires as many places to be got right as there are issuers. The property that makes the joined chains worth anything is that they are joined in one place, verifiably, once per run. A design with n issuers has n opportunities to join them differently.

## Consequences

A component on the run-start path is also a component whose failure stops runs from starting, and possibly stops runs already in flight from renewing. What happens to each of those populations when the broker is unavailable is a posture that gets declared and signed before the outage rather than improvised during it. Naming that obligation is this chapter's job. Answering it belongs to the fail-posture matrix in Part III. Answering it twice would give the reader two versions to choose between at the worst possible moment.

Markers `[ADR-08]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Direct per-tool grants from the existing identity provider.**

The cost lands on the run-start path, which is a path that did not previously exist. Our budget for a broker in the same cluster as the orchestrator is single-digit milliseconds at p99. For one reached across a region boundary or fronted by a vault in another data centre it is closer to 40–120 ms at p99. These are design budgets rather than measurements. The difference between them is a placement decision somebody makes early and lives with. Be precise about how that number relates to the one chapter 1 published. The 20–40 ms at p99 quoted there is per mediated call. The broker's cost is paid once per run. A run making 30 tool calls amortises it to something invisible. A run making one call pays all of it. That is why run-start latency is measured and reported separately rather than folded into a per-call average that will flatter it.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

The IdP gains first-class per-tool, audience-bound grants that remove the broker.
