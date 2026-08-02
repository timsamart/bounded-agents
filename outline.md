<!--
Where research becomes drafting raw material. One card per chapter in
toc.md. A card at DRAFT-READY can be drafted by role 1 without consulting
anything except manifesto.md, voice.md, conventions.md, this card, and the
sources it cites.
-->

# Outline: Governed Agentic Infrastructure

- **Subtitle:** *(deferred)*
- **Author:** Timo Sam
- **Linked artifacts:** `manifesto.md`, `voice.md`, `toc.md`, `references.bib`, `conventions.md`, `concept.md`, `open-questions.md`, `worked-moments.md`
- **Last revised:** 2026-08-01 (spine first draft complete; all chapter cards [DRAFTED])

## How to use this file

Each chapter is a **card**. The base card is status, function, argument, beats, cross-references, source integration, working quotations, gaps and queries. Cards are independent; one can reach `DRAFT-READY` without affecting the others.

This project extends the card with six fields, because six things have to be true of every mechanism chapter and the outline is where they are decided rather than discovered at draft time.

| Field | Why it is in the card and not in the draft |
|---|---|
| **Invariant** | Each mechanism chapter earns exactly one falsifiable invariant, stated once. If the card cannot state it in a sentence that could be false, the chapter has no mechanism in it. |
| **Decisions anchored** | Which ADRs this chapter argues, and the alternative each rejected. A chapter with no rejected alternative is a description, not a derivation. |
| **Worked moment(s)** | Cast-bound vignettes (150–400 words) that sandwich context and abstraction. Inventory in `worked-moments.md`; mandatory for Part II and chapter 12 (`CONV-015`). |
| **Figures** | Planned schematics with the question each answers, decided before drafting so that the three-per-chapter ceiling is a design constraint rather than an editing casualty (`voice.md` §8). |
| **The bill** | What the mechanism costs in latency, headcount, developer experience and standing obligation. `manifesto.md` decision 6 makes an unpriced control a defect. |
| **Decay question** | The single question that reveals whether this control is still true. Each becomes a row in Appendix G and a beat in chapter 16. |

Not every chapter carries every field. Chapters 1 to 4 argue a shape rather than a mechanism, and chapters 20 and 21 assemble rather than derive.

## Core Thesis

Prevention has a false-negative rate we do not control. Containment has a bound we do. Every mechanism in this document is a consequence of preferring the quantity we own, and the document's job is to make that consequence derivable rather than assertable – so that a reader can rebuild the argument in their own setting, where the constraints differ.

The second thesis is about the document rather than the system. A reference architecture that cannot say what it rejected is a diagram with an opinion. The decision layer is therefore not apparatus attached to the argument; it is the argument, moved to reference position so that it can be consulted rather than endured.

## Method and Voice Anchors

Answer first, then the reason, then what to do with it. Short sentences. Ordinary words before jargon. Clarity beats cleverness: if a plainer sentence carries the same claim, use it. Every mechanism states its cost and how you would know it had quietly stopped working. The adversary is a person. The naive design is good work under assumptions that no longer hold. British English, spaced en dashes, no em dashes, no normative keywords outside the appendices, and no marker that carries meaning.

## Evidence Ladder

1. **Normative specifications** – RFCs, OAuth and OIDC, MCP, W3C. Binding. A deviation is an ADR.
2. **Regulatory instruments** – DORA, EU AI Act, GDPR, supervisory guidance. Authoritative for obligation and burden of proof, never for design.
3. **Security engineering literature** – Saltzer and Schroeder, the capability tradition, Hardy, contemporary agent-security research. Supplies principles and vocabulary.
4. **Empirical and incident material** – published incidents, measured attack results, benchmark data. Strongest evidence available for claims about what actually happens; scarce in this field, and its scarcity is itself reportable.
5. **Vendor and platform documentation** – evidence of what is buildable today. Always dated in the citation.
6. **The superseded corpus** – `archive/`. Authoritative on what the author previously concluded, not on whether it was right. Input to re-litigation, never support.

## Source Notes

- **`archive/whitepaper.md`** – the largest input and the most dangerous. Its conclusions are largely sound and its argument order is not reusable. Policy: a chapter may consult it only after its own argument is outlined, to check for missed considerations. Never quoted as support. Any claim carried across without re-derivation is marked `[QUERY: inherited, not re-derived]`.
- **`archive/book-v2/`** – the derivations are the best in the corpus and are reusable at the level of *reasoning*, not prose. Its chapter openers are scenes, which this document does not use.
- **Vendor documentation** – retrieval date mandatory. Any claim depending on a vendor's current behaviour carries a sentence saying so, because it will be wrong within two editions.
- **Protocol specifications under active revision** – MCP in particular. Every claim about what the protocol does or does not carry is pinned to a named revision and a retrieval date, and chapter 8 is written so that the argument survives the protocol improving. See that card's gaps.
- **Multi-agent composition literature** – thin and fast-moving. Policy: cite preprints as preprints, and prefer stating the absence of an answer over citing a weak one.

## Cast and identifiers

Fictional but fixed, so that artefacts stay consistent across chapters and appendices (`CONV-010`).

| Thing | Value | Notes |
|---|---|---|
| Organisation | Borealis Mutual | European insurer; regulated, mid-size, plausible |
| Agent | `claims-triage` | The running example throughout |
| Human principal | Marta, claims lead | Competent, rushed, never foolish |
| Adversary | Kai, a person | Motivated, patient, external. Never the model |
| Run identifier form | `run_01J8…` | ULID, lowercase prefix |
| Tool identifier form | `tool:claims-core/post-adjustment` | Namespaced, verb-final |
| Tenant | `borealis-eu-1` | |

---

## Working Conventions for This File

### Status flags

`[SKELETON]` function and argument only · `[BEATS]` argument, beats, decisions, figures, bill and decay question in place, sources not yet integrated · `[SOURCE-INTEGRATION]` sources identified and noted · `[QUOTATIONS]` working quotations gathered · `[DRAFT-READY]` everything in place, role 1 may start · `[DRAFTED]` role 1 complete · `[FINAL]` cleared role 3.

### Quotation marker format

Per `CONV-002`. A working quotation without a marker is not draft-ready and role 1 will refuse it.

### Cross-references

`→ §X.Y` this chapter sets up material developed there. `← §X.Y` this chapter requires material established there. Renumbering updates both files in one revision.

### Pending evidence and queries

`[PENDING: description]` for expected evidence. `[QUERY: question]` for an author decision. Both resolved before `DRAFT-READY`.

These are questions about the draft. Questions about the subject – the ones whose answer changes what is true about the system rather than how a chapter is written – live in `open-questions.md` as `[OQ-nn]` and are referenced from a card by marker. A chapter cannot reach `DRAFT-READY` while an `[OQ-nn]` it depends on is open, and the register names which chapters each one blocks.

---

## The invariant set

Printed once in chapter 4, referenced by number everywhere after. Each is falsifiable, each is owned by one mechanism chapter, and each has a conformance test in Appendix F. A chapter that does not make one of these true or keep it true has to justify its page count.

| | Invariant | Made true in | Test |
|---|---|---|---|
| I1 | No effect leaves the platform except through a mediated call. | ch. 7, ch. 8 | coverage measurement |
| I2 | No call carries authority beyond the envelope in force at the moment of the call. | ch. 6 | envelope conformance |
| I3 | No delegation widens authority. Widening is unrepresentable, not forbidden. | ch. 6, ch. 18 | attenuation proof |
| I4 | No side effect occurs without a durable, tamper-evident record written first. | ch. 11 | write-before-effect ordering |
| I5 | The object approved and the object executed are the same object. | ch. 9 | hash binding |
| I6 | Revocation takes effect within a stated interval, without the agent's cooperation. | ch. 15 | quarterly drill |
| I7 | Every control has a test, an owner, and a date on which it was last exercised. | ch. 16 | recertification calendar |
| I8 | Authority derivation reads no input the agent can write. | ch. 6 | declared-need immutability audit |

## Decision index

Thirty records, Nygard form, Appendix B. Each is argued in exactly one chapter and referenced from anywhere else by marker. The rejected alternative is the load-bearing half; a record whose alternative was never seriously considered is deleted rather than padded.

| ADR | Decision | Rejected | Argued in |
|---|---|---|---|
| 01 | Containment over prevention as the primary strategy | Detection-first, with containment as backstop | ch. 1 states, ch. 4 argues |
| 02 | The run is the unit of authority, budget, evidence and revocation | Session-scoped; agent-scoped | ch. 3 |
| 03 | The trusted computing base is three components and stays that size | Trusting the orchestration framework | ch. 3 |
| 04 | Regulatory obligations map to evidence, not to controls | Mapping to a vendor control catalogue | ch. 2 |
| 05 | Discrete risk tiers rather than continuous risk scores | Continuous scoring with thresholds | ch. 2 |
| 06 | Two identity chains, joined by a per-run binding | Single agent identity acting for itself | ch. 5 |
| 07 | Sender-constrained credentials | Short-lived bearer tokens alone | ch. 5 |
| 08 | Token exchange at a broker | Direct grants per tool from the IdP | ch. 5 |
| 09 | Envelope as the intersection of declared need, principal reach, tier ceiling | Role-based authority inherited by the agent | ch. 6 |
| 10 | Attenuation-only delegation, enforced by construction | Policy rule forbidding escalation | ch. 6 |
| 11 | Allow-list of typed operations | Deny-list of dangerous operations | ch. 6 |
| 12 | One mediation interface, coverage published as a number | Mediation as a design assertion | ch. 7 |
| 13 | Federated gateways, centralised policy | Single central gateway | ch. 7 |
| 14 | Adopt MCP as the seam protocol; keep authority semantics in the gateway | Proprietary internal calling convention; waiting for the protocol to grow them | ch. 8 |
| 15 | Tool descriptions are untrusted data with provenance | Treating registered tool metadata as trusted configuration | ch. 8 |
| 16 | Pinned, signed server manifests from an internal registry | Runtime discovery from external registries | ch. 8 |
| 17 | Declared side-effect class per operation, required at onboarding | Inferring reversibility from the operation name | ch. 8 |
| 18 | Propose-then-execute with hash-bound frozen artefacts | Approving a rendered summary | ch. 9 |
| 19 | Approval gates are measured; unread gates are removed and the action demoted | Keeping the gate for the audit narrative | ch. 9 |
| 20 | Retrieval under the principal's entitlements | Retrieval under the agent's service identity | ch. 10 |
| 21 | Memory as a first-class data system with provenance and a quarantine tier | Memory as an implementation detail of the framework | ch. 10 |
| 22 | Hash-chained evidence, per-subject content keys, erasure by key destruction | Redaction in place; exemption claims against erasure | ch. 11 |
| 23 | No evidence, no side effects | Best-effort logging with an availability carve-out | ch. 11, ch. 14 |
| 24 | Embedded policy evaluation with signed bundles and declared staleness budgets | Central policy service call per decision | ch. 13 |
| 25 | Fail postures declared per dependency and tier, signed before launch | Uniform fail-closed; uniform fail-open | ch. 14 |
| 26 | Five distinct stop mechanisms | One kill switch | ch. 15 |
| 27 | A capability exists only if it was exercised last quarter | Documented procedures as evidence of capability | ch. 16 |
| 28 | The paved road is funded as a product with an owner | Security-owned tooling, funded as a project | ch. 17 |
| 29 | Sub-agents receive derived envelopes; approval and intent do not carry | Propagating the parent's authority and approval | ch. 18 |
| 30 | Cross-organisational trust rests on verifiable claims and attenuated credentials | Assuming a shared policy domain or a federated broker | ch. 19 |

---

# Part I. Why This Shape

## Chapter 1: Introduction

**Status:** [DRAFTED] – first draft written 2026-07-31 to lock the voice. Sources not yet integrated; see gaps.

**Function in the book.** The introduction has to do four things in eight pages and is the only chapter permitted to be complete on its own: separate the question that has no engineering answer from the one that does, state the claim the rest of the document defends, name the trust assumptions under which the claim fails, and tell a proportion of readers to stop. It is also where the reader learns the document's disclosure grammar – not by being told, but by encountering markers in the first two pages and finding that ignoring them costs nothing.

**Argument.** There are two questions about an agent that can act: how do we stop it being fooled, and what can it do once it has been. The first has no engineering answer that survives contact with an adversary, because the interface that makes an agent useful is the interface that makes it persuadable. The second has an answer, the answer is architectural rather than probabilistic, and the whole document is that answer. The cost of the answer is real, is stated, and is not worth paying for most systems.

**Narrative beats.**

- Open on the asymmetry: classic automation does what its code says; an agent decides at runtime, reads attacker-controllable input, and holds real credentials.
- The two questions, stated plainly. Retire the first with an argument rather than a dismissal, and without disparaging the people selling answers to it.
- The claim, in one paragraph, falsifiable.
- What the claim assumes – the trust assumptions, stated on page four rather than page two hundred, because a claim without them is marketing.
- Non-goals, as a short list, so the reader stops looking for chapters that do not exist.
- Who should not build this: the intersection test – unattended operation, irreversible or externally visible effect, regulated burden of proof. Miss all three and the correct build is a gateway and a quarter spent elsewhere.
- What this document is and what it replaces, in the author's own voice, briefly.
- The shape of what follows, in one short passage, closing on the guarantee that every mark is optional. The reading-paths table lives in the front matter and is not repeated here.
- The last beat is the residual and the decay, so that the chapter's final note is the document's honesty rather than its promise.

**Decisions anchored.** `[ADR-01]` is named here and argued in chapter 4. The introduction states the preference and its consequence; it does not litigate it, because the reader has not yet met the mechanisms whose cost the preference explains.

**Cross-references.**

- → §1.4: the five moves are named here without being explained; the introduction must not pre-empt them.
- → §4.3: who should not build this is stated here in a paragraph and argued there in a chapter. The paragraph must not contain the argument.
- → §4.4: the residual is promised here and delivered there.
- ← nothing. The introduction assumes only that the reader knows what an LLM-driven agent is.

**Source integration.**

- `hardy1988confused` – [1] in the draft. The confused deputy, for the sentence about authority and instruction arriving in the same envelope. Cited once, not explained; chapter 6 does the work.
- `saltzer1975protection` – [2] in the draft. Carries the closing move: the principles are fifty years old and the shortage is discipline, not ideas.
- `[PENDING: prompt-injection literature]` – the draft carries an explicit `[citation needed]` for measured false-negative rates under an adaptive adversary. Must be empirical and must not be a vendor claim. This is the single most load-bearing citation in the chapter, because the whole document's premise rests on it.

**Forward markers used in the draft** (each must resolve before the edition ships): `[ADR-01]` containment over prevention · `[A-1.1]` the trusted computing base · `[A-2.0]` the decision records, orientation · `[A-6.1]` the conformance tests for the three-part claim.

**Figures in the draft** (three, the maximum the chapter is allowed under `voice.md` §8):

- *Figure 1.1* – when each part of the claim is made true, across the life of a run. Placed after the three falsifiability paragraphs, so it summarises rather than previews.
- *Figure 1.2* – the trust boundary: what has to be correct for the claim to hold, and the unmediated path that decides whether the bound is real. This is the chapter's load-bearing schematic and the one the author asked for by name. It also introduces the document's only edge vocabulary, solid for mediated and dashed for not, in prose rather than in a legend.
- *Figure 1.3* – the intersection test as a decision tree, with three exits to the small build and one to the expensive one.

Deliberately not drawn: the architecture. Drawing it here would hand the reader the answer to Part II and they would skim it (`concept.md` §9, Evans).

**Working Quotations.** (none – the chapter cites rather than quotes, which is correct for its altitude)

**Gaps and Queries.**

- `[PENDING: adaptive-adversary detection rates]` – see above.
- `[QUERY: are the cost figures – four to six engineers for two to three quarters, 20–40 ms at p99, one engineer-day a week – defensible as stated, or should they carry a stated basis? They are the most quotable numbers in the document and currently rest on judgement.]`
- `[QUERY: does the introduction name the working title, or is the title deferral visible to the reader in edition 0.1?]`

---

## Chapter 2: What the Environment Forces On You

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Separate imposed constraints from assumed ones, so a reader in a different setting knows which parts of the design they may discard. This is the chapter that makes the rest of the document portable; without it, every mechanism reads as *what Borealis did* rather than *what follows from these constraints*.

**Argument.** Three kinds of constraint arrive at a design review wearing the same clothes. Some are genuinely imposed – the identity estate you already run, the latency a waiting human tolerates, the model vendor's interface. Some are obligations, and obligations are almost always requirements to *demonstrate* something rather than to build something in particular. The rest is convention. Teams routinely treat the second kind as the first, which produces controls that satisfy a citation and stop nothing, and treat the third kind as the second, which produces architecture by folklore.

**Beats.**

- Answer first: regulation imposes a burden of proof, not an architecture, and the distinction decides whether Appendix A is a control register or a compliance theatre script.
- The imposed set, itemised: the existing IdP and what it was designed for (humans and services, and an agent is neither); the latency budget and where it really comes from; the tools that already exist and cannot be rewritten; the model interface.
- The obligation set: what DORA, the AI Act and GDPR actually require in the specific case of an agent taking an action. Each stated as *you must be able to show X to Y within Z*.
- The move: derive requirements from obligations, never from a vendor's control catalogue `[ADR-04]`.
- Risk tiers rather than scores `[ADR-05]`. A continuous score invites negotiation at the boundary; a tier invites an argument about which tier, which is a better argument to have.
- The constraint inventory as a table – constraint, source, negotiable, what changes if it moves – and the instruction to fill it in before reading Part II.
- The political constraints, named without cynicism: who owns the gateway, who may sign a policy bundle, who is on the pager at 03:00. These decide more architecture than any of the above.

**Figures.**

- *Figure 2.1* – three sources of constraint and which of them a design review may renegotiate. Answers: when someone says *we cannot do that*, which kind of cannot is it?

**The bill.** The constraint inventory is a maintained artefact, and it goes stale at every regulatory revision and every platform migration. Budget a review per half-year and one per major change.

**Decay question.** When did we last check whether a constraint we treat as fixed still is?

**Cross-references.**

- → §2.1, §2.2: the identity estate constrains the two-chain model; the chapter states the constraint and not the design.
- → Appendix A: every requirement traces to an obligation named here.
- ← §1.1: the scope test, *a subject is in scope if a hostile model changes the answer*.

**Source integration.**

- `[PENDING: DORA articles]` – the specific provisions carrying resilience testing and ICT third-party obligations. Pin articles, not the instrument.
- `[PENDING: AI Act]` – logging and human oversight for high-risk systems. Pin articles, and note the applicability question honestly, because most agent deployments are not high-risk systems and the chapter must not imply otherwise.
- `[PENDING: GDPR]` – purpose limitation and erasure, as the two that bind hardest on memory and evidence.

**Gaps and Queries.**

- `[QUERY: how much regulatory detail belongs in the spine? The temptation is a compliance chapter. The function statement says the chapter exists to separate constraint classes, and the moment it starts summarising instruments it has failed. Proposed ceiling: one paragraph per instrument, with the mapping in Appendix A.]`
- **Resolved:** filled Borealis constraint inventory in spine (worked moment); blank template duplicated in Appendix E. Rows include incumbent PAM `[OQ-03]`, model vendor deprecation calendar `[OQ-22]`, tenancy/residency `[OQ-31]`.

**Worked moment(s).**

- Borealis constraint table excerpt: Entra for humans only; CyberArk vault already owns session recording; Guidewire API has no token exchange; OpenAI deprecation notice for `gpt-4.x` pinned 90-day migration – each row tagged imposed / obligation / convention.

---

## Chapter 3: The System in Its Landscape

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Fix vocabulary and boundary so that every later chapter can name things without redefining them. This is the chapter that pays for itself in the other seventeen.

**Argument.** The unit that matters is the run: bounded in time, tied to one principal, carrying one envelope, one budget and one evidence stream, and ending. Almost every confusion in this field comes from governing the wrong unit – authority attached to an agent that lives for months, or to a session whose boundaries are decided by a user interface. Attach it to the run and the awkward questions become answerable, starting with *what exactly are we revoking*.

**Beats.**

- Answer first: the run is the unit of authority, budget, evidence and revocation `[ADR-02]`.
- What a run is, precisely, with its five properties and its terminal states.
- The actors, named once: principal, agent, tool, system of record, platform operator, reviewer, and Kai.
- Where the boundary falls, and the size of the trusted computing base `[ADR-03]`. Chapter 1 drew this; here it is fixed as vocabulary rather than redrawn.
- The words the field uses in two senses – agent, tool, session, memory, autonomy – with one sense chosen for each and the other acknowledged, because a reader who uses the other sense needs to know we know.
- Sessions and long-lived agents as sequences of runs with explicit carry-over, and the observation that carry-over is where the interesting vulnerabilities live.
- What the C1 view adds and where it lives (Appendix B), so the reader who wants the boxes knows where they are.

**Figures.**

- *Figure 3.1* – the run lifecycle as a state machine, including the terminal states that are not *completed*. Answers: what states can a run be in, and which transitions are authorities rather than events?

**The bill.** Run granularity multiplies credential issuance, envelope derivation and evidence volume by the number of runs rather than the number of agents. For a busy triage agent that is four orders of magnitude, and it is the reason chapters 5 and 11 care about cost per run.

**Decay question.** Are there agents in production whose authority is not run-scoped, and how many?

**Cross-references.**

- → §2.1 through §2.7: every mechanism operates on a run.
- → §4.1: composition is defined as runs invoking runs, which is why the vocabulary has to be right here.
- ← §1.1: the trust boundary schematic.

**Source integration.**

- `saltzer1975protection` – the boundary and least privilege framing, cited once here and once in chapter 7. Not re-explained.
- `[PENDING: arc42 and C4 references]` – for the structural convention, cited once so that the reader recognises the shape.

**Gaps and Queries.**

- `[QUERY: does the run definition survive streaming and long-running agents that legitimately run for hours?` **Resolved `[OQ-30]`:** yes, with bounded maximum run duration as a security parameter and forced re-derivation at the boundary; per-call policy within fixed envelope ceiling `[OQ-09]`.

**Worked moment(s).**

- Marta starts `run_01J8…` at 09:04 for one claim triage; overnight batch started under `mandate:claims-nightly` at 03:00 with no human present – same agent, different second chain `[OQ-01]`. Budget counted in tool calls, not tokens `[OQ-26]`.

---

## Chapter 4: Five Moves and the Invariants They Buy

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** State the whole architecture at altitude 1 as five moves, print the invariant set once in falsifiable form, and argue the preference that generated all of it. A reader who stops at the end of this chapter can defend the shape in a design review and cannot yet implement it, which is exactly the intended state.

**Argument.** The architecture is not a component list. It is five moves, and each move converts a quantity that is unbounded into one that is bounded. Presenting it as components invites the reader to shop – to adopt the gateway and skip the evidence path – and the shape only holds because the moves compose. Presenting it as moves makes the dependencies visible and makes the omissions cost something.

**Beats.**

- Answer first: five moves, named, one line each.
- Move 1 – bind authority to a run rather than to an agent. Unbounded standing authority becomes a bounded per-run envelope.
- Move 2 – put one interface between guessing and doing. An unknown effect set becomes an enumerable one.
- Move 3 – make the record a precondition of the effect. An unknowable history becomes a provable one.
- Move 4 – decide the failure posture before the failure. Undefined behaviour under partial outage becomes declared behaviour.
- Move 5 – budget the decay. Silent degradation becomes scheduled exercise.
- The invariant set, printed once, seven rows, each falsifiable and each owned by a later chapter.
- `[ADR-01]` argued in full: containment over prevention. The alternative is stated at its strongest – detection genuinely reduces incident frequency and frequency reduction is worth money – and rejected on the ground that a false-negative rate the adversary chooses cannot appear in a safety case as though it were a design parameter.
- What the five moves do not buy, in three sentences, so that the reader arrives at chapter 21 having been warned twice.

**Figures.**

- *Figure 4.1* – the five moves and the quantity each bounds. Answers: what does each move buy, in one picture? This is the document's single most reused schematic and is the one likely to be screenshotted, which is an argument for making it good rather than for making it decorative.
- Invariants are a table, not a figure. A list of falsifiable statements gains nothing from boxes.

**The bill.** The whole shape is priced here once, at altitude 1, so that chapter 20 can assemble a build order against a number the reader has already seen. Per-mechanism cost stays in the mechanism chapters.

**Decay question.** Which invariant currently has no test?

**Cross-references.**

- → all of Part II: each move names its chapter without describing it.
- → §3.4: move 5 is the whole of the decay chapter.
- ← §1.3, §1.4 (chapter 3's vocabulary; the constraint classes).

**Source integration.**

- `[PENDING: capability-security literature]` – for move 1, one canonical source rather than four.
- `saltzer1975protection` – complete mediation for move 2, economy of mechanism for the size of the trusted computing base.
- `[PENDING: adaptive-adversary detection rates]` – the same source that chapter 1 needs, used here to carry weight rather than to open a chapter.

**Worked moment(s).**

- Borealis post-incident review: eleven action items; two wrong (harder system prompt, raise classifier threshold) – hygiene measures written into assurance slide as controls.

**Gaps and Queries.**

- `[QUERY: five moves or four? Move 5 is operational discipline rather than architecture, and a reviewer may say it does not belong in a solution strategy. Counter-argument: it is the only move that determines whether the other four are still true in month fourteen, and demoting it to Part III is precisely the mistake the field keeps making. Decide before drafting, because the figure depends on it.]`

---

# Part II. The Mechanisms

## Chapter 5: Identity and Binding

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Derive the two-chain identity model and sender-constrained run credentials from a single measured quantity: the interval between a credential being stolen and being used.

**Argument.** Short credential lifetimes shrink the theft window and do not close it, because in the agent case the attacker is already inside the window. A prompt-injected agent uses the credential in-band, in the same second, through the legitimate code path. The property that has to change is not lifetime but sufficiency: possession of the credential must stop being enough, so that a credential lifted from one workload is unusable from another.

**Invariant.** Contributes to I2. A credential presented from a workload other than the one it was issued to is refused, and the refusal is recorded.

**Beats.**

- Answer first: two chains, joined per run, and possession stops being sufficient.
- The promise: short-lived tokens, rotated automatically, are the modern answer to credential theft, and for human and service traffic they largely are.
- The failure: theft-to-use is not measured in hours here. The agent is the exfiltration path and the usage path at once.
- What short lifetimes still buy – persistence cost, a bounded replay interval, and a much better story after the fact. This is not a discarded idea; it is a necessary and insufficient one.
- The two chains: workload identity (what is executing) and human principal (on whose behalf), and why collapsing them breaks either the audit question or the entitlement question, depending on which one you collapse into.
- Binding them: the run credential, its claims, its audience, its proof-of-possession. Artefact in Appendix D, summarised here in six fields.
- The broker `[ADR-08]`, and the honest cost: a new component on the run-start path, with a fail posture that chapter 14 has to answer.
- Sender constraint in practice `[ADR-07]`: what mTLS binding costs an organisation that has never run it, and what the alternative costs.

**Decisions anchored.** `[ADR-06]` two chains, against a single agent identity acting for itself. `[ADR-07]` sender-constrained credentials, against short-lived bearer tokens alone. `[ADR-08]` token exchange at a broker, against direct per-tool grants from the identity provider.

**Figures.**

- *Figure 5.1* – sequence: the two chains joining at run start, and the audience binding that makes the resulting credential useless elsewhere. Answers: what exactly is bound to what, and at what moment?

**The bill.** Key material per workload and the rotation machinery to go with it. A broker call on the run-start path, single-digit milliseconds if it is close and much worse if it is not. An operational competence in mTLS or DPoP that many organisations do not currently have, which is a hiring and training cost rather than an engineering one, and therefore slower.

**Decay question.** How many run credentials issued last month were bearer-only, and under what exception?

**Cross-references.**

- → §2.2: the credential carries the envelope reference; the envelope's derivation is not this chapter's business.
- → §3.2: the broker's fail posture.
- ← §1.3: the run and its principal.

**Source integration.**

- `[PENDING: RFC 8705]` mutual-TLS client authentication and certificate-bound access tokens.
- `[PENDING: RFC 9449]` DPoP.
- `[PENDING: RFC 8693]` token exchange.
- `[PENDING: incident material]` on credential theft from agent and CI contexts, if any is publishable. If none is, say so; the absence is itself worth a sentence.

**Gaps and Queries.**

- `[QUERY: DPoP or mTLS as the recommended default?]` Unchanged – conditional ADR.
- **Resolved `[OQ-01]`:** standing mandate artefact for unattended runs; schema in Appendix D.
- **Resolved `[OQ-03]`:** integrate incumbent PAM for vault/session recording; elevation is always a new run.

**Worked moment(s).**

- Kai steals a run credential via prompt injection; uses it in the same second through the legitimate path – lifetime rotation irrelevant. Contrast: 03:00 batch derives envelope against `mandate:claims-nightly` signed by Marta last quarter, not against a live human.

---

## Chapter 6: The Envelope

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Establish per-run authority as a derived, intersected, attenuation-only object, and resolve the confused deputy properly rather than by exhortation.

**Argument.** An agent's role is the union of everything it might ever need, so role-based authority means every run carries the maximum. The envelope replaces that union with an intersection computed at run start: what this task declares it needs, what this principal can reach, and what this risk tier permits. Delegation then only narrows, and it only narrows because widening is not a representable operation – not because a policy forbids it. A rule that can be violated by a bug is not an invariant.

**Invariant.** I2 and I3. No call carries authority beyond the envelope in force at the moment of the call, and no delegation widens authority.

**Beats.**

- Answer first: authority is derived per run as an intersection, and it can only ever shrink.
- The promise: give the agent a role, scope the role tightly, review it quarterly. This is good practice and it is how the rest of the estate works.
- The failure: the role is a union over tasks, the tasks are added faster than they are removed, and the quarterly review is a list nobody can evaluate. Show the arithmetic on `claims-triage`.
- The intersection `[ADR-09]`: three inputs, three owners – the team declares need, the identity estate supplies reach, the tier supplies the ceiling. Note that the three owners disagreeing is the mechanism working.
- Attenuation by construction `[ADR-10]`: the capability tradition's actual contribution, which is that the widening operation does not exist. Hardy's deputy, resolved: authority and instruction stop sharing an envelope because the authority is no longer something the instruction can name.
- Allow-list of typed operations `[ADR-11]`, and the uncomfortable consequence: a new operation cannot be used the day it ships. That is the cost, it is real, and chapter 17 is about making it small rather than pretending it is not there.
- What happens when a run genuinely needs more: it does not get more. It ends, and a new run is derived, and a human sees the delta. Argue why this is better than expansion even though it is worse for throughput.
- Artefact: the envelope, its fields, its lifetime, its reference in the credential.

**Decisions anchored.** `[ADR-09]`, `[ADR-10]`, `[ADR-11]`.

**Figures.**

- *Figure 6.1* – the three inputs and the intersection, with the owner of each input named on the edge. Answers: who decides what an agent may do? Three parties, and none of them alone.
- *Figure 6.2* – attenuation across a delegation chain, showing the envelope shrinking at each hop and the operation that would widen it marked as absent.

**The bill.** Envelope derivation on the run-start path. A declared-need artefact per agent task, which somebody has to write and keep true, and which will be wrong in both directions in the first quarter. Developer friction concentrated at exactly the moment a developer is trying to ship, which is the worst possible moment and the reason chapter 17 exists.

**Decay question.** What fraction of derived envelopes sit within ten per cent of the tier ceiling? A rising fraction means need declarations have become copies of the ceiling, and the intersection has quietly become a constant.

**Cross-references.**

- → §4.1: attenuation is the invariant that survives composition, and this is where it is established.
- → §2.5: the envelope bounds what an approval can be about.
- ← §2.1: the credential that carries the envelope reference.

**Source integration.**

- `hardy1988confused` – the second and final citation. Here it does work rather than setting a tone.
- `[PENDING: capability-security literature]` – one canonical source for attenuation and the object-capability model.
- `saltzer1975protection` – least privilege, cited as the principle this mechanism operationalises.

**Gaps and Queries.**

- `[QUERY: is "envelope" the right name?]` Unchanged – glossary decision.
- **Resolved `[OQ-09]`:** envelope is upper bound at derivation; policy checks per call within it. **Resolved `[OQ-17]`:** declared need is static manifest field; promotes I8.

**Worked moment(s).**

- `claims-triage` role carries 47 tool permissions; manifest declared need lists 6; intersection with Marta's reach yields 4 operations for `run_01J8…`. Kai's attack used only permitted tools with hostile arguments – union arithmetic would have allowed 47 `[PENDING: worked derivation]` → Appendix E.2.

---

## Chapter 7: Complete Mediation

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Convert complete mediation from an adjective into a published number, and establish that the denominator is discovered paths rather than designed ones.

**Argument.** Every governance story ends with somebody finding the road nobody was watching. Mediation is therefore not a property you assert in a design document; it is a coverage ratio you measure against the paths you have found, publish, and watch move. The first measurement is embarrassing in every organisation that has taken it, and the ones that have not taken it are not doing better – they are reporting an unmeasured hundred per cent.

**Invariant.** I1. No effect leaves the platform except through a mediated call, and the coverage number is the honest statement of how true that currently is.

**Beats.**

- Answer first: coverage is a number, it is published, and the denominator is what you found rather than what you drew.
- The principle, at its source, and why it is the least glamorous and most frequently lost of Saltzer and Schroeder's eight.
- How paths escape, itemised from experience: the sidecar added in March, the developer laptop holding a production credential, the legacy service account, the batch job someone reused because it already had access, the direct SDK call inside a service that also hosts an agent.
- Discovery as a continuous function rather than a project: egress telemetry, credential usage attribution, dependency and code scanning, and the reconciliation between what the registry says exists and what the network says is talking.
- `[ADR-13]` federated gateways with centralised policy, against a single central gateway. The rejection is on latency, blast radius and organisational reality, and the cost is that policy distribution becomes a hot-path concern, which chapter 13 pays for.
- Publishing the number `[ADR-12]`, and the governance consequence: once it is on a slide, it becomes a target, and a targeted coverage number is gamed by narrowing the denominator. The counter-measure is that discovery is owned by someone who does not own coverage.
- What to do with an unmediated path you cannot close this quarter: it is a risk acceptance with an owner and a date, recorded in the same register as everything else, and it is not a secret.

**Decisions anchored.** `[ADR-12]`, `[ADR-13]`.

**Figures.**

- *Figure 7.1* – the coverage loop: discovered paths, mediated paths, residual, and the feedback edge from discovery. Answers: what is the number a ratio of, and what moves it?

**The bill.** Discovery tooling and, more expensively, the standing attention to run it. A gateway per domain rather than one, with the operational multiplication that implies. And a political cost that is easy to underestimate: publishing a number that starts at sixty per cent requires an organisation that can look at sixty per cent without punishing the person who measured it.

**Decay question.** What is this quarter's coverage number, is the denominator larger than last quarter's, and who read it?

**Cross-references.**

- → §2.4: mediation says every call goes through one interface; the next chapter is about what that interface actually is.
- → §3.5: coverage falls when the sanctioned path is slower than the shortcut. The causal link is stated here and the remedy is there.
- ← §1.1: the dashed line in the trust-boundary schematic is this chapter's subject.

**Source integration.**

- `saltzer1975protection` – complete mediation, the primary citation of the chapter.
- `[PENDING: empirical material on shadow integration rates]` – if published data exists on unmediated paths in enterprises, it belongs here. If it does not, the chapter says so and offers the measurement method instead, which is the more useful contribution anyway.

**Gaps and Queries.**

- `[QUERY: is there a defensible target coverage, or is the honest answer only "measured, published, and rising"?]` Unchanged.
- **Resolved `[OQ-12]`:** developer MCP connector config on laptop counts in discovery; enforcement cited to endpoint management, not designed here.

**Worked moment(s).**

- First Borealis coverage audit: 94% mediated by weight; Kai's path was a Cursor MCP config pointing at production Guidewire – discovered, not designed. Second dimension: hybrid gateway custody per tool `[OQ-04]`.

---

## Chapter 8: The Seam

**Status:** [DRAFTED] – first draft written 2026-08-01. Seam chapter; written to survive the protocol improving.

**Function.** Establish that the transition from non-deterministic to deterministic compute is the only governable moment in the system; show that a tool protocol's real contribution is standardising *where* that transition happens, which is what makes coverage measurable at all; then separate what the protocol carries today from what the platform carries on its behalf, and state the six properties the protocol would need before the seam could itself be the governance layer.

**Argument.** You cannot govern inference. There is no inspectable intermediate state, no stable pre-image of a decision, nothing to attach a rule to. What you can govern is the instant at which the non-deterministic side has to hand something to the deterministic side in a form the deterministic side can parse – a structured call, with a name and typed arguments. That instant is the seam, and it is the only place in the entire system where a decision can be made at all. Before a common protocol, the seam existed but was implicit and differently shaped in every framework and every integration, which is precisely why coverage was structurally impossible: you cannot count instances of a boundary that has no name. The Model Context Protocol's contribution is not security. It is that it *locates the seam*, identically, in a schema, across tools written by people who have never met. That is a governance precondition, and it is worth saying clearly because it is the strongest available argument for adopting it.

And then the honest half. The protocol as it currently stands carries plumbing semantics, not authority semantics. There is no per-run authority reference, no attenuation, no possession binding of the caller, no declared side-effect class, no idempotency contract, and no standard refusal shape. Tool descriptions – the text the protocol exists to distribute – are attacker-reachable input that flows directly into the model's context, which makes the protocol's own metadata channel an injection surface. So today the seam is where you *place* a control; it is not itself a control. Adopting the protocol and calling it governance is mistaking a socket for a fuse.

**Invariant.** Contributes to I1, and adds the chapter's own: every transition from non-deterministic to deterministic compute passes through one interface whose schema the platform controls, and no authority is derived from anything the non-deterministic side asserted about itself.

**Beats.**

- Answer first: the seam is the only governable moment, and the protocol's contribution is that it tells you where the seam is. It does not tell you what to do there.
- Why inference is ungovernable, in one short passage and without a detour into interpretability. The point is structural, not a claim about the state of the art: a rule needs an object, and there is no object until a call is emitted.
- What the seam looked like before a shared protocol: per-framework function calling, bespoke glue per integration, and the consequence that chapter 7's coverage number had no stable denominator. Name this as the real cost of the pre-protocol era, because it is the cost readers have not usually priced.
- What the protocol actually provides, stated fairly and pinned to a named revision: a schema for tools and calls, a discovery mechanism, transports, and a shared result shape. Show a real tool call artefact.
- What it does not provide. Six items, each in a sentence, each with the compensating mechanism the platform performs today: per-call authority reference; attenuation semantics; possession binding; declared side-effect class and idempotency key; signed manifests with provenance; a standard refusal shape.
- The three fixes the reader is already reaching for, killed by name and with respect. *Put the policy in the server* – then policy lives in the least trusted, most numerous, most frequently third-party component, and coverage becomes the number of servers you audited. *Trust the tool description* – it is attacker-reachable text with a supply chain behind it `[ADR-15]`. *Use the protocol's own authorisation story as the authority model* – it answers whether a client may connect to a server, which is a different question from whether this run may perform this operation on this object right now.
- The move `[ADR-14]`: the gateway speaks the protocol on both sides. It is a server to the agent and a client to the real servers, it is the only component holding authority, and the agent never sees a credential. This is the chapter's whole design content and it fits in a paragraph, which is a good sign.
- Making the metadata channel safe: manifests pinned and signed, sourced from an internal registry rather than discovered at runtime `[ADR-16]`; description hashes recorded and re-verified per run; a declared side-effect class per operation, supplied at onboarding rather than inferred from the name `[ADR-17]`.
- The limit, stated here rather than deferred: all of this assumes the far side of the seam is deterministic. When the far side is another agent, the seam stops being a boundary between kinds of compute and becomes a boundary between two non-deterministic systems, and the guarantees do not survive it. That case has its own chapter `[→ §4.1]`.
- What would have to change in the protocol for the seam to become the governance layer rather than its location. The same six properties, restated as a wish list with a revisit trigger attached to each, so that the ADR expires against the protocol's roadmap rather than against the author's attention span.

**Decisions anchored.** `[ADR-14]` adopt the protocol as the seam and keep authority in the gateway, against both a proprietary internal calling convention and waiting for the protocol to grow authority semantics. `[ADR-15]` tool descriptions as untrusted data with provenance, against treating registered metadata as trusted configuration. `[ADR-16]` pinned signed manifests from an internal registry, against runtime discovery from external registries. `[ADR-17]` declared side-effect class per operation, against inferring reversibility from the operation name.

**Figures.**

- *Figure 8.1* – the seam itself: non-deterministic compute above, deterministic below, and the single typed interface between them, with the annotation that everything above is unverifiable and everything below is inspectable. Answers: where is the only place a rule can attach? This figure is the chapter's thesis and should be the simplest drawing in the document.
- *Figure 8.2* – the gateway as server-and-client: what the agent sees, what the real server sees, and where the credential lives. Answers: if the agent never holds a credential, how does the call get authorised?
- *Figure 8.3* – the metadata channel as an attack path: registry to manifest to description to model context to emitted call. Answers: how does a tool description become an instruction? Only draw this if the prose cannot carry it; three figures is the ceiling and this is the most cuttable of the three.

**The bill.** An extra hop on every tool call – single-digit milliseconds if the gateway is co-located, worse if it is not, and it is additive to the decision path in chapter 13 rather than parallel to it. A registry to build and operate, with signing infrastructure behind it. Onboarding friction per tool, including a side-effect declaration somebody has to think about. And the loss of runtime discovery, which is the feature developers most like about the protocol and the one this design deliberately removes – say so plainly rather than burying it, because a reader who discovers it in implementation will trust the rest of the document less.

**Decay question.** How many tool servers are reachable from an agent runtime without a corresponding pinned registry entry, and how many description hashes have drifted since onboarding?

**Cross-references.**

- → §2.5: the frozen artefact that gets approved is a call at this interface, which is why hash-binding is possible at all.
- → §2.7: every call at the seam is an evidence event; the seam is why the evidence stream has a stable schema.
- → §4.1: the limit case where the far side is non-deterministic.
- ← §2.3: mediation is the principle, the seam is where it physically happens. This chapter must not re-argue coverage.
- ← §2.2: the gateway injects the envelope; it does not derive it.

**Source integration.**

- `[PENDING: MCP specification]` – pinned revision and retrieval date, per `voice.md` §5. Every claim about what the protocol does or does not carry is checked against that revision on the day the chapter is copy-edited, and the chapter carries a dated sentence saying so.
- `[PENDING: MCP authorisation specification]` – cited specifically where the chapter distinguishes connection authorisation from operation authorisation. This must be scrupulously fair; the specification is not wrong, it answers a different question, and the chapter's credibility depends on not misrepresenting it.
- `[PENDING: published MCP vulnerabilities and research]` – tool poisoning, description injection, transport and session weaknesses, malicious or typosquatted servers. Prefer reproducible research over vendor advisories. This is the evidence base for `[ADR-15]` and `[ADR-16]` and without it those records are opinion.
- `hardy1988confused` – not cited again here. The deputy is chapter 6's, and repeating it would dilute it.
- `saltzer1975protection` – economy of mechanism, cited once for the argument that the gateway is small on purpose.

**Gaps and Queries.**

- `[QUERY: placement. This chapter currently follows complete mediation, on the argument that mediation is the principle and the seam is its physical location. The alternative is to open Part II with it, since identity and envelope both presuppose that a call boundary exists. Test: draft chapter 5's opening paragraph and see whether it needs a forward reference to survive. If it does, move this chapter to 5.]`
- `[QUERY: how much of this chapter is about MCP specifically versus about the seam as a concept? The title says seam, which protects the argument against the protocol being replaced. But a reader searching for "MCP" needs to find it. Proposed resolution: the concept owns the chapter, the protocol owns two named sections, and the running head says seam. Confirm before drafting.]`
- `[QUERY: does the six-property wish list read as constructive or as a complaint? It is the most quotable passage in the chapter and the one most likely to be extracted without context. Draft it as specification requests with rationale, not as gaps, and make each one implementable by someone reading it.]`
- `[PENDING: a real tool call artefact]` – the `claims-triage` call to `tool:claims-core/post-adjustment`, valid against the pinned schema, with the gateway's injected fields marked. Appendix D holds the schema; this chapter shows one instance and nothing more.
- `[QUERY: the protocol is under active revision...]` Unchanged.
- **Resolved `[OQ-10]`:** elicitation never forwarded; sampling only under declared manifest capability with quarantine. **Resolved `[OQ-11]`:** extend untrusted-data treatment to all server payloads. **Resolved `[OQ-13]`:** browser automation out of scope above reversibility line. **Resolved `[OQ-14]`:** submit six-property list to MCP venue.

**Worked moment(s).**

- German instruction embedded in claim note; injection classifier scores 0.31; gateway terminates elicitation request from third-party MCP server; sampling blocked unless manifest declares capability `[OQ-10]`.

---

## Chapter 9: Approval and Effect Integrity

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Distinguish an approval that is a control from one that is theatre, and establish that what was approved and what was executed have to be the same object rather than two renderings of the same intention.

**Argument.** Human approval fails in two independent ways and most designs address neither. It fails on integrity, when the human approves a summary and the system executes a payload that the summary described loosely – or when the payload is regenerated after approval and is no longer the object that was seen. And it fails on attention, when the gate is the fourteenth of the morning and the approval rate is 99.4 per cent with a four-second median. The first is fixed by freezing and hashing. The second cannot be fixed by exhortation, only by measurement followed by removal, because a gate nobody reads manufactures confidence without supplying control.

**Invariant.** I5. The object approved and the object executed are the same object, verified by hash at execution time.

**Beats.**

- Answer first: freeze, hash, bind, execute – and measure the gate, because an unread gate is worse than no gate.
- The promise: a human in the loop for consequential actions. This is the control every risk committee asks for and it is not a foolish request.
- The first failure, integrity: what was rendered and what will execute are different objects, and the gap between them is where the interesting attack lives. Show it on a payment adjustment where the summary is faithful and the payload is not.
- Propose-then-execute `[ADR-18]`: the call is frozen at the seam, hashed, and the approval record references the hash. Regeneration voids the approval, because the hash no longer matches, and that is a mechanical fact rather than a rule.
- What the human is actually shown: the effect class from `[ADR-17]`, the irreversibility, the diff against current state, and the budget consumed. Not the prompt, and not the model's explanation of itself, which is the most persuasive and least evidential thing on the screen.
- The second failure, attention. The measurements that reveal it: time-to-decision distribution, approval rate, and whether the detail view was ever opened.
- The consequence `[ADR-19]`: a gate that fails its measurement is removed and the action is demoted to a tier that does not require it, or the gate is fixed. Keeping both the gate and its failure is the option that is not available, and it is the one most organisations choose.
- The approval record as evidence, and what it has to contain to answer *who authorised this* eighteen months later.

**Decisions anchored.** `[ADR-18]`, `[ADR-19]`.

**Figures.**

- *Figure 9.1* – sequence: propose, freeze, hash, approve, verify, execute, with the hash carried on every edge and the void path shown. Answers: what makes regeneration impossible to hide?

**The bill.** A human in the loop is latency measured in minutes and a throughput ceiling measured in humans. The approval interface becomes a security component, which means it needs the review, the testing and the on-call that security components get, and it is usually built by a team that does not know that yet.

**Decay question.** What is the median time-to-decision on each gate, and has it fallen since launch? A falling median with a rising volume is the shape of a gate becoming a formality.

**Cross-references.**

- → §2.7: the approval record is an evidence event and inherits its integrity properties.
- → §3.4: approval decay is one of the named decay modes and is measured on the same dashboard.
- ← §2.4: the frozen object is a call at the seam.
- ← §2.2: an approval can only be about something the envelope already permits. Approval does not grant authority; it consumes it.

**Source integration.**

- `[PENDING: automation bias and vigilance literature]` – aviation and clinical decision support both have decades of it, and it is the strongest available evidence that the attention failure is structural rather than cultural. This is the citation that keeps the chapter from sounding like an opinion about lazy colleagues.
- `[PENDING: measured approval-fatigue data]` – from any deployed system, ideally not this field. If none is available, the chapter proposes the measurement rather than asserting the result.

**Gaps and Queries.**

- `[QUERY: is "approval does not grant authority, it consumes it" defensible in all cases, or are there legitimate designs where a human approval genuinely extends the envelope for one call? Instinct says extension should be a new run with a new derivation. Confirm, because it is a strong claim and a reviewer will find the edge case.]`

---

## Chapter 10: Data, Retrieval and Memory

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Treat memory as the writable, adversary-reachable data system it actually is, and derive principal-aware retrieval, provenance and purpose binding from one property: externally sourced content is indistinguishable from authored content unless the platform makes it distinguishable.

**Argument.** Retrieval is usually built for quality and then inherits its security properties by accident. Two accidents matter. If retrieval runs under the agent's service identity, the agent is a lateral-movement engine that answers questions its principal has no right to ask, politely and at scale. And if stored content carries no provenance, then a paragraph an attacker wrote into a claim document two sessions ago is, at retrieval time, exactly as authoritative as a policy the organisation authored. Memory is not a cache. It is a writable store with an adversarial write path, and it is the only component in the system where an attack can wait.

**Invariant.** Content that entered from outside the trust boundary is distinguishable from content the principal authored, at every point where it can influence an action.

**Beats.**

- Answer first: retrieve under the principal, store with provenance, and quarantine what came from outside.
- The promise: retrieval grounds the model and reduces fabrication, which is true and is why everyone has it.
- The first failure: entitlements. Retrieval under the agent's identity, with a corpus assembled for coverage, and the resulting query that returns a document the principal could never have opened `[ADR-20]`.
- The second failure: provenance. The two-sessions-ago injection, told as a mechanism rather than a scene. This is the attack that most distinguishes agent systems from everything before them, because the write and the exploitation are separated in time and in principal.
- Memory as a first-class data system `[ADR-21]`: schema, retention, classification, provenance on every item, and a quarantine tier whose contents can inform but cannot instruct.
- Purpose binding, which arrives as a data-protection obligation from chapter 2 and turns out to be the control that limits blast radius across tasks. Note the coincidence honestly rather than claiming regulatory foresight.
- The classification ceiling per run, derived from the tier, and what happens when a retrieval would exceed it.
- The cost nobody mentions: partitioning an index by entitlement hurts recall, and the product team will notice before security does.

**Decisions anchored.** `[ADR-20]`, `[ADR-21]`.

**Figures.**

- *Figure 10.1* – the path an external document takes into memory and out again: ingestion, provenance stamp, quarantine tier, retrieval under principal, and the boundary it may not cross. Answers: at which point does something an attacker wrote become something the agent acts on?

**The bill.** Index partitioning by entitlement, with the recall cost that implies and the storage cost of maintaining per-principal views. Provenance metadata on every item, forever. And a retrieval path that now has to resolve entitlements in the hot path, which is a second staleness budget for chapter 13 to manage.

**Decay question.** What fraction of items in memory lack provenance, and is it rising? An unprovenanced item is not a gap in metadata; it is content whose trust level is unknown and is therefore being treated as trusted.

**Cross-references.**

- → §2.7: retrieval events are evidence, and the *what did it read* question is asked as often as *what did it do*.
- → §3.1: entitlement resolution in the hot path.
- ← §1.2: purpose limitation as an imposed obligation.
- ← §1.3: the run's principal, which is the identity retrieval runs under.

**Source integration.**

- `[PENDING: GDPR purpose limitation and storage limitation]` – pinned articles, from chapter 2's mapping rather than re-derived.
- `[PENDING: memory-poisoning and RAG-injection research]` – reproducible work preferred. This is the evidence base for the quarantine tier.
- `[QUERY: is there published work on entitlement-aware retrieval at enterprise scale, or is this an area where the document is ahead of the literature? If the latter, say so; an admitted gap is worth more than a weak citation.]`

**Gaps and Queries.**

- `[QUERY: does the quarantine tier survive contact with usefulness?]` Partially resolved: seam enforcement for tier-2 sole justification; cross-context memory `[OQ-15]`–`[OQ-16]`; cache prefix isolation `[OQ-27]`.

**Worked moment(s).**

- Session 1: Kai embeds instruction in claim document; session 3: Marta's run retrieves it with valid entitlement – write and exploit separated by time. Org-scoped memory holds platform-authored content only; derived facts stay principal-scoped `[OQ-16]`.

---

## Chapter 11: Evidence

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Resolve the apparent contradiction between records that must be tamper-evident forever and personal data that must be erasable on request, and price an evidence path that gates execution rather than trailing it.

**Argument.** Two requirements look incompatible and are not. Keep the chain and destroy the key: hash-chain the event metadata so the sequence is verifiable, encrypt the content under a per-subject key, and satisfy erasure by destroying the key rather than the record. The chain still verifies with the content gone, which is the property that makes the whole arrangement work. The harder decision is ordering. If the record is written after the effect, then the failure mode is an action with no evidence, which is precisely the state the document exists to prevent. The record is therefore a precondition, and that costs latency in the hot path.

**Invariant.** I4. No side effect occurs without a durable, tamper-evident record written first.

**Beats.**

- Answer first: keep the chain, destroy the key – and write before you act.
- The apparent contradiction, stated at full strength, because a reader who has fought this argument with a data-protection officer needs to see it taken seriously.
- The construction: hash chain over metadata, content encrypted per subject, erasure by key destruction, chain verifiable without content `[ADR-22]`.
- What an evidence record has to contain to answer the four questions actually asked eighteen months later: what happened, under whose authority, on whose behalf, and what did the platform know at the time.
- Ordering `[ADR-23]`: no evidence, no side effects. The cost, honestly – a durable write in the hot path, or a bounded queue with a stated and accepted loss window, which is a real alternative with a real number attached rather than a compromise to be embarrassed about.
- Verification: who verifies the chain, how often, and what a verification failure means operationally at 03:00. A verification job with no runbook is a compliance artefact.
- What evidence does not buy: it is not prevention, it does not shorten an incident, and its value is realised entirely in a conversation that may never happen. Say this, because it is the control most likely to be cut, and the argument for keeping it has to be honest about when it pays.

**Decisions anchored.** `[ADR-22]`, `[ADR-23]`.

**Figures.**

- *Figure 11.1* – the chain with per-subject content keys, and the same chain after an erasure, still verifying. Answers: how can a record be both immutable and erased?

**The bill.** A durable write on the effect path, which is the single largest latency item in the document after the decision path. Storage that grows with runs rather than with users. Key management per data subject, which is an operational commitment few teams have made before. And a verification job that produces nothing anyone wants until the day it produces everything.

**Decay question.** When was the chain last verified end to end, by whom, and did anyone read the result?

**Cross-references.**

- → §3.2: the one fail posture that is not negotiable is this chapter's ordering rule.
- → §4.1: evidence chains across composed runs by parent identifier, and it is one of only two things that compose.
- ← §2.4: every call at the seam is an evidence event with a stable schema.
- ← §1.2: the erasure and retention obligations, already mapped.

**Source integration.**

- `[PENDING: GDPR Art. 17 and the crypto-shredding position]` – including, honestly, the fact that key destruction as erasure is a defensible position rather than a settled one. If supervisory opinion is mixed, say so; the document loses nothing and gains a reader who has had the same argument.
- `[PENDING: DORA record-keeping obligations]` – from chapter 2's mapping.
- `[PENDING: tamper-evident logging literature]` – one canonical source for hash chaining, not a survey.

**Gaps and Queries.**

- `[QUERY: is crypto-shredding defensible...]` Unchanged – jurisdictional check.
- **Resolved `[OQ-18]`/`[OQ-28]`:** retrieval reference + content hash; tier-dependent full-context hash above reversibility line. **Resolved `[OQ-29]`:** effects are evidence; model reasoning is not.

**Worked moment(s).**

- Payment adjustment refused at seam until evidence write ack returns; supervisor query eighteen months later gets hash chain + retrieval refs, not reproducible model rationale. One subject erasure: key destroyed, chain verifies, content gone.

---

# Part III. Operating It

## Chapter 12: The Agent Manifest

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Define the deployable unit the rest of Part III assumes: what an agent version is, what it binds together, and how it is signed, promoted, evaluated and pinned – so that chapter 15 can quarantine something real and chapter 16 can recertify something enumerable.

**Argument.** Three mechanisms already assume an artefact nobody has named: declared need in chapter 6, pinned tool bindings in chapter 8, and version quarantine in chapter 15. Without a signed manifest that binds prompt hash, tool references, declared need, policy references, allowed model set and delegation graph, every control in Part II attaches to something the organisation cannot name, diff or roll back. Instructions change effective behaviour without touching the envelope; model routing changes the safety case silently; the manifest is where those changes become visible.

**Invariant.** Contributes to I8. The declared need in the manifest in production is the declared need used at derivation; the manifest hash in the run credential matches the promoted artefact.

**Beats.**

- Answer first: one signed manifest per agent version, promoted through environments, evaluated before promotion.
- The promise: prompts live in a product tool, policy in a repo, tools in a registry – separate lifecycles, one binding object.
- The failure: chapter 14 quarantines `claims-triage@4.2.1` but nobody can say what 4.2.1 contained; instruction diff widened behaviour while the envelope stayed constant `[OQ-19]`, `[OQ-20]`.
- Manifest fields: prompt content hash, tool manifest refs, declared need, policy bundle ref, allowed model set per tier, delegation graph for sub-agents, owner, promotion path.
- Standing mandate reference for unattended variants `[OQ-01]`; model version pin and revalidation on change `[OQ-22]`; allowed model set as tier property `[OQ-24]`.
- Deployment gate: red-team suite with tier threshold; override logged with mandatory review `[OQ-21]`.
- Relationship to chapter 6: envelope intersects manifest declared need; derivation reads manifest, not memory `[OQ-17]`, `[OQ-09]`.

**Worked moment(s).**

- Borealis promotes `claims-triage` manifest v2.3.1: prompt hash changes one sentence; eval suite refusal rate drops from 99.1% to 97.8%; tier-2 gate blocks promotion until a human signs the delta.
- Delegation graph declares one research sub-agent; platform derives child envelope at spawn – parent never holds meta-authority `[OQ-25]`.

**Decisions anchored.** `[ADR-37]` signed agent manifest as the deployable unit (new). `[ADR-38]` allowed model set in envelope (new). Extends `[ADR-16]` pinning to the agent–tool binding.

**Figures.**

- *Figure 12.1* – manifest composition and promotion path: dev → signed → evaluated → prod. Answers: what exactly is versioned when we say an agent version?

**The bill.** A promotion pipeline with signing, evaluation and rollback. Behavioural eval infrastructure per tier. Owner accountability for manifest drift. Revalidation cost on every model vendor deprecation.

**Decay question.** How many production runs last month used a manifest hash that does not match the promoted artefact in the registry?

**Cross-references.**

- → §2.2: declared need originates here.
- → §3.5: paved road must make manifest promotion faster than shortcut deployment.
- ← §2.7: evidence references manifest hash on every run.
- ← `[OQ-19]`–`[OQ-24]` resolutions in `open-questions.md`.

**Source integration.**

- `[PENDING: agent red-team suites and reported refusal rates]` – preprints only, for OQ-21 threshold argument.

**Gaps and Queries.**

- `[PENDING: mandate and manifest schemas in Appendix D]` – mandate artefact from OQ-01 joins manifest family.

---

## Chapter 13: Governance in the Hot Path

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Engineer the decision path as the latency-critical component it is, and make every input's tolerable staleness an explicit security statement rather than an accident of caching.

**Argument.** A decision path that adds two hundred milliseconds will be removed, and it will be removed by well-meaning engineers under delivery pressure who will describe it as an optimisation. Governance in the hot path therefore has a performance budget like anything else on the critical path. Meeting it means evaluating locally against a distributed bundle, and that immediately raises the question the design must answer explicitly: how old may each input be? Every cached input is a window in which the platform enforces a decision that is no longer true, and the length of that window is a number the design chooses rather than inherits.

**Beats.**

- Answer first: evaluate locally, distribute signed bundles, and declare a staleness budget per input.
- The latency budget, split: what the seam costs, what the decision costs, what the evidence write costs, and what is left for the work the user is waiting for.
- `[ADR-24]` embedded evaluation with signed bundles, against a policy service call per decision. The rejected option is genuinely better on freshness and that is why it is tempting.
- Staleness budgets, one per input: policy bundle, entitlements, revocation state, budget counters. Each has a different tolerable age and each age is a sentence about what the platform is willing to get wrong.
- Revocation as the exception. Its budget is the interval in the claim from chapter 1, which means it is the one input that cannot be handled by ordinary cache expiry.
- What may never be cached, and why the list is short and absolute.
- Measurement: the bundle propagation distribution, not its average, because the average is fine and the tail is the security property.

**Decisions anchored.** `[ADR-24]`.

**Figures.**

- *Figure 12.1* – the decision path with each input and its declared staleness budget on the edge. Answers: when this permits a call, how old is the information it permitted it on?

**The bill.** Twenty to forty milliseconds at p99 on every mediated call, most of it here. A bundle build, sign and distribute pipeline, which is a supply chain of its own and needs the same treatment chapter 8 gives tool manifests. And a permanent tension with the team that owns the user-facing latency target.

**Decay question.** What is the actual p99 bundle propagation time, when was it last measured rather than assumed, and does it still fit inside the declared budget?

**Cross-references.**

- → §3.3: revocation's interval is claimed here and drilled there.
- ← §2.4, §2.6: the seam and retrieval both add hot-path cost, and the budget here is the whole of it.
- ← §1.1: the stated interval in the claim.

**Source integration.**

- `[PENDING: policy-as-code and distributed authorisation practice]` – dated vendor and open-source documentation, because this is a claim about what is buildable today.

**Gaps and Queries.**

- `[QUERY: the 20–40 ms figure appears in chapter 1 and is defended here. It needs a stated basis – measured where, on what, with what policy complexity – or it needs to become a range with an explicit "in our setting". It is the number most likely to be quoted back.]`

---

## Chapter 14: The Outage You Decide in Advance

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Force the fail-posture matrix into a design review rather than an incident, and defend the single row that is not negotiable.

**Argument.** Fail-closed everywhere is a self-inflicted denial of service that the business will overrule during the first outage, usually verbally, usually at night, and usually without a record. Fail-open is negligence with extra steps. The answer is neither a principle nor a preference: it is a matrix, dependency by tier, decided while everyone is calm, signed by someone who can be named afterwards. One row does not vary. If evidence cannot be written, effects do not happen, because the alternative is a period of unrecorded action, which is the exact state the document exists to make impossible.

**Beats.**

- Answer first: the matrix, decided in advance, signed, and rehearsed.
- Why the uniform answers both fail, each argued at its strongest before it is rejected.
- The matrix itself: each dependency – broker, policy distribution, evidence store, retrieval, the seam's registry – against each tier, with the posture and the degraded capability set in the cell.
- Degraded mode as a designed product state with its own capability set, not as an absence of the normal one. It has a name, an entry authority, an exit authority, and a user-visible behaviour.
- `[ADR-25]`, and the political content of it: the signature matters more than the matrix, because the matrix's purpose is to make the decision attributable before it is urgent.
- `[ADR-23]` restated in its operational form: the evidence row does not vary, and here is what that means for availability, stated as a number rather than a virtue.
- What survives degraded mode: the evidence obligation, always, including evidence that the platform was degraded.

**Decisions anchored.** `[ADR-25]`, and the operational half of `[ADR-23]`.

**Figures.**

- *Figure 13.1* – state diagram: normal, degraded, halted, with the authority named on each transition. Answers: who can put the system into each state, and who can take it out?
- The matrix is a table. It has cells with text in them and no amount of drawing improves it.

**The bill.** Degraded mode is a second system, and an untested second system is a rumour. It needs its own tests, its own runbook and its own place in the drill calendar, which is a real ongoing cost and the reason most organisations have a fail posture on paper only.

**Decay question.** When was degraded mode last entered deliberately, and did the declared capability set match what actually happened?

**Cross-references.**

- → §3.3: halting is one of the five stop mechanisms and shares machinery with this.
- → §3.4: the matrix is on the recertification calendar.
- ← §2.7: the ordering rule this chapter refuses to negotiate.
- ← §2.1, §3.1: the dependencies that can fail.

**Source integration.**

- `[PENDING: DORA operational resilience provisions]` – specifically the parts about testing and about documented degraded operation, which map unusually well here and should be cited once rather than leaned on.
- `[PENDING: resilience engineering literature]` – for graceful degradation as a designed state. One source.

**Gaps and Queries.**

- `[QUERY: is there any defensible exception to the evidence row? A reviewer will propose one: a life-safety scenario where acting unrecorded beats not acting. The document's scope is enterprise agents and the answer is probably that the exception belongs to a different system with a different safety case. State the boundary rather than pretending the question is not asked.]`

---

## Chapter 15: Stopping It

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Replace the single kill switch with the five mechanisms the reader actually needs, give each an owner, an interval and a drill, and name plainly what no switch can undo.

**Argument.** Everyone asks for a kill switch and means five different things. Halting one run, revoking a class of authority, disabling one operation everywhere, quarantining an agent version, and cutting egress are five distinct mechanisms with five different reach profiles and five different intervals. Building one and calling it the kill switch means that in the incident, someone reaches for the wrong reach: too small to help or so large it takes the business down. And the interval is not a design parameter you can claim. It is a measured quantity, and it is only measured by executing the switch against a live run.

**Invariant.** I6. Revocation takes effect within a stated interval, without the agent's cooperation.

**Beats.**

- Answer first: five switches, five mechanisms, five owners, five drills.
- Each switch: what it stops, what it does not, its mechanism, its measured interval, and who is allowed to pull it at 03:00 without waking anyone.
- Why the intervals differ, and why the differences are structural rather than fixable: revoking authority propagates at the speed of the staleness budget from chapter 13, while halting a run is a direct action.
- Without the agent's cooperation, which is the whole point and the reason none of these can be implemented as a message the agent is asked to honour.
- `[ADR-26]`, against the single switch, with the honest cost: five mechanisms is five things to build, own, document and drill, and the temptation to build one is a resourcing argument rather than a design error.
- What no switch undoes. The mail that arrived, the payment that cleared, the data that left. Compensating action is a business capability, not a platform one, and the platform's contribution is knowing precisely what to compensate – which is chapter 11's contribution arriving when it matters.
- The drill `[ADR-27]`: a switch not executed against a live run in the last quarter does not exist. State it as a definition, not as advice.

**Decisions anchored.** `[ADR-26]`, and `[ADR-27]` in its first appearance.

**Figures.**

- *Figure 14.1* – the five switches drawn against the layers they cut: run, envelope, operation, agent version, egress. Answers: when I pull this one, what stops and what keeps running?

**The bill.** Five mechanisms, five runbooks, four drills a year each. And a standing organisational cost that is easy to miss: five named owners who are still at the company next year, which is an attrition problem disguised as an architecture one.

**Decay question.** For each of the five, on what date was it last executed against a live run, and what interval was measured?

**Cross-references.**

- → §3.4: the drill calendar.
- ← §3.1: the staleness budget that sets the revocation interval.
- ← §1.1: the third leg of the claim is this chapter's subject, and the claim is falsified here or nowhere.

**Source integration.**

- `[PENDING: incident response literature]` – for the containment taxonomy, one source, cited for vocabulary rather than for authority.
- `[QUERY: is there published practice on agent-specific kill mechanisms, or is this entirely derived? If derived, say so. The document's credibility rests on distinguishing what it inherited from what it invented.]`

**Gaps and Queries.**

- `[QUERY: five is a claim...]` Unchanged – merge test before draft.
- **Resolved `[OQ-05]`:** no agent break-glass; human manual path on system of record, maintained and drilled.

**Worked moment(s).**

- Eleven minutes to stop a run: kill switch in architecture doc, control register, and DORA filing – none executed in production before incident. After drill: L1 pause in agent UI, median under one minute. Emergency payment adjustment: Marta uses Guidewire directly; platform records human path, agent not widened `[OQ-05]`.

---

## Chapter 16: Decay

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Establish that every control in this document degrades silently, that each degradation has an indicator that can be measured, and that recertification and drills are the entire reason any of it is still true in month fourteen.

**Argument.** Nothing here fails loudly. Envelopes widen one reasonable exception at a time. Coverage falls when a team ships a service that talks directly to a system of record. Approval gates become formalities. Bundles go stale. Tool descriptions drift from the versions that were reviewed. Every one of these is invisible in a dashboard designed for availability, and every one of them is visible in a dashboard designed for this. The controls do not need heroism; they need a calendar, an owner, and a small number of indicators that someone is accountable for looking at.

**Invariant.** I7. Every control has a test, an owner, and a date on which it was last exercised.

**Beats.**

- Answer first: the decay catalogue, its indicators, and the calendar. This chapter is a maintenance schedule and does not apologise for it.
- Why decay is the default rather than a failure: each individual widening is a reasonable decision made by a competent person under delivery pressure, and the sum of reasonable decisions is the original problem restored.
- The catalogue, one row per control, with the indicator and the direction that means trouble. Every decay question from every previous chapter arrives here, which is why they were written into the cards.
- Canary runs: adversarial cases that should be refused, executed continuously against production. A canary that starts passing is an incident, and it is the only mechanism in the document that detects a control's absence rather than its presence.
- The recertification calendar, in outline, with the full version in Appendix G.
- Who owns the dashboard, and the failure mode where the dashboard exists and nobody is accountable for its trend.
- The month-fourteen argument, stated once and plainly: the difference between organisations that still have these properties and those that do not is not architecture, and everyone in the room already knows it.

**Decisions anchored.** `[ADR-27]` argued in full here, against documented procedures as evidence of capability.

**Figures.**

- *Figure 15.1* – decay indicators mapped to the invariant each one threatens. Answers: if this number moves, which promise stops being true?

**The bill.** Roughly one engineer-day a week, permanently. This is where chapter 1's most quotable number is defended, and the defence has to be an itemisation rather than an assertion: recertification, drills, canary maintenance, coverage discovery, and the archaeology of unmediated paths.

**Decay question.** Recursive, and deliberately so: who owns the decay dashboard, and when did they last look at it?

**Cross-references.**

- → Appendix G: the calendar and the canary suite.
- ← every chapter in Parts II and III. Each contributes exactly one row.

**Source integration.**

- `[PENDING: control-drift or compliance-decay evidence]` – from any regulated field. Aviation maintenance and clinical audit both have it, and borrowing from a mature field is stronger here than citing nothing.
- `saltzer1975protection` – possible closing callback, but chapter 1 and chapter 21 both use this move and three is one too many. `[QUERY: which two keep it?]`

**Gaps and Queries.**

- `[QUERY: does this chapter belong in Part III or is it the true ending of the document? Argument for moving it: it is the thesis about time and it would make a stronger close than chapter 21. Argument against: chapter 21's residual is the honest close and decay is one of the residual's causes. Current answer is Part III, but the two chapters have to be drafted with the seam between them clearly cut.]`

---

## Chapter 17: The Paved Road

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Show that an unadopted control has negative security value, and price the sanctioned path against the shortcut in the only unit that decides the outcome.

**Argument.** A control that is bypassed is worse than one that does not exist, because it produces a coverage number, a slide, and a belief. Adoption is not decided by policy, by training or by an architecture board. It is decided by an engineer at 16:00 comparing two paths and choosing the shorter one, and the comparison is made in minutes. That makes developer experience a security control with a measurable target, and it makes the paved road a product with an owner rather than a security project with a deadline.

**Beats.**

- Answer first: measure time-to-first-mediated-call, and treat it as a security metric with a target.
- The negative-value argument, stated carefully so it does not become an excuse for building nothing.
- The two paths, priced in minutes: the sanctioned route from *I want my agent to call this tool* to a working mediated call, against the shortcut of an SDK call and a credential from a colleague.
- Where the minutes actually go, itemised: need declaration, tool onboarding, side-effect classification, registry entry, local development against a gateway that does not exist on a laptop.
- The refusal as a product surface. A refusal that says which envelope field failed and what to request instead converts an adversary of the platform into a user of it. This is the cheapest high-value item in the document and is almost always skipped.
- `[ADR-28]`: funded as a product with an owner, against security-owned tooling funded as a project. The rejected option is how most organisations do it and the reason most paved roads are gravel.
- The feedback loop into chapter 7: coverage is a lagging indicator of friction. If coverage falls, measure minutes before writing a policy.

**Decisions anchored.** `[ADR-28]`.

**Figures.**

- *Figure 16.1* – the two paths, step by step, with minutes on each step and the totals. Answers: which path would you take at 16:00 on a Thursday? The figure should be almost embarrassing to look at, because in most organisations it is.

**The bill.** A product team, which is the largest single line item in the document and the one most likely to be cut. Say plainly what happens when it is cut: coverage falls, and the fall is attributed to culture.

**Decay question.** What is the current time-to-first-mediated-call at the median and the ninetieth percentile, and is it rising?

**Cross-references.**

- → §4.3: the build order funds this early, and the argument for that sequencing is here.
- ← §2.3: coverage as the lagging indicator.
- ← §2.2, §2.4: the two mechanisms that generate most of the friction.

**Source integration.**

- `[PENDING: developer experience and platform engineering evidence]` – for the adoption-versus-friction relationship. Dated, because the field's literature is young and mostly vendor-authored, which should be acknowledged.

**Gaps and Queries.**

- `[QUERY: does this chapter risk reading as platform-engineering advice rather than security architecture? The defence is the negative-value argument and the coverage link, and both have to be in the first page or the chapter loses its place in the document.]`

---

# Part IV. The Edges

## Chapter 18: Composition

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Establish precisely which invariants survive an agent calling an agent, which do not, and what the absence of a composition standard costs a reader who has to ship next quarter anyway.

**Argument.** Composition breaks the document's central assumption in one specific way, and naming it exactly is the chapter's contribution. Everything in Part II rests on the seam being a boundary between non-deterministic and deterministic compute – guessing on one side, inspectable execution on the other. When an agent calls an agent, both sides are non-deterministic, and the callee cannot verify that the caller's request reflects the principal's intent rather than an injection the caller absorbed three tool calls ago. Attenuation still holds, because it is structural. Evidence still holds, because it is mechanical. Approval, intent and budget do not, and no amount of care in the calling convention makes them.

**Invariant.** I3 extended: attenuation holds across delegation depth, and depth is bounded because nothing else about the chain is.

**Beats.**

- Answer first: attenuation and evidence compose; approval, intent and budget do not.
- Why, in one paragraph, using the seam: non-deterministic compute on both sides means there is no inspectable object to attach a rule to at the boundary between them.
- What survives: derived envelopes at each hop, strictly attenuating; evidence chained by parent run identifier, giving a verifiable tree after the fact.
- What does not: an approval given to the parent does not authorise the child's actions, because the approved object was a call at the parent's seam and the child's calls are different objects. Intent does not survive the hop for the same reason.
- Budget, which is the awkward middle case: it composes only if it is centrally held, and central holding costs contention on every call in a fan-out.
- Fan-out as an amplification threat rather than a performance one: depth limits, breadth limits, and cycle detection, none of which are elegant and all of which are necessary.
- `[ADR-29]`, against propagating the parent's authority and approval, which is what every framework does by default.
- The absence, stated rather than papered over: there is currently no standard that carries intent or approval across agent boundaries, and here is specifically what such a standard would have to carry. This is the same move as chapter 8's wish list and should be recognisably the same move.

**Decisions anchored.** `[ADR-29]`.

**Figures.**

- *Figure 17.1* – parent and child runs: envelope attenuating along the solid path, evidence chaining back, and the dashed edge where intent and approval do not cross. Reuses the solid-and-dashed vocabulary from Figure 1.2, which is the reason that vocabulary was introduced early.

**The bill.** Depth and fan-out limits that will block a legitimate workflow in the first month. Centrally held budget with its contention cost. And an evidence volume that multiplies with the tree rather than the run.

**Decay question.** What was the maximum observed delegation depth and fan-out last quarter, and were the limits ever raised without a review?

**Cross-references.**

- ← §2.4: the limit stated at the end of the seam chapter is delivered here.
- ← §2.2: attenuation by construction, which is why it survives.
- ← §2.7: evidence chaining.
- → §4.4: what composition leaves open is part of the residual.

**Source integration.**

- `[PENDING: multi-agent composition literature]` – preprints cited as preprints, per the source notes. Prefer stating an absence over citing a weak result.
- `[PENDING: current framework behaviour on authority propagation]` – dated, because it is a claim about what tools do today and it will be wrong within two editions.

**Gaps and Queries.**

- `[QUERY: is the claim "intent does not compose" too strong? A reviewer may argue that a signed intent artefact from the principal could travel with the chain. Steel-man it before rejecting it, because it is the most plausible objection in the chapter, and if it survives the steel-manning then the chapter changes shape.]`

---

## Chapter 19: Across the Boundary

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Extend the model to agents acting with and against other organisations' agents, and mark clearly which parts of what the reader wants are currently unbuildable.

**Argument.** Inside one organisation, the platform can assume a shared policy domain, a common identity estate and an evidence store both parties trust. Across organisations, none of that holds, and the instruments that survive mutual distrust are few: credentials that are attenuated and bound to a possessor, verifiable claims about the caller that the recipient can check without trusting the sender, and evidence obligations that are contractual rather than technical. Most of what people want here – knowing that the counterparty's agent was operating under an equivalent envelope, or auditing their run – cannot currently be built. Saying so precisely, and saying what would have to exist, is more useful than a design that assumes it away.

**Beats.**

- Answer first: three instruments survive, and a long list of things people want does not.
- The four cases, kept separate because they have different answers: our agent into their system, their agent into ours, agent to agent, and both agents acting for the same human.
- Instrument one: attenuated, possession-bound credentials, which work across boundaries for the same reason they work inside them.
- Instrument two: verifiable claims about the caller – what can be asserted, what a recipient can check, and the gap between the two.
- Instrument three: contractual evidence exchange. You cannot audit their run. You can require an attestation and hold a record of what you were told, which is a weaker property and a real one.
- What is unbuildable today, itemised, with what would have to exist for each. No hedging, no *emerging*.
- Liability, in three sentences and without pretending to legal expertise: the burden lands on whoever cannot demonstrate, which returns the reader to chapter 11 with a commercial motive rather than a compliance one.
- `[ADR-30]`, against assuming a shared policy domain or a federated broker, both of which are proposed regularly and both of which assume the trust the situation lacks.

**Decisions anchored.** `[ADR-30]`.

**Figures.**

- *Figure 18.1* – the four cases and which instrument applies to each, with the unbuildable cells marked as unbuildable rather than left empty. Answers: which of these four situations do we actually have an answer for?

**The bill.** Bilateral agreements, per-counterparty onboarding, and an attestation register with expiry dates that somebody has to watch. This is a legal and commercial cost more than an engineering one, which makes it slower and easier to underestimate.

**Decay question.** Which counterparty attestations have expired, and are the corresponding integrations still live?

**Cross-references.**

- ← §4.1: composition inside the boundary, which is the easier case and still has holes.
- ← §2.1: attenuated possession-bound credentials.
- → §4.4: the cross-boundary residual is the largest part of the residual.

**Source integration.**

- `[PENDING: verifiable credentials specifications]` – W3C, pinned and dated.
- `[PENDING: current interoperability proposals for agent-to-agent interaction]` – as preprints and drafts, dated, with an explicit statement of maturity. This section will age fastest in the document and should be written to age visibly rather than silently.

**Gaps and Queries.**

- `[QUERY: research priority 3 determines whether this is a design chapter or a survey of absences. Resolve before outlining further. If it is a survey, the chapter is shorter and more valuable, and the function statement should say so.]`

---

## Chapter 20: Build Order, and Who Should Not Build This

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Sequence the work for a real team with real constraints, and state without hedging the conditions under which the correct answer is to build almost none of it.

**Argument.** There is one defensible order, and it follows from a single rule: every step has to leave the system in a state that is defensible on its own, because every roadmap gets interrupted and the interruption arrives at a random point. That rule produces the gateway and the evidence path first, not because they are the most interesting but because a system with those two and nothing else can still answer the question that matters. And for a large class of readers the correct build is four things and then stopping, which is a recommendation the document has to make loudly enough that it survives being read by someone who wants to build all of it.

**Beats.**

- Answer first: the order, in one list, with the invariant each step makes true.
- The rule that generates the order, stated before the order so the reader can generate it themselves in a different setting.
- Step by step: what it costs, what it unlocks, and what you can defend at the end of it.
- The reduced build, in full: gateway, audience-bound credentials, egress allow-list, call logs. One quarter, four engineers, and then stop. This is the recommendation for most readers and it is stated as a recommendation rather than as a concession.
- The tier-0 build, for the case where the introduction's three conditions all hold.
- What to do if you already have half of it, which is the most common actual situation and the one least served by a greenfield roadmap.
- The failure mode of sequencing: building policy sophistication before coverage. A rich policy language over sixty per cent coverage is a rich policy language over sixty per cent coverage.

**Figures.**

- *Figure 19.1* – build order as a dependency graph, with the invariant made true at each node and the two stopping points marked. Answers: where can we stop and still be defensible?

**The bill.** Assembled once, from every chapter's bill, as a single table. This is the number a reader takes to a funding conversation and it should be easy to find, which is an argument for it being a table on a page of its own.

**Cross-references.**

- ← §1.1: the intersection test, argued here at length.
- ← every mechanism chapter, for cost.
- → §4.4: what remains after the full build.

**Source integration.**

- None new. This chapter assembles and does not introduce. `[QUERY: is that defensible, or does the build order need at least one external anchor – a published maturity model or migration pattern – so it does not read as pure assertion?]`

**Gaps and Queries.**

- `[QUERY: two quarters and five engineers, or the introduction's four to six over two to three? The two figures have to agree, and whichever survives has to carry the same stated basis in both places.]`

---

## Chapter 21: What It Can Still Do

**Status:** [DRAFTED] – first draft written 2026-08-01.

**Function.** Close the residual honestly – what an adversary can still do after everything here is built and operating correctly – and convert the document's expiry from an implication into a schedule.

**Argument.** Every control in this document is now built, operating, drilled and measured, and Kai can still do a specific and enumerable set of things. Naming that set is not a disclaimer. It is the last and most useful contribution the document makes, because a reader who knows the residual can decide what else to do, and a reader who does not will believe the apparatus is a boundary rather than a bound. The residual also has an expiry: the thirty decision records each carry a trigger that would reopen them, and collected, those triggers are the honest statement of how long this document is good for.

**Beats.**

- Answer first: here is the list. Seven items, each named plainly.
- Actions inside the envelope but against the principal's interest. The bound is a bound, not a judgement, and everything permitted remains permitted.
- Timing, ordering and aggregation attacks composed entirely of permitted operations.
- Exfiltration through channels the design allows, which is the residual that scales worst and the one the allow-list makes narrow rather than closed.
- Social engineering of the approver, which chapter 9 makes harder and does not remove.
- Supply chain above the trusted computing base: the model, the framework, the tool implementations.
- Compromise of the trusted computing base itself, where the document offers nothing beyond what any control-plane compromise offers.
- The unmediated paths that have not been found yet, which is the residual that chapter 7 measures and never closes.
- Why each is residual rather than a gap: what closing it would cost, and why that cost is not paid. Each one is a decision, not an oversight, and the difference should be visible.
- The expiry schedule: revisit triggers from all thirty records, collected into one table, sorted by likelihood of firing first. The protocol triggers from chapter 8 sit at the top, and saying so is a service to the reader.
- The close: back to 1975, briefly. The principles were published then, the shortage is discipline, and the reader now has both a schedule and a list of what the discipline does not buy.

**Figures.**

- *Figure 20.1* – the residual set placed against the invariant set: which invariants hold, and what remains possible anyway. Answers: if all seven promises are kept, what is still true for the adversary? This is the document's closing image and it should be uncomfortable.

**Cross-references.**

- ← §1.1: the promise made in the introduction is settled here.
- ← §3.4: decay is a cause of residual and is not repeated.
- ← Appendix B: the triggers.

**Source integration.**

- `saltzer1975protection` – the closing callback, if chapter 16 gives it up. `[QUERY: resolve the three-way contention for this citation. Recommendation: chapter 1 opens with it and chapter 21 closes with it, and chapter 16 finds another way.]`
- `[PENDING: anything published on residual risk in deployed agent systems]` – likely nothing. If so, say so, because a document that admits its final chapter has no literature behind it is more trustworthy than one that pads it.

**Gaps and Queries.**

- `[QUERY: seven residual items is currently a guess. The real test is whether each one survives the question "would a competent adversary bother?" Anything that fails that test is padding and should be cut, even if it leaves five.]`

---

## Citation Scaffolding: Pending Slots and Sources to Resolve

- Empirical evidence for prompt-injection detection false-negative rates under an adaptive adversary (ch. 1, ch. 4). The document's premise depends on it.
- Canonical citation for the confused deputy, Hardy 1988 (ch. 1, ch. 6). Resolved.
- Saltzer and Schroeder 1975 (ch. 1, ch. 3, ch. 4, ch. 6, ch. 7, ch. 8, ch. 21). Resolved. Contention over the closing callback is open.
- Sender-constrained token specifications: RFC 8705, RFC 9449, RFC 8693 (ch. 5).
- Capability security and attenuation, one canonical source (ch. 4, ch. 6).
- MCP specification and MCP authorisation specification, pinned revision and retrieval date (ch. 8). Re-checked at copy-edit.
- Published MCP vulnerability research: tool poisoning, description injection, malicious servers (ch. 8).
- Automation bias and vigilance literature from aviation or clinical decision support (ch. 9).
- Memory poisoning and retrieval injection research (ch. 10).
- Crypto-shredding against GDPR Art. 17, including known objections (ch. 11).
- DORA and EU AI Act articles carrying burden-of-proof, logging, oversight and resilience-testing obligations (ch. 2, ch. 11, ch. 14, Appendix A).
- Policy-as-code and distributed authorisation, dated vendor and open-source documentation (ch. 13).
- Verifiable credentials, W3C, pinned (ch. 19).
- Multi-agent composition and agent interoperability, preprints only (ch. 18, ch. 19).

## Research Priorities

0. **Close the blocking subject-matter questions in `open-questions.md`.** Nine of the thirty-one are marked blocking, and three of those – the envelope against the policy engine (`[OQ-09]`), what an agent version is (`[OQ-19]`), and who the principal is in an unattended run (`[OQ-01]`) – are places where chapters currently contradict each other rather than merely omit something. No Part II chapter reaches `DRAFT-READY` before its own blocking questions are answered, and the register names which chapter each one blocks. The register also concludes that four subjects are chapter-sized and homeless, which is why the chapter list is provisional.
1. **Rebuild the threat set for the widened scope**, before any Part II chapter passes `[BEATS]`. Everything in Part II is derived from it, and the seam chapter's evidence base is the thinnest. The register adds threat surface the current set does not cover – the reversed seam (`[OQ-10]`), the cross-context aggregation channel (`[OQ-15]`), the memory path that launders a widening request into a later derivation (`[OQ-17]`), and the shared context cache (`[OQ-27]`).
2. **Re-litigate the load-bearing decisions inherited from the whitepaper.** Until this is done, no Part II chapter can reach `DRAFT-READY`. The decision index above is provisional in exactly this respect: it lists thirty decisions, and some number of them will turn out to be one decision wearing two hats.
3. **Pin the protocol.** Chapter 8 cannot be drafted against a moving specification. Fix a revision, date it, and write the chapter so that its argument survives the revision improving – the concept of the seam has to carry the chapter, not the current state of one protocol.
4. **Establish the standards position for cross-organisational interaction**, which decides whether chapter 19 is a design or a survey of absences. The second is more likely and would be shorter and better.
5. **Gather empirical material on approval decay and on injection detection rates.** Both carry weight the document cannot afford to assert, and both are currently the largest gaps between what the document claims and what it can show.
