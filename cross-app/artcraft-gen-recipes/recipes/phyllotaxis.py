"""Phyllotaxis (golden-angle sunflower) -> neutral shapes.json on stdout.
Usage: python3 -I phyllotaxis.py N > shapes.json      (N dots on 512x512)
Dots are 12-sided polygons, split into three colour bands by index."""
import json, math, sys

n = int(sys.argv[1])
W = H = 512
GOLDEN = math.radians(137.50776405)
c = W / 2
spacing = (W * 0.46) / math.sqrt(n)
bands = [[], [], []]
for i in range(n):
    r, a = spacing * math.sqrt(i), i * GOLDEN
    x, y = c + r * math.cos(a), c + r * math.sin(a)
    dot = 1.5 + 4.5 * (i / n)
    poly = [[round(x + dot * math.cos(math.radians(30 * k)), 2),
             round(y + dot * math.sin(math.radians(30 * k)), 2)]
            for k in range(12)]
    bands[min(2, 3 * i // n)].append(poly)
colors = ["#ffd166", "#ef476f", "#06d6a0"]
print(json.dumps({"width": W, "height": H, "background": "#0b132b",
                  "layers": [{"name": "Dots %d" % (k + 1), "fill": colors[k],
                              "stroke": None, "polygons": bands[k]}
                             for k in range(3)]}))
