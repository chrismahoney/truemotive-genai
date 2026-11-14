"""List ArtCraft apps: registry row, CLI, GUI running, skill, command count.
Usage: python3 -I apps.py [--counts] [--json]     (read-only, prints to stdout)
Scans $ARTCRAFT_ROOT/*.app, so a newly installed app shows up as NEW."""
import glob, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.normpath(os.path.join(HERE, "..", ".."))
REG = os.path.join(PACK, "_shared", "registry")
ROOT = os.environ.get("ARTCRAFT_ROOT",
                      "/Users/chris/Claude/TrueMotive/artcraft-root")
sys.path.insert(0, HERE)


def slug(name):
    return name.lower().replace(" ", "-")


def process_paths():
    return subprocess.run(["ps", "-axo", "comm="], capture_output=True,
                          text=True).stdout


def scan(counts):
    ps = process_paths()
    rows = {}
    for f in glob.glob(os.path.join(REG, "*.json")):
        rows[os.path.basename(f)[:-5]] = json.load(open(f))
    apps = sorted(os.path.basename(a)[:-4]
                  for a in glob.glob(os.path.join(ROOT, "*.app")))
    out = []
    for app in apps:
        s, r = slug(app), rows.get(slug(app))
        rec = {"app": app, "slug": s, "registered": r is not None,
               "gui_running": (app + ".app/Contents/MacOS/") in ps}
        if r:
            sk = r["skill"]
            rec.update(wave=r["wave"], status=r["status"],
                       cli=os.path.exists(r["cli"]),
                       skill=bool(sk and os.path.exists(
                           os.path.join(PACK, sk, "SKILL.md"))))
            if counts and r["commands"]["format"] != "none":
                import artcraft_cmds
                rec["commands"] = len(artcraft_cmds.load(s))
        out.append(rec)
    return out, sorted(set(rows) - {x["slug"] for x in out})


def main():
    recs, orphans = scan("--counts" in sys.argv)
    if "--json" in sys.argv:
        print(json.dumps({"apps": recs, "registry_without_app": orphans}))
        return
    yn = lambda b: "yes" if b else "no"
    print("%-15s %-4s %-8s %-5s %-6s %-4s %s" %
          ("app", "wave", "status", "cli", "skill", "gui", "commands"))
    for r in recs:
        if not r["registered"]:
            print("%-15s NEW: not in the registry. Add _shared/registry/%s.json"
                  % (r["app"], r["slug"]))
            continue
        print("%-15s %-4s %-8s %-5s %-6s %-4s %s" % (
            r["app"], r["wave"], r["status"], yn(r["cli"]), yn(r["skill"]),
            yn(r["gui_running"]), r.get("commands", "-")))
    new = [r["app"] for r in recs if not r["registered"]]
    print("\n%d apps, %d registered, %d new" %
          (len(recs), len(recs) - len(new), len(new)))
    if orphans:
        print("registry rows with no installed app:", ", ".join(orphans))


if __name__ == "__main__":
    main()
