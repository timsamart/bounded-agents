# ADR-02. Run as unit of authority {#adr-02}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.3-context-and-scope.md`, `chapters/1.4-solution-strategy.md`

**In plain terms:** Authority, budget, evidence, and revocation attach to one run ID - not to the agent's standing identity forever.

## Context

Asked about an agent, "what are we revoking?" and "how much had it spent?" have answers of the form "it depends when you ask." Asked about a run ID, each question has one durable answer.

## Decision

Make the run the unit of authority, budget, evidence, and revocation. Derive at start; expire with the run.

## Why not the alternative

**Rejected:** Let the agent's service principal accumulate standing authority that every run inherits.

A standing identity has no natural end, no per-task budget, and no single evidence chain. Revocation becomes ambiguous and blast radius grows with every new permission.

## What changes if you follow this

Every mechanism later in the document can name one object. Incident review reconstructs one run. Unattended work still needs a principal story (see ADR-31), but the unit of effect remains the run.

## Cost

Run-start derivation and per-run credentials add a hop and an artefact. You pay that to make revocation and audit answerable.

## Reopen when

Long-running agents force a unit larger than a run without a security-parameter duration you can defend.
