# -*- coding: utf-8 -*-
"""Fill ADR Cost sections from priced paragraphs near spine markers."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = ROOT / "chapters"
DEC = ROOT / "decisions"

COST_RX = re.compile(
    r"(?:\bms\b|p99|engineer|€|\blatency\b|\bcosts?\b|headcount|"
    r"people permanently|drill|%\b|\bminutes?\b|\bquarter\b|"
    r"engineer-days?|availability)",
    re.I,
)
PLACEHOLDER = (
    "Cost is stated in the arguing chapter. This record does not invent a figure "
    "the spine does not price."
)


def nearby_cost(chapter: Path, adr_num: int) -> str | None:
    text = chapter.read_text(encoding="utf-8")
    # split into paragraphs
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    markers = {f"[ADR-{adr_num:02d}]", f"[ADR-{adr_num}]"}
    for i, p in enumerate(paras):
        if not any(m in p for m in markers):
            continue
        window = paras[max(0, i - 2) : i + 4]
        for cand in window:
            if not COST_RX.search(cand):
                continue
            # skip pure abstract without digits / currency / units
            if not re.search(r"\d|€|ms|p99|engineer", cand, re.I):
                continue
            clean = re.sub(r"\s*`?\[ADR-\d+\]`?", "", cand)
            clean = re.sub(r"\s*`?\[A-\d+(?:\.\d+)?\]`?", "", clean)
            clean = re.sub(r"\s*\[@[^\]]+\]", "", clean)
            clean = clean.replace("**", "").strip()
            if len(clean) > 80:
                return clean
    return None


def main() -> None:
    filled = 0
    for path in sorted(DEC.glob("ADR-*.md")):
        txt = path.read_text(encoding="utf-8")
        if PLACEHOLDER not in txt:
            continue
        m = re.search(r"ADR-(\d+)", path.name)
        if not m:
            continue
        num = int(m.group(1))
        argued = re.search(r"\*\*Argued in:\*\*\s*(.+)", txt)
        chapters: list[Path] = []
        if argued:
            for name in re.findall(r"chapters/([\w.-]+\.md)", argued.group(1)):
                chapters.append(CH / name)
        cost = None
        for ch in chapters:
            if ch.exists():
                cost = nearby_cost(ch, num)
                if cost:
                    break
        if not cost:
            print("still placeholder", path.name)
            continue
        # avoid duplicating text already present
        if cost[:80] in txt:
            # still replace placeholder with a short pointer
            replacement = (
                "Priced in the arguing chapter (latency, engineering effort, or operational "
                "burden appears in the narrative above or in the Decision section)."
            )
        else:
            replacement = cost
        path.write_text(txt.replace(PLACEHOLDER, replacement), encoding="utf-8")
        filled += 1
        print("filled", path.name)
    print("filled", filled)


if __name__ == "__main__":
    main()
