# TrueMotive PdfCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.8.0
**Test files used (filename only):** (existing smoke PDFs from artifacts-test/)

## Pipeline Configuration 1: Command Listing

**Command:** `pdfcraft-cli commands`

**Test:** List all available task subcommands

```bash
./bin/pdfcraft-cli commands
```

**Result:** Lists pdf commands for PDF document management, rendering, text extraction, editing, and batch operations.

**Verification:** Command array returned successfully with expected categories (info, render, text, edit, combine, etc.).

**Notes:**
- Task-shaped CLI: no command registry; subcommands are verb-noun phrases
- Render outputs: .png, .jpg, .tif, or .pam
- Batch steps: convert,ocr,optimize