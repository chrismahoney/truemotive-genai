"""Evaluate lesson compatibility across ArtCraft apps. Read-only, stdout only.
Usage: python3 -I sync.py [--lesson ID] [--app SLUG] [--todo]
Cell: A applied | P compatible but pending | ? needs a probe (flag is null) | - n/a
Lessons live in ../lessons.json; app flags in ../registry/<slug>.json."""
import glob, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SHARED = os.path.join(HERE, "..")


def load_registry():
    rows = {}
    for f in sorted(glob.glob(os.path.join(SHARED, "registry", "*.json"))):
        rows[os.path.basename(f)[:-5]] = json.load(open(f))
    return rows


def truthy(v):
    return v not in (None, False, "none", "")


def clause(flags, c):
    """True or False, or None when the flag has not been probed (null)."""
    neg = c.startswith("!") and "=" not in c
    key = c.lstrip("!")
    for op in ("!=", "="):
        if op in key:
            k, want = key.split(op, 1)
            have = flags.get(k)
            if have is None:
                return None
            return (str(have) == want) == (op == "=")
    have = flags.get(key)
    if have is None:
        return None
    return truthy(have) != neg


def cell(lesson, slug, row):
    st = lesson.get("status", {}).get(slug)
    verdicts = [clause(row["flags"], c) for c in lesson["requires"]]
    if False in verdicts:
        return "-"
    if None in verdicts:
        return "?"
    return "A" if st and st["state"] == "applied" else "P"


def main(argv):
    rows = load_registry()
    lessons = json.load(open(os.path.join(SHARED, "lessons.json")))["lessons"]
    if "--lesson" in argv:
        want = argv[argv.index("--lesson") + 1]
        lessons = [l for l in lessons if l["id"] == want]
    slugs = [argv[argv.index("--app") + 1]] if "--app" in argv else list(rows)
    print("%-22s %s" % ("lesson", " ".join(s[:4].ljust(4) for s in slugs)))
    todo = []
    for l in lessons:
        cells = [cell(l, s, rows[s]) for s in slugs]
        print("%-22s %s" % (l["id"], " ".join(c.ljust(4) for c in cells)))
        todo += [(l["id"], s, c) for s, c in zip(slugs, cells) if c in "P?"]
    print("\nA applied | P compatible, pending | ? probe a flag first | - n/a")
    if "--todo" in argv:
        for lid, s, c in todo:
            print("TODO %s %s %s" % (c, lid, s))


if __name__ == "__main__":
    main(sys.argv[1:])
