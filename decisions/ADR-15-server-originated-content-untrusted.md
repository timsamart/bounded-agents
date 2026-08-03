# ADR-15. Server-originated content untrusted {#adr-15}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/2.4-the-seam.md`

## Context

Three answers arrive before this one. All three have shipped in real systems. Each relocates the problem to a place with a worse property. The reasons they lose are specific.

*Put the policy in the server.* The argument for it is the classical one and it is strong: enforcement belongs at the point of effect, and the server is both where the effect happens and the only component that understands its own domain well enough to write a good rule. In a monolith this is correct. Here it places policy in the component that is most numerous, least trusted, most often written by a third party, and most likely to be updated by someone with no view of your tiers. Coverage stops being a property of the platform and becomes the number of servers you audited, which falls every time a team adds a tool. And the envelope would be re-interpreted inside software the platform does not operate, which puts the authority model on the far side of the boundary it exists to defend.

## Decision

Treat tool descriptions, resources, and prompt templates as untrusted data with provenance requirements.

*Trust the tool description.* The argument for it is that a description is registered metadata a human added to your own catalogue, and treating your own catalogue as hostile is exhausting. It loses on two counts. A description reaches the model with exactly the directness of a user instruction, so manipulating the text is an instruction to an agent that holds real authority, and published research has demonstrated this class of attack against real deployments. And a description has a supply chain behind it: a vendor, a package registry, an update mechanism, a maintainer account, and a change window between onboarding and the call in which nobody was watching. Server-originated content is therefore untrusted data with a provenance requirement. That covers descriptions, resources and prompt templates alike, because all three arrive from the same place and reach the same context.

## Consequences

The rejected alternative is not available as a silent default in conforming implementations. Markers in the spine resolve here; reopening needs an issue and an edition note.

Markers `[ADR-15]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Treat registered tool descriptions as trusted configuration.**

*Use the protocol's own authorisation story as the authority model.* This one deserves care, because the specification is not deficient and the temptation to misread it is strong. It answers whether a client may connect to a server, and it answers that properly, on well-understood foundations. The question here is a different one: whether this run, under this envelope, may perform this operation on this object at this moment, with this budget remaining and this principal behind it. Connection authorisation is a component of that answer rather than a substitute for it. A design that adopted the first as the second would not be inheriting a weak answer. It would be inheriting a correct answer to a question nobody in an incident review is going to ask.

## Cost

Cost is stated in the arguing chapter. This record does not invent a figure the spine does not price.

## Reopen when

Protocol carries signed provenance for every server-originated payload as a required field.
