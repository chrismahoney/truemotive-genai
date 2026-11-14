---
name: truemotive-ab-benchmark
description: Run a controlled A/B benchmark of one creative prompt across two ArtCraft apps (for example PhotoCraft vs VectorCraft) and report which wins and why. Use when asked to compare apps or workflows, A/B test a generative-art prompt, benchmark output quality, editability, or speed, or repeat the pc-vs-vc benchmark with a new prompt.
---

# TrueMotive A/B Benchmark

A repeatable method for comparing two ArtCraft apps on the same prompt. The worked example is `/Users/chris/Claude/AntiVoxel/benchmarks/pc-vs-vc/` (stained-glass Voronoi, PhotoCraft vs VectorCraft). Read its `README.md` and `run/comparison.md` once to see the finished shape.

Use the app skills for how to drive each app: [truemotive-photocraft](../../artcraft/photocraft/truemotive-photocraft/SKILL.md) and [truemotive-vectorcraft](../../artcraft/vectorcraft/truemotive-vectorcraft/SKILL.md). Routing between apps lives in [artcraft-skill](../../artcraft/artcraft-skill/SKILL.md). This skill owns only the benchmark method.

## Principles

1. **Define before you run.** Write the prompt and rules into the README first, so both runs are judged against one contract.
2. **Isolate the variable.** Compute shared geometry or data once; each app only renders it. Then the comparison measures the app, not the generator.
3. **Measure, don't eyeball.** Use numbers for time, size, pixel difference, and structure.
4. **Prove editability.** Make a real edit to the native file and diff the result.
5. **Record failures.** One attempt plus at most one fix-and-rerun per app; log every error.
6. **Report honestly.** Include caveats, and say when a gap is not meaningful.

## Process

### 1. Scope the benchmark

Pick one prompt that both apps can plausibly do: a fixed canvas, palette, seed, and counts (the Voronoi run used 1024x1024, 80 cells, seed 7, 8 colours, 6 px lead). Ask the user only if the prompt is genuinely ambiguous. Otherwise choose defaults and state them.

### 2. Create the layout

```
benchmarks/<name>/
  README.md        prompt, fairness rules, metrics, layout, reproduce
  shared/          generator script + generated data (JSON)
  run/
    <appA>/        gen.py, results.md, output/
    <appB>/        gen.py, results.md, output/
    comparison.md
```

Write the README before running anything. See [references/report-templates.md](references/report-templates.md).

### 3. Build the shared generator

A deterministic, dependency-free Python script (no numpy, no PIL; check with `python3 -I -c "import numpy"`). It takes a seed and writes one JSON file of geometry plus styling. The Voronoi example used half-plane clipping and Lloyd relaxation in about 2.2 KB.

### 4. Write one driver per app

Each `gen.py` reads the shared JSON and **prints** commands to stdout (JSON lines); it writes nothing. Pipe it into the app's headless CLI, with scratch intermediates in the session scratchpad. Follow each app skill for command shapes, and use the style that suits the app (PhotoCraft batches fills per colour; VectorCraft makes one named object per item).

### 5. Run each app

- Headless only, so no GUI state differs. PhotoCraft: `photocraft-cli serve --automation-write-root run/photocraft/output`. VectorCraft: `vectorcraft-cli run --commands - --export ...`.
- Create the `output/` directories first. Never overwrite a file you did not create.
- Check the result rows: `failed: 0` or no `error` rows, and read every export `warnings` array.
- View each PNG (Read it) before measuring.
- On failure, read the error, fix the driver once, rerun, and record both attempts.

### 6. Measure

Snippets are in [references/measure-snippets.md](references/measure-snippets.md).

| Metric | Method |
|---|---|
| Success, errors | Result rows and warnings |
| Commands, payload | Line count and byte size of the request stream |
| Wall time | `time.perf_counter` around the subprocess, 3 runs into **scratch** output dirs; report the median and note a cold first run |
| Output sizes | `ls -la` on each artifact |
| Visual difference | `sips` to BMP, then pure-Python diff: mean absolute difference, % pixels over 32, max |
| Feature fidelity | A measurable property, such as line width sampled along edge normals |
| Native structure | PhotoCraft `photocraft-cli info FILE`; VectorCraft `document.inspect` or `vectorcraft-cli info FILE` |
| Editability | Reopen the native file, change one element, re-export, diff. Record exactly what changed. |

Do not use zsh's `time` with `grep real`; its format differs and the line never appears.

### 7. Write the reports

- `run/<app>/results.md`: outcome, how it was built, metrics, visual check, editability, friction.
- `run/comparison.md`: one scoreboard table, the visual difference, a verdict with a clear "use A when, use B when", caveats, and follow-ups.
- Templates: [references/report-templates.md](references/report-templates.md). Keep every claim backed by a measurement from step 6.

## Gotchas learned (pc-vs-vc)

- **Style inheritance.** VectorCraft objects inherit the last fill and stroke; set paint explicitly per object in the driver.
- **Path caps.** PhotoCraft allows 4096 knots per path; chunk if a prompt exceeds it. VectorCraft took 60,000 points in one path.
- **Timing.** Sub-second runs are startup-dominated and a cold first run is slower. Say a small gap is not meaningful.
- **Line weight.** PhotoCraft's brush drew about 0.7 px heavier than its nominal size; VectorCraft's SVG records the exact stroke width. Compare apps with the same measurement method, not against the spec.
- **Output formats.** PNG export from PhotoCraft flattens layers (it warns); save the native file too.
- **Project rules.** Author files with the editor tools (Write and Edit); there is no per-write size limit. Generated data and app exports are tool output, not authored files.

## Variations

Swap the prompt (Truchet tiles, phyllotaxis, L-system fern, Penrose, clouds with a gradient map) or the pair (PhotoCraft vs a built-in filter route, VectorCraft vs another app that can draw). Keep the layout and metrics so results stay comparable across benchmarks.



