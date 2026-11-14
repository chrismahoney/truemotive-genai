# TrueMotive SolidCraft Command Quick Reference

**Pack version:** 0.7.0 (2026-11-14)
**Source:** `solidcraft-cli commands` registry, N commands captured.

Call shape: `solidcraft-cli <command> [json-params]`

## Session Management

| Command | Description |
|---|---|
| `session.new` | Create new design session |
| `session.run <script.json|design.sc|part.step>` | Run design script or open design |
| `session.save` | Persist `.sc` design to disk |
| `session.save <FILE>` | Save design to specified file |
| `session.exec <command> [json-params]` | Execute a single command on current design |

## Sketch Operations

| Command | Description |
|---|---|
| `sketch.create plane: XY|XZ|YZ [origin: [x,y,z]] [x_dir: [x,y,z]] [y_dir: [x,y,z]] [name: name]` | Create new sketch on plane |
| `sketch.edit sketch: id|name [restore_marker: position|false]` | Edit sketch by marker |
| `sketch.finish [restore_marker: position|false]` | Finish current sketch |

## Part Features

| Command | Description |
|---|---|
| `part.features feature: extrude|revolve|loft|rib|pattern|hole [params]` | Add feature to part |
| `part.export format: STL|OBJ|STEP [--quality standard|fine|finest] [--out FILE]` | Export part in format |
| `part.convert format: STL|OBJ|STEP [--quality standard|fine|finest] [--out FILE]` | Convert format |

## Query/Inspect

| Command | Description |
|---|---|
| `solidcraft-cli commands` | List all engine commands |
| `solidcraft-cli describe <command_id>` | Describe one command's details |
| `solidcraft-cli eval <script.json|design.sc|part.step>` | Evaluate script without side effects |

## Conversion

| Command | Description |
|---|---|
| `solidcraft-cli convert format: STL|OBJ|STEP [--quality standard|fine|finest] [--out FILE]` | Convert format |

## Project Conventions (AntiVoxel)

- Prefer editable results (parametric histories, feature history) over baked meshes
- Use `stopOnError: true` for batch operations; read every result before retrying
- Long commands wait by default; poll `results` before dependent edits with `wait:false`
- After timeout/disconnect, inspect design before replaying a mutation
- If write target already exists, look at it first; delete only partial outputs you created