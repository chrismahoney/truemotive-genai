# TextureCraft command quick reference

Source: `texturecraft-cli commands` registry, 175 commands, captured 2026-11-14. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app texturecraft`, or `texturecraft-cli commands --filter TEXT`.

Call shape: `texturecraft-cli run IN COMMAND 'JSON' -o OUT.tcraft` (the `-o` saves; without it the change is lost).

## Projects, meshes, files (file 11)

| Command | Params |
|---|---|
| `file.new` | `mesh: path to a mesh file, resolution? (2048), name?, uvTiles?: bool, template?` (the CLI `new` subcommand also takes `builtin:ID`) |
| `file.open`, `file.save`, `file.saveAs`, `file.saveCopy`, `file.close` | `file.save {path?}` |
| `file.exportTextures` | `dir, preset?, ts? (index\|"all"), format? (png\|jpg\|tga\|tif\|exr...), bitDepth?, padding?, dilation?, size?, normalFormat? (openGl\|directX)` |
| `file.exportMesh`, `file.reimportMesh` | mesh out and back in |
| `file.importMaterialX` | `path (.mtlx), material?, name?` makes one fill layer |

## Resources and layers (resource 4, layer 26)

| Command | Params |
|---|---|
| `resource.import` | `path` (png, jpg, tga, tif, bmp, webp, exr, hdr) returns `{name}` |
| `resource.list`, `resource.remove` | list and remove (`name`) |
| `layer.add.fill` | `name?, color?, roughness?, metallic?` returns `{layer}` |
| `layer.add.image` | `name, channel? (baseColor), projection? (uv\|triplanar\|planar), scale?` |
| `layer.add.paint`, `layer.add.group`, `layer.add.decal` | other layer kinds |
| `layer.fill.set` | `layer? \| effect?, channel, color? \| value? \| procedural? (kind, scale?, seed?, contrast?...) \| image? (resource name), normalFormat?, solo?` |
| `layer.fill.projection` | `layer? \| effect?, projection? (uv\|triplanar\|planar\|spherical\|cylindrical), scale? (number or [u,v]), rotation?, offset?` |
| `layer.remove`, `layer.duplicate`, `layer.rename`, `layer.blend`, `layer.visible` | layer management |

## Texture sets, baking, effects, cameras

| Command | Params |
|---|---|
| `textureSet.list`, `textureSet.inspect`, `textureSet.channel.add` | sets and channels |
| `textureSet.meshMap.set` | `ts?, map (normal, ambientOcclusion, curvature, id, height...), image` |
| `bake.run` | `ts? (index\|list\|"all"\|"selected"), cpu?, ...bake.settings` returns `{baked, tracer}` |
| `effect.add.generator` | `layer?, name?, generator? (edgeWear\|dirt\|thinAreas\|curvature\|ambientOcclusion\|position\|direction), level?, softness?, noise?, invert?, mode?` |
| `effect.add.levels`, `effect.add.filter`, `effect.add.fill` | other effects |
| `camera.set` | `yaw?, pitch?, distance?, fov?, target?, ortho?` |
| `camera.add`, `camera.get`, `camera.list` | save and read views; `render --camera NAME` uses a saved one |
| `export.plan`, `export.presets` | export presets and plan |

## Other families

`tool.*` (20), `viewport.*` (11), `mask.*` (10), `material.*` (8), `project.*` (5), `brush.*` (4).

CLI subcommands `new`, `run`, `batch`, `bake`, `export`, `render`, `info`, `mcp` and `serve` are not engine commands.
