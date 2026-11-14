"""Search every ArtCraft app's commands by text. Live, read-only, stdout only.
Usage: python3 -I find.py QUERY... [--app SLUG] [--limit N] [--readonly] [--json]
All query words must match (id, label, or params). Ranking: id > label > params."""
import glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import artcraft_cmds

REG = os.path.join(HERE, "..", "registry")


def score(rec, words):
    cid, lab, par = rec["id"].lower(), rec["label"].lower(), rec["params"].lower()
    total = 0
    for w in words:
        s = 0
        if w in cid.split("."):
            s += 15
        elif w in cid:
            s += 10
        if w in lab:
            s += 6
        if w in par:
            s += 2
        if s == 0:
            return 0
        total += s
    return total


def main(argv):
    opts = {"--app": None, "--limit": "15"}
    words, flags, i = [], set(), 0
    while i < len(argv):
        a = argv[i]
        if a in opts:
            opts[a] = argv[i + 1]
            i += 2
            continue
        (flags.add(a) if a.startswith("--") else words.append(a.lower()))
        i += 1
    slugs = [opts["--app"]] if opts["--app"] else sorted(
        os.path.basename(f)[:-5] for f in glob.glob(REG + "/*.json"))
    hits = []
    for s in slugs:
        try:
            recs = artcraft_cmds.load(s)
        except (SystemExit, Exception) as e:
            print("skip %s: %s" % (s, e), file=sys.stderr)
            continue
        for r in recs:
            if "--readonly" in flags and not r["readonly"]:
                continue
            sc = score(r, words)
            if sc:
                hits.append((sc, r))
    hits.sort(key=lambda h: (-h[0], h[1]["app"], h[1]["id"]))
    hits = hits[:int(opts["--limit"])]
    if "--json" in flags:
        print(json.dumps([h[1] for h in hits]))
        return
    for sc, r in hits:
        print("%s | %s | %s | %s%s" % (r["app"], r["id"], r["label"],
              r["params"][:90], "" if r["readonly"] else "  [mutates?]"))
    print("%d shown" % len(hits), file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1:])
