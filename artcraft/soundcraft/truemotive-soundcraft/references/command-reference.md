# TrueMotive SoundCraft Command Reference
**Pack version:** 0.6.0 (2026-11-14)
**CLI:** `/Users/chris/Claude/TrueMotive/artcraft-root/bin/soundcraft-cli`
**Status:** ✅ Fully Supported App (truemotive-genai pack v0.6.0)

---
# TrueMotive SoundCraft Command Reference
**Pack version:** 0.6.0 (2026-11-14)
**CLI:** `/Users/chris/Claude/TrueMotive/artcraft-root/bin/soundcraft-cli`

---
# Command List (sorted by category)

## File Management

| Command | Description | Usage |
|---|---|---|
| `file.import_audio` | Import audio into session | `path` or `paths` (required) |
| `file.export_midi` | Export MIDI from session | — |
| `file.export_session_text` | Export session info as text | — |
| `file.bounce_mix` | Bounce mix to audio file | `--out`, `--start`, `--end` |
| `file.bounce_stems` | Bounce stems to separate files | — |
| `file.export_clips` | Export clips as files | — |
| `file.import_session_data` | Import session data | — |
| `app.quit` | Quit the application | — |

## Session Management

| Command | Description | Usage |
|---|---|---|
| `session.new` | Create new session | — |
| `session.open` | Open existing `.scraft` session | `[file]` |
| `session.close` | Close current session | — |
| `session.save` | Save current session | — |
| `session.save_as` | Save session as new file | `[file]` |
| `session.save_copy` | Save session copy | In... |
| `session.revert` | Revert to saved version | — |

## Edit Operations

| Command | Description | Usage |
|---|---|---|
| `edit.undo` | Undo last action | — |
| `edit.redo` | Redo undone action | — |
| `edit.cut` | Cut selection | — |
| `edit.copy` | Copy selection | — |
| `edit.paste` | Paste from clipboard | — |
| `edit.clear` | Clear selection | — |
| `edit.select_all` | Select all elements | — |
| `edit.select_none` | Deselect all elements | — |
| `edit.nudge` | Nudge selection | `[direction]` |
| `edit.move_clips` | Move clips | `[direction]` |
| `edit.trim_start_to_insertion` | Trim to insertion point | — |
| `edit.trim_end_to_insertion` | Trim end to insertion | — |
| `edit.fade_to_start` | Fade to start of selection | — |
| `edit.fade_to_end` | Fade to end of selection | — |
| `edit.halve_selection` | Halve the selection | — |
| `edit.double_selection` | Double the selection | — |
| `edit.extend_selection_up` | Extend selection up | — |
| `edit.extend_selection_down` | Extend selection down | — |
| `edit.remove_selection_top` | Remove from top of selection | — |
| `edit.remove_selection_bottom` | Remove from bottom of selection | — |
| `edit.duplicate` | Duplicate selection | — |
| `edit.repeat` | Repeat last action | — |
| `edit.shift` | Shift selection | — |
| `edit.tool` | Set edit tool | — |
| `edit.consolidate` | Consolidate clips | — |

## Effects and Processing

| Command | Description | Usage |
|---|---|---|
| `effects.apply` | Apply effect | `[effect]`, `[params]` |
| `effects.chain` | Apply effect chain | `[chain definition]` |
| `edit.trim_start_to_insertion` | Trim to insertion | — |
| `edit.trim_end_to_insertion` | Trim end to insertion | — |
| `edit.nudge` | Nudge | `[direction]` |
| `edit.fade_to_start` | Fade to start | — |
| `edit.fade_to_end` | Fade to end | — |

## Conversion

| Command | Description | Usage |
|---|---|---|
| `convert resample` | Resample audio | `--rate <HZ>`, `[--dither|--no-dither]` |
| `convert normalize` | Normalize audio | `--normalize`, `[--dither|--no-dither]` |
| `convert bitdepth` | Change bit depth | `--bit-depth <16|24|32f>` |

## Query/Inspect

| Command | Description | Usage |
|---|---|---|
| `info` | Print audio file format as JSON | `[file]` |
| `describe` | Print one command's details as JSON | `<command_id>` |
| `commands` | List all engine commands | — |
| `parity` | Print parity report (markdown) | — |
| `plugins` | List built-in plugins | — |

## MCP and Live Control

| Command | Description | Usage |
|---|---|---|
| `mcp` | Serve MCP on stdin/stdout | — |
| `mcp --bridge 127.0.0.1:PORT --control-token-file F` | Live app MCP bridge | — |
| `app` | Call running app's control channel | — |