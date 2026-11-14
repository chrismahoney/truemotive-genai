---
name: artcraft-skill
description: Central router for the TrueMotive ArtCraft suite (PhotoCraft, VectorCraft, and other Craft apps). Use when a request involves generating or editing images, vector art, or documents and the right Craft app is not named, when chaining apps (for example vector to raster), or to find which ArtCraft skills are installed. Discovers per-app skills under artcraft/<AppName>/ and delegates to them.
---

# TrueMotive ArtCraft (root skill)

This skill picks the right ArtCraft app and hands off to that app's skill. It owns routing, discovery, and shared rules; each app skill owns the details of one app.

## Discover installed app skills (do this first)

Skill packs live at `/Users/chris/Claude/AntiVoxel/truemotive-genai/artcraft/<AppName>/<skill-name>/SKILL.md`. List them instead of trusting any table below:

```sh
ls /Users/chris/Claude/AntiVoxel/truemotive-genai/artcraft/*/*/SKILL.md
```

Each hit is one usable app skill. Read its `name` and `description` frontmatter to confirm what it covers. A Craft app **without** a folder here has no skill yet (see "Apps without a skill").

## Use a sub-skill

1. If the harness lists the sub-skill by name (for example `truemotive-photocraft`), invoke it with the Skill tool.
2. Otherwise Read its SKILL.md by absolute path and follow it as written. Its relative links (`references/...`) resolve from its own folder.
3. Load only the app skill(s) the task needs, then follow that skill's own rules.

## Route the request

| The result is... | Use |
|---|---|
| Photos, textures, painted or filtered pixels, layered PSD, blend modes, masks | PhotoCraft |
| Logos, icons, SVG/PDF/EPS, plotter or print art, geometric generators (tilings, spirographs, L-systems), editable type | VectorCraft |
| Large path counts from a generator | VectorCraft (60,000 points in one path worked; PhotoCraft caps a path at 4096 knots) |
| Noise, clouds, lighting, filters on a generated image | PhotoCraft |
| Both vector and raster qualities | Build vector in VectorCraft, export PNG, finish in PhotoCraft |

## Side-by-side

| | PhotoCraft | VectorCraft |
|---|---|---|
| CLI | `PhotoCraft.app/Contents/MacOS/photocraft-cli` | `artcraft-root/bin/vectorcraft-cli` |
| Batch mode | `serve` (JSON lines, `batch`) or `run --cmd` | `run --commands -` (JSON lines) |
| Desktop control | port 7878, token file | port 7979, no auth |
| Model | pixels on layers, work path then fill | objects, new object becomes the selection |
| Default units | pixels | points (set `units:"Pixels"`) |
| Registry | `photocraft-cli commands` (1009) | `vectorcraft-cli commands` (966) |

Both: discover param shapes from the registry, inspect before and after editing, and report real output paths and warnings.

## Apps without a skill

Run `artcraft-apps` for the live list. It scans the install and joins the registry in `_shared/registry/`, so it also reports newly installed apps (AniCraft appeared on 2026-11-11) and shows `skill: no` for any app not yet onboarded. For such an app: read `<cli> --help`, use `artcraft-find QUERY --app SLUG` to see its commands, apply the shared rules below, and offer to onboard it with `artcraft-skill-author`.

## Pipelines across apps

- Vector to raster: VectorCraft `--export x.png`, then PhotoCraft `doc.place` (documented, not yet run here).
- Raster to vector: PhotoCraft saves a PNG, VectorCraft `file.open` then `imageTrace.make`.
- Share files through one directory per task (for example `artifacts-test/`) and give each app a read or write root for it. Never reuse ports, tokens, or flags across apps.

## Shared rules

- Prefer headless CLI for file output; touch a user's live window only through that app's own control port.
- Check `ps aux | grep -i <app>` before assuming a GUI is running.
- Dump a registry once to the scratchpad and filter it; never print a whole one.
- Verify output by viewing the image, then report paths and warnings.
- Project files are written with the editor tools (Write and Edit), with each result checked; there is no per-write size limit (AGENTS.md amendment, 2026-11-14).

## Related cross-app skills

These live beside `artcraft/` in the pack, not under an app folder. Load the one that matches the request:

| Skill | Use it when |
|---|---|
| [artcraft-apps](../../cross-app/artcraft-apps/SKILL.md) | Which apps exist, what state each is in, is an app new |
| [artcraft-find](../../cross-app/artcraft-find/SKILL.md) | Which command or app does X; exact command ids and params |
| [artcraft-qa](../../cross-app/artcraft-qa/SKILL.md) | After any render, export or save: check and view the output |
| [artcraft-handoff](../../cross-app/artcraft-handoff/SKILL.md) | Moving work between apps (vector to raster, trace to vector) |
| [artcraft-gen-recipes](../../cross-app/artcraft-gen-recipes/SKILL.md) | Generating patterns or tilings, same art in two apps |
| [artcraft-skill-author](../../cross-app/artcraft-skill-author/SKILL.md) | Adding or rebuilding an app skill |
| [artcraft-sync](../../cross-app/artcraft-sync/SKILL.md) | Applying an improvement to every compatible app |
| [truemotive-ab-benchmark](../../benchmark/truemotive-ab-benchmark/SKILL.md) | Comparing two apps on one prompt (example: `benchmarks/pc-vs-vc/`) |

## Add a new app

Use [artcraft-skill-author](../../cross-app/artcraft-skill-author/SKILL.md): it probes the CLI, writes the registry row, scaffolds `artcraft/<AppName>/truemotive-<appname>/SKILL.md` and `references/command-quickref.md` from `_shared/templates/`, smoke-tests, lints, and runs the improvement sweep. Verify every claim by running it, and mark the rest "not yet run". No root edit is needed, because discovery uses the `ls` above.


