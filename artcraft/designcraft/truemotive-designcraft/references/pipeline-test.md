# TrueMotive DesignCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** smoke.pdf, smoke.png, smoke2.pdf, smoke2.png (in artifacts-test/designcraft/)

## Pipeline Configuration 1: Command Listing

**Command:** `designcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/designcraft-cli commands
```

**Result:** Lists design commands for graphic design, assets, and style management.

**Verification:** Command array returned successfully with expected categories (file, edit, effects, etc.).

**Notes:**
- Command IDs follow the pattern `command.family.subcommand`
- Style inheritance flags documented via `inherits_last_style`
- Full parameter shapes available via `describe <id>`