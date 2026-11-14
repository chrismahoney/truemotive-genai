"""shapes.json -> PhotoCraft JSON-lines requests on stdout. Writes no files.
Usage: python3 -I emit_photocraft.py SHAPES.json|- NAME |    (- reads stdin)
       photocraft-cli serve --automation-write-root DIR     (saves NAME.png, NAME.pcraft)
Each layer: a pixel layer; polygons are filled, polygons and polylines stroked.
Paths are chunked to stay under PhotoCraft's 4096-knot per-path cap."""
import json, sys

d = json.load(sys.stdin if sys.argv[1] == "-" else open(sys.argv[1]))
name = sys.argv[2]
CAP = 3500


def chunks(items):
    out, cur, n = [], [], 0
    for closed, pts in items:
        if cur and n + len(pts) > CAP:
            out.append(cur)
            cur, n = [], 0
        cur.append((closed, pts))
        n += len(pts) + 1
    return out + ([cur] if cur else [])


def path(group):
    return {"subpaths": [{"closed": c, "knots": p} for c, p in group],
            "fillRule": "nonzero"}


def step(command, **params):
    return {"command": command, "params": params}


steps = [step("file.new", width=d["width"], height=d["height"], name=name),
         step("edit.fill", contents="color", color=d["background"])]
for L in d["layers"]:
    steps.append(step("layer.new.layer", name=L["name"]))
    polys = [(True, p) for p in L.get("polygons", [])]
    lines = [(False, p) for p in L.get("polylines", [])]
    if L.get("fill"):
        for g in chunks(polys):
            steps += [step("path.set", path=path(g)),
                      step("path.fill", color=L["fill"])]
    if L.get("stroke"):
        for g in chunks(polys + lines):
            steps += [step("path.set", path=path(g)),
                      step("path.stroke", tool="brush", hardness=1,
                           size=L.get("stroke_width", 2), color=L["stroke"])]
reqs = [{"id": 1, "method": "batch", "params": {"steps": steps, "stopOnError": True}},
        {"id": 2, "method": "doc.inspect", "params": {}},
        {"id": 3, "method": "doc.save", "params": {"path": name + ".png"}},
        {"id": 4, "method": "doc.save", "params": {"path": name + ".pcraft"}}]
for r in reqs:
    print(json.dumps(r, separators=(",", ":")))
