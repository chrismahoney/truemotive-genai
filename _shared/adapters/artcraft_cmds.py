"""Normalise any ArtCraft app's command registry. Reads only; prints to stdout.

Library: load(slug) -> [{app, id, label, params, readonly}]
CLI:     python3 -I artcraft_cmds.py SLUG     (one JSON object per line)

Registry rows live in ../registry/<slug>.json. Two input forms exist:
  json  a JSON array of command objects (or {"result": [...]})
  text  `id  label  [shortcut]  [{params}]` lines, `id — label: {params}`
        lines, or an id line followed by indented parameter lines.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REG = os.path.join(HERE, "..", "registry")
ID = re.compile(r"^([A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z0-9_]+)+)\*?(?:\s+|$)")
# Judge only the last segment of the id (the action word), and only an EXACT
# match: "find.replace" is a replace, "developer.checkBox" inserts a control and
# "styles.inspectorClear" clears, so prefix matching is unsafe. A match means
# "probably read-only"; anything else is treated as possibly mutating. Tested
# against the native flags of AniCraft (240 commands: 0 misses) and WordCraft
# (670: 2 misses, both UI-state toggles a name cannot reveal). Registries with a
# native flag override this guess.
READ = re.compile(
    r"^(get|list|info|inspect|describe|find|query|read|count|status"
    r"|check|preview|help|sample|capabilities)$", re.I)


def guess_readonly(cid):
    return bool(READ.match(cid.split(".")[-1]))


def clean(s, n=400):
    return re.sub(r"\s+", " ", s).strip()[:n]


def from_json(data):
    if isinstance(data, dict):
        data = data.get("result", data.get("commands", []))
    out = []
    for c in data:
        cid = c.get("id") or c.get("command")
        p = c.get("params") or c.get("summary") or ""
        if not isinstance(p, str):
            p = json.dumps(p)
        ro = (not c["mutates"]) if "mutates" in c else guess_readonly(cid)
        out.append({"id": cid, "label": clean(str(c.get("label") or c.get("title") or "")),
                    "params": clean(p), "readonly": ro})
    return out


def from_text(text):
    recs, cur = [], None
    for line in text.splitlines():
        m = None if (not line or line[0].isspace()) else ID.match(line)
        if m:
            rest = line[m.end():].strip()
            if rest.startswith("—"):
                rest = rest[1:].strip()
            if ": {" in rest:
                label, _, params = rest.partition(": ")
            else:
                f = re.split(r"\s{2,}", rest)
                label = f[0]
                params = " ".join(x for x in f[1:] if x.startswith("{"))
            cur = {"id": m.group(1), "label": label, "params": params}
            recs.append(cur)
        elif cur and line.strip():
            cur["params"] += " " + line.strip()
    return [{"id": r["id"], "label": clean(r["label"]),
             "params": clean(r["params"]),
             "readonly": guess_readonly(r["id"])} for r in recs]


def load(slug):
    row = json.load(open(os.path.join(REG, slug + ".json")))
    c = row["commands"]
    if c["format"] == "none":
        return []
    p = subprocess.run([row["cli"]] + c["argv"], input=c.get("stdin"),
                       capture_output=True, text=True, timeout=90)
    head = p.stdout.lstrip()[:1]
    if head in ("[", "{") or c["format"] == "json":
        recs = from_json(json.loads(p.stdout))
    else:
        recs = from_text(p.stdout)
    if not recs:
        sys.exit("no commands parsed for %s (check registry/%s.json)" % (slug, slug))
    for r in recs:
        r["app"] = row["name"]
    return recs


if __name__ == "__main__":
    for r in load(sys.argv[1]):
        print(json.dumps(r, ensure_ascii=False))
