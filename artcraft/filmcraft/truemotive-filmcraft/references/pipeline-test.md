# TrueMotive FilmCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** clip.mp4, frame.png (in artifacts-test/filmcraft/)

## Pipeline Configuration 1: Command Listing

**Command:** `filmcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/filmcraft-cli commands
```

**Result:** Lists film commands for video editing, sequences, and audio integration.

**Verification:** Command array returned successfully with expected categories (file, edit, effects, export, etc.).

**Notes:**
- Sequence commands: `file.newSequence`, `file.import_sequence`
- Audio commands: `file.import_audio`, `file.export_mix`
- Timeline operations: `timeline well-known commands`