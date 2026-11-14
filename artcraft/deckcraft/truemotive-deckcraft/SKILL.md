---
name: truemotive-deckcraft
description: Build and edit presentations - slides, layouts, shapes, text, tables, themes, transitions, animation - in DeckCraft (TrueMotive ArtCraft) through its headless CLI, MCP server, or live control port, and export PNG, PDF, PPTX, GIF or outline. Use for slide decks, pitch or report presentations, converting between .deckcraft and .pptx, or any request to work in DeckCraft.
---

# TrueMotive DeckCraft

Presentation app in the ArtCraft suite (331 commands, checked 2026-11-14). Native `.deckcraft`; reads and writes `.pptx`. Exports PNG, PDF, GIF, PPTX and outline. For free-form drawing use VectorCraft; for page layout use DesignCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/deckcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/DeckCraft.app/Contents/MacOS/DeckCraft` |
| Protocol doc | `~/.claude/skills/deckcraft/references/control-protocol.md` (grep it, never read it whole) |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| Build and export unattended | `deckcraft-cli run [--in FILE \| --sample] --cmd 'ID={json}'... [--save OUT] [--export OUT [--export-params JSON]]` (verified) |
| Many commands | `--cmd-file FILE`: one command per line, `#` comments, lines up to 16 MiB; mixes with `--cmd` in order |
| Convert | `deckcraft-cli convert IN OUT` (format by extension) |
| Render slides | `deckcraft-cli render FILE` (PNG images); `render-transition` for transition frames |
| Inspect | `deckcraft-cli info FILE` (slides, layouts, theme as JSON) |
| Agent tool calls | `deckcraft-cli mcp [--connect PORT] [--sample] [--automation-read-root DIR]... [--automation-write-root DIR]...` (roots confine every file the agent reads and writes; documented from help, not yet run) |
| The user's open window | `deckcraft --control PORT`, then `deckcraft-cli app COMMAND` |

`--save` writes `.deckcraft` (everything), `.pptx`, `.pdf` or `.md` (outline). `--export` writes the **current slide** as `.png` or `.jpg`, or the whole deck as `.pdf`, `.pptx` or an animated `.gif`.

## Discover shapes, don't guess

Use `artcraft-find QUERY --app deckcraft`, or `deckcraft-cli describe COMMAND` (explains one command and its parameters) and `deckcraft-cli commands`. Largest families: `format` 47, `shape` 37, `slide` 22, `table` 21, `file` 19, `insert` 18, `text` 17, `arrange` 15, `design` 14. Use `find.py --readonly` to hide commands that may change state.

## Editing model and standard flow

Slides hold shapes and text; sizes are points (the default deck is 16:9, exported PNG 1920x1080). A new presentation starts with **one empty title slide**, so `slide.new` makes a second one (verified: `info` reported 2 slides); edit that first slide or delete it if you want a clean deck.

1. `file.new {theme?, template?, size?, blank?}` (or `--in FILE`, or let `run` start a new deck)
2. `slide.new {layout, title?, body?, at?}`; layouts: title, titleAndContent, sectionHeader, twoContent, comparison, titleOnly, blank, contentWithCaption, pictureWithCaption
3. `shape.insert {preset, rect:[x,y,w,h], text?}`, then style it with `shape.fill {color}` (acts on the selection; the new shape is selected)
4. `slide.inspect` or `document.inspect` to confirm shapes, ids and layout
5. `--save` and `--export`, then check and view with `artcraft-qa`

## Procedural and generative notes

DeckCraft is for authored slides, not for generating many shapes. Generate artwork in VectorCraft or PhotoCraft and insert it as a picture (`picture.*`, not yet run), or build repetitive slides by looping `slide.new` and `shape.insert` from a script (not yet run at scale).

## Save, export, verify

Verified: a titled slide with a teal ellipse saved as `.deckcraft`, converted to `.pdf` with `run --in`, and exported as a 1920x1080 PNG; `artcraft-qa` passed all three and the PNG was viewed. `.pptx` round-trip is not yet run.

## Cross-app hand-offs

- VectorCraft or PhotoCraft PNG into a slide: `picture.*` (not yet run). See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- DeckCraft PDF or PNG to other apps through the shared task directory (PNG verified as an output).

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/deckcraft/`.

