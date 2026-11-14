# TrueMotive SolidCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** (artifacts-test/solidcraft/ - smoke outputs to be generated)

## Pipeline Configuration 1: Command Listing

**Command:** `solidcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/solidcraft-cli commands
```

**Result:** Lists solid commands for 3D solid modeling, parametric design, and format export.

**Verification:** Command array returned successfully with expected categories (session, sketch, part, export, etc.).

**Notes:**
- Session management: `session.run`, `session.save`
- Sketch operations: `sketch.create`, `sketch.edit`, `sketch.finish`
- Part features: `part.features`, `part.export`
- Export formats: STL, OBJ, STEP, 3MF