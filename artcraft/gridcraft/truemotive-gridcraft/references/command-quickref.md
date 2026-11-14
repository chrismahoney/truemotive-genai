# GridCraft command quick reference

Source: `gridcraft-cli commands --json` registry, 385 commands, captured 2026-11-14 (parameters yes, native `mutates` flag no). Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app gridcraft`, or `gridcraft-cli commands --search X`.

Call shape: `gridcraft-cli run --cmd 'ID={json}' ...`, or a script line `id={json}` / `{"command": ID, "params": {...}}`.

## Cells and ranges

| Command | Params |
|---|---|
| `cell.set` | `cell?: "B2", input: text, number or =formula, sheet?, array?: bool` |
| `range.setValues` | write a block of values |
| `edit.fillDown`, `edit.fillRight`, `edit.autoFill`, `edit.fillSeries` | fill |
| `edit.clearContents`, `edit.clearFormats`, `edit.clearAll` | clear |
| `edit.find`, `edit.replace`, `edit.copy`, `edit.paste`, `edit.undo`, `edit.redo` | editing |

## Formatting and formulas (home 64, formulas 32)

| Command | Params |
|---|---|
| `home.bold`, `home.italic`, `home.underline` | `range?, on?: bool` |
| `home.fontSize`, `home.fontName`, `home.fontColor`, `home.fillColor` | character and fill formatting |
| `home.alignLeft`, `home.alignCenter`, `home.alignRight`, `home.borders`, `home.formatCells` | alignment, borders, number formats |
| `formulas.autoSum`, `formulas.insertFunction`, `formulas.defineName` | formulas and names |

## Data, tables, charts, sheets, files

| Command | Params |
|---|---|
| `data.sort`, `data.sortAscending`, `data.filter`, `data.removeDuplicates`, `data.subtotal` | data tools |
| `table.style`, `table.rename`, `table.totalRow`, `table.resize` | tables |
| `chart.set`, `chart.changeType`, `chart.selectData`, `chart.move` | charts |
| `sheet.rename`, `sheet.move`, `sheet.hide`, `sheet.activate` | sheets |
| `file.new` | `sample?: "budget" \| "sales" \| "grades"` |
| `file.open`, `file.save`, `file.saveAs`, `file.close` | `file.save {path?}` (XLSX by default; csv, tsv, json, html, pdf by extension) |
| `file.exportCsv`, `file.exportHtml`, `file.exportPdf` | single-format exports |
| `view.freezePanes`, `view.freezeTopRow`, `view.zoom` | view |

## Other families

`pivot.*` (22), `review.*` (21), `insert.*` (20), `pageLayout.*` (16), `macro.*` (9).

CLI subcommands `run`, `eval`, `cat`, `convert`, `check`, `info`, `functions`, `commands`, `mcp`, `send` and `version` are not engine commands.
