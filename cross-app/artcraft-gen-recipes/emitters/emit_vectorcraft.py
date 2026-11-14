"""shapes.json -> VectorCraft JSON-lines commands on stdout. Writes no files.
Usage: python3 -I emit_vectorcraft.py SHAPES.json|- NAME |    (- reads stdin)
       vectorcraft-cli run --commands - --export DIR/NAME.svg --export DIR/NAME.png --export DIR/NAME.vectorcraft
Each layer becomes ONE compound path (polygons closed, polylines open), named
after the layer. Paint is set explicitly because new objects inherit the last
fill and stroke."""
import json, sys

d = json.load(sys.stdin if sys.argv[1] == "-" else open(sys.argv[1]))
name = sys.argv[2]


def cmd(command, **params):
    print(json.dumps({"command": command, "params": params},
                     separators=(",", ":")))


def sub(pts, closed):
    body = " L".join("%s %s" % (x, y) for x, y in pts)
    return "M" + body + (" Z" if closed else "")


cmd("file.new", width=d["width"], height=d["height"], units="Pixels", name=name)
cmd("shape.rectangle", x=0, y=0, width=d["width"], height=d["height"])
cmd("paint.setFill", color=d["background"])
cmd("paint.setStroke", none=True)
cmd("object.setProps", name="Background")
for L in d["layers"]:
    parts = [sub(p, True) for p in L.get("polygons", [])]
    parts += [sub(p, False) for p in L.get("polylines", [])]
    cmd("path.create", d=" ".join(parts))
    if L.get("fill"):
        cmd("paint.setFill", color=L["fill"])
    else:
        cmd("paint.setFill", none=True)
    if L.get("stroke"):
        cmd("paint.setStroke", color=L["stroke"])
        cmd("stroke.set", weight=L.get("stroke_width", 2), join="round", cap="round")
    else:
        cmd("paint.setStroke", none=True)
    cmd("object.setProps", name=L["name"])
cmd("document.inspect", depth=1)
