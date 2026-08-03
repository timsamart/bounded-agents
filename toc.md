<!--
Initial and provisional. Chapters move, expand and contract as outlining
deepens. When outline.md reveals that a chapter should be merged, split,
renamed or reordered, update this file in the same revision.

Function statements say what a chapter does, not what it covers.
-->

# Table of Contents

- **Title:** Governed Agentic Infrastructure *(working title – see `concept.md` §8)*
- **Subtitle:** *(deferred)*
- **Author:** Timotheos Samartzidis (Timo Sam)

**Grouping map** (for `CONV-003` file naming, `chapters/P.C-slug.md`):

| `P` | Grouping | Divider |
|---|---|---|
| 0 | Front matter | none |
| 1 | Part I – Why This Shape | `1.0` |
| 2 | Part II – The Mechanisms | `2.0` |
| 3 | Part III – Operating It | `3.0` |
| 4 | Part IV – The Edges | `4.0` |
| 5 | Appendices | none |
| 6 | References | none |

**Altitude rule.** Each part is complete at its own altitude: a reader who stops at the end of any part holds a coherent and defensible position, not half of one. This is the structural claim the whole document rests on, and it is testable – cut the manuscript after any part and ask whether the remainder still answers *what do we build, and why*.

**Page figures.** Every `pp` figure below is a projection from the current chapter list, not an allowance (`manifesto.md` §10, decision 16). Completeness at an altitude is the property being claimed; the page count is what that completeness currently costs. Chapters may be added, split or merged where the material requires it, and the figures are revised in the same revision rather than defended.

---

## Front matter

- **`0.1-front-matter.md`** – title, supersession statement, and the reading paths, printed once as a table. *Function: tell a reader in one page which parts are theirs, and state plainly that this document replaces the whitepaper and the book.*
- **List of figures and tables** – generated.
- **List of abbreviations** – generated from Appendix H.

No preface. The introduction does that work, as argument rather than apology.

---

## Main matter

## Part I. Why This Shape *(altitude 0–1, ~35 pp)*

Complete for: the engineering or risk leader, and any reader who needs to defend the decision to build.

### Chapter 1. Introduction

`chapters/1.1-introduction.md`

Function: establish that there are only two questions, that the first has no engineering answer, and that everything following is the second – then state the claim, the non-goals, the trust assumptions under which the claim fails, and who should not build this at all. Complete on its own – the structural claim is the completeness, and eight pages is the current projection of what it takes.

### Chapter 2. What the Environment Forces On You

`chapters/1.2-constraints.md`

Function: separate the constraints that are genuinely imposed from the ones that are conventionally assumed, so a reader can tell which parts of the design are negotiable in their setting.

### Chapter 3. The System in Its Landscape

`chapters/1.3-context-and-scope.md`

Function: fix the vocabulary and the boundary – who the actors are, what a *run* is, where the trust boundary falls – so every later chapter can name things without redefining them.

### Chapter 4. Five Moves and the Invariants They Buy

`chapters/1.4-solution-strategy.md`

Function: state the whole architecture at altitude 1 as five moves rather than a component list, and print the invariant set once, in falsifiable form. A reader who stops here can defend the shape without being able to build it.

## Part II. The Mechanisms *(altitude 2, ~65 pp)*

Complete for: the architect and the platform engineer. Each chapter derives one mechanism from the failure that forces it, and each ends with what it costs and how you would know it had quietly stopped working.

### Chapter 5. Identity and Binding

`chapters/2.1-identity-and-binding.md`

Function: show why possession of a credential must stop being sufficient authority, and derive the two-chain identity model and sender-constrained run credentials from the theft-to-use window.

### Chapter 6. The Envelope

`chapters/2.2-the-envelope.md`

Function: derive per-run authority from declared need, principal reach and tier ceiling – never inherited from the agent's standing role – and establish attenuation-only delegation as an architectural property rather than a policy.

### Chapter 7. Complete Mediation

`chapters/2.3-complete-mediation.md`

Function: convert *complete mediation* from an adjective into a published number, and show why coverage is measured against discovered paths rather than designed ones.

### Chapter 8. The Seam

`chapters/2.4-the-seam.md`

Function: establish that the transition from non-deterministic to deterministic compute is the only governable moment in the system, show that a tool protocol's real contribution is standardising *where* that transition happens, and then separate what the protocol carries today from what the platform has to carry on its behalf – including the six properties the protocol would need before the seam could itself be the governance layer.

### Chapter 9. Approval and Effect Integrity

`chapters/2.5-approval-and-effect-integrity.md`

Function: distinguish an approval that is a control from one that is theatre, and establish that what was approved and what was executed must be the same object.

### Chapter 10. Data, Retrieval and Memory

`chapters/2.6-data-retrieval-memory.md`

Function: treat memory as the writable data system it actually is, and derive purpose binding, classification ceilings and principal-aware retrieval from the fact that externally sourced content is indistinguishable from authored content unless the platform makes it distinguishable.

### Chapter 11. Evidence

`chapters/2.7-evidence.md`

Function: resolve the apparent contradiction between tamper-evident records that must survive and personal data that must be erasable, and show what an evidence path that gates execution costs.

## Part III. Operating It *(altitude 3, ~40 pp)*

Complete for: the SRE and the platform owner. Written so it can be read first, by someone who has inherited the system rather than built it.

### Chapter 12. The Agent Manifest

`chapters/3.1-agent-manifest.md`

Function: define the signed deployable unit – prompt hash, tool bindings, declared need, policy refs, model set, delegation graph – so quarantine, recertification and evaluation attach to something the organisation can name and diff.

### Chapter 13. Governance in the Hot Path

`chapters/3.2-hot-path.md`

Function: engineer the decision path as the latency-critical component it is, and state what happens to runs in flight when the control plane dies.

### Chapter 14. The Outage You Decide in Advance

`chapters/3.3-failure-postures.md`

Function: force the fail-posture matrix into a design review rather than an incident, and defend the one posture that is not negotiable – no evidence, no side effects.

### Chapter 15. Stopping It

`chapters/3.4-stopping-it.md`

Function: replace the single kill switch with the five distinct mechanisms the reader actually needs, each with an owner and a drill, and name what no switch can undo.

### Chapter 16. Decay

`chapters/3.5-decay.md`

Function: establish that every control in this document degrades silently, that the degradation is measurable, and that recertification and drills are the only reason any of it still exists in month fourteen.

### Chapter 17. The Paved Road

`chapters/3.6-the-paved-road.md`

Function: show that an unadopted control has negative security value, and price the sanctioned path against the shortcut in the only unit that decides adoption – minutes.

## Part IV. The Edges *(~25 pp)*

Complete for: nobody, honestly. This part is where the field has no settled answer, and it says so.

### Chapter 18. Composition

`chapters/4.1-composition.md`

Function: establish which invariants survive an agent calling an agent, which do not, and what the current absence of a composition standard costs the reader today.

### Chapter 19. Across the Boundary

`chapters/4.2-across-the-boundary.md`

Function: extend the model to agents acting with and against other organisations' agents, where neither side controls the other's policy, and mark the parts that are currently unbuildable.

### Chapter 20. Build Order, and Who Should Not Build This

`chapters/4.3-build-order.md`

Function: sequence the work for a team of five over two quarters, and state without hedging the conditions under which the correct answer is to build almost none of it.

### Chapter 21. What It Can Still Do

`chapters/4.4-residual.md`

Function: close the residual honestly – what remains possible for an adversary after everything here is built and operating – and convert the document's expiry into a schedule rather than an implication.

---

## Back matter

### Appendices

| | Appendix | What it is |
|---|---|---|
| A | Control register | The normative requirements. RFC 2119 language, traced threat → control → test → evidence. What an auditor reads instead of the spine. |
| B | Architecture decision records | Thirty ADRs in Nygard's form, each with its rejected alternatives, its cost, and the trigger that would reopen it. Also holds the C4 views. |
| C | Threat model and method | The threat set, and the method for generating threats when this set ages. |
| D | Artefact schemas | Every wire format in one place: run credential, envelope, tool call, policy decision, refusal, approval record, evidence event, budget. |
| E | Worked examples | End-to-end walkthroughs compiled from spine worked moments: onboard a tool, derive an envelope, graduate an agent to unattended operation, work a suspected compromise. Inventory in `worked-moments.md`. |
| F | Conformance and scorecard | The conformance suite, and the adoption scorecard with its gating questions. |
| G | Drills and calendar | Kill-switch drills, the canary suite, the recertification calendar. |
| H | Glossary | Terms, and the ones the field commonly uses in two senses. |

### References

A single numbered list, ordered by first appearance, following the appendices. Sources with an expiry carry a retrieval date and a status word.

### Indexes *(PDF only)*

- Term index – substantive discussion only.
- Decision index – every ADR mapped to the section that argues it and the requirements that depend on it.
