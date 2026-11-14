# TrueMotive AniCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** anim.anicraft, anim.gif, frame6.png (in artifacts-test/anicraft/)

## Pipeline Configuration 1: Command Listing

**Command:** `anicraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/anicraft-cli commands
```

**Result:** Lists animation commands for timeline-based editing, keyframe operations, and GIF generation.

**Verification:** Command array returned successfully with expected categories (timeline, keyframe, export, etc.).

**Notes:**
- Timeline commands: `timeline.new`, `timeline.add`, `timeline.remove`
- Keyframe operations: `keyframe.set`, `keyframe.interpolate`
- Export formats: GIF, MP4, PNG sequence