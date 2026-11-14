# TrueMotive PdfCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.8.0
**Test files used (filename only):** (existing smoke PDFs from artifacts-test/)

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/pdfcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/PdfCraft.app/Contents/MacOS/PdfCraft` |
| Protocol doc | none (CLI help is the source of truth) |

## Choose a session

| Need | Use |
|---|---|
| One PDF file to operate on | `pdfcraft-cli <command> <file.pdf> [options]` (prints JSON results, then bounces, saves and inspects) |
| Many files batched | `pdfcraft-cli batch <files or dirs...> --steps convert,ocr,optimize --out-dir DIR` |
| Agent tool calls | `pdfcraft-cli mcp` (headless) or `mcp --bridge 127.0.0.1:PORT --control-token-file F` (live app) |
| The user's open window | Desktop `PdfCraft --control PORT --control-token-file F`. A headless session never edits it. |

## Discover commands, don't guess

`pdfcraft-cli commands` (via internal registry) returns a list of task subcommands. `params` is a doc-string with types, ranges, and defaults. Dump it once to the scratchpad and filter it with `python3 -I`; never print a whole one.

Standard flow:
1. `pdfcraft-cli info <file.pdf>` — document summary as JSON (includes any declared PDF/A or PDF/UA level)
2. `pdfcraft-cli render <file.pdf> --page N --dpi 96 --out x.png` — render a page
3. `pdfcraft-cli text <file.pdf> [--page N]` — extracted text (pages separated by form feeds)
4. `pdfcraft-cli edit <in.pdf> --out out.pdf [options]` — edit operations in order
5. `pdfcraft-cli combine <a.pdf> <b.pdf> … --out combined.pdf` — combine documents
6. `pdfcraft-cli extract <in.pdf> --pages 1,3,5-8 --out out.pdf` — extract pages
7. `pdfcraft-cli split <in.pdf> (--every N | --before 3,7) [--out-dir DIR]` — split document
8. `pdfcraft-cli check <files or dirs...> [--timeout 20] [--dpi 36] [--json out.json]` — validate documents
9. `pdfcraft-cli audit <file.pdf> [--password PW]` — find faux redactions

## Standard flow (AntiVoxel)

- Prefer headless CLI for file output; touch a user's live window only through that app's own control port.
- Check `ps aux | grep -i pdfcraft` before assuming a GUI is running.
- Dump a registry once to the scratchpad and filter it; never print a whole one.
- Verify output by viewing the image, then report paths and warnings.
- Project files are written with the editor tools (Write and Edit), with each result checked; there is no per-write size limit (AGENTS.md amendment, 2026-11-14).

## Cross-app hand-offs

| From PdfCraft | To App | Method |
|---|---|---|
| Rendered PNG | PhotoCraft | `doc.place` for image layer |
| Extracted text | WordCraft | Data for document workflow |
| Check/validation JSON | EffectCraft | Process metadata |
| Combined PDF | All apps | Interop format |

## Save

| Command | Description |
|---|---|
| `pdfcraft-cli info <file.pdf>` — document summary as JSON |
| `pdfcraft-cli render <file.pdf> --page 1 --dpi 96 --out x.png` — render a page |
| `pdfcraft-cli text <file.pdf>` — extracted text |
| `pdfcraft-cli check <file.pdf>` — validation result |
| `pdfcraft-cli audit <file.pdf>` — faux redactions located |