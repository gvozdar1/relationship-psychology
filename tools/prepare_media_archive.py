#!/usr/bin/env python3
"""Prepare reproducible, connector-friendly media payloads.

The GitHub connector used for this migration has no direct local-file upload action.
This helper therefore creates small base64 text chunks with explicit SHA-256 so a
binary source can be stored losslessly and later reconstructed without trusting a
human copy/paste step.
"""
from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import json
from pathlib import Path
import zipfile

DEFAULT_CHUNK_CHARS = 18_000


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def split_base64(data: bytes, out_dir: Path, chunk_chars: int) -> list[dict]:
    if chunk_chars % 4:
        raise ValueError("chunk size must be divisible by 4 for clean base64 boundaries")
    encoded = base64.b64encode(data).decode("ascii")
    out_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for i in range(0, len(encoded), chunk_chars):
        text = encoded[i:i + chunk_chars]
        name = f"part{i // chunk_chars:02d}.b64"
        path = out_dir / name
        path.write_text(text, encoding="ascii")
        records.append({
            "name": name,
            "chars": len(text),
            "sha256": hashlib.sha256(text.encode("ascii")).hexdigest(),
        })
    return records


def build_zip(files: list[Path], output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for p in files:
            zf.write(p, arcname=p.name)


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("source", type=Path, help="binary file or screenshot directory")
    ap.add_argument("--manifest", type=Path, help="screenshot CSV manifest when source is a directory")
    ap.add_argument("--output", type=Path, required=True, help="output preparation directory")
    ap.add_argument("--chunk-chars", type=int, default=DEFAULT_CHUNK_CHARS)
    ap.add_argument("--zip-name", default="payload.zip")
    args = ap.parse_args()

    args.output.mkdir(parents=True, exist_ok=True)

    if args.source.is_dir():
        if not args.manifest:
            raise SystemExit("--manifest required for a screenshot directory")
        rows = read_manifest(args.manifest)
        if not rows:
            raise SystemExit("empty manifest")
        name_field = list(rows[0])[0]
        files = [args.source / row[name_field] for row in rows]
        missing = [p.name for p in files if not p.exists()]
        if missing:
            raise SystemExit(f"missing {len(missing)} files; first={missing[:5]}")
        payload = args.output / args.zip_name
        build_zip(files, payload)
    else:
        payload = args.source

    data = payload.read_bytes()
    chunks_dir = args.output / "b64"
    chunks = split_base64(data, chunks_dir, args.chunk_chars)
    metadata = {
        "payload_name": payload.name,
        "payload_bytes": len(data),
        "payload_sha256": sha256_bytes(data),
        "base64_chunk_chars": args.chunk_chars,
        "chunk_count": len(chunks),
        "chunks": chunks,
    }
    (args.output / "PREPARED_MANIFEST.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    parts = " ".join(f"b64/{c['name']}" for c in chunks)
    reconstruct = (
        "# Reconstruction\n\n"
        f"Expected bytes: `{len(data)}`  \n"
        f"Expected SHA-256: `{sha256_bytes(data)}`\n\n"
        "```bash\n"
        f"cat {parts} | base64 -d > {payload.name}\n"
        f"test \"$(stat -c%s {payload.name})\" = \"{len(data)}\"\n"
        f"echo \"{sha256_bytes(data)}  {payload.name}\" | sha256sum -c -\n"
        "```\n"
    )
    (args.output / "RECONSTRUCT.md").write_text(reconstruct, encoding="utf-8")
    print(json.dumps(metadata, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
