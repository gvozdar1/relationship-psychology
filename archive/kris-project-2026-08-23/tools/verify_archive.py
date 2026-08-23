#!/usr/bin/env python3
import csv
import hashlib
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
MANIFEST = REPO / "archive/kris-project-2026-08-23/ARCHIVE_MANIFEST.tsv"

def hash_file(path):
    h = hashlib.sha256()
    size = 0
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            size += len(block)
            h.update(block)
    return size, h.hexdigest()

def hash_parts(path):
    h = hashlib.sha256()
    size = 0
    parts = sorted(path.glob("part-*.bin"))
    if not parts:
        raise FileNotFoundError(f"no parts in {path}")
    for part in parts:
        with part.open("rb") as f:
            for block in iter(lambda: f.read(1024 * 1024), b""):
                size += len(block)
                h.update(block)
    return size, h.hexdigest()

errors = []
checked = 0
with MANIFEST.open(encoding="utf-8", newline="") as f:
    for row in csv.DictReader(f, delimiter="\t"):
        path = REPO / row["path"]
        try:
            actual_size, actual_sha = hash_parts(path) if row["kind"] == "parts" else hash_file(path)
        except Exception as exc:
            errors.append(f'{row["path"]}: {exc}')
            continue
        checked += 1
        if actual_size != int(row["size"]) or actual_sha != row["sha256"]:
            errors.append(
                f'{row["path"]}: expected {row["size"]}/{row["sha256"]}, '
                f'got {actual_size}/{actual_sha}'
            )

if errors:
    print(f"FAIL: {len(errors)} problem(s), {checked} entry/entries checked")
    print("\n".join(errors))
    sys.exit(1)

print(f"OK: {checked} manifest entries verified")
