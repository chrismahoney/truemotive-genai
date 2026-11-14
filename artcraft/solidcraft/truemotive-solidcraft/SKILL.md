---
name: truemotive-solidcraft
description: Create and edit 3D solid models, generate meshes, and export STEP/STL/OBJ in SolidCraft (TrueMotive ArtCraft) via its CLI, JSON-lines server, or MCP bridge. Use for parametric 3D modeling, mesh generation, format conversion, or any request to work in SolidCraft.
---

# TrueMotive SolidCraft

3D solid modeling and parametric design in the ArtCraft suite (verified commands, checked 2026-11-14). Supports sketch-based modeling, feature-based design, mesh generation, and format conversion. If the result should stay editable (parametric history, design objects), use the native `.sc` design format; for flat exports, use STEP, STL, or OBJ.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/SolidCraft.app/Contents/MacOS/solidcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/SolidCraft.app/Contents/MacOS/SolidCraft` |
| Protocol doc | none (CLI help is the source of truth) |

## Choose a session

| Need | Use |
|---|---|
| One design script or batch of commands | `solidcraft-cli run <script.json\|design.sc\|part.step>` (prints JSON results, then bounces, saves and inspects) |
| Single command on a design | `solidcraft-cli exec <command> [json-params]` |
| Agent tool calls | `solidcraft-cli mcp` (headless) or `mcp --bridge 127.0.0.1:PORT --control-token-file F` (live app) |
| The user's open window | Desktop `SolidCraft --control PORT --control-token-file F`. A headless session never edits it. |

Run `ps aux | grep -i solidcraft` first. Never trust a PID from notes; if no GUI runs, headless is correct for file output.

## Discover shapes, don't guess

`solidcraft-cli commands` (or `engine.commands`) returns a bare array of `{id, label, params, enabled, needsDocument, disabledReason}`. `params` is a doc-string with types, ranges, and defaults. Dump it once to the scratchpad and filter it with `python3 -I`; never print all rows. Start from the CLI help for the major commands.

Standard flow:
1. `solidcraft-cli run <script.json\|design.sc\|part.step>` (opens or creates a design)
2. `sketch.create` (plane: XY\|XZ\|YZ, origin, x_dir, y_dir) - creates a new sketch
3. Sketch editing: `sketch.edit` (sketch, restore_marker), `sketch.finish` (finish the sketch)
4. `part.features` (add features: extrude, revolve, etc.)
5. `part.export` (export STL, OBJ, STEP; quality: standard\|fine\|finest)
6. `session.save` to persist `.sc` design

Prefer editable results (parametric designs, feature history) over baked meshes when they suit the request.

## Jobs, failures, and uncertain outcomes

- `batch` is not a transaction. Use `stopOnError: true`, read every result, and inspect `history` before retrying anything.
- Long commands wait by default; with `wait:false` poll `results` before dependent edits.
- After a timeout or disconnect, inspect the design before replaying a mutation.
- If a write target already exists, look at it first. Delete only partial outputs you created yourself.

## Cross-app hand-offs

- Solid to vector: export STEP from SolidCraft, then use VectorCraft `import.step` or `imageTrace.make` on a derived mesh.
- Solid to raster: export STL/OBJ, then use PhotoCraft `doc.place` or `filter.render.*` for texturing.
- Do not copy ports or auth flags between apps. SolidCraft MCP uses a token file; other apps use different bridges.

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad. Save test outputs to `artifacts-test/solidcraft/`.

Reference run: verify `solidcraft-cli run` with a simple `sketch.create` on a new design, 0 failures.

## Command Quick Reference (subset)

### Session Management
```
solidcraft-cli run <script.json\|design.sc\|part.step>
solidcraft-cli exec <command> [json-params]
solidcraft-cli eval <script.json\|design.sc\|part.step>
solidcraft-cli script <design.sc\|script.json>
solidcraft-cli session.save
```

### Sketch Operations
```
solidcraft-cli sketch.create plane: XY\|XZ\|YZ [origin: [x,y,z]] [x_dir: [x,y,z]] [y_dir: [x,y,z]] [name: name]
solidcraft-cli sketch.edit sketch: id\|name [restore_marker: position\|false]
solidcraft-cli sketch.finish [restore_marker: position\|false]
```

### Part Features
```
solidcraft-cli part.features feature: extrude\|revolve\|loft\|rib\|pattern\|hole [params]
solidcraft-cli part.export format: STL\|OBJ\|STEP [--quality standard\|fine\|finest] [--out FILE]
```

### Conversion
```
solidcraft-cli convert format: STL\|OBJ\|STEP [--quality standard\|fine\|finest] [--out FILE]
```

### Query/Inspect
```
solidcraft-cli commands
solidcraft-cli describe <command_id>
```

---