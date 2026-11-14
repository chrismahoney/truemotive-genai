---
name: artcraft-find
description: Search the live command registries of every ArtCraft app (or one app) by text and get back app, command id, label and parameter shape. Use when asked which command or app does something ("how do I add a gradient", "which app exports PNG", "keyframe commands"), when you need an exact command id or parameters before calling an app, or to compare what two apps offer.
---

# ArtCraft find (command search)

One query across about 8,900 commands in 17 apps (measured 8,859 on 2026-11-14). It reads each app's real registry at query time, so results are never stale.

## Run it

```sh
python3 -I /Users/chris/Claude/AntiVoxel/truemotive-genai/_shared/adapters/find.py QUERY... [--app SLUG] [--limit N] [--readonly] [--json]
```

- **All words must match** in the command id, label, or parameter text. Ranking: id segment match, then id substring, then label, then params.
- `--app SLUG` limits to one app (slug = registry file name, for example `vectorcraft`, `craft-anything`).
- `--limit N` (default 15). `--readonly` hides likely-mutating commands. `--json` prints records.
- Output lines: `App | command.id | Label | params (first 90 chars)`, with `[mutates?]` when the command may change state.
- About 1.7 seconds for all apps; `--app` is faster.

Verified examples: `find.py gradient` returns PhotoCraft `gradient.fill.create`, VectorCraft `gradient.presets.apply` and DesignCraft `object.gradient`. `find.py keyframe --app anicraft` returns `timeline.insert_keyframe` and friends. `find.py inspect --readonly` returns inspection commands from CADCraft and DeckCraft.

## After you find a command

1. Read the full params with the app's own detail command when available: `<cli> describe ID` on DeckCraft, SoundCraft, DesignCraft and FilmCraft (the registry `describe` flag says which). Otherwise load the app skill and its `references/command-quickref.md`.
2. Call it through that app's batch path (the registry `run` field), then verify the output with [artcraft-qa](../artcraft-qa/SKILL.md).

## How it works and its limits

- Adapters in `_shared/adapters/artcraft_cmds.py` normalise two input forms (a JSON array, or text listings in three layouts) into `{app, id, label, params, readonly}`. PhotoCraft is read through `serve` because its plain listing has no parameters. A registry that parses to nothing fails loudly instead of returning silent empty results.
- **No cache, by design.** Each query runs the CLIs live (about 1.7 s), so nothing is written to disk and nothing goes stale.
- **`readonly` is a guess** unless the registry carries a native `mutates` flag (AniCraft and WordCraft do). The guess accepts only an **exact** action word as the last id segment (get, list, info, inspect, describe, find, query, read, count, status, check, preview, help, sample, capabilities), because prefix matching misread `find.replace`, `developer.checkBox` and `styles.inspectorClear`. Checked against the native flags: 0 misses on AniCraft (240 commands), 2 on WordCraft (670: `mailings.preview` and `file.inspect` change UI state, which a name cannot reveal), plus many conservative false alarms (exports, selection). `[mutates?]` means "do not assume it is safe", not "it changes state".
- PdfCraft has no command registry, so it never appears. Text-listing commands without a dot in the id are skipped.
- Craft Anything lists tools (`command`, `title`, `summary`), not document commands.
- Quote multi-word phrases only if you want them as one word; separate words are matched independently.

