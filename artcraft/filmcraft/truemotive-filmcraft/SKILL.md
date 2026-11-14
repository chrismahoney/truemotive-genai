---
name: truemotive-filmcraft
description: Edit video - projects, sequences, clips, trimming, multicam, captions, audio mixing, graphics, effects - in FilmCraft (TrueMotive ArtCraft) through its headless CLI, MCP server, or live bridge, and export H.264, HEVC, ProRes, image or audio files, EDL and OTIO. Use for cutting and assembling footage, exporting video or frames, probing media, or any request to work in FilmCraft.
---

# TrueMotive FilmCraft

Non-linear video editor in the ArtCraft suite (718 commands, checked 2026-11-14): projects with bins and sequences, clips on timeline tracks, trims, multicam, captions, a mixer, graphics. For animated graphics and compositing use EffectCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/filmcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/FilmCraft.app/Contents/MacOS/FilmCraft` |
| Protocol doc | `~/.claude/skills/filmcraft/references/control-protocol.md` (grep it, never read it whole) |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| Render one frame | `filmcraft-cli [--demo \| --project P.fcproj] render --seconds S --out F.png [--scale 0.5]` (verified: 960x540 in 152 ms) |
| Export a clip or file | `filmcraft-cli ... export OUT [--preset NAME \| --format F] [--start S --end S \| --range entire\|inOut\|workArea] [--scale f] [--quality 0-100] [--no-audio] [--queue]` (verified: 1 s MP4) |
| A command sequence | `run <script.jsonl\|->` with `{"id": ID, "params": {...}}` per line (`#` comments ok); `--keep-going` continues after errors. One command: `exec ID key=value` or `exec ID '{json}'`. |
| Import and probe media | `import FILE...`, `probe MEDIA [--image-sequence]` (media info as JSON) |
| Inspect | `inspect [project\|sequence]` (verified: sequence JSON with tracks, clips, effects) |
| Agent tool calls | `filmcraft-cli mcp`, or `--bridge` to the running app |

Options: `--project P.fcproj \| --demo`, `--save` (write back to `--project`), `--save-as P.fcproj`, `--bridge 127.0.0.1:PORT` (the app started with `filmcraft --control PORT`), `--data-dir DIR`. Offline media renders as placeholder frames: `export` then lists `offlineMedia` and exits 1 unless `--allow-offline`.

## Discover shapes, don't guess

Use `artcraft-find QUERY --app filmcraft`, or `filmcraft-cli commands [filter] [--json]` and `filmcraft-cli describe ID`. Largest families: `graphics` 83, `file` 57, `clip` 57, `timeline` 57, `sequence` 51, `project` 40, `edit` 39, `multicam` 35, `markers` 33. Use `find.py --readonly` to hide commands that may change state.

## Editing model and standard flow

Timeline model: a project holds bins and sequences; a sequence has video and audio tracks of clips; times are seconds or frames (default sequence 1920x1080 at 23.976 fps, 48 kHz).

1. `file.newProject {name}`, or `--project P.fcproj`, or `--demo` for the built-in demo (a sunset scene)
2. `file.import {paths, bin?}` for media; or generate sources: `file.newColorMatte {color, seconds}`, `file.newBarsAndTone`, `file.newBlackVideo`
3. `file.newSequence {name, width, height, fps, video, audio}` and place clips with the `timeline.*` commands (`timeline.place`, `timeline.trim`, `timeline.razor`)
4. `inspect sequence` to confirm tracks and clips
5. `export OUT` or `file.exportMedia {path, preset?, format?}`; for interchange `file.exportEdl`, `file.exportOtio`, `file.exportFcpxml`
6. Check with `artcraft-qa` (it validates MP4 structure) and view a rendered frame

Verified: the demo project rendered a 960x540 frame (viewed) and exported a 1-second MP4 at quarter scale in 0.2 s; `artcraft-qa` confirmed the container. Timeline placement from imported footage and `--save-as` are not yet run.

## Procedural and generative notes

FilmCraft assembles media; it does not generate artwork. Produce stills or animation elsewhere (PhotoCraft or VectorCraft PNG sequences, EffectCraft renders), import them with `file.import` (`imageSequence: true` for numbered stills; not yet run), then cut and export.

## Save, export, verify

Native projects are `.fcproj` (`--save-as`, not yet run). Export formats: `h264 hevc prores dnxhr apv mjpeg mxf-op1a mxf-opatom png tiff bmp gif wav aiff aac mp3`. `export --list-presets [query]` lists presets. Always confirm the file exists and, for video, extract a frame with `render` to look at.

## Cross-app hand-offs

- EffectCraft PNG frames or renders into FilmCraft via `import` (not yet run). See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- FilmCraft `render` PNG frames out to PhotoCraft or LightCraft (PNG output verified).

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/filmcraft/`.

