# TrueMotive PdfCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.8.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | Task-shaped subcommand catalog |
| `info <file.pdf>` | ✅ Document summary | JSON output with PDF/A or PDF/UA level |
| `render <file.pdf> --page 1` | ✅ Page render to PNG | Tested with existing smoke PDF |
| `text <file.pdf>` | ✅ Text extraction | Pages separated by form feeds |
| `check <file.pdf>` | ✅ Document validation | Validation result JSON |
| `audit <file.pdf>` | ✅ Faux redaction audit | Finds faux redactions |
| `combine <a.pdf> <b.pdf> --out combined.pdf` | ✅ Document combination | Combined PDF generated |
| `extract <in.pdf> --pages 1,3 --out out.pdf` | ✅ Page extraction | Extracted pages saved |
| `split <in.pdf> --every 2 --out-dir DIR` | ✅ Document split | Split outputs generated |
| `batch <files> --steps convert --out-dir DIR` | ✅ Batch processing | Batch completed successfully |

## Verified Operations

### 1. Document Info (`info`)
- **Command pattern:** `./bin/pdfcraft-cli info <file.pdf>`
- **Result:** JSON summary with PDF/A or PDF/UA level
- **Status:** ✅ Pass

### 2. Render Page (`render`)
- **Command pattern:** `./bin/pdfcraft-cli render <file.pdf> --page 1 --dpi 96 --out /tmp/out.png`
- **Result:** PNG output at specified DPI
- **Status:** ✅ Pass

### 3. Text Extraction (`text`)
- **Command pattern:** `./bin/pdfcraft-cli text <file.pdf>`
- **Result:** Extracted text with form feed separators
- **Status:** ✅ Pass

### 4. Document Check (`check`)
- **Command pattern:** `./bin/pdfcraft-cli check <file.pdf>`
- **Result:** Validation JSON output
- **Status:** ✅ Pass

### 5. Audit (`audit`)
- **Command pattern:** `./bin/pdfcraft-cli audit <file.pdf>`
- **Result:** Faux redactions located (if any)
- **Status:** ✅ Pass

### 6. Combine Documents (`combine`)
- **Command pattern:** `./bin/pdfcraft-cli combine file1.pdf file2.pdf --out combined.pdf`
- **Result:** Combined PDF generated
- **Status:** ✅ Pass

### 7. Extract Pages (`extract`)
- **Command pattern:** `./bin/pdfcraft-cli extract <in.pdf> --pages 1,3 --out out.pdf`
- **Result:** Pages 1 and 3 extracted to new PDF
- **Status:** ✅ Pass

### 8. Split Document (`split`)
- **Command pattern:** `./bin/pdfcraft-cli split <in.pdf> --every 2 --out-dir DIR`
- **Result:** Document split into every-other-page PDFs
- **Status:** ✅ Pass

### 9. Batch Processing (`batch`)
- **Command pattern:** `./bin/pdfcraft-cli batch <files> --steps convert,ocr --out-dir DIR`
- **Result:** Batch conversion/OCR completed
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From PdfCraft | To App | Method |
|---|---|---|
| Rendered PNG | PhotoCraft | `doc.place` for image layer |
| Extracted text | WordCraft | Data for document workflow |
| Check/validation JSON | EffectCraft | Process metadata |
| Combined PDF | All apps | Interop format |