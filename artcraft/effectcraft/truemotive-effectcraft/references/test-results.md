# TrueMotive EffectCraft Test Results

**Date:** 2026-11-14
**Pack version:** 0.7.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned command array | Full effect command catalog |
| `effects.apply` | ✅ Applies single effect | Tested with multiple effects |
| `effects.chain` | ✅ Applies effect chain | JSON chain definition works |
| `convert resample` | ✅ Resamples audio | Rate conversion verified |
| `convert normalize` | ✅ Normalizes audio | Peak normalization tested |
| `convert bitdepth` | ✅ Changes bit depth | 16/24/32f modes verified |

## Verified Operations

### 1. Apply Effect (`effects.apply`)
- **Command pattern:** `./bin/effectcraft-cli run --cmd 'effects.apply' --params '{effect: "reverb"}`
- **Result:** Reverb effect applied to audio
- **Status:** ✅ Pass

### 2. Effect Chain (`effects.chain`)
- **Command pattern:** `./bin/effectcraft-cli run --cmd 'effects.chain' --params '{chain: ["compressor", "limiter"]}'
- **Result:** Chain of compressor then limiter applied
- **Status:** ✅ Pass

### 3. Resample (`convert resample`)
- **Command pattern:** `./bin/effectcraft-cli convert resample --rate 48000`
- **Result:** Resampled from 44100 Hz to 48000 Hz
- **Status:** ✅ Pass

### 4. Normalize (`convert normalize`)
- **Command pattern:** `./bin/effectcraft-cli convert normalize --normalize`
- **Result:** Peak normalized to -0.1 dBFS
- **Status:** ✅ Pass

### 5. Bitdepth Change (`convert bitdepth`)
- **Command pattern:** `./bin/effectcraft-cli convert bitdepth --bit-depth 32f`
- **Result:** Changed to 32-bit floating point
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From EffectCraft | To App | Method |
|---|---|---|
| Exported audio | SoundCraft | `.scraft` session or WAV import |
| Audio stems | FilmCraft | `file.import_audio` |
| Processed video | LightCraft | Exported frames as sequence |