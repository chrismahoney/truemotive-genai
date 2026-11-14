---
name: artcraft-apps
description: List the installed TrueMotive ArtCraft apps with each one's wave, status, CLI availability, whether its GUI is running, whether an app skill exists, and its live command count; detects newly installed apps that are not yet registered. Use when asked which ArtCraft apps exist, what is installed or supported, which app can do something, or before onboarding a new app.
---

# ArtCraft apps (inventory query)

Answers "which apps do we have, and what state is each in?" from the live install plus the registry, never from memory.

## Run it

```sh
python3 -I /Users/chris/Claude/AntiVoxel/truemotive-genai/_shared/adapters/apps.py --counts
```

Read-only, about 2 seconds with `--counts` (it runs each CLI's command listing). Drop `--counts` for an instant table; add `--json` for machine-readable output. Set `ARTCRAFT_ROOT` to scan a different install.

Columns: `app`, `wave` (rollout wave), `status` (`done` or `queued`), `cli` (the registered CLI path exists), `skill` (the app skill file exists), `gui` (the app's own process is running), `commands` (live registry size; `-` for PdfCraft, which has no registry).

## What it tells you

- **NEW** rows are installed apps with no registry file. AniCraft looked like this until it was registered. Tell the user, then follow [artcraft-skill-author](../artcraft-skill-author/SKILL.md) to onboard it.
- **registry rows with no installed app** means an app was removed or `ARTCRAFT_ROOT` is wrong.
- `gui: no` is normal. Headless CLIs need no GUI. Only edit a user's open window through an app that is actually running, using its own control port.

## Registry (source of truth)

One JSON file per app in `_shared/registry/<slug>.json`: bundle and CLI paths, how to run it, how to list its commands, capability `flags`, wave, status, and the app-skill path. Flags are defined in [capabilities.md](../../_shared/capabilities.md); `null` means not yet probed.

Five CLIs live **inside** the `.app` bundle (PhotoCraft, AniCraft, DesignCraft, SolidCraft, Craft Anything), the rest in `artcraft-root/bin/`. The registry holds the real path, so never guess one.

## Next steps by question

| The user asks | Do this |
|---|---|
| Which app can do X? | `artcraft-find` for X, then the app skill |
| Is app Y supported? | Check the `skill` column; if `no`, offer onboarding |
| An app is NEW | Add its registry row (probe `--help` and `commands`), then onboard |
| Which app for this task? | `artcraft-skill` (root) routing table |

Keep this skill read-only: it never edits registry rows. Updating a row happens during onboarding.

