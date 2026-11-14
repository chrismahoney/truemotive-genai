---
name: artcraft-qa
description: Check any file produced by an ArtCraft app before reporting success - exists, non-empty, readable, right size, not blank or fully transparent, drawable content present, warnings read, image actually viewed. Use after every render, export, or save from PhotoCraft, VectorCraft or any other Craft app, and when verifying benchmark or smoke-test outputs.
---

# ArtCraft QA (post-render checklist)

The single home for "is this output actually good?". App skills link here instead of repeating it.

## The checklist

1. **Command results:** every step succeeded (`failed: 0`, no `error` rows). A batch is not a transaction, so read each result.
2. **Warnings:** read every `warnings` array on saves and exports. Report material ones (flattened layers, lost features, fallbacks).
3. **Files exist:** run the checker below on every artifact, for example `--size 1024x1024` when the size was specified.
4. **Look at it.** Read the PNG (or a render of the file) and compare it with the request: composition, colours, text, edges, clipping. Counts and checks cannot judge appearance.
5. **Structure:** inspect the document (layers, objects, artboards) when editability matters, and say what you saw.
6. **Report honestly:** real output paths, sizes, what you verified, and what you did not run.

## Run the checker

```sh
python3 -I /Users/chris/Claude/AntiVoxel/truemotive-genai/_shared/adapters/qa.py FILE... [--size WxH]
```

Prints `STATUS path | details | bytes` per file and exits 1 if any file FAILs. Read-only, no dependencies, about 1 second for a 1024x1024 PNG.

## What it checks (verified on real outputs and bad fixtures)

| Type | Checks | FAIL when |
|---|---|---|
| PNG | decodes pixels (8-bit RGB/RGBA, up to 4 MP), colour count, dominant colour share | one colour covers over 99.9% (blank), fully transparent, wrong `--size`, unreadable |
| JPEG | start and end markers, size from the frame header (pixels are not decoded) | wrong `--size`; WARN if the end marker is missing |
| SVG | root is `<svg>`, counts drawable elements | no drawable elements |
| PDF | `%PDF` header, `%%EOF` marker | (WARN if no EOF) |
| ZIP containers (`.pcraft`, `.xlsx`) | entry count | unreadable |
| JSON documents (`.vectorcraft`, `.ecproj`) | parses as JSON, counts top-level keys | invalid or truncated JSON |
| any | exists and non-empty | missing or 0 bytes |

WARN means suspicious (a dominant colour above 98%, an unrecognised format, a PNG too large or unusual to decode): look at it yourself. Example run on the pc-vs-vc outputs: PhotoCraft PNG 1506 colours, VectorCraft PNG 129 colours, SVG 81 drawable elements, all OK.

## Rules that apply to every app

- Prefer headless CLI sessions for file output; do not touch a user's open window unless asked and the app is running.
- Scratch generators print to stdout and keep intermediate files in the scratchpad.
- After a timeout, disconnect, or partial failure, inspect state and history before replaying any mutation.
- Never overwrite a file you did not create; remove only partial outputs you made.
- Say plainly what was not verified. "Not yet run" is a valid status.

## Limits

The checker cannot judge appearance, so step 4 of the checklist is not optional. It does not decode pixels of 16-bit, indexed, or interlaced PNGs, JPEG (structure and size only), GIF, or WebP, so it cannot tell a blank one from a real one. For those, view the image.

