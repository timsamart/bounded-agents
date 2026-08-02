#!/usr/bin/env python3
"""Verify internal anchors in build/spine.html after a PDF/HTML build."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
HTML = ROOT / "build" / "spine.html"


def main() -> int:
    if not HTML.exists():
        print(f"Missing {HTML}; run build_spine_pdf.py first", file=sys.stderr)
        return 1
    text = HTML.read_text(encoding="utf-8")
    ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    hrefs = re.findall(r'href=["\'](#[^"\']+)["\']', text)
    missing: list[str] = []
    for href in hrefs:
        frag = unquote(urlparse(href).fragment)
        if frag and frag not in ids:
            missing.append(frag)
    missing = sorted(set(missing))
    print(f"Anchors: {len(ids)}  Internal links: {len(hrefs)}  Missing: {len(missing)}")
    for m in missing[:40]:
        print(f"  missing #{m}")
    if len(missing) > 40:
        print(f"  … and {len(missing) - 40} more")
    # Forward-ref markers are expected; citation-needed too.
    cn = len(re.findall(r"citation-needed", text))
    fr = len(re.findall(r"forward-ref", text))
    print(f"citation-needed spans: {cn}  forward-ref spans: {fr}")
    # Fail only if TOC chapter targets missing.
    required = [f"ch-{i}" for i in range(1, 22)] + [
        "part-i",
        "part-ii",
        "part-iii",
        "part-iv",
        "references",
        "cover",
    ]
    bad = [r for r in required if r not in ids]
    if bad:
        print("Required ids missing:", ", ".join(bad), file=sys.stderr)
        return 1
    return 1 if missing and len(missing) > 25 else 0


if __name__ == "__main__":
    raise SystemExit(main())
