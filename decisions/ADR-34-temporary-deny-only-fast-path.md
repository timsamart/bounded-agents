# ADR-34. Temporary deny-only fast path {#adr-34}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/3.2-hot-path.md`

**In plain terms:** Incidents may push a temporary deny list with hard expiry. Never a fast permit path.

## Context

Fast permits bypass review. Permanent incident narrowing without review becomes shadow policy.

## Decision

Allow a temporary deny-only incident path with hard expiry; never a permit-fast path.

## Why not the alternative

**Rejected:** Add a fast permit path, or make incident narrowing permanent without the ordinary bundle path.

Permit-fast is how authority leaks. Permanent bypass is how policy forks.

## What changes if you follow this

Second policy channel with clear precedence and expiry. Worst case is self-inflicted refusal.

## Cost

Operational complexity of two channels - bounded by expiry.

## Reopen when

Incident response requires permanent narrowing that cannot wait for the ordinary path.
