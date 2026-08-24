#!/usr/bin/env bash

set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: scripts/render_deck.sh slides/lecture-name.ipynb"
  exit 2
fi

deck="$1"
deck_name="$(basename "$deck" .ipynb)"
deck_dir="$(cd "$(dirname "$deck")" && pwd)"
output_dir="${TMPDIR:-/tmp}/gw-ece6210-rise/${deck_name}"
python_command="${PYTHON:-python3}"
jupyter_command="${JUPYTER:-jupyter}"
kernel_name="${KERNEL_NAME:-python3}"

mkdir -p "$output_dir"

if [[ -d "$deck_dir/img" ]]; then
  cp -R "$deck_dir/img" "$output_dir/"
fi

"$python_command" scripts/validate_deck.py "$deck"

"$jupyter_command" nbconvert \
  --to notebook \
  --execute "$deck" \
  --ExecutePreprocessor.kernel_name="$kernel_name" \
  --ExecutePreprocessor.timeout=180 \
  --output "${deck_name}-executed.ipynb" \
  --output-dir "$output_dir"

"$jupyter_command" nbconvert \
  --to slides \
  "$output_dir/${deck_name}-executed.ipynb" \
  --output "$deck_name" \
  --output-dir "$output_dir"

echo "$output_dir/${deck_name}.slides.html"
