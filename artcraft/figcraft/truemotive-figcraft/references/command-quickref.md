# FigCraft command quick reference

Source: `figcraft-cli commands` registry, 643 commands, captured 2026-11-14. Params are abbreviated; `?` means optional; `ids?` defaults to the selection (which is empty at the start of every session). The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app figcraft`.

Call shape: a JSON line `{"command": ID, "params": {...}}` in a script file passed to `figcraft-cli run`. Ids are integers; the page is 1 and new nodes start at 2.

## Layers and properties

| Command | Params |
|---|---|
| `node.create` | `type: rectangle \| ellipse \| polygon \| star \| line \| arrow \| vector \| text \| frame \| section \| component \| slice, x?, y?, width?, height?, parent? (default the page), index?, name?, text? \| characters?, path? \| points?` (no `fills`) returns `{id}` |
| `node.set` | `name, visible, locked, opacity (0-1 or "50%"), blend, x, y, width, height, rotation, fills (colours or paints; gradients as {type, stops}), cornerRadius...` plus `ids?` |
| `node.get` | `id` returns fills, bounds, type |
| `node.find` | `root?, name?, type?, text?, component?, limit?` |
| `node.reparent`, `node.reorder` | `ids?, parent, index?` |
| `fill.set` | `ids?, index?, paint \| color, opacity?, visible?, blend?` |
| `stroke.set` | `ids?, index?, paint \| color, opacity?, visible?, blend?` |
| `effect.add` | `ids?, type? (dropShadow \| innerShadow \| layerBlur \| backgroundBlur \| noise \| texture \| glass)` |
| `object.group`, `object.ungroup` | `ids?, name?` |
| `select.all`, `select.set`, `select.none` | selection (state lives only inside a session) |
| `edit.undo`, `edit.redo`, `edit.delete`, `edit.duplicate` | edits |

## Text, vectors, components, variables

| Command | Params |
|---|---|
| `text.create`, `text.set` | `text.set {id?, characters \| text}` |
| `vector.create`, `vector.flatten`, `vector.simplify`, `vector.outlineStroke` | vector paths |
| `component.create` | `ids?` turns a frame or group into a component |
| `component.list`, `component.addVariant`, `component.detach` | components and variants |
| `variable.create` | `collection, name, type (color\|number\|string\|boolean), value \| values {mode: value}, description?` |
| `variable.set`, `variable.bind`, `variable.list` | variables |

## Files, pages, exports

| Command | Params |
|---|---|
| `file.new` | `name?` |
| `file.open` | `path \| data (base64) + name` |
| `file.save`, `file.saveAs` | `file.save {path?, overwrite?}` (a path is required the first time) |
| `file.export` | `ids?, format? (png\|jpg\|svg\|pdf\|webp\|xml\|fig), ...` |
| `file.exportSvg`, `file.exportFramesPdf` | SVG and multi-frame PDF |
| `export.add` | `ids?, setting? {size: 2x\|512w\|512h, suffix?, format?, ...}` |
| `page.add`, `page.list`, `page.select`, `page.rename` | pages (`page.add {name?}`) |

## Other families (use `artcraft-find` for params)

`view.*` (49), `tool.*` (30), `object.*` (28), `collab.*` (22), `proto.*` (21, prototypes), `board.*` (21, whiteboard objects), `library.*` (19), `pref.*` (17), `comment.*` (15).

CLI subcommands `run`, `render`, `export`, `convert`, `info`, `commands`, `mcp`, `plugin`, `connect` and `perf` are not engine commands.
