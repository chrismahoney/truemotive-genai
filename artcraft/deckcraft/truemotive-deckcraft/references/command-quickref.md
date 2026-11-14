# DeckCraft command quick reference

Source: `deckcraft-cli commands` registry, 331 commands, captured 2026-11-14. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app deckcraft`, or `deckcraft-cli describe COMMAND`.

Call shape: `deckcraft-cli run --cmd 'ID={json}' ...` (a command with no params is just its id).

## Presentations and files (19)

| Command | Params |
|---|---|
| `file.new` | `theme?: name, template?: starter name, size?: [w,h] pt, blank?: bool` |
| `file.templates` | lists starter templates |
| `file.open`, `file.save`, `file.saveAs`, `file.close`, `file.revert` | lifecycle; `file.save {path?, format?: deckcraft\|pptx}` |
| `file.export` | `path, format? (png\|jpeg\|pptx\|deckcraft\|outline\|rtf\|pdf\|gif, else by path), slide?: index, all?, scale?: px per pt, layout? (slides\|notes\|handouts), perPage?, paper?` |
| `file.render`, `file.info` | render and file details |
| `document.inspect` | slides with titles, layouts, shape counts; selection; size; theme |

## Slides (22)

| Command | Params |
|---|---|
| `slide.new` | `layout? (title, titleAndContent, sectionHeader, twoContent, comparison, titleOnly, blank, contentWithCaption, pictureWithCaption), at?: index, title?, body?` |
| `slide.duplicate`, `slide.delete`, `slide.move`, `slide.hide`, `slide.rename` | manage slides |
| `slide.layout`, `slide.reset`, `slide.notes` | layout and speaker notes |
| `slide.go`, `slide.next`, `slide.previous` | change the current slide |
| `slide.inspect` | `index?` returns shapes with ids, kinds, boxes, text, fills, animations, transition, notes |

## Shapes and text (37 and 17)

| Command | Params |
|---|---|
| `shape.insert` | `preset: rect\|roundRect\|ellipse\|triangle\|rightArrow\|star5\|... (see shape.presets), rect: [x,y,w,h] pt, text?` |
| `shape.fill` | `color? \| none? \| background? \| gradient?: {stops: [[pos 0..1, color]], kind?, angle?}` (acts on the selection) |
| `shape.line`, `shape.effects`, `shape.quickStyle` | outline and effects |
| `shape.move`, `shape.resize`, `shape.rotate`, `shape.flip`, `shape.rename` | geometry |
| `text.insert` | `text` (`\n` is a new paragraph) |
| `format.size` | text size |

## Other families (use `artcraft-find` for params)

`format.*` (47), `table.*` (21), `insert.*` (18), `arrange.*` (15), `design.*` (14, themes), `smartArt.*` (13), `edit.*` (12), `picture.*` (12), `review.*` (12), `animation.*` (11).

CLI subcommands `run`, `convert`, `render`, `render-transition`, `info`, `describe`, `app`, `mcp` and `bench` are not engine commands.
