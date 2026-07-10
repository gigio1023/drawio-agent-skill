#!/usr/bin/env bash
# Clone official draw.io documentation and example sources into
# references/upstream/ for local lookup. The directory is gitignored;
# nothing cloned here is committed. Run from anywhere.
#
# Usage:
#   scripts/fetch_upstream_docs.sh                 # core set (~30MB)
#   scripts/fetch_upstream_docs.sh --with-mxgraph  # + archived mxGraph docs (~63MB)
#   scripts/fetch_upstream_docs.sh --with-app-templates
#       # + jgraph/drawio built-in templates via sparse checkout (~11MB).
#       # NOTE: that templates directory is CC BY 4.0, not Apache-2.0.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$ROOT/references/upstream"
WITH_MXGRAPH=0
WITH_APP_TEMPLATES=0

for arg in "$@"; do
  case "$arg" in
    --with-mxgraph) WITH_MXGRAPH=1 ;;
    --with-app-templates) WITH_APP_TEMPLATES=1 ;;
    *)
      echo "unknown option: $arg" >&2
      exit 2
      ;;
  esac
done

mkdir -p "$DEST"

clone_or_update() {
  local repo="$1" dir="$2"
  if [ -d "$DEST/$dir/.git" ]; then
    echo "updating $dir"
    git -C "$DEST/$dir" pull --ff-only
  else
    echo "cloning $repo -> references/upstream/$dir"
    git clone --depth 1 "https://github.com/$repo.git" "$DEST/$dir"
  fi
}

# Canonical AI-generation references (drawio.com/docs cites shared/ as canonical).
clone_or_update jgraph/drawio-mcp drawio-mcp

# Official sample diagrams and template gallery in raw draw.io XML/SVG.
clone_or_update jgraph/drawio-diagrams drawio-diagrams

if [ "$WITH_MXGRAPH" = 1 ]; then
  # Archived but authoritative model/style/edge-routing documentation.
  clone_or_update jgraph/mxgraph mxgraph
fi

if [ "$WITH_APP_TEMPLATES" = 1 ]; then
  if [ -d "$DEST/drawio/.git" ]; then
    echo "updating drawio app templates"
    git -C "$DEST/drawio" pull --ff-only
  else
    echo "sparse-cloning jgraph/drawio templates (CC BY 4.0)"
    git clone --depth 1 --filter=blob:none --sparse \
      https://github.com/jgraph/drawio.git "$DEST/drawio"
    git -C "$DEST/drawio" sparse-checkout set src/main/webapp/templates
  fi
fi

echo
echo "Done. Local map: references/local/upstream-docs-map.md"
