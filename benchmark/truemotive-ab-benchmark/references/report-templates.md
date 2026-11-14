# Report templates

Fill every `<...>`. Delete nothing from the metrics tables, so benchmarks stay comparable.

## README.md

```markdown
# Benchmark: <AppA> vs <AppB> (<short prompt name>)

## The prompt (identical for both apps)
> <one paragraph: canvas, counts, seed, palette, line weights, deliverables>

## Fairness rules
- Same data: shared/<generator> computes <what> once into shared/<file>.json.
- Headless CLI for both. One attempt each plus at most one fix-and-rerun.
- Canvas <WxH>, background <hex>, <other fixed styling>.

## Metrics
Success | Wall time | Commands | Visual fidelity | Editability | Output size | Friction

## Layout / Reproduce
<tree of the folders, and the three commands that regenerate everything>
```

## run/<app>/results.md

```markdown
# <App> results
Skill used: <skill>. Run date: <date>. <how it was run>
## Outcome   (success or failure, retries, artifact table with sizes)
## How it was built   (numbered steps, command counts, payload size)
## Metrics   (commands, wall time median of 3, feature width, native structure)
## Visual check   (seams, gaps, edges, deviations from the prompt)
## Editability   (what can be changed alone; the round-trip result)
## Friction   (limits hit, errors, retries)
```

## run/comparison.md

```markdown
# <AppA> vs <AppB>: <prompt name>
Same prompt, same data, both headless on <date>. Details: links to both results.md.
## Scoreboard
| Metric | <AppA> | <AppB> |
|---|---|---|
| Success | | |
| Commands sent | | |
| Request payload | | |
| Wall time (median of 3) | | |
| PNG size | | |
| Native file | | |
| Other deliverable | | |
| Feature width (spec <n>) | | |
| Native structure | | |
| Edit one element | | |
| Scales to any size | | |
## Visual difference   (mean abs diff, % over 32, max, where it concentrates)
## Verdict   (who wins and why; "use A when, use B when")
## Caveats   (sample size, timing noise, measurement method, encoders)
## Suggested follow-ups   (hybrid pipeline, scale test, feedback into skills)
```

## Verdict wording

State the winner for the task, not in general. Name what each app is better at, and say plainly when a gap is within noise. Never claim more than the measurements support.

