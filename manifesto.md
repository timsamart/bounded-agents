<!--
Project law. Every later artifact (voice.md, toc.md, outline.md, role-*.md)
and every editorial decision references this file as authority.

Edits are permitted and expected; each one should be deliberate and recorded
in the commit message. Sections are numbered for stable reference. Do not
renumber. Deprecate rather than delete.
-->

# Manifesto

Governed Agentic Infrastructure *(working title, deferred – see §10)*

---

## 1. What this project is

A technical whitepaper in book form: roughly 130 pages of argument plus roughly 170 pages of specification, rendered to PDF and HTML from a single markdown source. It describes how to build an enterprise platform that lets AI agents hold and exercise real authority – write to systems of record, move money, send mail, call third parties – under the assumption that the model driving them may at any moment be acting against the organisation's interest.

The work is organised by **altitude**, not by component and not by adversary move. It descends from a one-page claim to a set of mechanisms to their operational discipline, and each altitude is complete on its own: a reader who stops at the end of any part holds a coherent and defensible position rather than half of one. Beneath the descent sit two vertical layers that the prose points at but never contains. The **decision layer** is a set of architecture decision records in Nygard's form, each with a genuine rejected alternative and its cost. The **specification layer** is the normative register, the threat model, the schemas, the conformance suite, the drills, and the references. Neither layer is allowed to leak upward into the argument.

The structural commitment that shapes everything else is the *marker discipline*: the only trace a decision, a specification or a source may leave in running prose is a short bracketed marker, and the prose must remain complete and correct when every marker is deleted. This is what "non-obstructive" means here, stated as something that can be tested rather than aspired to.

Expected length: roughly **170 to 180 pages** of narrative spine and 150 to 200 pages of appendices. These are projections from the current twenty-one-chapter list (`open-questions.md` v0.2, `toc.md`), not a budget the content is cut to fit. Length is a diagnostic rather than a gate: a chapter that runs long is asked whether it holds two chapters or a digression, and the answer decides, not the number. A subject that is in scope under §4's boundary rule is never dropped because a page estimate has been reached – the estimate is revised, and the revision is recorded in §10. The constraint that does bind is usefulness per page, and it is enforced by the amputation test and the two-minute test rather than by a page count (`concept.md` §4).

---

## 2. Why this project

Three documents currently cover this material, and the problem is not that any of them is bad. It is that they cannot be handed to a team.

`archive/whitepaper.md` (2,926 lines) is rigorous, complete, and correct. It is also a specification with the argument distributed through it as connective tissue, which means it has exactly one reading order and no way to enter at the middle. It states its decisions and does not litigate them: a reader who disagrees with the choice of sender-constrained tokens over short-lived bearer tokens finds the conclusion but not the argument that would change their mind. And it is read by roughly one kind of person.

`archive/book-v2/` (*Blast Radius*, eighteen chapters plus eight Anlagen) solved the derivation problem beautifully. One system, one adversary, one earned invariant per chapter, nothing asserted that had not first failed on the page. It is the best teaching artifact in the corpus. It is also a book – three hundred and sixty pages that must be read in order, which is the correct shape for learning and the wrong shape for building. Nobody looks up a token schema in chapter five of a siege narrative.

`archive/executive-brief.md` is what the CISO reads, and it is a third document with its own drift risk.

So the gap is not explanatory and not evidentiary. It is one of **transfer**. An organisation that decides to build this needs an artifact that an architect, a platform engineer, an SRE and a security reviewer can each read at their own depth, argue with, hand to an auditor, and return to in month fourteen – without three documents falling out of sync with each other. That artifact does not exist in the corpus and, as far as the author's reading goes, does not exist in the field either: the published reference architectures for agentic systems are either vendor-shaped (a product diagram with governance vocabulary) or standards-shaped (normative and unmotivated). Neither shows its work.

The specific contribution is the decision layer. Around thirty architecture decision records, each naming an option a competent architect would plausibly have chosen, and each stating why it was rejected and what the chosen path costs. A reference architecture that cannot say what it rejected is a diagram with an opinion.

---

## 3. Target audience

**Primary audience.** The delivery organisation that has been told to build this, read at four depths.

- *The architect* is accountable for the shape and must defend it in review. They read the spine end to end and live in the decision layer. Their failure mode with existing material is being handed conclusions they cannot reconstruct, which makes them either a transcriber or an opponent.
- *The platform engineer* implements a mechanism at a time. They read one chapter of Part II and then move to the schemas and worked examples. They need bytes, not prose: a decoded token, a policy rule, a refusal payload.
- *The site reliability engineer* inherits the thing at 03:40 and cares about exactly four questions – what fails, what fails closed, what can be stopped, and what happens to runs in flight. Part III is theirs and is written so it can be read first.
- *The security reviewer* wants the threat model, the coverage claim, and the honest residual. They enter through Appendix C, cross into Appendix A, and judge the spine by whether it lies about what remains possible.

All four share one property that shapes the register: they will build something either way. The document competes with the afternoon they were about to spend wiring an agent to a tool, so a section that is not useful within its own page count loses to the repository they already have open.

**Secondary audience.** Two, both of whom read one part and stop.

- *The engineering or risk leader* deciding how much of this to build. They read the introduction, which is written to be complete at eight pages and includes the paragraph stating who should not build this at all. They are the reason the cost of every mechanism is printed.
- *The auditor or supervisory reader* in a regulated setting. They read Appendix A – the normative register, traced threat to control to test to evidence – and never open the spine. The register is written so that this is a reasonable thing to do.

---

## 4. Period or scope

**In scope.** A single enterprise operating AI agents that take actions with external effect against its own systems and its counterparties' systems. Identity and authority, the derivation and attenuation of permission, complete mediation of tool access, human approval where it earns its cost, data access and memory, tamper-evident evidence, the operational discipline that keeps all of it alive, and the failure postures for when it does not work.

Widened relative to the superseded whitepaper, at the author's direction: **multi-agent composition** and **cross-organisational agent interaction** are full parts of the work rather than acknowledged caveats. This is the fastest-moving and least settled ground in the field, which is precisely why the treatment is separated into its own part with its residual stated plainly rather than smuggled into the mechanisms as though it were solved.

**Out of scope.** Model training, fine-tuning, evaluation and alignment. Consumer and personal agent use. The internal safety properties of a model. Physical robotics. General enterprise IAM, except where the agent case breaks it. These are named as non-goals in the introduction rather than left to be discovered.

**Boundary rule.** A subject is in scope if a hostile model changes the answer. If the design of a thing is unaffected by whether the model is adversarial, it belongs to ordinary platform engineering and is cited, not explained.

**Version boundary.** The work is a living document with numbered editions. An edition is complete when every chapter has cleared the three editorial passes, every normative requirement in Appendix A traces to a threat and a test, and every architecture decision record has a stated revisit trigger. Standards in this field are wet cement; the revisit triggers are how the document declares its own expiry rather than pretending not to have one.

---

## 5. Methodological model

**Structure: arc42 and the C4 model.** arc42 supplies the section semantics (context and scope, solution strategy, building block view, runtime view, crosscutting concepts, quality requirements, risks and technical debt) and C4 supplies the zoom discipline for the views. Both are chosen because the primary audience already reads documents in these shapes, which buys orientation for free.

One deliberate deviation. arc42 places architecture decisions in section 9, as a section of the document. Here the decision layer is dissolved out of the spine entirely and lives in an appendix, reachable from any point in the argument by a marker. arc42's own guidance permits this; the reason for taking it is that a decisions section is read by nobody and referenced by everybody, which is the definition of material that belongs in reference position.

**Decisions: Michael Nygard's ADR form**, in its original short shape – context, decision, status, consequences – extended with two fields this project requires: the rejected alternatives with the reason each was rejected, and the revisit trigger that would reopen the decision.

**Derivation: Kleppmann's method in *Designing Data-Intensive Applications*.** State the promise a competent engineer would like to believe, show the specific circumstance in which it fails, and rebuild a weaker promise that survives. This is the engine that keeps a top-down document from reading as assertion. It is inherited directly from the superseded *Blast Radius* manuscript, which proved it works on this material.

**Presentation: Minto's pyramid principle, with one amendment.** Every section leads with its answer and then supports it, because a reader who is looking something up must not have to read a build-up. The amendment: within a section, the mechanism is still motivated by the failure that forces it. Answer first at the top, derivation underneath. This is the single hardest discipline in the project and the place where drafts will fail.

**Discipline: patterns in Alexander's sense, never printed as a template.** Each mechanism has a context, the forces acting on it, the move, the consequences, and links up and down the altitudes. The rhythm is performed and never announced, a rule learned expensively by the superseded drafts, all of which printed their chapter template on page nine and became forms being filled in.

---

## 6. Division of research labor

The project is primary work, not transcription. Three divisions.

**Re-litigated, not inherited.** Every decision carried over from the superseded whitepaper is reopened before it is recorded. A decision that survives arrives in Appendix B with the alternative that was actually tempting and the reason it lost. A decision that does not survive is changed, and the change is noted in the record. Transcribing the old conclusions into ADR shape would produce thirty documents of retrospective justification, which is the failure mode this appendix exists to prevent.

**New threat modelling.** The superseded threat model (T1–T10) predates the scope widening and does not cover multi-agent composition or cross-organisational interaction. The threat set is rebuilt, and Appendix C carries the method for generating threats rather than only the list, because a reader who can recognise this list and not produce their own is helpless the moment the list ages.

**New worked examples.** End-to-end walkthroughs are written fresh against the current mechanism set rather than adapted, because an adapted example is where inconsistencies hide.

**Synthesis, honestly labelled.** Standards, specifications and published research (OAuth token exchange, sender-constrained tokens, MCP, NIST and ENISA material, the EU regulatory instruments) are synthesis and are cited numerically. Where the field has no answer – multi-agent composition being the clearest case – the document says so in the residual rather than manufacturing one.

---

## 7. Priority sources

In descending order of authority for this project.

1. **Normative standards and specifications.** RFCs, OAuth and OIDC specifications, the Model Context Protocol specification, W3C material. These bind: where a standard settles a question, the document follows it and cites it, and any deviation is an ADR.
2. **Regulatory instruments.** DORA, the EU AI Act, the GDPR, and supervisory guidance. Used for obligations and burden of proof, never for design; the regulatory map in the appendices is explicitly non-normative, because a control that exists only to satisfy a citation is theatre.
3. **The security engineering literature.** Saltzer and Schroeder, the capability tradition, Hardy's confused deputy, contemporary work on prompt injection and agent security. These supply the vocabulary and the fifty-year-old principles the field keeps rediscovering.
4. **Vendor and platform documentation.** Cloud IdPs, gateways, policy engines. Treated as evidence of what is buildable today and dated on sight, because it is the fastest-rotting source class in the project.
5. **The superseded corpus.** `archive/whitepaper.md`, `archive/book-v2/`, `archive/executive-brief.md`, `raw-research.md`. Authoritative on what the author already concluded and not authoritative on whether it was right. Used as input to re-litigation, never quoted as support.

Known limits: the vendor layer will be stale within two editions, the regulatory layer within one, and the multi-agent literature is not yet a literature. All three are marked in the text where they carry weight.

---

## 8. Format and distribution

Markdown source, rendered to two targets from one build: a paginated PDF for download and an HTML edition for timosam.com. Free, no gate.

The dual target is a design constraint rather than a convenience. The marker discipline has to work in both: in HTML a marker expands in place, in PDF it resolves to a page reference. Any device that only works in one target is rejected. This kills, among other things, hover text, collapsible sections as the sole means of disclosure, and any diagram that depends on colour to carry meaning.

Versioning: numbered editions, version-controlled, with a document history recording what changed and which architecture decisions moved. Figures are the author's own generated work; the placement decision is deferred (§10).

---

## 9. Positioning against existing work

**Vendor reference architectures for agentic AI.** Complete, current, and shaped by what the vendor sells. They are useful as a survey of what is buildable and useless as an argument, because no vendor architecture names the option it rejected. This project's contrast is the decision layer.

**Standards and framework material** (NIST-style profiles, the emerging agent security guidance, regulatory technical standards). Authoritative and deliberately unmotivated: normative statements without derivation, which is correct for a standard and leaves the reader unable to adapt when their case does not match. This project's contrast is that the normative register is derived in the spine before it is stated in the appendix.

**The academic literature on prompt injection and agent security.** Precise on attacks, thin on platform construction. It is where the threat model comes from and it does not tell anyone what to build on Monday.

**The superseded corpus.** *Blast Radius* remains the better artifact for a reader who wants to learn the field, and the introduction says so and points at it. This project is not an improvement on it; it is a different object with a different job. Where the two disagree on substance, this document wins, because it re-litigated the decision and the book inherited it.

---

## 10. Decisions taken and recorded

1. **Supersession.** This document supersedes `archive/whitepaper.md` and `archive/book-v2/`. Both remain readable in `archive/` and neither is maintained. The supersession is stated in the front matter, not implied.
2. **Language.** British English throughout. *(Departure from the superseded whitepaper, which was American; the corpus had drifted and one variant had to win.)*
3. **Citations.** Numbered `[17]` markers resolving to a single reference list at the back.
4. **Decisions.** Nygard-form ADRs, extended with rejected alternatives and a revisit trigger, marked in prose as `[ADR-014]`, recorded in full in Appendix B.
5. **Normative language.** RFC 2119 keywords appear in the appendices only. The spine argues; the register specifies. No requirement is stated normatively in both places.
6. **Marker discipline.** Three marker classes – `[ADR-nn]`, `[A-3.2]`, `[17]` – sharing one visual grammar. **The deletion test governs:** remove every marker from a page and the prose must remain complete and correct. A marker that carries meaning is a defect.
7. **Back matter.** Called *Appendix A–H*, followed by the reference list. English document, English apparatus.
8. **Structure.** arc42 section semantics, C4 view discipline, altitude-complete parts.
9. **Person.** First person plural while reasoning, second person when instructing or handing over a decision, first person singular never. Impersonal voice only inside the appendices, where requirements name their actor explicitly.
10. **Inherited prohibitions**, carried from the *Blast Radius* voice bible because they survived a full council and eighteen chapters of drafting: no unpriced control; the adversary is a person and never the model; never sneer at the naive design.
11. **Scope widening.** Multi-agent composition and cross-organisational agent interaction are first-class parts.
12. **Title.** Deferred. Shortlist and decision procedure recorded in `concept.md` §3. The working title is used in all artifacts until it resolves.
13. **Figures.** Fourteen editorial illustrations exist in `assets/`; placement map is in `worked-moments.md`. They are optional tier-three anchors: after a worked moment, captioned with the idea they anchor, greyscale-safe, never load-bearing. New commissions only where a moment plus schematic still does not land. Schematics remain Mermaid-only in the spine.
14. **Schematics in the spine.** Permitted, in Mermaid, at most three per chapter, each captioned with the question it answers and each subject to the deletion test. Architectural views remain confined to Appendix B and keep their C4 level in the caption. *(Amendment 1, `concept.md` §9.)*
15. **The prose has a second job.** Beyond clarity, it has to make the reader want the next paragraph, on the grounds that a document which is only ever consulted cannot transfer reasoning, which is this project's purpose. The rules are in `voice.md` §4 and they are bounded: one reframe per chapter, one dry aside per two pages, and nothing that sells. *(Amendment 1.)*
16. **Length is an estimate, not a boundary.** Every page figure in this project – total, per part, per chapter, and the eight pages the introduction is written to be complete in – is a projection from the current structure and a signal to look at, never a limit that decides content. Scope is decided by §4's boundary rule and by the invariant set; the page figures follow from those decisions and are updated when they change. Where a chapter exceeds its projection, the test is whether it holds two chapters, a digression, or material that belongs in an appendix – and if it holds none of those, the projection was wrong. Chapters may be added to the table of contents on the same terms: an open subject-matter question that turns out to be chapter-sized gets a chapter, and the length figures are revised in the same revision. *(Amendment 2.)*
17. **Subject-matter questions are tracked separately from editorial ones.** `open-questions.md` holds the questions about the domain whose answers change the architecture. The `Gaps and Queries` blocks in `outline.md` hold questions about the draft. A question that changes what is true about the system does not belong in a chapter card, because it outlives the chapter. *(Amendment 2.)*
18. **Worked moments are a required pedagogical layer.** Mechanism chapters sandwich pragmatic cast-bound vignettes between context and abstraction. Rules in `worked-moments.md` and `CONV-015`. Appendix E walkthroughs compile spine moments; they are not authored separately. *(Amendment 3.)*
19. **Chapter count revised.** Twenty-one spine chapters. Chapter 12 (*The Agent Manifest*) inserted at the head of Part III to answer the agents-as-code cluster (`open-questions.md` OQ-19–OQ-24). Part III chapters renumbered 13–17; Part IV renumbered 18–21. Page projections revised in `toc.md`. *(Amendment 3.)*

---

*Version 0.1 – 2026-07-31. Generated through the Bookwright bootstrap interview. Sections 4, 5 and 6 are expected to sharpen once Part II is outlined; every other section is load-bearing as written.*
