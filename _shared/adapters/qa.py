"""Check ArtCraft output files. Read-only, stdout only, no dependencies.
Usage: python3 -I qa.py FILE... [--size WxH]    Exit 1 if any file FAILs.
Statuses: OK, WARN (suspicious), FAIL (missing, empty, unreadable, or blank)."""
import collections, json, os, struct, sys, zipfile, zlib
import xml.etree.ElementTree as ET

DRAW = {"path", "polygon", "rect", "circle", "ellipse", "line", "polyline",
        "text", "image", "use"}
MAX_PIXELS = 4000000


def paeth(a, b, c):
    p = a + b - c
    pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
    return a if pa <= pb and pa <= pc else (b if pb <= pc else c)


def unfilter(raw, w, h, bpp):
    stride, prev, pos, rows = w * bpp, bytearray(w * bpp), 0, []
    for _ in range(h):
        f, line = raw[pos], bytearray(raw[pos + 1:pos + 1 + stride])
        pos += 1 + stride
        if f == 2:
            line = bytearray((x + y) & 255 for x, y in zip(line, prev))
        elif f in (1, 3, 4):
            for i in range(stride):
                a = line[i - bpp] if i >= bpp else 0
                b, c = prev[i], (prev[i - bpp] if i >= bpp else 0)
                d = a if f == 1 else (a + b) // 2 if f == 3 else paeth(a, b, c)
                line[i] = (line[i] + d) & 255
        rows.append(line)
        prev = line
    return rows


def check_png(data):
    w, h, depth, ctype, _, _, inter = struct.unpack(">IIBBBBB", data[16:29])
    info = "PNG %dx%d" % (w, h)
    bpp = {2: 3, 6: 4}.get(ctype)
    if depth != 8 or inter or not bpp or w * h > MAX_PIXELS:
        return "WARN", info + " (pixels not checked)", w, h
    idat, pos = b"", 8
    while pos < len(data):
        n, kind = struct.unpack(">I4s", data[pos:pos + 8])
        if kind == b"IDAT":
            idat += data[pos + 8:pos + 8 + n]
        pos += 12 + n
    rows = unfilter(zlib.decompress(idat), w, h, bpp)
    if bpp == 4 and not any(max(r[3::4]) for r in rows):
        return "FAIL", info + ", fully transparent", w, h
    seen = collections.Counter()
    for r in rows:
        seen.update(zip(r[0::bpp], r[1::bpp], r[2::bpp]))
    top = seen.most_common(1)[0][1] / float(w * h)
    st = "FAIL" if top > 0.999 else ("WARN" if top > 0.98 else "OK")
    return st, "%s, %d colours, dominant %.1f%%" % (
        info, len(seen), 100 * top), w, h


def check_svg(data):
    root = ET.fromstring(data)
    if not root.tag.endswith("svg"):
        return "FAIL", "root is not <svg>", 0, 0
    n = sum(1 for e in root.iter() if e.tag.split("}")[-1] in DRAW)
    return ("OK" if n else "FAIL"), "SVG %sx%s, %d drawable elements" % (
        root.get("width"), root.get("height"), n), 0, 0


def check_jpeg(data):
    i = 2
    while i + 9 < len(data):
        if data[i] != 0xFF:
            i += 1
            continue
        m = data[i + 1]
        if m in (0xC0, 0xC1, 0xC2):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            ok = data[-2:] == b"\xff\xd9"
            return ("OK" if ok else "WARN"), "JPEG %dx%d%s (pixels not checked)" % (
                w, h, "" if ok else ", no end marker"), w, h
        if m == 0xD8 or m == 0x01 or 0xD0 <= m <= 0xD7:
            i += 2
        else:
            i += 2 + struct.unpack(">H", data[i + 2:i + 4])[0]
    return "WARN", "JPEG without a frame header", 0, 0


def check(path):
    if not os.path.isfile(path):
        return "FAIL", "missing", 0, 0
    data = open(path, "rb").read()
    if not data:
        return "FAIL", "empty file", 0, 0
    try:
        if data[:8] == b"\x89PNG\r\n\x1a\n":
            return check_png(data)
        if data[:3] == b"\xff\xd8\xff":
            return check_jpeg(data)
        if b"<svg" in data[:400]:
            return check_svg(data)
        if data[:4] == b"%PDF":
            ok = b"%%EOF" in data[-1024:]
            return ("OK" if ok else "WARN"), "PDF, %s" % (
                "EOF marker found" if ok else "no EOF marker"), 0, 0
        if data[:4] == b"GIF8":
            w, h = struct.unpack("<HH", data[6:10])
            frames = data.count(b"\x21\xf9\x04")
            ok = data[-1:] == b";"
            return ("OK" if ok else "WARN"), "GIF %dx%d, %d frames%s (pixels not checked)" % (
                w, h, frames, "" if ok else ", no trailer"), w, h
        if data[4:8] == b"ftyp":
            ok = b"moov" in data
            return ("OK" if ok else "WARN"), "MP4/MOV container, %s" % (
                "moov atom found" if ok else "no moov atom"), 0, 0
        if data[:1] == b"{":
            doc = json.loads(data)
            return "OK", "JSON document, %d top-level keys" % len(doc), 0, 0
        if zipfile.is_zipfile(path):
            n = len(zipfile.ZipFile(path).namelist())
            return "OK", "ZIP container, %d entries" % n, 0, 0
    except Exception as e:
        return "FAIL", "unreadable: %s" % e, 0, 0
    return "WARN", "%d bytes, format not recognised" % len(data), 0, 0


def main(argv):
    want, files, i = None, [], 0
    while i < len(argv):
        if argv[i] == "--size":
            want = tuple(int(x) for x in argv[i + 1].split("x"))
            i += 2
        else:
            files.append(argv[i])
            i += 1
    bad = 0
    for f in files:
        st, msg, w, h = check(f)
        if want and w and (w, h) != want:
            st, msg = "FAIL", "%s, expected %dx%d" % (msg, want[0], want[1])
        bad += st == "FAIL"
        size = os.path.getsize(f) if os.path.isfile(f) else 0
        print("%-4s %s | %s | %d bytes" % (st, f, msg, size))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main(sys.argv[1:])
