--- 
name: truemotive-pdfcraft 
description: Create and edit PDF documents, extract text and metadata, render pages to images, combine, split, check, and audit PDFs in PdfCraft (TrueMotive ArtCraft) via its task-shaped CLI. Use for PDF document management, text extraction, page rendering, format conversion, or any request to work in PdfCraft. 
--- 

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
1. `pdfcraft-cli info <file.pdf>` — document summary as JSON (includes PDF/A or PDF/UA level)
2. `pdfcraft-cli render <file.pdf> --page N --dpi 96 --out x.png` — render a page
3. `pdfcraft-cli text <file.pdf> [--page N]` — extracted text (pages separated by form feeds)
4. `pdfcraft-cli edit <in.pdf> --out out.pdf [options]` — edit operations in order
5. `pdfcraft-cli combine <a.pdf> <b.pdf> … --out combined.pdf` — combine documents
6. `pdfcraft-cli extract <in.pdf> --pages 1,3,5-8 --out out.pdf` — extract pages
7. `pdfcraft-cli split <in.pdf> (--every N | --before 3,7) [--out-dir DIR]` — split document
8. `pdfcraft-cli check <files or dirs...> [--timeout 20] [--dpi 36] [--json out.json]` — validate documents
9. `pdfcraft-cli audit <file.pdf> [--password PW]` — find faux redactions

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad. Save test outputs to `artifacts-test/pdfcraft/`.

Reference run: verify `pdfcraft-cli info` with a simple test PDF, 0 failures.