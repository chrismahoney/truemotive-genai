---
name: truemotive-lightcraft
description: Organize, rate, develop, crop, render, merge and export whole photos in LightCraft (TrueMotive ArtCraft photo library and raw developer) through its headless CLI (render, run, snapshot, merge), MCP server, or live control port. Use for photo develop and export, batch tonal finishing of a rendered image, HDR or panorama merges, or any request to work in LightCraft.
---

# TrueMotive LightCraft

Photo library and raw developer in the ArtCraft suite (389 commands, checked 2026-11-14). It develops and exports whole photos non-destructively: sliders, presets, crop, masks, keywords, albums. For pixel and layer editing use PhotoCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing. LightCraft is PhotoCraft's raster sibling: a PhotoCraft or VectorCraft PNG can be given a tonal finish here.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/lightcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/LightCraft.app/Contents/MacOS/LightCraft` |
| Protocol doc | `~/.claude/skills/lightcraft/references/control-protocol.md` (grep: `Methods`, `Headless rendering`, `When the library can't be saved`) |
| Upstream MCP doc | `https://github.com/storytold/lightcraft/blob/main/docs/mcp.md` |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| One file in, one file out | `lightcraft-cli render IN -o OUT [--set CONTROL=VALUE]... [--preset ID] [--size N] [--quality Q] [--opt KEY=VALUE]`. The extension picks the format: `.jpg .png .tif .webp .avif .jxl .psd .dng`. |
| A sequence of commands | `lightcraft-cli run [--demo \| --library DIR] [--import PATH] COMMAND [key=value \| '{json}'] ...` prints one JSON line per command and exits non-zero if one fails. `--script FILE\|-` takes JSON lines; `--keep-going` continues after errors. |
| Edits that persist | `--library /absolute/dir` (opens or creates it). One program holds a library at a time; if the app has it, connect to the app, never remove the lock. Without `--library`, edits do not persist. |
| The user's open app | `lightcraft --control 7980`, then `run --connect` or `mcp --connect` (loopback, no authentication) |
| Agent tools | `lightcraft-cli mcp [FILES] [--library DIR] [--compact]` |
| UI screenshots | `lightcraft-cli snapshot --script tour.jsonl -o shot.png` |
| Photo Merge | `lightcraft-cli merge hdr\|panorama\|hdr-panorama\|hdr-batch FILES` writes a DNG next to the first file |

Verified: `render` turned a 1024x1024 PNG into an 800x800 JPEG with `--set light.exposure=0.6`; `run --demo develop.set control=light.exposure value=0.7 develop.auto app.export path=OUT longEdge=800` exported a 533x800 JPEG.

## Discover shapes, don't guess

Search with `artcraft-find QUERY --app lightcraft`. Largest families: `library` 48, `photo` 44, `mask` 31, `develop` 29, `keyword` 23, `faces` 21, `print` 20, `denoise` 16, `album` 15. Slider control ids come from `develop.controls`; `light.exposure` is verified. Use `find.py --readonly` to hide commands that may change state.

## Standard flow

1. Import (`--import PATH`, or `library.import {paths, mode}`) or open a library. `mode` is `add` (reference in place), `copy`, or `move`; **move deletes the originals** after cataloguing, and undo does not bring them back.
2. Use real photo ids from the library, and select explicitly before acting on several photos.
3. Develop: `develop.set {control, value}` or `{values:{controlId: number}}`, `develop.auto`, `preset.apply {id, amount}`. Read current values first and keep unrelated edits.
4. Crop with `crop.set {rect:[x0,y0,x1,y1] normalized, angle}`.
5. Export: `app.export {path, format, longEdge}`. MCP export defaults to a 3000 px long edge; `longEdge: 0` means cropped native size.
6. Verify with `artcraft-qa` (it checks JPEG structure and size) and view the image.

## Procedural and generative notes

LightCraft develops photos; it does not generate geometry. Pair it with the generators: render a PhotoCraft or VectorCraft PNG, then give it a tonal finish with `render` (verified on the Voronoi benchmark PNG: brighter, 800 px, clean edges).

## Save, export, verify

A persistent library journals each edit. The error `saved in memory but not written to disk` means the edit happened and is queued: inspect `library.info` for `unsavedOps` and do not repeat it. Desktop exports with `background: true` only queue work; poll the app's export state, then confirm the file exists. Exports can write XMP sidecars (`sidecars` in the result).

## Cross-app hand-offs

- PhotoCraft or VectorCraft PNG into LightCraft: `render IN -o OUT` (verified). See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- LightCraft output into PhotoCraft: export TIFF or PNG, then `doc.open` it (not yet run).

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/lightcraft/`.

