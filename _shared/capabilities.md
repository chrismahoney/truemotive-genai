# Capability flags

Every app row in `app-registry.json` has a `flags` object using these keys. Lessons in `lessons.json` use them in `requires` predicates, so `artcraft-sync` can decide which apps a lesson applies to.

## Flags

| Flag | Type | Meaning |
|---|---|---|
| `batch_stdin` | bool | Headless batch of commands from stdin or a script file |
| `run_single` | bool | Run one command from the shell |
| `serve` | bool | Long-lived JSON-lines session over stdio or TCP |
| `mcp_headless` | bool | `mcp` runs a headless session |
| `mcp_bridge` | bool | `mcp` can attach to a running app |
| `desktop_control` | string | `none`, `port`, or `port+token` |
| `roots_flags` | bool | Read and write root flags confine file access |
| `render_cli` | bool | CLI renders a document to an image |
| `convert_cli` | bool | CLI converts formats by extension |
| `commands_list` | string | `json`, `text` (any of three text layouts; the adapter handles all), or `none` |
| `describe` | bool | `describe <id>` explains one command |
| `mutates_flag` | bool | Registry marks mutating commands natively |
| `object_model` | string | `pixel`, `object`, `cells`, `timeline`, `3d`, `audio`, `doc`, `pages`, `graph` (node graphs), `tools` |
| `units` | string | Default document units (`px`, `pt`, `mm`, `none`) |
| `path_commands` | bool | Has commands that take explicit path geometry |
| `inherits_last_style` | bool | New objects inherit the last-used fill and stroke (object-model apps; always probe, never assume: VectorCraft true, DesignCraft false) |

## Predicates

A `requires` predicate is a list of clauses that must all hold. Each clause is `flag` (true), `!flag` (false), or `flag=value`. Example: `["object_model=object", "path_commands"]`.

An app is **compatible** when every clause holds for its flags. Unknown flag values count as **not yet known**: probe the app before applying, never assume.
