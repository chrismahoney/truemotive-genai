# WordCraft command quick reference

Source: `wordcraft-cli commands --json` registry, 670 commands (each with parameter text and a native `mutates` flag), captured 2026-11-14. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app wordcraft`.

Call shape: a script step `{"command": ID, "params": {...}}` (or just the id string when there are no params) in `run --script -`, or `--cmd 'ID={json}'`. Commands act at the caret or the selection.

## Typing and formatting (text 24, format 41, para 59)

| Command | Params |
|---|---|
| `text.insert` | `text: string, raw?: bool, paragraphs?: bool` (each line a paragraph, one undo step, up to 10,000 lines) |
| `text.newParagraph`, `text.lineBreak`, `text.pageBreak`, `text.columnBreak`, `text.tab` | `{}` |
| `format.bold`, `format.italic`, `format.underline` | `value?: bool` |
| `format.size` | `size: number` |
| `format.color` | `color: "RRGGBB" \| "auto"` |
| `format.font` | font family |
| `para.heading1`, `para.heading2`, `para.heading3`, `para.normal` | `{}` apply a heading or normal style |
| `para.style` | `style: string (name or id)` |
| `para.align` | `value: left \| center \| right \| justify \| distribute \| start \| end` |
| `para.alignCenter`, `para.bullets`, `para.numbering`, `para.indent`, `para.lineSpacing` | paragraph formatting and lists |
| `styles.apply`, `styles.create`, `styles.list` | `styles.apply {style?}` |

## Objects (insert 44, table 48)

| Command | Params |
|---|---|
| `insert.table` | `rows: n, cols: n, style?: string` |
| `insert.picture` | `path?, data? (base64), width? (pt), alt?` |
| `insert.pageBreak`, `insert.header`, `insert.footer`, `insert.pageNumber`, `insert.link`, `insert.bookmark` | headers, footers, links |
| `table.insertRowBelow`, `table.deleteRow`, `table.merge`, `table.style` | table editing |

## Files and editing (file 30, edit 31)

| Command | Params |
|---|---|
| `file.new`, `file.open` | open a document and make it active |
| `file.save` | `path?, password?, markup?: bool, format?` |
| `file.saveAs` | `path, password?, markup?, format?` |
| `file.exportPdf`, `file.exportPng` | export the active document |
| `file.properties`, `file.info` | document properties |
| `edit.undo`, `edit.redo`, `edit.find`, `edit.copy`, `edit.paste` | editing |

## Other families (use `artcraft-find` for params)

`view.*` (45), `review.*` (36, comments and tracked changes), `outline.*` (26), `references.*` (25), `mailings.*` (23), `equation.*` (21), `layout.*` (18), `caret.*` (16).

CLI subcommands `run`, `convert`, `render`, `info`, `text`, `inspect`, `commands`, `parity` and `mcp` are not engine commands.
