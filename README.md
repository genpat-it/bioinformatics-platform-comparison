# Genomic-surveillance platform comparison

> **Anyone can correct or update this table by opening a pull request.**
> If you develop or use one of these platforms and a value is wrong, outdated or missing, please
> [open a pull request](CONTRIBUTING.md) — or, if you prefer, an
> [issue](../../issues/new?template=correction.yml) — with a public source for the new value. Accepted
> corrections are recorded in the [changelog](CHANGELOG.md). You can also
> [suggest a new feature to compare](../../issues/new?template=feature.yml) or
> [a platform to add](../../issues/new?template=platform.yml).
>
> **Browse the table online:** https://genpat-it.github.io/bioinformatics-platform-comparison/

## How these values were obtained — please read

This table reports **what we could learn from public sources only**: published articles and preprints,
official documentation, licence files, source repositories, release notes and public web pages of each
platform. **We do not hold user or administrator accounts on most of these platforms and have not used them
ourselves**, so we could not verify features that are not publicly documented.

As a consequence:

- a value may be **incomplete or outdated**: a platform may offer a feature that its public documentation
  does not describe, or may have changed since the date in the `Last checked` column;
- **n.d.** (*not documented*) means only that we found no public source — **not** that the feature is absent;
- the table describes **documented features**, not the quality, reliability or suitability of any platform,
  and is **not a ranking**.

Platform developers and users who know better are explicitly invited to correct us by pull request.

A documented, open and correctable comparison of software platforms used for bacterial and viral genomic
surveillance. It supports the comparison discussed in:

> de Ruvo A. *et al.* GENPAT: an extensible multi-tenant architecture for cooperative One Health genomic
> surveillance (manuscript submitted, 2026).

**Every value is backed by a cited source and a verbatim supporting passage.** The authors hold no accounts on
most of the platforms compared, so no value rests on our own use. The table is meant to be corrected in the open.

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
| D6 | Microorganisms covered |
| D7 | Phylogeny, metadata and map in one view |
| D8 | Built-in submission, brokerage or structured exchange with an external repository or authority (a plain download does not count) |
| D9 | Integration with a laboratory information management system (LIMS) |
| D10 | **Raw reads accepted.** Raw sequencing reads (e.g. FASTQ) accepted as input and processed by the platform, rather than only assemblies, consensus sequences or derived results |

<!-- TABLE:START -->
| Platform | Code | Status | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | Last checked |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [GENPAT / COHESIVE](https://genpat.izs.it) | [source](https://github.com/genpat-it) | authors' own platform (see disclosure) | Y | Y<sup>*</sup> | Y | Y | Y | B,V | Y | P<sup>*</sup> | Y | Y<sup>*</sup> | 2026-10-02 |
| [BIGSdb-Pasteur](https://bigsdb.pasteur.fr) | [source](https://github.com/kjolley/BIGSdb) | active | P† | Y<sup>*</sup> | Y | Y | P† | B | P | n.d. | n.d.<sup>*</sup> | N<sup>*</sup> | 2026-10-02 |
| [PubMLST](https://pubmlst.org) | [source](https://github.com/kjolley/BIGSdb) | active | P† | Y<sup>*</sup> | Y | Y | P† | B,F<sup>*</sup> | P | n.d. | n.d.<sup>*</sup> | N<sup>*</sup> | 2026-10-02 |
| [EnteroBase](https://enterobase.warwick.ac.uk) | [source](https://bitbucket.org/enterobase/enterobase-web) | active | P | N<sup>*</sup> | Y | P | P | B | P | P<sup>*</sup> | n.d. | P<sup>*</sup> | 2026-10-02 |
| [CGE (genepi.dk)](https://genepi.dk) | [source](https://bitbucket.org/genomicepidemiology) | 2016 platform withdrawn; legacy site retiring (notice 2026-08-01) | P<sup>*</sup> | P<sup>*</sup> | N<sup>*</sup> | n.d. | n.d. | B | n.d. | n.d. | n.d. | Y<sup>*</sup> | 2026-10-02 |
| [IRIDA](https://phac-nml.github.io/irida-documentation/) | [source](https://github.com/phac-nml/irida) | no longer developed; successor IRIDA Next | Y | Y<sup>*</sup> | Y | Y | Y | B§ | P<sup>*</sup> | Y<sup>*</sup> | n.d. | Y<sup>*</sup> | 2026-10-02 |
| [IRIDA Next](https://phac-nml.github.io/irida-next/) | [source](https://github.com/phac-nml/irida-next) | active (no tagged releases) | Y | Y<sup>*</sup> | Y | Y | Y<sup>*</sup> | n.d. | n.d. | n.d.<sup>*</sup> | n.d. | Y<sup>*</sup> | 2026-10-02 |
| [Galaxy](https://galaxyproject.org) | [source](https://github.com/galaxyproject/galaxy) | active | Y | Y<sup>*</sup> | P | P<sup>*</sup> | Y | B,V,F | P | P<sup>*</sup> | n.d.<sup>*</sup> | Y<sup>*</sup> | 2026-10-02 |
| [Pathogenwatch](https://pathogen.watch) | [source](https://github.com/pathogenwatch-oss) | active | P<sup>*</sup> | N<sup>*</sup> | P | P | N | B,V,F | Y | n.d. | n.d. | P<sup>*</sup> | 2026-10-02 |
| [AusTrakka](https://austrakka.net) | [source](https://github.com/AusTrakka) | active | N | N<sup>*</sup> | Y | P | P | B,V | P | n.d. | n.d. | Y<sup>*</sup> | 2026-10-02 |
| [NCBI Pathogen Detection](https://www.ncbi.nlm.nih.gov/pathogens/) | — | active | N | P<sup>*</sup> | N<sup>*</sup> | P | N | B,F | P | Y<sup>*</sup> | n.d. | P<sup>*</sup> | 2026-10-02 |
| [EFSA One Health WGS System](https://www.efsa.europa.eu/en/topics/topic/whole-genome-sequencing-foodborne-outbreaks) | [source](https://dev.azure.com/efsa-devops/EFSA/_git/efsa.wgs.onehealth) | active | N | P<sup>*</sup> | Y | N‡ | P | B<sup>*</sup> | P | Y‡<sup>*</sup> | n.d. | Y<sup>*</sup> | 2026-10-02 |
| [Nextstrain](https://nextstrain.org) | [source](https://github.com/nextstrain) | active | Y | Y<sup>*</sup> | P | P | Y | B,V | Y | n.d. | n.d. | P<sup>*</sup> | 2026-10-02 |
| [GISAID](https://gisaid.org) | — | active | N§ | N§<sup>*</sup> | P | n.d. | n.d. | V | P | N | n.d. | n.d.<sup>*</sup> | 2026-10-02 |
| [Pathoplexus](https://pathoplexus.org) | [source](https://github.com/loculus-project/loculus) | active | P<sup>*</sup> | Y<sup>*</sup> | P | Y | P | V | P<sup>*</sup> | Y<sup>*</sup> | n.d. | P<sup>*</sup> | 2026-10-02 |

<sup>*</sup> A note qualifies the value; notes are in `data/comparison.csv` (columns `D1_note` … `D9_note`). Platform names link to the official website; **Code** links to the public source code, where one exists.
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

Cite the article above, together with this repository and the date or release you consulted. The date in the
`Last checked` column and the commit history identify the version consulted.

## Licence

Data and documentation: [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE). Scripts: MIT
(see the header of `LICENSE`). Quotations remain the property of their respective authors and are reproduced
as short excerpts for the purpose of citation.
