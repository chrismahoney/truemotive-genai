# TrueMotive SolidCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.7.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | Full solid command catalog |
| `session.run` | ✅ Runs design script | JSON results, saves and inspects |
| `sketch.create` | ✅ Creates new sketch | Plane: XY/XZ/YZ, origin, x_dir, y_dir |
| `part.features` | ✅ Adds features | Extrude, revolve, loft, rib, hole, pattern |
| `part.export` | ✅ Exports format | STL, OBJ, STEP, 3MF formats |
| `session.save` | ✅ Saves design | `.sc` design format persisted |

## Verified Operations

### 1. Run Design Script (`session.run`)
- **Command pattern:** `./bin/solidcraft-cli run <script.json>`
- **Result:** JSON results output, design saved and inspected
- **Status:** ✅ Pass

### 2. Create Sketch (`sketch.create`)
- **Command pattern:** `./bin/solidcraft-cli run --cmd 'sketch.create' --params '{plane: "XY", origin: [0,0,0], x_dir: [1,0,0], y_dir: [0,1,0], name: "base"}`
- **Result:** New sketch created on XY plane
- **Status:** ✅ Pass

### 3. Add Features (`part.features`)
- **Command pattern:** `./bin/solidcraft-cli run --cmd 'part.features' --params '{feature: "extrude", height: 50}'
- **Result:** Extruded feature added to design
- **Status:** ✅ Pass

### 4. Export Format (`part.export`)
- **STL export:** `./bin/solidcraft-cli run --cmd 'part.export' --params '{format: "STL", quality: "fine"}`
- **Result:** STL file exported with fine quality
- **Status:** ✅ Pass

### 5. Export OBJ (`part.export obj`)
- **Command pattern:** `./bin/solidcraft-cli run --cmd 'part.export' --params '{format: "OBJ"}`
- **Result:** OBJ file exported
- **Status:** ✅ Pass

### 6. Export STEP (`part.export step`)
- **Command pattern:** `./bin/solidcraft-cli run --cmd 'part.export' --params '{format: "STEP", quality: "standard"}`
- **Result:** STEP file exported
- **Status:** ✅ Pass

### 7. Save Design (`session.save`)
- **Command pattern:** `./bin/solidcraft-cli run --cmd 'session.save'`
- **Result:** Design saved as `.sc` format
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From SolidCraft | To App | Method |
|---|---|---|
| Exported STL | VectorCraft | `import.step` or `imageTrace.make` |
| Exported OBJ | PhotoCraft | `doc.place` for texturing |
| Exported STEP | All apps | Neutral format for interop |
| `.sc` design | AniCraft | Export keyframe data from feature history |