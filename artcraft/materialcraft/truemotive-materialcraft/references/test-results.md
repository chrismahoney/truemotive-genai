# TrueMotive MaterialCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.7.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | Full material command catalog |
| `material.create` | ✅ Creates new material | Default PBR material |
| `pbr.metalness` | ✅ Sets metalness value | 0.0 to 1.0 range |
| `pbr.roughness` | ✅ Sets roughness value | 0.0 to 1.0 range |
| `bake normal` | ✅ Bakes normal map | 1024x1024 output |
| `bake ao` | ✅ Bakes ambient occlusion | 1024x1024 output |
| `export obj` | ✅ Exports OBJ format | Material libraries included |
| `export gltf` | ✅ Exports GLTF format | Embedded textures |

## Verified Operations

### 1. Create Material (`material.create`)
- **Command pattern:** `./bin/materialcraft-cli run --cmd 'material.create'`
- **Result:** Creates default PBR material
- **Status:** ✅ Pass

### 2. Set Metalness (`pbr.metalness`)
- **Command pattern:** `./bin/materialcraft-cli run --cmd 'pbr.metalness' --params '{metalness: 0.5}'
- **Result:** Metalness set to 0.5 (half-metallic)
- **Status:** ✅ Pass

### 3. Set Roughness (`pbr.roughness`)
- **Command pattern:** `./bin/materialcraft-cli run --cmd 'pbr.roughness' --params '{roughness: 0.8}'
- **Result:** Roughness set to 0.8 (mostly smooth)
- **Status:** ✅ Pass

### 4. Bake Normal Map (`bake normal`)
- **Command pattern:** `./bin/materialcraft-cli run --cmd 'bake normal' --params '{size: 1024}'
- **Result:** 1024x1024 normal map generated
- **Status:** ✅ Pass

### 5. Bake AO (`bake ao`)
- **Command pattern:** `./bin/materialcraft-cli run --cmd 'bake ao' --params '{size: 1024}'
- **Result:** 1024x1024 ambient occlusion map generated
- **Status:** ✅ Pass

### 6. Export OBJ (`export obj`)
- **Command pattern:** `./bin/materialcraft-cli run --cmd 'export obj' --params '{path: "/tmp/test.obj"}`
- **Result:** OBJ file with material libraries
- **Status:** ✅ Pass

### 7. Export GLTF (`export gltf`)
- **Command pattern:** `./bin/materialcraft-cli run --cmd 'export gltf' --params '{path: "/tmp/test.gltf"}`
- **Result:** GLTF 2.0 with embedded textures
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From MaterialCraft | To App | Method |
|---|---|---|
| Exported STL | SolidCraft | `part.export format: STL` |
| PBR textures | LightCraft | Baked maps imported as textures |
| GLTF model | VectorCraft | 3D model import for further editing |