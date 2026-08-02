<!--
Project law for prose-level decisions. Mechanical source conventions live in
conventions.md. A copy editor unfamiliar with the project should be able to
enforce everything below without asking the author.
-->

# Voice and Style Guide

For *Governed Agentic Infrastructure* (working title).

---

## 1. Language

The work is written in **British English**.

The superseded whitepaper was American, the superseded book had drifted British, and a document that replaces both cannot hold two variants. British wins on three counts: the author is European, the primary regulatory frame is European, and the register the project wants – dry, understated, unhurried – sits more naturally in it. The cost is a one-off normalisation pass over anything harvested from the archive, which is cheap and must be done deliberately rather than left to the copy editor to notice.

### Spelling and punctuation conventions

- `-ise` and `-isation` throughout: *authorise*, *organisation*, *normalise*. **Exception:** technical terms that are proper nouns or spec vocabulary keep their source spelling – `authorization_details`, `OAuth 2.0 Authorization Server`, `Authorization` header. The rule is that anything inside code formatting or quoted from a specification is never respelled.
- *Behaviour, licence* (noun) / *license* (verb), *catalogue, defence, centre, grey*.
- **Serial comma: yes.** Contrary to common British practice, and for a technical reason: enumerated lists of controls, actors and obligations are frequent here, and the ambiguity a missing serial comma creates is expensive in a document that will be read as a requirement.
- Double quotation marks for quoted speech and quoted text; single inside double. Punctuation goes **outside** the closing quotation mark unless it belongs to the quoted material. This follows British logical punctuation and matters because quoted specification text must be reproduced exactly.
- Spaced en dashes for parenthetical breaks in running prose. See the departure below.
- Hyphenate compound modifiers before a noun: *sender-constrained token*, *short-lived credential*, *policy-decision point*. Do not hyphenate after: *the token is sender constrained*.
- Sentence case for all headings, including chapter titles. Title case is reserved for the names of published works and specifications.

### Deliberate departures from the style authority

The project declares **no external style authority**. Neither CMOS nor MLA nor APA serves a document whose apparatus consists of decision records, normative requirements and machine-readable artefacts; adopting one would create a long list of overridden rules and no benefit. The rules in this file are the authority, and where they are silent, *New Hart's Rules* is the tiebreaker.

Three project-internal departures from ordinary technical-writing practice, each with its reason:

1. **No em dashes in running prose.** Spaced en dashes only. An em dash gives no signal as to whether it opens or closes a parenthetical, which is tolerable in prose read once and costly in prose read under pressure at three in the morning. This also removes the most recognisable tell of machine-generated text, which matters for a document arguing that provenance is a design property.
2. **No normative keywords in the spine.** *MUST*, *SHOULD*, *MAY* and their negations appear in the appendices and nowhere else. In the spine, a requirement is argued in plain declarative prose. A reader must never have to decide which of two statements of the same rule is authoritative. **[CONV-008]**
3. **No footnotes.** Everything a footnote would do is done by one of the three markers. A document with markers *and* footnotes has two competing disclosure systems, and the reader learns neither.

---

## 2. Treatment of foreign-language vocabulary

The document is monolingual. German, Latin and other foreign terms are used only where the English equivalent loses something, are italicised on every occurrence, and are glossed in parentheses on first use. This is a rare event; a technical document reaching for a German noun is usually a writer enjoying themselves.

Specification vocabulary is not foreign vocabulary. `cnf`, `act`, `aud`, `jti` and their kin are set in code formatting, never italicised, and defined at first use in the chapter that introduces them and again in Appendix H.

### Personal names

Full name at first mention, surname thereafter: *Jerome Saltzer*, then *Saltzer*. Diacritics preserved. Named principles keep their conventional attribution – *the Saltzer and Schroeder principles*, *Nygard's ADR form*, *the confused deputy problem*, attributed to Norm Hardy at first use.

Fictional actors in worked examples are given a first name and a role and are never given a surname, so that they cannot be mistaken for cited persons. They are competent. See §4.

### Place names

English forms: *Munich*, *Cologne*, *Vienna*. Jurisdictions in their formal short form: *the European Union*, *Germany*, *the United Kingdom*.

### Institutional names

Full name at first mention with the abbreviation in parentheses, abbreviation thereafter: *the European Banking Authority (EBA)*. Specification and regulation names in full at first mention with their common short form in parentheses: *Regulation (EU) 2022/2554 (DORA)*, then *DORA*. Article references in the form *DORA Art. 30(3)*.

---

## 3. Style authority and citation system

The project follows **its own house rules** (this file) and uses **numbered citations** resolving to a single reference list at the back of the document.

### In-text citations

Numeric, in square brackets, at the end of the sentence, before the full stop: `... sender-constrained tokens are specified in RFC 9449 [12].` Never mid-clause. Never more than two markers on one sentence; if a claim needs three sources, it needs a sentence of its own or it belongs in an appendix.

Two sibling marker classes share the same grammar and the same typographic weight:

- `[ADR-014]` – a decision record. Placed at the end of the paragraph in which the decision is argued, never in the middle of the argument.
- `[A-3.2]` – an appendix pointer, to a specific numbered subsection. Placed at the end of the sentence whose detail lives there.

**The deletion test is the governing rule.** Strip every marker from a page. If any sentence becomes incomplete, ambiguous or wrong, the marker was carrying meaning and the sentence must be rewritten. Markers are exits, not load-bearing structure. This is the mechanism by which the document is non-obstructive, and it is checkable – a copy editor can run it on any page.

Density budget: no more than roughly six markers per page. Beyond that the page is reference material wearing narrative clothes and should be moved into an appendix.

### Footnotes

Not used. See §1, departure 3.

### Bibliography

A single numbered reference list at the back, ordered by first appearance, following the appendices. Entries carry: author or issuing body, title, publication or specification identifier, version or edition, date, and an access date for anything web-only. Specifications lead with their identifier (*RFC 9449*), because that is how the reader will search for them.

Sources with an expiry – vendor documentation, draft specifications, anything pre-standardisation – carry their retrieval date in the entry and a status word: *draft*, *proposed standard*, *vendor documentation*. The reader must be able to see at a glance which citations are cement and which are wet.

### Archival and primary-source citations

Not applicable in the ordinary sense; the project has no archival component. Internal predecessor documents are cited by repository path (`archive/whitepaper.md §6.3`) and only where a claim is genuinely inherited rather than re-derived. This should be rare, and each occurrence is a signal that the section has not yet done its own work.

### Foreign-language sources

Cited in the original language, with an English translation of the title in square brackets. Regulatory instruments are cited in their English-language official version where one exists. Quoted passages are translated by the author and marked *(author's translation)*.

---

## 4. Register and prose

**Clarity beats cleverness.** The topic is already hard. The prose must not make it harder. If a sentence sounds impressive and a plainer sentence would carry the same claim, use the plainer sentence. A reader who has to decode the writing has less attention left for the idea.

The audience is building something. They read in a hurry. A section earns its keep by being useful on the page where they opened it.

The ideal sentence states one thing. The ideal paragraph opens with its conclusion, then earns it. The ideal section can be read alone and leaves the reader able to defend one position in a design review.

### The plain-language rule (prime)

If you cannot explain a mechanism in ordinary words to a competent engineer who has not read the previous chapter, you do not yet understand it well enough to write it down. Rewrite until you can.

Practical tests, run on every draft page:

1. **Read-aloud test.** Read the paragraph out loud. If you stumble, the reader will too. Break the sentence.
2. **Colleague test.** Could a platform engineer paraphrase the claim after one pass? If not, cut abstractions until they can.
3. **Substitution test.** Replace every abstract noun phrase (*probabilistic architecture*, *governable moment*, *attenuation by construction*) with a concrete one (*filters miss sometimes*, *the place a rule can attach*, *authority can only shrink*). If the paragraph gets clearer, keep the concrete version.

### How information builds

Stairs, not elevators. Each paragraph should need only the last one. Do not stack three new abstractions before the reader has a picture of the first.

1. **Answer first.** Say the conclusion in plain words. Then give the reason. Then say what to do with it.
2. **Open where the reader already is.** One or two sentences of a situation they have lived – four lines of configuration, 16:40 with a review at 17:00. Then the claim. Not a scene; recognition, then the point.
3. **One idea per sentence.** Prefer short sentences. Prefer active voice. Prefer concrete nouns over abstract ones.
4. **Define jargon once, then use it.** Ordinary words first. Introduce a technical term only when you need it, with a one-line gloss. After that, use the term consistently – do not rotate synonyms for style.
5. **Show a number, a name, or a time.** Every abstract claim needs one physical anchor in the same paragraph: *40 ms at p99*, *claims-triage*, *09:04*. If you cannot find one, the claim is not ready.
6. **Ask and answer on the same page.** Never *as we will see in chapter 9*. Curiosity is fine; debt is not.
7. **Never sell.** No urgency theatre, no *as AI adoption accelerates*, no inflated consequences. The material does not need help.

### What this forbids

These patterns produced the first spine draft and are banned from the rewrite:

- Sentences that exist because they sound smart.
- Quotable one-liners that need a second sentence to decode.
- Nested abstractions (*a safety case resting on detection is a probabilistic architecture written up in deterministic language*).
- Clever chiasmus and recursive punchlines (*a version that cannot be talked into anything is a version that cannot be talked into anything*).
- Dry asides as a standing habit. One light touch per chapter is enough; zero is fine.
- Tricolons that arrived on autopilot, and the words *robust*, *seamless*, *leverage* as a verb, *simply* as an intensifier, *in today's rapidly evolving*.

Dull and clear beats brilliant and opaque. Every time.

### Other failure modes

- *The specification voice creeping upward.* The spine starts listing requirements instead of earning them. Move the list to the appendix.
- *The summary spine.* Chapters become précis of their own appendices. Delete sentences that exist only because an appendix says them.
- *Unearned confidence.* State costs and residuals. Invite disagreement.
- *Uniform density.* Chapters may be short. A clear seven-page chapter beats a dense fifteen-page one.

### Three inherited prohibitions

1. **No unpriced mechanism.** Every control states what it costs in latency, engineering effort, operational burden, or capability foregone.
2. **The adversary is a person.** Never the model. If the model is the villain, the reader concludes the answer is a better model.
3. **Never sneer at the naive design.** The reader built it. It was good work under assumptions that no longer hold.

### Grammatical person and voice

- **First person plural while reasoning.** *We* means the author and the reader deriving together. Never the vendor, the platform team, or the organisation.
- **Second person when instructing.** *You decide the fail posture per tier before the outage, not during it.*
- **First person singular never**, except in the front matter, where the author speaks about what this document replaces.
- **Impersonal only in the appendices**, with a named actor: *the gateway MUST reject…*
- Active voice by default. Passive is allowed when the actor is genuinely unknown or deliberately left open.

---

## 5. Numbers, dates, currencies

- Digits for all quantities with units and for anything measurable: *40 ms*, *3 attempts*, *12 tools*. Words for zero through nine when used as ordinary counts in prose: *five switches, not one*.
- Thousands separated by a comma: *1,200 requests*. Decimal point, not comma, notwithstanding the European frame – the document is in English and the reader's tooling is in English.
- **Dates in ISO 8601 in running prose and everywhere else:** *2026-07-31*. No *31 July 2026*, no *July 31*. The document is full of timestamps, retention windows and incident clocks, and one date format across prose, tables, logs and schemas removes a whole class of ambiguity.
- Times of day in 24-hour form with a timezone where it matters: *03:40 UTC*.
- Durations in the largest unit that stays exact: *90 s*, *15 min*, *24 h*, *30 d*. Token lifetimes and retention periods always carry a unit; never *a short TTL* where a number is knowable.
- Latency always with a percentile: *p99 of 40 ms*. A latency figure without a percentile is deleted.
- Currency in euros with the symbol before the figure: *€40,000*. Other currencies with the ISO code: *USD 40,000*.
- Percentages with the symbol, no space: *3%*. Ranges with an en dash and no spaces: *20–40 ms*.

---

## 6. Field-specific standards

- **RFC 2119 / RFC 8174** keywords for normative statements, in the appendices only, in capitals, with the boilerplate interpretation clause stated once at the head of Appendix A.
- **arc42** for section semantics; **C4** for the levels of architectural views, with the level named in every diagram caption.
- **ISO 8601** for dates, times and durations.
- **RFC 5424** severity vocabulary where log levels are discussed.
- **CVSS** only where a vendor advisory is being quoted, never for this project's own risk statements, which use the project's tiering.
- Specification terminology follows the specification: OAuth, OIDC, JWT, DPoP, mTLS, MCP. Where a term is used loosely in the field and precisely in a spec, the precise sense governs and the loose sense is flagged in Appendix H.
- Threat identifiers `T1`–`Tn`, control identifiers by family (`IDN-3`, `ENV-7`), decision identifiers `ADR-nn`, convention identifiers `CONV-nn`. Each namespace is stable across editions; identifiers are retired, never reused.

---

## 7. Specialized apparatus

### Architecture decision records

Every ADR in Appendix B carries, in this order: **title** (a decision stated as an outcome, not a topic – *Derive the envelope per run rather than inherit the agent's role*, never *Envelope derivation*); **status** (proposed, accepted, superseded by ADR-nn); **date**; **context** (the forces, in one paragraph); **decision**; **rejected alternatives**, each with the reason it lost and what it would have been good for; **consequences**, split into what this makes easy and what it makes hard; **cost**; **revisit trigger** – the specific change in the world that would reopen this decision.

Two rules govern the set. An ADR whose rejected alternatives are strawmen is a defect: at least one rejected option must be something a competent architect would plausibly have chosen, and it must be argued at its strongest. And an ADR with no revisit trigger is not finished, because a decision that cannot expire is a belief.

Target: around thirty. If the count climbs past forty, decisions are being recorded that were never actually decided.

### Artefacts

Where a thing has a wire format, show the thing. A decoded token, a policy rule, a refusal payload, an evidence event, an approval record. Artefacts are shown as bytes in fenced blocks, are valid against the schema in Appendix D, and carry a one-line caption saying what to look at. An example that does not validate is a bug in the document.

### Mechanism sections

Each mechanism in Part II runs: the promise a competent engineer would like to believe, the circumstance in which it fails, the **worked moment** that shows the failure on the fixed cast, the move that survives, the artefact, the cost, and how you would know it had quietly stopped working. Part I and Part III use the same sandwich where the chapter is derivational or operational rather than purely abstract. **[CONV-015]** The worked moment is 150–400 words on Borealis, one mechanism, one decision point; it is not a scene and it does not defer the answer. Inventory and rules are in `worked-moments.md`.

**This rhythm is never printed, never named in a heading, and never announced.** Any draft that includes a section called *The promise* or *Worked example* has failed the rule.

### The residual

Each part ends with a short statement of what the adversary can still do after everything in the part is built. It is never omitted, never softened, and never phrased as future work when it is in fact a limitation.

---

## 8. Reproduction standards: figures, tables, images

**Figures.** Three admissible kinds, and no fourth.

*Schematics* live in the spine and exist for comprehension: a trust boundary, a decision path, a lifecycle, an intersection test. Mermaid only, per `CONV-013`. At most three per chapter and roughly one per three pages. The caption states the **question the figure answers**, phrased as a question. The figure is placed **after** the claim it illustrates, never before, because a diagram arriving before the answer is a puzzle. It must be readable in fifteen seconds. It carries no legend, because a figure that needs a legend has failed. And it is subject to **the deletion test** exactly as markers are: remove every figure and the prose must remain complete and correct. If a schematic is easier to understand than the paragraph beside it, delete the paragraph, not the schematic.

*Views* are the architectural ones and live in Appendix B. Every caption states its question and names its C4 level: *Figure B.6 – C2. Which components see a run credential, and where is it verified?* A spine schematic is not a view and is never captioned as one; conflating the two is how a document ends up with two competing architectural descriptions and no authority over either.

*Artefacts* are the bytes themselves and count as figures for numbering.

Generated illustration images follow `manifesto.md` §10.13 and the placement map in `worked-moments.md`. Rules: never load-bearing, never a substitute for a schematic or a view, placed after the worked moment they anchor, captioned with the idea not the image, always intelligible in greyscale.

**Tables.** For enumerable facts only – matrices, ceilings, postures, mappings. A table that carries an argument is a section that has given up. Every table has a number, a caption, and a stated unit for every numeric column.

**Colour.** Never carries meaning on its own. The PDF must survive greyscale printing and the HTML must survive a colour-blind reader; encoding is by position, label or shape.

**Attribution.** Diagrams are the author's own unless captioned otherwise. Anything adapted from a specification or a published source names it in the caption and cites it numerically.

---

## 9. Indexes and apparatus

The HTML edition carries no index; search does that job. The PDF carries two, both generated:

- A **term index**, restricted to substantive discussion. A term mentioned in passing is not indexed; a term defined, argued or specified is.
- A **decision index**, mapping every ADR to the section in which it is argued and the requirements in Appendix A that depend on it. This is the auditor's entry point and the closest thing the document has to a map of its own reasoning.

Appendix H is a glossary rather than an index, and carries a standing obligation: any term the field commonly uses in two senses is listed with both senses and a statement of which one governs here.

---

## 10. Length and pace

| Unit | Target |
|---|---|
| Whole document | 300–350 pages |
| Narrative spine | 120–150 pages |
| Appendices and references | 150–200 pages |
| Chapter | 6–10 pages; 12 is a warning, 15 means it is two chapters |
| Introduction | 8 pages, complete on its own |
| Section within a chapter | 400–900 words |
| ADR | 400–700 words |

Pace rule: a reader who opens the document at a random page should reach something useful – a claim they can act on, an artefact, a cost, a decision – within one page in either direction.

---

## 11. The author's voice

The author appears explicitly in exactly two places: the front matter, where the supersession of the earlier documents is stated in the first person and the reason for it is given plainly; and the residual sections, where the limits of the author's own knowledge are marked as such. Everywhere else the author is present as judgement rather than as a person – this design was chosen, that alternative was rejected, this cost is accepted.

Certainty is graded and the grades are visible. *This is settled* for anything a specification or a fifty-year-old principle decides. *This is our judgement, and here is the cost of being wrong* for the project's own positions. *This is unsolved* where the field has no answer, stated without hedging and without a consoling sentence afterwards. False confidence is the characteristic sin of reference architectures and the fastest way to lose the only readers worth having: the ones who have run one of these systems and know where it hurts.

---

## 12. Editorial process

The project uses the three-role editorial pipeline: draft editor (`role-1-draft-editor.md`), development-line editor (`role-2-development-line-editor.md`), copy editor (`role-3-copy-editor.md`). Roles run sequentially per chapter. `role-0-outliner.md` handles source extraction into `outline.md` and `references.bib`. `role-4-acquiring-editor.md` reads the assembled PDF blind at the end.

Two project-specific gates sit inside the copy-edit pass, both mechanical and both non-negotiable:

- **The deletion test.** Strip all markers from the chapter; the prose must remain complete and correct.
- **The normative test.** No RFC 2119 keyword appears anywhere in the spine, and no requirement is stated in both the spine and the register.

A chapter that fails either gate does not ship, regardless of how good the prose is.

---

*Version 0.2 – 2026-08-02. Clarity-first rewrite of §4 after the first spine draft failed the read-aloud test.*
