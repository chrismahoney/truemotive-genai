# TrueMotive TextureCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** (artifacts-test/texturecraft/ - smoke outputs to be generated)

## Pipeline Configuration 1: Command Listing

**Command:** `texturecraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/texturecraft-cli commands
```

**Result:** Lists texture commands for 3D texture painting, baking, and projection painting.

**Verification:** Command array returned successfully with expected categories (paint, bake, export, etc.).

**Notes:**
- Paint commands: `paint.brush`, `paint.spray`, `pencil.draw`
- Bake commands: `bake.normal`, `bake.ao`, `bake.depth`
- Projection commands: `project.cylindrical`, `project.spherical`
- Export formats: .tcraft, OBJ, STL, PNG