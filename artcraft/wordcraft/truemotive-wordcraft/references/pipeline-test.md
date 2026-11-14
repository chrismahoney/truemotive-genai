# TrueMotive WordCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** smoke.docx, smoke.pdf, smoke.png (in artifacts-test/wordcraft/)

## Pipeline Configuration 1: Command Listing

**Command:** `wordcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/wordcraft-cli commands
```

**Result:** Lists word commands for document creation, editing, and formatting.

**Verification:** Command array returned successfully with expected categories (file, edit, format, etc.).

**Notes:**
- File commands: `file.new`, `file.open`, `file.save`, `file.export`
- Edit commands: `edit.undo`, `edit.redo`, `edit.cut`, `edit.copy`, `edit.paste`
- Format commands: `format.font`, `format.size`, `format.bold`, `format.italic`
- Export formats: .docx, .pdf, .png, .txt