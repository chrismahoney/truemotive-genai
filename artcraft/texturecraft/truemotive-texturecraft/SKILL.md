---
name: truemotive-texturecraft
description: Paint, fill and bake textures on 3D meshes and built-in primitives (sphere, cube, torus and more) in TextureCraft (TrueMotive ArtCraft), with layers, projection modes, generators, mesh-map baking, texture export and GPU or path-traced renders, through its headless CLI, MCP server or JSON-lines server. Use to put an image or generated geometry onto a 3D object, compare UV and triplanar projection, export PBR texture sets, or any request to work in TextureCraft.
---

# TrueMotive TextureCraft

3D texture painting and baking in the ArtCraft suite (175 commands, checked 2026-11-14): a project (`.tcraft`) holds a mesh, texture sets, layers that fill channels (baseColor, height, roughness, metallic), baked mesh maps, and cameras. It renders the viewport on the GPU. For node-graph materials use MaterialCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/texturecraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/TextureCraft.app/Contents/MacOS/TextureCraft` |
| Protocol doc | none installed; the CLI points to `docs/control-protocol.md` upstream |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| New project | `texturecraft-cli new <MESH \| builtin:ID> OUT.tcraft [--resolution PX] [--sample]` (verified with `builtin:torus`, 512). Built-ins: material_ball, sphere, cube, rounded_cube, cylinder, torus, plane, crate, udim_plane. Meshes: glb, gltf, fbx, dae, usd, abc, obj, ply, stl. |
| One edit | `texturecraft-cli run IN COMMAND 'JSON' -o OUT.tcraft`; **`-o` is required to keep the change**, so chain calls through files (verified) |
| A script | `texturecraft-cli batch script.json` (`[{"id","params"}...]` or `{"open","steps","save"}`; not yet run) |
| Bake | `texturecraft-cli bake IN [-o OUT] [--resolution PX] [--maps id,id]` (verified on a torus: 0.65 to 0.9 s at 512, 2.1 to 2.2 s at 1024; the project grows from 119 KB to 6.0 MB and 23.4 MB) |
| Export textures | `texturecraft-cli export IN DIR [--preset NAME] [--format EXT] [--padding MODE] [--size PX]` (verified: 5 PNG maps) |
| Render | `texturecraft-cli render IN OUT.png [--size WxH] [--view 3d\|2d] [--camera NAME] [--yaw D] [--pitch D] [--samples N] [--bounces N] [--cpu]` (verified: viewport render, 4.0 s) |
| Servers | `mcp [--bridge PORT --token T] [--read-root DIR] [--write-root DIR]`, `serve [--port P]` (not yet run) |

`IN` is a `.tcraft`, a mesh file, or `builtin:ID`. `render` needs a GPU or a software adapter (the probe used an Apple M1 Max); `--samples` path-traces instead of the viewport render (verified: 32 samples took 0.34 to 1.1 s and gave a glossy, physical look).

## Discover shapes, don't guess

Use `artcraft-find QUERY --app texturecraft` or `texturecraft-cli commands --filter TEXT`. Families: `layer` 26, `tool` 20, `camera` 17, `effect` 16, `textureSet` 16, `bake` 13, `viewport` 11, `file` 11, `mask` 10, `material` 8. Use `find.py --readonly` to hide commands that may change state.

## Editing model and standard flow

Layers fill texture-set channels on a mesh; an image reaches a layer through the project's resources. Commands address layers by id, and an image is referred to by its **resource name, which is the file name including its extension**.

1. `new builtin:torus P.tcraft --resolution 512` (or a mesh file)
2. `resource.import {path}` returns `{"name": "<file name>"}`
3. `layer.add.fill {name}` returns `{"layer": N}`
4. `layer.fill.set {channel:"baseColor", image: NAME}`, then again with `channel:"height"` for relief; `layer.fill.projection {projection: uv\|triplanar\|planar\|spherical\|cylindrical, scale?, rotation?}`
5. Optional: `effect.add.generator {generator: edgeWear\|dirt\|curvature\|ambientOcclusion...}`, `bake` mesh maps, `camera.add` to save a view
6. `render` and `export`, then check with `artcraft-qa` and view

**Verified:** a Penrose PNG as baseColor and height on `builtin:torus` rendered with the tiling wrapped on the torus (viewed), and `export` wrote `torus_Torus_baseColor.png`, `_height`, `_metallic`, `_normal`, `_roughness`. Benchmarked on four seeds (procedural-3d S2 and S3): per primitive, 7 to 10 commands, viewport renders in 0.16 to 0.39 s, exports in 0.1 to 0.3 s.

**Gotchas:** every `run` needs `-o` (saving over the input file works); greyscale maps (height, metallic) make `artcraft-qa` WARN because it decodes colour PNGs only, so view them. **Order changes what an export means:** a UV export of the sphere or torus is an exact copy of the seed (difference 0.0; the cube 1.2 to 3.2 because of its UV islands), but after `layer.fill.projection` triplanar the exported baseColor is re-projected (a difference of 61 to 69), so export before switching projection. UV on a sphere pinches at the pole and shows a meridian seam; triplanar avoids both but renders the pattern at a very different scale (a cube's UV and triplanar renders differed by 17).

## Procedural and generative notes

Seeds are images from `artcraft-gen-recipes`, rendered by PhotoCraft or VectorCraft. `layer.fill.set` takes a `procedural` kind with `scale` and `seed` for noise-style channels (verified: roughness from `clouds`). The kinds are not listed anywhere and an unknown one only says "unknown procedural"; by trial `noise`, `perlin`, `clouds`, `cells`, `voronoi`, `marble` work and `fbm`, `worley`, `grain` do not. UV projection follows the mesh's UVs; triplanar ignores them.

## Save, export, verify

Native `.tcraft` (`file.save`, or `-o`). `file.exportTextures {dir, preset?, format?, padding?, size?, normalFormat?}` or the `export` subcommand writes maps named `<project>_<set>_<channel>`. `bake` writes mesh maps for normal, AO, curvature and more.

## Cross-app hand-offs

- Recipe PNG in from PhotoCraft or VectorCraft (verified for PhotoCraft's PNG).
- From MaterialCraft: `file.sendToTextureCraft` or `file.exportMaterial` writes a `.mcmat` that `file.importMaterialX` and the shelf can read (not yet run). See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- Renders out to LightCraft for a tonal finish (verified: `lightcraft-cli render IN -o OUT --set light.exposure=0.3` on TextureCraft renders).

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/texturecraft/`.

