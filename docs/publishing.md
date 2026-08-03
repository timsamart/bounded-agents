# Publishing

## Editions

- `main` is the living draft.
- Tagged releases use SemVer with an optional `-draft` suffix (`v0.1.0-draft`).
- Only the lead author cuts tags until maintainers are named in `GOVERNANCE.md`.

## How readers get the book

| Channel | When | URL / location |
|---|---|---|
| GitHub Pages (HTML) | Every push to `main` | https://timsamart.github.io/bounded-agents/ |
| Continuous PDF pre-release | Every push to `main` | [latest-draft / bounded-agents.pdf](https://github.com/timsamart/bounded-agents/releases/download/latest-draft/bounded-agents.pdf) |
| Actions artefact (PDF) | `main`, PRs, tags, manual runs | Workflow run → artefact `bounded-agents.pdf` (90-day retention) |
| Versioned release | Git tag `v*` | Draft GitHub Release with PDF attached; author publishes when ready |

The `latest-draft` tag is a **pre-release** only. It is not a production "Latest" edition. Numbered public releases stay on intentional `v*` tags.

GitHub Pages must use **Settings → Pages → Build and deployment → Source: GitHub Actions** (not a branch deploy).

## CI pipeline

Workflow: `.github/workflows/build-pdf.yml` (`Build PDF and Pages`)

**Triggers**

- `push` to `main`
- `pull_request` targeting `main` (build + verify + PDF artefact; no Pages deploy, no release mutation)
- `push` tags `v*`
- `workflow_dispatch`

**Jobs**

1. `build` — pandoc, Playwright Chromium, `pypdf`
   - `python build/build_spine_pdf.py` → `build/spine.html` + `build/bounded-agents.pdf`
   - `python build/verify_links.py` (fails the job on missing anchors)
   - `python build/prepare_pages.py` → `build/site/` (`index.html`, `spine-pdf.css`, `.nojekyll`)
   - Upload PDF artefact `bounded-agents.pdf`
   - On `main`: upload Pages artefact from `build/site/`
   - On `v*` tags: create a **draft** GitHub Release with the PDF
   - On `main` push: create or update the `latest-draft` pre-release (`gh release upload --clobber`)
2. `deploy-pages` — on `main` only; `actions/deploy-pages` into the `github-pages` environment

Permissions used: `contents: write` (releases), `pages: write`, `id-token: write` (Pages). No other secrets.

## What a versioned release contains

1. Git tag `v*`
2. CI builds `build/bounded-agents.pdf` from `chapters/` + `references.bib`
3. Draft GitHub Release attaches the PDF and generated notes
4. Lead author reviews and publishes the draft when the cut is intentional

HTML on Pages always tracks `main`; it is not frozen to a `v*` tag unless you add a separate versioned Pages workflow later.

## Local check before tagging

```bash
python build/build_spine_pdf.py
python build/verify_links.py
python build/prepare_pages.py
```

Open `build/site/index.html` for a Pages-shaped preview.

## Second Brain mirror

The author's private Second Brain folder points here as source of truth for
the published spine. Do not treat that private path as the community edit
target.
