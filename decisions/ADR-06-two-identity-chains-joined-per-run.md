# ADR-06. Two identity chains joined per run {#adr-06}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.1-identity-and-binding.md`

## Context

Collapse the principal into the workload, and the agent runs under its own service identity. The audit question survives in a weak form, because you can tell that `claims-triage` did something. The entitlement question dies, because the run now acts under the union of everything that service account can reach, for every task the agent has ever been given. Retrieval under that identity returns documents Marta could not open. A hostile model gets that union in one step. The blast radius of a single injected paragraph becomes the standing authority of the busiest identity in the estate.

Collapse the workload into the principal, and the agent acts with Marta's tokens. Now the entitlement question answers cleanly, which is why the arrangement is tempting. The audit question dies. The evidence record says Marta posted the adjustment. She did not. She was in a meeting. There is no field in which the difference can be expressed. Incident response cannot separate what Marta did from what was done in her name. The leaver process now has to reason about agents. You have handed a process that takes instruction from adversarial text a credential that a person is accountable for. At 03:00 the arrangement does not even have a fiction to offer, because there is no Marta to impersonate.

## Decision

Keep principal and workload chains distinct; join them once per run in the credential.

Joined rather than collapsed, both questions stay answerable. The standard vocabulary already exists for saying so. The credential's `sub` names the run. The `act` claim carries the acting workload and the principal it acts for. The pair is what the gateway reasons about. Keeping the chains distinct is also what makes the authority arithmetic possible at all, because an intersection needs two inputs. The credential carries a reference to the envelope in force, not the derivation that produced it. That derivation is chapter 6's business rather than this chapter's.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-06]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Collapse both questions into one agent identity.**

The run credential is a short-lived, audience-restricted, sender-constrained token. It names a run, names both chains, points at an envelope, and is good at exactly one place. It is not a downstream credential and cannot be spent at a tool. The agent never holds one of those, because the gateway holds them and spends them on the run's behalf. That is a property of the seam rather than an argument to make here. What matters at this altitude is the contribution to the second invariant. A credential presented from a workload other than the one it was issued to is refused. The refusal is written to the evidence path as an event against the run, not dropped as a 401 in an access log nobody reads.

## Cost

Cost is stated in the arguing chapter. This record does not invent a figure the spine does not price.

## Reopen when

Unattended operation outgrows the standing-mandate artefact.
