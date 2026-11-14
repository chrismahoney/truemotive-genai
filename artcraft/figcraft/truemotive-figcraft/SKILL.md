---
name: truemotive-figcraft
description: Design interfaces and vector layouts - frames, shapes, text, components, variables, auto layout, prototypes - in FigCraft (TrueMotive ArtCraft, a Figma-style design tool) through its headless CLI, scripts or MCP server, and render or export PNG, JPG, WebP, SVG, PDF, Android vector drawables or .fig files. Use for UI mockups, design-system cards, icons, multi-size exports, importing or converting Figma, Penpot or Sketch files, or any request to work in FigCraft.
---

# TrueMotive FigCraft

Design tool in the ArtCraft suite (643 commands, checked 2026-11-14), in the Figma family: pages, frames, layers, components and variants, variables, prototypes, comments and collaboration. Native `.figcraft`; also reads `.penpot`, `.json`, `.fig` (best effort) and `.sketch`. Its object model is VectorCraft's: objects with fills and strokes. For free-form vector art use VectorCraft; for page layout DesignCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/figcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/FigCraft.app/Contents/MacOS/FigCraft` |
| Protocol doc | none installed (the CLI points to `docs/cli.md` and `docs/mcp.md` upstream) |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| Build a file from commands (best default) | `figcraft-cli run SCRIPT.jsonl [--in FILE] [--out FILE]`: a JSON array or JSON lines of `{"command": ID, "params": {...}}`, one result line per step (verified) |
| Render the page | `figcraft-cli render FILE --out F.png` (png, jpg or webp; verified: 400x300 in 0.25 s) |
| Export frames or a layer | `figcraft-cli export FILE --out DIR` writes one file per top-level frame (`DIR/Card.png`), or `--out F.png` / `--node` for one (verified) |
| Convert | `figcraft-cli convert IN OUT` by extension: `.figcraft .json .svg .png .jpg .webp .pdf .fig .penpot` (verified to `.svg`) |
| Inspect | `figcraft-cli info FILE` (pages, node counts, frames, styles) |
| Agent tool calls | `figcraft-cli mcp` (headless, or attached to a running app; not yet run) |
| Confine file access | `run --automation-read-root DIR --automation-write-root DIR` (not yet run) |

**`run` needs a regular script file**: stdin, a pipe and `/dev/stdin` are rejected ("isn't a regular file"), so write the script with the editor tools first. **A script is one all-or-nothing undo step**: any failing step rolls the whole document back (`rolledBack: true`). Each `run` is its own session; `--no-system-fonts` makes text renders match on every machine.

## Discover shapes, don't guess

Use `artcraft-find QUERY --app figcraft` or `figcraft-cli commands`. Families: `text` 63, `view` 49, `vector` 42, `tool` 30, `object` 28, `file` 24, `collab` 22, `select` 21, `component` 21, `proto` 21, `board` 21, `variable` 19, `library` 19. Use `find.py --readonly` to hide commands that may change state.

## Editing model and standard flow

Objects on pages. Node ids are integers: the page is 1 and new nodes count up from 2 in creation order. **A new node's default parent is the page, not the last frame**, so pass `parent`.

1. `node.create {type: frame, x, y, width, height, name}` returns `{id}` (2 on a fresh file)
2. Children: `node.create {type: rectangle \| ellipse \| polygon \| star \| line \| arrow \| vector \| text \| component, parent: 2, x, y, width, height, name, text?}`
3. Style with `node.set {ids, fills: ["#hex"], cornerRadius, opacity, ...}`, `fill.set {ids?, color}`, `stroke.set`, `effect.add`. `node.create` itself rejects `fills`.
4. `node.get {id}` reads a node back (fills, bounds)
5. `--out F.figcraft`, then render, export, or convert, and check with `artcraft-qa` (PNG, SVG and the ZIP `.figcraft` are recognised); view the render

**Verified (smoke test, `artifacts-test/figcraft/smoke.jsonl`):** a 400x300 card with a rounded orange rectangle, a default rectangle, a teal ellipse and text rendered correctly (viewed); the SVG had 6 drawable elements. **Style inheritance: none.** A rectangle created after an orange one came back the default `#D9D9D9`. **New nodes are auto-selected:** `fill.set` without `ids` styled the ellipse just created. **Selection does not survive between sessions:** the same `fill.set` in a new `run --in FILE` fails with "nothing is selected (pass `ids`)". Unknown parameters are reported with the list of accepted ones.

## Procedural and generative notes

Shapes are commands, so a generator can emit a JSON-lines script (`node.create` with `vector` and `path`/`points`). The script must be a file. An `artcraft-gen-recipes` emitter for FigCraft does not exist yet. The per-path point limit was not tested (it needs a very large script file), so treat it as unknown.

## Save, export, verify

Native `.figcraft` is a ZIP (9 KB for the smoke test) via `--out`, or `file.save {path, overwrite?}` (a path is required the first time). Exports: `file.export {ids?, format: png \| jpg \| svg \| pdf \| webp \| xml \| fig}`, `file.exportSvg`, `export.add` (per-node export settings with `size` such as `2x`, `512w`), and the CLI `export`, `render`, `convert`.

## Cross-app hand-offs

- FigCraft SVG into VectorCraft for styling or tracing (`file.open`), and VectorCraft SVG into FigCraft (`file.open`/`file.import`): not yet run. See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- PNG renders out to LightCraft or PhotoCraft for finishing (PNG output verified).

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/figcraft/`.
