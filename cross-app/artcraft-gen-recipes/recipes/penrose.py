"""Penrose P3 tiling (Robinson triangle subdivision) -> neutral shapes.json.
Usage: python3 -I penrose.py LEVELS > shapes.json     (6 gives about 1,500 triangles)
Two fill colours (thick and thin rhombs) plus navy edge lines. Verified in
both apps: see the pc-vs-vc benchmark's earlier Penrose test."""
import json, math, sys

levels = int(sys.argv[1])
W = H = 512
PHI = (1 + 5 ** 0.5) / 2
R = 420
mix = lambda a, b, t: (a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t)
tris = []
for i in range(10):
    B = (math.cos((2 * i - 1) * math.pi / 10), math.sin((2 * i - 1) * math.pi / 10))
    C = (math.cos((2 * i + 1) * math.pi / 10), math.sin((2 * i + 1) * math.pi / 10))
    tris.append((0, (0.0, 0.0)) + ((C, B) if i % 2 == 0 else (B, C)))
for _ in range(levels):
    out = []
    for c, A, B, C in tris:
        if c == 0:
            P = mix(A, B, 1 / PHI)
            out += [(0, C, P, B), (1, P, C, A)]
        else:
            Q, X = mix(B, A, 1 / PHI), mix(B, C, 1 / PHI)
            out += [(1, X, C, A), (1, Q, X, B), (0, X, Q, A)]
    tris = out
px = lambda p: [round(W / 2 + p[0] * R, 2), round(H / 2 + p[1] * R, 2)]
fills, edges = {0: [], 1: []}, []
for c, A, B, C in tris:
    a, b, cc = px(A), px(B), px(C)
    if any(-20 <= x <= W + 20 and -20 <= y <= H + 20 for x, y in (a, b, cc)):
        fills[c].append([a, b, cc])
        edges.append([cc, a, b])
print(json.dumps({"width": W, "height": H, "background": "#0b132b",
    "layers": [{"name": "Thick rhombs", "fill": "#f2b705", "polygons": fills[0]},
               {"name": "Thin rhombs", "fill": "#1fa2a6", "polygons": fills[1]},
               {"name": "Edges", "fill": None, "stroke": "#0b132b",
                "stroke_width": 1.5, "polylines": edges}]}))
