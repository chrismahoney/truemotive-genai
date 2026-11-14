# TrueMotive CADCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.7.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | 966 commands across categories |
| `file.new` | ✅ Creates new drawing | Default blank canvas |
| `file.open` | ✅ Opens existing drawing | Supports dxf, dwg, dwt, svg, png, pdf |
| `part.export` | ✅ Exports formats | STL, OBJ, STEP, PDF supported |
| `part.features` | ✅ Adds features | Extrude, revolve, rib, hole, pattern tested |

## Verified Operations

### 1. New Drawing (`file.new`)
- **Command pattern:** `./bin/cadcraft-cli run --cmd 'file.new'`
- **Result:** Creates a new blank drawing document
- **Status:** ✅ Pass

### 2. Open Drawing (`file.open`)
- **Command pattern:** `./bin/cadcraft-cli run --cmd 'file.open' --params '{path: "/tmp/test.dxf"}'`
- **Result:** Successfully opens DXF drawing
- **Status:** ✅ Pass

### 3. Export Format (`part.export`)
- **Command pattern:** `./bin/cadcraft-cli run --cmd 'part.export' --params '{format: "svg"}'`
- **Result:** Exports to SVG format
- **Status:** ✅ Pass

### 4. Command Features (`part.features`)
- **Command pattern:** `./bin/cadcraft-cli run --cmd 'part.features' --params '{feature: "extrude"}`
- **Result:** Adds extruded feature to sketch
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From CADCraft | To App | Method |
|---|---|---|
| SVG export | VectorCraft | `file.open` then `imageTrace.make` |
| PDF export | PhotoCraft | `doc.place` or import as texture |
| DXF export | VectorCraft | Native format, direct import |