"""Truchet quarter-arc tiling -> neutral shapes.json on stdout. Writes no files.
Usage: python3 -I truchet.py SEED N > shapes.json     (N x N tiles on 512x512)
Each tile randomly joins one pair of opposite corners with quarter-circle arcs."""
import json, math, random, sys

seed, n = int(sys.argv[1]), int(sys.argv[2])
W = H = 512
t = W / n
rng = random.Random(seed)


def arc(cx, cy, a0, r, steps=10):
    pts = []
    for k in range(steps + 1):
        a = math.radians(a0 + 90.0 * k / steps)
        pts.append([round(cx + r * math.cos(a), 2), round(cy + r * math.sin(a), 2)])
    return pts


lines = []
for i in range(n):
    for j in range(n):
        x, y = i * t, j * t
        if rng.random() < 0.5:
            lines += [arc(x, y, 0, t / 2), arc(x + t, y + t, 180, t / 2)]
        else:
            lines += [arc(x + t, y, 90, t / 2), arc(x, y + t, 270, t / 2)]
print(json.dumps({"width": W, "height": H, "background": "#f4efe6",
                  "layers": [{"name": "Truchet arcs", "fill": None,
                              "stroke": "#1b4965", "stroke_width": 6,
                              "polylines": lines}]}))
