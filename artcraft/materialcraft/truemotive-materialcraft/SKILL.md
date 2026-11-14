---
name: truemotive-materialcraft
description: Build procedural PBR materials as node graphs (bitmaps, filters, normals, gradients, outputs) in MaterialCraft (TrueMotive ArtCraft), cook them, export texture maps, and render them on 3D primitives, through its headless CLI, MCP server or JSON-lines server. Use to turn an image or generated geometry into a tileable material, export basecolor, normal, roughness, metallic, height and AO maps, or any request to work in MaterialCraft.
---

# TrueMotive MaterialCraft

Procedural material editor in the ArtCraft suite (112 commands, checked 2026-11-14), in the Substance Designer family: a package (`.sbs`) holds graphs of atomic nodes that cook into texture maps. It renders materials on built-in 3D primitives without a GPU. For painting directly on a mesh use TextureCraft; see [artcraft-skill](../../artcraft-skill/SKILL.md) for routing.

## Installed paths (verified)

| Item | Path |
|---|---|
| CLI | `/Users/chris/Claude/TrueMotive/artcraft-root/bin/materialcraft-cli` |
| GUI | `/Users/chris/Claude/TrueMotive/artcraft-root/MaterialCraft.app/Contents/MacOS/MaterialCraft` |
| Protocol doc | none installed; the CLI points to `docs/control-protocol.md` upstream |
| Quick reference | [references/command-quickref.md](references/command-quickref.md) |

## Choose a session

| Need | Use |
|---|---|
| New package | `materialcraft-cli new <empty\|pbr\|atomics> OUT.sbs [--size PX] [--name NAME]` (verified with `pbr`, 512) |
| One edit | `materialcraft-cli run IN.sbs COMMAND 'JSON' -o OUT.sbs` prints the result; **`-o` is required to keep the change**, so chain calls through files (verified) |
| A script | `materialcraft-cli batch script.json` (`[{"id","params"}...]` or `{"open","steps","save"}`; verified with `{"open","steps","save"}`, which keeps selection across steps) |
| Cook | `materialcraft-cli cook IN.sbs [--graph N] [--set input=value]... [--full]` returns per-node timings and errors |
| Export maps | `materialcraft-cli export IN.sbs DIR [--format png\|jpg\|tga\|tif\|bmp\|webp\|exr\|hdr] [--depth 8\|16\|32] [--size PX]` (verified: 6 PNG maps) |
| Render | `materialcraft-cli render IN.sbs OUT.png --scene rounded_cube\|cube\|sphere\|cylinder\|plane\|torus\|material_ball [--size WxH] [--tiling N] [--hq] [--yaw D --pitch D]`, or `--view 2d --node ID` for one node (verified) |
| Servers | `mcp`, `serve [--port P]` with `--read-root` and `--write-root` confining file access (not yet run) |

`IN` is a `.sbs` package or `sample`. Each CLI call is its own session; there is no GUI to be running, and `render` needs no GPU. `--set input=value` overrides a graph input before cooking.

## Discover shapes, don't guess

Use `artcraft-find QUERY --app materialcraft`, `materialcraft-cli commands --filter TEXT`, and `materialcraft-cli nodes [--filter T] [--category C]` for the node library (29 nodes: 24 atomic, including `bitmap`, `blend`, `blur`, `levels`, `normal`, `gradient_map`, `warp`, `emboss`, `transformation`). Families: `graph` 61, `file` 13, `edit` 13, `view` 8. Use `find.py --readonly` to hide commands that may change state.

## Editing model and standard flow

A graph of nodes with ports; edits address nodes by integer id. The `pbr` template starts with six output nodes (2 basecolor, 4 normal, 6 roughness, 8 metallic, 10 height, 12 ambientocclusion), each fed by a grey uniform colour, so connecting a node to an output replaces that map.

1. `new pbr OUT.sbs --size 512 --name NAME`
2. `file.importBitmap {path, name?}` to bring an image into the package's Resources
3. `graph.node.add {def:"bitmap", params:{resource:NAME}}` returns `{id}` (13 on a fresh `pbr`)
4. `graph.connect {from, to}` wires colour (`to: 2`) and height (`to: 10`); other nodes: `normal`, `levels`, `blur`, `gradient_map`, `blend`
5. `cook`, then `export` the maps and `render` previews on primitives
6. Check with `artcraft-qa` and view the renders

**Verified:** a Penrose PNG wired to basecolor and height gave a torus with the tiling wrapped on it and real relief (viewed). `graph.connect` and `file.importBitmap` print `null`/a name on success. Benchmarked on four seeds (procedural-3d S1 and S3): 16 commands built the material, exported 6 maps and rendered four views in 4.4 to 4.9 s; `graph.node.add` with `connectFrom` wires the `normal` node in one step; the exported basecolor was an exact copy of the seed every time.

**Gotchas:** every `run` needs `-o` to persist (saving over the input file works); greyscale maps (height, metallic) make `artcraft-qa` WARN because it decodes colour PNGs only, so view them. **Selection is session state and does not persist between CLI calls**, so `graph.node.param` under a plain `run` fails with "no node is selected": run `graph.select` and the edit together in `batch` (`{"open", "steps", "save"}` in a JSON file). Verified: swapping the bitmap node's `resource` that way took 0.07 s and reproduced the other seed's render exactly.

## Procedural and generative notes

Seeds are images: render a recipe (`artcraft-gen-recipes`) to PNG in PhotoCraft or VectorCraft, import it as a bitmap, and use it as colour, height or both. Vector sources (`file.importVector`, SVG) keep their original bytes. A generated tiling is not automatically seamless; check edges or render with `--tiling 3`.

## Save, export, verify

Native `.sbs` (`file.save`, or `-o`). `export` cooks at full size and writes every output, named `<graph>_<identifier>.<ext>` (verified: `PenroseMat_basecolor.png` and five more). `file.exportMaterial {path}` writes a portable `.mcmat` for TextureCraft.

## Cross-app hand-offs

- Recipe PNG in from PhotoCraft or VectorCraft (verified). See [artcraft-handoff](../../../cross-app/artcraft-handoff/SKILL.md).
- To TextureCraft: `file.sendToTextureCraft {graph?}` exports the graph as a material into TextureCraft's library folder (`Documents/TextureCraft/library`); not yet run.
- Renders out to LightCraft for a tonal finish (verified: `lightcraft-cli render IN -o OUT --set light.exposure=0.3` on MaterialCraft renders).

## Project conventions (AntiVoxel)

Write project files with the editor tools (Write and Edit) and check each result; there is no per-write size limit (AGENTS.md amendment, 2026-11-14). Keep scratch generators in the session scratchpad and test outputs in `artifacts-test/materialcraft/`.

