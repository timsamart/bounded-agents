# ADR-21. Memory as governed primary store {#adr-21}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.6-data-retrieval-memory.md`

## Context

Memory gets a schema, a classification, a retention period, an owner, and provenance on every item. That is the treatment any other store of personal data in the organisation already receives.

## Decision

Treat agent memory as a governed primary store with provenance, retention, and scopes.

The alternative deserves its strongest form. It is what the framework hands you, and it is pleasant to build with. A vector store the orchestration library manages, an append call, a similarity search, and no ceremony at all: the agent remembers things, the demo improves, and nobody spends a sprint on data governance for what is presented as a cache. The trouble is that it is not a cache. A cache can be dropped and rebuilt from an authoritative source. This cannot. It is a primary store. It accumulates content derived from personal data. It has no retention rule. The moment its existence becomes organisationally visible is usually a subject access request that somebody has fifteen days to answer.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-21]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Treat framework vector stores as unmanaged caches.**

The fields that carry the weight are provenance and version. Provenance records the origin of the content, the run and principal that wrote it, the trust level, and the identifiers of the items it was derived from. That is what makes the inheritance rule computable rather than aspirational. Versioning is forced by a decision that belongs to chapter 11: evidence records a retrieval reference and a content hash rather than the content itself. So a memory item that is corrected becomes a new version rather than an edited row, and retrieval returns the version identifier alongside the text. Retention is per item and per classification. It is the field most likely to be set to null in the first bulk migration.

## Cost

Cost is stated in the arguing chapter. This record does not invent a figure the spine does not price.

## Reopen when

Memory must be shared across principals to deliver funded product value.
