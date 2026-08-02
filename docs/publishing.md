# Publishing

## Editions

- `main` is the living draft.
- Tagged releases use SemVer with an optional `-draft` suffix (`v0.1.0-draft`).
- Only the lead author cuts tags until maintainers are named in `GOVERNANCE.md`.

## What a release contains

1. Git tag `v*`
2. CI builds `build/bounded-agents.pdf` from `chapters/` + `references.bib`
3. GitHub Release attaches the PDF and notes which chapters changed

## Local check before tagging

```bash
python build/build_spine_pdf.py
python build/verify_links.py
```

## Second Brain mirror

The author's private Second Brain folder points here as source of truth for
the published spine. Do not treat that private path as the community edit
target.
