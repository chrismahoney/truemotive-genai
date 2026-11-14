# TrueMotive DeckCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.7.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | 966 commands across categories |
| `file.new` | ✅ Creates new presentation | Default blank canvas |
| `file.templates` | ✅ Lists starter templates | budget, sales, grades themes |
| `file.open` | ✅ Opens existing deck | Supports deckcraft format |
| `file.export` | ✅ Exports to PDF | PDF output verified |

## Verified Operations

### 1. New Presentation (`file.new`)
- **Command pattern:** `./bin/deckcraft-cli run --cmd 'file.new'`
- **Result:** Creates a new blank presentation
- **Status:** ✅ Pass

### 2. Templates (`file.templates`)
- **Command pattern:** `./bin/deckcraft-cli run --cmd 'file.templates'`
- **Result:** Lists starter templates (budget, sales, grades)
- **Status:** ✅ Pass

### 3. Open Presentation (`file.open`)
- **Command pattern:** `./bin/deckcraft-cli run --cmd 'file.open' --params '{path: "/tmp/test.deckcraft"}'`
- **Result:** Successfully opens deck file
- **Status:** ✅ Pass

### 4. Export to PDF (`file.export`)
- **Command pattern:** `./bin/deckcraft-cli run --cmd 'file.export' --params '{format: "pdf"}'`
- **Result:** Exports to PDF format
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From DeckCraft | To App | Method |
|---|---|---|
| PDF export | PhotoCraft | `doc.place` or import as texture |
| SVG export | VectorCraft | `file.open` then `imageTrace.make` |
| Presentation format | FilmCraft | Export frames for video sequence |