# PhotoCraft command quick reference

Source: `photocraft-cli commands` registry, 1009 commands, captured 2026-11-14. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected.

Calls are `{command, params}` in `engine.execute` or `batch` steps. Params must be an object.

## Documents and files

| Command | Params |
|---|---|
| `file.new` | `width, height (1..300000), mode (rgb\|gray\|cmyk\|lab), depth (8\|16\|32), background (white\|black\|transparent\|#rrggbb), resolution (ppi), name` |
| `document.inspect` | `document?: index` |
| `document.activate` | switch the active document |
| `file.placeEmbedded` | place as Smart Object (ambient path refused; use `doc.place`) |
| `file.export.layersToFiles` | one file per layer (use `doc.exportLayers` headless) |

Transport methods (serve): `doc.new`, `doc.open {path}`, `doc.save {path, format?, quality?}`, `doc.render {maxSide, path?}`, `doc.inspect`, `doc.place {path, scale?, fit?, center?}`, a session-list method, `batch {steps, stopOnError}`, `methods`. These are transport methods, not engine commands, so they never appear in `commands`.

## Layers (233 commands; `layer.*`)

| Command | Params |
|---|---|
| `layer.new.layer` | `name?, mode?, opacity? (0..1), color?, clipToPrevious?, fillNeutral?, position? (above\|below)` |
| `layer.new.group` | `name?, mode?, opacity? (0..100), position?` |
| `layer.duplicate` | `layer?, name?, inPlace?, document? (index\|"new")` |
| `layer.delete` | `layer?` (none: all selected) |
| `layer.select` | `layer: id\|name\|{index}\|{ordinal}, mode? (replace\|toggle\|range\|add\|remove)` |
| `layer.setProps` | `layer?, layers?[], name?, visible?, opacity? (0..1), fill?, blend?...` |
| `layer.arrange.bringToFront` / `sendToBack` / `bringForward` / `sendBackward` | `layer?` |
| `layer.mergeDown` / `layer.flattenImage` | `layer?` / `{}` |
| `layer.createClippingMask` | clip to the layer below |
| `layer.layerMask.revealAll` / `hideAll` / `revealSelection` | add a mask |
| `layer.newFillLayer.solidColor` | `color?, path?, opacity?, name?, mode?` |
| `layer.newFillLayer.gradient` | `from, to (#hex), angle=90, style (linear\|radial\|angle\|reflected\|diamond), reverse, stops?` |
| `layer.newFillLayer.pattern` | `pattern: id\|name, scale, angle, link, phase?` |
| `layer.newAdjustmentLayer.<kind>` | kinds: `brightnessContrast levels curves exposure vibrance hueSaturation colorBalance blackWhite photoFilter channelMixer invert posterize threshold gradientMap selectiveColor colorLookup` |
| `layer.layerStyle.gradientOverlay` / `patternOverlay` | `from, to, stops?` / `pattern, scale, angle, opacity` |

Adjustment-layer params mirror `image.adjustments.<kind>` plus `path?, opacity?, name?, mode?, clipToPrevious?`.

## Fill, stroke, paths, shapes

| Command | Params |
|---|---|
| `edit.fill` | `contents (color\|foreground\|background\|pattern\|history\|contentAware\|black\|gray\|white), color?: #hex\|[r,g,b,a], pattern?, scale?, angle?, mode?, opacity?, preserveTransparency?, target?` |
| `edit.stroke` | `width (1..250), color?, location (inside\|center\|outside), mode?, opacity?` (strokes the selection) |
| `edit.transform` | `layer?, layers?[]` plus transform fields (see registry) |
| `path.set` | `name? ("work"), path: {subpaths:[{closed, op?, knots:[[x,y]\|{anchor,in,out,smooth}]}], fillRule (nonzero\|evenodd)}, op? (append)`. **4096 knot cap.** |
| `path.fill` | `name? ("work"\|"layer"\|saved), layer?, color?: #hex, opacity?, mode?, feather?, antiAlias?` |
| `path.stroke` | `name?, layer?, tool (brush\|pencil\|eraser\|...), size?, hardness?, opacity?, color?: #hex` |
| `path.toSelection` | `name?, feather?, antiAlias?, mode (replace\|add\|subtract\|intersect)` |
| `path.toShape` | `name? \| path?, fill?: #hex\|gradient, stroke?` (makes an editable shape layer) |
| `shape.create` | `kind (rect\|roundedRect\|ellipse\|polygon\|star\|line\|path), rect?: [x,y,w,h], radii?, sides?, starRatio?, cornerRadius?, fill?, stroke?` |
| `shape.edit` / `shape.info` / `shape.rasterize` | edit live shape params / read / bake to pixels |

## Selection

`select.all {}`, `select.deselect`, `select.inverse`, `select.rect {x,y,width,height,mode?,ellipse?,feather?}`, `select.colorRange`, `select.subject`, `select.modify.expand|contract|feather|smooth|border`, `select.saveSelection`, `select.loadSelection`.

## Paint, gradients, patterns

- `paint.stroke {points:[[x,y,pressure?]...], size?, hardness?, opacity?, flow?, preset?, target?}`; also `paint.pencil`, `paint.bucket`, `paint.cloneStamp`, `paint.healingBrush`, `paint.dodge|burn|blur|sharpen|smudge`.
- `paint.gradient {from:[x,y], to:[x,y], style?, colors?:[#hex], stops?:[[t,#hex]], transparency?}` paints pixels.
- `gradient.fill.create {from, to, style, stops, reverse, dither}` makes an editable gradient layer; `gradient.fill.set|stop|get` edit it. `gradient.presets.list|apply|new`.
- `pattern.list`, `pattern.presets.new {name?, rect?}` (define from canvas), `pattern.presets.apply {pattern, scale, angle}`, `layer.newFillLayer.pattern`.

## Adjustments and filters

- Destructive: `image.adjustments.<kind>` (same kinds as adjustment layers, plus `desaturate`). Prefer the `layer.newAdjustmentLayer.<kind>` form.
- `filter.render.*`: `clouds {seed, foreground?, background?}`, `differenceClouds`, `fibers {variance, strength, seed}`, `lensFlare`, `lightingEffects`, `relight`, `tree`, `flame`, `pictureFrame`.
- `filter.blur.gaussianBlur {radius 0.1..1000}`, `motionBlur`, `radialBlur`, `surfaceBlur`, `shapeBlur`.
- `filter.noise.addNoise {amount, distribution, monochromatic, seed}`; `filter.sharpen.unsharpMask|smartSharpen`.
- `filter.stylize.*`, `filter.distort.*` (twirl, wave, ripple, spherize), `filter.pixelate.*`, `filter.gallery.*` (47 artistic filters), `filter.liquify`, `filter.cameraRaw`.

## Type, history, actions

- `type.create {x, y, text, box?, name?, align?, ...character fields}`, `type.edit`, `type.setStyle`, `type.fonts`, `type.rasterize`.
- `history.undo|redo|stepBackward|newSnapshot|selectState`; `edit.undo|redo`.
- `actions.list|play|record|load` replay Photoshop-style action sets; `batch`/`droplet` CLI subcommands apply one to a folder.
- `jobs.list`, `jobs.cancel` (transport methods) track `wait:false` commands.



