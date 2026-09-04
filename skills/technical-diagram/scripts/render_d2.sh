#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: bash scripts/render_d2.sh <input.d2> <output.svg>" >&2
  exit 2
fi

input=$1
output=$2
script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)
d2_bin=${D2_BIN:-}

if [[ ! -f "$input" ]]; then
  echo "input not found: $input" >&2
  exit 2
fi
if [[ "$output" != *.svg ]]; then
  echo "output must end in .svg: $output" >&2
  exit 2
fi
if [[ -z "$d2_bin" ]]; then
  d2_bin=$(command -v d2 || true)
fi
if [[ -z "$d2_bin" || ! -x "$d2_bin" ]]; then
  echo "D2 renderer not found; install d2 or set D2_BIN to an executable" >&2
  exit 127
fi

"$d2_bin" fmt --check "$input"
"$d2_bin" validate "$input"
"$d2_bin" --layout elk --pad 16 "$input" "$output"
python3 "$script_dir/validate_svg.py" "$output"
