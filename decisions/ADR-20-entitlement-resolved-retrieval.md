# ADR-20. Entitlement-resolved retrieval {#adr-20}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.6-data-retrieval-memory.md`

## Context

The identity question arrives separately and quietly. An index is built once and read a few million times. The entitlement data lives in a different system owned by a different team. The corpus was assembled by asking what the agent needs to see, rather than what any particular person is allowed to see. So the reader identity ends up being the indexer identity, which is the union of everything the corpus needed. What that produces is not an access violation. No log records one. It produces a run in which Marta asks a reasonable question about a subsidence claim and receives, faithfully summarised and correctly cited, three paragraphs from a document she has never been entitled to open. Across 4,000 claims a day, an agent built this way is the most courteous lateral-movement engine in the building. The courtesy is the problem: everything it does looks like the system working.

Start with what retrieval is for. The mechanism is not in dispute. Grounding a model in retrieved organisational content reduces fabrication, gives the answer a source somebody can open, and turns a general model into one that knows how this insurer handles a subsidence claim. That is why every serious deployment has retrieval in it. A design that made retrieval worse in exchange for a security property would deserve the argument it would get.

## Decision

Resolve entitlements inside retrieval against a partitioned index so unreachable items never score, count, or rank.

The engineering objection to fixing this is serious. Resolving entitlements per query costs latency in a path that was fast. The entitlement service is owned by somebody else. The obvious cheap fix is to retrieve first and filter afterwards. Post-filtering fails on a property that is easy to miss: the filter leaks through everything around the text. Result counts, ranking positions, relevance scores, and the latency difference between a query that matched something and one that did not are all observable from inside the run. A patient questioner can map the shape of a corpus they cannot read. So the decision is that entitlement resolution happens inside retrieval rather than after it, against a partitioned index, with the principal's cohort deciding which partitions are searched at all. An item the principal cannot reach is never scored, never counted, and never contributes to the ranking of the items that are returned.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-20]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Retrieve first, filter afterwards.**

State the evidential position plainly. The position is weaker than the argument. No published work settles entitlement-aware retrieval at enterprise scale. This design is ahead of its literature rather than derived from it Peer-reviewed and industrial write-ups of entitlement-resolved retrieval at enterprise scale are thin; the design here is derived, not surveyed.. This is unsolved.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

A data owner requires retrieval under a non-principal identity the model cannot avoid.
