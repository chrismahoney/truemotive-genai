# TrueMotive Craft Anything Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.8.0
**Test files used (filename only):** (craft-anything-cli doctor/capabilities outputs; project folder *.cany)

## Pipeline Configuration 1: Command Listing

**Command:** `craft-anything-cli commands`

**Test:** List all available tools

```bash
./Craft\ Anything.app/Contents/MacOS/craft-anything-cli commands
```

**Result:** Lists every tool as a JSON object with `command`, `title`, `summary`, `tool`, and `toolset`.

**Verification:** JSON array returned successfully with expected categories (core, setup, core_target, ai_models, etc.).

**Notes:**
- 323+ tools catalogued across core, setup, ai_models, and MCP toolsets
- Tool IDs are dotted (e.g., `core-target-open`) and validate via `lint.py --app craft-anything`
- `--format` global option controls output: `json|jsonl|md|text|csv|tsv` (default: json)
- `--project <PROJECT>` creates a `*.cany` project folder for evidence/memory/journal

## Pipeline Configuration 2: Doctor + Capabilities

**Command:** `craft-anything-cli doctor` / `craft-anything-cli capabilities`

**Test:** Check install and report capabilities

```bash
./Craft\ Anything.app/Contents/MacOS/craft-anything-cli doctor
./Craft\ Anything.app/Contents/MacOS/craft-anything-cli capabilities
```

**Result:** Diagnostic output and capability summary.

**Verification:** No critical failures reported; toolsets and engine availability listed.

**Notes:**
- `doctor` checks install, registrations, engines, AI backends, and MCP server
- `capabilities` reports toolsets, tool availability, and engine backends
- Both commands support `--format` for output customization