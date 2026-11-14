---
name: truemotive-cadcraft
description: Create and edit 2D CAD drawings - lines, circles, arcs, polylines, text, dimensions, hatches, layers, blocks, layouts - in CADCraft (TrueMotive ArtCraft) through its headless CLI, MCP server, or live control port, and export DXF, DWG, SVG, PNG or PDF. Use for technical drawings, floor plans, schematics, DXF/DWG conversion, or any request to work in CADCraft.
---

# TrueMotive CADCraft

2D CAD in the ArtCraft suite (457 commands, checked 2026-11-14), AutoCAD-style: entities on layers, command names like `line`, `circle`, `pline`, `layer.new`. Native formats DXF and DWG. For illustration use VectorCraft; for page layout DesignCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/cadcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/CADCraft.app/Contents/MacOS/CADCraft` |
| Protocol doc | `~/.claude/skills/cadcraft/references/control-protocol.md` (grep it, never read it whole) |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| Build and export unattended | `cadcraft-cli run [FILE]... [--metric \| --sample] --cmd 'ID {json}'... [--save OUT] [--export OUT] [--window=x0,y0,x1,y1]` (verified) |
| AutoCAD-style scripts | `--script TEXT` (`\n` separates lines) or `--script-file F.scr`; steps run in the order given (script syntax not yet run) |
| Convert | `cadcraft-cli convert IN OUT` (dxf, dwg, dwt, svg, png, pdf by extension) |
| Inspect | `cadcraft-cli info FILE` |
| Agent tool calls | `cadcraft-cli mcp` (headless) or a bridge to the running app |

Note the `--cmd` form: the command id, then a space, then the JSON (`--cmd 'circle {"center":[50,30],"radius":15}'`). Each `--cmd` prints its JSON result. A new drawing is **imperial** unless you pass `--metric`. `--window` takes drawing units; a negative `x0` needs the `=` form: `--window=-10,-10,110,90`. `--save` and `--export` pick the format by extension.

## Discover shapes, don't guess

Use `artcraft-find QUERY --app cadcraft`. Largest families: `table` 12, `arc` 11, `zoom` 10, `layout` 8, `dimstyle` 8, `vports` 7, `blocks` 7, `grip` 7, `circle` 6, `layer` 5. Many ids have no dot (`line`, `circle`, `text`, `export`). Use `find.py --readonly` to hide commands that may change state.

## Editing model and standard flow

Entities live on **layers**; a new entity lands on the **current layer** and takes its colour (`ByLayer`). There is no "last used fill and stroke" to inherit: change layer instead. Units are drawing units (imperial by default).

1. `--metric` (or `new {metric, template}`) for a new drawing, or open a DXF/DWG
2. `layer.new {name, color?, linetype?, lineweight? (mm), current?: true}`
3. Draw: `line {points:[[x,y],...], closed?}`, `circle {center, radius}`, `text {at, text, height?}`, `arc`, `pline`, `hatch`, `dim`
4. `drawing.inspect {entities:true, limit}` to confirm counts, current layer, and each entity's layer
5. `--export OUT.png` (use `--window` to frame it), `--save OUT.dxf`, then check and view with `artcraft-qa`

**Gotchas (verified):** `line` with `closed: true` produced **four separate Line entities**, not one polyline; use `pline` for a single closed outline (verified: one Polyline entity). **New entities are not selected**: `erase {}` right after `line` erased 0, so pass `handles` (draw commands return them, for example `{"handles":["100"]}`). There is no tight vertex cap: one 40,000-vertex `pline` was accepted (60,000 only hit the OS argument-length limit; `--script-file` avoids that). Exported PNG is 2400x1600 on a dark background with hairline strokes, so `artcraft-qa` warns "dominant 99%+": that is expected for CAD line art, so view the image instead of treating it as blank.

## Procedural and generative notes

CAD suits exact, repeatable geometry (grids, hatching, parametric plans). Use `artcraft-gen-recipes` output only as line work: a `shapes.json` emitter for CADCraft does not exist yet. A script that emits `line` and `circle` commands is straightforward (not yet run at scale).

## Save, export, verify

Verified: layers, a rectangle, a circle and text saved as `.dxf` (17 KB) and exported as PNG; the PNG was viewed (red rectangle on Walls, blue circle and text on Notes). `.dwg`, `.svg` and `.pdf` outputs are listed by `--help` and not yet run.

## Cross-app hand-offs

- CADCraft SVG into VectorCraft for styling: not yet run. See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- DXF is also readable by VectorCraft (`file.open`), not yet run.

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/cadcraft/`.

