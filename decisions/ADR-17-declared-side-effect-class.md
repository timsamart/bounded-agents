# ADR-17. Declared side-effect class {#adr-17}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.4-the-seam.md`

## Context

Server manifests are pinned and signed, fetched from an internal registry, and never discovered at runtime. Description digests are recorded at onboarding and re-verified before the description reaches a model's context. A side-effect class is declared by a person and stored against the operation.

Runtime discovery is the feature developers most like about the protocol. This design removes it. That is worth stating plainly, because a reader who discovers it during implementation will discount everything else here. Discovery is the mechanism by which the set of callable operations changes without anyone deciding to change it. An allow-list whose contents move between two runs is a list with an adversary on the write path. What replaces it is dull: a registry entry per server, a signature from a publisher the organisation can name, a pinned version, and a promotion step when the version moves. The registry is also where the second coverage dimension lives, because a server with no entry is a server nobody chose.

## Decision

Require a human-declared side-effect class (and idempotency) for operations above the reversibility line.

The side-effect class is the field people argue about. The argument is always that the name says what the operation does, so why make somebody type it. Because the name is written by whoever wrote the tool, and there are tools called `get-quote` that send an email. Inference from names fails in the direction that produces an effect rather than a refusal, and it fails silently, which is the pairing this document treats as disqualifying. The declared class carries an idempotency contract with it, because the gateway retries and because a run that dies mid-call leaves an unknown somebody resolves at 03:00. Nothing above the reversibility line executes without a declared class. The declaration is made by a human at onboarding who has to think for a minute about whether the effect can be undone. That minute is the cheapest control in this chapter and the one most likely to be handed to whoever is free.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-17]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Infer side-effect class from operation names.**

The argument here reaches exactly as far as the typed call. Two edges are worth naming rather than discovering.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Protocol standardises side-effect class and idempotency on the call itself.
