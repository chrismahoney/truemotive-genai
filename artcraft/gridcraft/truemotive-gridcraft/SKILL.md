---
name: truemotive-gridcraft
description: Build, calculate and convert spreadsheets - cells, formulas, ranges, tables, charts, pivots, sorting, filtering, number formats - in GridCraft (TrueMotive ArtCraft) through its headless CLI or MCP server, and read or write XLSX, CSV, TSV, JSON, HTML and PDF. Use for budgets and metrics tables, evaluating formulas, converting or checking workbooks, or any request to work in GridCraft.
---

# TrueMotive GridCraft

Spreadsheet app in the ArtCraft suite (385 commands, checked 2026-11-14): workbooks with sheets, cells and formulas, ranges, tables, charts, pivots, data tools. XLSX by default; reads and writes CSV, TSV, JSON, HTML and PDF. For documents use WordCraft; for slides DeckCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/gridcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/GridCraft.app/Contents/MacOS/GridCraft` |
| Protocol doc | none installed |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| Build a workbook (best default) | `gridcraft-cli run [--in FILE \| --sample NAME] --cmd 'ID={json}'... [--script FILE.jsonl] [--out FILE] [--print RANGE] [--quiet]`. A script line is `id={json}` or `{"command": ID, "params": {...}}`; blank lines and lines starting `#` or `//` are skipped. `--out` picks the format by extension. Verified. |
| Evaluate a formula | `gridcraft-cli eval FORMULA [--in FILE] [--sheet S] [--cell A1] [--json]` (verified: `=SUM(B2:B3)*2` gave 3300.0) |
| Read cells | `gridcraft-cli cat FILE [--range A1:D20] [--sheet S] [--formulas] [--csv]` |
| Convert | `gridcraft-cli convert IN OUT [--sheet NAME]` for `xlsx csv tsv json html pdf` (verified to csv, html, pdf and json) |
| Check | `gridcraft-cli check FILE-OR-DIR... [--json] [--tolerance T]`: recomputes cached formula values and checks the XLSX round trip; exit 1 on any difference (verified) |
| Inspect | `gridcraft-cli info FILE [--json]`; `gridcraft-cli functions [--json] [--search X] [--category C]` lists spreadsheet functions |
| Agent tool calls | `gridcraft-cli mcp [--connect PORT] [--in FILE \| --sample NAME]` (not yet run); `send PORT METHOD [json]` calls a running app |

`--sample` takes `budget`, `sales` or `grades`. Each `run` is its own session: use `--out` to keep the result.

## Discover shapes, don't guess

Use `artcraft-find QUERY --app gridcraft` or `gridcraft-cli commands [--json] [--search X]` (the `--json` form has parameters but no native `mutates` flag, so `find.py --readonly` is a name-based guess here). Families: `home` 64, `data` 41, `formulas` 32, `view` 30, `edit` 26, `pivot` 22, `review` 21, `insert` 20, `pageLayout` 16, `table` 14, `file` 13, `chart` 12, `sheet` 10, `macro` 9.

## Editing model and standard flow

Cells addressed by A1 references; most commands take a `range` or `cell` and fall back to the current selection or active cell (session state).

1. `file.new {sample?}` or `--in FILE` (a plain `run` starts a new workbook)
2. `cell.set {cell: "B2", input: "text, number or =formula", sheet?, array?}`, or `range.setValues` for blocks
3. Format: `home.bold {range, on}`, number formats, fills, borders, tables, charts
4. `--print RANGE` shows the computed values; `cat --formulas` shows formulas
5. `--out F.xlsx`, `convert` to other formats, `check`, and read the result back

**Verified (artifacts-test/gridcraft):** a 4-row budget with `=SUM(B2:B3)` and a bold header row saved as XLSX (4.2 KB, 10 ZIP entries); `--print A1:B4` showed Total 1650; `cat --formulas` showed `=SUM(B2:B3)`; `eval` 3300.0; `convert` wrote CSV (44 B), HTML, a one-page PDF and JSON; `check` reported 1 formula cell matched and 0 of 1 files differing. There is no image output, so verify through `cat`, `--print` and `check` (plus `artcraft-qa` on the files).

## Procedural and generative notes

GridCraft is the natural home for generated tables: loops of `cell.set` or `range.setValues`, formulas for derived columns, `chart.*` for plots (not yet run), and `convert --sheet` to export one sheet. It has no path or image commands.

## Save, export, verify

`file.save {path?}` (XLSX by default; `.csv .tsv .json .html .pdf` by extension), `file.exportCsv`, `file.exportHtml`, `file.exportPdf`. Always run `check` on a workbook another tool will read.

## Cross-app hand-offs

- Benchmark metrics into a GridCraft sheet, then a chart or table into a WordCraft report or DeckCraft slide: not yet run. See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- CSV, JSON and HTML out are plain text for any other app.

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/gridcraft/`.
