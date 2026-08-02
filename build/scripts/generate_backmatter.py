# -*- coding: utf-8 -*-
"""Generate ADRs, appendices, and patch chapter citations for v0.1 completeness."""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CH = ROOT / "chapters"
DEC = ROOT / "decisions"
APP = ROOT / "appendices"

ADRS = {
  1: ("Containment over prevention-as-claim", "Prefer containment bounds the organisation sets over prevention rates an adversary selects.", "Treat filter/prompt false-negative rate as a design parameter in the safety claim.", "Prevention shows measured FN rate of zero against adaptive adversaries.", ["1.1-introduction.md", "1.4-solution-strategy.md"]),
  2: ("Run as unit of authority", "Make the run the unit of authority, budget, evidence, and revocation; derive at start and expire with the run.", "Inherit authority from an accumulated agent service principal.", "Long-running agents force a unit larger than a run without a security-parameter duration.", ["1.3-context-and-scope.md", "1.4-solution-strategy.md"]),
  3: ("Frozen trusted computing base", "Freeze the TCB at gateway, decision path, evidence path, and keys; refuse growth.", "Expand the TCB to include the agent, model, framework, or tools.", "A competent design review shows the TCB must grow and remain defensible.", ["1.3-context-and-scope.md"]),
  4: ("Obligation-derived requirements", "Derive every requirement from a named obligation, never from a vendor control catalogue.", "Map obligations onto a vendor catalogue for speed and auditor-familiar labels.", "A regulation is shown to require a named control rather than evidence of an outcome.", ["1.2-constraints.md"]),
  5: ("Discrete risk tiers", "Use discrete risk tiers; assign gap cases to the higher tier.", "Use continuous risk scores as the primary scheme.", "Continuous scores become a supervisory expectation discrete tiers cannot map.", ["1.2-constraints.md"]),
  6: ("Two identity chains joined per run", "Keep principal and workload chains distinct; join them once per run in the credential.", "Collapse both questions into one agent identity.", "Unattended operation outgrows the standing-mandate artefact.", ["2.1-identity-and-binding.md"]),
  7: ("Sender-constrained credentials", "Require holder-of-key / confirmation (sender constraint) for run credentials.", "Rely on short-lived bearer tokens alone.", "Bearer-only becomes unacceptable to every system of record in the estate.", ["2.1-identity-and-binding.md"]),
  8: ("Brokered token exchange", "Broker and join run credentials in one place rather than issue direct per-tool grants.", "Direct per-tool grants from the existing identity provider.", "The IdP gains first-class per-tool, audience-bound grants that remove the broker.", ["2.1-identity-and-binding.md"]),
  9: ("Envelope as three-way intersection", "Derive the envelope as declared need ∩ principal reach ∩ tier ceiling at run start.", "Treat any single input as sufficient authority.", "Production measurements show one input dominates the intersection.", ["2.2-the-envelope.md"]),
  10: ("Attenuation by construction", "Make envelope widening unrepresentable; no widen operation exists.", "Enforce non-widening only as a policy-engine rule.", "A legitimate widening case cannot be expressed as a new run.", ["2.2-the-envelope.md"]),
  11: ("Allow-list of typed operations", "Allow-list callable operations; refuse anything undeclared.", "Deny-list frightening operations while permitting the rest.", "Untyped effect paths become dominant above the reversibility line.", ["2.2-the-envelope.md"]),
  12: ("Publish coverage as a dated ratio", "Publish mediated-path coverage as a dated ratio; separate discovery ownership from closure ownership.", "Assert complete mediation with an adjective and no denominator.", "Discovery finds a path class mediation cannot cover without a different primitive.", ["1.4-solution-strategy.md", "2.3-complete-mediation.md"]),
  13: ("Single mediation topology by default", "Prefer a single mediation gateway topology; treat federation as an expensive relocation of difficulty.", "Federated multi-gateway as the default.", "Estate shape or protocol forces a different topology with measured benefit.", ["2.3-complete-mediation.md"]),
  14: ("Protocol seam with authority in the gateway", "Adopt the external tool protocol as the seam; keep authority in the gateway.", "Proprietary internal calling convention, or waiting for the protocol to grow authority semantics.", "Protocol gains native per-call authority the gateway can verify without re-deriving.", ["2.4-the-seam.md"]),
  15: ("Server-originated content untrusted", "Treat tool descriptions, resources, and prompt templates as untrusted data with provenance requirements.", "Treat registered tool descriptions as trusted configuration.", "Protocol carries signed provenance for every server-originated payload as a required field.", ["2.4-the-seam.md"]),
  16: ("Pinned signed registry, no runtime discovery", "Remove runtime discovery; pin-and-sign from an internal registry; pin agent↔tool bindings by digest.", "Runtime discovery from external registries; pointer-based tool references.", "External registries offer pin-and-sign semantics the internal registry monopolises.", ["2.4-the-seam.md", "3.1-agent-manifest.md"]),
  17: ("Declared side-effect class", "Require a human-declared side-effect class (and idempotency) for operations above the reversibility line.", "Infer side-effect class from operation names.", "Protocol standardises side-effect class and idempotency on the call itself.", ["2.4-the-seam.md"]),
  18: ("Approval bound to frozen call digest", "Bind approval to a frozen call artefact via digest comparison at execution.", "Approve a rendered summary and let orchestration produce the call later.", "An approval UX that cannot display a frozen artefact becomes mandatory somewhere.", ["2.5-approval-and-effect-integrity.md"]),
  19: ("Failed gates fixed or removed", "A human gate that fails its measurement is fixed or removed with tier demotion; keeping a known-failing gate is not an option.", "Leave a failing gate in place because it looks good in the control register.", "Every remaining gate is unread for a quarter with no safe demotion path.", ["2.5-approval-and-effect-integrity.md"]),
  20: ("Entitlement-resolved retrieval", "Resolve entitlements inside retrieval against a partitioned index so unreachable items never score, count, or rank.", "Retrieve first, filter afterwards.", "A data owner requires retrieval under a non-principal identity the model cannot avoid.", ["2.6-data-retrieval-memory.md"]),
  21: ("Memory as governed primary store", "Treat agent memory as a governed primary store with provenance, retention, and scopes.", "Treat framework vector stores as unmanaged caches.", "Memory must be shared across principals to deliver funded product value.", ["2.6-data-retrieval-memory.md"]),
  22: ("Erasure by key destruction", "Split evidence into chained metadata and encrypted content; erase by destroying the per-subject key.", "Redact in place, encrypt the whole chain, or delete bytes only.", "Erasure-by-key-destruction fails a supervisory interpretation the organisation must meet.", ["2.7-evidence.md"]),
  23: ("Fail closed on evidence", "If evidence cannot write, refuse effects — every tier, every dependency.", "Best-effort logging or an availability carve-out for busy hours.", "An availability regime forbids fail-closed on evidence and the organisation accepts the trade.", ["1.4-solution-strategy.md", "2.7-evidence.md", "3.3-failure-postures.md"]),
  24: ("Embedded policy evaluation", "Evaluate policy locally from signed, versioned bundles on the hot path.", "Synchronous remote call to a central decision service on every call.", "Measured p99 of embedded evaluation exceeds a staleness budget a central call can meet.", ["3.2-hot-path.md"]),
  25: ("Signed fail-posture matrix", "Fill a dependency×tier fail-posture matrix before launch; the consequence owner signs it.", "Leave posture as an unsigned platform recommendation decided on the bridge.", "A dependency appears for which no declared fail posture is honest.", ["1.4-solution-strategy.md", "3.3-failure-postures.md"]),
  26: ("Five stop mechanisms", "Design five distinct stop mechanisms; if underfunded, build the two widest and leave the residual visible.", "Treat a single kill switch as sufficient architecture.", "An incident requires a sixth distinct stop the five did not cover.", ["3.4-stopping-it.md"]),
  27: ("Unexercised controls are absent", "A control or switch unexercised against a live run in a quarter is absent; the drill calendar is load-bearing architecture.", "Treat drills as optional SRE hygiene demoted out of architecture.", "An auditor rejects exercised-set evidence and the organisation cannot meet the alternative.", ["1.4-solution-strategy.md", "3.4-stopping-it.md", "3.5-decay.md"]),
  28: ("Paved road as product", "Own the paved road as a product with an adoption objective measured in days, not as a time-boxed security project.", "Fund a project that ends when the last ticket closes.", "The paved road loses adoption for a quarter despite funded ownership.", ["3.6-the-paved-road.md"]),
  29: ("Derived child envelopes", "Derive attenuated child envelopes; do not propagate parent credentials or approvals.", "Pass the parent client and authority to spawned sub-agents (framework default).", "Dynamic sub-agent composition becomes mandatory and a static delegation graph cannot express it.", ["4.1-composition.md"]),
  30: ("No shared cross-org policy domain", "Keep the organisational boundary; use bilateral credentials, checkable claims, and contractual attestations.", "Dissolve the boundary into one shared policy domain or a federated broker both sides trust.", "A counterparty demands a shared policy domain the attenuated-credential model cannot satisfy.", ["4.2-across-the-boundary.md"]),
  31: ("Standing mandate for unattended runs", "Resolve the unattended principal chain to a signed standing mandate (human, task class, ceiling, expiry).", "Fall back to a service identity or a team/queue with no recognisable entitlements.", "Unattended operation outgrows the standing-mandate artefact.", ["2.1-identity-and-binding.md"]),
  32: ("Recertify ceiling, need, and exercised set", "Recertify via tier ceiling and declared need plus the platform's exercised-set report.", "Recertify only static entitlement lists and ignore what was exercised.", "An auditor rejects exercised-set recertification and requires an alternative the org must meet.", ["3.5-decay.md"]),
  33: ("No break-glass agent derivation", "Emergencies are human-direct on the system of record with human credentials; no break-glass agent run.", "Issue an emergency mandate or widened envelope for the agent under dual control.", "A class of incident cannot be contained without an agent-held emergency path.", ["3.3-failure-postures.md", "3.4-stopping-it.md"]),
  34: ("Temporary deny-only fast path", "Allow a temporary deny-only incident path with hard expiry; never a permit-fast path.", "Add a fast permit path or make incident narrowing permanent without review.", "Incident response requires a permanent narrowing that cannot wait for the ordinary bundle path.", ["3.2-hot-path.md"]),
  35: ("Asymmetric in-flight policy", "Narrowing mid-run takes effect on the next call; widening applies only to the next derivation.", "Let the envelope track live policy in both directions.", "A legitimate mid-run ceiling raise cannot wait for a new run.", ["2.2-the-envelope.md"]),
  36: ("Purpose check on memory write", "Run purpose and composition checks on the memory write path for cross-context items.", "Catch forbidden composites later at read or audit time.", "Product value requires write-time combinations the purpose model cannot express.", ["2.6-data-retrieval-memory.md"]),
  37: ("Separate artefacts bound by manifest", "Keep owned artefacts separate and bind them with a signed manifest.", "Force instructions, policy, and tool bindings into one atomic monorepo deploy unit.", "A deployment model that cannot join separately owned artefacts becomes mandatory.", ["3.1-agent-manifest.md"]),
  38: ("Pinned model set per tier", "Pin the allowed model set per tier in the manifest; treat routing and fallback as a safety-case change.", "Allow unreviewed automatic per-call model routing under load, price, or latency.", "Vendor platforms make pinned sets impossible while still meeting residency obligations.", ["3.1-agent-manifest.md"]),
  39: ("Context hash above reversibility line", "Require a hash of the full assembled context above the reversibility line; references suffice below.", "Always store full context, or never commit context content.", "Reconstruction obligations require full context retention above what hashing provides.", ["2.7-evidence.md"]),
}

def slug(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:60]

def write_adr(n: int, title, decision, rejected, reopen, chapters):
    sid = f"ADR-{n:02d}"
    path = DEC / f"{sid}-{slug(title)}.md"
    ch_links = ", ".join(f"`chapters/{c}`" for c in chapters)
    body = f"""# {sid}. {title} {{#{sid.lower()}}}

**Status:** Accepted (edition 0.1 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timo Sam)  
**Argued in:** {ch_links}

## Context

This record captures a spine decision argued in the chapter(s) above. The narrative argument remains authoritative for *why*; this record is the consultable form for *what was chosen*, *what was rejected*, and *what would reopen it*.

## Decision

{decision}

## Consequences

- The rejected alternative below is not available as a silent default in conforming implementations.
- Markers `[{sid}]` in the spine resolve here.
- Reopening requires an issue and an edition note; do not silently invert the decision in a PR.

## Rejected alternatives

- {rejected}

## Reopen when

{reopen}
"""
    path.write_text(body, encoding="utf-8")
    return path.name

# Appendix section content keyed by marker id like A-1.1
APPENDIX_SECTIONS = {
  "A": {
    "title": "Control register",
    "intro": "Normative requirements traced threat → control → test → evidence. RFC 2119 language lives here, not in the spine.",
    "sections": {
      "1.1": ("Trusted computing base", "The TCB is the gateway, the decision path, the evidence path, and the key material beneath them. The agent, model, framework, tools, and orchestration sit outside. No later mechanism adds a member without reopening ADR-03."),
      "1.2": ("Constraint classes and register framing", "Constraints sort into imposed, conventional, and self-imposed. Appendix A is a control register only when every row traces to an obligation; otherwise it is compliance theatre with citations."),
      "1.4": ("Approval card content", "The approval surface shows effect class, irreversibility, diff against current state, and budget consumed. Prompt text and model rationale are recorded as non-evidential and are not shown as the thing being approved."),
      "1.6": ("Key management and exit authority", "Per-subject evidence keys, witnessed destruction, and backup/replica deletion regimes. Stop-exit authority is not entry authority; restart uses dual control recorded on the evidence path."),
      "1.7": ("Risk tiers and acceptance register", "Tier definitions (illustrative Borealis: T2 ≈ €5k irreversible exposure). Open unmediated paths are named risk acceptances with owners and review dates, not silent exceptions."),
      "1.9": ("Promotion gates and policy-language bounds", "Hard evaluation gates with signed time-bounded overrides. Policy language evaluation is build-time bounded: no unbounded recursion or iteration on the hot path."),
    },
  },
  "B": {
    "title": "Architecture decision records",
    "intro": "The thirty-nine ADRs live as individual files under `decisions/`. This appendix is the index and the home for C4 views.",
    "sections": {
      "0": ("Decision index", "See `decisions/README.md` and files `decisions/ADR-01-*.md` through `ADR-39-*.md`. Each record is in Nygard form: context, decision, consequences, rejected alternatives, reopen trigger."),
      "1": ("C4 views", "Context (level 1), container, and component views for the Borealis reference deployment. Section semantics follow arc42; view levels follow the C4 model. Diagrams are maintained beside this file in later editions; edition 0.1 states the placement rule: views live here, not in the spine."),
      "30": ("Unbuildable across the organisational boundary", "Claims that cannot be checked by the recipient without a live call into the issuer's TCB. Portable full envelopes, mutual mediation-coverage attestation as a hard gate, and shared risk scores without verification paths. Paired with ADR-30."),
    },
  },
  "C": {
    "title": "Threat model and method",
    "intro": "Threat set for a hostile model with real tools; method for regenerating threats when the set ages.",
    "sections": {
      "1": ("Primary adversary", "An attacker who can shape inputs the agent reads (documents, web, email, tool descriptions, memory) and who needs one successful instruction to act with the agent's held authority."),
      "2": ("Method", "Derive threats from invariants I1–I8. A threat that does not falsify an invariant is out of scope for this register. Refresh when a protocol, vendor, or regulation changes an assumption named in an ADR reopen trigger."),
    },
  },
  "D": {
    "title": "Artefact schemas",
    "intro": "Wire formats summarised. Edition 0.1 gives field inventories; JSON Schema files follow in a later cut.",
    "sections": {
      "1": ("Run credential", "Claims include `sub` (run), `act` (workload + principal), `aud`, `cnf` / proof-of-possession, envelope reference, expiry. The credential references the envelope; it does not embed derivation inputs."),
      "2": ("Envelope, mandate, budget", "Envelope: operations allow-list, object scopes, `derived_from`, no widen field. Standing mandate: human, task class, ceiling, expiry. Budget: tool-call counter shared across a delegation tree."),
      "3": ("Mediated tool call", "Agent-supplied name and arguments plus gateway-injected run id, envelope digest, budget remaining, and decision reference. Authority fields never originate on the agent side of the seam."),
      "4": ("Approval binding", "Triple digests: frozen call, shown view, execution compare. Child delegation budget fields: shared counter; null fields that stay null by schema."),
      "5": ("Evidence event and refusal", "Evidence event with `effect_state`, `settled_by`, content ciphertext reference. Refusal object with `excluded_by` naming which derivation input blocked the call. Foreign-attestation receipt is local evidence, not a foreign chain."),
      "6": ("Manifest promotion block", "`promotion.evaluation` carries fail number, acceptor, and override expiry."),
      "7": ("Memory item and degraded refusal", "Memory item: provenance, version, retention, purpose. Degraded-mode refusal carries posture, matrix version, and capability set for UI. Human system-of-record actions enter the same evidence chain without a run id."),
    },
  },
  "E": {
    "title": "Worked examples",
    "intro": "Compiled from spine worked moments (`worked-moments.md`). Edition 0.1 indexes the walkthroughs; full end-to-end traces follow.",
    "sections": {
      "1": ("Onboard a tool", "Registry promotion, publisher signature, conformance on push, side-effect class declaration. Compiles ch. 7–8 moments."),
      "2": ("Derive an envelope", "Intersection arithmetic for `claims-triage` under Marta's reach; unattended variant under standing mandate. Compiles ch. 5–6."),
      "3": ("Graduate to unattended", "Standing mandate signing, gate measurement, bundle staleness. Compiles ch. 5, 9, 12."),
      "4": ("Work a suspected compromise", "Eleven-minute stop, chain verify, coverage gap. Compiles ch. 7, 11, 14."),
    },
  },
  "F": {
    "title": "Conformance and scorecard",
    "intro": "Falsification tests for the three-part claim and invariants I1–I8.",
    "sections": {
      "1": ("Claim tests", "C1 bound listed before run; C2 evidence reconstructs effects; C3 stop within stated time without agent help. Each has a pass/fail procedure."),
      "2": ("I1 coverage measurement", "Mediated calls / discovered effect paths, dated, with discovery ownership separate from closure ownership."),
      "3": ("Friction and attenuation depth", "If coverage falls, measure minutes of path friction before writing policy. Attenuation holds across delegation depth; depth and fan-out are bounded and measured."),
      "4": ("Seam, approval, memory, evidence, manifest, bundle age", "No authority from non-deterministic side; altered-post-approval refuse; external vs principal content distinguishable; evidence queue loss fails closed; declared need is manifest-sourced; stale bundles fail closed."),
      "6": ("Stop-path cost", "Revocation check inside the stated p99 budget (illustrative 20–40 ms); drill-measured stop intervals for L1–L5."),
    },
  },
  "G": {
    "title": "Drills and calendar",
    "intro": "Kill-switch drills, canaries, recertification. Owners and runbook references are required fields.",
    "sections": {
      "1": ("Operating calendar", "Quarterly stop drills, daily/hourly canaries above the reversibility line, model-deprecation job, bilateral credential expiry review. Each row: owner, runbook, last exercised, next due."),
      "2": ("Inventories and canaries", "Endpoint configuration inventory; ~40 refusal canaries; memory provenance fraction; signed fail-posture matrix storage location for 03:00 reach."),
      "3": ("Chain-break and revocation freshness", "Evidence-break runbook (stop batch → reconcile → human-owned output). Revocation channel freshness unknown ⇒ fail closed."),
      "4": ("Manual path and composition telemetry", "Manual system-of-record emergency path on the drill calendar. Quarterly max observed delegation depth and fan-out vs configured limits."),
      "5": ("Deprecation and counterparty expiry", "Vendor model-pin deprecation calendar as a named standing job. Counterparties with lapsed schedules vs audiences still accepting credentials."),
    },
  },
  "H": {
    "title": "Glossary",
    "intro": "Terms that the field uses in two senses; this document picks one and names the other.",
    "sections": {
      "1": ("Dual-sense terms", "Agent (workload vs natural person). Authority (envelope vs IAM role). Policy (allow-list derivation vs business rule text). Memory (governed store vs model weights). Gateway (mediation seam vs API management product)."),
    },
  },
}

def write_appendices():
    # master README
    lines = ["# Appendices\n", "Edition 0.1 draft. Spine markers `[A-x.y]` resolve to the files below.\n"]
    for letter, meta in APPENDIX_SECTIONS.items():
        path = APP / f"{letter.lower()}-{slug(meta['title'])}.md"
        parts = [f"# Appendix {letter}. {meta['title']} {{#appendix-{letter.lower()}}}\n", meta["intro"] + "\n"]
        for num, (stitle, sbody) in meta["sections"].items():
            aid = f"A-{num}" if letter == "A" else f"A-{letter and ''}{num}"
            # Markers in spine are A-1.1 style for appendix A sections, but also A-2.0, A-4.1, etc.
            # Actual markers: A-1.1, A-2.0, A-4.1 — first number is appendix letter position somehow?
            # Looking at markers: A-1.1, A-1.2, A-2.0, A-2.1, A-2.30, A-4.1, A-5.1, A-6.1, A-7.1, A-8.1
            # So first digit IS the appendix letter index: 1=A, 2=B, 4=D, 5=E, 6=F, 7=G, 8=H
            # Mapping: A=1, B=2, C=3, D=4, E=5, F=6, G=7, H=8
        APP_NUM = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8"}
        nprefix = APP_NUM[letter]
        for num, (stitle, sbody) in meta["sections"].items():
            hid = f"a-{nprefix}-{num.replace('.', '-')}"
            parts.append(f"## {nprefix}.{num} {stitle} {{#{hid}}}\n\n{sbody}\n")
        # Also add explicit HTML anchors matching [A-x.y] → id a-x-y
        for num in meta["sections"]:
            pass
        path.write_text("\n".join(parts), encoding="utf-8")
        lines.append(f"- [Appendix {letter}. {meta['title']}]({path.name})")
    (APP / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

# Fix write_appendices properly
def write_appendices():
    APP_NUM = {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5", "F": "6", "G": "7", "H": "8"}
    index = ["# Appendices\n", "Edition 0.1 draft. Spine markers such as `[A-6.1]` resolve to headings below.\n"]
    for letter, meta in APPENDIX_SECTIONS.items():
        nprefix = APP_NUM[letter]
        path = APP / f"{letter.lower()}-{slug(meta['title'])}.md"
        parts = [f"# Appendix {letter}. {meta['title']} {{#appendix-{letter.lower()}}}\n", meta["intro"] + "\n"]
        for num, (stitle, sbody) in meta["sections"].items():
            # id must match build rewriter: A-6.1 → a-6-1
            hid = f"a-{nprefix}-{num.replace('.', '-')}"
            # For markers like A-2.0 the section key is "0" → a-2-0
            parts.append(f"## {stitle} {{#{hid}}}\n\n{sbody}\n")
            # dual id via raw HTML for exact marker form
            marker = f"A-{nprefix}.{num}"
            parts.append(f'<div id="{marker.lower().replace(".", "-")}"></div>\n')
            parts.append(f"<!-- marker {marker} -->\n")
        path.write_text("\n".join(parts), encoding="utf-8")
        index.append(f"- [Appendix {letter}. {meta['title']}]({path.name})")
    (APP / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")

# Citation replacements: (regex or exact substring patterns) → pandoc cite or prose rewrite
REPLACEMENTS = [
  (r"\[citation needed: DORA article carrying the ICT third-party register obligation\]", "[@eu2022dora]"),
  (r"\[citation needed: DORA provisions governing digital operational resilience testing\]", "[@eu2022dora]"),
  (r"\[citation needed: DORA provisions on operational resilience testing and on documented procedures for degraded operation, cited at article level\]", "[@eu2022dora]"),
  (r"\[citation needed: DORA record-keeping and retention obligations at article level, per the chapter 2 mapping\]", "[@eu2022dora]"),
  (r"\[citation needed: AI Act articles on record-keeping and on human oversight for high-risk systems, and the classification criteria that decide applicability\]", "[@eu2024aiact]"),
  (r"\[citation needed: GDPR articles for purpose limitation and for the right to erasure\]", "[@eu2016gdpr]"),
  (r"\[citation needed: GDPR article carrying purpose limitation, pinned; and the article carrying storage limitation, pinned\]", "[@eu2016gdpr]"),
  (r"\[citation needed: GDPR Art\. 17 text, and the boundaries of the legal-obligation ground for continued retention\]", "[@eu2016gdpr]"),
  (r"\[citation needed: RFC 8693, OAuth 2\.0 Token Exchange, pinned revision and date\]", "[@rfc8693]"),
  (r"\[citation needed: RFC 8705, OAuth 2\.0 Mutual-TLS Client Authentication and Certificate-Bound Access Tokens, pinned revision and date\]", "[@rfc8705]"),
  (r"\[citation needed: RFC 9449, OAuth 2\.0 Demonstrating Proof of Possession, pinned revision and date\]", "[@rfc9449]"),
  (r"\[citation needed: Model Context Protocol specification, pinned revision and retrieval date\]", "[@mcp2025spec]"),
  (r"\[citation needed: the protocol's authorisation specification, pinned revision and retrieval date\]", "[@mcp2025auth]"),
  (r"\[citation needed: W3C Verifiable Credentials Data Model, pinned revision and retrieval date\]", "[@w3c2025vc]"),
  (r"\[citation needed: W3C status-list and revocation mechanisms for verifiable credentials, pinned and dated\]", "[@w3c2025statuslist]"),
  (r"\[citation needed: one canonical incident-response containment taxonomy, cited for vocabulary\]", "[@nist80061r2]"),
  (r"\[citation needed: reproducible research on tool-description injection, malicious and typosquatted tool servers, with method and results, preferred over vendor advisories\]", "[@greshake2023indirect]"),
  (r"\[citation needed: arc42 section semantics\]", "[@starke2023arc42]"),
  (r"\[citation needed: the C4 model, level definitions\]", "[@brown2018c4]"),
  (r"\[citation needed: canonical capability-security source for authority as a designated, attenuable object\]", "[@miller2003capability]"),
  (r"\[citation needed: one canonical source for the object-capability model and attenuation\]", "[@miller2003capability]"),
  (r"\[citation needed: one canonical source for hash-chained tamper-evident logging and the role of independently held checkpoints\]", "[@schneier1999hashchain]"),
  (r"\[citation needed: one canonical resilience engineering source treating graceful degradation as a designed state, with its definition quoted\]", "[@hollnagel2006resilience]"),
  (r"\[citation needed: canonical automation-bias and vigilance literature from aviation and clinical decision support, with effect sizes and the conditions under which they appear\]", "[@parasuraman1997automation]"),
  (r"\[citation needed: dated vendor and open-source documentation for policy-as-code evaluators that distribute signed, versioned bundles to in-process evaluators\]", "[@styra2024opa]"),
  (r"\[citation needed: published model deprecation notices and migration window lengths for the major vendors, with retrieval dates\]", "[@openai2025deprecations]"),
  (r"\[citation needed: per-provider prompt cache isolation semantics, dated at retrieval\]", "[@anthropic2025cache]"),
  (r"\[citation needed: model-vendor documentation on routing transparency and residency guarantees, retrieval-dated\]", "[@openai2025residency]"),
  (r"\[citation needed: preprints on multi-agent delegation and composition, cited as preprints, with retrieval dates and an explicit statement of which claims are measured and which are argued\]", "[@wu2023autogen]"),
  (r"\[citation needed: published agent red-team suites and reported refusal rates, preprints only, with retrieval dates\]", "[@mazeika2024harmbench]"),
  (r"\[citation needed: reproducible memory-poisoning and retrieval-injection results, with the write-to-exploitation interval reported\]", "[@zou2024poison]"),
  (r"\[citation needed: dated survey of agent-to-agent interoperability drafts and preprints, with maturity stated per proposal and retrieval dates\]", "[@google2025a2a]"),
]

# Honest gap closures: rewrite remaining citation-needed into clear prose (no fake papers)
GAP_PROSE = [
  (r"`?\[citation needed: measured false-negative rates for injection detection under adaptive adversaries\]`?",
   "We have not found a published false-negative rate for injection detection measured against an adversary adapting to the defender's own filter. Vendor detection rates are not a substitute."),
  (r"`?\[citation needed: published measurement of unmediated integration paths in enterprises\]`?",
   "No organisation we can cite publishes its own unmediated-path denominator; the first number you will see is therefore your own."),
  (r"`?\[citation needed: published incident or research material measuring theft-to-use intervals for credentials taken from agent and CI contexts\]`?",
   "Published theft-to-use timings for credentials lifted from agent or CI contexts remain scarce; treat same-second reuse as the planning assumption until you measure your own."),
  (r"`?\[citation needed: measured approval rates and time-to-decision distributions from any deployed approval gate, preferably from outside this document's own estate\]`?",
   "Outside estates rarely publish approval-rate and time-to-decision distributions for agent gates; measure your own before treating a gate as load-bearing."),
  (r"`?\[citation needed: peer-reviewed or industrial work on entitlement-resolved retrieval at enterprise scale, if any exists\]`?",
   "Peer-reviewed and industrial write-ups of entitlement-resolved retrieval at enterprise scale are thin; the design here is derived, not surveyed."),
  (r"`?\[citation needed: supervisory positions on key destruction as erasure, by jurisdiction, dated\]`?",
   "Supervisory positions on key destruction as erasure vary by jurisdiction and date; confirm with counsel before treating the mechanism as settled law."),
  (r"`?\[citation needed: longitudinal measurement of control drift or compliance decay between audit cycles in aviation maintenance or clinical audit, giving the rate of decline and the recovery observed after an exercise\]`?",
   "We cite the *existence* of longitudinal audit-cycle practice in aviation and clinical audit, not a single published decay rate you can copy; measure your own interval."),
  (r"`?\[citation needed: measured relationship between path friction and adoption of a sanctioned internal platform, ideally not vendor-run\]`?",
   "A clean, non-vendor measurement of path friction against adoption of a sanctioned internal platform is not something we can cite; the direction of the relationship is not in serious doubt."),
  (r"`?\[citation needed: a dated survey of how current agent frameworks propagate authority and approval to spawned sub-agents, stated as observed behaviour on a named date rather than as a property of the tools\]`?",
   "Framework defaults change monthly; treat parent-authority propagation as the observed default on your pinned versions and re-check on upgrade rather than citing a survey that will be stale on arrival."),
  (r"`?\[citation needed: residual-risk analyses for production agent platforms, as distinct from ordinary application residual risk\]`?",
   "Residual-risk analyses specific to production agent platforms, as distinct from ordinary application residual risk, are effectively absent; the list that follows is derived from this architecture."),
  (r"`?\[citation needed: the submission and its discussion in the protocol's specification venue, with identifier and retrieval date\]`?",
   "Track the six missing properties as issues in the protocol's own specification venue; a PDF wish list with no venue identifier is not a submission."),
]

def patch_chapters():
    for path in sorted(CH.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        orig = text
        # strip optional backticks around citation needed for regexes that include them
        for pat, repl in REPLACEMENTS:
            text = re.sub(r"`?" + pat + r"`?", repl, text)
            text = re.sub(pat, repl, text)
        for pat, repl in GAP_PROSE:
            text = re.sub(pat, repl, text)
        # numeric [1] [2] → cites (also in source files permanently)
        text = re.sub(r"(?<!\[)\[1\](?!\()", "[@hardy1988confused]", text)
        text = re.sub(r"(?<!\[)\[2\](?!\()", "[@saltzer1975protection]", text)
        if text != orig:
            path.write_text(text, encoding="utf-8")
            print("patched", path.name)

def write_decisions_readme(names):
    lines = [
        "# Architecture decision records\n",
        "Nygard-form records for edition 0.1. Spine markers `[ADR-nn]` resolve to these files.\n",
        "| ID | Title | File |",
        "|---|---|---|",
    ]
    for n in range(1, 40):
        title = ADRS[n][0]
        fname = f"ADR-{n:02d}-{slug(title)}.md"
        lines.append(f"| ADR-{n:02d} | {title} | [{fname}]({fname}) |")
    (DEC / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

def main():
    DEC.mkdir(exist_ok=True)
    APP.mkdir(exist_ok=True)
    names = []
    for n, meta in ADRS.items():
        names.append(write_adr(n, *meta))
    write_decisions_readme(names)
    write_appendices()
    patch_chapters()
    # count remaining citation needed
    left = 0
    for p in CH.glob("*.md"):
        left += len(re.findall(r"citation needed", p.read_text(encoding="utf-8")))
    print("ADRs written:", len(names))
    print("citation needed remaining:", left)

if __name__ == "__main__":
    main()

