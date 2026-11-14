---
name: truemotive-soundcraft
description: Edit audio, mix tracks, apply effects, convert formats, and manage sessions in SoundCraft (TrueMotive ArtCraft) via its CLI, JSON-lines server, or MCP bridge. Use for audio post-production, format conversion, session management, or any request to work in SoundCraft.
---

# TrueMotive SoundCraft

Audio editing and production in the ArtCraft suite (verified commands, checked 2026-11-14). Supports multitrack editing, effects, format conversion, and session management. If the result should stay in a DAW project format, use the native `.scraft` format; for flat exports, use WAV or FLAC.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/soundcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/SoundCraft.app/Contents/MacOS/SoundCraft` |
| Protocol doc | none (CLI help is the source of truth) |

## Choose a session

| Need | Use |
|---|---|
| One short edit sequence on a file | `soundcraft-cli run [session] ... --cmd ID --params JSON` |
| Many edits or generated geometry | `soundcraft-cli serve --automation-write-root DIR`, then pipe JSON lines on stdin |
| Agent tool calls | `soundcraft-cli mcp` (headless) or `mcp --bridge 127.0.0.1:PORT --control-token-file F` (live app) |
| The user's open window | Desktop `SoundCraft --control PORT --control-token-file F`. A headless session never edits it. |

Run `ps aux | grep -i soundcraft` first. Never trust a PID from notes; if no GUI runs, headless is correct for file output.

## Discover shapes, don't guess

`soundcraft-cli commands` (or `engine.commands`) returns a bare array of `{id, label, params, enabled, needsDocument, disabledReason}`. `params` is a doc-string with types, ranges, and defaults. Dump it once to the scratchpad and filter it with `python3 -I`; never print all rows. Start from the CLI help for the major commands.

## Standard flow

1. `session.new` (or `session.open` an existing `.scraft` file)
2. `file.import_audio` to bring in audio assets
3. `edit.trim_start_to_insertion`, `edit.trim_end_to_insertion` to set bounds
4. `edit.nudge`, `edit.move_clips` to position clips
5. `edit.fade_to_start`, `edit.fade_to_end` for transitions
6. `effects.apply` or `effects.chain` for processing
7. `file.export_midi`, `file.export_session_text`, or `file.export_mix` to finish
8. `session.save` to persist `.scraft`

Prefer non-destructive edits (effects chains, fades) over baked operations when they suit the request.

## Jobs, failures, and uncertain outcomes

- `batch` is not a transaction. Use `stopOnError: true`, read every result, and inspect `history` before retrying anything.
- Long commands wait by default; with `wait:false` poll `jobs.list` before dependent edits.
- After a timeout or disconnect, inspect the session before replaying a mutation.
- If a write target already exists, look at it first. Delete only partial outputs you created yourself.

## Cross-app hand-offs

- Audio to video: export WAV from SoundCraft, then use FilmCraft `file.import_audio` or LightCraft `audio` support.
- Audio to vector: export stems, then use VectorCraft if spectral data is needed.
- Do not copy ports or auth flags between apps. SoundCraft MCP uses a token file; other apps use different bridges.

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad. Save test outputs to `artifacts-test/soundcraft/`.

Reference run: verify `soundcraft-cli run` with a simple `edit.nudge` on a test audio file, 0 failures.

## Command Quick Reference (subset)

### Session Management
```
soundcraft-cli session.new
soundcraft-cli session.open [file]
soundcraft-cli session.close
soundcraft-cli session.save
soundcraft-cli session.save_as [file]
```

### File Operations
```
soundcraft-cli file.import_audio [file]
soundcraft-cli file.export_mix [file]
soundcraft-cli file.export_midi [file]
soundcraft-cli file.export_session_text [file]
```

### Edit Operations
```
soundcraft-cli edit.trim_start_to_insertion
soundcraft-cli edit.trim_end_to_insertion
soundcraft-cli edit.nudge [direction]
soundcraft-cli edit.move_clips [direction]
soundcraft-cli edit.fade_to_start
soundcraft-cli edit.fade_to_end
soundcraft-cli edit.undo
soundcraft-cli edit.redo
```

### Effects and Processing
```
soundcraft-cli effects.apply [effect] [params]
soundcraft-cli effects.chain [chain definition]
```

### Conversion
```
soundcraft-cli convert resample [params]
soundcraft-cli convert normalize [params]
soundcraft-cli convert bitdepth [params]
```