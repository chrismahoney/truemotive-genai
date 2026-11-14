# Scenario 2: geometry as paint on 3D primitives (TextureCraft)

Paint generated geometry onto built-in meshes and compare how UV and triplanar projection treat it. TextureCraft works on a mesh: layers fill texture channels, mesh maps are baked, and the viewport renders on the GPU.

**Apps, in order of use:** VectorCraft (crisp seed PNG from a recipe) → TextureCraft (paint, bake, export, render) → LightCraft (tonal finish).

**Seed inputs (two runs, different each time)**

| Run | Seed | File (already generated) |
|---|---|---|
| 1 | Penrose P3, 6 levels, VectorCraft render, 512 px | `artifacts-test/gen-recipes/penrose-vc.png` |
| 2 | Voronoi stained glass, VectorCraft render, 1024 px | `benchmarks/pc-vs-vc/run/vectorcraft/output/voronoi-glass.png` |

Primitives available as `builtin:<id>`: material_ball, sphere, cube, rounded_cube, cylinder, torus, plane, crate, udim_plane. Use sphere, cube and torus.

## Verified commands (2026-11-14, Penrose PNG seed, probe only)

```sh
T=/Users/chris/Claude/TrueMotive/artcraft-root/bin/texturecraft-cli
$T new builtin:torus P.tcraft --resolution 512
$T run P.tcraft resource.import '{"path":"SEED.png"}' -o P.tcraft          # returns {"name": "<file name>"}
$T run P.tcraft layer.add.fill '{"name":"Seed"}' -o P.tcraft               # returns {"layer": 2}
$T run P.tcraft layer.fill.set '{"channel":"baseColor","image":"SEED.png"}' -o P.tcraft
$T run P.tcraft layer.fill.set '{"channel":"height","image":"SEED.png"}' -o P.tcraft
$T render P.tcraft out.png --size 800x600 --view 3d --yaw 25 --pitch 20   # 4.0 s on Apple M1 Max; viewed: tiling on the torus
$T export P.tcraft MAPS_DIR --size 512      # baseColor, height, metallic, normal, roughness
```

Viewed: the torus render shows the tiling wrapped on the surface with relief from the height channel.

## Steps

1. For each of sphere, cube and torus: `new builtin:<id>`, import the seed, add a fill layer, set baseColor and height from the image.
2. Projection comparison: `layer.fill.projection {"projection":"uv"}` vs `"triplanar"` on the cube and sphere; render each from the same camera. Export the UV maps and run any swap-seed edit **before** switching to triplanar.
3. Add one procedural channel (`layer.fill.set` with `procedural` for roughness) to show seed plus noise.
4. `bake` mesh maps at 512 and 1024 (`bake P.tcraft --resolution N`), then `export`.
5. One path-traced render (`render ... --samples 32`) against the viewport render.
6. Tonal finish of the renders with `lightcraft-cli render`.

## Metrics

| Metric | How |
|---|---|
| Setup cost | commands per primitive, `.tcraft` size at 512 and 1024 |
| Bake time | wall time of `bake` at 512 and 1024 |
| Render time | viewport render per primitive (GPU), and the path-traced render |
| Projection | UV vs triplanar: visible seams or stretching on the cube and sphere (view both, same camera), noted in words |
| Maps | exported map set and sizes; `artcraft-qa` on each (greyscale maps WARN; view them) |
| Fidelity | exported baseColor vs the seed PNG, mean absolute difference |
| Editability | swap the image on the layer and re-render; layers and fill channels are still editable |

## Pass criteria

Three primitives render non-blank with the seed visible; the exported baseColor matches the seed within a recorded difference; the projection comparison produces two different renders on the cube; no command returns an error.

## Run results (2026-11-14)

Both runs passed (Penrose, Voronoi glass): 43 commands, 7.4 and 9.8 s. Everything in the steps ran, including both bake sizes and the path-traced render. TextureCraft's `render` needs a GPU or software adapter (this used an Apple M1 Max). Findings: UV exports of the sphere and torus are exact copies of the seed, while exports made after switching to triplanar are re-projected, so **export before changing projection**; UV pinches at a sphere's pole and shows a seam; triplanar renders at a very different scale. Details: [`benchmarks/procedural-3d/run/s2-texturecraft/`](../../../../benchmarks/procedural-3d/run/s2-texturecraft/penrose/results.md).

