#!/usr/bin/env bash
# Regenerate images/profile/photos.txt from the image files in images/profile/.
#
# The homepage picks a random photo from that list on every visit, so run this
# script after adding or removing photos, then commit both the photos and the
# updated photos.txt.
#
# Usage:  ./scripts/update_profile_photos.sh
set -euo pipefail

cd "$(dirname "$0")/.."
dir="images/profile"
list="$dir/photos.txt"

: > "$list"
for path in "$dir"/*; do
  [ -f "$path" ] || continue
  name="${path##*/}"
  ext="$(printf '%s' "${name##*.}" | tr '[:upper:]' '[:lower:]')"
  case "$ext" in
    jpg|jpeg|png|webp|gif|avif) printf '%s\n' "$name" >> "$list" ;;
  esac
done

echo "Wrote $(wc -l < "$list" | tr -d ' ') photo(s) to $list:"
cat "$list"
