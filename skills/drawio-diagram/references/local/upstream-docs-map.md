# Upstream docs map

Official draw.io documentation and examples can be cloned locally for deep lookup. Run once from the skill root:

```bash
bash scripts/fetch_upstream_docs.sh
```

This populates `references/upstream/` (gitignored, ~30MB). Add `--with-mxgraph` for the archived deep model docs, or `--with-app-templates` for the built-in app templates (CC BY 4.0, attribution required).

If the clones are absent and network access is unavailable, fall back to the vendored digests under `references/fetched/` and the local overlay files; do not block a diagram request on this fetch.

## Where to look

| Question | Location |
| --- | --- |
| Exact style key/value semantics | `references/upstream/drawio-mcp/shared/style-reference.md` |
| Canonical XML generation rules | `references/upstream/drawio-mcp/shared/xml-reference.md` |
| Structural schema validation | `references/upstream/drawio-mcp/shared/mxfile.xsd` |
| Shape name lookup (10k+ shapes) | `references/upstream/drawio-mcp/shape-search/search-index.json` |
| Real, well-routed official diagrams | `references/upstream/drawio-diagrams/blog/` and `examples/` |
| Template gallery by domain (19 categories) | `references/upstream/drawio-diagrams/templates/` |
| Deep model docs (mxCell, mxGeometry, edge routing internals) | `references/upstream/mxgraph/docs/manual.html` (optional clone) |
| Every STYLE_*/EDGESTYLE_* constant | `references/upstream/mxgraph/docs/js-api/files/util/mxConstants-js.html` |

Note: many files under `drawio-diagrams/templates/` store the model compressed (base64 deflate inside `<diagram>`); prefer `blog/` and `examples/`, which are mostly plain XML you can read directly.

## What the official examples actually do

Measured across 133 plain-XML official diagrams (2,956 edges) in `drawio-diagrams`:

- ~38% of edges use `edgeStyle=orthogonalEdgeStyle`.
- ~22-27% pin at least one terminal with `exitX/exitY` or `entryX/entryY`.
- ~29% carry explicit waypoint arrays (`<Array as="points">`).

Official diagrams do not rely on fully automatic routing. Where a route matters, they pin the connection side and add waypoints. Match that practice.

## Online references (when clones are absent)

- Docs hub: https://www.drawio.com/docs/
- AI diagram generation rules: https://www.drawio.com/docs/reference/diagram-generation/
- Style reference for generation: https://www.drawio.com/docs/reference/diagram-generation/style-reference/
- Connector how-tos (waypoints, fixed vs floating, labels): https://www.drawio.com/docs/manual/connectors/
- Fixed vs floating connectors: https://www.drawio.com/docs/manual/connectors/connector-fixed-vs-floating/
- Custom connection points on a shape: https://www.drawio.com/docs/manual/shapes/shape-connection-points-customise/
- mxGraph user manual: https://jgraph.github.io/mxgraph/docs/manual.html
- mxConstants (all STYLE_*/EDGESTYLE_* keys): https://jgraph.github.io/mxgraph/docs/js-api/files/util/mxConstants-js.html

## Licensing

- `jgraph/drawio-mcp`, `jgraph/drawio-diagrams`, `jgraph/mxgraph`: Apache-2.0.
- `jgraph/drawio` `src/main/webapp/templates/`: CC BY 4.0 (its own LICENSE file inside that directory). Attribute if any template content is reused.
