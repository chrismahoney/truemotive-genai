# LightCraft command quick reference

Source: `lightcraft-cli commands` registry, 389 commands, captured 2026-11-14. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app lightcraft`.

Call shape: `lightcraft-cli run COMMAND key=value ...` (values are JSON when they parse), or `COMMAND '{json}'`, or a JSON line `{"command": ID, "params": {...}}` through `--script`.

## Develop (29)

| Command | Params |
|---|---|
| `develop.set` | `control?: controlId, value?: number, values?: {controlId: number}, ids?: [photo]` (the crop-angle control id also works, like `crop.straighten`) |
| `develop.get` | read current settings |
| `develop.controls` | list control ids, ranges and defaults (for example `light.exposure`) |
| `develop.auto` | `{}`; returns the settings it chose (exposure, contrast, highlights...) |
| `develop.reset`, `develop.resetControl`, `develop.resetSection` | undo develop edits |
| `develop.copy`, `develop.paste`, `develop.sync`, `develop.autoSync` | move settings between photos |
| `develop.wb`, `develop.treatment`, `develop.matchExposure` | white balance, colour or B&W, exposure match |

## Crop

| Command | Params |
|---|---|
| `crop.set` | `rect?: [x0,y0,x1,y1] normalized in the straightened frame, angle?: degrees` |
| `crop.reset`, `crop.straighten`, `crop.autoStraighten`, `crop.aspect` | adjust the crop |

## Presets and history

| Command | Params |
|---|---|
| `preset.apply` | `id: presetId, amount?: 0..200 (percent), ids?` |
| `preset.create`, `preset.update`, `preset.rename`, `preset.delete`, `preset.favorite` | manage presets |
| `preset.import`, `preset.export` | `.lcpreset` and XMP presets |
| `history.list`, `history.restore`, `history.clear` | develop history |

## Library, photos, export

| Command | Params |
|---|---|
| `library.import` | `paths: [file or folder, recursive], mode?: add \| copy \| move` (move removes originals) |
| `library.info` | library state, including `unsavedOps` and `unsavedError` |
| `library.filter`, `library.clearFilter`, `library.folders`, `library.findSimilar` | browse and query |
| `library.buildPreviews`, `library.next`, `library.previous` | previews and navigation |
| `photo.inspect` | one photo's details |
| `photo.flag`, `photo.label`, `photo.clearLabel`, `photo.increaseRating`, `photo.decreaseRating` | cull and rate |
| `photo.duplicate`, `photo.delete`, `photo.convertToDng`, `photo.flipHorizontal` | file-level edits |
| `app.export` | `path?: output file (.jpg .png .tif .webp .avif .jxl .psd .dng) \| dir?, ids?, preset?, format? (jpeg\|png\|tiff\|webp\|avif\|jxl\|psd\|dng\|original), longEdge?\|shortEdge?\|width?\|height?\|megapixels?...` |
| `export.presets`, `export.savePreset`, `export.deletePreset` | export presets |
| `export.contactSheet`, `export.checkTarget`, `export.addToPhotos` | sheets, validation, Apple Photos |

## Other families (use `artcraft-find` for parameters)

`mask.*` (31), `keyword.*` (23), `faces.*` (21), `print.*` (20), `denoise.*` (16), `album.*` (15), `slideshow.*` (15), `stack.*` (11), `curve.*` (7), `metadata.*` (7), `spot.*` (7), `folder.*` (6), `label.*` (6), `beforeAfter.*` (5), `version.*` (5), `activity.*`.

The CLI subcommands `render`, `snapshot`, `merge`, and `synth-merge` are not engine commands; `render` takes `--set CONTROL=VALUE`, `--preset ID`, `--size N`, `--quality Q` and `--opt KEY=VALUE` (any `app.export` option).

