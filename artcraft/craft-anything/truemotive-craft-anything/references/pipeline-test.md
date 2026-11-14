# TrueMotive Craft Anything Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.8.0
**Test files used (filename only):** (craft-anything-cli doctor/capabilities outputs; project folder *.cany)

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/Craft\ Anything.app/Contents/MacOS/craft-anything-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/Craft\ Anything.app/Contents/MacOS/Craft Anything` |
| Protocol doc | none (CLI help is the source of truth) |

## Choose a session

| Need | Use |
|---|---|
| One tool operation on a file or target | `craft-anything-cli <tool> [key=value …]` (output format `--format json|jsonl|md|text|csv|tsv`) |
| Many operations batched via script | `craft-anything-cli run --script steps.json [--root DIR] [--report]` |
| MCP server (stdin/stdout) | `craft-anything-cli mcp [--root DIR] [--compact] [--automation-read-root DIR] [--automation-write-root DIR]` |
| Agent tool calls | `craft-anything-cli mcp` (headless) or live app through control port |
| The user's open window | Desktop `Craft Anything --control PORT --control-token-file F`. A headless session never edits it. |

## Discover tools, don't guess

`craft-anything-cli commands` lists every tool as a JSON object with `command`, `title`, `summary`, `tool`, and `toolset`. Run `craft-anything-cli commands` and filter via `python3 -I`; never print a whole one. Core tools include: `core_target_open`, `core_target_close`, `core_session_show`, `core_targets_list`, `core_target_select`, `native_cursor_show`, `core_evidence_show`, `core_evidence_export`, `core_evidence_import`, `rebuild_check`, `assets_key_status`, `assets_key_set`, `assets_key_remove`, `ai_models_list`, `ai_model_set`, `ai_model_options_show`, `ai_model_options_set`, `setup_plan`, `setup_apply`, `setup_doctor`, `setup_uninstall`, and many more.

Standard flow:
1. `craft-anything-cli doctor` — check the install, registrations, engines, AI backends and the MCP server
2. `craft-anything-cli capabilities` — what this install can do: toolsets, tool availability, engines
3. `craft-anything-cli triage <target>` — open a file and run a first look at it
4. `craft-anything-cli report` — write a readable investigation report (Markdown or HTML) from findings and evidence
5. `craft-anything-cli chat` — ask the AI agent a question about a target (streams to stdout)
6. `craft-anything-cli setup plan` — what connecting Craft Anything to coding-agent apps would change
7. `craft-anything-cli setup apply` — connect Craft Anything to coding-agent apps: register its MCP server
8. `craft-anything-cli setup doctor` — check the install, each agent app's registration, engines, and that the MCP server answers
9. `craft-anything-cli mcp` — run the MCP server on stdin/stdout

## Standard flow (AntiVoxel)

- MCP ports and tokens must not be reused across apps.
- Project folders (`*.cany`) store evidence, memory and the journal; created if missing.
- Project defaults to the project this tool server works for.
- `--format` after a tool name goes to the tool; `--format` global option sets output format (json|jsonl|md|text|csv|tsv, default: json).

## Cross-app hand-offs

| From Craft Anything | To App | Method |
|---|---|---|
| Investigation report | All apps | Text content transfer |
| AI chat output | EffectCraft | Processed via `effects.chain` |
| Tool catalog | VectorCraft | Tool IDs as data for workflow |
| Target analysis | GridCraft | Evidence data as CSV/JSON |

## Save

| Command | Description |
|---|---|
| `craft-anything-cli doctor` — check the install, registrations, engines, AI backends and the MCP server |
| `craft-anything-cli capabilities` — toolsets, tool availability, engine availability |
| `craft-anything-cli triage <target>` — open a file and run a first look at it |
| `craft-anything-cli report` — write a readable investigation report (Markdown or HTML) from findings and evidence |
| `craft-anything-cli chat` — ask the AI agent a question about a target (streams to stdout) |
| `craft-anything-cli setup plan` — what connecting Craft Anything to coding-agent apps would change |
| `craft-anything-cli setup apply` — connect Craft Anything to coding-agent apps: register its MCP server |
