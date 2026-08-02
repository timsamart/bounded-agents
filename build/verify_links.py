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
    for m in missing[:50]:
        print(f"  missing #{m}")
    if len(missing) > 50:
        print(f"  … and {len(missing) - 50} more")
    cn = len(re.findall(r'class="citation-needed"', text))
    print(f"citation-needed spans: {cn}")
    required = [f"ch-{i}" for i in range(1, 22)] + [
        "part-i",
        "part-ii",
        "part-iii",
        "part-iv",
        "references",
        "cover",
        "appendix-a",
        "appendix-b",
    ] + [f"adr-{i:02d}" for i in range(1, 40)]
    # Sample of appendix markers used in spine
    for marker in ["a-1-1", "a-2-0", "a-4-2", "a-6-1", "a-7-1", "a-8-1"]:
        required.append(marker)
    bad = [r for r in required if r not in ids]
    if bad:
        print("Required ids missing:", ", ".join(bad), file=sys.stderr)
        return 1
    if cn:
        print("citation-needed spans remain in HTML", file=sys.stderr)
        return 1
    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
