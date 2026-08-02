<!--
Pedagogical layer between context and abstraction. Inventory, rules, and
Appendix E assembly map. Linked from outline.md, voice.md §7, CONV-015,
role-1-draft-editor.md, and open-questions.md resolutions.
-->

# Worked Moments – Inventory and Rules

- **Project:** Governed Agentic Infrastructure *(working title)*
- **Linked artifacts:** `outline.md`, `voice.md`, `conventions.md`, `open-questions.md`, `toc.md`
- **Last revised:** 2026-07-31
- **Cast:** Borealis Mutual · `claims-triage` · Marta · Kai · `borealis-eu-1`

## What this file is for

The reference architecture teaches by derivation. `archive/book-v2/` taught by siege narrative. This document rejects scene openers (`voice.md` §4.1) but still needs a middle layer: pragmatic beats that make abstract mechanisms land before the general form is stated. Those beats are **worked moments**.

A worked moment is not a scene. It is 150–400 words on the fixed cast, one mechanism, one decision point, with numbers where possible. It sits in the mechanism rhythm **after** the promise and its failure, **before** the surviving move and the artefact.

## The three pedagogical tiers

| Tier | Where | Length | Job |
|---|---|---|---|
| **Worked moment** | Spine, per mechanism beat | 150–400 words | Make the abstract claim intuitive on Borealis |
| **Worked walkthrough** | Appendix E | End-to-end | Assemble spine moments into one traceable run |
| **Illustration** | Spine, optional | One image | Visual parable after the moment; never load-bearing |

Appendix E is compiled from spine material, not written separately. Identifiers in E must match the cast table in `outline.md` and every artefact in Appendix D.

## Rules

1. **Answer-first still holds.** The section opens with its conclusion. The moment illustrates; it does not defer.
2. **Deletion test, split.** Remove one moment and the argument stands. Remove all moments from a chapter and a reader who has never built one of these cannot follow the intuition.
3. **Cast is law.** Same names, same identifier forms, same tenant. Fictional actors get a first name and role only (`voice.md` §2).
4. **One moment per major beat** in mechanism chapters. Part I: one per chapter minimum. Part III–IV: one where the mechanism is operational rather than derivational.
5. **No dialogue arcs, no suspense, no chapter openers.** Two sentences of recognition at a section open; a worked moment is longer and does one job.
6. **Pointer to Appendix E** where a moment is a slice of a walkthrough: end the moment with `[A-E.n]` only if E exists; until E is drafted, cite the walkthrough name in the card.

## Mechanism rhythm (performed, never printed)

```
promise → failure → worked moment → surviving move → artefact → cost → decay
```

## Appendix E – walkthrough assembly

| Walkthrough | `[A-E.n]` | Spine moments it compiles | New material in E only |
|---|---|---|---|
| Onboard a tool | E.1 | ch. 8 (manifest pin), ch. 7 (first mediated path) | Registry promotion, conformance check |
| Derive an envelope | E.2 | ch. 5 (run start), ch. 6 (intersection arithmetic) | Mandate artefact for unattended variant |
| Graduate to unattended | E.3 | ch. 5 (03:00 batch), ch. 9 (gate measurement), ch. 12 (bundle staleness) | Standing mandate signing ceremony |
| Work a suspected compromise | E.4 | ch. 14 (eleven-minute stop), ch. 11 (chain verify), ch. 7 (coverage gap) | Drill timeline, incident clock |

## Illustration placement map

Images in `assets/` are optional tier-three anchors. Rules: after the worked moment, captioned with the idea they anchor, greyscale-safe, never substituting for a schematic (`voice.md` §8; `manifesto.md` §10.13).

| Asset | Mechanism anchored | Chapter | After moment |
|---|---|---|---|
| `ki eingespert in isolation.jpg` | Trust boundary; model outside TCB | 1, 3 | TCB size |
| `capability envelope.jpg` | Intersection vs union | 6 | Role arithmetic |
| `papier klopft auf schulter key oeffnet tuer.jpg` | Confused deputy; authority ≠ instruction | 6 | Attenuation |
| `schloss amboss kette.jpg` | Attenuation-only chain | 6, 17 | Delegation shrink |
| `ai handing id stempel.jpg` | Two chains joined at run start | 5 | Binding |
| `durchgang ki plus paket.jpg` | Mediation as turnstile | 7 | Coverage ratio |
| `gripper gripping a mail envelope.jpg` | Untrusted payload at seam | 8, 10 | Provenance |
| `akten dispenser sheriff.jpg` | Pinned manifest / allow-list | 8 | Registry |
| `aufzug mit ticket.jpg` | Write-before-effect | 11 | Ordering |
| `switch red.jpg` | Stop mechanisms | 14 | L1–L5 |
| `lever in a glass box.jpg` | No agent break-glass; human path | 14 | Manual path |
| `stares leading to wall thermometer in broken.jpg` | Decay measurement | 15 | Canary / recert |
| `infinite scroll.jpg` | Budget exhaustion | 3, 14 | Call budget |
| `egg.jpg` | Residual; what remains | 20 | Residual list |

## Chapter inventory

Status: **planned** until drafted. `[OQ-nn]` marks subject-matter resolutions that supply the moment's facts.

### Part I

| Ch | Worked moment(s) | Seed |
|---|---|---|
| 1 | Payment batch vs agent deputy; four lines in a Tuesday PR | Draft ch. 1 §1–2 |
| 2 | Borealis constraint inventory (filled example): Entra, Guidewire, model deprecation calendar, incumbent PAM | `[OQ-03]`, `[OQ-22]`, `[OQ-31]` – blank form in spine, full row set here |
| 3 | `claims-triage` at 09:00: one run, four thousand yesterday; Marta's run vs overnight batch run | `[OQ-01]` mandate vs attended |
| 4 | Post-incident review: eleven action items, two wrong fixes (classifier + prompt) | `archive/book-v2/` ch. 4 |

### Part II

| Ch | Worked moment(s) | Seed |
|---|---|---|
| 5 | Token lifted and used same second; 03:00 batch under standing mandate `mandate:claims-nightly` | `[OQ-01]`, `[OQ-02]` |
| 6 | Role union 47 tools → declared need 6 → intersection 4 after Marta's reach; Kai's path used only permitted tools | `[OQ-09]` ceiling fixed; `[OQ-17]` need is static |
| 7 | First coverage measurement: 94% mediated, path found via developer MCP config on laptop | `[OQ-12]` |
| 8 | German note in claim doc; classifier 0.31; sampling blocked, elicitation terminated at gateway | `[OQ-10]`, `[OQ-11]` |
| 9 | Payment adjustment: faithful summary, different payload hash; Marta's 14th approval at 08:47 | `archive/book-v2/` ch. 4 |
| 10 | Session-1 injection in claim note; session-3 retrieval; org memory holds authored only | `[OQ-15]`–`[OQ-17]`, `[OQ-27]` cache prefix |
| 11 | Effect refused until evidence write ack; erasure by key destruction on one subject | `[OQ-18]`, `[OQ-28]`, `[OQ-29]` |
| **12 (new)** | Agent manifest v2.3.1: binding prompt hash, tool refs, declared need, model set, delegation graph | `[OQ-19]`–`[OQ-21]`, `[OQ-24]` |

### Part III

| Ch | Worked moment(s) | Seed |
|---|---|---|
| 13 | Marta signs fail-posture matrix before outage; model-unavailable row terminates run | `[OQ-24]`, `[OQ-30]` |
| 14 | Eleven minutes to stop; L1 pause button in UI; human manual adjustment path (no break-glass run) | `[OQ-05]`, `archive/book-v2/` ch. 16 |
| 15 | Envelope within 8% of tier ceiling; rule never fired in 90 days; exercised-set recert query | `[OQ-02]`, `[OQ-08]` |
| 16 | Local dev tier: synthetic tenant, hard T1 ceiling, 340 budget-exhausted runs first month | `[OQ-23]` |
| 17 | Parent spawns research sub-agent; platform derives child envelope from manifest graph | `[OQ-25]` |

### Part IV

| Ch | Worked moment(s) | Seed |
|---|---|---|
| 18 | Cross-org credential exchange; routing sends inference to wrong region | `[OQ-31]` |
| 19 | Build order quarter 1: gateway before evidence before unattended | assemble |
| 20 | Residual: browser automation path, gateway concentration, model drift | `[OQ-04]`, `[OQ-13]` |

---

*Inventory v0.1 – 2026-07-31. Grows as cards reach `[BEATS]` with a **Worked moment(s)** field filled.*
