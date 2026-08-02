# Source Conventions

<!--
Rules for writing the markdown source of Governed Agentic Infrastructure.
These rules are mechanical: they govern how the source is structured, named
and labelled, not what the prose says or how it reads. Voice and style live
in voice.md.

Each convention is a numbered entry with a stable identifier. Identifiers are
never reused or renumbered. New conventions take the next available number.
-->

## CONV-001 · Line wrapping in paragraphs

**Status:** Accepted · 2026-07-31

**Context.** Hard line breaks at fixed columns are a relic of fixed-width terminals. Modern editors soft-wrap, diff tools highlight intra-line changes, and the markdown engine reflows on render. Hard wrapping creates spurious diffs on every sentence edit and serves no rendering purpose.

**Decision.** Do not break paragraph lines in the source. One paragraph is one source line. Tables, code blocks, list items and any construct requiring structural newlines remain wrapped per their own syntax.

**Consequences.** Diffs are accurate at prose level. Search and replace works across whole sentences. Editors without soft wrap are unpleasant; acceptable.

## CONV-002 · Working quotation format in outline.md

**Status:** Accepted · 2026-07-31

**Context.** `outline.md` gathers working quotations before drafting. Each must bind unambiguously to its bibliography entry so that citekey renames surface as broken references rather than rotting silently, and so the draft editor can copy the marker into the chapter without inferring the key from prose attribution. Quote and analytical note must travel together through card reordering.

**Decision.** Every working quotation is introduced by a pandoc-citeproc marker on the block-quote line, followed by an analytical note on a `>` continuation line inside the same block-quote, prefixed with the literal label `Analytical note:`:

    > [@citekey, p. X] "Quoted passage."
    >
    > Analytical note: how this lands in the chapter argument.

Marker variants: whole-work `[@citekey]`; specification section `[@rfc9449, §5.2]`; regulatory article `[@eu2022dora, Art. 30(3)]`; online source without pagination `[@citekey]`; pending verification `[@citekey, p. X, verification TBD]`. Resolve TBD qualifiers in place.

**Consequences.** A citekey rename is one grep. Role 1 refuses cards whose quotations lack markers. Note and quote stay bound.

## CONV-003 · Chapter file naming

**Status:** Accepted · 2026-07-31

**Context.** The build consumes chapter files in alphabetical order. A flat global sequence (`NN-slug.md`) makes insertion painful. A hierarchical scheme mirrors the document's structure in the filesystem and keeps identifiers stable within a grouping.

**Decision.** Chapter files live in `chapters/` and follow `P.C-slug.md`, where `P` is the grouping number per the map in `toc.md`, `C` is the sequence within the grouping with `0` reserved for the part divider, and `slug` is lowercase ASCII with hyphens. Groupings without a divider (front matter, appendices, references) start at `1`. Single digits until a grouping reaches ten entries, then zero-pad.

**Consequences.** Build order is visible in a directory listing. Inserting a chapter renumbers only within its grouping. When a chapter is renamed, update `toc.md` and `outline.md` cross-references in the same revision.

## CONV-004 · Bibliography is a single BibTeX file

**Status:** Accepted · 2026-07-31

**Context.** The bibliography is the authoritative source for every citation. Splitting it hinders deduplication; pandoc-citeproc handles one large file efficiently.

**Decision.** All entries live in `references.bib` at the project root. No per-chapter bibliographies. Comments and working section dividers are permitted and do not affect the rendered list, which is numeric and ordered by first appearance (see `voice.md` §3).

**Consequences.** One file to edit. Keys unique project-wide. Working notes stripped at render.

## CONV-005 · Citation keys

**Status:** Accepted · 2026-07-31

**Context.** Keys must be unique, stable and readable at the point of citation. This project's corpus is dominated by specifications, regulations and vendor documentation rather than authored books, so a surname-year scheme alone collides and reads badly.

**Decision.** Keys take the form `creatorYYYYshorttitle`, lowercase ASCII, no accents. `creator` is the first author's surname; for standards bodies and corporate authors it is a short institutional token (`ietf`, `w3c`, `nist`, `enisa`, `eu`, `anthropic`); for specifications with a canonical identifier the identifier is the key (`rfc9449`, `rfc8693`, `rfc2119`). Regulations use jurisdiction plus year plus short name (`eu2022dora`, `eu2024aiact`, `eu2016gdpr`).

**Consequences.** A reader recognises `rfc9449` at the point of citation. Specification keys survive title changes. Vendor documentation keys carry the vendor token and the year of retrieval, which makes staleness visible in the source.

## CONV-006 · BibTeX entry formatting

**Status:** Accepted · 2026-07-31

**Context.** Machine-generated exports and hand-added entries drift toward mixed formatting. Parsers accept anything; diffs and the "add field, forget comma" failure do not.

**Decision.** Single space around `=`, and a trailing comma on every field line including the last. No field-name alignment – it breaks whenever a longer field name is added.

**Consequences.** New fields are single-line diffs. `git blame` stays precise. No rendering impact.

## CONV-007 · Marker grammar and the deletion test

**Status:** Accepted · 2026-07-31

**Context.** The document's central promise is that detail is reachable without being intrusive. That promise is easy to state and easy to violate one sentence at a time, so it needs a mechanical form and a mechanical test. Three kinds of detail are reachable from the spine – a decision, a specification, a source – and if each grew its own notation the reader would have to learn three systems and would learn none.

**Decision.** Exactly three marker classes, sharing one visual grammar (square brackets, same typographic weight, mid-grey in both targets):

| Marker | Points to | Placement |
|---|---|---|
| `[ADR-014]` | Appendix B, one decision record | End of the paragraph that argues the decision |
| `[A-3.2]` | An appendix, at subsection granularity | End of the sentence whose detail lives there |
| `[17]` | The reference list | End of the sentence, before the full stop |

Markers never appear mid-clause, never in a heading, and never more than two on one sentence. Budget: roughly six per page.

**The deletion test.** Strip every marker from a page. If any sentence becomes incomplete, ambiguous or wrong, the marker was carrying meaning and the sentence is rewritten. This runs as a gate in the copy-edit pass (`role-3-copy-editor.md`) and is not waivable.

**Consequences.** The reader learns one system in the first three pages, and learns it by encountering it rather than by being told. Detail is always one jump away and never in the path. Any device that cannot be expressed in this grammar – hover text, sidebars, inline collapsibles as the sole disclosure route – is out of the document, which is a real constraint and is intended.

## CONV-008 · Normative keywords confined to the appendices

**Status:** Accepted · 2026-07-31

**Context.** A document that both argues and specifies will state the same rule twice if it is not prevented from doing so, and a reader who finds two statements of one rule must decide which is authoritative. That decision is the reader's, made under time pressure, and it will sometimes be made wrongly.

**Decision.** RFC 2119 and RFC 8174 keywords – MUST, MUST NOT, SHOULD, SHOULD NOT, MAY, REQUIRED, SHALL, OPTIONAL – appear only in the appendices, in capitals, under the interpretation clause stated once at the head of Appendix A. In the spine, requirements are argued in plain declarative prose. No requirement is stated normatively in two places.

**Consequences.** The register in Appendix A is the single authority for what is required, which is what makes it handable to an auditor on its own. The spine must earn its requirements by argument rather than assert them by keyword, which is harder to write and is the point. Grep for the keyword list across `chapters/` is a copy-edit gate.

## CONV-009 · Every device must work in both render targets

**Status:** Accepted · 2026-07-31

**Context.** The build produces a paginated PDF and an HTML edition from one source. Progressive disclosure is natural in HTML and unnatural in print, and the temptation is to design for the web and degrade the PDF.

**Decision.** No device enters the document unless it works in both targets. A marker expands in place in HTML and resolves to a page reference in the PDF; both behaviours come from the same source token. Colour never carries meaning. Figures are legible in greyscale. Tables fit the PDF measure – a table wider than the page is a table that should be an appendix.

**Consequences.** Some genuinely good web affordances are unavailable. The compensation is that the PDF is not a second-class artefact, which matters because the PDF is what gets attached to an email and read on a train.

## CONV-010 · Artefacts are real and validate

**Status:** Accepted · 2026-07-31

**Context.** The document shows wire formats – credentials, decisions, refusals, evidence events – because the audience trusts bytes over prose. An example that does not parse or does not match its schema damages more trust than it built.

**Decision.** Every artefact block in the spine is valid against the corresponding schema in Appendix D, and every schema in Appendix D carries at least one example that validates against it. Artefacts are fenced with a language tag, carry a one-line caption stating what to look at, and use consistent fictional identifiers across the document (see `outline.md`, cast and identifiers).

**Consequences.** A validation pass belongs in the build. Changing a schema means finding every artefact that uses it, which is the intended cost of showing bytes.

## CONV-011 · Identifier namespaces

**Status:** Accepted · 2026-07-31

**Context.** The document carries five parallel identifier sets, cross-referenced from each other and from an external audience's own documentation. Reuse of a retired identifier silently invalidates someone else's traceability matrix.

**Decision.** Five namespaces, each stable across editions: threats `T1`…`Tn`; controls by family and number (`IDN-3`, `ENV-7`, `APV-2`, `TUL-5`, `DAT-4`, `EVD-6`, `BUD-1`, `EGR-2`, `OPS-8`, `GOV-3`); decisions `ADR-nn`; conventions `CONV-nn`; drills `DRL-nn`. Identifiers are **retired, never reused**. A retired identifier keeps a stub entry saying what it was and what replaced it.

**Consequences.** External traceability survives editions. The registers accumulate tombstones, which is the correct trade.

## CONV-013 · Mermaid is the only diagram source

**Status:** Accepted · 2026-07-31

**Context.** The document needs schematics in the spine (see `voice.md` §8) and architectural views in Appendix B, rendered to both PDF and HTML from one source (`CONV-009`). Any binary diagram format creates a second source of truth that drifts from the prose and cannot be reviewed in a diff. Mermaid is text, diffs cleanly, renders in both targets, and is already the house standard for diagrams in this workspace.

**Decision.** All diagrams are Mermaid, in fenced blocks tagged `mermaid`, in the chapter source. Rules:

- **One theme, defined once** in `build/mermaid-config.json`, never per diagram. No `%%{init}%%` blocks in chapter source, no inline `style` or `classDef` statements. A diagram that needs local styling is a diagram doing too much. The theme is `neutral` with a serif face matching the body text, mid-grey borders and near-white fills, so that a figure prints and photocopies without loss. Renderer: `@mermaid-js/mermaid-cli`, pinned; verified at 11.16.0 on 2026-07-31.
- **No colour semantics** (`CONV-009`). Structure is carried by shape, position, subgraph grouping and edge style. Solid edges are paths the platform mediates; dashed edges are paths it does not. That single distinction is the only edge vocabulary the document uses, and it is stated in prose the first time it appears rather than in a legend.
- **Node text is short.** Roughly six words per line, at most three lines, using `<br/>` for breaks. A node holding a sentence belongs in the prose.
- **Diagram types.** `flowchart` for schematics and structure, `sequenceDiagram` where causality and ordering genuinely carry the point, `stateDiagram-v2` for lifecycles. Nothing else without an entry in this file.
- **Figure numbering** is per chapter (`Figure 1.2`) and per appendix (`Figure B.6`), assigned in source order, with the caption in italics immediately beneath the block.
- **Rendering.** The build renders Mermaid to SVG for HTML and to a vector asset for the PDF. A diagram that fails to render fails the build; it is never allowed to degrade to a fenced code block in the output, because a reader must never be shown diagram source.

**Consequences.** Diagrams are reviewable in a pull request, which is the main reason for the choice. The build acquires a Mermaid rendering dependency, which is the cost, and it must be pinned. The prohibition on per-diagram styling will feel restrictive at exactly the moment someone wants to highlight one node; the answer in that case is a sentence of prose, which the reader can search and a reviewer can argue with.

## CONV-014 · Working documents obey the prose rules

**Status:** Accepted · 2026-07-31

**Context.** The first generation of this project's working documents (`manifesto.md`, `voice.md`, `concept.md`, `toc.md`, `outline.md`, this file) was written with em dashes throughout, while `voice.md` §1 bans em dashes from the manuscript. A style guide that violates its own rule teaches everyone reading it that the rule is decorative, and the copy-edit gate loses its authority before the first chapter reaches it.

**Decision.** The prose rules in `voice.md` §1 and §5 – no em dashes, British spelling, ISO 8601 dates, serial comma – apply to the working documents as well as to the manuscript. The role files, the templates and the chapter source are all in scope. The exception is quoted material and anything inside code formatting, exactly as in the manuscript.

**Consequences.** A one-off normalisation pass was run over the working documents on 2026-07-31, replacing em dashes with spaced en dashes. Anything harvested from `archive/` needs the same treatment when it is carried across, and this is the copy editor's job the moment archived phrasing enters a chapter.

## CONV-012 · ADR records

**Status:** Accepted · 2026-07-31

**Context.** The decision layer is the project's main contribution, and decision records rot in two characteristic ways: they multiply until nobody reads them, and they justify rather than record.

**Decision.** ADRs live in Appendix B, in the fixed field order given in `voice.md` §7. Two admission rules. An ADR must name at least one rejected alternative that a competent architect would plausibly have chosen, argued at its strongest – a record whose alternatives are strawmen is a defect, not a weak record. An ADR must state a revisit trigger: the specific change in the world that would reopen it. Target set size is around thirty; past forty, decisions are being recorded that were never made.

**Consequences.** Writing an ADR is expensive, which is the throttle. The revisit triggers collectively form the document's expiry schedule and are extracted into chapter 20.

## CONV-015 · Worked moments in the spine

**Status:** Accepted · 2026-07-31

**Context.** The reference architecture teaches by derivation and rejects scene openers, but abstract mechanisms still need a pragmatic middle layer between the reader's lived context and the general form. Without it, Part II reads as conclusions without the intuition that makes someone who has not built one of these believe them. Appendix E walkthroughs are too far from the claim; one physical anchor per paragraph is not enough.

**Decision.** Each mechanism chapter carries one or more **worked moments** in its outline card: 150–400 words on the fixed cast (Borealis, `claims-triage`, Marta, Kai), one mechanism, one decision point, numbers where possible. They are placed in the performed rhythm after the promise and its failure and before the surviving move and the artefact. They are not scenes: no dialogue arc, no suspense, no chapter opener. Inventory, illustration map, and Appendix E assembly live in `worked-moments.md`. A mechanism chapter card without at least one worked moment is not `[DRAFT-READY]`.

**Deletion test, split.** Remove one worked moment and the argument must stand. Remove all worked moments from a chapter and the chapter must lose intuitive grip for a reader new to the field.

**Consequences.** Role 1 drafts from the card's worked-moment lines. Role 2 checks that moments use cast identifiers consistently with Appendix D. Appendix E is compiled from spine moments rather than written with a separate cast.
