# TrueMotive CADCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** (smoke test outputs in artifacts-test/cadcraft/)

## Pipeline Configuration 1: Command Listing

**Command:** `cadcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/cadcraft-cli commands
```

**Result:** Lists CAD commands for 2D drafting, formats, and roundtrip operations.

**Verification:** Command array returned successfully with expected categories (draw, edit, export, etc.).

**Notes:**
- Command IDs follow the pattern `command.category.subcommand`
- Full parameter shapes available via `describe <id>`