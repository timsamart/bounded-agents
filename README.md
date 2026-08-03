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
| [Read online (HTML)](https://timsamart.github.io/bounded-agents/) | Rendered spine on GitHub Pages |
| [Download PDF](https://github.com/timsamart/bounded-agents/releases/download/latest-draft/bounded-agents.pdf) | Latest draft from `main` (stable URL) |
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

## Read online and download

| Format | Link |
|---|---|
| **Read online (HTML)** | https://timsamart.github.io/bounded-agents/ |
| **Latest draft PDF** (stable URL) | https://github.com/timsamart/bounded-agents/releases/download/latest-draft/bounded-agents.pdf |
| **Versioned editions** | [GitHub Releases](https://github.com/timsamart/bounded-agents/releases) on `v*` tags (draft until the author publishes) |

CI (`.github/workflows/build-pdf.yml`) builds `build/spine.html` and `build/bounded-agents.pdf` on every push to `main`, on pull requests targeting `main`, on `v*` tags, and via `workflow_dispatch`. The job runs `build/build_spine_pdf.py`, then `build/verify_links.py` as a gate.

On `main` pushes the workflow also:

1. Prepares a static site (`build/prepare_pages.py` → `build/site/`) and deploys it to **GitHub Pages** (Settings → Pages → source: **GitHub Actions**)
2. Uploads a GitHub Actions artefact named `bounded-agents.pdf` (90-day retention)
3. Refreshes the `latest-draft` **pre-release** PDF attachment

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
