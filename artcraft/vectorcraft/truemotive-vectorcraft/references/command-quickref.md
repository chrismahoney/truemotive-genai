# VectorCraft command quick reference

Source: `vectorcraft-cli commands` registry, 966 commands, captured 2026-11-14. Params are abbreviated; `?` means optional; `ids?` means "defaults to the selection". The live registry is authoritative: re-dump it if a call is rejected.

Call shape in `run --commands`: `{"command":"ID","params":{...}}` per line. Over MCP use `run_command {command, params}`.

## Documents and files

| Command | Params |
|---|---|
| `file.new` | `preset?, name?, width? (pt=612), height? (pt=792), units? ("Pixels"\|"Points"\|"Millimeters"\|...), orientation?, artboards? (1..1000), artboardLayout?` |
| `file.open` | `{path}` any readable format, opens as a new document |
| `file.save` / `document.save` | `path?, format? (.vectorcraft\|.ai\|.pdf\|.svg\|.svgz), options?, svg?` |
| `file.export` / `document.export` | `path?, format?, artboard?, range?, scale?` (no path returns `dataBase64`) |
| `file.place` | place a file as linked or embedded art |
| `document.inspect` | `depth?, childLimit?` returns artboards, history, layers |
| `document.find` | `name?, kind? (Group\|Path\|Type\|Image), text?, within?: [x,y,w,h]` |
| `document.node` | `id, summary?, depth?, childLimit?` |
| `document.formats` | installed format list and options |
| `document.setUnits` | change document units |

## Shapes and paths (all return `{id}`; the new object becomes the selection)

| Command | Params |
|---|---|
| `shape.rectangle` | `x, y, width, height, radius?, rotation?` |
| `shape.ellipse` | `x, y, width, height, rotation?` |
| `shape.polygon` | `cx, cy, radius, sides=6, rotation?` |
| `shape.star` | `cx, cy, radius1, radius2, points=5, rotation?` |
| `shape.line` | `x1, y1, x2, y2, fill?` |
| `shape.spiral` | `cx, cy, radius, decay=80 (%), segments=10, clockwise?` |
| `shape.arc`, `shape.flare`, `shape.rectangularGrid`, `shape.polarGrid` | see registry |
| `path.create` | `anchors: [{x,y,in?,out?}], closed?` **or** `d: "SVG path data"` |
| `path.setAnchors` | `id, subpaths: [{anchors:[{x,y,in?,out?}], closed}]` replaces geometry |
| `path.appendAnchor`, `path.close`, `path.reverse`, `path.join` | edit an open path |
| `path.moveAnchors`, `path.setHandle`, `path.convertAnchors`, `path.insertAnchor`, `path.deleteAnchors` | anchor edits |
| `path.setFillRule` | `rule: "nonZero"\|"evenOdd", ids?` |
| `path.knife`, `path.split`, `path.cutAtAnchors`, `path.blob` | cutting and merging |

## Paint and stroke

| Command | Params |
|---|---|
| `paint.setFill` | `color?: "#rrggbb"\|[r,g,b]\|{c,m,y,k}\|{gray}\|{l,a,b}, none?, swatch?, tint?, ids?` (`#rrggbbaa` refused) |
| `paint.setStroke` | same as `paint.setFill`, plus `item?` |
| `paint.editGradient` | `stroke?, kind? (linear\|radial\|freeform), stops?...` |
| `paint.swap`, `paint.none`, `paint.default`, `paint.invert` | convenience paint ops |
| `stroke.set` | `weight? (pt), cap? (butt\|round\|square), join? (miter\|round\|bevel), miterLimit?, align?, dash?: [d,g,...]\|null, dashOffset?` |
| `stroke.widthProfile.add\|list\|set` | variable-width strokes |
| `gradient.presets.list\|apply\|save` | `apply {name, stroke?, ids?}` |
| `swatch.new\|list\|edit\|delete`, `swatch.library.get\|add` | swatch and library management |

## Objects (152 commands; all take `ids?`)

| Command | Params |
|---|---|
| `object.move` | `dx, dy, copy?` |
| `object.rotate` | `angle (deg, counter-clockwise), absolute?, origin?: [x,y], copy?` |
| `object.scale` | `sx (%), sy?, origin?, copy?, strokes?` |
| `object.reflect`, `object.shear`, `object.transformEach` | `transformEach {scaleH?, scaleV?, ...}` |
| `object.transform` | `matrix: [a,b,c,d,e,f], copy?` (affine) |
| `object.setProps` | `name?, visible?, locked?, opacity? (0..100), blend?: "Multiply"...` |
| `object.align` / `object.distribute` | `horizontal?, vertical?, to? (selection\|artboard\|key)` |
| `object.group` / `object.ungroup` | `{id}` of the new group |
| `object.arrange.bringToFront\|sendToBack\|bringForward\|sendBackward` | z-order |
| `object.pathfinder.unite\|minusFront\|intersect\|exclude\|divide\|trim\|merge\|crop\|outline\|minusBack` | boolean ops |
| `object.compoundPath.make\|release` | combine into a compound path |
| `object.clippingMask.make\|release` | topmost selected object clips the rest |
| `object.path.offsetPath` | `offset (pt, negative insets), joins?, miterLimit?` |
| `object.path.outlineStroke\|simplify\|smooth\|addAnchorPoints` | path cleanup |
| `object.rasterize`, `object.expandShape` | bake appearance |

## Text, artboards, effects, trace

| Command | Params |
|---|---|
| `text.create` | `x, y, text, size? (pt), font?, style?, color?, rotation?, vertical?` |
| `text.setText`, `text.setStyle`, `text.fonts`, `text.createInPath` | edit and discover type |
| `artboard.new` | `x?, y?, width?, height?, name?, color?, beside?, side?` |
| `artboard.setProps` | `index, name?, color?, x?, y?, width?, height?` |
| `artboard.fitToArt`, `artboard.duplicate`, `artboard.delete` | manage artboards |
| `effect.list` | `{catalog:[{id, params, defaults}]}` for the selection |
| `effect.apply` | `effect: "stylize.dropShadow"\|"distort.roughen"\|"warp.arc"..., params?, ids?` (live, non-destructive) |
| `effect.expandAppearance` | bake live effects |
| `imageTrace.make` | `id?, preset?` (raster to vector); then `imageTrace.expand` |

## Selection and discovery

- `select.all`, `select.none`, `select.inverse`, `select.set {ids}`, `select.add`, `select.toggle`
- `select.same.fillColor|strokeColor|strokeWeight|opacity|appearance|shapeType`
- `select.object.textObjects|openPaths|clippingMasks|strayPoints`
- `document.find {name?, kind?, text?, within?}` then `select.set {ids}`

## Other families (use the registry for params)

`symbol.*` (25), `perspective.*` (25), `livePaint.*`, `shapeBuilder.*`, `graph.*` (charts), `variable.*` and `dataset.*` (data-driven art), `graphicStyle.*`, `appearance.*`, `transparency.*`, `charStyle.*`, `paraStyle.*`, `guide.*`, `links.*`, `library.*`, `svgFilter.*`, `svgInteractivity.*`, `webExport.*`, `pdf.*`, `print.*`, `addon.*`.

## Registry snippet

```sh
vectorcraft-cli commands > "$SCRATCH/vc-cmds.json"
python3 -I -c "import json,sys;[print(c['id'],'|',c['params'][:160]) for c in json.load(open(sys.argv[1])) if c['id'].startswith(sys.argv[2])]" "$SCRATCH/vc-cmds.json" shape.
```



