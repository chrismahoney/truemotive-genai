# TrueMotive GridCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** smoke.csv, smoke.html, smoke.json, smoke.pdf, smoke.xlsx (in artifacts-test/gridcraft/)

## Pipeline Configuration 1: Command Listing

**Command:** `gridcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/gridcraft-cli commands
```

**Result:** Lists grid commands for spreadsheet/doc creation, data operations, and grid-based design.

**Verification:** Command array returned successfully with expected categories (file, edit, data, export, etc.).

**Notes:**
- Data commands: `activity.list`, `activity.cancel`
- File operations: `file.new`, `file.open`
- Export formats: PDF, HTML, XLSX, JSON