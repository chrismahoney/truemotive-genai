---
name: artcraft-skill-author
description: Onboard an ArtCraft app into the truemotive-genai pack - probe its CLI, write its registry row, scaffold its skill and command quick-reference from the shared templates, smoke-test it, lint it, register it, and run the improvement sweep. Use when an app is NEW or queued in artcraft-apps, when asked to add or support another Craft app, or to rebuild a stale app skill.
---

# ArtCraft skill author (the onboarding loop)

Each app takes the same seven steps, so every app skill has the same shape as `truemotive-photocraft` and `truemotive-vectorcraft`. Work in `/Users/chris/Claude/AntiVoxel/truemotive-genai/`. Helpers live in `_shared/adapters/`.

## 1. Probe

1. `python3 -I _shared/adapters/apps.py` shows the app as NEW or queued.
2. Read `<cli> --help` fully. Note: how a batch is run (stdin, script file, `--cmd`), the `commands` form (flags such as `--json`, `--filter`), `describe`, `render`, `convert`, `mcp`, `app`/control port, and file-access roots.
3. Create or fix `_shared/registry/<slug>.json`. Copy the row of the most similar finished app and edit it. Fields are explained in [capabilities.md](../../_shared/capabilities.md); use `null` for flags you have not probed.
4. `python3 -I _shared/adapters/artcraft_cmds.py <slug> | wc -l` must return the app's command count. It exits with an error if a registry parses to nothing. Use `"format":"none"` only for apps with no registry (PdfCraft).
5. Run one real command (new document, one edit, one export) so the `run` field records a syntax that works, not one you read about.

## 2. Scaffold the skill

Create `artcraft/<App>/truemotive-<slug>/SKILL.md` from [app-skill.md](../../_shared/templates/app-skill.md). Fill each section from the probe, and delete any template line you cannot back up. The heading names matter: `lint.py --app` requires Installed paths, Choose a session, Discover, Standard flow, Save, Cross-app and Project conventions. The folder name must equal the frontmatter `name`.

Set `"skill"` in the registry row to `artcraft/<App>/truemotive-<slug>`.

## 3. Quick reference

Rank the families, then document the 6 to 10 an agent needs first:

```sh
python3 -I -c "import sys,collections;sys.path.insert(0,'_shared/adapters');import artcraft_cmds as a;print(collections.Counter(r['id'].split('.')[0] for r in a.load('SLUG')).most_common(25))"
```

Use [quickref.md](../../_shared/templates/quickref.md) for the layout and `find.py QUERY --app SLUG` for exact parameters. Write transport methods and CLI subcommands as plain words, not backticked IDs. Then `python3 -I _shared/adapters/lint.py artcraft/<App>/truemotive-<slug> --app <slug>` must report 0 FAIL.

## 4. Smoke test

Run the smallest real job in the app's native workflow: create a document, add some content, export an image or file, then inspect state.

- Put outputs in `artifacts-test/<slug>/` and check them with `python3 -I _shared/adapters/qa.py FILE...`, then view the image.
- Record what you actually ran. In the skill, claims you ran are stated plainly; anything else says "not yet run".
- Note limits you hit (caps, defaults that bite, style inheritance, units). These are lesson candidates for step 6.

## 5. Register

1. Registry row: set `"status": "done"` and fill every flag you verified.
2. Update the status table in `PACK.md` and add a line to its changelog; bump the pack version.
3. Register a wrapper so Claude Code lists the skill by name. With the Write tool, create `/Users/chris/Claude/AntiVoxel/.claude/skills/truemotive-<slug>/SKILL.md`: frontmatter `name` and `description` copied exactly from the real skill, and a body telling the reader to read and follow the real file by absolute path (copy any existing wrapper). Then run `python3 -I _shared/adapters/wrappers.py`; it must report 0 problems (it flags missing wrappers, changed descriptions, and wrong paths). Whenever you change a skill's description, update its wrapper in the same change.

4. Re-run `apps.py`: the app must show `skill: yes`. The root skill needs no edit, because it discovers skills with `ls artcraft/*/*/SKILL.md`.

## 6. Improvement sweep

Run [artcraft-sync](../artcraft-sync/SKILL.md) with the findings from steps 1 to 4. It records each as a lesson, applies it to every compatible earlier app, and marks the rest n/a with a reason. An app is not done until the sweep has run.

## 7. Done means

Registry row complete, skill and quick-reference written, quick-reference IDs 100% valid, smoke test passed and viewed, lint clean, wrapper registered and `wrappers.py` clean, sweep recorded.

## Special cases

- **No command registry** (PdfCraft): `"format":"none"`; hand-write the quick-reference as the list of subcommands in plain words, and skip `lint.py --app` ID checks.
- **Tool-shaped CLI** (Craft Anything): its registry lists tools with `command`, `title`, `summary`; the adapter maps those keys.
- **Text listings:** the adapter handles columns, `id — label: params`, and indented-block layouts. A row that parses to nothing fails loudly; fix the row's argv rather than editing the adapter, unless the layout is genuinely new.
- **Upstream skill exists** under `~/.claude/skills/<slug>/`: reference its `control-protocol.md` by path, never copy it, and take only what is app-specific.
- **App has no upstream docs** (AniCraft, FigCraft and others): rely on `--help`, `commands`, `describe`, and your smoke test.

