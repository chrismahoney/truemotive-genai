---
name: truemotive-photocraft
description: Create and edit raster images, layered documents, filters, and pixel-based procedural/generative art in PhotoCraft (TrueMotive ArtCraft) via its headless CLI, JSON-lines server, MCP bridge, or live desktop control port. Use for photo edits, layered PNG/PSD/.pcraft output, generated textures and patterns, or any request to work in PhotoCraft.
---

# TrueMotive PhotoCraft

Raster and layer editor in the ArtCraft suite (1009 engine commands, checked 2026-11-14). Output is pixels. If the result should stay scalable (logos, SVG, print vectors), use VectorCraft instead; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/PhotoCraft.app/Contents/MacOS/photocraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/PhotoCraft.app/Contents/MacOS/PhotoCraft` |
| Protocol doc | `~/.claude/skills/photocraft/references/control-protocol.md` (131 KB: grep it, never read it whole) |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

`artcraft-root/bin/` holds CLIs for other apps but **not** photocraft-cli. Do not look for it there.

## Choose a session

| Need | Use |
|---|---|
| One short edit sequence on a file | `photocraft-cli run --new '{json}' --cmd ID --params '{json}' --out FILE` (`--params` binds to the `--cmd` before it; `--out` refuses to replace the input unless `--in-place`) |
| Many edits or generated geometry | `photocraft-cli serve --automation-write-root DIR`, then pipe JSON lines on stdin: `batch`, `doc.inspect`, `doc.render`, `doc.save` |
| Agent tool calls | `photocraft-cli mcp` (headless) or `mcp --bridge 127.0.0.1:PORT --control-token-file F` (live app) |
| The user's open window | Desktop `photocraft --control PORT --control-token-file F`. A headless session never edits it. |
| A folder of images | `photocraft-cli batch` (action list) or `droplet` |

Run `ps aux | grep -i photocraft` first. Never trust a PID from notes; if no GUI runs, headless is correct for file output.

File access fails closed: set `--automation-write-root` to the output dir (add `--automation-read-root` for inputs). Request paths are relative to the root, forward-slash, and the parent dir must exist. Ambient-path commands (`file.save`, `file.open`) are refused; use `doc.save` and `doc.open`.

## Discover shapes, don't guess

`photocraft-cli commands` (or `engine.commands`) returns a bare array of `{id, label, params, enabled, needsDocument, disabledReason}`. `params` is a doc-string with types, ranges, and defaults. Dump it once to the scratchpad and filter it with `python3 -I`; never print all 1009 rows. Start from [references/command-quickref.md](references/command-quickref.md) for the major commands, and treat the registry as authoritative when they differ. To search by text across apps use `artcraft-find`; add `--readonly` to hide commands that may change state (a name-based guess for PhotoCraft, for example `document.inspect`, `session.inspect`).

## Standard flow

1. `file.new {width,height,name,background?}` (the new doc becomes active)
2. Solid background: `edit.fill {"contents":"color","color":"#rrggbb"}` on the Background layer
3. `layer.new.layer {name}` (the new layer becomes active; draw on it)
4. Draw: paths, `shape.create`, `paint.*`, `filter.render.*`, fill or adjustment layers
5. `doc.inspect`: confirm `layers` and `history`, and that `batch` reported `failed: 0`
6. `doc.save` to `.png` (flattens, with a warning) **and** `.pcraft` (keeps layers)
7. View the PNG (Read it) or `doc.render {maxSide, path}` (headless edge limit 2048)

Prefer editable results (adjustment layers, fill layers, masks, live shapes) over baked pixels when they suit the request.

## Procedural and generative art (verified: Penrose P3 tiling)

PhotoCraft has no tiler, L-system, or Voronoi generator. Compute the geometry in Python, then send it as paths:

- `path.set {path:{subpaths:[{closed:true,knots:[[x,y],...]}],fillRule:"nonzero"}}` sets the work path.
- `path.fill {color:"#rrggbb"}` fills it on the active pixel layer. One path per colour means one fill and no seams.
- Open lines: `{closed:false}` subpaths, then `path.stroke {tool:"pencil",size:1.5,color:"#rrggbb"}`.
- **Hard limit: 4096 knots/subpaths per path.** Chunk long paths (about 600 triangles per step). Also: at most 256 steps per `batch`, and a request line of at most 1 MiB.
- Coordinates are document pixels, y down, origin top-left. Cull geometry outside the canvas to save budget.
- Built-in generators take a `seed`: `filter.render.clouds`, `differenceClouds`, `fibers`, `tree`, `flame`, `lensFlare`, `lightingEffects`. Combine them with `layer.newAdjustmentLayer.gradientMap` or `posterize` to keep the result editable.
- Write the generator as a scratch script that emits a JSON-lines request file, then pipe it into `serve`.

## Jobs, failures, and uncertain outcomes

- `batch` is not a transaction. Use `stopOnError: true`, read every result, and inspect `history` before retrying anything.
- Long commands wait by default; with `wait:false` poll `jobs.list` before dependent edits.
- After a timeout or disconnect, inspect the document before replaying a mutation.
- If a write target already exists, look at it first. Delete only partial outputs you created yourself.

## Cross-app hand-offs

- Vector to raster: export PNG from VectorCraft, then `doc.place {path}` here (read root required; per the protocol doc, not yet run in this repo).
- Raster to vector: save the PNG here, then use VectorCraft `imageTrace.make`.
- Do not copy ports or auth flags between apps. PhotoCraft desktop control uses a token file; VectorCraft's port 7979 does not.

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad. Save test outputs to `artifacts-test/`.

Reference run: `artifacts-test/test_pc_penrose-tiles.png`, 512x512, 13-step batch, 0 failures.




