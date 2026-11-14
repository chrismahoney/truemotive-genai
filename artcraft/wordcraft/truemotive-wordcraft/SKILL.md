---
name: truemotive-wordcraft
description: Write and edit word-processor documents - paragraphs, headings, styles, tables, pictures, headers, footers, references, review comments, mail merge - in WordCraft (TrueMotive ArtCraft) through its headless CLI or MCP server, and save or convert DOCX, PDF, ODT, RTF, HTML, Markdown, TeX, text or page PNGs. Use for reports, letters, converting between document formats, extracting text, rendering pages to images, or any request to work in WordCraft.
---

# TrueMotive WordCraft

Word processor in the ArtCraft suite (670 commands, checked 2026-11-14): paragraphs, character and paragraph formatting, styles, tables, pictures, headers and footers, references, review (comments and tracked changes), mailings and equations. Reads and writes DOCX and more. For slide decks use DeckCraft, for page layout DesignCraft, for spreadsheets GridCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/wordcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/WordCraft.app/Contents/MacOS/WordCraft` |
| Protocol doc | none installed |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| Build a document (best default) | `wordcraft-cli run --script - ` with a JSON script on **stdin**: `{"file"?, "template"?, "commands": [{"command": ID, "params"?: {...}} \| ID, ...], "save": [OUT, ...]}`. `save` formats follow the extension, so DOCX and PDF come from one run (verified). |
| Commands inline | `wordcraft-cli run [--file F \| --template T] --cmd 'ID={json}' ... [--save OUT] [--print] [--author NAME]` |
| Render a page | `wordcraft-cli render FILE OUT.png [--page N] [--scale S]` (verified: 1224x1584 for one page) |
| Convert | `wordcraft-cli convert IN OUT [--markup] [--update-fields] [--format wordml2003\|flatopc]`; formats docx, doc (read only), pdf, odt, rtf, html, md, tex, txt, json, png, xml |
| Read | `wordcraft-cli info FILE` (pages, words, paragraphs, properties), `text FILE` (plain text), `inspect FILE` (structure) |
| Agent tool calls | `wordcraft-cli mcp [--connect HOST:PORT \| --author NAME] [--automation-read-root DIR] [--automation-write-root DIR]` (not yet run) |

`file.new` and `file.open` inside a script open another document and make it the active one; later commands and the saves act on it. `--author` names the author of tracked changes and comments.

## Discover shapes, don't guess

The plain `wordcraft-cli commands` listing carries **no parameter text**; use **`commands --json`**, which has parameters and a native `mutates` flag for every command (the registry row uses it, so `artcraft-find` shows real parameters). Use `artcraft-find QUERY --app wordcraft`. Families: `para` 59, `table` 48, `view` 45, `insert` 44, `format` 41, `review` 36, `edit` 31, `file` 30, `outline` 26, `references` 25, `text` 24, `mailings` 23, `equation` 21, `layout` 18, `caret` 16, `styles` 16. `find.py --readonly` uses the native flag here.

## Editing model and standard flow

Caret-based, like a word processor: commands act at the caret or on the selection.

1. Start a document (a new one by default, or `--file F`, or `--template T`)
2. Set the paragraph style, then type: `para.heading1`, `text.insert {text}`, `text.newParagraph`, `para.normal`, `text.insert {text}`. `text.insert` also takes `paragraphs: true` (each line a paragraph, up to 10,000 lines).
3. Format: `format.bold {value?}`, `format.size {size}`, `format.color {color: "RRGGBB"}`, `para.align {value}`, `para.style {style}`
4. Insert objects: `insert.table {rows, cols, style?}`, `insert.picture {path, width?, alt?}`, headers, footers, page numbers, links, bookmarks
5. Save in several formats at once with the script's `save` list, then `render` a page and check with `artcraft-qa`; view the page

**Verified (artifacts-test/wordcraft):** a Heading 1, a body paragraph and a 3x3 table saved as DOCX (9 ZIP entries) and PDF in one run in 0.11 s; `render` gave a clear page; `info` reported 1 page and 12 paragraphs (table cells count as paragraphs); `text` extracts the content with tabs for the table cells. **Gotcha:** a rendered page is mostly white, so `artcraft-qa` reports "dominant 99%" (WARN): expected for text pages, so view the page instead of treating it as blank.

## Procedural and generative notes

WordCraft generates documents, not images. A script can emit hundreds of `text.insert` and `insert.table` commands from data (reports, mail merge via the `mailings.*` family, not yet run). It has no path commands.

## Save, export, verify

`file.save {path, password?, markup?, format?}` and `file.saveAs`; a script's `save` list writes several formats; `file.exportPdf`, `file.exportPng`. Print Markup (`markup`) shows comments and tracked changes in PDF and PNG. `convert` also reads `.doc`.

## Cross-app hand-offs

- A WordCraft PDF into PdfCraft for checks or into DeckCraft, and benchmark results from GridCraft into a report: not yet run. See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- Page PNGs out to LightCraft or PhotoCraft (PNG output verified).
- Pictures in: `insert.picture` with a PhotoCraft or VectorCraft PNG (not yet run).

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/wordcraft/`.
