# CADCraft command quick reference

Source: `cadcraft-cli commands` registry, 457 commands, captured 2026-11-14. Params are abbreviated; `?` means optional; `handles` are entity ids (hex strings, default: the selection). The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app cadcraft`.

Call shape: `cadcraft-cli run --cmd 'ID {json}' ...` (id, a space, then the JSON object). Many ids have no dot.

## Drawing and files

| Command | Params |
|---|---|
| `new` | `metric?: bool, template?: path to .dwt/.dxf ("." for none)` |
| `open` | `path` or `{data: base64, name}` returns `{index, entities?, warnings}` |
| `saveas` | `path, version? (2000..2018), binary?: bool, portableFonts?` |
| `export` | `path? (else base64 data), format? (dxf\|dwg\|svg\|png\|pdf, default by extension)` |
| `drawing.inspect` | `entities?: bool, limit?: n` returns counts, current layer, layers, entities |

## Draw

| Command | Params |
|---|---|
| `line` | `points: [[x,y],...], closed?` (closed makes separate Line entities) |
| `pline` | `vertices: [[x,y] or {p, bulge, startWidth, endWidth}], closed?, width?` |
| `circle` | `{center, radius}` or `{center, diameter}` or `{p1, p2}` or `{p1, p2, p3}` |
| `arc` | `{p1, p2, p3}` or `{center, radius, start, end}` (degrees) or `{start, center, end}` |
| `text` | `at, text, height?, rotation?, justify? (L\|C\|R\|M\|TL..BR)` |
| `mtext` | `at, text, height?, width?, attach?, rotation?, style?, lineSpacing?, list?` |
| `hatch` | `points? (internal points) and/or handles?, pattern? ("ANSI31"), patternFile?` |
| `dim` | `p1, p2, at` |

## Layers and editing

| Command | Params |
|---|---|
| `layer.new` | `name, color?, linetype?, lineweight? (mm), current?: bool` |
| `layer.set` | `name, on?, frozen?, locked?, plot?, color?, linetype?, lineweight?, newName?` |
| `layer.current`, `layer.delete` | switch or remove a layer |
| `erase`, `move`, `copy`, `rotate`, `scale` | `handles?` plus `delta` or `from,to`, `base,angle`, `base,factor` |
| `offset` | `handle, distance, side: [x,y], erase?, layer?` |
| `trim` | `handle, pick \| fence \| crossing, edges?, edgeMode?, mode?` |
| `zoom.window`, `zoom.extents` | frame the view |

## Other families (use `artcraft-find` for params)

`table.*` (12), `arc.*` (11), `zoom.*` (10), `layout.*` (8), `dimstyle.*` (8), `vports.*` (7), `blocks.*` (7), `grip.*` (7), `circle.*` (6), `draworder.*` (5), `layerstate.*` (5), `style.*` (5).

CLI subcommands `run`, `convert`, `info`, `commands`, `mcp`, `perf`, `sample` and `roundtrip` are not engine commands.
