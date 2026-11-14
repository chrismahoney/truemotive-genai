# PdfCraft command quick reference

**Pack version:** 0.8.0 (2026-11-14)
**Source:** `pdfcraft-cli commands` via internal registry (task-shaped CLI, no command registry).
**Lint note:** No dotted command IDs; bare task words. `lint.py --app pdfcraft` validation is trivially satisfied.

## Session Management / Batch

| Command | Params |
|---|---|
| `batch <files or dirs...> --steps convert,ocr,optimize --out-dir DIR` | `[--recursive] [--root DIR] [--stop-on-error] [--ppi 150] [--quality 60] [--dpi 300] [--language en] [--ocr-all-pages]` |
| `mcp [--root DIR] [--compact] [--automation-read-root DIR] [--automation-write-root DIR]` | MCP server on stdin/stdout; `--compact` lists core set plus `tool_search` and `tool_call`; `--automation-read-root`/`--automation-write-root` confine file access |

## Document Operations

| Command | Params |
|---|---|
| `info <file.pdf> [--password PW]` | document summary as JSON (includes any declared PDF/A or PDF/UA level) |
| `render <file.pdf> --page N --dpi 96 --out x.png` | (.png, .jpg, .tif or .pam) |
| `text <file.pdf> [--page N]` | extracted text (pages separated by form feeds) |
| `edit <in.pdf> --out out.pdf [--rotate 1,3:90] [--delete 2,4] [--move 5:1] [--insert-blank 1] [--title T] [--author A] [--full]` | options run in order; page numbers refer to the document after the earlier options |
| `combine <a.pdf> <b.pdf> … --out combined.pdf` | — |
| `extract <in.pdf> --pages 1,3,5-8 --out out.pdf` | pages and ranges, in the order given |
| `split <in.pdf> (--every N | --before 3,7) [--out-dir DIR]` | — |

## Document Analysis

| Command | Params |
|---|---|
| `check <files or dirs...> [--timeout 20] [--dpi 36] [--json out.json]` | — |
| `audit <file.pdf> [--password PW]` | find faux redactions (fails when found) |

## Tools & MCP

| Command | Params |
|---|---|
| `tools` | automation tools and their JSON Schemas |
| `run <tool> [key=value …] [--root DIR] [--out image.png]` | — |
| `run --script steps.json [--root DIR] [--report]` | — |
| `ui --control FILE <method> [key=value …] [--out shot.png]` | drive a running app started with `--control FILE` |

## Project conventions (AntiVoxel)

- Prefer headless CLI for file output; touch a user's live window only through that app's own control port.
- Check `ps aux | grep -i pdfcraft` before assuming a GUI is running.
- Dump a registry once to the scratchpad and filter it; never print a whole one.
- Verify output by viewing the image or reading the JSON, then report paths and warnings.
- Project files are written with the editor tools (Write and Edit), with each result checked; there is no per-write size limit (AGENTS.md amendment, 2026-11-14).