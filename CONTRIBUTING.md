# Contributing

PRs welcome. One concern per PR. Read `voice.md` §4 (clarity beats cleverness)
before editing prose.

## License of your contribution

By opening a pull request you agree that:

- manuscript edits are contributed under **CC BY 4.0**
- script/CI edits are contributed under **Apache-2.0**
- you have the right to contribute the material

No CLA. Keep lead-author credit intact (`NOTICE`, cover, `CITATION.cff`,
`AUTHORS.md`). Do not remove or rephrase it. Add yourself to
`CONTRIBUTORS.md` in the same PR when you land a non-trivial change.

## What belongs where

| Change | First step |
|---|---|
| Typo, broken link, formatting | PR directly |
| Clarity rewrite in one chapter | PR; say which paragraphs moved |
| New bibliography entry | PR; follow CONV-005/006 in `conventions.md`; no invented citations |
| Substantive claim change | Open an issue first; lead author merges spine-affecting changes |
| New ADR or appendix content | Issue with proposed ID; stub under `decisions/` or `appendices/` |

## Editorial bar

- British English, answer-first, no em dashes, no RFC 2119 voice in the spine
- Prefer concrete nouns over nested abstractions
- Markers like `[citation needed:…]` stay until a real source lands
- Do not invent measured results to close a gap

## Build check

```bash
python build/build_spine_pdf.py
```

PDF and HTML land under `build/` (gitignored). CI builds on tags.

## Review

Lead author retains final call on architectural claims. See `GOVERNANCE.md`.
