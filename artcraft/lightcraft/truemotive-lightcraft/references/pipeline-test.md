# TrueMotive LightCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** demo-lc.jpg, voronoi-lc.jpg (in artifacts-test/lightcraft/)

## Pipeline Configuration 1: Command Listing

**Command:** `lightcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/lightcraft-cli commands
```

**Result:** Lists light commands for 3D lighting, ray tracing, and atmospheric effects.

**Verification:** Command array returned successfully with expected categories (render, bake, project, etc.).

**Notes:**
- Render commands: `render.cli`, `render.bucket`
- Bake commands: `bake.diffuse`, `bake.normal`
- Project commands: `project.new`, `project.save`