# Evidence — sources and verbatim supporting passages for every cell

All URLs were accessed on **2 October 2026**. Quotations are verbatim; typographical errors in the originals
are preserved and marked [sic].

**Dimensions.** D1 installable by an institution on its own infrastructure · D2 licence meeting the Open
Source Definition · D3 data ownership and access control across institutions · D4 metadata model extensible
by an operator without code changes · D5 operator- or user-added analysis pipelines · D6 organisms ·
D7 phylogeny, metadata and map in one view · D8 built-in submission, brokerage or structured exchange with
an external repository or authority · D9 integration with a laboratory information management system ·
D10 raw sequencing reads (e.g. FASTQ) accepted as input and processed by the platform (added 2 October 2026;
P where only some read technologies or organisms are accepted, or reads are stored but not processed).

**Values.** Y: core function of the service or software named in the row. P: available only through the
software underlying a hosted service (†), through a plug-in, an external component or a third-party
integration, or only in part. N: a source states that the feature is not available (for D2, also code that
is source-available under a non-open-source licence or without a licence). n.d.: no source found; this does
not imply absence.

**Source status.** Peer-reviewed articles are cited by DOI. Preprints (IRIDA, bioRxiv 2018; Pathogenwatch,
medRxiv 2026) and presentations by the developers (EFSA, AusTrakka) are identified as such. Cells marked ‡
rest on an abstract and are to be confirmed against the full text.

**Platform status.** IRIDA is no longer developed; its successor is IRIDA Next (github.com/phac-nml/irida).
The legacy CGE website (genomicepidemiology.org) has announced its replacement by https://genepi.dk.

---

## (a) Per-platform evidence

### 1. Pasteur BIGSdb (bigsdb.pasteur.fr)

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | P† (the BIGSdb software is installable; the site is a central service) | jolley2018bigsdb, DOI 10.12688/wellcomeopenres.14826.1 | "The underlying BIGSdb software can be locally installed on a Linux machine with as little as 4GB RAM and a single processor" |
| D2 | yes (GPL-3.0) | https://bigsdb.pasteur.fr/policy/ | "This Platform is powered by the BIGSdb software developed at Oxford University (GNU General Public Licence version 3)." |
| D3 | yes | https://bigsdb.pasteur.fr/policy/ (version 2025_08_11) | "Isolates-data, as posted by Contributors, remain the property of said Contributors" … "Isolates-data provided by Contributors can be made publicly available, or private for a defined embargo period." |
| D4 | Y (configured by the operator of the site) | BIGSdb docs https://bigsdb.readthedocs.io/en/latest/dbase_setup.html | "Isolate databases can have any fields defined for the isolate table,allowing [sic] customisation of metadata - these fields are described in the XML file (config.xml) and must match the fields defined in the database itself." |
| D5 | P† (operator plug-ins, BIGSdb software) | jolley2010bigsdb, DOI 10.1186/1471-2105-11-595 | "The software employs a plug-in architecture, allowing additional features and analysis packages to be added by third-parties without modification of the core code." |
| D6 | bacteria | https://bigsdb.pasteur.fr/ | "This web platform hosts collections of curated, open or private databases of bacterial isolates, genomes and genotypes" |
| D7 | partial (GrapeTree/iTOL integrated; tree+map+timeline via external Microreact) | https://bigsdb.readthedocs.io/en/latest/data_analysis/microreact.html | "The generated tree will be uploaded to the Microreact website and displayed. Clicking any node will show its position(s) within the tree, map and timeline." |
| D8 | n.d. | — | (docs only show linking to existing ENA accessions) |
| D9 | n.d. (the built-in sample table described in 2010 was removed in 2019; no external LIMS link documented) | bigsdb_issue257, https://github.com/kjolley/BIGSdb/issues/257 (2019-05-14) | "This has never really worked well and using a proper LIMS system which can be linked to from a BIGSdb record makes more sense." |
| D10 | N (Assemblies only (FASTA contigs). Reads must be assembled before deposition (BIGSdb software).) | jolley2018bigsdb; bigsdbpasteurwga2026; bigsdbdocs2026 ; DOI 10.12688/wellcomeopenres.14826.1 (2018); https://bigsdb.pasteur.fr/whole-genome-assembly-submission-guidelines/ (n.s.) | "BIGSdb works exclusively with assembled nucleotide sequences … Therefore, genomic data present in the sequence read archives must be assembled before deposition into the database." / Pasteur: "Upload the assembly files for each isolate using the box provided." |

Supporting extra: deployment at Pasteur — Brisse, open peer-review report on jolley2018bigsdb (10.21956/wellcomeopenres.16155.r33972): "My group is using the BIGSdb platform to power the Pasteur MLST web site and databases". Projects: https://bigsdb.pasteur.fr/about/ "Single- or multiple-user projects can be created from the web interface to facilitate the analysis of stored data and/or data upload."

### 2. PubMLST (pubmlst.org)

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | P† (the BIGSdb software is installable; PubMLST is centrally hosted) | jolley2018bigsdb | "The underlying BIGSdb software can be locally installed on a Linux machine with as little as 4GB RAM and a single processor" |
| D2 | yes (GPL-3.0) | jolley2018bigsdb (Software availability) | "The source code for BIGSdb, including the RESTful API application, is available from: https://github.com/kjolley/BIGSdb … License: GNU General Public License v3.0" |
| D3 | yes | jolley2018bigsdb | "The BIGSdb platform supports the combination of private and public data, with authorised users able to upload private data that can be shared with specified groups as required." |
| D4 | Y (per-organism fields configured by the operator) | https://pubmlst.org/submit-data ; dbase_setup.html (as above) | "Each organism isolate database has a particular set of fields specific for it, although some fields are found in every database." |
| D5 | P† (as BIGSdb-Pasteur) | jolley2010bigsdb | (same plug-in quote as Pasteur D5) |
| D6 | B, F (mainly bacteria; Candida schemes; one bacteriophage scheme, not counted as viral-surveillance support) | jolley2018bigsdb; https://pubmlst.org/organisms (lists Candida albicans, C. auris, C. glabrata, C. krusei, C. tropicalis) | "PubMLST hosted databases for over 100 species or genera, mainly bacteria, but also included some schemes for eukaryotes and plasmids. In principle, the BIGSdb platform can be used for any organism or virus." |
| D7 | partial (iTOL/GrapeTree; map via external Microreact; native dashboard map for country field only) | jolley2018bigsdb | "Phylogenetic trees can be generated … and visualised with metadata overlays in Interactive Tree of Life or combined with geographical and temporal data for visualisation in the Microreact software" |
| D8 | n.d. | — | — |
| D9 | n.d. (the built-in sample table described in 2010 was removed in 2019; no external LIMS link documented) | bigsdb_issue257, https://github.com/kjolley/BIGSdb/issues/257 (2019-05-14) | "This has never really worked well and using a proper LIMS system which can be linked to from a BIGSdb record makes more sense." |
| D10 | N (Assemblies only (same BIGSdb software). Genome submission requires a contig FASTA per isolate.) | jolley2018bigsdb; bigsdbdocs2026 ; DOI 10.12688/wellcomeopenres.14826.1 (2018); https://bigsdb.readthedocs.io/en/latest/submissions.html (docs © 2014-2026, v1.54/1.55) | "BIGSdb works exclusively with assembled nucleotide sequences …" / "assembly_filename - this is the name of the FASTA file containing the assembly contigs. … you will not be able to finalize the submission until every isolate record has a matching contig file." |

Additional evidence (D3): private records docs https://bigsdb.readthedocs.io/en/latest/private_records.html "Users with a status of 'submitter', 'curator', or 'admin' can upload private isolate records that will be hidden from public view." Organism list (D6): https://pubmlst.org/organisms?page=2 lists "Lactococcus lactis 936-like bacteriophage"; no human/animal virus databases listed.

### 3. EnteroBase

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | partial (developer install docs; operated at Warwick and DSMZ; "Local EnteroBase" is a satellite feeding Warwick) | dyer2025enterobase, DOI 10.1093/nar/gkae902 | "A wealth of detailed information for advanced users and developers has been added, to make it easier to install EnteroBase locally and to set up new databases and genotyping schemes." |
| D2 | N (source-available without a declared licence) | https://bitbucket.org/enterobase/enterobase-web | Repo description: "Source code for enterobase.warwick.ac.uk"; PKG-INFO: "License: UNKNOWN" (LICENCE.md is empty). The GitHub repository EnteroBaseGroup (GPL-2.0) is an empty 2014 skeleton and is not used as a source. |
| D3 | yes | Zhou2020, DOI 10.1101/gr.251678.119 | "However, ownership of uploaded data remains with the user and extends to all calculations performed by EnteroBase. Only owners and their buddies, administrators, or curators can edit the metadata" |
| D4 | partial (user-defined fields in custom views; operator config via data_param table) | https://enterobase.readthedocs.io/en/latest/features/user-defined-content.html | "A User Defined Field can be created by giving a name (text box 5) and selecting a datatype (6) and then pressing the Create button (7)." |
| D5 | partial (developer-level: DB edits + server restart) | https://enterobase.readthedocs.io/en/latest/developer/developer-full-example.html | "The server has to be restarted so that it is aware of the scheme which will apepar [sic] on the associated search page." |
| D6 | bacteria | dyer2025enterobase | "more recently including Streptococcus spp. and Mycobacterium tuberculosis , in addition to Salmonella , Escherichia / Shigella , Clostridioides , Vibrio , Helicobacter , Yersinia and Moraxella ." |
| D7 | partial (GrapeTree tree+metadata integrated; map via Microreact) | Zhou2020 | "MLST trees are visualized with the EnteroBase tools GrapeTree (Zhou et al. 2018a) and Dendrogram, which in turn can transfer data to external websites such as Microreact" |
| D8 | partial (ENA on request per 2020 paper; current GDPR page says only "eventually") | Zhou2020 | "Short reads are deleted after genome assembly, or after automated, brokered uploading of the reads and metadata to the European Nucleotide Archive (ENA) upon user request." |
| D9 | n.d. | — | — |
| D10 | P (Illumina short reads only (paired by default). The only other input is a complete-genome FASTA, on request. Long-read assembly is planned, not available.) | enterobasedocs2026; dyer2025enterobase ; https://enterobase.readthedocs.io/en/latest/features/add-upload-reads.html (© 2026); DOI 10.1093/nar/gkae902 (2025) | "By default, reads are Illumina and paired. … to specify a Complete genome, which is the only other type available to date (please ask for permission)" / Dyer 2025: "develop and install additional bioinformatics tools (e.g. for assembling long sequencing reads …)" |

Conflicts: GDPR page https://enterobase.readthedocs.io/en/latest/GDPR.html: "We would eventually like to transfer sequence read data to services such as ENA/NCBI/DDBJ, but we will contact you directly for your permission when this occurs." Embargo: Zhou2020 "up to 12 mo"; current About page "6 months after uploads". Release delay quote (Zhou2020): "a delay in the release date of up to 12 mo can be imposed by users when uploading short-read sequences."

### 4. CGE (Center for Genomic Epidemiology, DTU) — current platform genepi.dk

The web platform described in 2016 (Bacterial Analysis Platform, thomsen2016bap) has been withdrawn; the
legacy website carries a retirement notice dated 2026-08-01 (cgeretirement2026): "After 15 years of service,
this legacy CGE website is no longer being maintained and will be retired shortly. We refer users of our CGE
tools to the new website ( https://genepi.dk )." Values describe genepi.dk.

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | P (tools installable locally; the platform itself is not distributed) | genepi2026, https://genepi.dk ; florensa2022resfinder | "All tools available from this website can also be downloaded and installed locally for offline use." |
| D2 | P (tools Apache-2.0; website not open source) | bortolaia2020resfinder ; https://bitbucket.org/genomicepidemiology/resfinder/raw/master/LICENSE ; https://genepi.dk/license | "Licensed under the Apache License, Version 2.0" / "all materials on this website are provided for your personal, non-commercial use only" |
| D3 | N (no accounts; no data retained) | genepi2026, https://genepi.dk | "Our services are provided free of charge with no registration required. We do not retain uploaded data or store information about individual users." |
| D4 | n.d. (current forms have no sample-metadata fields; no source states that metadata cannot be extended) | https://genepi.dk/listpred | "Upload assembled genomes (FASTA) or raw sequencing reads (FASTQ). Only one isolate per analysis is supported." |
| D5 | n.d. (fixed tool menus; no source states that pipelines cannot be added) | https://bitbucket.org/genomicepidemiology/lpap (README, 2026-10-01) | "Name the analysis and select a pipeline: Bacteria, Virus or Metagenomics" |
| D6 | B | https://genepi.dk/resfinder | "ResFinder identifies acquired genes and/or finds chromosomal mutations mediating antimicrobial resistance in total or partial DNA sequence of bacteria." |
| D7 | n.d. (no tree, map or metadata view documented on genepi.dk) | — | — |
| D8 | n.d. (integrated ENA upload announced in 2016, never documented as implemented; a standalone uploader exists, 2017) | thomsen2016bap ; https://bitbucket.org/genomicepidemiology/ENAUploader | "In addition, an optional automatic upload to the European Nucleotide Archive (ENA) of sample metadata and WGS data will soon be implemented." |
| D9 | n.d. | — | — |
| D10 | Y (FASTQ: Illumina ("non-nanopore") and ONT. Nanopore input exists for ResFinder, SpeciesFinder and ListPred. PathogenFinder2 takes FASTA only. One isolate per run.) | genepi2026 ; https://genepi.dk/virulencefinder, /resfinder (site last-modified 2026-09-29; text from the site's JS bundle) | "Upload assembled genomes (FASTA) or raw sequencing reads (FASTQ). Only one isolate per analysis is supported." / input options: "FASTQ (Non-nanopore Reads)", "FASTQ (Nanopore Reads)" |

### 5. IRIDA

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | yes | matthews2018irida, DOI 10.1101/381830 | "Instances can be independently installed on local high-performance computing infrastructure, enabling private and secure data management and analyses according to organizational policies and governance." |
| D2 | yes (Apache 2.0) | matthews2018irida | "IRIDA is open source software released under the Apache 2.0 license." |
| D3 | yes (per-project access; project managers own data; per-field metadata restriction) | matthews2018irida | "Data access is provided on a per-project basis. Users who are added to a project are given access to all data contained within the project." |
| D4 | Y (metadata fields and templates created in the interface, without code changes) | iridadocs2026, https://phac-nml.github.io/irida-documentation/user/user/sample-metadata/ | "Each sample can contain an indefinite number of metadata terms." |
| D5 | yes (Galaxy workflows as pipeline plugins) | matthews2018irida | "External developers can include pipelines not provided by IRIDA by building the pipeline as a Galaxy workflow, then integrating the pipeline into IRIDA via an internal API designed to expose the pipeline's analysis parameters." |
| D6 | bacteria (built-in); viruses only via third-party plugin | matthews2018irida ; https://github.com/phac-nml/irida-pipeline-plugins | "…a secure, decentralized, open-source, freely available, end-to-end public health genomics platform for microbial infectious disease investigations." / plugin list: "The IRIDA group does not maintain these plugins" (incl. "Human RNA Virus Genotyping") |
| D7 | partial (tree + metadata; map only via external GenGIS) | matthews2018irida | "IRIDA's Advanced Phylogenomic Visualization tool integrates phylogenetic trees displayed by PhyloCanvas with epidemiological metadata." |
| D8 | yes (NCBI SRA) | matthews2018irida | "IRIDA is also capable of submitting sequence data and metadata to NCBI's sequence read archive (SRA), which is synchronized daily with EBI-EMBL's ENA and Japan's DDBJ." |
| D9 | n.d. | — | — |
| D10 | Y (FASTQ single- and paired-end, plus ONT FAST5. FastQC runs automatically on upload. No longer developed.) | iridasamplesdocs2026; iridagithub ; https://phac-nml.github.io/irida-documentation/user/user/samples/ (n.s.; docs release 24.12, 2024-12-20) | "Sequence, fast5, and assembly files can be uploaded at the same time." / "Upload Sequence Files - Files must have the extension .fastq or .fastq.gz, all other formats will be ignored." |

Additional evidence (D3): "Project Managers "own" the project data." (matthews2018irida); "Metadata Fields can be restricted at the project level by metadata role." (iridadocs2026, sample-metadata page). D7 map: "GenGIS provides a connector to IRIDA to download the results of phylogenetic analyses and geographic information stored within IRIDA, integrating this information into a phylogeographic map."

### 5b. IRIDA Next (successor of IRIDA). Repo https://github.com/phac-nml/irida-next (Apache-2.0, last commit 2026-10-01, no releases); docs https://phac-nml.github.io/irida-next/

| D | Value | Source page | Source date | Verbatim quote |
|---|---|---|---|---|
| D1 | Y | …/docs/intro | 2026-08-05 | "Administer a self-managed IRIDA Next instance." |
| D2 | Y (Apache-2.0) | GitHub README + LICENSE | 2026-10-01 | "IRIDA Next is an open source bioinformatics platform for the storage, management, and analysis of genomic sequences and metadata." |
| D3 | Y | …/docs/user/organization/groups/share-groups | 2024-05-27 | "In IRIDA Next you can invite a group to a group to allow the members of the group access to the shared group" |
| D4 | Y (metadata keys added to samples in the interface, without code changes) | …/docs/user/project/samples/sample-metadata | 2026-08-05 | "Metadata can be added to samples to give them any additional information required by users." |
| D5 | Y (Nextflow via GA4GH WES) | …/docs/configuration/pipelines | 2026-02-02 | "Currently, only **Nextflow** pipelines are supported and they must have a GitHub repository." |
| D6 | n.d. | — | — | — |
| D7 | n.d. (no tree or map viewer documented) | — | — | — |
| D8 | n.d. (downloads only; **regression vs IRIDA's SRA export**) | …/docs/user/export/getting-started | 2026-08-05 | "In IRIDA Next, you can download data from multiple samples or all files associated with a workflow execution at once by creating a data export." |
| D9 | n.d. | — | — | — |
| D10 | Y (Single- and paired-end FASTQ attached to samples. Automated pipelines run on newly uploaded paired-end files. Technology not stated.) | iridanextdocs2026 ; https://phac-nml.github.io/irida-next/docs/user/analysis/getting-started ; …/docs/user/project/samples/sample-files (n.s.; repo HEAD 2026-10-01) | 2026-10-02 (access) | "Automated workflow executions belong to projects and once set-up, an analysis is performed on all newly uploaded paired-end files within that project" / "Files can be uploaded and attached to samples for analysis" |

### 6. Galaxy

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | yes | afgan2018galaxy, DOI 10.1093/nar/gky379 | "The Galaxy framework and software ecosystem (https://github.com/galaxyproject)—an open-source software package that anyone can use to run a Galaxy server on any Unix-based operating system." |
| D2 | yes (MIT) | https://github.com/galaxyproject/galaxy/blob/dev/LICENSE.txt | "Galaxy is provided from 2026-02-25 onwards entirely under the MIT License." (earlier: MIT for work from 2021-04-07, AFL 3.0 before) |
| D3 | partial (user/group/role permissions; no organisation tenancy or data ownership model documented) | https://galaxyproject.org/learn/privacy-features/ | "The model allows permissions to be set on a fine-grained level, from completely private through a couple of users to entire collaborative groups." |
| D4 | P (Sample Sheets, release 25.1, Dec 2025: typed per-sample metadata for workflow inputs, not a persistent metadata model) | galaxy251release ; galaxy2026, DOI 10.1093/nar/gkag469 | "Sample Sheets are particularly useful for workflows that require multiple related inputs or when you need to process batches of samples with associated metadata in a structured format." |
| D5 | yes | galaxy2024, DOI 10.1093/nar/gkae410 | "For any new analysis package to become a tool, a developer prepares a Galaxy wrapper once, and uploads it to the sharable Galaxy global tool 'appstore' called the Galaxy Toolshed" |
| D6 | B, V, F (domain-agnostic) | galaxy2024 ; galaxy2022, DOI 10.1093/nar/gkac247 ; Galaxy Training Network, "Identifying Mycorrhizal Fungi from ITS2 sequencing using LotuS2" ("What is the fungal community composition in a given soil sample?") | "…enabling a wide variety of analyses in both the life and physical sciences, including astronomy, genomics, proteomics…" / "providing a platform for global pathogen monitoring" (SARS-CoV-2) |
| D7 | partial (separate tree and map viewers; no combined dashboard) | https://galaxyproject.org/learn/visualization/ ; galaxy2022 | "…advanced viewers for molecules, proteins, networks, and phylogenetic trees." / "geographic maps from OpenLayers." |
| D8 | partial (ENA via community Tool Shed tool) | roncoroni2021ena, DOI 10.1093/bioinformatics/btab421 | "A Galaxy wrap of the tool allows users with little or no bioinformatics knowledge to do bulk sequencing read submissions." |
| D9 | n.d. (the third-party Galaxy LIMS of 2013, scholtalbers2013galaxylims, relied on sample tracking, removed in 2017) | galaxypr5103, https://github.com/galaxyproject/galaxy/pull/5103 (2017-12-01) | "This PR removes the sample tracking features entirely from the backend." |
| D10 | Y (FASTQ is a core datatype. Illumina paired-end (2026 paper) and ONT MinION (GTN workflows).) | galaxy2026; galaxynanopore2023 ; DOI 10.1093/nar/gkag469 (2026); https://training.galaxyproject.org/training-material/topics/microbiome/tutorials/pathogen-detection-from-nanopore-foodborne-data/tutorial.html (published 2023-01-26, modified 2026-09-23) | "each of the six samples … is represented as a pair of compressed fastqsanger.gz datasets ready for downstream analysis." / "sequenced using MinION (ONT). … In this tutorial, we will be presenting a series of Galaxy workflows" |

### 7. Pathogenwatch

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | partial (workflows runnable locally; platform deployed on AWS, no institutional install guide) | alikhan2026pathogenwatch (medRxiv preprint, full text https://www.medrxiv.org/content/10.64898/2026.03.18.26348693v1.full), DOI 10.64898/2026.03.18.26348693 | "the same workflows can be run locally via Pathogenwatch Local." / "with its primary deployment implemented on Amazon Web Services (AWS)." |
| D2 | N (source-available under a non-commercial licence; does not meet the Open Source Definition) | https://github.com/pathogenwatch-oss/website (LICENSE) | "CGPS Non-Commercial Licence (Version 1.0)… Use, modify, and distribute this software for personal, academic, research, or non-commercial purposes only." |
| D3 | partial (private uploads/collections shared per user; no organisation tenancy) | argimon2021typhi, DOI 10.1038/s41467-021-23091-2 | "User-uploaded genomes, their metadata, and derived collections remain private in the Pathogenwatch user account, unless the user specifically shares them via a collection URL." |
| D4 | partial (user adds free CSV columns; no operator vocabularies) | https://cgps.gitbook.io/pathogenwatch/ ("Editing metadata") | "All fields included in the CSV included in the initial genome upload can be edited, except the FASTA file name. It's also possible to add or delete fields." |
| D5 | no (pipelines added by CGPS only) | https://cgps.gitbook.io/pathogenwatch/ ("Supported Organisms") | "Pathogenwatch provides annotation pipelines for a limited set of species." |
| D6 | both (bacteria, SARS-CoV-2, fungi) | alikhan2026pathogenwatch | "supports bacterial, viral, and fungal pathogens within a consistent analytical framework." |
| D7 | yes | argimon2021typhi | "The Collection view displays the user genomes clustered by genetic similarity on a tree, their location on a map, a timeline, as well as tables…" |
| D8 | n.d. | — | — |
| D9 | n.d. | — | — |
| D10 | P (Paired-end short-read FASTQ only, in a limited number, assembled by the in-house short-read pipeline. No long reads documented.) | pathogenwatchdocs2026 ; https://cgps.gitbook.io/pathogenwatch/how-to-use-pathogenwatch/uploads-and-folders/genome-uploads-folders (n.s.) | "You can also upload a limited number of pairs of FASTQ files for assembly using our in-house assembly pipeline." |

### 8. AusTrakka

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | no (central) | hoang2022austrakka, DOI 10.1038/s41467-022-28529-9 | "rapid data sharing between states and territories through a centralised platform." |
| D2 | N (public client and CLI code without a licence; backend not public) | trakkacli, https://github.com/AusTrakka ; GitHub API license endpoint returns 404 for every repository | "# Pick your license as you wish" (template comment in setup.py; no LICENSE file) |
| D3 | yes | hoang2022austrakka ; https://docs.trakka.org/ (orgs overview) | "enables fine-grained access controls of data between public health laboratories." / "Organisations within Trakka represent institutions or groups of users, which may wish to manage their own users, and manage their own data" |
| D4 | partial (proformas/project fields configured by AusTrakka staff on request) | https://docs.trakka.org/ (metadata uploads; projects overview) | "Proformas allow customised data validation and give permission to modify particular metadata fields." / "Project datasets allow project analysts to attach extra metadata fields to the project." |
| D5 | partial (analysts upload external trees/results; no pipeline plug-in) | https://docs.trakka.org/ (projects overview) ; hoang2022austrakka | "phylogenetic trees that have been added to the project by project analysts" / "the platform is able to visualise trees using any method." |
| D6 | both | https://austrakka.net/ (history; governance) | "initially developed to serve as Australia's national genomics surveillance platform for SARS-CoV-2 and has since expanded to other nationally agreed pathogens." |
| D7 | P (annotated trees and maps are documented; their combination in one view is not stated explicitly) | https://docs.trakka.org/ (projects overview) ; sloggett2024austrakka, DOI 10.5281/zenodo.15293599 | "These may for instance include epidemiological curves, cluster timeline diagrams, bar charts, maps, etc." / "the ability to incorporate metadata onto phylogenetic trees." |
| D8 | n.d. | — | — |
| D9 | n.d. | — | — |
| D10 | Y (FASTQ: Illumina paired-end and single-end, and ONT. FASTA consensus and assemblies are also accepted. Analysis runs on the platform's analysis server.) | austrakkadocs; austrakkagovernance2025 ; https://docs.trakka.org/docs/Reference/sequence-data (© 2026); governance protocol endorsed 2025-11-12 | "fastq-ill-pe Paired-end Illumina FASTQ sequences … fastq-ill-se Single-end Illumina FASTQ sequences … fastq-ont Oxford Nanopore (ONT) FASTQ sequences" / "Sequence data should be uploaded using FASTA or FASTQ data formats, as appropriate for the pathogen and analysis." |

Additional evidence (D3): austrakka.net "the retainment of data custodianship for jurisdictions." Reference: hoang2022austrakka, Nat Commun 13:865 (2022).

### 9. NCBI Pathogen Detection

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | no | https://www.ncbi.nlm.nih.gov/pathogens/about/ | "NCBI Pathogen Detection project is a centralized system…" |
| D2 | partial (components e.g. AMRFinderPlus, SKESA public domain; SNP pipeline unpublished) | https://www.ncbi.nlm.nih.gov/pathogens/faq/ | "several of the components NCBI developed for the pipeline are published and open source" / "Is your SNP pipeline published? Not yet." |
| D3 | no (all data public) | https://www.ncbi.nlm.nih.gov/pathogens/about/ | "Assemblies and annotations generated by our system are deposited in GenBank and made publicly available." |
| D4 | partial (fixed BioSample package + free custom attributes) | https://www.ncbi.nlm.nih.gov/pathogens/pathogens_help/ ; https://www.ncbi.nlm.nih.gov/biosample/docs/attributes/ | "a template/package is used that has a minimal set of required fields that was developed specifically for this project" / "submitters may provide any number of custom attributes to fully describe a sample." |
| D5 | no / n.d. (single NCBI-run pipeline) | https://www.ncbi.nlm.nih.gov/pathogens/about/ | "NCBI has developed a pipeline that assembles short-read Illumina sequence data and analyzes it…" |
| D6 | bacteria (+ one fungus); no viruses | sayers2026ncbi, DOI 10.1093/nar/gkaf1060 | "over 2 474 299 pathogen isolates covering 100 bacterial taxa and one emerging fungal pathogen, Candidozyma auris (renamed from Candida auris…)" |
| D7 | partial (SNP tree + metadata labels; no map documented) | https://www.ncbi.nlm.nih.gov/pathogens/pathogens_help/ | "The SNP Tree Viewer displays a phylogenetic tree of pathogen isolates…" |
| D8 | yes (intrinsic: data enter via NCBI SRA/GenBank submission) | https://www.ncbi.nlm.nih.gov/pathogens/about/ | "Public health agencies and researchers sequence the samples and submit the data to NCBI…" |
| D9 | n.d. | — | — |
| D10 | P (Illumina reads only, submitted via SRA and assembled by the NCBI pipeline. Other technologies must be submitted as assemblies to GenBank.) | ncbipathogenssubmit; ncbipathogensabout ; https://www.ncbi.nlm.nih.gov/pathogens/submit-data/ ; https://www.ncbi.nlm.nih.gov/pathogens/about/ (n.s.) | "The Pathogen system accepts genomic data from the ILLUMINA platform sequencing of cultured microbial organisms." / "If you sequenced your isolates using another technology then you can submit the assembled genomes directly to GenBank" |

Component of the pipeline published separately: AMRFinderPlus (Feldgarden et al. 2021, DOI 10.1038/s41598-021-91456-0).

### 10. EFSA One Health WGS System

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | no (central EFSA cloud; analytical pipeline runs locally) | Rossi M, EURL-Salmonella workshop 24 May 2022 (rossi2022efsa) ; efsa2026pipeline | "Through WGS PORTAL: use cloud resources of EFSA…" / "This repository provides the Nextflow-based analytical pipeline used within this framework." |
| D2 | partial (pipeline EUPL-1.2; portal/database code n.d.) | efsa2026pipeline https://dev.azure.com/efsa-devops/EFSA/_git/efsa.wgs.onehealth (LICENSE.md) | "EUROPEAN UNION PUBLIC LICENCE v. 1.2" |
| D3 | yes (MS own data; data provider can unrelease) | efsaecdc2022collab (Art. 6) ; rossi2022efsa | "The Member States or EEA countries own the Data resulting from testing performed by NRLs…" / "Data Provider can 'unrelease' Entries at any time blocking the sharing of data" |
| D4 | no (fixed data model) | efsaecdc2022collab (Annex I §4.1.2) ; efsa2022onehealthwgs, DOI 10.2903/sp.efsa.2022.EN-7413 (abstract) ‡ | "submit… to EFSA MTS according to the data model described in 'Guidelines for reporting…'" / "detailed information on the types and formats of data that can be submitted" |
| D5 | partial (typing data may come from "comparable" external pipelines under fixed rules; no workflow add-in) | rossi2022efsa | "Typing data are set of information extracted from the experiment by the EFSA One Health WGS analytical pipeline or by comparable bioinformatic pipelines." |
| D6 | B (five species) | efsa2026pipeline README (tag ONE_HEALTH-v3.0.0, 2026-05-22) | "Salmonella enterica, Listeria monocytogenes, Escherichia coli (including STEC) of non-human origin, Campylobacter jejuni, and Campylobacter coli" |
| D7 | partial (trees/MSTs; no map/dashboard documented) | rossi2023efsaecdc | "Perform analysis (search for matches, build trees, etc.) and compare the data" / "MSTs including human and food data" |
| D8 | yes (to ECDC, cgMLST + minimum metadata); ENA n.d. | efsa2022onehealthwgs (abstract) ‡ | "interoperates with the ECDC Molecular Typing system exchanging core genome Multi Locus Sequence Typing (cgMLST) profiles and minimum metadata." |
| D9 | n.d. | — | — |
| D10 | Y (FASTQ is uploaded to the WGS portal and typed by the EFSA pipeline in EFSA's cloud. The alternative route sends pre-computed profiles. Technology not stated.) | rossi2023efsaecdc; rossi2022efsa ; https://www.efsa.europa.eu/sites/default/files/2023-09/presentation-1-rossi-nannapaneni.pdf (2023-09-05) | "Share data using the WGS portal uploading fastq → take advantage of EFSA computing resources" / "Experimental data: information related to the experiment (raw sequencing reads)" |

Additional evidence (D3): efsaecdc2022collab: "The inclusion of Data in the ECDC and EFSA MTSs does not affect the ownership…". D5: "valid only if the allele calling is performed… using chewBBACA v >2.8.4 with schemas downloaded from chewieNS" (rossi2022efsa). Background ref: efsa2019wgs, DOI 10.2903/sp.efsa.2019.EN-1337.

### 11. Nextstrain

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | yes (CLI/augur/auspice installable; Auspice on own server; Groups only on nextstrain.org) | https://docs.nextstrain.org/en/latest/guides/share/index.html | "Auspice can be run on your own server, including customizations to the appearance and functionality. This may be appropriate when you want or need full control over how the website is deployed and where the data is stored." |
| D2 | yes (AGPL-3.0 augur/auspice/nextstrain.org; MIT CLI) | https://docs.nextstrain.org/en/latest/learn/about.html | "All source code for Nextstrain is freely available under the terms of an open-source license , typically AGPL-3.0 or MIT ." |
| D3 | partial (public/private Groups for derived datasets; not a primary sequence store) | https://docs.nextstrain.org/en/latest/learn/groups/index.html | "Nextstrain Groups is a feature that allows research labs, public health entities, and other organizations to share their Nextstrain datasets and narratives directly on nextstrain.org within the context of a named "group". Groups can be shared publicly or privately ." |
| D4 | partial (free TSV columns per build; no managed schema/vocabularies) | https://docs.nextstrain.org/projects/augur/en/stable/usage/cli/export.html | "--color-by-metadata Metadata columns to include as coloring options." |
| D5 | yes | https://docs.nextstrain.org/projects/augur/en/stable/index.html | "It provides a collection of commands which are designed to be composable into larger processing pipelines." |
| D6 | both | huddleston2021augur, DOI 10.21105/joss.02906 | "When Nextstrain replaced nextflu and expanded to support multiple viral and bacterial pathogens, each pathogen received its own copy of the original script." |
| D7 | yes | hadfield2018nextstrain, DOI 10.1093/bioinformatics/bty407 | "The visualization integrates sequence data with other data types such as geographic information, serology, or host species." |
| D8 | n.d. (ingest from NCBI/GISAID only) | hadfield2018nextstrain (context) | "sourced from public repositories such as NCBI ( www.ncbi.nlm.nih.gov ), GISAID ( www.gisaid.org ) and ViPR" |
| D9 | n.d. | — | — |
| D10 | P (Viral workflows start from consensus genomes. Only the *M. tuberculosis* workflow starts from short-read FASTQ, which it fetches from SRA. Nextclade Web does not take FASTQ (not checked against a primary source).) | andrews2026nextstrain ; DOI 10.64898/2026.03.23.713807 (bioRxiv preprint, 2026-03-26) | "One of the main differences of the M. tuberculosis pipeline compared to the viral pipelines is that it starts with raw short-read sequence data rather than consensus genome sequences." |

D3 and D4 are P: Groups share derived datasets rather than primary sequence data, and metadata are per-build TSV columns without a managed schema.

### 12. GISAID

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | no | GISAID EpiFlu Database Access Agreement, https://gisaid.org/terms-of-use/ (gisaiddaa) | "The GISAID EpiFlu™ Database utilizes a proprietary platform and software technology (collectively, the " Database Platform ") owned by GISAID and/or third party contractors. You will not copy, reverse engineer, disseminate or disclose any part of the Database Platform." |
| D2 | no (proprietary) | gisaiddaa | (same quote) |
| D3 | partial (provider keeps ownership & credit; but all data shared with all registered users, no private/project visibility) | shu2017gisaid, DOI 10.2807/1560-7917.ES.2017.22.13.30494 | "The essential features of the DAA encourage sharing of data by securing the provider's ownership of the data, requiring acknowledgement of those providing the samples and producing the data, while placing no restriction on the use of the data by registered users adhering to the DAA." |
| D4 | n.d. | — | — |
| D5 | n.d. | — | (mission page only mentions third-party tools consuming GISAID data) |
| D6 | viruses | https://gisaid.org/about-us/mission/ | "…rapid sharing of data from priority pathogens including influenza, hCoV-19, respiratory syncytial virus (RSV), hMpxV as well as arboviruses including chikungunya, dengue and zika." |
| D7 | partial (global tree; variant distribution/prevalence) | khare2021gisaid, DOI 10.46234/ccdcw2021.255 | "A global phylogenetic tree comprising of all high-quality sequences is available to all GISAID users ( Figure 1C )." |
| D8 | no (is itself the repository; does not forward to others) | https://gisaid.org/help/faq/ | "GISAID does not offer a mechanism to release data to any other database." |
| D9 | n.d. | — | — |
| D10 | n.d. (Submission documentation is behind login. No primary public source on input formats was found. Third-party guidance (e.g. APHL) says consensus goes to GISAID and reads go to SRA; not counted.) | — | — |

Additional evidence (D3): DAA "You acknowledge and agree that all Data will be freely shared among and used by all other Authorized Users." The quoted agreement is the EpiFlu Database Access Agreement.

### 13. Pathoplexus (Loculus software)

| D | Value | Source | Verbatim quote |
|---|---|---|---|
| D1 | P (installable through the Loculus software; pathoplexus.org itself is centrally hosted) | https://loculus.org/for-administrators/getting-started/ | "All services are available as Docker images. For local development and the preview instances, we use Kubernetes and Helm for deployment but it is also possible to deploy Loculus without Kubernetes." |
| D2 | yes (AGPL-3.0, Loculus & Pathoplexus) | https://pathoplexus.org/about ; github.com/loculus-project/loculus | "Our open-source model encourages innovation and community engagement, with all code available on GitHub" |
| D3 | partial (group-owned submissions, restricted-use ≤1 year; no private data) | https://loculus.org/for-users/create-manage-groups/ ; https://pathoplexus.org/ | "Everyone within a group is able to submit, edit, and revoke sequences uploaded by anyone else in that group." / "all data is accessible. Some data ("Restricted-Use Data") does have restrictions on how it can be used" |
| D4 | yes (Loculus config; pre-1.0 config may change) | https://loculus.org/introduction/what-is-loculus/ | "Highly configurable: The list of metadata fields is fully configurable and Loculus supports both single- and multi-segmented genomes." |
| D5 | partial (operator-level per-organism preprocessing/QC pipeline; not downstream analysis) | https://loculus.org/introduction/system-overview/ | "The pipeline contains organism -specific logic, thus, there is a separate pipeline for each organism. We maintain a customizable preprocessing pipeline that uses Nextclade for alignment, quality checks and annotations but it is easy to write a new one" |
| D6 | viruses (Pathoplexus); Loculus "microbial" | https://pathoplexus.org/about | "Pathoplexus is a new open-source database designed to enhance the sharing and analysis of human viral pathogen genomic data." |
| D7 | P (tree placement and geographic distribution through external link-out tools; no built-in combined view) | pathoplexustools, https://pathoplexus.org/docs/how-to/use-tools-and-add-new-ones (2025-07-07) | "perform QC on sequences with Nextclade and see their placement on a phylogenetic tree (only available for some organisms) - visualise the geographic distribution of your sequences" |
| D8 | yes (ENA/INSDC for open data) | https://pathoplexus.org/about/faq | "If you've chosen for your data to be open straight away, it will be submitted to the European Nucleotide Archive (ENA)." |
| D9 | n.d. | — | — |
| D10 | P (Since 2026-09-22, gzipped FASTQ (single- or paired-end) can be added only alongside a consensus sequence. Reads are hosted and brokered to INSDC; no documented processing of reads.) | pathoplexusrawreads2026 ; https://pathoplexus.org/docs/how-to/upload-raw-reads ; https://pathoplexus.org/news/2026-09-22-announcing-raw-reads (2026-09-22) | "You can provide either a single fastq.gz file or a pair of fastq.gz files for consensus sequences generated from single-end or paired-end reads, respectively." / "you can optionally include raw sequencing reads in your submissions." |

---

## (b) Summary matrix (as in `data/comparison.csv`, after the re-check of 2 October 2026)

† through the BIGSdb software, not a function offered to users of the hosted site. ‡ quotation verified on
the abstract; full text not accessible. § only source predates 2023. B bacteria, V viruses, F fungi.

| Platform | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 |
|---|---|---|---|---|---|---|---|---|---|---|
| BIGSdb-Pasteur | P† | Y (GPL-3.0) | Y | Y | P† | B | P | n.d. | n.d. (built-in sample table removed 2019) | N (assemblies only) |
| PubMLST | P† | Y (GPL-3.0) | Y | Y | P† | B, F (one bacteriophage scheme, not counted as viral surveillance) | P | n.d. | n.d. (as above) | N (assemblies only) |
| EnteroBase | P | N (no licence) | Y | P | P | B | P | P (brokered ENA upload with consent) | n.d. | P (Illumina only) |
| CGE (genepi.dk) | P | P (tools Apache-2.0; website not open) | N | n.d. | n.d. | B | n.d. | n.d. | n.d. | Y |
| IRIDA (no longer developed) | Y | Y (Apache-2.0) | Y | Y | Y | B§ | P (no map) | Y (NCBI SRA) | n.d. | Y |
| IRIDA Next | Y | Y (Apache-2.0) | Y | Y | Y | n.d. | n.d. | n.d. | n.d. | Y |
| Galaxy | Y | Y (MIT) | P | P (Sample Sheets) | Y | B, V, F | P | P (ENA, community tool) | n.d. | Y |
| Pathogenwatch | P | N (non-commercial) | P | P | N | B, V, F | Y | n.d. | n.d. | P (limited paired-end FASTQ) |
| AusTrakka | N | N (no licence) | Y | P | P | B, V | P | n.d. | n.d. | Y |
| NCBI Pathogen Detection | N | P (components) | N (all public) | P | N | B, F | P (no map) | Y (data enter by NCBI submission) | n.d. | P (Illumina only) |
| EFSA One Health WGS | N | P (pipeline EUPL-1.2) | Y | N‡ | P | B | P (no map) | Y‡ (ECDC cgMLST exchange) | n.d. | Y |
| Nextstrain | Y | Y (AGPL-3.0/MIT) | P | P | Y | B, V | Y | n.d. | n.d. | P (M. tuberculosis workflow only) |
| GISAID | N§ | N§ (proprietary) | P | n.d. | n.d. | V | P | N | n.d. | n.d. |
| Pathoplexus | P (via Loculus) | Y (AGPL-3.0) | P | Y | P | V | P (external link-out tools) | Y (ENA) | n.d. | P (reads stored with consensus, not processed) |

Sections (a) and (b) show the current values; sections (c) and (d) document the re-check.
Full references for the source keys are in `data/sources.bib`.

## (c) Audit trail — re-check of 2 October 2026: platform status

- **CGE**: the legacy site https://www.genomicepidemiology.org/services/ has a notice dated **2026-08-01**: "After 15 years of service, this legacy CGE website is no longer being maintained and will be retired shortly. We refer users of our CGE tools to the new website ( https://genepi.dk )."
  - The **Bacterial Analysis Pipeline (BAP, Thomsen 2016), the source of the old CGE values, is no longer listed.**
  - **genepi.dk** is a stateless front-end that runs one tool on one isolate at a time (ResFinder, MLST, PlasmidFinder, VirulenceFinder, SpeciesFinder, PathogenFinder2, ListPred, CholeraeFinder). It has no accounts and no sample store.
  - **GPAP** (Global Pathogen Analysis Platform, DTU, Novo Nordisk Foundation, announced 2025-10-13) is described only in the future tense, so it is not used for any cell.
  - **LPAP** (Bitbucket, GPL-3.0, v0.29.0 2026-10-01) is a new single-user CGE desktop app.
- **IRIDA**: deprecated ("⛔️ DEPRECATED"; last release 24.12, 2024-12-20). The successor is **IRIDA Next** (Apache-2.0, actively developed, **no tagged releases**). IRIDA Next is evaluated separately below as successor evidence.
- **BIGSdb**: the "sample table / LIMS" module cited from Jolley & Maiden 2010 was **removed from the software in 2019**.
- **Galaxy**: the built-in sample-tracking subsystem was **removed in 2017** (PRs #4902, #5103). The 2013 "Galaxy LIMS" was built on top of it.
- **EFSA**: EN-7413 (2022) is superseded as the current reporting guideline by **EN-9830 (Dec 2025)**, issued under Commission Implementing Regulation (EU) 2025/179. That regulation makes reporting mandatory from 23 Aug 2026.
- **GISAID**: the only public terms are still the **EpiFlu DAA of 2011**; no EpiCoV-specific text is public. Context only, no cell affected: Nextstrain blog 2025-11-06 says "On Oct 1, 2025, we received an email from GISAID Secretariat informing us that GISAID has immediately ended updates to the flat file of SARS-CoV-2 genomic sequences and associated metadata".

## (d) Audit trail — changes after the re-check (every cell resting on a source older than 2023, and every N or n.d.)

This section records the value each re-checked cell had before 2 October 2026 and the newer source that confirmed or changed it. Sections (a) and (b) already show the current values.

Legend for the "New" column: **confirmed** = value unchanged; **CHANGED** = value changes; "refined" = value class unchanged, wording or citation updated.

#### Pasteur BIGSdb (B) and PubMLST (P). Same BIGSdb software (v_1.54.0, 2026-09-17; pubmlst.org runs 1.54.0, bigsdb.pasteur.fr runs 1.53.6)

| Platform·D | Old | New | Source | Source date | Verbatim quote (≤40 words) |
|---|---|---|---|---|---|
| B,P·D1 | Y† (2018 paper) | confirmed | https://bigsdb.readthedocs.io/en/latest/installation.html | 2024-06-27 (docs v1.55.0) | "BIGSdb consists of two main Perl scripts, bigsdb.pl and bigscurate.pl, that run the query and curator’s interfaces respectively." / "Download from SourceForge.net or GitHub" |
| P·D2 | Y GPL-3.0 (2018 paper) | confirmed (newer source) | https://pubmlst.org/software/bigsdb | n.s. (page © 2010-2025) | "The software has been released under the GNU General Public Licence version 3 . Source code is available from GitHub" |
| B·D2 | Y GPL-3.0 | confirmed (exact: GPL-3.0-or-later) | https://bigsdb.pasteur.fr/cgi-bin/bigsdb/bigsdb.pl?db=pubmlst_klebsiella_isolates&page=version | n.s. (BIGSdb 1.53.6) | "…under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version." |
| P·D3 | Y (2018 paper) | confirmed (current docs) | https://bigsdb.readthedocs.io/en/latest/user_projects.html | 2026-06-18 | "If private data and user quotas are enabled, these projects can include private records that can then be shared with other user accounts." |
| B,P·D5 | P† (2010 paper) | confirmed | https://bigsdb.readthedocs.io/en/latest/administration.html ; release https://github.com/kjolley/BIGSdb/releases/tag/v_1.51.6 | 2026-06-08 ; 2025-11-25 | "If the system_flag value is not defined then the plugin is always enabled if it is installed on the system" / "…support for third-party analysis fields (data stored as JSON within the database following analysis by external tools such as Kleborate and Kaptive)." |
| P·D6 | mostly B (2018 paper) | confirmed, refined: 150 organisms; bacteria + some eukaryotes + 1 phage + plasmid MLST; **no human/animal viruses** | https://pubmlst.org/organisms | n.s. | "150 organisms" (list incl. Aspergillus fumigatus, Candida spp., Trichomonas vaginalis, "Lactococcus lactis 936-like bacteriophage", "Plasmid MLST") |
| B,P·D7 | P (2018 paper) | confirmed | https://bigsdb.readthedocs.io/en/latest/data_analysis/microreact.html | 2026-06-24 | "These trees are then sent together with country and year field values to the Microreact website for display." / "…the BIGSdb plugin is currently limited to the level of country." |
| B,P·D8 | n.d. | confirmed n.d. Code and changelog searched for ENA/SRA/Webin: only accession *linking*. The BIGSdb "submission system" sends data to the database's own curators, not to a repository. | https://github.com/kjolley/BIGSdb/releases/tag/v_1.47.1 | 2024-07-25 | (linking only) "This version adds an option to isolate field configurations to enable a different hyperlink to be set depending on the regular expression of the field value." |
| B,P·D9 | P (built-in sample table, 2010 paper) | **CHANGED → n.d.** (built-in LIMS removed in 2019; no external-LIMS integration documented; the current docs have 0 hits for "LIMS").  | https://github.com/kjolley/BIGSdb/issues/257 ; commit https://github.com/kjolley/BIGSdb/commit/6696fec5975d2225c3f497ec8745ef5f107d1b99 | 2019-05-14 (in v_1.22.4+) | Issue #257 "Remove sample management code": "This has never really worked well and using a proper LIMS system which can be linked to from a BIGSdb record makes more sense." |

#### EnteroBase

| D | Old | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D3 | Y (2020 paper) | confirmed (current docs) | https://enterobase.readthedocs.io/en/latest/features/editing-strain-metadata.html ; …/features/buddies.html | 2026-09-11 | "By default, only the owner (the one who uploaded the data) and curators/administrators of the database have access to the genomic assemblies, metadata and genotypes prior to the release date." |
| D7 | P (2020 paper) | confirmed (current docs) | https://enterobase.readthedocs.io/en/latest/grapetree/grapetree-manual.html | 2026-09-11 | "MicroReact locate genomes on a map using GPS coordinates. EnteroBase will transfer GPS co-ordinates if they are included in the metadata." |
| D8 | P (2020 paper; GDPR page "eventually") | confirmed P, **new primary source**: brokered ENA upload of reads from users who gave permission, run by cron. This supersedes the vaguer GDPR page (last edited 2022-03-01). | https://enterobase.readthedocs.io/en/latest/developer/developer-maintenance-scripts.html ; code https://bitbucket.org/enterobase/enterobase-web (manage.py, entero/admin/ENAsubmission.py) | 2023-09-30 | "it will use the default user file that contains all the user names who have permitted us to submit their read to the EBI." … "Currently run twice a day as a cron job" |
| D9 | n.d. | confirmed n.d. ("LIMS": 0 hits in docs, code and Dyer 2025) | — | — | — |

Note: Dyer 2025 (NAR) does not mention buddies, Microreact, ENA or LIMS, so it supports none of EnteroBase D3, D7, D8 or D9. The current docs disagree on the embargo period: About page (2022) says "6 months", upload page (2026-09-11) says "up to 12 months".

#### CGE (now genepi.dk). Old values came from BAP (2016), which is no longer offered

| D | Old | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D1 | P (2022 paper) | confirmed P (tools local; the new LPAP desktop app is local; the genepi.dk platform is not distributed) | https://genepi.dk ; https://bitbucket.org/genomicepidemiology/lpap | n.s. (server last-modified 2026-09-29) ; 2026-10-01 | "All tools available from this website can also be downloaded and installed locally for offline use." / "LPAP is a desktop application for running CGE bioinformatics analysis workflows locally." |
| D2 | Y tools Apache-2.0 (2020 paper) | **CHANGED → P**: tools Apache-2.0, LPAP GPL-3.0, genepi.dk website proprietary | https://bitbucket.org/genomicepidemiology/resfinder/raw/master/LICENSE ; https://genepi.dk/license | LICENSE ©2021 ; n.s. | "Licensed under the Apache License, Version 2.0" / "all materials on this website are provided for your personal, non-commercial use only" |
| D3 | P (2016 BAP) | **CHANGED → N** (no accounts; no data kept; BAP withdrawn) | https://genepi.dk (Home) | n.s. | "Our services are provided free of charge with no registration required. We do not retain uploaded data or store information about individual users." |
| D4 | N (2016) | **CHANGED → n.d.** (the N rested on the withdrawn BAP; the current forms have no sample-metadata fields, but no source states that metadata cannot be extended) | https://genepi.dk/listpred | n.s. | "Upload assembled genomes (FASTA) or raw sequencing reads (FASTQ). Only one isolate per analysis is supported." |
| D5 | N (2016) | **CHANGED → n.d.** (the N rested on the withdrawn BAP; current tools and LPAP pipelines are fixed menus, but no source states that pipelines cannot be added) | https://bitbucket.org/genomicepidemiology/lpap (README) | 2026-10-01 | "Name the analysis and select a pipeline: Bacteria, Virus or Metagenomics" / "optionally toggling individual analysis components (species ID, AMR, virulence, plasmid, MLST)" |
| D6 | B (2016/2021) | confirmed B for the web platform (LPAP desktop also does virus and metagenomics) | https://genepi.dk/resfinder | n.s. | "ResFinder identifies acquired genes and/or finds chromosomal mutations mediating antimicrobial resistance in total or partial DNA sequence of bacteria." |
| D7 | P (TreeViewer; map planned 2016) | **CHANGED → n.d.** for the current platform (genepi.dk offers no tree, map or metadata view, but no source *states* absence, so N is not allowed under the base file's rule). TreeViewer is still listed on the legacy services page, which is retiring. The row describes genepi.dk. Context: the standalone "phylodash" library (2022) is not a platform feature. | https://www.genomicepidemiology.org/services/ (retirement notice; still lists "TreeViewer Phylogeny Tree Viewer.") | 2026-08-01 | "After 15 years of service, this legacy CGE website is no longer being maintained and will be retired shortly." |
| D8 | n.d. ("will soon be implemented", 2016) | confirmed n.d. No integrated ENA upload. Context only: a standalone CLI "ENAUploader" exists (Python 2.7, README 2017). | https://bitbucket.org/genomicepidemiology/ENAUploader | 2017-06-09 | "The tool has been released and should be working. We are still in the process of updating the documentation." |
| D9 | n.d. | confirmed n.d. | — | — | — |

#### IRIDA (deprecated) — current docs (release 24.12)

| D | Old (2018 bioRxiv) | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D1 | Y | confirmed | https://phac-nml.github.io/irida-documentation/administrator/web/ | n.s. (docs release 24.12, 2024-12-20) | "This document describes how to install the IRIDA web interface." |
| D2 | Y Apache-2.0 | confirmed (GitHub LICENSE Apache-2.0; deprecated) | https://github.com/phac-nml/irida | 2024-12-20 (last release) | "IRIDA is no longer being developed, our successor is IRIDA Next" |
| D3 | Y | confirmed | https://phac-nml.github.io/irida-documentation/user/user/project/ | page last changed 2022-05-06 (in 24.12 docs) | "Project members can have two different project roles: a project collaborator ( read-only permissions), and a project manager ( read and modify permissions)." |
| D5 | Y | confirmed | https://github.com/phac-nml/irida-plugin-example | repo pushed 2026-03-27 | "This can be used as a template for implementing your own pipelines within IRIDA." |
| D6 | B (+V 3rd-party plugin) | confirmed; **no newer source found** | matthews2018irida ; https://github.com/phac-nml/irida-pipeline-plugins | 2018 ; n.s. | (existing quotes) |
| D7 | P (no map) | confirmed | https://phac-nml.github.io/irida-documentation/user/user/analysis-visualizations/ | page last changed 2022-10-07 (in 24.12 docs) | "Phylogenetic trees produced by analysis pipelines, for example SNVPhyl, are displayed on the analysis page in the "Phylogentic Tree" Tab. Sample metadata can be displayed concurrently with the tree" [sic] |
| D8 | Y (NCBI SRA) | confirmed (reads to SRA only; BioProject/BioSample must exist; export fixed in 2023, issues #1449/#1451/#1452) | https://phac-nml.github.io/irida-documentation/user/user/samples/ | n.s. | "IRIDA can assist in uploading sequence files to NCBI's Sequence Read Archive . IRIDA requires that BioProjects and BioSamples be created before uploading" |
| D9 | n.d. | confirmed n.d. (no LIMS feature in docs or issues) | — | — | — |

#### IRIDA Next (successor; separate row in the table). Repo https://github.com/phac-nml/irida-next (Apache-2.0, last commit 2026-10-01, no releases); docs https://phac-nml.github.io/irida-next/

| D | Value | Source page | Source date | Verbatim quote |
|---|---|---|---|---|
| D1 | Y | …/docs/intro | 2026-08-05 | "Administer a self-managed IRIDA Next instance." |
| D2 | Y (Apache-2.0) | GitHub README + LICENSE | 2026-10-01 | "IRIDA Next is an open source bioinformatics platform for the storage, management, and analysis of genomic sequences and metadata." |
| D3 | Y | …/docs/user/organization/groups/share-groups | 2024-05-27 | "In IRIDA Next you can invite a group to a group to allow the members of the group access to the shared group" |
| D4 | Y/P (free key–value) | …/docs/user/project/samples/sample-metadata | 2026-08-05 | "Metadata can be added to samples to give them any additional information required by users." |
| D5 | Y (Nextflow via GA4GH WES) | …/docs/configuration/pipelines | 2026-02-02 | "Currently, only **Nextflow** pipelines are supported and they must have a GitHub repository." |
| D6 | n.d. | — | — | — |
| D7 | n.d. (no tree or map viewer documented) | — | — | — |
| D8 | n.d. (downloads only; **regression vs IRIDA's SRA export**) | …/docs/user/export/getting-started | 2026-08-05 | "In IRIDA Next, you can download data from multiple samples or all files associated with a workflow execution at once by creating a data export." |
| D9 | n.d. | — | — | — |

#### Galaxy (releases 25.1 Dec 2025, 26.0 Mar 2026, 26.1 Jul 2026; new paper galaxy2026, NAR 54(W1):W105–W116)

| D | Old | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D1 | Y (2018 paper) | confirmed | https://docs.galaxyproject.org/en/release_26.1/admin/production.html ; galaxy2026 doi:10.1093/nar/gkag469 | Jul 2026 ; 2026-06-09 | "…when setting up Galaxy for a multi-user production environment, there are some additional steps that should be taken for the best performance." / "cloud deployments using Helm charts" |
| D2 | Y MIT | confirmed (peer-reviewed source) | galaxy2026 | 2026 | "We also completed a multiyear transition of the Galaxy codebase from the Academic Free License 3.0 (AFL-3.0) to the MIT License." |
| D4 | n.d. | **CHANGED → P**: "Sample Sheets" (25.1) are typed, author-defined per-sample metadata columns for workflow inputs. They are not a persistent metadata registry. | https://docs.galaxyproject.org/en/release_25.1/releases/25.1_announce_user.html ; galaxy2026 | Dec 2025 ; 2026-06-09 | "Sample Sheets are particularly useful for workflows that require multiple related inputs or when you need to process batches of samples with associated metadata in a structured format." / "allowing workflow authors to define tabular templates that map sample attributes to workflow parameters." |
| D8 | P (2021 paper) | confirmed P (community IUC tools `ena_upload` v0.10.2 and `ena_webin_cli`; no NCBI submission tool; not core) | https://github.com/galaxyproject/tools-iuc/tree/main/tools/ena_upload ; galaxy2026 | 2026-07-31 ; 2026 | "Submits experimental data and respective metadata to the European Nucleotide Archive (ENA)." / "the community has adopted these new capabilities into tools that upload data to ENA" |
| D9 | P (3rd-party 2013) / n.d. | **CHANGED → n.d.** The 2013 Galaxy LIMS was built on the sample-tracking subsystem that Galaxy removed in 2017. An openBIS (ELN-LIMS) file source was merged into `dev` 2026-09-16, but it is **unreleased** and only moves files. | https://github.com/galaxyproject/galaxy/pull/5103 ; https://github.com/galaxyproject/galaxy/pull/23458 | 2017-12-01 ; 2026-09-16 | "This PR removes the sample tracking features entirely from the backend." / "This PR adds an [openBIS](https://openbis.ch/) Galaxy file source using [pyBIS](https://pypi.org/project/pybis/)." |

#### Pathogenwatch (full PDF of alikhan2026pathogenwatch obtained: medRxiv v1, 2026-03-20, CC-BY-NC-ND 4.0)

| D | Old | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D1 | P (quotes to re-check) | confirmed P; quotes verified. No public "Pathogenwatch Local" artefact found (no repo, no docs). | alikhan2026pathogenwatch, DOI 10.64898/2026.03.18.26348693 | 2026-03-20 | "while the same workflows can be run locally via Pathogenwatch Local." / "…with its primary deployment implemented on Amazon Web Services (AWS)." |
| D3 | P (2021 paper) | confirmed P (per-collection invites with roles; no organisation tenancy) | alikhan2026pathogenwatch ; https://cgps.gitbook.io/pathogenwatch/how-to-use-pathogenwatch/collections/creating-sharing-collections | 2026-03-20 ; n.s. | "user-submitted data remain private unless explicitly shared." / "\"Private\" limits access to people you specifically add in the \"Invite\" box, and you can choose what kind of access they should each have (Viewer, Editor, Manager)." |
| D5 | N | confirmed N | https://cgps.gitbook.io/pathogenwatch/supported-organisms | n.s. | "Pathogenwatch provides annotation pipelines for a limited set of species. The pipelines for these species have been constructed and validated with community experts" |
| D7 | Y (2021 paper) | confirmed (2026 source) | alikhan2026pathogenwatch | 2026-03-20 | "Within Collections, phylogenetic trees, maps, timelines, and metadata tables are interactively linked, allowing users to explore how genetic relatedness corresponds to patterns of spread, persistence, and genomic risk factors." |
| D8 | n.d. | confirmed n.d. (data only flow in from INSDC; export is downloads and a REST API). Export is by download and REST API only. | alikhan2026pathogenwatch ; https://cgps.gitbook.io/pathogenwatch/how-to-use-pathogenwatch/the-api | 2026-03-20 ; n.s. | (inbound) "…continuously ingested public genomes from international sequence archives (INSDC: ENA/EBI, NCBI, DDBJ)." |
| D9 | n.d. | confirmed n.d. ("LIMS" absent from the full text and all 104 docs pages) | — | — | — |

#### AusTrakka

| D | Old | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D1 | N (2022 paper) | confirmed N (2025–2026 sources) | https://austrakka.net/docs/overview ; Governance Protocol https://austrakka.net/docs/austrakka-governance-protocol.pdf ; mcewan2026austrakka DOI 10.1186/s44263-026-00265-y | n.s. ; endorsed 2025-11-12 ; 2026-04-17 | "All state and territory public health laboratories upload genomic sequences and agreed epidemiological metadata to AusTrakka on a dedicated server for nationally aggregated genomics analysis and visualisation of sequences." |
| D2 | n.d. | **CHANGED → N** under the D2 rule (public code without a licence). No LICENSE in any repo (`gh api …/license` → 404); web client `"private": true`; backend not public. The only statement is an MIT classifier under a template comment in the CLI `setup.py`, which is not enough to upgrade. | https://github.com/AusTrakka/austrakka2-cli (setup.py) | 2026-09-30 (PyPI trakka 0.92.2) | "# Pick your license as you wish" / "License :: OSI Approved :: MIT License" |
| D8 | n.d. | confirmed n.d. (data only flow in from ENA/NCBI; reports to CDNA/PHLN/AHPC are written by the National Analysis Team, not exported by the platform) | Governance Protocol p. 6 | 2025-11-12 | "AusTrakka integrates publicly available sequences from international databases into the platform for additional context" |
| D9 | n.d. | confirmed n.d. (no LIMS mention; interoperability only planned) | Governance Protocol fn. 7 | 2025-11-12 | "AusTrakka's interoperability with national public health surveillance systems will also be explored further." |

Meumann et al. 2022 (Pathology) describes one laboratory's own SRA and GISAID uploads and is not evidence for AusTrakka D8.

#### NCBI Pathogen Detection

| D | Old | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D1 | N | confirmed N (stronger quote) | https://www.ncbi.nlm.nih.gov/pathogens/faq/ | n.s. | "Unfortunately the complete current pipeline is tied very tightly to many NCBI internal resources and so it can't be run outside of our environment." |
| D3 | N | confirmed N | https://www.ncbi.nlm.nih.gov/pathogens/submit-data/ | n.s. | "The NCBI Pathogen Detection system is built on the foundation of open data. Data are intended to be submitted and released to the public immediately." |
| D5 | N | confirmed N | https://www.ncbi.nlm.nih.gov/pathogens/faq/ | n.s. | "However, the Pathogen Detection system is a high-throughput, automated system and we are unable to customize SNP cluster contents" |
| D9 | n.d. | confirmed n.d. (automated XML submission exists; not stated as LIMS integration) | https://www.ncbi.nlm.nih.gov/pathogens/submit-data/ | n.s. | "Fully autonomous xml-based document exchange (appropriate for automated systems)" |

#### EFSA One Health WGS System

| D | Old | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D1 | N (2022 talk) | confirmed N | rossi2026aesan (slide 10) ; efsa2026pipeline README | May 2026 ; 2026-05-22 (tag ONE_HEALTH-v3.0.0) | "FLEXIBLE SUBMISSION ROUTES FOR DIFFERENT NATIONAL SETUPS EFSA Azure cloud infrastructure" |
| D3 | Y (2022) | confirmed (2026 sources) | efsa2026topic https://www.efsa.europa.eu/en/topics/topic/whole-genome-sequencing-foodborne-outbreaks ; rossi2026aesan | last reviewed 2026-08-24 ; May 2026 | "Member States are the owners of their own data in the EFSA platform and can manage it within the system." / "Countries have the authority to decide at any time whether to share, edit, or withhold the data (release/unrelease)." |
| D4 | N (2022) | confirmed N (EN-7413 quote verified; EN-9830 defines fixed metadata standards) | efsa2022onehealthwgs abstract ; efsa2025wgsguidelines (EN-9830) abstract | 2022-06-29 ; Dec 2025 | "This report provides also detailed information on the types and formats of data that can be submitted to the EFSA One Health WGS system." / "They define acceptance criteria for WGS data quality, metadata standards, and procedures for voluntary and mandatory data submissions." |
| D5 | P (2022) | confirmed P (external profiles accepted under fixed rules) | rossi2025campy (slide 7) ; efsa2026pipeline README | 2025-09-30 ; 2026-05-22 | "WGS API: Allows the sharing of just profiles and integration with country systems." / "If you download a schema from chewieNS, you must ensure interoperability with the EFSA WGS data collection in order to submit data." |
| D6 | B (2022 + README) | confirmed B, **refined: 5 species** (adds *C. jejuni*, *C. coli*) | efsa2026pipeline README | 2026-05-22 | "Salmonella enterica, Listeria monocytogenes, Escherichia coli (including STEC) of non-human origin, Campylobacter jejuni, and Campylobacter coli" |
| D7 | P no map (2023) | confirmed P (no map or interactive phylogeny documented in 2025–2026 sources) | rossi2023efsaecdc ; efsa2026topic | 2023-09-05 ; 2026-08-24 | "Building databases of genomic profiles from human and food isolates to detect clusters and identify foodborne outbreaks" |
| D8 | Y (ECDC exchange; abstract to re-check); ENA n.d. | confirmed Y (quote verified; current EN-9830 wording; now also the legally mandated reporting route). **ENA stays n.d.** (sources only describe import *from* NCBI/ENA). | efsa2025wgsguidelines abstract ; desmet2025wgs | Dec 2025 ; 2025-10-03 | "Interoperability between EFSA and ECDC WGS systems relies on a query–response mechanism exchanging Core genome Multilocus Sequence Typing (cgMLST) profiles and essential metadata under strict visibility rules." / "Mandatory submission of results to EFSA One Health WGS system" |
| D9 | n.d. | confirmed n.d. (an "API … integration with country systems" exists but is not stated to be LIMS; not counted) | rossi2025campy | 2025-09-30 | (closest, not counted) "API Access Automated system-to-system integration" |

#### Nextstrain

| D | Old | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D6 | B+V (2021 paper) | confirmed (live *M. tuberculosis* build; the only bacterium among 24 pathogens) | https://github.com/nextstrain/tb | 2026-05-25 | "The results of running this workflow are publicly visible at [nextstrain.org/tb/global](https://nextstrain.org/tb/global)." |
| D7 | Y (2018 paper) | confirmed (current docs) | https://docs.nextstrain.org/en/latest/learn/interpret/interacting-with-nextstrain.html | n.s. | "These allow us to display relationships between isolates such as their phylogenetic relationships, putative transmissions on the map, and variability across the genome." |
| D8 | n.d. | confirmed n.d. (ingest only; users are pointed to NCBI for submission) | https://nextstrain.org/blog/2025-11-06-gisaid-based-ncov-analyses | 2025-11-06 | "If you're interested to see your data in these open analyses please consider submitting sequences to INSDC via the NCBI SARS-CoV-2 submission portal ." |
| D9 | n.d. | confirmed n.d. | — | — | — |

#### GISAID

| D | Old | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D1 | N | confirmed; **still only the 2011 EpiFlu DAA** | gisaiddaa https://gisaid.org/terms-of-use/ | effective 2011-03-16 | "The GISAID EpiFlu™ Database utilizes a proprietary platform and software technology (collectively, the " Database Platform ") owned by GISAID and/or third party contractors." |
| D2 | N | confirmed (same source) | gisaiddaa | 2011-03-16 | "You will not copy, reverse engineer, disseminate or disclose any part of the Database Platform." |
| D3 | P (2017 paper) | confirmed P (current FAQ) | https://gisaid.org/help/faq/ | n.s. | "GISAID policies do not permit the storage of restricted sequences in its databases to ensure rapid sharing of all data with the public." / "While Data in GISAID are publicly accessible, Submitters do not forfeit their rights (IPR) to the Data they deposit in GISAID." |
| D4 | n.d. | confirmed n.d. (submission template docs sit behind login; third-party help pages are not primary) | — | — | — |
| D5 | n.d. | confirmed n.d. | — | — | — |
| D7 | P (2021 paper) | confirmed P (current global phylogeny page; no map stated in the text, although it embeds an Auspice view) | https://gisaid.org/sars-cov-2-phylogeny/global/ | n.s. (site © 2008–2026) | "Geographic Spread Modeling: Trees reconstructed from thousands of genomes can identify source populations and paths of international spread, shedding light on how global travel or local factors shape transmission." |
| D8 | N | confirmed | https://gisaid.org/help/faq/ | n.s. | "GISAID does not offer a mechanism to release data to any other database." |
| D9 | n.d. | confirmed n.d. | — | — | — |

#### Pathoplexus (Loculus)

| D | Old | New | Source | Source date | Verbatim quote |
|---|---|---|---|---|---|
| D7 | n.d. | **CHANGED → P** (tree placement and country map through external link-out tools: Nextclade, Taxonium/UShER, Mapoplexus; no built-in combined view) | https://pathoplexus.org/docs/how-to/use-tools-and-add-new-ones ; config https://github.com/pathoplexus/pathoplexus/blob/main/loculus_values/values.yaml | doc 2025-07-07 ; config 2026-09-29 | "perform QC on sequences with Nextclade and see their placement on a phylogenetic tree (only available for some organisms) - visualise the geographic distribution of your sequences" |
| D9 | n.d. | confirmed n.d. ("LIMS" absent from code and issues in both GitHub orgs; only a generic API) | nextstrain2025ppx (context) | 2025-08-28 | (not counted) "Pathoplexus provides a modern API to the data, meaning that it is straightforward and fast to retrieve (and submit) data in an automated way." |

Extra (D8 reconfirmed, 2025): "Open sequences are submitted to INSDC (ENA/NCBI/DDBJ) immediately, while restricted use data are made available for public health and surveillance purposes right away on Pathoplexus" (nextstrain2025ppx).

---

