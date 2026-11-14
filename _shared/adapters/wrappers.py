"""Check that .claude/skills registration wrappers match the pack's skills.
Read-only, stdout only. Usage: python3 -I wrappers.py   (exit 1 on any problem)
A wrapper is .claude/skills/<name>/SKILL.md: same name and description as the
real skill, plus the absolute path of the real file in its body."""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.normpath(os.path.join(HERE, "..", ".."))
SKILLS = os.path.normpath(os.path.join(PACK, "..", ".claude", "skills"))


def description(path):
    m = re.search(r"^description:\s*(.*)$", open(path).read(), re.M)
    return m.group(1) if m else None


real = []
for pattern in ("artcraft/*/*", "artcraft/*", "cross-app/*", "benchmark/*"):
    real += glob.glob(os.path.join(PACK, pattern, "SKILL.md"))
bad = 0
for r in sorted(real):
    name = os.path.basename(os.path.dirname(r))
    w = os.path.join(SKILLS, name, "SKILL.md")
    if not os.path.isfile(w):
        print("MISSING wrapper:", name)
        bad += 1
    elif description(w) != description(r):
        print("DRIFT description:", name)
        bad += 1
    elif r not in open(w).read():
        print("WRONG PATH in wrapper:", name)
        bad += 1
print("%d skills, %d problem(s)" % (len(real), bad))
sys.exit(1 if bad else 0)
