"""Lint an ArtCraft skill folder. Read-only, stdout only.
Usage: python3 -I lint.py SKILL_DIR [--app SLUG]
Checks: frontmatter name equals folder, links resolve; with --app also the
required sections and that every command id in references/command-quickref.md
exists in that app's live registry. Exit 1 on any FAIL."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
SECTIONS = ["Installed paths", "Choose a session", "Discover", "Standard flow",
            "Save", "Cross-app", "Project conventions"]
ID = re.compile(r"`([a-z][A-Za-z0-9]*(?:\.[A-Za-z0-9_]+)+)")


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    return dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))


def lint_basic(d, problems):
    sk = os.path.join(d, "SKILL.md")
    if not os.path.isfile(sk):
        problems.append(("FAIL", "SKILL.md missing"))
        return ""
    text = open(sk).read()
    fm = frontmatter(text)
    folder = os.path.basename(os.path.normpath(d))
    if fm.get("name") != folder:
        problems.append(("FAIL", "name %r != folder %r" % (fm.get("name"), folder)))
    if not fm.get("description"):
        problems.append(("FAIL", "description missing"))
    return text


def lint_links(d, problems):
    for root, _, files in os.walk(d):
        for f in files:
            if not f.endswith(".md"):
                continue
            for link in re.findall(r"\]\(([^)#\s]+)\)",
                                   open(os.path.join(root, f)).read()):
                target = os.path.normpath(os.path.join(root, link))
                if "://" not in link and not os.path.exists(target):
                    problems.append(("FAIL", "broken link %s in %s" % (link, f)))


def lint_ids(d, slug, problems):
    q = os.path.join(d, "references", "command-quickref.md")
    if not os.path.isfile(q):
        problems.append(("WARN", "no references/command-quickref.md"))
        return
    import artcraft_cmds
    ids = {r["id"] for r in artcraft_cmds.load(slug)}
    fam = {i.split(".")[0] for i in ids}
    bad = set()
    for t in ID.findall(open(q).read()):
        t = t.rstrip(".")
        if t.split(".")[0] in fam and t not in ids and not any(
                i.startswith(t + ".") for i in ids):
            bad.add(t)
    for t in sorted(bad):
        problems.append(("FAIL", "quickref id not in registry: " + t))


def main(argv):
    d = argv[0]
    slug = argv[argv.index("--app") + 1] if "--app" in argv else None
    problems = []
    text = lint_basic(d, problems)
    lint_links(d, problems)
    if slug:
        for s in SECTIONS:
            if s.lower() not in text.lower():
                problems.append(("WARN", "section missing: " + s))
        lint_ids(d, slug, problems)
    for level, msg in problems:
        print("%-4s %s" % (level, msg))
    bad = sum(1 for p in problems if p[0] == "FAIL")
    print("%s: %d FAIL, %d WARN" % (os.path.basename(os.path.normpath(d)), bad,
                                    len(problems) - bad))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
