# ADR-25. Signed fail-posture matrix {#adr-25}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.4-solution-strategy.md`, `chapters/3.3-failure-postures.md`

**In plain terms:** Before launch, fill dependency × tier with refuse/degrade/terminate - and get the consequence owner's signature.

## Context

Unsigned recommendations lose to a 03:00 phone call. Then posture is invented under pressure.

## Decision

Require a signed fail-posture matrix by the person who owns the business consequence, before launch.

## Why not the alternative

**Rejected:** Leave posture as an unsigned platform recommendation to be decided on the incident bridge.

Urgent defaults become permanent architecture without a decider.

## What changes if you follow this

Some cells are uncomfortable (terminate run on model outage). That discomfort belongs before launch.

## Cost

Meeting time with business owners; matrix storage reachable at 03:00.

## Reopen when

A dependency appears for which no declared fail posture is honest.
