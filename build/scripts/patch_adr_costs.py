# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[2]
DEC = ROOT / "decisions"

p = DEC / "ADR-01-containment-over-prevention-as-claim.md"
t = p.read_text(encoding="utf-8")
old = (
    "## Cost\n\n"
    "Cost is stated in the arguing chapter. This record does not invent a figure the spine does not price."
)
new = (
    "## Cost\n\n"
    "Neither was a bad thing to do. The threshold change plausibly stops the next copy of this attack. "
    "The prompt change costs almost nothing. The problem appeared three weeks later, in the assurance pack "
    "that went to the risk committee, where both items were listed in the controls column alongside the other nine. "
    "In that column they carry a claim neither can support. The threshold change had an operational tail: "
    "`claims-triage` handles about 4,000 runs a day; the tightened threshold held roughly 3% for human review; "
    "by the sixth week a queue of about 120 runs a day was being cleared in batches by people who had stopped "
    "reading them individually."
)
if old in t:
    p.write_text(t.replace(old, new), encoding="utf-8")
    print("fixed ADR-01 cost")
else:
    print("ADR-01 cost pattern miss")

n = 0
for f in sorted(DEC.glob("ADR-*.md")):
    txt = f.read_text(encoding="utf-8")
    if "does not invent a figure" in txt:
        n += 1
        print("placeholder cost:", f.name)
print("placeholder count", n)

en = " \u2013 "  # spaced en dash
for f in DEC.glob("ADR-*.md"):
    txt = f.read_text(encoding="utf-8")
    txt2 = txt.replace("\u2014", en).replace("â€”", en)
    txt2 = re.sub(r"\s+\u2013\s+", en, txt2)
    if txt2 != txt:
        f.write_text(txt2, encoding="utf-8")
        print("normalised dashes:", f.name)
