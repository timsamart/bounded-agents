# Appendix G. Drills and calendar {#appendix-g}

Kill-switch drills, canaries, recertification. Owners and runbook references are required fields. A blank "last exercised" cell means the control is absent for the quarter (ADR-27).

## Operating calendar {#a-7-1}

| Cadence | Item | Owner (role) | Runbook | Notes |
|---|---|---|---|---|
| Quarterly | Stop drills L1–L5 | Platform SRE | stop-l1…l5 | Against live run |
| Quarterly | Degraded-mode entry/exit | Platform SRE | degraded-mode | Dual-control exit |
| Daily | Refusal canaries (above reversibility) | Platform on-call | canary-refuse | ~40 probes |
| Hourly | Revocation freshness sample | Platform on-call | revoke-fresh | Unknown ⇒ fail closed |
| Standing | Model-pin deprecation watch | Agent owners | model-deprec | Vendor calendar |
| Quarterly | Bilateral credential expiry review | Integration owner | bilateral-exp | Counterparties |
| Weekly | Recertification pack (ceiling, need, exercised set) | Data owner + platform | recert-pack | ADR-32 |

## Inventories and canaries {#a-7-2}

Maintain: endpoint configuration inventory; about 40 refusal canaries; memory provenance fraction; signed fail-posture matrix storage location reachable at 03:00. Canary failures open incidents, not tickets filed next week.

## Chain-break and revocation freshness {#a-7-3}

Evidence-break runbook: stop batch → reconcile → human-owned output. Revocation channel freshness unknown means fail closed for effects. Drill number for stop freshness belongs beside chapter 15 intervals.

## Manual path and composition telemetry {#a-7-4}

Manual system-of-record emergency path stays on the drill calendar (ADR-33). Quarterly: max observed delegation depth and fan-out versus configured limits (ADR-29).

## Deprecation and counterparty expiry {#a-7-5}

Vendor model-pin deprecation is a named standing job. Counterparties with lapsed schedules MUST NOT keep audiences that still accept their credentials without an acceptance row.
