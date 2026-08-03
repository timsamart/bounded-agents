# -*- coding: utf-8 -*-
"""Deepen edition 0.1 ADRs and appendices from spine extraction; fix aside merges."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = ROOT / "chapters"
DEC = ROOT / "decisions"
APP = ROOT / "appendices"
EXTRACTION = ROOT / "build" / "adr-extraction.json"

# --- Chapter aside-merge fixes (honest-gap prose incorrectly glued mid-sentence) ---

ASIDE_FIXES: list[tuple[str, str, str]] = [
    (
        "1.1-introduction.md",
        "The rate that matters – against someone adapting to *your* defence – is rarely published at all We have not found a published false-negative rate for injection detection measured against an adversary adapting to the defender's own filter. Vendor detection rates are not a substitute..",
        "The rate that matters – against someone adapting to *your* defence – is rarely published at all. We have not found a published false-negative rate for injection detection measured against an adversary adapting to the defender's own filter. Vendor detection rates are not a substitute.",
    ),
    (
        "1.4-solution-strategy.md",
        "That number is not published We have not found a published false-negative rate for injection detection measured against an adversary adapting to the defender's own filter. Vendor detection rates are not a substitute..",
        "That number is not published. We have not found a published false-negative rate for injection detection measured against an adversary adapting to the defender's own filter. Vendor detection rates are not a substitute.",
    ),
    (
        "2.1-identity-and-binding.md",
        "The honest position is that the number is unmeasured rather than small Published theft-to-use timings for credentials lifted from agent or CI contexts remain scarce; treat same-second reuse as the planning assumption until you measure your own..",
        "The honest position is that the number is unmeasured rather than small. Published theft-to-use timings for credentials lifted from agent or CI contexts remain scarce; treat same-second reuse as the planning assumption until you measure your own.",
    ),
    (
        "2.3-complete-mediation.md",
        "The useful contribution here is the method, because no published measurement exists of how many unmediated integration paths a typical enterprise carries No organisation we can cite publishes its own unmediated-path denominator; the first number you will see is therefore your own.. Vendors publish detection rates. No organisation publishes its own denominator. That is why the first number you see will be your own.",
        "The useful contribution here is the method, because no published measurement exists of how many unmediated integration paths a typical enterprise carries. No organisation we can cite publishes its own unmediated-path denominator; the first number you see will be your own. Vendors publish detection rates. Organisations rarely publish their own denominator.",
    ),
    (
        "2.4-the-seam.md",
        "The six missing properties are drafted as specification requests and submitted to the protocol's own proposal process rather than kept in a PDF, because a wish list with no recipient is a complaint with a bibliography Track the six missing properties as issues in the protocol's own specification venue; a PDF wish list with no venue identifier is not a submission..",
        "The six missing properties are drafted as specification requests and submitted to the protocol's own proposal process rather than kept in a PDF, because a wish list with no recipient is a complaint with a bibliography. Track the six missing properties as issues in the protocol's own specification venue; a PDF wish list with no venue identifier is not a submission.",
    ),
    (
        "2.5-approval-and-effect-integrity.md",
        "What follows is a proposed instrument rather than a reported result Outside estates rarely publish approval-rate and time-to-decision distributions for agent gates; measure your own before treating a gate as load-bearing..",
        "What follows is a proposed instrument rather than a reported result. Outside estates rarely publish approval-rate and time-to-decision distributions for agent gates; measure your own before treating a gate as load-bearing.",
    ),
    (
        "2.6-data-retrieval-memory.md",
        "This design is ahead of its literature rather than derived from it Peer-reviewed and industrial write-ups of entitlement-resolved retrieval at enterprise scale are thin; the design here is derived, not surveyed..",
        "This design is ahead of its literature rather than derived from it. Peer-reviewed and industrial write-ups of entitlement-resolved retrieval at enterprise scale are thin; the design here is derived, not surveyed.",
    ),
    (
        "2.7-evidence.md",
        "Supervisory opinion is not uniform on whether rendering data permanently unreadable amounts to erasure Supervisory positions on key destruction as erasure vary by jurisdiction and date; confirm with counsel before treating the mechanism as settled law..",
        "Supervisory opinion is not uniform on whether rendering data permanently unreadable amounts to erasure. Supervisory positions on key destruction as erasure vary by jurisdiction and date; confirm with counsel before treating the mechanism as settled law.",
    ),
    (
        "3.5-decay.md",
        "What is needed here is the rate rather than the anecdote We cite the *existence* of longitudinal audit-cycle practice in aviation and clinical audit, not a single published decay rate you can copy; measure your own interval..",
        "What is needed here is the rate rather than the anecdote. We cite the *existence* of longitudinal audit-cycle practice in aviation and clinical audit, not a single published decay rate you can copy; measure your own interval.",
    ),
    (
        "3.6-the-paved-road.md",
        "There is no published benchmark to set it against: the platform-engineering literature on friction and adoption of a sanctioned path is young, largely vendor-authored, and drawn from surveys of self-selected respondents A clean, non-vendor measurement of path friction against adoption of a sanctioned internal platform is not something we can cite; the direction of the relationship is not in serious doubt..",
        "There is no published benchmark to set it against: the platform-engineering literature on friction and adoption of a sanctioned path is young, largely vendor-authored, and drawn from surveys of self-selected respondents. A clean, non-vendor measurement of path friction against adoption of a sanctioned internal platform is not something we can cite; the direction of the relationship is not in serious doubt.",
    ),
    (
        "4.1-composition.md",
        "It is the obvious design rather than a careless one Framework defaults change monthly; treat parent-authority propagation as the observed default on your pinned versions and re-check on upgrade rather than citing a survey that will be stale on arrival..",
        "It is the obvious design rather than a careless one. Framework defaults change monthly; treat parent-authority propagation as the observed default on your pinned versions and re-check on upgrade rather than citing a survey that will be stale on arrival.",
    ),
    (
        "4.4-residual.md",
        "That emptiness is itself the finding Residual-risk analyses specific to production agent platforms, as distinct from ordinary application residual risk, are effectively absent; the list that follows is derived from this architecture..",
        "That emptiness is itself the finding. Residual-risk analyses specific to production agent platforms, as distinct from ordinary application residual risk, are effectively absent; the list that follows is derived from this architecture.",
    ),
]


def fix_asides() -> int:
    n = 0
    for fname, old, new in ASIDE_FIXES:
        path = CH / fname
        text = path.read_text(encoding="utf-8")
        if old not in text:
            print(f"WARN aside miss: {fname}")
            continue
        path.write_text(text.replace(old, new, 1), encoding="utf-8")
        n += 1
    # Normalise backtick ADR markers in the seam chapter
    seam = CH / "2.4-the-seam.md"
    s = seam.read_text(encoding="utf-8")
    s2 = re.sub(r"`\[(ADR-\d+)\]`", r"[\1]", s)
    if s2 != s:
        seam.write_text(s2, encoding="utf-8")
        n += 1
    return n


def scrub(p: str) -> str:
    p = p.strip()
    p = re.sub(r"\s*`?\[ADR-\d+\]`?", "", p)
    p = re.sub(r"\s*`?\[A-\d+(?:\.\d+)?\]`?", "", p)
    p = re.sub(r"\s*\[@[^\]]+\]", "", p)
    p = p.replace("**", "")
    p = p.replace("—", " – ")
    return p.strip()


def is_narrative(p: str) -> bool:
    p = p.strip()
    if not p or len(p) < 60:
        return False
    if p.startswith("```") or p.startswith("*Figure") or p.startswith("##"):
        return False
    if p.startswith("|") or p.startswith("---") or p.startswith(">"):
        return False
    return True


def concrete_score(p: str) -> int:
    """Prefer paragraphs with physical anchors over pure abstraction."""
    s = 0
    low = p.lower()
    for needle in (
        "borealis",
        "marta",
        "kai",
        "2026-",
        "claims-triage",
        "€",
        " ms",
        "p99",
        "engineer",
        "run_",
        "guidewire",
        "%",
    ):
        if needle in low:
            s += 3
    if re.search(r"\d", p):
        s += 1
    if low.startswith(("notice what", "a claim without", "this buys", "ordering is")):
        s -= 2  # mid-argument openers are weak as Context lead
    return s


def deepen_adrs() -> int:
    data = json.loads(EXTRACTION.read_text(encoding="utf-8"))
    count = 0
    for key in sorted(data.keys(), key=lambda x: int(x)):
        item = data[key]
        n = int(item["num"])
        title = item["title"]
        decision = item["decision"].strip().replace("—", " – ")
        rejected = item["rejected"].strip().lstrip("- ").strip().replace("—", " – ")
        reopen = item["reopen"].strip().replace("—", " – ")
        argued = item["argued_in_stub"]
        sid = f"ADR-{n:02d}"
        marker = f"[ADR-{n:02d}]"
        # also accept unpadded in rare cases
        marker_alt = f"[ADR-{n}]"

        before: list[str] = []
        decision_paras: list[str] = []
        after: list[str] = []
        all_raw: list[str] = []

        for _ch, blocks in item.get("chapters", {}).items():
            for block in blocks:
                raws = [p for p in block.get("paragraphs", []) if is_narrative(p)]
                for i, p in enumerate(raws):
                    all_raw.append(p)
                    if marker in p or marker_alt in p:
                        decision_paras.append(scrub(p))
                        # take up to two paragraphs before as context candidates
                        for j in range(max(0, i - 2), i):
                            before.append(scrub(raws[j]))
                        for j in range(i + 1, min(len(raws), i + 3)):
                            after.append(scrub(raws[j]))
                    else:
                        # keep pool for scoring if marker block thin
                        pass

        # Deduplicate while preserving order
        def uniq(seq: list[str]) -> list[str]:
            out: list[str] = []
            seen: set[str] = set()
            for p in seq:
                if not p:
                    continue
                sig = p[:100]
                if sig in seen:
                    continue
                seen.add(sig)
                out.append(p)
            return out

        before = uniq(before)
        after = uniq(after)
        decision_paras = uniq(decision_paras)
        pool = uniq([scrub(p) for p in all_raw if is_narrative(p)])

        # Context: highest-scoring before-paras, else best from pool excluding decision para
        ctx_candidates = before[:] or sorted(pool, key=concrete_score, reverse=True)
        context_paras: list[str] = []
        used: set[str] = set()
        for p in sorted(ctx_candidates, key=concrete_score, reverse=True):
            if p[:100] in used:
                continue
            # skip pure decision restatement as context lead
            context_paras.append(p)
            used.add(p[:100])
            if len(context_paras) >= 2 or sum(len(x) for x in context_paras) > 900:
                break
        if not context_paras:
            context_paras = [
                f"This decision is argued in {argued}. The forces are those of the chapter: "
                "a hostile model with real tools, and an organisation that must state a bound before the run starts."
            ]
            used.add(context_paras[0][:100])

        # Decision elaboration: marker paragraph(s), else first high-score unused
        dec_extra = [p for p in decision_paras if p[:100] not in used]
        if not dec_extra:
            for p in pool:
                if p[:100] not in used and concrete_score(p) >= 0:
                    dec_extra.append(p)
                    break
        for p in dec_extra[:2]:
            used.add(p[:100])

        # Rejected: paragraphs that steel-man an alternative
        rej_keys = (
            "alternative",
            "rejected",
            "loses on",
            "what most",
            "temptation",
            "instead of",
            "rather than",
            "the obvious",
            "framework default",
            "deny-list",
            "best-effort",
            "fail-open",
            "bearer",
            "catalogue",
            "continuous risk",
            "break-glass",
            "runtime discovery",
            "single kill",
            "project form",
            "shared policy",
            "central decision",
            "federated",
        )
        rejected_body = ""
        for p in pool:
            if p[:100] in used:
                continue
            low = p.lower()
            if any(k in low for k in rej_keys):
                rejected_body = p
                used.add(p[:100])
                break
        if not rejected_body:
            rejected_body = (
                f"A competent architect reaches for this under time pressure: {rejected} "
                "It is familiar, often already funded, and easy to defend in a review that never asks "
                "what happens when the optimistic assumption fails. It loses here because the safety claim "
                "would then rest on a quantity the organisation does not control, or on an unbounded object."
            )

        # Consequences: after-marker paras, else unused pool about buys/effects
        cons: list[str] = []
        for p in after + pool:
            if p[:100] in used:
                continue
            low = p.lower()
            if any(
                k in low
                for k in (
                    "buy",
                    "lose",
                    "makes",
                    "means",
                    "consequence",
                    "coverage",
                    "fail",
                    "refuse",
                    "bound",
                    "invariant",
                )
            ):
                cons.append(p)
                used.add(p[:100])
            if len(cons) >= 2:
                break
        if not cons:
            cons = [
                "The rejected alternative is not available as a silent default in conforming implementations. "
                "Markers in the spine resolve here; reopening needs an issue and an edition note."
            ]

        # Cost: numeric / priced paragraphs not yet used
        cost_body = ""
        for p in pool:
            if p[:100] in used:
                continue
            low = p.lower()
            if any(
                k in low
                for k in (
                    " ms",
                    "p99",
                    "engineer",
                    "€",
                    "latency",
                    "cost",
                    "people permanently",
                    "headcount",
                    "drill",
                    "%",
                    "minutes",
                )
            ):
                cost_body = p
                used.add(p[:100])
                break
        if not cost_body:
            cost_body = (
                "Cost is stated in the arguing chapter. This record does not invent a figure "
                "the spine does not price."
            )

        def join(ps: list[str], max_chars: int) -> str:
            buf: list[str] = []
            total = 0
            for p in ps:
                if total + len(p) > max_chars and buf:
                    break
                buf.append(p)
                total += len(p)
            return "\n\n".join(buf)

        decision_block = decision
        if dec_extra:
            decision_block = decision + "\n\n" + join(dec_extra, 1100)

        body = f"""# {sid}. {title} {{#{sid.lower()}}}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** {argued}

## Context

{join(context_paras, 1600)}

## Decision

{decision_block}

## Consequences

{join(cons, 1200)}

Markers `[{sid}]` in the spine resolve here. Reopening requires an issue and an edition note; do not silently invert the decision in a pull request.

## Rejected alternatives

**{rejected}**

{rejected_body}

## Cost

{cost_body}

## Reopen when

{reopen}
"""
        # If still thin, add one unused high-score paragraph under Consequences
        if len(body.split()) < 320:
            for p in sorted(pool, key=concrete_score, reverse=True):
                if p[:100] not in used:
                    body = body.replace(
                        "## Consequences\n\n",
                        f"## Consequences\n\n{p}\n\n",
                        1,
                    )
                    break

        path = DEC / item["file"]
        path.write_text(body, encoding="utf-8")
        count += 1
        print(f"  {sid}: {len(body.split())} words")
    return count


# --- Expanded appendix substance (inventory → useful) ---

APPENDICES: dict[str, str] = {}

APPENDICES["a-control-register.md"] = r'''# Appendix A. Control register {#appendix-a}

Normative requirements traced threat to control to test to evidence. RFC 2119 / RFC 8174 keywords appear only in this appendix and in the other appendices. In the spine the same rules are argued in plain declarative prose.

The key words "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" are to be interpreted as described in RFC 2119 and RFC 8174.

## Trusted computing base {#a-1-1}

The trusted computing base (TCB) MUST be limited to:

1. the gateway that mediates tool calls;
2. the decision path that permits or refuses a call;
3. the evidence path that writes tamper-evident records;
4. the key material under those three.

The agent, the model, the orchestration framework, tool implementations, prompt caches, and summarisers MUST sit outside the TCB. Adding a member to the TCB MUST reopen ADR-03 and produce an edition note. A control that depends on model behaviour for correctness is not a TCB control.

## Constraint classes and register framing {#a-1-2}

Every row in this register MUST name an obligation owner (person or body owed a demonstration), a control, a falsification test, and an evidence artefact. Rows that cite a regulation without naming those four fields are non-conforming. Constraints sort as imposed (estate or vendor), obligation (demonstration owed), or convention (renegotiable in the review). Convention MUST NOT be recorded as obligation.

## Approval card content {#a-1-4}

Above the reversibility line the approval surface MUST show: effect class, irreversibility, a diff against current system-of-record state, budget remaining, and the frozen call digest. Prompt text and model rationale MAY be stored as non-evidential attachment. They MUST NOT be presented as the object under approval. A card that cannot display the frozen artefact MUST fail closed for that gate.

## Key management and exit authority {#a-1-6}

Evidence content above personal-data thresholds MUST be encrypted under per-subject keys. Erasure of content MUST be implemented as witnessed key destruction with backup and replica coverage named in the runbook. Authority to exit a stop or degraded mode MUST be dual-controlled and distinct from authority to enter it. Restart without dual control on the evidence path MUST be refused.

## Risk tiers and acceptance register {#a-1-7}

Tiers MUST be discrete. Gap cases MUST be assigned to the higher tier. Borealis illustrative T2 ceiling: about €5,000 irreversible exposure per run. Open unmediated paths MUST appear in a risk-acceptance register with owner, dated review, and residual statement. An unmediated path without an acceptance row is a defect, not an exception.

## Promotion gates and policy-language bounds {#a-1-9}

Promotion of an agent version above the reversibility line MUST pass hard evaluation gates, or carry a signed time-bounded override with named acceptor and expiry. Policy-language evaluation on the hot path MUST be build-time bounded: no unbounded recursion or iteration. A bundle that fails the bound MUST NOT be signed.
'''

APPENDICES["b-architecture-decision-records.md"] = r'''# Appendix B. Architecture decision records {#appendix-b}

The thirty-nine ADRs live as individual files under `decisions/`. This appendix indexes them and holds the architectural views that the spine must not duplicate.

## Decision index {#a-2-0}

| ID | Decision (outcome form) | Argued in |
|---|---|---|
| ADR-01 | Containment over prevention-as-claim | ch. 1, 4 |
| ADR-02 | Run as unit of authority | ch. 3, 4 |
| ADR-03 | Frozen trusted computing base | ch. 3 |
| ADR-04 | Obligation-derived requirements | ch. 2 |
| ADR-05 | Discrete risk tiers | ch. 2 |
| ADR-06 | Two identity chains joined per run | ch. 5 |
| ADR-07 | Sender-constrained credentials | ch. 5 |
| ADR-08 | Brokered token exchange | ch. 5 |
| ADR-09 | Envelope as three-way intersection | ch. 6 |
| ADR-10 | Attenuation by construction | ch. 6 |
| ADR-11 | Allow-list of typed operations | ch. 6 |
| ADR-12 | Publish coverage as a dated ratio | ch. 4, 7 |
| ADR-13 | Single mediation topology by default | ch. 7 |
| ADR-14 | Protocol seam with authority in the gateway | ch. 8 |
| ADR-15 | Server-originated content untrusted | ch. 8 |
| ADR-16 | Pinned signed registry, no runtime discovery | ch. 8, 12 |
| ADR-17 | Declared side-effect class | ch. 8 |
| ADR-18 | Approval bound to frozen call digest | ch. 9 |
| ADR-19 | Failed gates fixed or removed | ch. 9 |
| ADR-20 | Entitlement-resolved retrieval | ch. 10 |
| ADR-21 | Memory as governed primary store | ch. 10 |
| ADR-22 | Erasure by key destruction | ch. 11 |
| ADR-23 | Fail closed on evidence | ch. 4, 11, 14 |
| ADR-24 | Embedded policy evaluation | ch. 13 |
| ADR-25 | Signed fail-posture matrix | ch. 4, 14 |
| ADR-26 | Five stop mechanisms | ch. 15 |
| ADR-27 | Unexercised controls are absent | ch. 4, 15, 16 |
| ADR-28 | Paved road as product | ch. 17 |
| ADR-29 | Derived child envelopes | ch. 18 |
| ADR-30 | No shared cross-org policy domain | ch. 19 |
| ADR-31 | Standing mandate for unattended runs | ch. 5 |
| ADR-32 | Recertify ceiling, need, and exercised set | ch. 16 |
| ADR-33 | No break-glass agent derivation | ch. 14, 15 |
| ADR-34 | Temporary deny-only fast path | ch. 13 |
| ADR-35 | Asymmetric in-flight policy | ch. 6 |
| ADR-36 | Purpose check on memory write | ch. 10 |
| ADR-37 | Separate artefacts bound by manifest | ch. 12 |
| ADR-38 | Pinned model set per tier | ch. 12 |
| ADR-39 | Context hash above reversibility line | ch. 11 |

Full records follow this appendix in the assembled document. Each record is Nygard form: context, decision, consequences, rejected alternatives, cost, reopen trigger.

## C4 views {#a-2-1}

Views live here, not in the spine. Edition 0.1 states placement and the questions each view must answer. Diagram files may be attached in a later cut; the prose below is authoritative for what the view must show.

**C1 – System context.** Question: which external actors and systems exchange credentials, tools, or evidence with the platform? Show: humans (principal, approver, operator), identity provider, model vendor, systems of record, external tool servers, auditors.

**C2 – Containers.** Question: which components see a run credential, and where is it verified? Show: broker, gateway, embedded policy evaluator, evidence store, registry, agent runtime (outside TCB).

**C3 – Gateway components.** Question: where does typed-call mediation, envelope check, approval compare, and evidence append happen? Show decision order on the hot path matching chapter 13.

Section semantics follow arc42; view levels follow the C4 model.

## Unbuildable across the organisational boundary {#a-2-30}

The following claims cannot be checked by a recipient without a live call into the issuer's TCB. They MUST NOT appear as hard gates in bilateral contracts without a verification path the recipient controls.

1. Portable full envelopes that re-encode another organisation's tier ceiling and principal reach.
2. Mutual mediation-coverage attestation as a hard connect gate.
3. Shared risk scores without a verification path into the scorer's decision inputs.
4. Foreign evidence chains treated as local evidence without a local attestation receipt.

Paired with ADR-30. What remains buildable: bilateral credentials the recipient can verify, claims the recipient can check locally, and contractual attestations with expiry owners.
'''

APPENDICES["c-threat-model-and-method.md"] = r'''# Appendix C. Threat model and method {#appendix-c}

Threat set for a hostile model with real tools. Method for regenerating threats when the set ages.

## Primary adversary {#a-3-1}

The primary adversary can shape inputs the agent reads – documents, web pages, email, tool descriptions, memory entries – and needs one successful instruction to act with authority the agent already holds. The model itself is treated as hostile at any moment, including between tool calls. The adversary is a person. The model is not the villain; it is an unreliable intermediary.

Secondary adversaries (insider misuse of approval, supply-chain compromise of a tool server, availability attacks on the evidence path) are in scope where they falsify an invariant. Physical robots, consumer agents, and model-training attacks are out of scope per chapter 1.

## Method {#a-3-2}

Derive threats from invariants I1–I8 (Appendix F). A threat that does not falsify an invariant is out of scope for this register. Refresh the set when a protocol, vendor, or regulation changes an assumption named in an ADR reopen trigger. Prefer threats with a worked path on the Borealis cast over abstract STRIDE categories without a seam attachment point.
'''

APPENDICES["d-artefact-schemas.md"] = r'''# Appendix D. Artefact schemas {#appendix-d}

Wire formats summarised. Edition 0.1 gives field inventories; JSON Schema files follow in a later cut. Examples in the spine MUST validate against these inventories.

## Run credential {#a-4-1}

| Field | Meaning |
|---|---|
| `sub` | Run identifier (unit of authority) |
| `act` | Workload identity and human principal (or standing-mandate id) |
| `aud` | Audience; gateway and declared systems of record |
| `cnf` | Confirmation / proof-of-possession (mTLS or DPoP) |
| `env` | Reference (digest) to the derived envelope |
| `exp` | Expiry aligned to run lifetime |

The credential references the envelope. It MUST NOT embed derivation inputs that would allow reconstruction of a wider envelope from the token alone.

## Envelope, mandate, budget {#a-4-2}

**Envelope.** Operations allow-list (typed names), object scopes, `derived_from` (parent digest or null), tier id. There is no widen field; widening is unrepresentable (ADR-10).

**Standing mandate.** Signing human, task class, ceiling (money or effect class), expiry, revocation pointer. Used when the principal chain has no interactive session (ADR-31).

**Budget.** Shared tool-call counter across a delegation tree. Null fields that must stay null by schema are listed explicitly so frameworks cannot silently invent defaults.

## Mediated tool call {#a-4-3}

Agent-supplied: operation name, typed arguments. Gateway-injected: run id, envelope digest, budget remaining, decision reference, side-effect class from registry. Authority fields MUST NOT originate on the agent side of the seam.

## Approval binding {#a-4-4}

Triple digests: frozen call, shown view, execution compare. Child delegation records carry the shared budget counter. A mismatch at execution MUST refuse the call (ADR-18).

## Evidence event and refusal {#a-4-5}

Evidence event: `effect_state`, `settled_by`, content ciphertext reference, optional context hash above the reversibility line. Refusal object: `excluded_by` naming which derivation input blocked the call. Foreign-attestation receipt is local evidence, not a foreign chain.

## Manifest promotion block {#a-4-6}

`promotion.evaluation` carries fail number, acceptor identity, override expiry. Model set per tier is pinned in the same manifest (ADR-38).

## Memory item and degraded refusal {#a-4-7}

Memory item: provenance, version, retention, purpose, entitlement scope. Degraded-mode refusal carries posture, matrix version, and capability set for UI. Human system-of-record actions enter the same evidence chain without a run id.
'''

APPENDICES["e-worked-examples.md"] = r'''# Appendix E. Worked examples {#appendix-e}

Compiled from spine worked moments. Edition 0.1 indexes the walkthroughs with the decision points a reader must be able to defend; full byte-level traces follow in a later cut.

## Onboard a tool {#a-5-1}

1. Publisher signs tool description and side-effect class.
2. Registry promotion requires conformance checks on push.
3. Pin digest into agent manifest; no runtime discovery.
4. First live call under mediation; refusal canary registered.

Compiles chapters 7–8. Constraint inventory template from chapter 2 belongs in the same onboarding pack: imposed / obligation / convention rows before the first envelope is derived.

## Derive an envelope {#a-5-2}

Intersection: declared need ∩ principal reach ∩ tier ceiling. Worked Borealis case: `claims-triage` under Marta's reach yields four typed operations against one claim. Unattended variant substitutes standing mandate for interactive principal.

## Graduate to unattended {#a-5-3}

Standing mandate signing ceremony, gate measurement for the human queue left behind, bundle staleness budget agreed. Compiles chapters 5, 9, 12.

## Work a suspected compromise {#a-5-4}

Stop within stated interval (chapter 15), evidence chain verify (chapter 11), coverage gap check (chapter 7). Eleven-minute historical stop at Borealis (2026-03-02) is the negative example: wrong lever first.
'''

APPENDICES["f-conformance-and-scorecard.md"] = r'''# Appendix F. Conformance and scorecard {#appendix-f}

Falsification tests for the three-part claim and invariants I1–I8.

## Claim tests {#a-6-1}

| Id | Claim | Pass | Fail |
|---|---|---|---|
| C1 | Bound listed before run | Enumerate reachable effects from envelope + credential; empty surprise set | Any reachable effect absent from the pre-run list |
| C2 | Evidence reconstructs effects | External actions match evidence events; chain verifies | Action without record, or silent rewrite |
| C3 | Stop within stated time | Revoke without agent help; wall-clock ≤ published interval | Run continues past interval, or stop requires agent cooperation |

## I1 coverage measurement {#a-6-2}

Publish mediated calls over discovered effect paths as a dated ratio. Discovery ownership MUST be separate from closure ownership. Open paths enter the acceptance register (A-1.7).

## Friction and attenuation depth {#a-6-3}

If coverage falls, measure minutes of path friction on the sanctioned road before rewriting policy. Attenuation MUST hold across delegation depth; depth and fan-out are bounded and measured quarterly.

## Seam, approval, memory, evidence, manifest, bundle age {#a-6-4}

| Invariant | Test sketch |
|---|---|
| I2 Seam | Authority field injected from agent side is ignored or refused |
| I5 Approval | Altered-post-approval payload refuses at execution |
| I6 Memory | External vs principal content distinguishable; provenance present |
| I3 Evidence | Evidence queue loss fails closed for effects |
| I7 Manifest | Declared need is manifest-sourced; digest mismatch refuses start |
| I8 Bundle | Stale bundle beyond staleness budget fails closed |

## Stop-path cost {#a-6-6}

Revocation check MUST fit inside the stated p99 budget on the hot path (illustrative 20–40 ms mediation envelope). Drill-measured stop intervals for L1–L5 are published beside the claim; an unexercised level is scored absent (ADR-27).
'''

APPENDICES["g-drills-and-calendar.md"] = r'''# Appendix G. Drills and calendar {#appendix-g}

Kill-switch drills, canaries, recertification. Owners and runbook references are required fields. A blank "last exercised" cell means the control is absent for the quarter (ADR-27).

## Operating calendar {#a-7-1}

| Cadence | Item | Owner (role) | Runbook | Notes |
|---|---|---|---|---|
| Quarterly | Stop drills L1–L5 | Platform SRE | stop-l1…l5 | Against live run |
| Quarterly | Degraded-mode entry/exit | Platform SRE | degraded-mode | Dual-control exit |
| Daily | Refusal canaries (above reversibility) | Platform on-call | canary-refuse | ~40 probes |
| Hourly | Revocation freshness sample | Platform on-call | revoke-fresh | Unknown ⇒ fail closed |
| Standing | Model-pin deprecation watch | Agent owners | model-deprec | Vendor calendar |
| Quarterly | Bilateral credential expiry review | Integration owner | bilateral-exp | Counterparties |
| Weekly | Recertification pack (ceiling, need, exercised set) | Data owner + platform | recert-pack | ADR-32 |

## Inventories and canaries {#a-7-2}

Maintain: endpoint configuration inventory; about 40 refusal canaries; memory provenance fraction; signed fail-posture matrix storage location reachable at 03:00. Canary failures open incidents, not tickets filed next week.

## Chain-break and revocation freshness {#a-7-3}

Evidence-break runbook: stop batch → reconcile → human-owned output. Revocation channel freshness unknown means fail closed for effects. Drill number for stop freshness belongs beside chapter 15 intervals.

## Manual path and composition telemetry {#a-7-4}

Manual system-of-record emergency path stays on the drill calendar (ADR-33). Quarterly: max observed delegation depth and fan-out versus configured limits (ADR-29).

## Deprecation and counterparty expiry {#a-7-5}

Vendor model-pin deprecation is a named standing job. Counterparties with lapsed schedules MUST NOT keep audiences that still accept their credentials without an acceptance row.
'''

APPENDICES["h-glossary.md"] = r'''# Appendix H. Glossary {#appendix-h}

Terms the field uses in two senses. This document picks one and names the other.

## Dual-sense terms {#a-8-1}

| Term | Sense that governs here | Sense that does not |
|---|---|---|
| Agent | Deployed workload / versioned software | Natural person; also not the run |
| Run | Bounded execution: one principal, one envelope, one budget, one evidence stream | Session, conversation, or deployment |
| Authority | Envelope: typed operations and scopes derived per run | IAM role or group membership alone |
| Policy | Allow-list derivation and hot-path evaluation bundles | Free-text business rule documents |
| Memory | Governed primary store with provenance and retention | Model weights or opaque vendor "memory" products |
| Gateway | Mediation seam that holds credentials and injects authority | Generic API management product |
| Coverage | Dated ratio of mediated paths over discovered effect paths | Marketing completeness claims |
| Envelope | Three-way intersection object (need ∩ reach ∩ ceiling) | Email or message wrapper |

Specification vocabulary (`cnf`, `act`, `aud`, `jti`) is defined at first use in the spine and is never italicised.
'''


def write_appendices() -> int:
    n = 0
    for name, body in APPENDICES.items():
        path = APP / name
        path.write_text(body.strip() + "\n", encoding="utf-8")
        n += 1
        print(f"  appendix {name}: {len(body.split())} words")
    readme = """# Appendices

Edition 0.1. Spine markers such as `[A-6.1]` resolve to headings in these files.

- [Appendix A. Control register](a-control-register.md)
- [Appendix B. Architecture decision records](b-architecture-decision-records.md)
- [Appendix C. Threat model and method](c-threat-model-and-method.md)
- [Appendix D. Artefact schemas](d-artefact-schemas.md)
- [Appendix E. Worked examples](e-worked-examples.md)
- [Appendix F. Conformance and scorecard](f-conformance-and-scorecard.md)
- [Appendix G. Drills and calendar](g-drills-and-calendar.md)
- [Appendix H. Glossary](h-glossary.md)
"""
    (APP / "README.md").write_text(readme, encoding="utf-8")
    return n


def main() -> None:
    print("Fixing chapter asides…")
    print(f"  fixed {fix_asides()}")
    print("Deepening ADRs…")
    print(f"  wrote {deepen_adrs()} ADRs")
    print("Expanding appendices…")
    print(f"  wrote {write_appendices()} appendices")


if __name__ == "__main__":
    main()
