# Appendix F. Conformance and scorecard {#appendix-f}

Falsification tests for the three-part claim and invariants I1–I8.

## Claim tests {#a-6-1}

| Id | Claim | Pass | Fail |
|---|---|---|---|
| C1 | Bound listed before run | Enumerate reachable effects from envelope + credential; empty surprise set | Any reachable effect absent from the pre-run list |
| C2 | Evidence reconstructs effects | External actions match evidence events; chain verifies | Action without record, or silent rewrite |
| C3 | Stop within stated time | Revoke without agent help; wall-clock ≤ published interval | Run continues past interval, or stop requires agent cooperation |

## I1 coverage measurement {#a-6-2}

Publish mediated calls over discovered effect paths as a dated ratio. Discovery ownership MUST be separate from closure ownership. Open paths enter the acceptance register (A-1.7).

## Friction and attenuation depth {#a-6-3}

If coverage falls, measure minutes of path friction on the sanctioned road before rewriting policy. Attenuation MUST hold across delegation depth; depth and fan-out are bounded and measured quarterly.

## Seam, approval, memory, evidence, manifest, bundle age {#a-6-4}

| Invariant | Test sketch |
|---|---|
| I2 Seam | Authority field injected from agent side is ignored or refused |
| I5 Approval | Altered-post-approval payload refuses at execution |
| I6 Memory | External vs principal content distinguishable; provenance present |
| I3 Evidence | Evidence queue loss fails closed for effects |
| I7 Manifest | Declared need is manifest-sourced; digest mismatch refuses start |
| I8 Bundle | Stale bundle beyond staleness budget fails closed |

## Stop-path cost {#a-6-6}

Revocation check MUST fit inside the stated p99 budget on the hot path (illustrative 20–40 ms mediation envelope). Drill-measured stop intervals for L1–L5 are published beside the claim; an unexercised level is scored absent (ADR-27).
