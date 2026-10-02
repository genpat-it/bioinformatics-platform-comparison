#!/usr/bin/env python3
"""Build the GitHub Pages site (site/index.html) from data/comparison.csv and evidence/EVIDENCE.md.

Run from the repository root:  python3 scripts/build_site.py
"""
import csv, json, re, html, os

REPO = "https://github.com/genpat-it/bioinformatics-platform-comparison"
DIMS = [f"D{i}" for i in range(1, 12)]
LABELS = {
    "D1": ("Deployment", "Self-hosted or cloud service: can an institution install it on its own infrastructure? Y installable; N only a centrally hosted service; P only the underlying software or some components"),
    "D2": ("Open licence", "Licence meeting the Open Source Definition; source-available code under another licence, or without one, is N"),
    "D3": ("Ownership & access", "Data ownership and access control across institutions"),
    "D4": ("Extensible metadata", "Metadata model extensible by an operator without code changes"),
    "D5": ("Added pipelines", "Operator- or user-added analysis pipelines"),
    "D6": ("Microorganisms", "Microorganisms covered: B bacteria, V viruses, F fungi"),
    "D7": ("Tree + metadata + map", "Phylogeny, metadata and map in one view"),
    "D8": ("Submission / exchange", "Built-in submission, brokerage or structured exchange with an external repository or authority (a plain download does not count)"),
    "D9": ("LIMS integration", "Integration with a laboratory information management system"),
    "D11": ("Sample grouping", "Samples can be grouped into named, persistent sets (projects, collections, tags, workspaces) reused to select samples for analysis, visualisation or sharing"),
    "D10": ("Raw reads", "Raw sequencing reads (e.g. FASTQ) accepted as input and processed by the platform, rather than only assemblies, consensus sequences or derived results"),
}
# evidence section heading (prefix) -> platform name in the CSV
SECTIONS = {"1.": "BIGSdb-Pasteur", "2.": "PubMLST", "3.": "EnteroBase", "4.": "CGE (genepi.dk)",
            "5.": "IRIDA", "5b.": "IRIDA Next", "6.": "Galaxy", "7.": "Pathogenwatch", "8.": "AusTrakka",
            "9.": "NCBI Pathogen Detection", "10.": "EFSA One Health WGS System", "11.": "Nextstrain",
            "12.": "GISAID", "13.": "Pathoplexus"}

def evidence():
    text = open("evidence/EVIDENCE.md", encoding="utf-8").read()
    part = text[text.index("## (a)"):text.index("## (b)")]
    ev = {}
    for sec in re.split(r"\n### ", part)[1:]:
        key = sec.split()[0]
        plat = SECTIONS.get(key)
        if not plat:
            continue
        cells = {}
        for line in sec.split("\n"):
            m = re.match(r"^\| (D\d+) \|(.*)\|\s*$", line)
            if not m:
                continue
            cols = [c.strip() for c in m.group(2).split(" | ")]
            source = " · ".join(c for c in cols[1:-1] if c)
            source = source.replace("…/", "https://phac-nml.github.io/irida-next/") if plat == "IRIDA Next" else source
            cells[m.group(1)] = {"value": cols[0], "source": source, "quote": cols[-1]}
        ev[plat] = cells
    return ev

def main():
    rows = list(csv.DictReader(open("data/comparison.csv", newline="", encoding="utf-8")))
    ev = evidence()
    data = []
    for r in rows:
        data.append({
            "platform": r["platform"], "website": r["website"], "code": r["source_code"],
            "scope": r["scope"], "status": r["status"], "checked": r["last_checked"],
            "values": {d: r[d] for d in DIMS}, "notes": {d: r[f"{d}_note"] for d in DIMS},
            "sources": [s for s in r["sources"].split(";") if s],
            "evidence": ev.get(r["platform"], {}),
        })
    tpl = open("scripts/site_template.html", encoding="utf-8").read()
    out = (tpl.replace("__DATA__", json.dumps(data, ensure_ascii=False))
              .replace("__LABELS__", json.dumps(LABELS, ensure_ascii=False))
              .replace("__DIMS__", json.dumps(DIMS))
              .replace("__REPO__", REPO)
              .replace("__CHECKED__", max(r["last_checked"] for r in rows)))
    os.makedirs("site", exist_ok=True)
    open("site/index.html", "w", encoding="utf-8").write(out)
    export = {
        "title": "Bioinformatics platform comparison",
        "description": "Documented features of genomic-surveillance platforms, from public sources only. "
                       "n.d. = not documented (not absent); not a ranking.",
        "source": REPO,
        "site": "https://genpat-it.github.io/bioinformatics-platform-comparison/",
        "license": "CC-BY-4.0",
        "last_checked": max(r["last_checked"] for r in rows),
        "values": {"Y": "core function of the service or software named in the row",
                   "P": "available only through underlying software, a plug-in, an external component or a third-party integration, or only in part",
                   "N": "a public source states that the feature is not available",
                   "n.d.": "no public source found (does not imply absence)"},
        "features": {d: {"name": LABELS[d][0], "definition": LABELS[d][1]} for d in DIMS},
        "platforms": data,
    }
    open("site/data.json", "w", encoding="utf-8").write(json.dumps(export, ensure_ascii=False, indent=2))
    print(f"site/index.html, site/data.json: {len(data)} platforms")

if __name__ == "__main__":
    main()
