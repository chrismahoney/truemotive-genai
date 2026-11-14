# Scenario 1: geometry as a PBR material (MaterialCraft)

Turn generated geometry into a procedural PBR material and render it on 3D primitives. MaterialCraft builds a node graph; the seed image becomes colour and height, so the tiling is also surface relief.

**Apps, in order of use:** PhotoCraft (seed PNG from a recipe) → MaterialCraft (graph, export, render) → LightCraft (tonal finish of the renders).

**Seed inputs (two runs, different each time)**

| Run | Seed | File (already generated) |
|---|---|---|
| 1 | Penrose P3, 6 levels, 512 px | `artifacts-test/test_pc_penrose-tiles.png` |
| 2 | Truchet, seed 3, 12x12, 512 px | `artifacts-test/gen-recipes/truchet-pc.png` |

## Verified commands (2026-11-14, Penrose seed, probe only)

```sh
M=/Users/chris/Claude/TrueMotive/artcraft-root/bin/materialcraft-cli
$M new pbr OUT.sbs --size 512 --name SeedMat
$M run OUT.sbs file.importBitmap '{"path":"SEED.png","name":"seed"}' -o OUT.sbs
$M run OUT.sbs graph.node.add '{"def":"bitmap","params":{"resource":"seed"}}' -o OUT.sbs   # returns {"id":13}
$M run OUT.sbs graph.connect '{"from":13,"to":2}'  -o OUT.sbs    # basecolor
$M run OUT.sbs graph.connect '{"from":13,"to":10}' -o OUT.sbs    # height
$M render OUT.sbs torus.png --scene torus --size 800x600 --hq     # 1.4 s; viewed: tiling wrapped with relief
$M export OUT.sbs MAPS_DIR --format png --size 512                # writes 6 maps
$M render OUT.sbs cube3.png --scene cube --size 640x480 --tiling 3 # 0.3 s
```

The `pbr` template has six output nodes: 2 basecolor, 4 normal, 6 roughness, 8 metallic, 10 height, 12 ambientocclusion. Each `run ... -o` saves the package, so chain them. A node library entry `normal` (input to output) exists for deriving a normal map.

## Steps

1. Create the package, import the seed, add the bitmap node, connect colour and height.
2. Derive a normal map: `graph.node.add {"def":"normal","connectFrom":{"node":13}}`, then connect it to output 4 (not yet run).
3. `cook` to get per-node timings; `export` the six maps.
4. Render the material on a torus, a cube and a sphere (`--hq`), and the cube again with `--tiling 3`.
5. Give each render a tonal finish with `lightcraft-cli render IN -o OUT --set light.exposure=0.3`.

## Metrics

| Metric | How |
|---|---|
| Graph build | commands sent, package size (`.sbs`) |
| Cook time | `cook` total and per-node ms |
| Render time | wall time per primitive, `--hq` and plain |
| Maps | the six exported maps present, sizes, `artcraft-qa` on each (greyscale maps WARN; view them) |
| Tiling | left/right and top/bottom edge difference of the exported basecolor map (pixel-diff snippet), plus the `--tiling 3` render viewed for seams |
| Fidelity | exported basecolor vs the seed PNG, mean absolute difference |
| Editability | change one parameter (the bitmap resource or a node value), re-render, confirm only that changed |

## Pass criteria

All six maps exist and open; the three primitive renders are non-blank and show the seed; the basecolor export matches the seed within a small difference (record the number); no `error` in `cook`.

## Run results (2026-11-14)

Both runs passed (Penrose, Truchet): 16 commands, 4.4 to 4.9 s, 6 maps, 4 renders and 3 LightCraft finishes each. Normal derivation, the sphere render and the second seed all ran. Greyscale-map QA was skipped by decision. Findings: the exported basecolor was an exact copy of the seed; selection is session state, so a parameter edit needs a `batch`; Penrose has a vertical seam when tiled and Truchet does not. Details: [`benchmarks/procedural-3d/run/s1-materialcraft/`](../../../../benchmarks/procedural-3d/run/s1-materialcraft/penrose/results.md).

