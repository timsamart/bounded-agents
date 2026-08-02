# Governance

**Model:** benevolent lead author.

The manuscript states architectural claims. Community proposes improvements;
the lead author decides contested claims that change the spine.

## Roles

| Role | Who | Decides |
|---|---|---|
| Lead author | Timo Sam | Spine claims, edition cuts, release tags |
| Contributor | Anyone with a merged PR | Own edits within review feedback |
| Maintainer | Named later if needed | Day-to-day triage; not claim ownership |

## Decision path

1. Issue for substantive change (claim, invariant, ADR, appendix shape).
2. Discussion; disagreement is expected and useful.
3. PR against `main` with one concern.
4. Lead author merges or rejects with a short reason.

Typo and clarity PRs do not need an issue first.

## Releases

Tagged `v*` builds produce a PDF artefact. Draft editions may carry
`-draft` in the version. Only the lead author cuts releases until a
maintainer group is named here.

## Revisiting this file

If a maintainer group forms, replace this model explicitly rather than
letting informal practice diverge from the text.
