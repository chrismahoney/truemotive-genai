---
name: truemotive-<slug>
description: <What the app creates and edits, in one sentence>, through its headless CLI, <MCP or control port if any>. Use for <typical requests> or any request to work in <AppName>.
---

# TrueMotive <AppName>

<One paragraph: what the app is, its command count (from `artcraft-apps`), what its output is, and when to use a different Craft app instead. Link ../../artcraft-skill/SKILL.md for routing.>

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `<cli path from _shared/registry/<slug>.json>` |
| GUI | `<bundle>/Contents/MacOS/<gui>` |
| Protocol doc | `<~/.claude/skills/<slug>/references/control-protocol.md, or "none">` (grep it, never read it whole) |
| Quick reference | In the filled-in skill, link `references/command-quickref.md` here as a markdown link |

## Choose a session

| Need | Use |
|---|---|
| Unattended file output | `<run syntax from the registry, verified>` |
| One command | `<single-command form>` |
| Agent tool calls | `<mcp form, if the flag is true>` |
| The user's open window | `<control port and auth, if desktop_control is set>` |

Check whether the GUI is running first (`artcraft-apps`). Note any file-access roots.

## Discover shapes, don't guess

Use `artcraft-find` (`find.py QUERY --app <slug>`) for a command, and the registry's `describe` form if the app has one. Start from the quick reference; the live registry wins when they differ.

## Editing model and standard flow

<Describe how this app differs: objects vs pixels vs cells vs timeline, units, selection model, defaults that bite. Then a numbered flow that was actually run: create, add content, style, inspect, save/export, view.>

## Procedural and generative notes

<What this app can generate, caps and limits found by testing, and which `artcraft-gen-recipes` emitter exists. Mark everything verified or "not yet run".>

## Save, export, verify

<Native format and export formats, warnings to read, background-save behaviour. Verify with `artcraft-qa`.>

## Jobs, failures, and uncertain outcomes

<Is a batch a transaction? Long-running commands? What to inspect after a timeout.>

## Cross-app hand-offs

<Routes to and from other apps, linking `artcraft-handoff`. List only what was run.>

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/`.

