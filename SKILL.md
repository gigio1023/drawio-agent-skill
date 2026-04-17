---
name: drawio-diagram
description: >
  Create native draw.io diagrams that fully use draw.io as an editable authoring
  surface, not just as XML output. Use when the user asks for draw.io, .drawio
  files, flowcharts, architecture diagrams, research figures, compact editorial
  visuals, component-to-component arrows, or wants AI to produce a mostly-finished
  diagram that a human can still refine cleanly. Prefer this over ad-hoc diagram
  XML when readability, editability, explicit structure, and shareable PNG/SVG/PDF
  exports all matter.
---

# Draw.io Diagram

## Quick Start

Use this skill when the goal is not merely “generate a diagram,” but “author a native `.drawio` file that already contains the intended elements, stays readable, and remains easy for a human to revise.”

Default path:

1. Choose one grammar from `references/figure-grammars.md`
2. Keep the first pass compact:
   - 3-5 primary components
   - one dominant component-to-component arrow path
   - optional side rail
   - optional bottom strip
3. Generate native draw.io XML with real draw.io structure
4. Prefer inclusion over perfection:
   - if an intended element matters, include it explicitly
   - never drop important components just to keep the page pretty
5. Run the preflight from `references/layout-safety.md`
6. If the user wants an external review artifact, export `.drawio.png` or `.drawio.svg` when the draw.io CLI is available

## Prerequisites

- Authoring `.drawio` source files needs no tools beyond the agent — the skill writes native mxGraphModel XML directly.
- Exporting to PNG / SVG / PDF requires the draw.io CLI (bundled with the desktop app).
- draw.io Desktop is optional but recommended for interactive refinement after the skill finishes authoring.

### Locating the draw.io CLI

First, try `which drawio` (or `where drawio` on Windows). If not on PATH, fall back to the platform-specific path.

| Environment | CLI location | Detection hint |
|---|---|---|
| macOS | `/Applications/draw.io.app/Contents/MacOS/draw.io` | Install [draw.io Desktop](https://github.com/jgraph/drawio-desktop/releases) |
| Linux (native) | `drawio` on PATH | Via snap / apt / flatpak |
| Windows (native) | `C:\Program Files\draw.io\draw.io.exe` | Default installer path |
| WSL2 | `` `/mnt/c/Program Files/draw.io/draw.io.exe` `` | Detect via `grep -qi microsoft /proc/version 2>/dev/null && echo WSL2`. Backticks around the path handle the space in `Program Files` in bash. |
| Headless / CI | `npx --yes @hediet/drawio-export` | No prior install; prefer when no desktop app is available |

If the primary path is missing on WSL2, check the per-user install at `/mnt/c/Users/$WIN_USER/AppData/Local/Programs/draw.io/draw.io.exe`.

## Runtime modes

Use this order unless the user explicitly asks for something else:

1. `offline-first`
   - native `.drawio` is the source of truth
2. `desktop-enhanced`
   - same authoring model, plus draw.io Desktop export when available
3. `reference-refresh`
   - refresh official references with `scripts/download_reference_set.py`

## Reference Files

| File | When to read | What's in it |
|------|-------------|--------------|
| `references/upstream-drawio-rules.md` | Always before generating XML from scratch | Tight opinionated digest of the rules this skill enforces: root cells, edges, containers, metadata, export |
| `references/drawio-xml-reference.md` | When you need authoritative depth on XML | Full vendored copy of `jgraph/drawio-mcp` `shared/xml-reference.md` (Apache-2.0): edge routing priorities, fan-out bundling, containers, layers, tags, metadata, placeholders, dark mode, well-formedness |
| `references/drawio-style-reference.md` | When you need a non-default shape or to verify a style property spelling | Full vendored copy of `jgraph/drawio-mcp` `shared/style-reference.md` (Apache-2.0): comprehensive shape / style catalog |
| `references/figure-grammars.md` | Before choosing a page structure | The allowed grammars and page-budget rules |
| `references/layout-safety.md` | Before finalizing any figure | Overlap, routing, text overflow, arrowhead, and corridor gotchas |
| `references/visual-patterns.md` | When the user wants compact, high-signal, editorial/product-style figures | Pattern extraction from OpenAI, Anthropic, and Vercel references collected in the last year |
| `references/reference-set.md` | When you need provenance for the visual guidance | Curated official pages and what they contributed |
| `references/community-lessons.md` | When improving the skill or handling dense/specialized requests | Practical lessons extracted from community draw.io skills and adjacent diagram ecosystems |

## Detailed Workflow

### 1. Understand the figure

Extract:

- what the figure must communicate
- which components must appear
- which arrows must connect which components
- whether the user needs `.drawio` only or also exported review artifacts

If the user asks for “OpenAI/Anthropic/Vercel-like,” treat that as a compact layout and information-hierarchy hint, not as permission to clone brand assets.

### 2. Choose one grammar only

Read `references/figure-grammars.md`.

Allowed grammars:

- `flow-canvas`
- `report-split`
- `system-map`
- `insight-panels`
- `annotated-chart-card`

Do not improvise a fourth grammar on the first pass. If the request does not fit, simplify it until it does.

### 3. Lock the page budget

Before writing XML, decide:

- page size
- title stack
- main panel
- optional side rail
- optional bottom strip
- primary component count
- arrow count

Default limits:

- 3-5 primary components
- 1 dominant arrow path
- 0-2 secondary arrows
- 1 feedback loop max
- 1 main takeaway per panel

If the request exceeds that, split into multiple pages instead of forcing density.

### 4. Use draw.io as an authoring surface

Generate native draw.io structure, not loose decorative XML.

Required structure:

- `mxfile > diagram > mxGraphModel`
- root cells `0` and `1`
- `adaptiveColors="auto"`
- every edge has `<mxGeometry relative="1" as="geometry" />`

Preferred draw.io primitives:

- `swimlane` for titled panels
- `group;` for invisible grouping
- `container=1;pointerEvents=0;` for decorative containers
- `object` / `UserObject` wrappers when placeholders or metadata improve editability
- extra layers only when commentary would clutter the main layer

### 5. Make important arrows obvious

If components are meant to be connected, the arrows must be obvious at a glance.

That means:

- component-to-component arrows, not only corridor hints
- visible arrowheads
- short edge labels only when they carry meaning
- one dominant path with stronger color and weight
- quieter secondary paths, usually dashed
- explicit waypoints whenever multiple edges would compete for the same corridor

### 6. Preserve editability

The human should be able to open the file and keep working without reconstructing missing intent.

So:

- include all intended components even if some are conservative
- use clear panel headers
- keep caption, source, and explanation strips outside the main node field
- prefer simple shapes with strong labels over decorative cleverness
- keep `.drawio` as the authoring source of truth

### 7. Use the reference set when compact polish matters

When the figure should feel compact, very clear, and high-signal:

1. Read `references/visual-patterns.md`
2. Borrow layout behaviors, not brand assets
3. Use the collected official references under `data/references/` only as pattern evidence

### 8. Choose fast path or full path

Use `fast path` when all are true:

- the diagram type is obvious
- the figure is single-page and low-branching
- required components are already explicit

Use `full path` when any are true:

- dense branching
- chart annotations matter
- replication or heavy edit
- report quality matters
- the user explicitly wants compact editorial polish

In `full path`, write a tiny internal plan first:

- grammar
- panel roles
- required components
- required arrows
- export target

### 9. Post-process edge routing (optional)

If `npx @drawio/postprocess` is available, run it against the `.drawio` file to simplify waypoints, fix edge-vertex collisions, and straighten approach angles. Skip silently if not installed — do not prompt the user to install it.

```bash
npx @drawio/postprocess <path>.drawio   # in-place; keep the original via git before running
```

### 10. Export only if supported

If the draw.io CLI exists, export with `--embed-diagram` so the output still carries the diagram XML. Then open the result if the environment supports it. If the CLI is missing, keep the `.drawio` source and tell the user the editable file is ready.

**Export command:**

```bash
drawio -x -f <format> -e -b 10 -o <output> <input.drawio>
```

WSL2 variant:

```bash
`/mnt/c/Program Files/draw.io/draw.io.exe` -x -f png -e -b 10 -o diagram.drawio.png diagram.drawio
```

**Flags:**

| Flag | Meaning |
|---|---|
| `-x` / `--export` | Export mode |
| `-f` / `--format` | Output format: `png`, `svg`, `pdf`, `jpg` |
| `-e` / `--embed-diagram` | Embed diagram XML in the output (PNG, SVG, PDF only) |
| `-o` / `--output` | Output file path |
| `-b` / `--border` | Border width around the diagram (default 0) |
| `-t` / `--transparent` | Transparent background (PNG only) |
| `-s` / `--scale` | Scale factor |
| `--width` / `--height` | Fit into specified dimensions (preserves aspect ratio) |
| `-a` / `--all-pages` | Export all pages (PDF only) |
| `-p` / `--page-index` | Select a specific page (1-based) |

**Deliberate divergence from upstream:** `jgraph/drawio-mcp` skill-cli deletes the intermediate `.drawio` after export because the exported `.drawio.*` carries the embedded XML. **This skill does not delete the source.** Keep `.drawio` alongside `.drawio.{png|svg|pdf}` — it is the round-trippable source of truth and avoids having to decode embedded XML from an image later.

### 11. Open the result

| Environment | Command |
|---|---|
| macOS | `open <file>` |
| Linux (native) | `xdg-open <file>` |
| WSL2 | `cmd.exe /c start "" "$(wslpath -w <file>)"` |
| Windows (native) | `start <file>` |

On WSL2, `wslpath -w` converts a WSL path to a Windows path; the empty string after `start` prevents `start` from treating the filename as a window title. If the open command fails, print the absolute path so the user can open it manually.

## File naming

- Base name: lowercase, hyphen-separated, content-descriptive (`login-flow`, `database-schema`, `ingestion-pipeline`).
- Source: `<name>.drawio`.
- Exports: double extension — `<name>.drawio.png`, `<name>.drawio.svg`, `<name>.drawio.pdf`. The double extension signals that the file contains embedded diagram XML and remains editable in draw.io.

## Outputs

- Primary: `.drawio` — native mxGraphModel XML, source of truth. Editable in draw.io Desktop or diagrams.net.
- Optional exports: `.drawio.png`, `.drawio.svg`, `.drawio.pdf`. The `.drawio.*` double extension signals that the export carries the source XML embedded in the file, so any of them can be reopened in draw.io and revised without rebuilding from scratch.

| Format | Extension | Notes |
|--------|-----------|-------|
| (default) | `.drawio` | Native XML, no CLI required |
| `png` | `.drawio.png` | Viewable everywhere, embedded XML, still editable in draw.io |
| `svg` | `.drawio.svg` | Scalable, embedded XML, still editable in draw.io |
| `pdf` | `.drawio.pdf` | Printable, embedded XML, still editable in draw.io |

Preferred export defaults when the CLI is available:

- `.drawio.png` for easy sharing with embedded XML
- `.drawio.svg` for vector review

If the CLI is unavailable, return the `.drawio` source and note that the editable authoring target is ready; exporting is a strictly optional second step.

## Why native `.drawio` only?

A `.drawio` file is literally mxGraphModel XML. Mermaid and CSV intents require the draw.io server-side converter and cannot be round-tripped as editable sources of truth. Generating XML directly means:

- no server dependency
- no conversion step
- the file is immediately editable in draw.io Desktop or diagrams.net

The `.drawio.*` double-extension exports are optional convenience artifacts; the `.drawio` file itself is always the authoring target.

## CRITICAL: XML well-formedness

Adapted from `jgraph/drawio-mcp` (Apache-2.0). Violating any of these will silently corrupt the diagram — draw.io may render blank, hang, or drop cells without warning.

- **NEVER include ANY XML comments (`<!-- -->`) in the output.** XML comments are strictly forbidden — they waste tokens, can cause parse errors, and serve no purpose in diagram XML.
- Escape special characters in attribute values: `&amp;`, `&lt;`, `&gt;`, `&quot;`. Line breaks in labels: `&#xa;` or `&lt;br&gt;` (requires `html=1`). Never `\n`.
- Every `mxCell` uses a unique `id`.
- Every edge must contain `<mxGeometry relative="1" as="geometry" />` as a child element. Self-closing edge cells will not render correctly.
- When a label contains HTML tags, include `html=1` in the style. Best practice: include `html=1` in every cell style — plain text is unaffected.
- Root cells `id="0"` and `id="1" parent="0"` must exist.

For the full ruleset, see [`references/drawio-xml-reference.md`](references/drawio-xml-reference.md).

## Troubleshooting

| Problem | Cause | Solution |
|---------|-------|----------|
| `drawio` CLI not found | Desktop app not installed, not on PATH | Install [draw.io Desktop](https://github.com/jgraph/drawio-desktop/releases), or use `npx --yes @hediet/drawio-export`; otherwise keep the `.drawio` file and tell the user |
| Export produces empty / corrupt file | Invalid XML (double-hyphen comments, unescaped specials, malformed nesting) | Validate XML well-formedness before writing; see the section above |
| Diagram opens but looks blank | Missing root cells `id="0"` / `id="1"` | Ensure the basic `mxGraphModel` structure is complete |
| Edges don't render | Edge `mxCell` self-closing (no child `mxGeometry`) | Every edge must have `<mxGeometry relative="1" as="geometry" />` as a child |
| File won't open after export | Path resolution failure (especially on WSL2) | Print the absolute path so the user can open it manually; on WSL2, use `wslpath -w` |
| Labels overflow their shape | Long text + small box | Shorten the label first; only widen the shape if the label is irreducible |
| Edges tangle through unrelated boxes | No obstacle-avoidance in auto-router | Add explicit waypoints; route around rows / columns; see the orthogonal routing rules in [`references/drawio-xml-reference.md`](references/drawio-xml-reference.md) |

## Scripts

- `scripts/download_reference_set.py` — refresh official reference pages and selected images into `data/references/`

Use the script when the reference set is stale or when you want to expand the visual study.

## Sample Assets

- `assets/safe-layout-flow-canvas.drawio`
- `assets/safe-layout-routed-canvas.drawio`
- `assets/drawio-skill-template-pack.drawio`

Use them as editable starting points, not as rigid finished artwork.

## Gotchas

- The main failure mode is not “weak styling.” It is overlap, unreadable routing, and hidden intent.
- draw.io does not perform collision detection for edges. If arrows matter, you must budget corridors manually.
- If an arrow is important, do not trust default routing when multiple edges leave one component.
- Long labels create fake overlap. Shorten text before enlarging the page.
- Missing components are worse than conservative styling. Include the intended elements first.
- Do not optimize for “fancy” on pass one. Optimize for editable correctness.
- If the page starts needing too many components and cross-links, split the figure.
- Compact figure design from strong tech blogs usually comes from page grammar and annotation discipline, not decorative flourishes.
- Dense chart panels should prefer direct labels and on-chart callouts over detached legends.
- If a figure looks attractive but forces the reader to hunt for the conclusion, it is still a bad figure.
- Community skills often over-index on DSLs. Keep this skill focused on authoring quality unless extra abstraction is clearly worth it.

## Validation Checklist

- XML is well-formed (no `<!-- -->` comments; unique `mxCell` ids; escaped `&amp;` / `&lt;` / `&gt;` / `&quot;`)
- Root cells `id="0"` and `id="1" parent="0"` are present
- Every edge has `<mxGeometry relative="1" as="geometry" />` as a child
- `adaptiveColors="auto"` is set on `mxGraphModel`
- All requested components are present
- One consistent edge style per diagram (all orthogonal, all straight, or all curved — never mixed with elbow as the simpler-bend variant)
- Main arrows connect visible components directly
- No text escapes a component box
- No component visibly overlaps another
- Feedback loops and side links use separate corridors
- The file remains understandable if a human opens it with no chat context
- If the figure contains a chart, the takeaway is visible without reading every axis tick

## Attribution

This skill vendors portions of [`jgraph/drawio-mcp`](https://github.com/jgraph/drawio-mcp) under Apache-2.0. See the repo-root [`NOTICE`](NOTICE) file for the full attribution, including the upstream commit and the precise mapping of upstream files to local paths. Deliberate divergences (most notably: we keep the `.drawio` source after export instead of deleting it) are listed there too.
