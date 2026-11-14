# EffectCraft command quick reference

Source: `effectcraft-cli commands` registry, 761 commands, captured 2026-11-14. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app effectcraft`, or `effectcraft-cli commands --filter TEXT`.

Call shape: a JSON line `{"command": ID, "params": {...}}` through `run --commands -`, or `run ID JSON`.

## Project and files (66)

| Command | Params |
|---|---|
| `file.newProject`, `file.openDemoProject` | `{}` |
| `file.open`, `file.save`, `file.saveAs` | `{path}`, `{path?}`, `{path}` (the project is JSON text, `.ecproj`) |
| `file.import` | `paths: [files or folders], sequence?: bool` |

## Compositions (33)

| Command | Params |
|---|---|
| `comp.new` | `name?, width?, height?, frameRate?, duration? (s), startTime?, background? ([r,g,b] or #hex), pixelAspect?, shutterAngle?, motionBlurSamples?` |
| `comp.settings` | `comp?, name?, width?, height?, anchor?, frameRate?, duration?, background?` |
| `comp.open` | `comp: id or name` |

## Layers (124)

| Command | Params |
|---|---|
| `layer.newSolid` | `name?, color? (#hex or [r,g,b]), width?, height?, pixelAspect?` |
| `layer.newShape` | `kind? (rect\|rounded\|ellipse\|star\|polygon\|none), name?, size?, fill?, fillType?, fillOpacity?, stroke?, strokeWidth?, position?` |
| `layer.newText` | `text?, name?, position? [x,y], box? [x,y,w,h]` |
| `layer.newNull`, `layer.newAdjustment` | `name?` |
| `layer.settings` | `layer?, name?, color?, width?, height?, pixelAspect?` |

## Properties, keyframes, effects, masks

| Command | Params |
|---|---|
| `prop.set` | `layer?, path \| prop, value, time? (layer seconds), timeBase? (layer\|comp), merge?` |
| `keys.set` | `layer?, path \| prop, time, newTime?, value?, merge?` |
| `keys.easyEase`, `keys.easyEaseIn`, `keys.easyEaseOut`, `keys.delete`, `keys.move` | keyframe edits |
| `effect.apply` | `effect: id or name (for example Gaussian Blur), layers?` |
| `effect.remove`, `effect.toggle`, `effect.reorder` | manage effects |
| `mask.new` | `layer?, vertices: [[x,y]...], inTangents?, outTangents?, closed?, mode?` |
| `mask.addVertex`, `mask.setVertex`, `mask.setClosed`, `mask.setRoundness` | mask edits |

## Render queue

| Command | Params |
|---|---|
| `renderQueue.add` | `comp?: id or name, template?, format? (h264\|hevc\|av1\|prores\|webm\|png\|jpeg\|tiff\|exr\|tga\|gif\|wav\|aiff), output?: path` |
| `renderQueue.remove`, `renderQueue.setOutput`, `renderQueue.setRenderSettings` | queue management |

## Other families (use `artcraft-find` for params)

`view.*` (78), `edit.*` (27), `effect.*` (25), `track.*` (22), `essential.*` (22), `camera.*` (20), `renderQueue.*` (20), `prop.*` (18), `mask.*` (18), `time.*` (17), `roto.*` (14), `text.*` (14).

CLI subcommands `run`, `exec`, `props`, `get`, `set`, `render-frame`, `render`, `script`, `info`, `bench` and `mcp` are not engine commands.
