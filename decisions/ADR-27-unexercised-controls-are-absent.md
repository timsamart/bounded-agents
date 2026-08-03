# ADR-27. Unexercised controls are absent {#adr-27}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.4-solution-strategy.md`, `chapters/3.4-stopping-it.md`, `chapters/3.5-decay.md`

**In plain terms:** If a stop or control has not been exercised against a live run this quarter, treat it as absent.

## Context

Unlike database failover, agent stops have no organic exercise. Undrilled switches have never run.

## Decision

A control unexercised against a live run in a quarter is absent. The drill calendar is load-bearing architecture.

## Why not the alternative

**Rejected:** Treat drills as optional SRE hygiene demoted out of architecture.

First execution during the real incident is training under fire with production stakes.

## What changes if you follow this

Quarterly drills with owners and measured intervals (Appendix G).

## Cost

Calendar time and incident-like inconvenience - cheaper than fiction.

## Reopen when

An auditor rejects exercised-set evidence and requires an alternative you must meet.
