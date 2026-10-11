#!/usr/bin/env python3
"""Sync images/self/photos.json with the image files in images/self/.

The homepage shows a random entry from photos.json on every visit, captioned
"<year> at <place>". Run this after adding or removing photos:

    ./scripts/update_profile_photos.py

New files are appended with an empty year/place for you to fill in; entries
whose file no longer exists are dropped. Then commit the photos and photos.json.
"""
import json
import sys
from pathlib import Path

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif"}

root = Path(__file__).resolve().parent.parent
photo_dir = root / "images" / "self"
manifest = photo_dir / "photos.json"

entries = json.loads(manifest.read_text(encoding="utf-8")) if manifest.exists() else []
files = sorted(
    p.name for p in photo_dir.iterdir() if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES
)

kept = []
for entry in entries:
    if entry.get("file") in files:
        kept.append(entry)
    else:
        print(f"dropped: {entry.get('file')!r} (file not found in {photo_dir.relative_to(root)})")
listed = {entry["file"] for entry in kept}
for name in files:
    if name not in listed:
        kept.append({"file": name, "year": "", "place": ""})
        print(f"added:   {name!r} (fill in year and place)")

manifest.write_text(json.dumps(kept, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

print(f"{manifest.relative_to(root)}: {len(kept)} photo(s)")
for entry in kept:
    print(f"  {entry['file']:<24} {entry.get('year') or '?'} at {entry.get('place') or '?'}")

incomplete = [entry["file"] for entry in kept if not (entry.get("year") and entry.get("place"))]
if incomplete:
    print("Fill in year and place for:", ", ".join(incomplete))
    sys.exit(1)
