#!/usr/bin/env python3
"""Build the Bounded Agents PDF (Governed Agentic Infrastructure spine).

chapters/ → numbered markdown → pandoc HTML (+ citeproc) → Playwright PDF.

Usage:
  python build/build_spine_pdf.py
  py -3.11 build/build_spine_pdf.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = ROOT / "chapters"
DECISIONS = ROOT / "decisions"
APPENDICES = ROOT / "appendices"
BUILD_DIR = ROOT / "build"
BUILD_MD = BUILD_DIR / "spine-build.md"
HTML_OUT = BUILD_DIR / "spine.html"
CSS_OUT = BUILD_DIR / "spine-pdf.css"
PDF_OUT = BUILD_DIR / "bounded-agents.pdf"
BIB = ROOT / "references.bib"
CSL = BUILD_DIR / "csl" / "ieee.csl"
MERMAID_CFG = BUILD_DIR / "mermaid-config.json"

PAGE_MARGIN_TOP = "26mm"
PAGE_MARGIN_BOTTOM = "28mm"
PAGE_MARGIN_LEFT = "20mm"
PAGE_MARGIN_RIGHT = "20mm"
CONTENT_PAD = "8mm"
HEADER_PAD = "28mm"

# Filename stem → (kind, number_or_roman, stable_id, display_prefix)
# kind: front | part | chapter
CHAPTER_META: dict[str, tuple[str, str, str, str]] = {
    "0.1-front-matter": ("front", "", "front-matter", ""),
    "1.0-part-i": ("part", "I", "part-i", "Part I."),
    "1.1-introduction": ("chapter", "1", "ch-1", "Chapter 1."),
    "1.2-constraints": ("chapter", "2", "ch-2", "Chapter 2."),
    "1.3-context-and-scope": ("chapter", "3", "ch-3", "Chapter 3."),
    "1.4-solution-strategy": ("chapter", "4", "ch-4", "Chapter 4."),
    "2.0-part-ii": ("part", "II", "part-ii", "Part II."),
    "2.1-identity-and-binding": ("chapter", "5", "ch-5", "Chapter 5."),
    "2.2-the-envelope": ("chapter", "6", "ch-6", "Chapter 6."),
    "2.3-complete-mediation": ("chapter", "7", "ch-7", "Chapter 7."),
    "2.4-the-seam": ("chapter", "8", "ch-8", "Chapter 8."),
    "2.5-approval-and-effect-integrity": ("chapter", "9", "ch-9", "Chapter 9."),
    "2.6-data-retrieval-memory": ("chapter", "10", "ch-10", "Chapter 10."),
    "2.7-evidence": ("chapter", "11", "ch-11", "Chapter 11."),
    "3.0-part-iii": ("part", "III", "part-iii", "Part III."),
    "3.1-agent-manifest": ("chapter", "12", "ch-12", "Chapter 12."),
    "3.2-hot-path": ("chapter", "13", "ch-13", "Chapter 13."),
    "3.3-failure-postures": ("chapter", "14", "ch-14", "Chapter 14."),
    "3.4-stopping-it": ("chapter", "15", "ch-15", "Chapter 15."),
    "3.5-decay": ("chapter", "16", "ch-16", "Chapter 16."),
    "3.6-the-paved-road": ("chapter", "17", "ch-17", "Chapter 17."),
    "4.0-part-iv": ("part", "IV", "part-iv", "Part IV."),
    "4.1-composition": ("chapter", "18", "ch-18", "Chapter 18."),
    "4.2-across-the-boundary": ("chapter", "19", "ch-19", "Chapter 19."),
    "4.3-build-order": ("chapter", "20", "ch-20", "Chapter 20."),
    "4.4-residual": ("chapter", "21", "ch-21", "Chapter 21."),
}

# Manual numbered cites → pandoc cite keys (order of appearance in spine).
NUMERIC_CITE_MAP = {
    "1": "hardy1988confused",
    "2": "saltzer1975protection",
}

# Resolve a few citation-needed gaps that now have real bib entries.
CITATION_NEEDED_RESOLVE: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(
            r"`?\[citation needed: Model Context Protocol specification,[^\]]*\]`?",
            re.I,
        ),
        "[@mcp2025spec]",
    ),
    (
        re.compile(
            r"`?\[citation needed: the protocol's authorisation specification,[^\]]*\]`?",
            re.I,
        ),
        "[@mcp2025auth]",
    ),
    (
        re.compile(
            r"`?\[citation needed: W3C Verifiable Credentials Data Model,[^\]]*\]`?",
            re.I,
        ),
        "[@w3c2025vc]",
    ),
    (
        re.compile(
            r"`?\[citation needed: W3C s[^\]]*status[^\]]*\]`?",
            re.I,
        ),
        "[@w3c2025statuslist]",
    ),
    (
        re.compile(
            r"`?\[citation needed: one canonical incident-response containment taxonomy[^\]]*\]`?",
            re.I,
        ),
        "[@nist80061r2]",
    ),
    (
        re.compile(
            r"`?\[citation needed: reproducible research on tool-description injection[^\]]*\]`?",
            re.I,
        ),
        "[@greshake2023indirect]",
    ),
]

PY311 = Path(r"C:\Users\Chrysanth\AppData\Local\Programs\Python\Python311\python.exe")


def list_chapters() -> list[Path]:
    files = sorted(CHAPTERS.glob("*.md"))
    if not files:
        raise SystemExit(f"No chapters under {CHAPTERS}")
    return files


def shift_headings(text: str, by: int = 1) -> str:
    def repl(m: re.Match[str]) -> str:
        return "#" * (len(m.group(1)) + by) + " "

    return re.sub(r"^(#{1,5}) ", repl, text, flags=re.MULTILINE)


def preprocess_mermaid(text: str) -> str:
    return re.sub(
        r"```mermaid\s*\n(.*?)```",
        lambda m: "```{.mermaid}\n" + m.group(1).strip() + "\n```\n",
        text,
        flags=re.DOTALL,
    )


def strip_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def rewrite_cites(text: str) -> str:
    for pat, repl in CITATION_NEEDED_RESOLVE:
        text = pat.sub(repl, text)

    def num_repl(m: re.Match[str]) -> str:
        key = NUMERIC_CITE_MAP.get(m.group(1))
        return f"[@{key}]" if key else m.group(0)

    text = re.sub(r"(?<!\[)\[(\d+)\](?!\()", num_repl, text)
    # Remaining citation-needed (should be none after source pass).
    text = re.sub(
        r"`?\[citation needed:([^\]]+)\]`?",
        r'<span class="citation-needed">[citation needed:\1]</span>',
        text,
    )

    def adr_repl(m: re.Match[str]) -> str:
        raw = m.group(1)
        # Normalise ADR-1 → adr-01
        num = int(raw.split("-", 1)[1])
        hid = f"adr-{num:02d}"
        return f'<a class="adr-ref" href="#{hid}">[{raw}]</a>'

    def app_repl(m: re.Match[str]) -> str:
        raw = m.group(1)  # A-6.1
        hid = raw.lower().replace(".", "-")  # a-6-1
        return f'<a class="app-ref" href="#{hid}">[{raw}]</a>'

    text = re.sub(r"`?\[(ADR-\d+)\]`?", adr_repl, text)
    text = re.sub(r"`?\[(A-\d+(?:\.\d+)?)\]`?", app_repl, text)
    return text


def number_title(stem: str, title_line: str) -> str:
    meta = CHAPTER_META.get(stem)
    if not meta:
        return title_line
    kind, _num, stable_id, prefix = meta
    title = title_line[2:].strip()
    if kind == "front":
        return f"# {title} {{#{stable_id}}}"
    if kind == "part":
        # Title already often starts with "Part N."; avoid double prefix.
        if title.lower().startswith("part "):
            return f"# {title} {{#{stable_id}}}"
        return f"# {prefix} {title} {{#{stable_id}}}"
    # chapter
    bare = re.sub(r"^Chapter\s+\d+\.?\s*", "", title, flags=re.I)
    return f"# {prefix} {bare} {{#{stable_id}}}"


def process_chapter(path: Path) -> str:
    stem = path.stem
    raw = strip_comments(path.read_text(encoding="utf-8")).strip() + "\n"
    raw = rewrite_cites(raw)
    lines = raw.split("\n")
    if not lines or not lines[0].startswith("# "):
        return raw
    lines[0] = number_title(stem, lines[0])
    raw = "\n".join(lines)
    # Demote body headings under chapter/part H1 for TOC nesting.
    if re.match(r"^[1-4]\.[1-9]", path.name) or re.match(r"^[1-4]\.0-", path.name):
        body = "\n".join(lines[1:]).lstrip("\n")
        body = shift_headings(body, by=1)
        raw = lines[0] + "\n\n" + body
    return raw


def process_backmatter(path: Path) -> str:
    raw = strip_comments(path.read_text(encoding="utf-8")).strip() + "\n"
    raw = rewrite_cites(raw)
    # Demote H1 under a part-level divider already in file; keep stable ids.
    return raw


def build_markdown() -> str:
    parts: list[str] = []
    for path in list_chapters():
        parts.append(process_chapter(path))
        parts.append("\n\\newpage\n")

    appendix_order = ["a-", "b-", "c-", "d-", "e-", "f-", "g-", "h-"]
    appendix_files = [
        p
        for prefix in appendix_order
        for p in sorted(APPENDICES.glob(f"{prefix}*.md"))
        if p.name != "README.md"
    ]
    for path in appendix_files:
        parts.append(process_backmatter(path))
        parts.append("\n\\newpage\n")
        if path.name.startswith("b-"):
            for adr in sorted(DECISIONS.glob("ADR-*.md")):
                parts.append(process_backmatter(adr))
                parts.append("\n\\newpage\n")

    parts.append("# References {#references}\n\n::: {#refs}\n:::\n")
    full = "\n\n".join(parts)
    full = preprocess_mermaid(full)
    full = full.replace("\\newpage", '<div class="page-break"></div>')
    return full.strip() + "\n"


def run_pandoc() -> None:
    if not CSL.exists():
        raise SystemExit(f"Missing CSL: {CSL}")
    if not BIB.exists():
        raise SystemExit(f"Missing bibliography: {BIB}")
    cmd = [
        "pandoc",
        str(BUILD_MD),
        "-f",
        "markdown+raw_attribute+pipe_tables+strikeout+smart+raw_html+citations",
        "-t",
        "html5",
        "--standalone",
        "--toc",
        "--toc-depth=2",
        "--css",
        str(CSS_OUT),
        "--citeproc",
        f"--bibliography={BIB}",
        f"--csl={CSL}",
        "-o",
        str(HTML_OUT),
        "--metadata",
        "title=Bounded Agents",
        "--metadata",
        "subtitle=Governed Agentic Infrastructure",
        "--metadata",
        "author=Timotheos Samartzidis",
        "--metadata",
        "date=2026-08-01",
        "--metadata",
        "toc-title=Contents",
        "--metadata",
        "reference-section-title=References",
        "--metadata",
        "link-citations=true",
        "--highlight-style=kate",
    ]
    subprocess.run(cmd, check=True, cwd=ROOT)


def mermaid_init_js() -> str:
    cfg = json.loads(MERMAID_CFG.read_text(encoding="utf-8"))
    return f"""
<script>
  mermaid.initialize({{
    startOnLoad: false,
    securityLevel: "loose",
    theme: {json.dumps(cfg.get("theme", "neutral"))},
    themeVariables: {json.dumps(cfg.get("themeVariables", {}))},
    flowchart: {json.dumps(cfg.get("flowchart", {}))},
    sequence: {json.dumps(cfg.get("sequence", {}))}
  }});
  document.querySelectorAll("pre.mermaid, code.mermaid, pre > code.language-mermaid").forEach((node) => {{
    const div = document.createElement("div");
    div.className = "mermaid";
    div.textContent = node.textContent;
    const host = node.closest("pre") || node;
    host.replaceWith(div);
  }});
  mermaid.run({{ querySelector: ".mermaid" }}).catch(console.error);
</script>
"""


def inject_cover_and_mermaid(html: str) -> str:
    cover = """
<header class="cover" id="cover">
  <div class="cover-frame">
    <p class="cover-kicker">Edition 0.1 draft · Narrative spine</p>
    <h1 class="cover-title">Bounded Agents</h1>
    <p class="cover-subtitle">Governed Agentic Infrastructure</p>
    <p class="cover-tagline">How to give AI agents real authority when the model may be hostile</p>
    <div class="cover-rule"></div>
    <p class="cover-meta">Chapters 1–21 · Appendices A–H · ADR-01–ADR-39</p>
    <p class="cover-date">Timotheos Samartzidis · timosam.com · 2026</p>
    <p class="cover-license">CC BY 4.0 · github.com/timsamart/bounded-agents</p>
  </div>
</header>
"""
    head_inject = f"""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<style>
  :root {{ --content-pad: {CONTENT_PAD}; }}
  @page {{
    size: A4;
    margin: {PAGE_MARGIN_TOP} {PAGE_MARGIN_RIGHT} {PAGE_MARGIN_BOTTOM} {PAGE_MARGIN_LEFT};
    background: #faf8f5;
  }}
  .citation-needed {{
    font-style: italic;
    color: #5c6b7a;
    font-size: 0.92em;
  }}
  .forward-ref {{
    font-family: "IBM Plex Mono", monospace;
    font-size: 0.85em;
    color: #5c6b7a;
  }}
  .cover-tagline {{
    margin: 4mm 0 0;
    font-size: 11pt;
    line-height: 1.4;
    color: #5c6b7a;
  }}
  .cover-license {{
    margin: 4mm 0 0;
    font-family: "IBM Plex Mono", monospace;
    font-size: 8pt;
    color: #5c6b7a;
  }}
  nav#TOC {{
    page-break-after: always;
  }}
  nav#TOC > ul {{
    list-style: none;
    padding-left: 0;
  }}
  nav#TOC a {{
    text-decoration: none;
    color: inherit;
  }}
  nav#TOC a:hover {{
    color: #c45c3e;
  }}
</style>
"""
    html = html.replace("</head>", head_inject + "</head>")
    html = html.replace("<body>", "<body>" + cover)
    html = html.replace("</body>", mermaid_init_js() + "</body>")
    return html


def render_chunk(page_range: str, out_path: Path) -> None:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(HTML_OUT.as_uri(), wait_until="networkidle", timeout=120000)
        page.wait_for_function(
            """() => {
                const blocks = document.querySelectorAll('.mermaid');
                if (!blocks.length) return true;
                return [...blocks].every((b) => b.querySelector('svg'));
            }""",
            timeout=180000,
        )
        page.wait_for_timeout(800)
        kwargs = dict(
            path=str(out_path),
            format="A4",
            print_background=True,
            prefer_css_page_size=True,
            margin={"top": "0", "bottom": "0", "left": "0", "right": "0"},
            display_header_footer=True,
            header_template=f"""
                <div style="width:100%; margin:0; padding:2.5mm {HEADER_PAD} 0; box-sizing:border-box;
                            font-family: Georgia, 'Times New Roman', serif;
                            font-size:8px; color:#6b7a8a; letter-spacing:0.04em;">
                  Bounded Agents · Governed Agentic Infrastructure
                </div>
            """,
            footer_template=f"""
                <div style="width:100%; margin:0; padding:0 {HEADER_PAD} 2.5mm; box-sizing:border-box;
                            font-family: Georgia, 'Times New Roman', serif;
                            font-size:8px; color:#6b7a8a;
                            display:flex; justify-content:space-between;">
                  <span>Timotheos Samartzidis · CC BY 4.0 · Edition 0.1 draft</span>
                  <span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>
                </div>
            """,
        )
        if page_range:
            kwargs["page_ranges"] = page_range
        page.pdf(**kwargs)
        browser.close()


def page_count(pdf_path: Path) -> int:
    return len(PdfReader(str(pdf_path)).pages)


def merge_pdfs(paths: list[Path], out: Path) -> None:
    writer = PdfWriter()
    for path in paths:
        reader = PdfReader(str(path))
        for page in reader.pages:
            writer.add_page(page)
    with out.open("wb") as f:
        writer.write(f)


def render_pdf() -> None:
    BUILD_DIR.mkdir(exist_ok=True)
    probe = BUILD_DIR / "_spine_probe.pdf"
    print("Rendering full PDF (first pass)…")
    try:
        render_chunk("", probe)
        pages = page_count(probe)
        print(f"Probe pages: {pages}")
        if pages <= 180:
            probe.replace(PDF_OUT)
            return
    except Exception as exc:
        print(f"Full render failed ({exc}); falling back to chunks.")
        probe.unlink(missing_ok=True)

    chunks: list[Path] = []
    start = 1
    step = 40
    while start < 800:
        end = start + step - 1
        chunk_path = BUILD_DIR / f"_spine_chunk_{start}_{end}.pdf"
        print(f"Rendering pages {start}-{end}…")
        try:
            render_chunk(f"{start}-{end}", chunk_path)
        except Exception as exc:
            print(f"Chunk {start}-{end} failed: {exc}")
            break
        n = page_count(chunk_path)
        if n == 0:
            chunk_path.unlink(missing_ok=True)
            break
        chunks.append(chunk_path)
        if n < step:
            break
        start = end + 1

    if not chunks:
        raise SystemExit("No PDF chunks produced")
    merge_pdfs(chunks, PDF_OUT)
    for c in chunks:
        c.unlink(missing_ok=True)
    probe.unlink(missing_ok=True)


def main() -> int:
    BUILD_DIR.mkdir(exist_ok=True)
    if not CSS_OUT.exists():
        raise SystemExit(f"Missing stylesheet: {CSS_OUT}")
    BUILD_MD.write_text(build_markdown(), encoding="utf-8")
    print(f"Wrote {BUILD_MD} ({BUILD_MD.stat().st_size // 1024} KB)")
    run_pandoc()
    HTML_OUT.write_text(
        inject_cover_and_mermaid(HTML_OUT.read_text(encoding="utf-8")),
        encoding="utf-8",
    )
    print(f"Wrote {HTML_OUT} ({HTML_OUT.stat().st_size // 1024} KB)")
    render_pdf()
    print(f"Wrote {PDF_OUT} ({PDF_OUT.stat().st_size // 1024} KB, {page_count(PDF_OUT)} pages)")
    return 0


if __name__ == "__main__":
    try:
        import playwright  # noqa: F401
    except ImportError:
        if PY311.exists() and Path(sys.executable).resolve() != PY311.resolve():
            raise SystemExit(
                subprocess.run([str(PY311), str(Path(__file__).resolve()), *sys.argv[1:]]).returncode
            )
        print("Playwright not installed. Try: pip install playwright && playwright install chromium", file=sys.stderr)
        raise SystemExit(1)
    raise SystemExit(main())
