# TrueMotive EffectCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** smoke.ecproj, smoke.png (in artifacts-test/effectcraft/)

## Pipeline Configuration 1: Command Listing

**Command:** `effectcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/effectcraft-cli commands
```

**Result:** Lists effect commands for audio and video processing, effect chains, and conversion.

**Verification:** Command array returned successfully with expected categories (effects, conversion, batch, etc.).

**Notes:**
- Effect chain parameters documented per command
- Conversion options: resample, normalize, bitdepth
- Batch mode via `serve` JSON lines pipeline