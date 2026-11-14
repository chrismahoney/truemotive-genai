---
name: truemotive-vectorcraft
description: Create and edit vector artwork (paths, shapes, text, artboards, gradients, live effects) and procedural/generative vector art in VectorCraft (TrueMotive ArtCraft) via its headless CLI batch runner, MCP server, or live desktop control port; export SVG, PDF, AI, PNG, EPS and more. Use for logos, icons, scalable patterns, plotter or print art, or any request to work in VectorCraft.
---

# TrueMotive VectorCraft

Vector editor in the ArtCraft suite (966 engine commands, checked 2026-11-14). Output stays scalable until exported. If the result is photographic, pixel-filtered, or needs layers with blend and mask workflows, use PhotoCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/vectorcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/VectorCraft.app/Contents/MacOS/VectorCraft` |
| Protocol doc | `~/.claude/skills/vectorcraft/references/control-protocol.md` (114 KB: grep it, never read it whole) |
| Upstream MCP doc | `https://github.com/storytold/vectorcraft/blob/main/docs/mcp.md` |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

Readable: `.vectorcraft .svg .pdf .ai .eps .psd .png .jpg .tif .webp .dxf .afdesign` and more. Writable: `.vectorcraft .svg .svgz .pdf .ai .png .jpg .gif .webp .tif .bmp .eps .emf .wmf .dxf .tga .psd .txt`.

## Choose a session

| Need | Use |
|---|---|
| Generate or edit files unattended (best default) | `vectorcraft-cli run [--in FILE] --commands - --export OUT...` with JSON lines on stdin (verified) |
| One command | `vectorcraft-cli run --cmd ID --params '{json}' --export OUT` |
| Format conversion | `vectorcraft-cli convert IN OUT [--scale N\|--ppi N] [--artboard I\|--range "1-3,5"] [--outline-text] [--decimals N]` |
| Inspect a file | `vectorcraft-cli info FILE` (warnings, artboards, object counts, fonts) |
| Agent tool calls | `vectorcraft-cli mcp --headless`, or `mcp --connect 127.0.0.1:7979` for the live app |
| The user's open window | Desktop `VectorCraft --control 7979`, then raw TCP JSON lines or `mcp --connect` |

`run` takes `--commands FILE|-` as a JSON array of `{command, params}` or JSON Lines (up to 100000 steps). It prints one JSON result per step, and each `--export` writes the format its extension names. Later steps can refer to earlier results with `$N` (step index from 0; see `vectorcraft-cli run --help`).

With no mode flag, `mcp` tries port 7979 and silently falls back to headless. Pin the mode when the target matters. `--automation-read-root` and `--automation-write-root` confine file access and force headless. The control port is loopback-only with **no authentication**, so open it only while needed. Do not carry PhotoCraft's token flags over.

## Editing model (differs from PhotoCraft)

- Objects, not pixels. Creating a shape or path returns `{id}` and **makes it the selection**. `paint.*`, `stroke.set`, and `object.*` act on the selection, or on `ids: [...]` where supported. Check the result before chaining, and use `select.set {ids}` to be explicit.
- No layers to create for drawing. Z-order is creation order; change it with `object.arrange.*`. Group with `object.group`.
- Units: `file.new` defaults to **points (612x792)**. Pass `units: "Pixels"` for screen sizes. Coordinates are y-down from the first artboard's top-left.
- Colours: `#rrggbb`, `[r,g,b]`, `{c,m,y,k}`, `{gray}`, or `{l,a,b}`. **`#rrggbbaa` is refused**; set transparency through `object.setProps {opacity}`.
- Discover shapes with `vectorcraft-cli commands` (a JSON array of `{id, label, params, enabled, menu}`). Dump it once to the scratchpad and filter it; the full file is 600 KB. To search by text use `artcraft-find`; add `--readonly` to hide commands that may change state (a name-based guess here, for example `document.inspect`). Start from [references/command-quickref.md](references/command-quickref.md).

## Standard flow (verified headless)

1. `file.new {width, height, units:"Pixels", name}`
2. Background: `shape.rectangle {x,y,width,height}`, then `paint.setFill {color}`
3. Draw: `path.create {d:"M.. L.. Z"}` or `{anchors:[{x,y,in?,out?}], closed}`; `shape.polygon|star|ellipse|spiral|line|arc`
4. Style: `paint.setFill`, `paint.setStroke`, `stroke.set {weight,cap,join,dash}`, `object.setProps {opacity,blend}`
5. `document.inspect {depth:2}` to confirm `artboards`, `history`, and object counts
6. `--export out.svg --export out.png`, and `--export out.vectorcraft` when editability matters
7. Read the PNG to check the visual result

## Procedural and generative art

VectorCraft is the better target for geometric generators (tilings, Truchet, Voronoi, L-systems, spirographs, plotter art): there is no tight knot cap and the output stays editable.

- **Verified:** `path.create {d}` takes SVG path data. Many `M..Z` subpaths in one `d` become one compound path, so one `d` per colour gives one object. A 20000-subpath (60000-point) path ran in about 30 ms with no limit hit. Curves work through `C`/`Q` in `d` or `anchors` with `in`/`out` handles.
- **Verified:** fill, stroke (`stroke.set`), opacity (`object.setProps {opacity: 0..100}`), `shape.polygon {cx,cy,radius,sides}`, `object.rotate {angle}`, `select.all`, `object.group`, then SVG and PNG export.
- **Gotcha:** a new object **inherits the last-used fill and stroke**. Set paint explicitly after every create.
- Write the generator as a scratch script that prints JSON lines, then pipe it into `vectorcraft-cli run --commands -`.
- Building blocks (listed in the registry, not yet run here): `shape.star|spiral|arc|polarGrid`, `object.transformEach`, `object.pathfinder.unite|minusFront|intersect`, `object.clippingMask.make`, `object.path.offsetPath|simplify`, `effect.apply {effect:"distort.roughen"|"warp.arc"|"stylize.dropShadow"}`, `gradient.presets.apply`, `pattern.*`, `symbol.*`.
- Raster in, vector out: `file.open` a PNG, then `imageTrace.make {preset}` and `imageTrace.expand`.

## Save, export, verify

- Headless `run --export FILE` picks the format by extension and returns `{bytes, format, path, warnings}`. Read `warnings` and report real paths. Raster exports use `--scale` (px per pt) or `--ppi` (wins over `--scale`).
- Save an editable `.vectorcraft` next to any delivery export. `convert --outline-text` writes SVG text as paths, and `--decimals 1..7` sets SVG precision.
- Artboard scope: `--artboard` is zero-based, `--range` is one-based (`"1-3,5"`). PDF gets every artboard unless one is given; other formats get the first.
- Desktop saves and exports run in the background: `background: true` only means queued. Poll `ui.inspect` `background` jobs, then confirm the file exists. Query `document.formats` for options.
- Verify visually by reading the exported PNG; verify structure with `document.inspect` or `vectorcraft-cli info FILE`.
- After a timeout or lost reply, inspect `history` before replaying a mutation. Desktop request lines max 4 MiB, 16 connections.

## Cross-app hand-offs

- Vector to raster: export PNG here, then `doc.place` it in PhotoCraft (not yet run in this repo).
- Raster to vector: take a PhotoCraft PNG, `file.open` it here, then `imageTrace.make`.
- Never reuse ports, tokens, or flags between apps.

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/`.




