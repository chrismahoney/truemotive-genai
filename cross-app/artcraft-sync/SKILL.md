---
name: artcraft-sync
description: Propagate improvements across ArtCraft app skills - record a finding as a lesson with a capability predicate, see which apps it applies to, test it in each compatible app, update those skills, and log evidence in the ledger. Use after onboarding or improving any app skill, when a bug or limit found in one app might affect others, or to audit which lessons are still pending.
---

# ArtCraft sync (propagating improvements)

Improvements found in one app should reach every app they apply to. The ledger `_shared/lessons.json` plus the evaluator make that repeatable. Work in `/Users/chris/Claude/AntiVoxel/truemotive-genai/`.

## See the state

```sh
python3 -I _shared/adapters/sync.py [--lesson ID] [--app SLUG] [--todo]
```

One row per lesson, one column per app. `A` applied (with evidence), `P` compatible but pending, `?` the predicate needs a flag that is still `null` (probe the app first), `-` not applicable. `--todo` lists every `P` and `?` cell. Applicability comes from the app's registry flags, so it stays correct as flags are probed.

## The protocol

Run it at the end of every app onboarding and whenever a skill improves.

1. **Record.** Write each new finding as a lesson in `lessons.json`: `id`, `found_in`, `date`, `text` (one sentence, imperative), and `requires`, a list of clauses over [capability flags](../../_shared/capabilities.md): `flag`, `!flag`, `flag=value`, `flag!=value`. An empty list means every app. Universal guidance (view the output, report warnings) belongs in [artcraft-qa](../artcraft-qa/SKILL.md) or the root skill instead, not in a lesson.
2. **Evaluate.** Run `sync.py --lesson ID`. Incompatible apps show `-` automatically; do not edit them.
3. **Resolve `?` cells.** Probe the missing flag in that app (run its `--help` or a command), write the value into its registry row, and re-run.
4. **Test each `P` cell** in that app with the smallest command that would show the lesson holding or not. Keep the command.
5. **Apply.** If it holds, add one line to that app's skill (a small edit in the right section) and record `{"state": "applied", "evidence": "<the command and what it showed>"}` under the lesson's `status`. If it does not hold, add a clause to `requires` that excludes the app, or note it and leave the cell pending with a reason. Never mark applied without a test.
6. **Re-lint** every touched skill (`lint.py DIR --app SLUG`) and note the change in `PACK.md`'s changelog.

## Worked example (first run, 2026-11-14)

Lesson `readonly-classification` (found while probing AniCraft, whose registry has a native `mutates` flag) was compatible with every app that lists commands, and pending in PhotoCraft and VectorCraft. For each, the test was `find.py inspect --readonly --app <slug>`, which returned inspection commands, so one line was added to each skill's Discover section and the ledger was updated. See the ledger entry for the evidence.

The seed lessons from PhotoCraft and VectorCraft already predict later work: `style-inheritance` and `select-before-act` are pending for CADCraft, DesignCraft and FigCraft (all object-model apps), and `units-not-pixels` is pending for DeckCraft, GridCraft and SolidCraft. Check the matrix when onboarding each of them.

## Rules

- A lesson is a tested fact, not a guess. If you cannot test it in an app yet, leave the cell pending.
- Keep lesson text short and app-neutral; the app skill's line may add the app's own command names.
- Lessons found in a **later** app flow back to **earlier** apps through the same loop. That is what the `P` cells are for.
- Do not edit `-` cells. If the predicate is wrong, fix the predicate.
- The ledger and the registry flags are the only shared state: update them in the same change as the skill edits.

