# ADR-01. Containment over prevention-as-claim {#adr-01}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.1-introduction.md`, `chapters/1.4-solution-strategy.md`

**In plain terms:** Keep filters and prompts, but do not treat them as the safety claim. The claim is what still holds when the filter misses.

## Context

After a claim-document injection, Borealis's review mixed two kinds of action: raise the classifier threshold and harden the prompt (frequency reducers), with nine items that actually bound what a fooled run can do. Listing both in the same "controls" column makes a miss rate the adversary chooses look like a design parameter the organisation chose.

## Decision

Prefer containment bounds the organisation sets over prevention rates an adversary selects. Keep detection; keep it out of the column that carries the safety claim.

## Why not the alternative

**Rejected:** Put filter or prompt false-negative rate in the safety claim as if it were a controlled design parameter.

A filter can be right most of the time and still fail once. The adversary chooses inputs and can adapt. A rate you do not control cannot be the thing you promise supervisors.

## What changes if you follow this

Hygiene stays funded and honest under "reduces frequency." The claim column only holds bounds you can test: envelope, mediation, evidence, stop. Assurance packs must not list classifiers beside containment as if they did the same job.

## Cost

Better prompts and thresholds are cheap. Measuring and maintaining coverage and enumeration is not. That maintenance is the price of a claim you can defend.

## Reopen when

Prevention shows a measured false-negative rate of zero against adaptive adversaries (not vendor marketing rates).
