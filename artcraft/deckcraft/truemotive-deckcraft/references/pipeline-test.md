# TrueMotive DeckCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** smoke.deckcraft, smoke.pdf, smoke.png (in artifacts-test/deckcraft/)

## Pipeline Configuration 1: Command Listing

**Command:** `deckcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/deckcraft-cli commands
```

**Result:** Lists deck commands for presentation creation, templates, and exports.

**Verification:** Command array returned successfully with expected categories (file, edit, export, etc.).

**Notes:**
- Command IDs follow the pattern `command.family.subcommand`
- Full parameter shapes available via `describe <id>`
- Templates available via `file.templates`