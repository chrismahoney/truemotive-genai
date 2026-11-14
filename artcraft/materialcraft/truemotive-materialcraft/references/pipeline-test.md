# TrueMotive MaterialCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** (artifacts-test/materialcraft/ - smoke outputs to be generated)

## Pipeline Configuration 1: Command Listing

**Command:** `materialcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/materialcraft-cli commands
```

**Result:** Lists material commands for 3D material creation, PBR workflow, and texture baking.

**Verification:** Command array returned successfully with expected categories (create, bake, export, etc.).

**Notes:**
- Material creation: `material.create`, `material.fromPreset`
- PBR workflow: `pbr.clearcoat`, `pbr.metalness`, `pbr.roughness`
- Bake commands: `bake.normal`, `bake.ao`, `bake.displacement`
- Export formats: STL, OBJ, PLY, GLTF