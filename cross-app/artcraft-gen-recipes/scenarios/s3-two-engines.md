# Scenario 3: same seed, two engines (MaterialCraft vs TextureCraft)

An A/B benchmark in the style of `pc-vs-vc` (see [truemotive-ab-benchmark](../../../benchmark/truemotive-ab-benchmark/SKILL.md)). One seed image, one primitive set, one camera: build the textured primitive in MaterialCraft (node graph) and in TextureCraft (mesh layers), then compare the workflow and the results, and finish both renders identically in LightCraft.

**Apps, in order of use:** VectorCraft (seed PNG) → MaterialCraft (route A) → TextureCraft (route B) → LightCraft (identical finish on both renders).

**Seed inputs (two runs, different each time)**

| Run | Seed | File (already generated) |
|---|---|---|
| 1 | Truchet, seed 3, 12x12, VectorCraft render, 512 px | `artifacts-test/gen-recipes/truchet-vc.png` |
| 2 | Phyllotaxis, 700 dots, VectorCraft render, 512 px | `artifacts-test/gen-recipes/phyllotaxis-vc.png` |

**Fixed across both routes:** torus and cube, 800x600 renders, the seed as colour and as height, 512 px maps.

## Commands

Route A uses the MaterialCraft commands in [s1-materialcraft-pbr.md](s1-materialcraft-pbr.md). Route B uses the TextureCraft commands in [s2-texturecraft-paint.md](s2-texturecraft-paint.md), with `builtin:torus` and `builtin:cube`. Finish both renders with `lightcraft-cli render IN -o OUT --set light.exposure=0.3`.

## Steps

1. Route A: build the package, render torus and cube, export the six maps. Record commands and timing for each step.
2. Route B: build the project, render torus and cube, export maps. Record the same.
3. Compare the two exported baseColor maps against the seed (pixel-diff snippet), and the two height maps against each other.
4. Finish all four renders identically in LightCraft and view them side by side.
5. Write `results.md` for each route and `comparison.md` using the report templates in the benchmark skill.

## Metrics (scoreboard rows)

| Metric | How |
|---|---|
| Success | each route completes with no errors |
| Commands sent | count per route, from new document to final render |
| Wall time | end to end, median of 3 runs into scratch directories; note cold starts |
| Render time | per primitive, per route (MaterialCraft is CPU-friendly; TextureCraft uses the GPU) |
| Maps produced | which of baseColor, height, normal, roughness, metallic, AO each route writes |
| Fidelity | exported baseColor vs seed, mean absolute difference |
| Surface | height relief visible in the render; seams on the cube; tiling behaviour |
| Editability | swap the seed and re-render in each route; what has to be redone |
| Output size | `.sbs` vs `.tcraft`, maps, renders |

## Pass criteria

Both routes finish both primitives for both seeds with a viewed, non-blank render each. The comparison states a winner per criterion and an overall "use A when, use B when", with caveats: the two routes use different lighting and scenes, so renders are compared by visible features and the exported maps are compared numerically.

## Run results (2026-11-14)

Both runs passed (Truchet, phyllotaxis). TextureCraft was about twice as fast end to end (1.18 s vs 2.27 and 2.37 s) and six times faster at rendering; MaterialCraft writes six maps including AO from a 9.7 KB package, needs no GPU, and its exported base colour matched the seed exactly in both runs. Both exported the seed faithfully in UV. Verdict: MaterialCraft for a reusable, tileable material; TextureCraft for painting a specific mesh. Details: [`benchmarks/procedural-3d/run/s3-two-engines/`](../../../../benchmarks/procedural-3d/run/s3-two-engines/truchet/comparison.md).

