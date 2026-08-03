#!/usr/bin/env python3
"""Assemble a static site tree for GitHub Pages from the spine HTML build."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

BUILD = Path(__file__).resolve().parent
SITE = BUILD / "site"
HTML_SRC = BUILD / "spine.html"
CSS_SRC = BUILD / "spine-pdf.css"


def main() -> None:
    if not HTML_SRC.exists():
        raise SystemExit(f"Missing {HTML_SRC}; run build_spine_pdf.py first")
    if not CSS_SRC.exists():
        raise SystemExit(f"Missing {CSS_SRC}")

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)

    html = HTML_SRC.read_text(encoding="utf-8")
    # Pandoc embeds an absolute --css path; Pages needs a relative stylesheet.
    html, n = re.subn(
        r'href=(["\'])[^"\']*spine-pdf\.css\1',
        r'href=\1spine-pdf.css\1',
        html,
        count=1,
    )
    if n != 1:
        raise SystemExit("Could not rewrite spine-pdf.css href to a relative path")

    (SITE / "index.html").write_text(html, encoding="utf-8")
    shutil.copy2(CSS_SRC, SITE / "spine-pdf.css")
    (SITE / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Pages site ready at {SITE} ({(SITE / 'index.html').stat().st_size} bytes HTML)")


if __name__ == "__main__":
    main()
