# Bounded Agents

**Governed Agentic Infrastructure** – how to give AI agents real authority when the model may be hostile.

Timo Sam · Edition 0.1 draft · [CC BY 4.0](LICENSE)

This is the public home of the manuscript. The claim in one sentence: a platform can limit what a compromised agent run can do to a set listed before the run started, prove afterwards what it actually did, and stop it within a stated time – without help from the agent.

## Read

| Path | Use |
|---|---|
| [`chapters/`](chapters/) | Narrative spine (Parts I–IV, chapters 1–21) |
| [`decisions/`](decisions/) | ADR-01–ADR-39 (Nygard form) |
| [`appendices/`](appendices/) | Appendices A–H |
| [`references.bib`](references.bib) | Bibliography (citeproc) |
| Releases | Built PDF on each `v*` tag |
| [`toc.md`](toc.md) | Structure and reading altitudes |
| [`voice.md`](voice.md) | Editorial voice (read §4 before editing) |

**Linked reading:** the HTML build preserves internal anchors (TOC, `[ADR-nn]`, `[A-x.y]`, citations). Use the PDF for offline/print; use HTML or markdown when you need clickable navigation.

## Cite

```bibtex
@misc{sam2026boundedagents,
  author = {Sam, Timo},
  title  = {Bounded Agents: Governed Agentic Infrastructure},
  year   = {2026},
  url    = {https://github.com/timsamart/bounded-agents},
  note   = {Edition 0.1 draft},
}
```

Machine-readable: [`CITATION.cff`](CITATION.cff). Attribution is required under CC BY 4.0; see [`NOTICE`](NOTICE).

## Build the PDF

Requires Python 3.11+, [pandoc](https://pandoc.org/) 3.x with citeproc, Playwright Chromium, and `pypdf`.

```bash
pip install playwright pypdf
playwright install chromium
python build/build_spine_pdf.py
```

Outputs: `build/spine.html`, `build/bounded-agents.pdf`.

## Contribute

See [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`GOVERNANCE.md`](GOVERNANCE.md). PRs welcome; lead author retains final call on spine claims.

## License

- Manuscript: [CC BY 4.0](LICENSE)
- Build scripts / CI: [Apache-2.0](LICENSE-APACHE)
