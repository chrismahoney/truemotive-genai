# MaterialCraft command quick reference

Source: `materialcraft-cli commands` registry, 112 commands, captured 2026-11-14. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app materialcraft`, or `materialcraft-cli commands --filter TEXT`.

Call shape: `materialcraft-cli run IN.sbs COMMAND 'JSON' -o OUT.sbs` (the `-o` saves; without it the change is lost).

## Packages and files (13)

| Command | Params |
|---|---|
| `file.new` | `name?, folder?, kind? (material\|function), template? (see graph.templates), size? (px, power of two)` adds a graph |
| `file.newPackage`, `file.open`, `file.save`, `file.saveAs`, `file.saveCopyAs` | package lifecycle; `file.save {path?}` writes `.sbs` or `.mcraft` |
| `file.importBitmap` | `path, name?, folder?` returns the resource name |
| `file.importVector` | `path (SVG), name?, folder?` keeps the original bytes |
| `file.export` | `dir, format? (png\|jpg\|tga\|tif\|bmp\|webp\|exr\|hdr), pattern? ($(graph)_$(identifier)), depth? (8\|16\|32), size? (px), graph?` |
| `file.exportMaterial` | `path, graph?, size?, values?, inputs?` writes a portable `.mcmat` |
| `file.sendToTextureCraft` | `graph?` puts the material in TextureCraft's library folder |

## Graph editing (graph 61)

| Command | Params |
|---|---|
| `graph.templates` | `{}` lists templates for `file.new` |
| `graph.node.add` | `def (see library.list), at?, params? {id: value}, connectFrom? {node, port?}, label?` returns `{id}` |
| `graph.node.param` | `id?, param, value` (numbers, `[x, y]`, `"#rrggbb"`, enum index, typed `{t, v}`) |
| `graph.node.info` | `id` describes a node |
| `graph.connect` | `from, fromPort?, to, toPort?, detach? {to, toPort}` |
| `graph.disconnect` | `to, toPort` |
| `graph.cook` | `full?: bool` returns per-node timings and errors |
| `graph.input.bind`, `graph.input.unbind` | `identifier, resource? \| path?, linear?` shows an image on an input node |
| `graph.exposed.add`, `graph.exposed.set`, `graph.exposed.delete` | exposed inputs: `graph.exposed.set {id, value}` |
| `graph.size`, `graph.seed`, `graph.rename`, `graph.duplicate`, `graph.delete`, `graph.open` | graph settings and management |
| `graph.preset.save`, `graph.preset.apply` | input presets |

## Library and views

| Command | Params |
|---|---|
| `library.list` | `filter?, category?` every node definition with ports and parameters |
| `view.3d.assign` | `graph?, node?, port?, channel: baseColor\|normal\|roughness\|metallic\|height\|ambientOcclusion\|emissive\|opacity, reset?` |
| `view.2d`, `view.3d`, `view.3d.loadMesh` | switch views, load a mesh |

## Other families

`edit.*` (13), `view.*` (8), `folder.*` (5), `package.*` (3), `explorer.*` (3), `session.*` (3).

CLI subcommands `new`, `run`, `batch`, `cook`, `export`, `render`, `nodes`, `info`, `mcp` and `serve` are not engine commands.
