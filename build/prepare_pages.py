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
ICONS_SRC = BUILD / "assets" / "icons.svg"

CHROME = """
<nav class="site-chrome" id="site-chrome" aria-label="Document navigation">
  <a href="#TOC">Contents</a>
  <a href="#cover">Cover</a>
  <span class="site-chrome-progress" id="site-progress" aria-live="polite">Bounded Agents</span>
  <span class="site-chrome-bar" id="site-progress-bar" aria-hidden="true"></span>
</nav>
<script>
(function () {
  const progress = document.getElementById("site-progress");
  const bar = document.getElementById("site-progress-bar");
  const markers = Array.from(document.querySelectorAll(
    "#part-i, #part-ii, #part-iii, #part-iv, [id^=ch-], #front-matter, #references, [id^=appendix-]"
  )).filter((el) => el.id);
  function nearest() {
    let best = null;
    let bestTop = -Infinity;
    const y = window.scrollY + 72;
    for (const el of markers) {
      const top = el.getBoundingClientRect().top + window.scrollY;
      if (top <= y && top >= bestTop) {
        bestTop = top;
        best = el;
      }
    }
    return best;
  }
  function labelFor(el) {
    if (!el) return "Bounded Agents";
    const id = el.id || "";
    if (id === "front-matter") return "Front matter";
    if (id === "part-i") return "Part I · Why this shape";
    if (id === "part-ii") return "Part II · The mechanisms";
    if (id === "part-iii") return "Part III · Operating it";
    if (id === "part-iv") return "Part IV · The edges";
    if (id === "references") return "References";
    if (id.startsWith("appendix-")) return "Appendix " + id.slice("appendix-".length).toUpperCase();
    const h = el.tagName && el.tagName.match(/^H\\d$/i) ? el : el.querySelector("h1, h2, h3");
    const t = (h || el).textContent || id;
    return t.replace(/\\s+/g, " ").trim().slice(0, 72);
  }
  function tick() {
    const doc = document.documentElement;
    const max = Math.max(1, doc.scrollHeight - window.innerHeight);
    const pct = Math.min(100, Math.max(0, (window.scrollY / max) * 100));
    if (bar) bar.style.width = pct.toFixed(1) + "%";
    if (progress) progress.textContent = labelFor(nearest());
  }
  window.addEventListener("scroll", tick, { passive: true });
  window.addEventListener("resize", tick);
  tick();
})();
</script>
"""


def main() -> None:
    if not HTML_SRC.exists():
        raise SystemExit(f"Missing {HTML_SRC}; run build_spine_pdf.py first")
    if not CSS_SRC.exists():
        raise SystemExit(f"Missing {CSS_SRC}")

    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir(parents=True)
    assets = SITE / "assets"
    assets.mkdir(parents=True, exist_ok=True)

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

    if "<body>" not in html:
        raise SystemExit("Could not find <body> to inject site chrome")
    html = html.replace("<body>", '<body class="pages-view">\n' + CHROME, 1)

    (SITE / "index.html").write_text(html, encoding="utf-8")
    shutil.copy2(CSS_SRC, SITE / "spine-pdf.css")
    if ICONS_SRC.exists():
        shutil.copy2(ICONS_SRC, assets / "icons.svg")
    (SITE / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Pages site ready at {SITE} ({(SITE / 'index.html').stat().st_size} bytes HTML)")


if __name__ == "__main__":
    main()
