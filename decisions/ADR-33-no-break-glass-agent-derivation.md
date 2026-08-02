# ADR-33. No break-glass agent derivation {#adr-33}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** `chapters/3.3-failure-postures.md`, `chapters/3.4-stopping-it.md`

## Context

On 2026-03-02 the overnight reconciliation report showed an adjustment posting against a claim `claims-triage` had never been asked to touch. At 09:14 the platform lead decided to stop the agent. The stop had three homes by then: a section in the architecture document, control `OPS-4` in the register, and a paragraph in a filing submitted to the supervisor the previous autumn describing the organisation's ability to halt automated processing. None of the three had ever been executed against a production run. The runbook named a script. The script authenticated with a credential the on-call engineer's group had lost read access to in a January reorganisation. At 09:19, with 34 runs active, the engineer scaled the runtime deployment to zero, which stopped the pods and not the work: the batch scheduler had six new runs derived by 09:21, each against a mandate nobody had touched. The last run stopped at 09:25, when a second engineer, woken up, revoked the mandate. That is 11 min, most of it spent discovering that the fast thing available was the wrong thing to do.

## Decision

Emergencies are human-direct on the system of record with human credentials; no break-glass agent run.

There is no break-glass run. The emergency path is a human acting directly against the system of record, with their own credentials, under whatever four-eyes procedure the organisation already runs. The platform's obligation is that this path exists, is roughly as fast as the agent path, and is recorded. The alternative that was seriously considered is a break-glass run derived under an emergency mandate with a hard expiry and two signatures. It is not a strawman: attenuation survives it, because the mandate is itself a bound, and every enterprise already has the organisational muscle for exactly that ceremony. It was rejected on what it creates rather than on what it permits. A legitimate, high-authority, seldom-exercised derivation path is the most attractive object in the estate to a patient person. It is attractive precisely because it is the one path whose use under pressure nobody questions. Kai does not need to defeat the envelope if the organisation has built a supported way to be handed a wider one.

## Consequences

A switch that has not been executed against a live run in the last quarter does not exist. Not degraded. Not probably fine. Not *documented*. It does not exist. The register carries it as absent. The interval column beside it is blank rather than optimistic. The calendar that makes this survivable, and the argument that generalises it from stop mechanisms to every control in this document, belong to chapter 16, which owns them.

Markers `[ADR-33]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Issue an emergency mandate or widened envelope for the agent under dual control.**

A reviewer will ask for the exception. It is always the same one: a case where acting without a record beats not acting, usually life safety, usually posed with an example nobody wants to argue against. The honest answer is a boundary rather than a carve-out. This document's scope is enterprise agents holding real authority under a burden of proof owed to a third party, which chapter 1 fixed with three conditions. A system in the path of a person's safety is a different system with a different hazard analysis, a different safety case, a different regulator, and a different answer to what unrecorded action costs. It is not built by taking this architecture and cutting a hole in its evidence row. If that is the system you are building, the exception you are looking for is not here, and the safety case you need was never the one written in this document.

## Cost

The cost is a manual path somebody maintains and exercises. That is another row on the drill calendar and a genuinely unpopular one, because the manual path is slow, is used twice a year, and is the first thing to rot when the system of record changes its screens. An emergency path that has not been walked in a year is not an emergency path. It is a paragraph. And the reason this belongs in a chapter about outages rather than in the chapter about stopping things is that *what no switch can undo* and *what no envelope permits* are one conversation approached from opposite ends. The switches themselves are chapter 15's material. The speed limit is this chapter's.

## Reopen when

A class of incident cannot be contained without an agent-held emergency path.
