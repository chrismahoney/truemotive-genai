# TrueMotive LightCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.7.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | Full light command catalog |
| `project.new` | ✅ Creates new project | Blank lighting project |
| `project.save` | ✅ Saves project | `.lcproject` format |
| `render.cli` | ✅ Renders image | Tested with voronoi pattern |
| `bake diffuse` | ✅ Bakes diffuse map | Generated texture map |
| `bake normal` | ✅ Bakes normal map | Normal map output verified |

## Verified Operations

### 1. New Project (`project.new`)
- **Command pattern:** `./bin/lightcraft-cli run --cmd 'project.new'`
- **Result:** Creates new lighting project
- **Status:** ✅ Pass

### 2. Save Project (`project.save`)
- **Command pattern:** `./bin/lightcraft-cli run --cmd 'project.save' --params '{path: "/tmp/test.lcproject"}`
- **Result:** Project saved successfully
- **Status:** ✅ Pass

### 3. Render Image (`render.cli`)
- **Command pattern:** `./bin/lightcraft-cli run --cmd 'render.cli' --params '{width: 1920, height: 1080}'
- **Result:** Rendered image output
- **Status:** ✅ Pass

### 4. Bake Diffuse Map (`bake diffuse`)
- **Command pattern:** `./bin/lightcraft-cli run --cmd 'bake diffuse' --params '{size: 1024}'
- **Result:** Diffuse texture map baked
- **Status:** ✅ Pass

### 5. Bake Normal Map (`bake normal`)
- **Command pattern:** `./bin/lightcraft-cli run --cmd 'bake normal' --params '{size: 1024}'
- **Result:** Normal map baked
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From LightCraft | To App | Method |
|---|---|---|
| Rendered image | PhotoCraft | `doc.place` for texturing |
| Diffuse map | EffectCraft | Process via `effects.chain` |
| Normal map | VectorCraft | Bump map conversion |