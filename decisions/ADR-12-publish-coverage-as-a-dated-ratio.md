# ADR-12. Publish coverage as a dated ratio {#adr-12}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** `chapters/1.4-solution-strategy.md`, `chapters/2.3-complete-mediation.md`

## Context

The alternative is mediation as a design assertion, and it is not dishonest. A design document exists to state intent. The intent is right. *All tool access is mediated by the gateway* is what the team is building towards. The defect is that an assertion has no failure mode anyone notices. It cannot be wrong on a Tuesday. It can only be discovered, eighteen months later, to have been wrong since the spring. An unmeasured hundred per cent is not a better number than a measured 60%: it is the same estate with the measurement missing, and only one of those two organisations knows which path to close first.

The effect set becomes enumerable at the moment every effect has to pass through one interface, and not before. This is complete mediation, which Jerome Saltzer and Michael Schroeder stated in 1975 and which is not new to anyone reading this. What is new is the denominator. In an agent system the interface is also the boundary between the part that guesses and the part that acts. Mediation stops being a property of the design and becomes a measured fraction: the proportion of paths to a system of record that go through the interface, counted against paths discovered rather than paths designed.

## Decision

Publish mediated-path coverage as a dated ratio; separate discovery ownership from closure ownership.

That number is never 100% at first measurement. The missing percentage points all have names. A credential in a developer's local configuration. A service account from a 2023 integration. A sidecar somebody added in March to unblock a release. Chapter 7 measures the fraction. Chapter 8 takes the seam itself, where a tool protocol decides the point at which the transition from guessing to doing physically happens. The first honest coverage measurement is uncomfortable in a way that a design assertion never is. That is the argument for publishing a number rather than an adjective: an adjective cannot be tracked quarter over quarter and a fraction can.

## Consequences

A path you cannot close this quarter is not a gap in a report. It is a risk acceptance with a named owner, a date, and a compensating control where one exists, recorded in the same register as every other risk acceptance the organisation carries and visible to the same people. A register holding 17 open paths, each with an owner and a date, is a plan. The same 17 in a footnote is a finding that somebody else will make later, with worse timing and a larger audience.

Markers `[ADR-12]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**Assert complete mediation with an adjective and no denominator.**

What it costs: 20–40 ms at p99 on every mediated call, most of it in the decision path. One interface is also one concentration of risk, which is why the design is federated gateways with centralised policy rather than a single gateway with a single failure domain. The heavier cost is organisational. Every tool now has an onboarding step, with a declared side-effect class and a manifest entry. The sanctioned road is therefore slower than the shortcut that goes around it.

## Cost

Priced in the arguing chapter (latency, engineering effort, or operational burden appears in the narrative above or in the Decision section).

## Reopen when

Discovery finds a path class mediation cannot cover without a different primitive.
