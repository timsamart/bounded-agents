# ADR-35. Asymmetric in-flight policy {#adr-35}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.2-the-envelope.md`

## Context

The envelope is an upper bound fixed at derivation, not a cached policy result. Policy is evaluated per call, inside that bound, against the arguments of the call. It can refuse anything the envelope permits.

## Decision

Narrowing mid-run takes effect on the next call; widening applies only to the next derivation.

This is the seam a hostile reviewer finds fastest, so it is worth having the answer before the question. If policy narrows while a run is in flight – a tool is quarantined at 09:11, a counterparty is added to a block list, a value threshold drops – the next call the run makes is evaluated against the new policy and is refused. Narrowing is immediate, because narrowing happens where the decision happens. If policy widens while a run is in flight, nothing happens at all. The run finishes under the ceiling it was born with, and the wider authority becomes available to the next run that derives one. A ceiling that moved during a run would not be a ceiling. An envelope that tracked policy would be a cache with a staleness budget, which would put the authority model in the hot path and make its correctness a property of a distribution mechanism rather than of a derivation.

## Consequences

That is also what the phrase *in force at the moment of the call* is doing in I2. An envelope that has expired is not in force. A revoked envelope is not in force. A call arriving after either is refused on the same code path as a call for an operation that was never in the set.

Markers `[ADR-35]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Let the envelope track live policy in both directions.**

What this concedes is precise, and stating it is cheaper than being caught with it. For the remaining lifetime of a run in flight, the platform is enforcing a ceiling that has been withdrawn. That window has a maximum, and the maximum is the maximum run duration. That is why that parameter is a security parameter and not an operational convenience. Borealis runs T2 work with a 30 min ceiling. Whether 30 min is acceptable is a risk decision, taken with the knowledge that everything derived before the withdrawal keeps its old bound for at most that long. Where 30 min is too long, the answer is not to make the envelope mutable. The answer is revocation, which stops the run rather than editing its authority, and which has its own interval and its own drill.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

A legitimate mid-run ceiling raise cannot wait for a new run.
