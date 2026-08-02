# ADR-39. Context hash above reversibility line {#adr-39}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/2.7-evidence.md`

## Context

The stream has a stable schema because chapter 8 established that every call at the seam is an evidence event. That is why this chapter can discuss integrity properties rather than re-derive the seam. Approval records are evidence events and inherit everything here without a second construction. That is chapter 9's business. Evidence also chains across composed runs by parent identifier, and it is one of only two things that compose at all.

The fourth question is the expensive one. The resolution is deliberately weaker than a reader would prefer. What the platform knew is mostly what it retrieved. Retrieved content lives in memory, which chapter 10 establishes as mutable by design: items are corrected, superseded and forgotten as normal operation. So the record carries a retrieval reference and a content hash rather than the content. Copying retrieved content into the evidence store would duplicate personal data into the one system built to resist deletion, on every call. The consequence is worth stating rather than discovering: the record is verifiable and not always reconstructible. If the claim note was corrected in September, the hash no longer matches. What you learn eighteen months later is that the item changed, not what it said at the time.

## Decision

Require a hash of the full assembled context above the reversibility line; references suffice below.

Above the reversibility line the record additionally carries a hash of the full assembled context. Below it, references alone are enough. The reason for the split is that the assembled context is the largest object in the system, the most sensitive object in the system and the most useful object in an incident, all three at once. The balance between those three changes when the effect at the end of the call cannot be undone. Notice what a hash does and does not buy. This is where the design would be misread: it commits, it does not preserve. You cannot reconstruct a context from its digest. You can prove whether a context somebody produces later is the one the model actually saw. That turns an argument about reassembly into an arithmetic check and costs deletability nothing. The price is not storage, since a digest is 32 bytes. It is canonical serialisation: the hash requires a deterministic byte representation of prompt template, retrieved items, tool descriptions and ordering. That representation breaks quietly whenever a template is reformatted or a provider changes how it renders a message. Somebody owns that canonicalisation. From the day it drifts, every hash after the drift verifies against nothing.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-39]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Always store full context, or never commit context content.**

Effects are evidence and model reasoning is not. The reason is structural rather than sceptical. Every entry in the chain commits to bytes that existed and can be recomputed by anyone holding the bytes. A model's stated rationale is a pre-image of nothing: no artefact it commits to, no recomputation that checks it, and no obligation on the model to have described its own computation rather than produced a plausible account of one. Re-running the same prompt against the same pinned version yields different text, persuasive both times. The platform can record the rationale, labelled non-evidential and outside the chain, because it genuinely helps a responder at 03:00 form a hypothesis. It is also the most dangerous artefact in the file at a hearing, because it is the most readable thing there and the least verifiable. The record answers what was done and under what authority. It does not answer why in the sense a person means by why.

## Cost

The letter that arrives on 2028-01-19 concerns `CLM-2026-448120` and one run, `run_01J8F3K2QW7XN4ZB9V6HRTMD5C`. Borealis Mutual returns the chain segment for that run: 63 events, sequence-contiguous, verified against the checkpoint published the following morning. Inside it sit the envelope with its three derivation inputs, four policy decisions, Marta's approval record with the hash of the adjustment payload, and eleven retrieval references with their content hashes. Two of the eleven no longer match, because the claim note was corrected on 2026-09-08. The reply says so in one sentence and gives the correction's own reference. What Borealis does not send is any account of why the model proposed €4,180 rather than €2,000, because nothing in the file would survive being called evidence. Three months earlier, on 2027-11-03, an unrelated erasure request had arrived from a claimant whose personal data appeared in the content records of 214 evidence events across 37 runs. The data protection team identified one subject key from a query built when the platform shipped, and destroyed it with a witnessed record. The nightly verification on 2027-11-04 passed. The 214 events are still there, still in sequence, still hashed into their neighbours, and the content behind them is unreadable for good.

## Reopen when

Reconstruction obligations require full context retention above what hashing provides.
