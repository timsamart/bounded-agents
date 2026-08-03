# ADR-02. Run as unit of authority {#adr-02}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.3-context-and-scope.md`, `chapters/1.4-solution-strategy.md`

## Context

Somebody in a design review asks what happens if the agent is compromised. The next four minutes are spent discovering that nobody in the room means the same thing by *it*. One person means the deployment. One means the conversation open on their screen. One means the service principal in the identity provider. All three are real objects. All three are called the agent. Only one of them can be switched off in a way that stops anything.

The unit that matters is the run: bounded in time, acting for exactly one principal, carrying one envelope, one budget and one evidence stream, and ending. The agent is what you deploy. The run is what acts, and it is the only thing in the system you can revoke. Attach authority, budget, evidence and revocation to the run and a set of questions that were previously matters of opinion acquire answers.

## Decision

Make the run the unit of authority, budget, evidence, and revocation; derive at start and expire with the run.

Four questions decide most of these design reviews. What exactly are we revoking? What could it reach at 09:07? Who authorised this? How much had it spent before anyone looked? Asked about an agent, every one of them has an answer of the form *it depends when you ask*. That is not an answer. It is a description of an unbounded object. Asked about `run_01J8DXQ3`, each has one answer. It is the same answer at 09:07 and at the audit eighteen months later. It does not require anyone to read the orchestration code to reconstruct it. This is the chapter's single decision and everything after it is consequence.

Authority attached to an agent has no number attached to it. Authority attached to a run does. Chapter 3 fixed the run as the unit of authority, budget, evidence, and revocation, with terminal states. That makes the question *what exactly are we revoking* answerable for the first time. The move here is the consequence: authority is derived at the start of each run and expires with it, rather than being inherited from whatever the agent's service principal has accumulated.

## Consequences

A run is one bounded execution of one agent on behalf of one principal. It has five properties. Each one exists because a later mechanism needs something specific to attach to: someone to act for, a thing to bound, a thing to count, a thing to chain evidence to, and a thing to take away.

The budget rides on the same boundary. It is counted in tool calls, because tool calls are what produce effects. Tokens are telemetry, useful for cost control and useless as a bound on damage. Chapter 5 derives the identity binding and the standing mandate that makes an unattended run possible without a live human. Chapter 6 derives the envelope arithmetic and attenuation. None of the underlying position is new: the capability tradition in security engineering has argued for decades that authority travels best as a designated, attenuable object rather than as an ambient property of whoever is holding an identity.

Markers `[ADR-02]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Inherit authority from an accumulated agent service principal.**

The derivation is an intersection rather than an inheritance. What the agent declared it needs, what the human principal can actually reach in the systems of record, and what the risk tier permits, with the smallest of the three governing. For one claim triage at Borealis Mutual that comes out at four typed operations against one claim. That is a set a reviewer can read in ten seconds, disagree with, and narrow. The comparison that matters is not against a perfect design but against the honest alternative: a service account whose permission set was last reviewed at onboarding and is now the union of everything anyone has asked for since.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Long-running agents force a unit larger than a run without a security-parameter duration.
