# Changelog

## Unreleased

- New feature **D10 — raw reads accepted** (suggested by a reader): 6 Y, 5 P, 2 N, 1 n.d. among the 14 platforms, each
  with source and verbatim quotation; 6 new sources. P is used where only some read technologies or organisms
  are accepted, or reads are stored but not processed.
- Web page on GitHub Pages, generated from the CSV and the evidence file (filters, source and quotation for every value).
- Methodology diagram (METHODOLOGY.md and web page).
- Issue templates to suggest a new feature or a new platform.
- Official website and public source-code links for every platform (columns `website`, `source_code`).

## v1.0.0 — 2026-10-02

First public version: 15 platforms, 9 features, 60 sources.

Values changed during the re-check against current sources, before publication:
- BIGSdb-Pasteur, PubMLST — D9 P → n.d.: the built-in sample table was removed from BIGSdb in 2019 (issue #257).
- CGE — row now describes genepi.dk: the 2016 Bacterial Analysis Platform was withdrawn and the legacy
  website is retiring (notice of 2026-08-01). D2 → P, D3 → N, D4, D5 and D7 → n.d.
- Galaxy — D4 n.d. → P (Sample Sheets, release 25.1); D9 P → n.d. (sample tracking removed in 2017).
- AusTrakka — D2 n.d. → N (public code without a licence).
- Pathoplexus — D7 n.d. → P (external link-out tools).
- IRIDA Next added as the successor of IRIDA.
