# Craft Anything command quick reference

**Pack version:** 0.8.0 (2026-11-14)
**Source:** `craft-anything-cli commands` registry (tool-oriented, JSON list of tool IDs).
**Lint note:** Every backticked ID in this file is validated against the live `craft-anything-cli commands` output via `lint.py --app craft-anything`. IDs must match exactly.

## Core Tools (first 30)

| Command | Title | Toolset |
|---|---|---|
| `core-target-open` | Open | core |
| `core-target-close` | Close | core |
| `core-session-show` | Session status | core |
| `core-targets-list` | List open targets | core |
| `core-target-select` | Switch target | core |
| `native-cursor-show` | Where am I | native |
| `core-evidence-show` | Evidence so far | core |
| `core-evidence-export` | Export evidence | core |
| `core-evidence-import` | Import evidence | core |
| `rebuild-check` | Check my build | core |
| `assets-key-status` | Is an asset key set up? | setup |
| `assets-key-set` | Save an asset key | setup |
| `assets-key-remove` | Remove an asset key | setup |
| `ai-models-list` | List an agent's models | setup |
| `ai-model-set` | Choose an agent's model and thinking | setup |
| `ai-model-options-show` | Show model options | setup |
| `ai-model-options-set` | Set model options | setup |
| `setup-plan` | What connecting agent apps would change | setup |
| `setup-apply` | Connect agent apps | setup |
| `setup-doctor` | Check the install | setup |
| `setup-uninstall` | Disconnect agent apps | setup |

## Investigation Tools

| Command | Title | Toolset |
|---|---|---|
| `rebuild` | Study a website, app or game and have a coding agent rebuild it | core |
| `rebuild-check` | Check my build | core |
| `assets-key-status` | Whether each asset provider has a key | setup |
| `assets-key-set` | Store an asset provider's key | setup |
| `assets-key-remove` | Remove an asset provider's stored key | setup |
| `ai-models-list` | List the visible chat models | setup |
| `ai-model-set` | Save a configured coding agent's model | setup |
| `ai-model-options-set` | Save a Copilot backend's context tier | setup |

## Interaction Tools

| Command | Title | Toolset |
|---|---|---|
| `chat` | Ask the AI agent a question about a target | setup |
| `report` | Write a readable investigation report | core |
| `triage` | Open a file and run a first look | core |
| `doctor` | Check the install, registrations, engines, AI backends and the MCP server | setup |
| `capabilities` | What this install can do: toolsets, tool availability, engines | setup |
| `setup-plan` | What connecting agent apps would change | setup |
| `setup-doctor` | Check the install, each agent app's registration, engines, and that the MCP server answers | setup |

## MCP and Setup

| Command | Title | Toolset |
|---|---|---|
| `mcp` | Run the MCP server on stdin/stdout | core |
| `help` | Print this message or the given subcommand's help | core |

## Project conventions (AntiVoxel)

- Every backticked command ID in this file is validated against `craft-anything-cli commands` via `lint.py --app craft-anything`.
- MCP ports and tokens must not be reused across apps.
- Project folders (`*.cany`) store evidence, memory and the journal; created if missing.
- Project defaults to the project this tool server works for.
- `--format` after a tool name goes to the tool; `--format` global option sets output format.

**Note:** This quickref is a subset of the full tool catalog (323+ tools). Only include IDs that an agent needs first; expand as required.