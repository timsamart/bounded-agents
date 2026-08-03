"""Single source of truth for reader orientation strips and part maps.

Injected at build time by build_spine_pdf.py. Strips are aids: delete them and
the chapters still make sense (deletion test in voice.md).
"""

from __future__ import annotations

from typing import Any

# Icon keys used in strips and the front-matter legend.
# compass = orientation · book = Part I / claim · wrench = Part II / mechanism
# stop = Part III / ops · edge = Part IV · link = appendix / ADR exit · path = reading path

PARTS: dict[str, dict[str, Any]] = {
    "1.0-part-i": {
        "icon": "book",
        "part": "I",
        "altitude": "Claim and shape",
        "payoff": "Decide whether to build, and defend the shape without implementing it.",
        "cold_open": True,
        "prerequisite": "None. This is the intended start for leaders.",
        "children": [
            ("ch-1", "1", "Introduction", "State the claim, the non-goals, and who should not build this."),
            ("ch-2", "2", "What the environment forces on you", "Separate real constraints from habitual ones."),
            ("ch-3", "3", "The system in its landscape", "Fix vocabulary: run, actors, trust boundary."),
            ("ch-4", "4", "Five moves and the invariants they buy", "Print the architecture as five moves and eight falsifiable invariants."),
        ],
    },
    "2.0-part-ii": {
        "icon": "wrench",
        "part": "II",
        "altitude": "How each piece works",
        "payoff": "Argue for or against each mechanism in a design review, and know what it costs.",
        "cold_open": True,
        "prerequisite": "Part I helps. Not required. Each chapter opens with the plain claim before invariant codes.",
        "children": [
            ("ch-5", "5", "Identity and binding", "Possession of a credential stops being sufficient authority."),
            ("ch-6", "6", "The envelope", "Per-run authority from need, reach, and tier – never standing role."),
            ("ch-7", "7", "Complete mediation", "Coverage as a published number against discovered paths."),
            ("ch-8", "8", "The seam", "The only governable moment: guessing becomes doing."),
            ("ch-9", "9", "Approval and effect integrity", "What was approved and what executed must be the same object."),
            ("ch-10", "10", "Data, retrieval and memory", "Memory as a governed writable store, not a side effect."),
            ("ch-11", "11", "Evidence", "Tamper-evident records that still permit erasure."),
        ],
    },
    "3.0-part-iii": {
        "icon": "stop",
        "part": "III",
        "altitude": "Run, break, decay",
        "payoff": "Answer what fails, what fails closed, what can be stopped, and what happens in flight.",
        "cold_open": True,
        "prerequisite": "None for operations. Part I vocabulary helps; Part II explains why the dials sit where they sit.",
        "children": [
            ("ch-12", "12", "The agent manifest", "The signed deployable unit everything else attaches to."),
            ("ch-13", "13", "Governance in the hot path", "Latency-critical decisions, and runs in flight when the plane dies."),
            ("ch-14", "14", "The outage you decide in advance", "Fail-posture matrix signed before the incident."),
            ("ch-15", "15", "Stopping it", "Five stop mechanisms, each with an owner and a drill."),
            ("ch-16", "16", "Decay", "Silent degradation, and why recertification is the control."),
            ("ch-17", "17", "The paved road", "Unadopted controls have negative security value."),
        ],
    },
    "4.0-part-iv": {
        "icon": "edge",
        "part": "IV",
        "altitude": "Composition, boundaries, residual",
        "payoff": "Name what remains unsolved, and what an adversary can still do.",
        "cold_open": False,
        "prerequisite": "Parts I–II. The residual is sharper if you already hold the claim and the mechanisms.",
        "children": [
            ("ch-18", "18", "Composition", "Which invariants survive an agent calling an agent."),
            ("ch-19", "19", "Across the boundary", "Cross-organisation agents without a shared policy domain."),
            ("ch-20", "20", "Build order, and who should not build this", "Two quarters for five people, and when to build almost none of it."),
            ("ch-21", "21", "What it can still do", "Honest residual after everything else is true."),
        ],
    },
}

CHAPTERS: dict[str, dict[str, Any]] = {
    "1.1-introduction": {
        "icon": "book",
        "part": "I",
        "altitude": "Claim",
        "payoff": "State the two questions, the claim, the non-goals, and who should walk away.",
        "cold_open": True,
        "prerequisite": "None.",
    },
    "1.2-constraints": {
        "icon": "book",
        "part": "I",
        "altitude": "Claim and shape",
        "payoff": "Sort real constraints from habit so later chapters stay discardable.",
        "cold_open": False,
        "prerequisite": "Chapter 1 (the claim and the non-goals).",
    },
    "1.3-context-and-scope": {
        "icon": "book",
        "part": "I",
        "altitude": "Claim and shape",
        "payoff": "Use a shared vocabulary: run, principal, envelope, trust boundary.",
        "cold_open": False,
        "prerequisite": "Chapters 1–2.",
    },
    "1.4-solution-strategy": {
        "icon": "book",
        "part": "I",
        "altitude": "Shape",
        "payoff": "Defend five moves and eight falsifiable invariants in a design review.",
        "cold_open": False,
        "prerequisite": "Chapters 1–3 (claim, constraints, vocabulary).",
    },
    "2.1-identity-and-binding": {
        "icon": "wrench",
        "part": "II",
        "altitude": "Mechanism",
        "payoff": "Argue that possession must stop being sufficient authority, and what replaces it.",
        "cold_open": True,
        "prerequisite": "None required. Part I vocabulary helps. Plain claim opens before invariant codes.",
    },
    "2.2-the-envelope": {
        "icon": "wrench",
        "part": "II",
        "altitude": "Mechanism",
        "payoff": "Derive per-run authority as intersection, not inheritance from standing role.",
        "cold_open": True,
        "prerequisite": "None required. Chapter 5 (identity) helps. Plain claim opens before invariant codes.",
    },
    "2.3-complete-mediation": {
        "icon": "wrench",
        "part": "II",
        "altitude": "Mechanism",
        "payoff": "Treat coverage as a published ratio against discovered paths, not designed ones.",
        "cold_open": True,
        "prerequisite": "None required. Plain claim opens before invariant codes.",
    },
    "2.4-the-seam": {
        "icon": "wrench",
        "part": "II",
        "altitude": "Mechanism",
        "payoff": "Locate the only governable moment and separate protocol contribution from platform duty.",
        "cold_open": True,
        "prerequisite": "None required. Chapters 5–7 help. Plain claim opens before invariant codes.",
    },
    "2.5-approval-and-effect-integrity": {
        "icon": "wrench",
        "part": "II",
        "altitude": "Mechanism",
        "payoff": "Tell approval-as-control from approval-as-theatre, and bind both to one digest.",
        "cold_open": True,
        "prerequisite": "None required. Plain claim opens before invariant codes.",
    },
    "2.6-data-retrieval-memory": {
        "icon": "wrench",
        "part": "II",
        "altitude": "Mechanism",
        "payoff": "Treat memory as governed primary storage with purpose, ceiling, and principal reach.",
        "cold_open": True,
        "prerequisite": "None required. Plain claim opens before invariant codes.",
    },
    "2.7-evidence": {
        "icon": "wrench",
        "part": "II",
        "altitude": "Mechanism",
        "payoff": "Resolve tamper-evidence with erasability, and price evidence that gates execution.",
        "cold_open": True,
        "prerequisite": "None required. Plain claim opens before invariant codes.",
    },
    "3.1-agent-manifest": {
        "icon": "stop",
        "part": "III",
        "altitude": "Operations",
        "payoff": "Name the signed deployable unit quarantine and recertification attach to.",
        "cold_open": True,
        "prerequisite": "None. Written for someone who inherited the system.",
    },
    "3.2-hot-path": {
        "icon": "stop",
        "part": "III",
        "altitude": "Operations",
        "payoff": "State what happens to governance and in-flight runs when the control plane dies.",
        "cold_open": True,
        "prerequisite": "None required. Chapter 12 (manifest) helps.",
    },
    "3.3-failure-postures": {
        "icon": "stop",
        "part": "III",
        "altitude": "Operations",
        "payoff": "Put the fail-posture matrix in a design review, including the non-negotiable.",
        "cold_open": True,
        "prerequisite": "None required.",
    },
    "3.4-stopping-it": {
        "icon": "stop",
        "part": "III",
        "altitude": "Operations",
        "payoff": "Replace the single kill switch with five owned, drilled mechanisms.",
        "cold_open": True,
        "prerequisite": "None required.",
    },
    "3.5-decay": {
        "icon": "stop",
        "part": "III",
        "altitude": "Operations",
        "payoff": "Treat silent degradation as expected, and recertification as the reason controls still exist.",
        "cold_open": True,
        "prerequisite": "None required.",
    },
    "3.6-the-paved-road": {
        "icon": "stop",
        "part": "III",
        "altitude": "Operations",
        "payoff": "Price the sanctioned path in minutes, because adoption decides coverage.",
        "cold_open": True,
        "prerequisite": "None required.",
    },
    "4.1-composition": {
        "icon": "edge",
        "part": "IV",
        "altitude": "Edge",
        "payoff": "Know which invariants survive agent-to-agent composition, and which do not.",
        "cold_open": False,
        "prerequisite": "Parts I–II. Composition breaks assumptions the mechanisms rely on.",
    },
    "4.2-across-the-boundary": {
        "icon": "edge",
        "part": "IV",
        "altitude": "Edge",
        "payoff": "Mark what is currently unbuildable across organisational boundaries.",
        "cold_open": False,
        "prerequisite": "Parts I–II, and preferably chapter 18.",
    },
    "4.3-build-order": {
        "icon": "edge",
        "part": "IV",
        "altitude": "Edge",
        "payoff": "Sequence two quarters of work, or decide to build almost none of it.",
        "cold_open": False,
        "prerequisite": "Part I at minimum. Sharper after Parts II–III.",
    },
    "4.4-residual": {
        "icon": "edge",
        "part": "IV",
        "altitude": "Edge",
        "payoff": "State what remains possible for an adversary after everything else is true.",
        "cold_open": False,
        "prerequisite": "The rest of the spine, or Appendix C then A for a security reviewer.",
    },
}

# Front-matter legend rows: (icon, label, meaning)
LEGEND: list[tuple[str, str, str]] = [
    ("compass", "Orientation", "You-are-here strip on every part and chapter"),
    ("book", "Part I", "Claim and shape"),
    ("wrench", "Part II", "Mechanisms (cold-openable by chapter)"),
    ("stop", "Part III", "Operations"),
    ("edge", "Part IV", "Edges and residual"),
    ("link", "Exit", "Appendix or ADR pointer in the text"),
    ("path", "Path", "Reading path in the front matter"),
]


def lookup(stem: str) -> dict[str, Any] | None:
    if stem in PARTS:
        return {"kind": "part", **PARTS[stem]}
    if stem in CHAPTERS:
        return {"kind": "chapter", **CHAPTERS[stem]}
    return None
