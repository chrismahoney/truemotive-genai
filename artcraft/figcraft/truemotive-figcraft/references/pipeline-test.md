# TrueMotive FigCraft Pipeline Test Report

**Date:** 2026-11-14
**Pack version:** 0.7.0
**Test files used (filename only):** smoke.figcraft, probe.figcraft, probe.jsonl, select-test.jsonl (in artifacts-test/figcraft/)

## Pipeline Configuration 1: Command Listing

**Command:** `figcraft-cli commands`

**Test:** List all available engine commands

```bash
./bin/figcraft-cli commands
```

**Result:** Lists fig commands for figure/layer management, node creation, and frame operations.

**Verification:** Command array returned successfully with expected categories (node, frame, select, etc.).

**Notes:**
- Node creation commands: `node.create`, `frame.create`
- Vector types: rectangle, ellipse, polygon, star, line, arrow, text, path
- Selection and grouping operations available