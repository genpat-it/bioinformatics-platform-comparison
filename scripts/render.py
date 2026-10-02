#!/usr/bin/env python3
"""Render data/comparison.csv as the Markdown table in README.md (between the TABLE markers).

Run from the repository root:  python3 scripts/render.py          (rewrite README.md)
                                python3 scripts/render.py --check  (fail if README.md is out of date)
"""
import csv, sys

DIMS = [f"D{i}" for i in range(1, 11)]
START, END = "<!-- TABLE:START -->", "<!-- TABLE:END -->"

def table():
    with open("data/comparison.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    head = "| Platform | Code | Status | " + " | ".join(DIMS) + " | Last checked |"
    sep = "|" + "---|" * (len(DIMS) + 4)
    lines = [head, sep]
    for r in rows:
        cells = []
        for d in DIMS:
            v = r[d]
            if r[f"{d}_note"]:
                v += "<sup>*</sup>"
            cells.append(v)
        name = f"[{r['platform']}]({r['website']})" if r["website"] else r["platform"]
        code = f"[source]({r['source_code']})" if r["source_code"] else "—"
        lines.append(f"| {name} | {code} | {r['status']} | " + " | ".join(cells) + f" | {r['last_checked']} |")
    lines.append("")
    lines.append("<sup>*</sup> A note qualifies the value; notes are in `data/comparison.csv` (columns `D1_note` … `D9_note`). "
                 "Platform names link to the official website; **Code** links to the public source code, where one exists.")
    return "\n".join(lines)

def main():
    readme = open("README.md", encoding="utf-8").read()
    i, j = readme.index(START) + len(START), readme.index(END)
    new = readme[:i] + "\n" + table() + "\n" + readme[j:]
    if "--check" in sys.argv:
        if new != readme:
            print("README.md is out of date: run python3 scripts/render.py")
            sys.exit(1)
        print("README.md table is up to date")
    else:
        open("README.md", "w", encoding="utf-8").write(new)

if __name__ == "__main__":
    main()
