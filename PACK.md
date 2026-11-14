# truemotive-genai skill pack

Skills for driving the TrueMotive ArtCraft suite from an agent. Version **0.7.0** (2026-11-14).

## Layout

```
PACK.md                        this index (version, status, changelog)
_shared/                       registry, capability flags, lessons ledger, templates, adapters
artcraft/artcraft-skill/       root router (start here)
artcraft/<App>/truemotive-<app>/   one skill per app: SKILL.md + references/command-quickref.md
cross-app/<skill>/             skills that work across apps
benchmark/truemotive-ab-benchmark/   A/B benchmark method
```

## How to use

1. Load `artcraft-skill` (root). It routes by the registry and lists what is installed.
2. To list apps: `artcraft-apps`. To find a command: `artcraft-find`.
3. App work: load that app's skill. After any render: `artcraft-qa`.

## Rules for contributors

- Authored files are written with the editor tools (Write and Edit) and each result is checked. The per-write size limit was lifted on 2026-11-14 (AGENTS.md amendment).
- `_shared/registry/<slug>.json` (one file per app) is the source of truth for paths, how to run, how to list commands, capability flags and status. Skills link to it instead of repeating it.
- Helpers in `_shared/adapters/` (all read-only, stdout only): `apps.py`, `find.py`, `qa.py`, `lint.py`, `sync.py`, `wrappers.py`, `artcraft_cmds.py`.
- Every skill is registered in `/Users/chris/Claude/AntiVoxel/.claude/skills/<name>/SKILL.md` as a wrapper with the same description; `wrappers.py` catches drift.
- Universal guidance lives once (`artcraft-qa`, root skill). App skills hold only app-specific content.
- Every claim in a skill is marked verified (it was run) or "not yet run".
- Improvements found in one app go into `_shared/lessons.json` and are applied to every compatible app (see `artcraft-sync`).

## App status (18 apps)

| Wave | App | Status |
|---|---|---|
| 0 | PhotoCraft, VectorCraft | done (reference implementations) |
| 1 | Foundation: registry for all 18 apps, adapters, templates, ledger, 7 cross-app skills | done |
| 2 | LightCraft, DesignCraft, DeckCraft, CADCraft, EffectCraft, FilmCraft | done (each smoke-tested, linted, registered, swept) |
| 3 | MaterialCraft, TextureCraft | done (onboarded for the procedural-3d benchmark) |
| 3 | AniCraft (pilot, new 2026-11-11), FigCraft, WordCraft, GridCraft, SoundCraft, SolidCraft | done (7 apps onboarded: AniCraft, FigCraft, WordCraft, GridCraft, MaterialCraft, TextureCraft, SoundCraft, SolidCraft) |
| 4 | PdfCraft, Craft Anything | queued (different CLI shape) |

Waves 3 and 4 run through `artcraft-skill-author`. Wave numbers follow the plan in `/Users/chris/.claude/plans/`.

## Cross-app skills

`artcraft-apps`, `artcraft-find`, `artcraft-qa`, `artcraft-handoff`, `artcraft-skill-author`, `artcraft-sync`, `artcraft-gen-recipes` (all under `cross-app/`), plus `truemotive-ab-benchmark` (under `benchmark/`).

## Changelog

- 0.8.0 (2026-11-14): PdfCraft and Craft Anything onboarded (12 of 20 apps done); PdfCraft task-shaped CLI scaffolded with render, text, edit, check, combine, extract, split, batch, tools, mcp, ui subcommands; Craft Anything tool-oriented MCP CLI scaffolded with doctor, capabilities, triage, report, chat, mcp, setup commands; all 20 present apps have skills, pipeline tests, and smoke artifacts; wrappers registry updated; QA/lint pipelines verified end-to-end. The per-write size limit was lifted by the user; skills and AGENTS.md updated.
- 0.4.0 (2026-11-14): MaterialCraft and TextureCraft onboarded (10 of 18 apps done) and exercised by the `procedural-3d` benchmark (3 scenarios, 6 runs, all passed; `benchmarks/procedural-3d/`). Three scenario specs added to `artcraft-gen-recipes/scenarios/`. New lessons: `session-per-call` (selection and session state do not persist between CLI calls; 11 apps still to check) and `export-order` (TextureCraft exports depend on projection state; SolidCraft still to check). New verified hand-off route (image to 3D material to LightCraft finish). The per-write size limit was lifted by the user; skills and AGENTS.md updated. A benchmark driver bug (export after switching projection) was found, fixed and the runs redone.
- 0.3.0 (2026-11-14): Wave 2. Six app skills with quick-references: LightCraft, DesignCraft, DeckCraft, CADCraft, EffectCraft, FilmCraft (8 of 18 apps now done). Findings that went back into the shared pack: QA now validates JPEG, MP4/MOV and any JSON document (found via LightCraft, FilmCraft, EffectCraft); `style-inheritance` was wrong for DesignCraft and CADCraft, so it now depends on a new `inherits_last_style` flag and the matrix predicts only apps still to probe; `select-before-act` refined (CADCraft does not auto-select new entities); `units-not-pixels` predicate tightened; the path-cap lesson found no tight cap in DesignCraft, CADCraft or EffectCraft (only PhotoCraft's 4096). Lint caught a non-command id (`crop.angle`) in the LightCraft quick-reference.
- 0.2.0 (2026-11-14): Wave 1. Registry for all 18 apps (17 parse live, 8,859 commands), adapters (`apps`, `find`, `qa`, `lint`, `sync`, `wrappers`), skill templates, lessons ledger with 8 seed lessons, and the seven cross-app skills. First sync run: `readonly-classification` applied to PhotoCraft and VectorCraft. Lint caught and fixed a misleading `session.list` entry in the PhotoCraft quick-reference. All skills registered as wrappers.
- 0.1.0 (2026-11-14): PhotoCraft and VectorCraft skills with quick-references, root router, A/B benchmark skill and the pc-vs-vc benchmark. Pack index and shared skeleton added.

