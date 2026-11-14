# DesignCraft command quick reference

Source: `designcraft-cli commands` registry, 555 commands, captured 2026-11-14. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app designcraft`.

Call shape: `designcraft-cli run --cmd ID='{json}' ...` (or `--cmd ID` with no params); results come back bare, one per line.

## Documents and files (41)

| Command | Params |
|---|---|
| `file.new` | `preset? ("Letter", "A4", or saved), intent? (print\|web\|mobile), units?, width?, height?, pages?, facingPages?, columns?, gutter?, margins?, bleed?, slug?` |
| `file.open`, `file.save`, `file.saveAs`, `file.saveACopy`, `file.close` | document lifecycle |
| `file.place` | place an image or text file into the layout |
| `file.exportPdf` | `path?, pages? ("1-3,5" or [1,3], 1-based), flatten?: high\|medium\|low\|ppi ...` |
| `file.exportIdml`, `file.exportEpub`, `file.exportHtml`, `file.exportPptx` | other formats |
| `document.inspect` | `{}` returns pages, spreads, items, stories (with overset), styles, swatches, selection |
| `file.info` | title, author, description, keywords, copyright |

## Frames, paths, objects

| Command | Params |
|---|---|
| `frame.create` | `rect: [x0,y0,x1,y1] (spread coords), spread?, shape? (rectangle\|ellipse\|polygon), content? (graphic\|text\|unassigned), sides?, text?, vertical?` returns `{id}` (text frames also `{story}`) |
| `frame.grid` | grid of frames |
| `path.create` | `anchors: [{p:[x,y], in?:[x,y], out?:[x,y]}], closed?` |
| `path.appendAnchor`, `path.close`, `path.join`, `path.split`, `path.smooth` | path editing |
| `object.fill` | `swatch?, tint? (0..1), ids?` (with nothing selected, sets the fill of new shapes) |
| `object.stroke` | `swatch?, tint?, weight?, align? (center\|inside\|outside), type?: {kind: solid\|dashed\|dotted...}` |
| `object.opacity` | `opacity: 0..1, blend?, ids?` |
| `object.group`, `object.ungroup`, `object.bringToFront`, `object.sendToBack`, `object.dropShadow` | arrange and effects |

## Swatches, text, styles

| Command | Params |
|---|---|
| `swatch.create` | `name?, color: "#rrggbb"\|{c,m,y,k}\|[r,g,b], spot?` or `gradient: {kind?, stops: [...]}` returns `{name}` |
| `swatch.new`, `swatch.delete`, `swatch.load` | manage swatches |
| `story.setText` | `story, text` replaces a story's whole text |
| `story.get`, `story.replaceRange` | read and partial edits |
| `text.insert`, `text.select`, `text.delete` | caret-based editing |

## Other families (use `artcraft-find` for params)

`type.*` (43), `table.*` (41), `layout.*` (32), `style.*` (28), `edit.*` (18), `swatch.*` (13), `transform.*` (10), `book.*` (10), `guide.*` (10), `xml.*` (10), `data.*` (10, data merge), `note.*` (9), `layer.*` (9), `library.*` (8), `links.*` (7).

CLI subcommands `run`, `script`, `app`, `mcp`, `describe`, `validate-pdf`, `perf` and `bench` are not engine commands.
