---
name: truemotive-designcraft
description: Lay out pages, frames, text stories, styles, tables, and swatches and export PDF, PNG, IDML, EPUB or HTML in DesignCraft (TrueMotive ArtCraft page-layout app) through its headless CLI, MCP server, or live control port. Use for brochures, posters, documents, data-merge layouts, print-ready PDFs, or any request to work in DesignCraft.
---

# TrueMotive DesignCraft

Page-layout app in the ArtCraft suite (555 commands, checked 2026-11-14), in the InDesign family: pages and spreads, frames, threaded text stories, paragraph and character styles, tables, swatches, books. Output is a layout that exports to PDF, PNG, IDML, EPUB or HTML. For free-form drawing use VectorCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/DesignCraft.app/Contents/MacOS/designcraft-cli` (inside the bundle, not `bin/`) |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/DesignCraft.app/Contents/MacOS/DesignCraft` |
| Protocol doc | `~/.claude/skills/designcraft/references/control-protocol.md` (grep it, never read it whole) |
| Upstream guides | `https://github.com/storytold/designcraft/blob/main/docs/mcp.md`, `.../agents.md` (script syntax, result references, data merge) |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| Unattended build and export | `designcraft-cli run [--in FILE \| --sample] --cmd ID[=JSON]... --export OUT` (verified). `--export` picks the format by extension (`.png`, `.pdf`); `--page N`, `--scale S`, `--pdf-options JSON` apply to the exports after them; `--all-pages DIR` writes every page. |
| A longer script | `designcraft-cli script [FILE\|-] [--in FILE \| --sample] [--save OUT] [--export OUT] [--keep-going]` |
| Agent tool calls | `designcraft-cli mcp [--sample] [--automation-read-root DIR]... [--automation-write-root DIR]...` (roots confine every file read and write and conflict with `--connect`) |
| The user's open window | `designcraft --control PORT`, then `designcraft-cli app [--port PORT] COMMAND [JSON]` or `mcp --connect PORT` (loopback, no authentication) |
| Print checks | `designcraft-cli validate-pdf FILE.pdf [--standard x4\|x1a]` |

`run` prints each command's bare result, then one line per export. Details such as `{"id": 8}` come back for created items, and `{"id": 9, "story": 10}` for text frames.

## Discover shapes, don't guess

Use `artcraft-find QUERY --app designcraft`, or `designcraft-cli describe COMMAND` and `designcraft-cli commands FILTER`. Largest families: `object` 60, `type` 43, `file` 41, `table` 41, `layout` 32, `style` 28. Use `find.py --readonly` to hide commands that may change state.

## Editing model and standard flow

Frames, not free objects. Coordinates are **points**, y down, in spread space (on facing spreads the right page starts at x = page width). Text lives in stories linked to frames; use the returned `id` and `story` values for later edits.

1. `file.new {width, height, units, preset?, pages?, margins?}` (or `--in FILE`)
2. `swatch.create {name, color}` for any colour you need (`[Black]`, `[Paper]`, `[None]` exist)
3. `frame.create {rect:[x0,y0,x1,y1], shape:"rectangle"\|"ellipse"\|"polygon", content:"graphic"\|"text", text?}`
4. Style it: `object.fill {swatch}`, `object.stroke {swatch, weight}`, `object.opacity {opacity}`
5. `document.inspect` to confirm items, stories, overset, swatches
6. `--export out.png --export out.pdf`, then check and view with `artcraft-qa`

**Gotchas (verified):** a new frame has **no fill and no stroke**, so it is invisible until styled (the QA checker flagged the first smoke render as 99.6% one colour for this reason). New frames do **not** inherit the previous object's fill, unlike VectorCraft: a second frame created after a filled one came back `[None]`. Style commands such as `object.fill` act on `ids` or the current selection, and a newly created frame becomes the selection (verified: `object.fill` without `ids` styled the frame just created).

## Procedural and generative notes

DesignCraft can draw with `path.create {anchors:[{p:[x,y], in?, out?}], closed?}`, but it is built for layout, not for generating thousands of shapes. There is no tight point cap: one path with 60,000 anchors was accepted (tested through `script -`, which takes `ID JSON` lines or JSON lines on stdin). Use the generators in VectorCraft or PhotoCraft and place the result, or drive layout programmatically (data merge, tables, repeated frames). The `artcraft-gen-recipes` emitters do not target DesignCraft yet.

## Save, export, verify

Native: `file.save`, `file.saveAs`. Exports: `file.exportPdf {path, pages, flatten...}`, `file.exportIdml`, `file.exportEpub`, `file.exportHtml`, `file.exportPptx`; PNG through `run --export`. Verified: a 400x400 document exported to a 400x400 PNG and a one-page PDF; `artcraft-qa` passed both.

## Cross-app hand-offs

- VectorCraft SVG, PDF, or PNG placed into a layout with `file.place` (not yet run). See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- DesignCraft PDF into other apps through the shared task directory (not yet run).

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/designcraft/`.

