---
name: artcraft-gen-recipes
description: Verified generative-art recipes (Truchet arcs, phyllotaxis, Penrose tiling) that emit one neutral shapes.json which per-app emitters turn into PhotoCraft or VectorCraft commands. Use when asked to generate patterns, tilings, or algorithmic art in an ArtCraft app, to produce the same artwork in two apps, to seed an A/B benchmark prompt, or to add generative support for a newly onboarded app.
---

# ArtCraft generative recipes

Compute geometry once, render it in any app. Recipes print a neutral `shapes.json`; an emitter turns that into the app's command stream; the app's headless CLI renders it. Nothing is written by the scripts themselves.

```
recipes/<name>.py ARGS  |  emitters/emit_<app>.py - NAME  |  app CLI        (pure pipes, no intermediate file)
```

## shapes.json (neutral format)

```json
{"width": 512, "height": 512, "background": "#0b132b",
 "layers": [{"name": "Dots", "fill": "#ffd166", "stroke": null, "stroke_width": 2,
             "polygons": [[[x,y],[x,y],[x,y]]], "polylines": [[[x,y],[x,y]]]}]}
```

Coordinates are pixels, y down. Layers draw bottom to top. `polygons` are closed and filled when `fill` is set; `polygons` and `polylines` are stroked when `stroke` is set. Generators should group by colour (one layer per colour), which keeps command counts low.

## Recipes (all verified through both apps, 2026-11-14)

| Recipe | Run | Output |
|---|---|---|
| `truchet.py` | `python3 -I recipes/truchet.py SEED N` | N x N quarter-arc tiles, one stroked layer of 288 open polylines at N=12 |
| `phyllotaxis.py` | `python3 -I recipes/phyllotaxis.py N` | N golden-angle dots in three colour bands; 700 dots ran cleanly |
| `penrose.py` | `python3 -I recipes/penrose.py LEVELS` | Penrose P3 tiling, two fill layers plus an edge layer; 6 levels about 1,500 triangles |

The Voronoi stained-glass benchmark keeps its own generator and data in `benchmarks/pc-vs-vc/shared/`.

## Emitters

```sh
# PhotoCraft (the app saves NAME.png and NAME.pcraft into DIR)
python3 -I recipes/truchet.py 3 12 | python3 -I emitters/emit_photocraft.py - NAME | photocraft-cli serve --automation-write-root DIR
# VectorCraft (the app exports SVG, PNG and native file)
python3 -I recipes/truchet.py 3 12 | python3 -I emitters/emit_vectorcraft.py - NAME | vectorcraft-cli run --commands - --export DIR/NAME.svg --export DIR/NAME.png --export DIR/NAME.vectorcraft
```

The `-` makes an emitter read `shapes.json` from stdin; a file path also works if you already have one.

## What the verification showed

- **Truchet** (12x12, 288 arcs): identical geometry in both apps, continuous curves, no seams. PhotoCraft 5 steps; VectorCraft 2 objects (background plus one compound path).
- **Phyllotaxis** (700 dots): both rendered cleanly in three colour bands.
- **Penrose** (6 levels): PhotoCraft needed 15 steps because the emitter chunks paths under the 4096-knot cap; VectorCraft took each layer as one path. The PhotoCraft render shows a few faint stray diagonal lines near the upper right that the earlier standalone Penrose test did not; the pattern itself is correct.
- Outputs for all of these are in `artifacts-test/gen-recipes/`. Check yours with [artcraft-qa](../artcraft-qa/SKILL.md).

## Scenarios (multi-app test plans)

`scenarios/` holds test plans that start from a recipe's output and carry it through other apps. Each lists the apps in order, the seed inputs, the commands that were verified, the metrics, and what is not yet run.

- [s1-materialcraft-pbr.md](scenarios/s1-materialcraft-pbr.md): geometry as a PBR material on 3D primitives (MaterialCraft).
- [s2-texturecraft-paint.md](scenarios/s2-texturecraft-paint.md): geometry as paint on primitives, UV vs triplanar (TextureCraft).
- [s3-two-engines.md](scenarios/s3-two-engines.md): the same seed in both engines, head to head.

Their benchmark root, with the apps-by-color diagram and the approval status, is [benchmarks/procedural-3d/README.md](../../../benchmarks/procedural-3d/README.md).

## Adding a recipe

Write a script that prints `shapes.json` to stdout and takes its parameters as arguments (a seed first, for anything random). Test it through both emitters and look at both images. Keep one layer per colour.

## Adding an emitter for a new app

Do it during onboarding with [artcraft-skill-author](../artcraft-skill-author/SKILL.md): copy the closest existing emitter, map layers to that app's primitives, and prove it on one recipe. Note the app's own limits in its skill (PhotoCraft's knot cap is the model). Apps with timeline, cell, audio, or 3D models need their own mapping and may support only some recipes.

## Recipes as benchmarks

Any recipe is a ready A/B prompt for [truemotive-ab-benchmark](../../benchmark/truemotive-ab-benchmark/SKILL.md): same `shapes.json` into two apps, then measure the outputs.

