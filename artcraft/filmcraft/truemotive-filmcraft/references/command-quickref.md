# FilmCraft command quick reference

Source: `filmcraft-cli commands` registry, 718 commands, captured 2026-11-14. Params are abbreviated; `?` means optional. The live registry is authoritative: re-dump it if a call is rejected. Search it with `artcraft-find QUERY --app filmcraft`, or `filmcraft-cli describe ID`.

Call shape: a JSON line `{"id": ID, "params": {...}}` through `run -`, or `exec ID key=value` / `exec ID '{json}'`.

## Projects, sequences, media (file 57)

| Command | Params |
|---|---|
| `file.newProject` | `{"name": str}` |
| `file.openDemoProject` | `{}` |
| `file.open`, `file.save`, `file.saveAs` | `file.save {"path"?}`, `file.saveAs {"path"}` |
| `file.newSequence` | `name, width=1920, height=1080, fps=23.976, sampleRate=48000, video=3, audio=3, mix?, fromItem?` |
| `file.import` | `paths: [str], bin?: binId, imageSequence?: bool, replace?: bool` |
| `file.newColorMatte` | `color? (#rrggbb), seconds=5, bin?` |
| `file.newBarsAndTone`, `file.newBlackVideo`, `file.newCountingLeader` | generated sources |
| `file.exportMedia` | `path, preset?, settings?, format? (h264\|hevc\|prores\|dnxhr\|apv\|mjpeg\|png\|tiff\|jpg\|gif\|wav\|aiff\|aac\|mp3\|flac...), audioCodec?, ...` |
| `file.exportEdl`, `file.exportOtio`, `file.exportFcpxml`, `file.exportAaf` | interchange formats |
| `project.inspect` | project tree |

## Sequences and timeline

| Command | Params |
|---|---|
| `sequence.settings` | `width?, height?, fps?, name?, sampleRate?, mix?, dropFrame?` |
| `sequence.addEdit`, `sequence.matchFrame` | edit at the playhead, match frame |
| `sequence.renderInToOut`, `sequence.renderAudio` | pre-render |
| `timeline.place`, `timeline.delete`, `timeline.select`, `timeline.move` | place and move clips |
| `timeline.trim`, `timeline.roll`, `timeline.slip`, `timeline.slide`, `timeline.razor` | trim and cut |
| `clip.rename`, `clip.makeSubclip` | clip metadata |

## Media and export queue

| Command | Params |
|---|---|
| `media.findMissing`, `media.relink`, `media.linkMedia` | `media.relink {"item": id, "path": str, "force"?: bool}` |
| `media.createProxies`, `media.attachProxies`, `media.toggleProxies` | proxy workflow |
| `export.presets.list`, `export.presets.get`, `export.formats` | export presets and formats |
| `export.queue.add`, `export.queue.list`, `export.queue.start` | batch export |

## Other families (use `artcraft-find` for params)

`graphics.*` (83), `edit.*` (39), `multicam.*` (35), `markers.*` (33), `trim.*` (24), `captions.*` (23), `mixer.*` (20), `effects.*` (16), `shortcuts.*` (16).

CLI subcommands `run`, `exec`, `commands`, `describe`, `inspect`, `import`, `export`, `render`, `probe`, `bench-decode` and `mcp` are not engine commands.
