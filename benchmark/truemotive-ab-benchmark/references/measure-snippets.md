# Measurement snippets

All pure Python 3 (run with `python3 -I`), no PIL or numpy. Keep outputs in the session scratchpad, never in the benchmark's `output/` dirs.

## 1. Wall time (3 runs, median)

Run into scratch dirs so the real outputs are not overwritten. Report the first run separately: it is the cold start.

```python
import subprocess, time, statistics, sys
# usage: python3 -I timing.py REQUEST.jsonl CMD [ARGS...]
req, cmd = sys.argv[1], sys.argv[2:]
runs = []
for _ in range(3):
    t = time.perf_counter()
    subprocess.run(cmd, stdin=open(req), stdout=subprocess.DEVNULL,
                   stderr=subprocess.DEVNULL)
    runs.append(time.perf_counter() - t)
print([round(r, 2) for r in runs], "median", round(statistics.median(runs), 2))
```

Absolute times drift between sessions (the same VectorCraft run measured 0.12 s in one session and 0.04 s in a later one), so treat sub-second gaps as noise and only compare runs made back to back.

Give each repeat its own write root or export path (`$SCRATCH/t-a/0`, `/1`, `/2`) if the app refuses to overwrite.

## 2. PNG to BMP for pixel work

```sh
sips -s format bmp A.png --out "$SCRATCH/a.bmp"
sips -s format bmp B.png --out "$SCRATCH/b.bmp"
```

## 3. Pixel difference (mean, % over 32, max)

```python
import struct, sys
def load(p):
    b = open(p, "rb").read()
    off = struct.unpack_from("<I", b, 10)[0]
    w, h, _, bpp = struct.unpack_from("<iiHH", b, 18)
    neg, h, bpp = h < 0, abs(h), bpp // 8
    row = (w * bpp + 3) // 4 * 4
    img = []
    for y in range(h):
        o = off + (y if neg else h - 1 - y) * row
        img.append([(b[o+i*bpp+2], b[o+i*bpp+1], b[o+i*bpp]) for i in range(w)])
    return w, h, img
w, h, A = load(sys.argv[1]); _, _, B = load(sys.argv[2])
tot = w * h; s = big = mx = 0
for y in range(h):
    for x in range(w):
        d = [abs(A[y][x][i] - B[y][x][i]) for i in range(3)]
        s += sum(d) / 3; big += max(d) > 32; mx = max(mx, max(d))
print("mean %.3f | >32: %.2f%% | max %d" % (s / tot, 100 * big / tot, mx))
```

Usage: `python3 -I diff.py a.bmp b.bmp`. Images must be the same size.

## 4. Feature width (lines, strokes)

Take edge midpoints from the shared geometry, step along each edge's normal in 0.1 px increments over +/-10 px, and sum the steps where the pixel is within 40 of the line colour (for example `#1a1a1a` is 26, 26, 26). Skip short edges (under 60 px) and edges near the border. Report the median over all sampled edges, using the same method for both apps. The Voronoi run sampled 220 edges.

## 5. Editability round-trip

- VectorCraft: `vectorcraft-cli run --in X.vectorcraft --commands -` with `document.find {name}`, then `select.set {ids}`, then one `paint.setFill`, and `--export` an SVG. Diff old and new fill lists.
- PhotoCraft: `photocraft-cli info X.pcraft` for the layer list, then edit a layer property through `run` and compare the PNG.

