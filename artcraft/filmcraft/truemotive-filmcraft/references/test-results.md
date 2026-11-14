# TrueMotive FilmCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.7.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | Full film command catalog |
| `file.newProject` | ✅ Creates new project | Cmd+Alt+N shortcut |
| `file.openDemoProject` | ✅ Opens demo project | Pre-built demo scene |
| `file.import_audio` | ✅ Imports audio clip | WAV/M4A formats supported |
| `file.export_mix` | ✅ Exports mix | Stereo WAV output verified |
| `file.export_session_text` | ✅ Exports session info | JSON summary generated |

## Verified Operations

### 1. New Project (`file.newProject`)
- **Command pattern:** `./bin/filmcraft-cli run --cmd 'file.newProject' --params '{name: "test-project"}`
- **Result:** Creates new film project
- **Status:** ✅ Pass

### 2. Import Audio (`file.import_audio`)
- **Command pattern:** `./bin/filmcraft-cli run --cmd 'file.import_audio' --params '{path: "/tmp/test clip.mp3"}`
- **Result:** Audio clip imported into project
- **Status:** ✅ Pass

### 3. Export Mix (`file.export_mix`)
- **Command pattern:** `./bin/filmcraft-cli run --cmd 'file.export_mix'`
- **Result:** Exported mix as stereo WAV
- **Status:** ✅ Pass

### 4. Export Session Text (`file.export_session_text`)
- **Command pattern:** `./bin/filmcraft-cli run --cmd 'file.export_session_text'`
- **Result:** JSON session summary generated
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From FilmCraft | To App | Method |
|---|---|---|
| Exported mix | SoundCraft | `file.import_audio` for further editing |
| Sequence frames | PhotoCraft | PNG sequence import for texturing |
| Audio stems | EffectCraft | Processed via `effects.chain` |