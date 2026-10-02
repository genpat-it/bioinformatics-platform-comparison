# Genomic-surveillance platform comparison

A documented, open and correctable comparison of software platforms used for bacterial and viral genomic
surveillance. It supports the comparison discussed in:

> de Ruvo A. *et al.* GENPAT: an extensible multi-tenant architecture for cooperative One Health genomic
> surveillance (manuscript submitted, 2026).

**Every value is backed by a cited source and a verbatim supporting passage.** The authors hold no accounts on
most of the platforms compared, so no value rests on our own use. If a value is wrong or outdated, please
[open a pull request](CONTRIBUTING.md): the table is meant to be corrected in the open.

## The table

Values as of the date in the last column. **Y** core function of the service or software named in the row ·
**P** available only through the software underlying a hosted service (†), a plug-in, an external component,
a third-party integration, or only in part · **N** a source states that the feature is not available ·
**n.d.** not documented: no source found, which does **not** imply that the feature is absent.
‡ quotation verified on an abstract only · § only source predates 2023. Organisms: **B** bacteria, **V**
viruses, **F** fungi.

| Code | Feature |
|---|---|
| D1 | **Deployment: self-hosted or cloud service.** Can an institution install it on its own infrastructure? Y installable; N only available as a centrally hosted (cloud) service; P only the underlying software or some components are installable |
| D2 | Licence meeting the [Open Source Definition](https://opensource.org/osd); source-available code under another licence, or without one, is N |
| D3 | Data ownership and access control across institutions |
| D4 | Metadata model extensible by an operator without code changes |
| D5 | Operator- or user-added analysis pipelines |
| D6 | Organisms covered |
| D7 | Phylogeny, metadata and map in one view |
| D8 | Built-in submission, brokerage or structured exchange with an external repository or authority (a plain download does not count) |
| D9 | Integration with a laboratory information management system (LIMS) |

<!-- TABLE:START -->
| Platform | Status | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | Last checked |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GENPAT / COHESIVE | authors' own platform (see disclosure) | Y | Y<sup>*</sup> | Y | Y | Y | B,V | Y | P<sup>*</sup> | Y | 2026-10-02 |
| BIGSdb-Pasteur | active | P† | Y<sup>*</sup> | Y | Y | P† | B | P | n.d. | n.d.<sup>*</sup> | 2026-10-02 |
| PubMLST | active | P† | Y<sup>*</sup> | Y | Y | P† | B,F<sup>*</sup> | P | n.d. | n.d.<sup>*</sup> | 2026-10-02 |
| EnteroBase | active | P | N<sup>*</sup> | Y | P | P | B | P | P<sup>*</sup> | n.d. | 2026-10-02 |
| CGE (genepi.dk) | 2016 platform withdrawn; legacy site retiring (notice 2026-08-01) | P<sup>*</sup> | P<sup>*</sup> | N<sup>*</sup> | n.d. | n.d. | B | n.d. | n.d. | n.d. | 2026-10-02 |
| IRIDA | no longer developed; successor IRIDA Next | Y | Y<sup>*</sup> | Y | Y | Y | B§ | P<sup>*</sup> | Y<sup>*</sup> | n.d. | 2026-10-02 |
| IRIDA Next | active (no tagged releases) | Y | Y<sup>*</sup> | Y | Y | Y<sup>*</sup> | n.d. | n.d. | n.d.<sup>*</sup> | n.d. | 2026-10-02 |
| Galaxy | active | Y | Y<sup>*</sup> | P | P<sup>*</sup> | Y | B,V,F | P | P<sup>*</sup> | n.d.<sup>*</sup> | 2026-10-02 |
| Pathogenwatch | active | P<sup>*</sup> | N<sup>*</sup> | P | P | N | B,V,F | Y | n.d. | n.d. | 2026-10-02 |
| AusTrakka | active | N | N<sup>*</sup> | Y | P | P | B,V | P | n.d. | n.d. | 2026-10-02 |
| NCBI Pathogen Detection | active | N | P<sup>*</sup> | N<sup>*</sup> | P | N | B,F | P | Y<sup>*</sup> | n.d. | 2026-10-02 |
| EFSA One Health WGS System | active | N | P<sup>*</sup> | Y | N‡ | P | B<sup>*</sup> | P | Y‡<sup>*</sup> | n.d. | 2026-10-02 |
| Nextstrain | active | Y | Y<sup>*</sup> | P | P | Y | B,V | Y | n.d. | n.d. | 2026-10-02 |
| GISAID | active | N§ | N§<sup>*</sup> | P | n.d. | n.d. | V | P | N | n.d. | 2026-10-02 |
| Pathoplexus | active | P<sup>*</sup> | Y<sup>*</sup> | P | Y | P | V | P<sup>*</sup> | Y<sup>*</sup> | n.d. | 2026-10-02 |

<sup>*</sup> A note qualifies the value; notes are in `data/comparison.csv` (columns `D1_note` … `D9_note`).
<!-- TABLE:END -->

## What is in this repository

| Path | Content |
|---|---|
| [`data/comparison.csv`](data/comparison.csv) | the table, machine-readable: one row per platform, a value and a note per feature, the source keys and the date of the last check |
| [`data/sources.bib`](data/sources.bib) | full references for every source key |
| [`evidence/EVIDENCE.md`](evidence/EVIDENCE.md) | for every cell: value, source and verbatim supporting passage; audit trail of the re-check |
| [`METHODOLOGY.md`](METHODOLOGY.md) | how the comparison was built and checked |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | how to propose a correction |
| [`CHANGELOG.md`](CHANGELOG.md) | every change to a value, with its reason |
| `scripts/` | `validate.py` checks the CSV; `render.py` regenerates the table above |

## Disclosure

The authors develop and operate GENPAT, which appears in the first row. Its values refer to the sections of
the article cited above rather than to an independent source; corrections to it are welcome on the same
terms as for any other row.

## How to cite

Cite the article above, together with this repository and the date or release you consulted. Releases are
tagged so that a given version of the table can be referred to unambiguously.

## Licence

Data and documentation: [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). Scripts: MIT
(see the header of `LICENSE`). Quotations remain the property of their respective authors and are reproduced
as short excerpts for the purpose of citation.
