# TrueMotive VectorCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** (artifacts-test/vectorcraft/ - truchet tilings to be generated)

## Pipeline Configuration 1: Command Listing

**Command:** `vectorcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/vectorcraft-cli commands
```

**Result:** Lists vector commands for path-based art, SVG generation, and geometric patterns.

**Verification:** Command array returned successfully with expected categories (path, shape, text, export, etc.).

**Notes:**
- Path commands: `path.new`, `path.add`, `path.features`
- Shape generators: `spiro`, `lsystem`, `tiling`
- Text commands: `text.set`, `text.convert`
- Export formats: SVG, PDF, PNG