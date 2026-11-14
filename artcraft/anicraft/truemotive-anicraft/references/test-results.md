# TrueMotive AniCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.7.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | Full animation command catalog |
| `timeline.new` | ✅ Creates new timeline | Blank timeline ready for keyframes |
| `timeline.add` | ✅ Adds keyframe | Timeline position, value parameters |
| `keyframe.set` | ✅ Sets keyframe value | Parameter interpolation |
| `export gif` | ✅ Exports GIF | Frame sequence to GIF |
| `export mp4` | ✅ Exports MP4 | Video format export |
| `export png seq` | ✅ Exports PNG sequence | Individual frames as PNG |

## Verified Operations

### 1. New Timeline (`timeline.new`)
- **Command pattern:** `./bin/anicraft-cli run --cmd 'timeline.new'`
- **Result:** Creates new blank timeline
- **Status:** ✅ Pass

### 2. Add Keyframe (`timeline.add`)
- **Command pattern:** `./bin/anicraft-cli run --cmd 'timeline.add' --params '{track: "anim", position: 0, value: 100}'
- **Result:** Keyframe added at timeline position 0
- **Status:** ✅ Pass

### 3. Set Keyframe (`keyframe.set`)
- **Command pattern:** `./bin/anicraft-cli run --cmd 'keyframe.set' --params '{param: "opacity", value: 0.5}'
- **Result:** Keyframe value set to 0.5
- **Status:** ✅ Pass

### 4. Export GIF (`export gif`)
- **Command pattern:** `./bin/anicraft-cli run --cmd 'export gif' --params '{out: "/tmp/test.gif", duration: 1}'
- **Result:** GIF exported from animation sequence
- **Status:** ✅ Pass

### 5. Export MP4 (`export mp4`)
- **Command pattern:** `./bin/anicraft-cli run --cmd 'export mp4' --params '{out: "/tmp/test.mp4", fps: 30}'
- **Result:** MP4 video exported
- **Status:** ✅ Pass

### 6. Export PNG Sequence (`export png seq`)
- **Command pattern:** `./bin/anicraft-cli run --cmd 'export png seq' --params '{out: "/tmp/frames/", prefix: "frame"}`
- **Result:** Individual PNG frames exported
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From AniCraft | To App | Method |
|---|---|---|
| Exported GIF | FilmCraft | `file.import_audio` for sync |
| Exported MP4 | PhotoCraft | Import as texture or sequence |
| Animation timeline | LightCraft | Keyframe data for lighting rigs |
| Frame PNGs | VectorCraft | Individual frames as SVG traces |