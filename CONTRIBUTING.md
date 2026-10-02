# Proposing a correction

Corrections are welcome — this is the reason the table is public. A value changes only on the basis of a
source that anyone can check.

## Pull request (preferred)

1. Edit the row in [`data/comparison.csv`](data/comparison.csv): the value (`Y`, `P`, `N`, `n.d.`; organisms
   as `B`, `V`, `F`), the note if useful, the source key in `sources`, and `last_checked` (YYYY-MM-DD).
2. Add the reference to [`data/sources.bib`](data/sources.bib) if it is new.
3. Add the verbatim supporting passage (at most about 40 words), the URL or DOI and the access date to the
   platform's section in [`evidence/EVIDENCE.md`](evidence/EVIDENCE.md).
4. Run `python3 scripts/validate.py` and `python3 scripts/render.py`, and commit the updated `README.md`.
5. Open the pull request and fill in the template. The automatic check must pass.

## Issue

If you prefer not to edit files, open an issue with the "Correction" template, giving the platform, the
feature, the proposed value and the source with its supporting passage.

## What counts as a source

Official documentation, licence files, source repositories, release notes, terms of use, presentations by the
developers, peer-reviewed articles and identified preprints. Personal experience of a platform, screenshots
of a private account or statements without a public source cannot be used, because the next reader could not
check them.

## Maintainers' commitment

Pull requests and issues are reviewed against the rule in [`METHODOLOGY.md`](METHODOLOGY.md). Accepted changes
are recorded in [`CHANGELOG.md`](CHANGELOG.md) and released with a new tag. Developers of a listed platform
are especially welcome to correct their own row.
