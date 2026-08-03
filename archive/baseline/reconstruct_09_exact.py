#!/usr/bin/env python3
"""Byte-exact reconstruction of the pre-sync 09_COMBINED_MASTER.md.

The readable archive was split at source line boundaries 220, 440 and 660.
Those three source lines were empty and were omitted by the early split export.
This script restores exactly those missing blank lines and validates the source hash.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARTS = [
    HERE / "09_COMBINED_MASTER.baseline.part01.md",
    HERE / "09_COMBINED_MASTER.baseline.part02.md",
    HERE / "09_COMBINED_MASTER.baseline.part03.md",
    HERE / "09_COMBINED_MASTER.baseline.part04.md",
]
EXPECTED_SIZE = 38249
EXPECTED_SHA256 = "ddd407c8f85bc1d940571cc2dd8468aeaf2fda10360df5156c98893408e16c28"


def main() -> int:
    missing = [p.name for p in PARTS if not p.exists()]
    if missing:
        raise SystemExit(f"missing parts: {missing}")

    texts = [p.read_text(encoding="utf-8") for p in PARTS]
    counts = [len(t.splitlines()) for t in texts]
    if counts != [219, 219, 219, 87]:
        raise SystemExit(f"unexpected part line counts: {counts}")

    # Source lines 220, 440 and 660 were verified as blank in the original local file.
    reconstructed = "\n\n".join(t.rstrip("\n") for t in texts[:-1]) + "\n\n" + texts[-1]
    data = reconstructed.encode("utf-8")
    digest = hashlib.sha256(data).hexdigest()

    if len(data) != EXPECTED_SIZE:
        raise SystemExit(f"size mismatch: {len(data)} != {EXPECTED_SIZE}")
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"sha256 mismatch: {digest} != {EXPECTED_SHA256}")

    out = HERE / "09_COMBINED_MASTER.baseline.exact.md"
    out.write_bytes(data)
    print(f"OK {out.name}: {len(data)} bytes, sha256={digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
