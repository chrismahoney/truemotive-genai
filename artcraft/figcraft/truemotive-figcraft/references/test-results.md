# TrueMotive FigCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.7.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | Full figure command catalog |
| `node.create` | ✅ Creates new node | Rectangle, ellipse, polygon, star, line, arrow, text, path |
| `frame.create` | ✅ Creates new frame | Parent frame, index, name |
| `select-test` | ✅ Selection operations | Select/deselect, group, ungroup |
| `probe` | ✅ Inspect command | JSON output of command details |

## Verified Operations

### 1. Create Node (`node.create`)
- **Command pattern:** `./bin/figcraft-cli run --cmd 'node.create' --params '{type: "rectangle", x: 100, y: 100, width: 200, height: 200}'
- **Result:** Rectangle node created on canvas
- **Status:** ✅ Pass

### 2. Create Frame (`frame.create`)
- **Command pattern:** `./bin/figcraft-cli run --cmd 'frame.create' --params '{parent: "page1", index: 0, name: "frame-1"}`
- **Result:** New frame created on page
- **Status:** ✅ Pass

### 3. Selection Operations (`select-test`)
- **Command pattern:** `./bin/figcraft-cli run --cmd 'select-test'`
- **Result:** Selection test pattern verified
- **Status:** ✅ Pass

### 4. Probe Command (`probe`)
- **Command pattern:** `./bin/figcraft-cli describe node.create`
- **Result:** JSON output with command parameters
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From FigCraft | To App | Method |
|---|---|---|
| Exported figure | VectorCraft | SVG export, then `file.open` |
| Figure to image | PhotoCraft | PNG export, then `doc.place` |
| Node structure | CADCraft | Vector paths exported as DXF |