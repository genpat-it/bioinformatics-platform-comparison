#!/usr/bin/env python3
"""Validate data/comparison.csv: allowed values, known sources, dates.

Run from the repository root:  python3 scripts/validate.py
"""
import csv, re, sys

DIMS = [f"D{i}" for i in range(1, 10)]
VALUE = re.compile(r"^(Y|P|N|n\.d\.)(†|‡|§)*$")
ORGANISMS = re.compile(r"^(n\.d\.|[BVF](,[BVF])*)(†|‡|§)*$")
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

def main():
    bib = open("data/sources.bib", encoding="utf-8").read()
    keys = set(re.findall(r"@\w+\{([^,\s]+),", bib))
    errors = []
    with open("data/comparison.csv", newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    seen = set()
    for n, r in enumerate(rows, start=2):
        name = r["platform"].strip()
        if not name:
            errors.append(f"line {n}: empty platform name")
        if name in seen:
            errors.append(f"line {n}: duplicate platform {name!r}")
        seen.add(name)
        for d in DIMS:
            v = r[d].strip()
            ok = ORGANISMS.match(v) if d == "D6" else VALUE.match(v)
            if not ok:
                errors.append(f"line {n} ({name}): {d} has invalid value {v!r}")
        srcs = [s for s in r["sources"].split(";") if s]
        if not srcs:
            errors.append(f"line {n} ({name}): no sources")
        for s in srcs:
            if s not in keys:
                errors.append(f"line {n} ({name}): source {s!r} not found in data/sources.bib")
        if not DATE.match(r["last_checked"].strip()):
            errors.append(f"line {n} ({name}): last_checked must be YYYY-MM-DD")
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print(f"OK: {len(rows)} platforms, {len(keys)} sources")

if __name__ == "__main__":
    main()
