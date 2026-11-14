---
name: artcraft-handoff
description: Move work between ArtCraft apps - vector to raster (VectorCraft to PhotoCraft), raster to vector (PhotoCraft to VectorCraft via image trace), and other format bridges - with tested recipes, shared-directory and read/write-root rules, and the known losses at each hop. Use when a task spans two apps, when asked to trace or vectorise an image, to finish a vector design with raster effects, or to pick a bridge format between apps.
---

# ArtCraft hand-offs

Each hop goes through a file in a shared task directory. Verify every hop with [artcraft-qa](../artcraft-qa/SKILL.md).

## Verified route 1: vector to raster (VectorCraft to PhotoCraft)

1. VectorCraft exports PNG: `vectorcraft-cli run ... --export DIR/x.png` (set `--scale N` or `--ppi N` for resolution).
2. PhotoCraft opens it headlessly with DIR as the **read root**: `photocraft-cli serve --automation-read-root DIR --automation-write-root OUT`, then `{"method":"doc.open","params":{"path":"x.png"}}` (path relative to the read root).
3. Edit as usual (new layers, blend modes, filters), then `doc.save` PNG and `.pcraft`.

Tested with the pc-vs-vc VectorCraft PNG: it opened as a 1024x1024 Background layer; a new Overlay layer at 0.5 opacity plus a radial gradient applied with 0 failures; PNG and `.pcraft` saved (the PNG warns that 2 layers were flattened). Not yet run: `doc.place` (placing as a Smart Object in an existing document).

## Verified route 2: raster to vector (PhotoCraft to VectorCraft)

```
file.open (via run --in IMAGE.png)  ->  select.all  ->  imageTrace.make {"preset":"6 Colors"}  ->  imageTrace.expand  ->  --export out.svg
```

- **Select first.** `imageTrace.make` fails with "nothing selected" otherwise, and an unknown preset name fails with the valid list. Built-in presets: Default, Auto Color, High Fidelity Photo, Low Fidelity Photo, 3 Colors, 6 Colors, 16 Colors, Shades of Gray, Black and White Logo, Sketched Art, Silhouettes, Line Art, Technical Drawing, Outline, Flat Logo.
- Tested on the 512x512 Penrose PNG: 645 paths, 7,316 anchors, 3 colours detected, SVG 309 KB, re-exported PNG viewed and faithful. One small artifact: a faint dashed outline around one tile near the top centre. Trace output is an approximation, so compare it visually.

## Verified route 3: image to 3D material, then tonal finish

```
PhotoCraft or VectorCraft PNG  ->  MaterialCraft  (file.importBitmap, bitmap node to basecolor and height, export, render)
                               ->  TextureCraft   (resource.import, layer.fill.set image on baseColor and height, export, render)
renders  ->  LightCraft  (lightcraft-cli render IN -o OUT --set light.exposure=0.3)
```

Run six times with Penrose, Truchet, Voronoi and phyllotaxis seeds (see `benchmarks/procedural-3d/`). Rules learned: the exported MaterialCraft base colour equals the seed exactly; a TextureCraft UV export equals it for the sphere and torus (cube within 3.2), but an export made after switching to triplanar projection is re-projected, so export first. Non-periodic seeds (Penrose) show a seam when tiled; periodic ones (Truchet) do not. `file.sendToTextureCraft` (MaterialCraft to TextureCraft's library) is documented but not yet run.

## Format bridges (from each CLI's own help; probe the rest)

| App | Reads and writes |
|---|---|
| PhotoCraft | `.pcraft .psd .png .jpg .tif .webp .exr` |
| VectorCraft | reads many (`.svg .pdf .ai .eps .psd .png .dxf`...), writes `.vectorcraft .svg .pdf .ai .png .eps .dxf .psd` |
| CADCraft | `.dxf .dwg .dwt .svg .png .pdf` |
| FigCraft | `.figcraft .json .svg .png .jpg .webp .pdf .fig .penpot` |
| GridCraft | `.xlsx .csv .tsv .json .html .pdf` |
| MaterialCraft | reads PNG and SVG (`file.importBitmap`, `file.importVector`); writes maps as `png jpg tga tif bmp webp exr hdr`, packages as `.sbs`, portable materials as `.mcmat` |
| TextureCraft | reads meshes (`glb gltf fbx dae usd abc obj ply stl`) and images (`png jpg tga tif bmp webp exr hdr`); writes textures `png jpg tga tif exr`, projects as `.tcraft` |

Universal bridges: **PNG** (any raster), **SVG** (VectorCraft, FigCraft, CADCraft), **PDF** (VectorCraft, CADCraft, FigCraft, GridCraft). For apps not listed run `<cli> convert --help` and add the result here.

## Rules

- One shared task directory. Give each app a read root or write root for it (`--automation-read-root`, `--automation-write-root`); never reuse ports or tokens between apps.
- Losses per hop: PhotoCraft PNG export flattens layers (save `.pcraft` too); tracing is approximate; SVG to raster is resolution-fixed.
- Save a native file at each stage so any step can be redone.
- Run the QA checker after every hop, and view the final image.

## Not yet run

SVG into FigCraft or CADCraft, PDF into DeckCraft, GridCraft charts to VectorCraft. Verify, then move each into the verified section.

