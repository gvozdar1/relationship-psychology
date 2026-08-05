#!/usr/bin/env python3
"""Integrity verifier for the relationship-psychology archive.

The script never promotes analytical claims. It only verifies physical source files,
manifests and reconstructable archive payloads.
"""
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import lzma
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

MESSAGES12_HTML_SHA256 = "d968abf216fc920ea152bced80d06eed5df10d665ba8639726f864e15b0c6bcf"
MESSAGES12_HTML_SIZE = 630716
MESSAGES12_XZ_SHA256 = "7a362a7cd5fd08e1420516e68a842a6ddbe44c804d736aaacec8407f42571de2"
MESSAGES12_XZ_SIZE = 51152
SCREENSHOT_COUNT = 161


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def fail(msg: str) -> None:
    raise AssertionError(msg)


def verify_messages12() -> None:
    base = ROOT / "sources" / "messages12" / "b64"
    parts = [base / f"messages12.html.xz.b64.part{i:02d}" for i in range(1, 5)]
    missing = [str(p.relative_to(ROOT)) for p in parts if not p.exists()]
    if missing:
        fail(f"messages12 missing parts: {missing}")

    encoded = b"".join(p.read_bytes().strip() for p in parts)
    try:
        xz = base64.b64decode(encoded, validate=True)
    except Exception as exc:
        fail(f"messages12 base64 decode failed: {exc}")

    if len(xz) != MESSAGES12_XZ_SIZE:
        fail(f"messages12 XZ size {len(xz)} != {MESSAGES12_XZ_SIZE}")
    if sha256_bytes(xz) != MESSAGES12_XZ_SHA256:
        fail("messages12 XZ SHA-256 mismatch")

    try:
        html = lzma.decompress(xz, format=lzma.FORMAT_XZ)
    except Exception as exc:
        fail(f"messages12 XZ decompression failed: {exc}")

    if len(html) != MESSAGES12_HTML_SIZE:
        fail(f"messages12 HTML size {len(html)} != {MESSAGES12_HTML_SIZE}")
    if sha256_bytes(html) != MESSAGES12_HTML_SHA256:
        fail("messages12 HTML SHA-256 mismatch")

    print("OK messages12.html: lossless reconstruction verified")


def load_screenshot_manifest() -> tuple[list[dict[str, str]], str]:
    path = ROOT / "sources" / "screenshots" / "original_manifest.csv"
    if not path.exists():
        fail("missing sources/screenshots/original_manifest.csv")
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        if not reader.fieldnames:
            fail("screenshot manifest has no header")
        name_field = reader.fieldnames[0]
    if len(rows) != SCREENSHOT_COUNT:
        fail(f"screenshot manifest rows {len(rows)} != {SCREENSHOT_COUNT}")
    names = [r[name_field] for r in rows]
    if len(names) != len(set(names)):
        fail("duplicate canonical screenshot names in manifest")
    print(f"OK screenshot manifest: {len(rows)} unique canonical rows")
    return rows, name_field


def detect_field(row: dict[str, str], candidates: tuple[str, ...]) -> str | None:
    lower = {k.lower(): k for k in row}
    for c in candidates:
        if c in lower:
            return lower[c]
    for key in row:
        lk = key.lower()
        if any(c in lk for c in candidates):
            return key
    return None


def verify_local_screenshots(directory: Path) -> None:
    rows, name_field = load_screenshot_manifest()
    if not rows:
        return
    sha_field = detect_field(rows[0], ("sha256", "sha-256", "sha_256"))
    size_field = detect_field(rows[0], ("size", "bytes", "byte_size"))
    if not sha_field:
        fail("cannot identify SHA-256 column in screenshot manifest")

    missing: list[str] = []
    mismatched: list[str] = []
    for row in rows:
        name = row[name_field]
        path = directory / name
        if not path.exists():
            missing.append(name)
            continue
        if size_field and row.get(size_field):
            expected_size = int(row[size_field])
            if path.stat().st_size != expected_size:
                mismatched.append(f"{name}: size")
                continue
        if sha256_file(path) != row[sha_field].strip().lower():
            mismatched.append(f"{name}: sha256")

    if missing:
        fail(f"missing local screenshots: {len(missing)}; first={missing[:5]}")
    if mismatched:
        fail(f"mismatched local screenshots: {len(mismatched)}; first={mismatched[:5]}")
    print(f"OK local originals: {len(rows)} screenshots match manifest")


def reconstruct_b64_parts(directory: Path, output: Path) -> None:
    parts = sorted(p for p in directory.glob("*.b64") if p.is_file())
    if not parts:
        fail(f"no .b64 parts in {directory}")
    encoded = b"".join(p.read_bytes().strip() for p in parts)
    data = base64.b64decode(encoded, validate=True)
    output.write_bytes(data)
    print(f"WROTE {output}: {len(data)} bytes, sha256={sha256_bytes(data)}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--local-screenshots", type=Path, help="directory containing canonical original screenshots")
    ap.add_argument("--reconstruct-b64", type=Path, help="directory with ordered .b64 chunks")
    ap.add_argument("--output", type=Path, help="output file for --reconstruct-b64")
    args = ap.parse_args()

    try:
        verify_messages12()
        load_screenshot_manifest()
        if args.local_screenshots:
            verify_local_screenshots(args.local_screenshots)
        if args.reconstruct_b64:
            if not args.output:
                fail("--output is required with --reconstruct-b64")
            reconstruct_b64_parts(args.reconstruct_b64, args.output)
    except AssertionError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
