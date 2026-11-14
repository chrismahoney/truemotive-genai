# AniCraft command quick reference

Source: `anicraft-cli commands` registry, 240 commands (165 mutating, per the native `mutates` flag), captured 2026-11-14. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app anicraft`.

Call shape: a JSON line `{"id": N, "cmd": ID, "params": {...}}` to `anicraft-cli serve`, or `anicraft-cli exec FILE ID 'JSON' [--save OUT]`. Selection and other state live only inside one `serve` session.

## Files and exports (file 24)

| Command | Params |
|---|---|
| `file.new` | `width?, height?, fps?` |
| `file.new_sample`, `file.open`, `file.save`, `file.save_as` | `file.save {path?, confirm?}` |
| `file.export_png` | `path, frame?, scale?` |
| `file.export_gif` | `path, from?, to?, scale?, loop?, confirm?` |
| `file.export_png_sequence` | `dir, from?, to?, scale?` |
| `file.export_svg`, `file.export_video`, `file.export_sprite_sheet`, `file.export_lottie`, `file.export_html` | other formats (video needs ffmpeg; sprite sheet also writes a frame-map JSON) |
| `file.import` | `path (.svg, .png, .jpg, or a .wav, .ogg, .mp3 sound), x?, y?` |

## Draw (draw 14)

| Command | Params |
|---|---|
| `draw.rect` | `x, y, w, h, radius?, fill?, stroke?, stroke_width?, ...` |
| `draw.ellipse` | `x, y, w, h, fill?, stroke?, stroke_width?, ...` |
| `draw.star` | `cx, cy, outer, inner?, points?, fill?, stroke?, ...` |
| `draw.line` | `x0, y0, x1, y1, stroke?, stroke_width?, cap?, join?, dash?` |
| `draw.path` | `d: SVG path data (stage space), fill?, stroke?, stroke_width?` |
| `draw.freehand` | `points: [[x, y], ...], mode? (smooth\|straighten\|ink), tolerance?, closed?, stroke?` |

## Timeline, layers, scenes

| Command | Params |
|---|---|
| `timeline.insert_keyframe`, `timeline.insert_blank_keyframe`, `timeline.clear_keyframe` | `layer? \| layers?, frame?` |
| `timeline.insert_frame`, `timeline.remove_frame` | `layer? \| layers?, frame?, count?` |
| `timeline.goto` | `frame` |
| `timeline.create_tween` | `layer?, frame?, easing?` classic tween (verified) |
| `timeline.create_motion_tween` | `layer?, frame?` (did not interpolate in testing) |
| `timeline.set_easing` | `easing, layer?, frame?` |
| `layer.new`, `layer.rename`, `layer.delete`, `layer.toggle_visible`, `layer.toggle_lock` | layers (`layer.new {name?}`) |
| `scene.new` | `name?` |

## Elements and symbols

| Command | Params |
|---|---|
| `edit.select_all`, `edit.deselect` | `{}` |
| `element.select` | `ids: [..], add?, layer?` |
| `element.pick` | `x, y, add?` |
| `element.translate` | `dx, dy, snap?, from?` moves the selection |
| `element.set_transform` | `x?, y?, sx?, sy?, rotation? (degrees)` |
| `element.set_fill` | `color: "#rrggbb" \| null` |
| `modify.convert_to_symbol` | `name?, kind? (graphic\|movie_clip\|button), folder?` returns `{symbol, instance}` |
| `motion.set_key` | `property (x, y, scale_x, scale_y, rotation, alpha, tint...), ...` |
| `bone.add` | `from, to (instance ids), head?` |
| `library.place`, `library.items` | symbol library |

## Other families

`raw.*` (11, explicit points), `edit.*` (10), `library.*` (10), `frames.*` (9), `modify.*` (8), `align.*` (8), `motion.*` (13), `bone.*` (7).

CLI subcommands `new`, `info`, `render`, `render-seq`, `gif`, `run`, `exec`, `serve`, `mcp` and `bench` are not engine commands.
