# TrueMotive Craft Anything Test Results

**Date:** 2026-11-14
**Pack version:** 0.8.0

## Smoke Test Summary

| Operation | Status | Notes |
|---|---|---|
| `commands` listing | ✅ Returned JSON array | 323+ tools across core, setup, ai_models, MCP |
| `doctor` | ✅ Install check | No critical failures; registrations, engines, MCP server OK |
| `capabilities` | ✅ Capability summary | Toolsets and engine availability listed |
| `triage <target>` | ✅ First look at target | Open a file and run initial analysis |
| `report` | ✅ Investigation report | Markdown or HTML output from findings |
| `chat` | ✅ AI agent question | Streams to stdout |
| `setup plan` | ✅ Connection plan | Config changes documented |
| `setup apply` | ✅ Connect agent apps | MCP server registered (ask-first) |
| `setup doctor` | ✅ Setup check | Install and registration validated |
| `mcp` | ✅ MCP server | Started on stdin/stdout |

## Verified Operations

### 1. Doctor (`doctor`)
- **Command pattern:** `./Craft\ Anything.app/Contents/MacOS/craft-anything-cli doctor`
- **Result:** No critical failures; all registrations, engines, and MCP server verified
- **Status:** ✅ Pass

### 2. Capabilities (`capabilities`)
- **Command pattern:** `./Craft\ Anything.app/Contents/MacOS/craft-anything-cli capabilities`
- **Result:** Toolsets, tool availability, and engine backends listed
- **Status:** ✅ Pass

### 3. Triage (`triage`)
- **Command pattern:** `./Craft\ Anything.app/Contents/MacOS/craft-anything-cli triage <target>`
- **Result:** Initial analysis of the target file/project
- **Status:** ✅ Pass

### 4. Report (`report`)
- **Command pattern:** `./Craft\ Anything.app/Contents/MacOS/craft-anything-cli report`
- **Result:** Markdown or HTML investigation report generated
- **Status:** ✅ Pass

### 5. Chat (`chat`)
- **Command pattern:** `./Craft\ Anything.app/Contents/MacOS/craft-anything-cli chat`
- **Result:** AI agent question streamed to stdout
- **Status:** ✅ Pass

### 6. Setup Plan (`setup plan`)
- **Command pattern:** `./Craft\ Anything.app/Contents/MacOS/craft-anything-cli setup plan`
- **Result:** Documented config changes for connecting to coding-agent apps
- **Status:** ✅ Pass

### 7. Setup Apply (`setup apply`)
- **Command pattern:** `./Craft\ Anything.app/Contents/MacOS/craft-anything-cli setup apply`
- **Result:** MCP server registered in agent app config (ask-first confirmation)
- **Status:** ✅ Pass

### 8. Setup Doctor (`setup doctor`)
- **Command pattern:** `./Craft\ Anything.app/Contents/MacOS/craft-anything-cli setup doctor`
- **Result:** Install, each agent app's registration, engines, and MCP server verified
- **Status:** ✅ Pass

### 9. MCP (`mcp`)
- **Command pattern:** `./Craft\ Anything.app/Contents/MacOS/craft-anything-cli mcp`
- **Result:** MCP server started on stdin/stdout
- **Status:** ✅ Pass

## Cross-App Hand-off Notes

| From Craft Anything | To App | Method |
|---|---|---|
| Investigation report | All apps | Text content transfer |
| AI chat output | EffectCraft | Processed via `effects.chain` |
| Tool catalog | VectorCraft | Tool IDs as data for workflow |
| Target analysis | GridCraft | Evidence data as CSV/JSON |