from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
segments_path = ROOT / "ch01_segments.json"
pronunciation_path = ROOT / "ch01_pronunciation.json"
build_dir = ROOT.parents[1] / "build" / "pantheon_ch01"
build_dir.mkdir(parents=True, exist_ok=True)
audit_path = build_dir / "pronunciation_audit.txt"

segments = json.loads(segments_path.read_text(encoding="utf-8"))
pronunciation = json.loads(pronunciation_path.read_text(encoding="utf-8"))

# Manual correction layer for words whose stress is project-specific/slang or
# was previously entered incorrectly. This operates only on the pronunciation
# copy; the literary source text is never changed.
EXACT_CORRECTIONS = {
    "ебани́стической": "ебанисти́ческой",
}

VOWELS = set("аеёиоуыэюяАЕЁИОУЫЭЮЯ")
ALLOW_UNSTRESSED_MULTISYLLABLE = {
    "обо",  # unstressed preposition in "обо мне"
}

missing = []
unstressed = []
audit_lines = []

for i, seg in enumerate(segments, start=1):
    original = seg["text"]
    spoken = pronunciation.get(original)
    if spoken is None:
        missing.append((i, original))
        continue

    for bad, good in EXACT_CORRECTIONS.items():
        spoken = spoken.replace(bad, good)

    # Hard QA gate: every multi-syllable Russian lexical token must carry an
    # explicit acute accent (or ё, which already fixes stress), except listed
    # unstressed function words. This prevents a fallback path from silently
    # returning plain unaccented Russian again.
    for token in re.findall(r"[А-Яа-яЁё\u0301-]+", spoken):
        plain = token.replace("\u0301", "").strip("-")
        if not plain:
            continue
        vowel_count = sum(ch in VOWELS for ch in plain)
        if vowel_count <= 1:
            continue
        if plain.lower() in ALLOW_UNSTRESSED_MULTISYLLABLE:
            continue
        if "ё" in plain.lower() or "\u0301" in token:
            continue
        unstressed.append((i, token, spoken))

    seg["source_text"] = original
    seg["text"] = spoken
    audit_lines.append(f"[{i:02d}] {seg.get('voice', '?')} / {seg.get('role', '?')}\n{spoken}\n")

if missing:
    raise SystemExit("Missing pronunciation entries: " + repr(missing))

if unstressed:
    details = "\n".join(f"segment {i}: {token!r} :: {line}" for i, token, line in unstressed)
    raise SystemExit("Pronunciation QA failed: multisyllable tokens without explicit stress:\n" + details)

segments_path.write_text(
    json.dumps(segments, ensure_ascii=False, indent=2) + "\n",
    encoding="utf-8",
)
audit_path.write_text("\n".join(audit_lines), encoding="utf-8")
print(f"Applied and QA-checked full pronunciation layer to {len(segments)} segments")
print(f"Pronunciation audit: {audit_path}")
