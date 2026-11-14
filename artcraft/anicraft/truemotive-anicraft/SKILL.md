---
name: truemotive-anicraft
description: Draw and animate 2D scenes - shapes, layers, keyframes, tweens, motion paths, symbols, bones, scenes - in AniCraft (TrueMotive ArtCraft, a frame-by-frame animator) through its headless CLI, JSON-lines server or MCP server, and export PNG, GIF, SVG, video, sprite sheets, PNG sequences, Lottie or HTML. Use for animated GIFs, sprite sheets, motion graphics drawn by hand, or any request to work in AniCraft.
---

# TrueMotive AniCraft

Frame-by-frame animator in the ArtCraft suite (240 commands, version 0.2.1, checked 2026-11-14), in the Flash family: a movie has scenes, layers, a timeline of frames and keyframes, tweens, motion paths, symbols and bones. It was added 2026-11-11 and has no upstream skill or protocol doc, so this skill comes from `--help`, the registry and tests. For compositing footage use EffectCraft; for video editing FilmCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/AniCraft.app/Contents/MacOS/anicraft-cli` (inside the bundle, not `bin/`) |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/AniCraft.app/Contents/MacOS/AniCraft` |
| Protocol doc | none installed (the CLI refers to `docs/mcp.md`, `docs/plugins.md`, `docs/performance.md` upstream) |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| Build an animation in one session (best default) | `anicraft-cli serve [FILE \| --sample]` with JSON lines on stdin: `{"id":1,"cmd":"draw.rect","params":{...}}`. It prints a ready line, then one reply per request with `ok`, `result` and `frame`. Verified. |
| One command on a file | `anicraft-cli exec FILE\|--sample COMMAND '[json]' [--save OUT]` |
| A script of commands | `anicraft-cli run FILE\|--sample SCRIPT.json [--save OUT]` (not yet run) |
| New empty file | `anicraft-cli new --out F.anicraft [--width W --height H --fps F]` |
| Render | `render FILE --out F.png [--frame N] [--scale S]`, `render-seq FILE --out-dir DIR [--from A --to B]`, `gif FILE --out F.gif [--from --to --scale --overwrite yes]` (not yet run; exports through `serve` were verified) |
| Inspect | `anicraft-cli info FILE\|--sample` |
| Agent tool calls | `anicraft-cli mcp [FILE\|--sample]` (not yet run) |

`--plugins DIR` loads WebAssembly plug-ins; without it headless runs use none, so they are repeatable. **Each `exec` or `run` is its own session, but a `serve` session keeps state**: a selection made by one `exec` is gone in the next (`element.translate` then fails with "nothing is selected"), while the same two commands in one `serve` session work. Use `serve` for anything that selects.

## Discover shapes, don't guess

Use `artcraft-find QUERY --app anicraft`. Families: `file` 24, `timeline` 21, `layer` 16, `element` 15, `draw` 14, `motion` 13, `raw` 11, `edit` 10, `library` 10, `scene` 9, `frames` 9, `modify` 8, `align` 8, `bone` 7. This is the only registry with a **native `mutates` flag** (165 of 240 commands mutate); `find.py --readonly` uses it here and a name-based guess elsewhere.

## Editing model and standard flow

Elements live on layers at keyframes; most edits act on the **selection** at the playhead. Frame numbers in `serve` replies start at 0; the CLI help says command-line frames are 1-based, so confirm by exporting a frame.

1. `file.new {width, height, fps}` (or `--sample`, or a file)
2. `draw.rect {x, y, w, h, fill?, stroke?, stroke_width?}`, `draw.ellipse`, `draw.star`, `draw.line`, `draw.path`, `draw.freehand`; the new shape lands on the current layer
3. `timeline.insert_keyframe {frame}`, then `timeline.goto {frame}`, `edit.select_all` (or `element.select {ids}` / `element.pick {x, y}`), and edit: `element.translate {dx, dy}`, `element.set_transform {x?, y?, sx?, sy?, rotation?}`, `element.set_fill {color}`
4. Animate between keyframes: `timeline.create_tween {layer?, frame?, easing?}` (classic tween)
5. Export and check with `artcraft-qa` (PNG, GIF and the JSON `.anicraft` are recognised), then view a mid-animation frame

**Verified:** a 60 px red square drawn at frame 0, a keyframe at 12 moved 200 px right, and a classic linear tween: frame 3 had the square at x≈71 to 128 and frame 6 at x≈121 to 178 (a linear slide). **Gotcha: use classic tweens.** `timeline.create_motion_tween` did not work in three attempts, so its correct usage is still unknown: on a raw drawn rect it returned `converted: false, motion: 0` and the in-between frames stayed at the start; after `modify.convert_to_symbol` (verified: returns `{symbol, instance}`) with the keyframe edit made first, the same; and created first on a one-frame span it failed with "frame 2 is empty on this layer". `timeline.create_tween` (classic) is the verified route.

## Procedural and generative notes

Shapes are drawn with commands, so a generator can emit `draw.*` calls frame by frame (a loop over `timeline.insert_keyframe`, `edit.select_all`, `element.set_transform`). `raw.*` and `motion.add_point` take explicit points. There is no tight point cap: one `draw.path` with 60,000 points was accepted in 0.14 s. An emitter for `artcraft-gen-recipes` does not exist yet (not yet run at scale).

## Save, export, verify

Native `.anicraft` (JSON text, 4.7 KB for the smoke test) via `file.save {path}`. Exports through `serve`, all verified in the smoke test unless noted: `file.export_gif {path, from, to, scale, loop}` (12 frames, 9.4 KB), `file.export_png {path, frame, scale}`; also `file.export_svg`, `file.export_png_sequence {dir}`, `file.export_video {path (.mp4 or .webm)}` (needs ffmpeg), `file.export_sprite_sheet`, `file.export_lottie`, `file.export_html` (not yet run). Some commands take `confirm` for overwrites or prompts.

## Cross-app hand-offs

- AniCraft PNG frames or sequences into FilmCraft (`file.import`, `imageSequence`) or LightCraft (not yet run). See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- Images into AniCraft: `file.import` (not yet run).

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/anicraft/`.
