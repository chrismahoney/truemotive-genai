---
name: truemotive-effectcraft
description: Build and render motion-graphics compositions - layers, shapes, text, keyframes, masks, effects, expressions, cameras - in EffectCraft (TrueMotive ArtCraft, an After Effects-style compositor) through its headless CLI, JavaScript scripting, MCP server, or live bridge, and render frames or video. Use for animated graphics, titles, compositing, effect stacks, or any request to work in EffectCraft.
---

# TrueMotive EffectCraft

Compositing and motion-graphics app in the ArtCraft suite (761 commands and 308 effects, version 0.23.1, checked 2026-11-14). A project holds compositions; compositions hold layers with animatable properties. Renders to PNG frames or video. For stills use PhotoCraft or VectorCraft; for editing footage into a film use FilmCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/effectcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/EffectCraft.app/Contents/MacOS/EffectCraft` |
| Protocol doc | `~/.claude/skills/effectcraft/references/control-protocol.md` (grep it, never read it whole) |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| Build a project | `effectcraft-cli run --commands -` with JSON lines `{"command": ID, "params": {...}}` (or a JSON array; up to 100000 steps). Also `run ID JSON ID JSON ...` and `run --args-file F`. |
| Render one frame | `effectcraft-cli render-frame PROJECT.ecproj --comp NAME --time S --out F.png` (verified: 640x360 in 32 ms) |
| Render a clip | `effectcraft-cli render --comp C --out FILE [--format h264\|hevc\|av1\|prores\|webm\|png\|gif\|...] [--start S --end S]` (not yet run) |
| Read or set a property | `props COMP LAYER [--flat]`, `get COMP LAYER PATH`, `set COMP LAYER PATH VALUE [--expression E]` (not yet run) |
| Scripting | `script FILE.jsx \| --eval CODE` with an After Effects-style object model (not yet run) |
| Inspect | `effectcraft-cli info PROJECT.ecproj` |
| Agent tool calls | `effectcraft-cli mcp`; `--bridge PORT` attaches to a running app |

Global options: `--project F.ecproj \| --demo \| --empty`, `--save \| --save-as F`, `--json`, `--gpu`. `COMP` is an id or name (`-` is the active comp); `LAYER` is an id, `#n`, or a name. **Each invocation is its own session**: state persists only if you `file.saveAs` and pass the project path to the next call.

## Discover shapes, don't guess

Use `artcraft-find QUERY --app effectcraft`, or `effectcraft-cli commands --filter TEXT [--enabled]`. Largest families: `layer` 124, `view` 78, `file` 66, `keys` 37, `comp` 33, `edit` 27, `effect` 25, `track` 22, `camera` 20, `renderQueue` 20, `mask` 18. Use `find.py --readonly` to hide commands that may change state.

## Editing model and standard flow

Timeline model: a project, compositions with a frame rate and duration in seconds, layers with timing, and properties that take keyframes or expressions. Sizes are pixels; times are seconds.

1. `file.newProject {}` (or `--project F.ecproj`, `--demo`)
2. `comp.new {name, width, height, frameRate, duration, background}` (the new comp becomes active)
3. Add layers: `layer.newSolid {name, color}`, `layer.newShape {kind: rect\|rounded\|ellipse\|star\|polygon, size, fill, stroke, position}`, `layer.newText`, `layer.newNull`, `layer.newAdjustment`
4. Animate and style: keyframes (`keys.*`), effects (`effect.*`), masks (`mask.*`), expressions (`set ... --expression`)
5. `file.saveAs {path}` to persist, then `effectcraft-cli info PROJECT` to confirm
6. `render-frame PROJECT --comp NAME --time S --out F.png`, then check and view with `artcraft-qa`

Verified: a project with a teal solid and a gold ellipse shape saved as `.ecproj` (JSON text) and rendered as a 640x360 PNG at 0.5 s; the PNG was viewed.

## Procedural and generative notes

EffectCraft generates through animation: shape layers, expressions, and JavaScript (`script`). There is no tight point cap: a single `mask.new` with 40,000 vertices was accepted. Static geometry generators are still better placed in VectorCraft or PhotoCraft; render their PNG and import it as footage (`file.import`, not yet run). The `artcraft-gen-recipes` emitters do not target EffectCraft yet.

## Save, export, verify

Native `.ecproj` is JSON; `artcraft-qa` checks that it parses. Frames: `render-frame` (PNG). Video: `render` with `--format`, `--resolution`, `--quality`, `--fps` (not yet run); a relative `--out` is relative to the working directory. Always check an exported file exists and view a frame.

## Cross-app hand-offs

- PNG frames out to PhotoCraft or LightCraft for finishing (PNG output verified). See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- VectorCraft or PhotoCraft PNG into a composition with `file.import` (not yet run).

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/effectcraft/`.

