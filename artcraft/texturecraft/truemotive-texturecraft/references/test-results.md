# TrueMotive TextureCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.7.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | Full texture command catalog |
| `paint.brush` | ✅ Brush stroke | RGB color, opacity, size |
| `paint.spray` | ✅ Spray stroke | Multiple particles, size jitter |
| `bake normal` | ✅ Bakes normal map | 1024x1024 output format |
| `bake ao` | ✅ Bakes ambient occlusion | 1024x1024 output format |
| `bake depth` | ✅ Bakes depth map | 1024x1024 output format |
| `project cylindrical` | ✅ Cylindrical projection | Wrap-around texture generated |
| `project spherical` | ✅ Spherical projection | Full sphere map generated |
| `export tcraft` | ✅ Exports .tcraft | Native format with layers |
| `export png` | ✅ Exports PNG | 16-bit output with alpha |

## Verified Operations

### 1. Brush Stroke (`paint.brush`)
- **Command pattern:** `./bin/texturecraft-cli run --cmd 'paint.brush' --params '{color: "rgba(255,0,0,1)", size: 50, opacity: 1.0}'
- **Result:** Red brush stroke on texture canvas
- **Status:** ✅ Pass

### 2. Spray Stroke (`paint.spray`)
- **Command pattern:** `./bin/texturecraft-cli run --cmd 'paint.spray' --params '{color: "rgba(0,0,255,1)", size: 30, count: 100}'
- **Result:** Blue spray stroke with particle variation
- **Status:** ✅ Pass

### 3. Bake Normal Map (`bake normal`)
- **Command pattern:** `./bin/texturecraft-cli run --cmd 'bake normal' --params '{size: 1024}'
- **Result:** 1024x1024 normal map generated
- **Status:** ✅ Pass

### 4. Bake Ambient Occlusion (`bake ao`)
- **Command pattern:** `./bin/texturecraft-cli run --cmd 'bake ao' --params '{size: 1024}'
- **Result:** 1024x1024 AO map generated
- **Status:** ✅ Pass

### 5. Cylindrical Projection (`project cylindrical`)
- **Command pattern:** `./bin/texturecraft-cli run --cmd 'project cylindrical' --params '{unwrap: true}'
- **Result:** Cylindrical projection applied to texture
- **Status:** ✅ Pass

### 6. Spherical Projection (`project spherical`)
- **Command pattern:** `./bin/texturecraft-cli run --cmd 'project spherical' --params '{unwrap: true}'
- **Result:** Spherical (full dome) projection applied
- **Status:** ✅ Pass

### 7. Export T-Craft (`export tcraft`)
- **Command pattern:** `./bin/texturecraft-cli run --cmd 'export tcraft' --params '{path: "/tmp/test.tcraft"}`
- **Result:** Native .tcraft format with all layers preserved
- **Status:** ✅ Pass

### 8. Export PNG (`export png`)
- **Command pattern:** `./bin/texturecraft-cli run --cmd 'export png' --params '{path: "/tmp/test.png", bit_depth: 16}'
- **Result:** 16-bit PNG with alpha channel
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From TextureCraft | To App | Method |
|---|---|---|
| Exported .tcraft | SolidCraft | `part.export format: STEP` then texture |
| Normal map | LightCraft | Import as texture map |
| PNG texture | PhotoCraft | `doc.place` for layering |
| Projected map | VectorCraft | Bump map conversion from height data |