# -*- coding: utf-8 -*-
from pathlib import Path
import re

ROOT = Path(r"H:\repos\bounded-agents")
APP = ROOT / "appendices"
DEC = ROOT / "decisions"

# letter -> (title, intro, {section_num: (title, body)})
# Markers are A-{appendix_num}.{section_num}
DATA = {
"A": ("Control register",
"Normative requirements traced threat to control to test to evidence. RFC 2119 language lives here, not in the spine.",
{
"1": ("Trusted computing base", "The TCB is the gateway, the decision path, the evidence path, and the key material beneath them. The agent, model, framework, tools, and orchestration sit outside. No later mechanism adds a member without reopening ADR-03."),
"2": ("Constraint classes and register framing", "Constraints sort into imposed, conventional, and self-imposed. Appendix A is a control register only when every row traces to an obligation; otherwise it is compliance theatre with citations."),
"4": ("Approval card content", "The approval surface shows effect class, irreversibility, diff against current state, and budget consumed. Prompt text and model rationale are recorded as non-evidential and are not shown as the thing being approved."),
"6": ("Key management and exit authority", "Per-subject evidence keys, witnessed destruction, and backup or replica deletion regimes. Stop-exit authority is not entry authority; restart uses dual control recorded on the evidence path."),
"7": ("Risk tiers and acceptance register", "Tier definitions (illustrative Borealis: T2 about 5,000 EUR irreversible exposure). Open unmediated paths are named risk acceptances with owners and review dates, not silent exceptions."),
"9": ("Promotion gates and policy-language bounds", "Hard evaluation gates with signed time-bounded overrides. Policy language evaluation is build-time bounded: no unbounded recursion or iteration on the hot path."),
}),
"B": ("Architecture decision records",
"The thirty-nine ADRs live as individual files under decisions/. This appendix indexes them and holds the C4 views.",
{
"0": ("Decision index", "See decisions/README.md and files ADR-01 through ADR-39. Each record is in Nygard form: context, decision, consequences, rejected alternatives, reopen trigger."),
"1": ("C4 views", "Context (level 1), container, and component views for the Borealis reference deployment. Section semantics follow arc42; view levels follow the C4 model. Edition 0.1 states the placement rule: views live here, not in the spine."),
"30": ("Unbuildable across the organisational boundary", "Claims that cannot be checked by the recipient without a live call into the issuer's TCB. Portable full envelopes, mutual mediation-coverage attestation as a hard gate, and shared risk scores without verification paths. Paired with ADR-30."),
}),
"C": ("Threat model and method",
"Threat set for a hostile model with real tools; method for regenerating threats when the set ages.",
{
"1": ("Primary adversary", "An attacker who can shape inputs the agent reads (documents, web, email, tool descriptions, memory) and who needs one successful instruction to act with the agent's held authority."),
"2": ("Method", "Derive threats from invariants I1 to I8. A threat that does not falsify an invariant is out of scope for this register. Refresh when a protocol, vendor, or regulation changes an assumption named in an ADR reopen trigger."),
}),
"D": ("Artefact schemas",
"Wire formats summarised. Edition 0.1 gives field inventories; JSON Schema files follow in a later cut.",
{
"1": ("Run credential", "Claims include sub (run), act (workload and principal), aud, cnf or proof-of-possession, envelope reference, expiry. The credential references the envelope; it does not embed derivation inputs."),
"2": ("Envelope, mandate, budget", "Envelope: operations allow-list, object scopes, derived_from, no widen field. Standing mandate: human, task class, ceiling, expiry. Budget: tool-call counter shared across a delegation tree."),
"3": ("Mediated tool call", "Agent-supplied name and arguments plus gateway-injected run id, envelope digest, budget remaining, and decision reference. Authority fields never originate on the agent side of the seam."),
"4": ("Approval binding", "Triple digests: frozen call, shown view, execution compare. Child delegation budget fields: shared counter; null fields that stay null by schema."),
"5": ("Evidence event and refusal", "Evidence event with effect_state, settled_by, content ciphertext reference. Refusal object with excluded_by naming which derivation input blocked the call. Foreign-attestation receipt is local evidence, not a foreign chain."),
"6": ("Manifest promotion block", "promotion.evaluation carries fail number, acceptor, and override expiry."),
"7": ("Memory item and degraded refusal", "Memory item: provenance, version, retention, purpose. Degraded-mode refusal carries posture, matrix version, and capability set for UI. Human system-of-record actions enter the same evidence chain without a run id."),
}),
"E": ("Worked examples",
"Compiled from spine worked moments (worked-moments.md). Edition 0.1 indexes the walkthroughs; full end-to-end traces follow.",
{
"1": ("Onboard a tool", "Registry promotion, publisher signature, conformance on push, side-effect class declaration. Compiles chapters 7 and 8."),
"2": ("Derive an envelope", "Intersection arithmetic for claims-triage under Marta's reach; unattended variant under standing mandate. Compiles chapters 5 and 6."),
"3": ("Graduate to unattended", "Standing mandate signing, gate measurement, bundle staleness. Compiles chapters 5, 9, and 12."),
"4": ("Work a suspected compromise", "Eleven-minute stop, chain verify, coverage gap. Compiles chapters 7, 11, and 14."),
}),
"F": ("Conformance and scorecard",
"Falsification tests for the three-part claim and invariants I1 to I8.",
{
"1": ("Claim tests", "C1 bound listed before run; C2 evidence reconstructs effects; C3 stop within stated time without agent help. Each has a pass/fail procedure."),
"2": ("I1 coverage measurement", "Mediated calls over discovered effect paths, dated, with discovery ownership separate from closure ownership."),
"3": ("Friction and attenuation depth", "If coverage falls, measure minutes of path friction before writing policy. Attenuation holds across delegation depth; depth and fan-out are bounded and measured."),
"4": ("Seam, approval, memory, evidence, manifest, bundle age", "No authority from the non-deterministic side; altered-post-approval refuse; external versus principal content distinguishable; evidence queue loss fails closed; declared need is manifest-sourced; stale bundles fail closed."),
"6": ("Stop-path cost", "Revocation check inside the stated p99 budget (illustrative 20 to 40 ms); drill-measured stop intervals for L1 to L5."),
}),
"G": ("Drills and calendar",
"Kill-switch drills, canaries, recertification. Owners and runbook references are required fields.",
{
"1": ("Operating calendar", "Quarterly stop drills, daily and hourly canaries above the reversibility line, model-deprecation job, bilateral credential expiry review. Each row: owner, runbook, last exercised, next due."),
"2": ("Inventories and canaries", "Endpoint configuration inventory; about 40 refusal canaries; memory provenance fraction; signed fail-posture matrix storage location for 03:00 reach."),
"3": ("Chain-break and revocation freshness", "Evidence-break runbook (stop batch, reconcile, human-owned output). Revocation channel freshness unknown means fail closed."),
"4": ("Manual path and composition telemetry", "Manual system-of-record emergency path on the drill calendar. Quarterly max observed delegation depth and fan-out versus configured limits."),
"5": ("Deprecation and counterparty expiry", "Vendor model-pin deprecation calendar as a named standing job. Counterparties with lapsed schedules versus audiences still accepting credentials."),
}),
"H": ("Glossary",
"Terms that the field uses in two senses; this document picks one and names the other.",
{
"1": ("Dual-sense terms", "Agent (workload versus natural person). Authority (envelope versus IAM role). Policy (allow-list derivation versus business rule text). Memory (governed store versus model weights). Gateway (mediation seam versus API management product)."),
}),
}
NUM = {"A":"1","B":"2","C":"3","D":"4","E":"5","F":"6","G":"7","H":"8"}

def slug(t):
    return re.sub(r"[^a-z0-9]+","-",t.lower()).strip("-")[:50]

APP.mkdir(exist_ok=True)
for old in APP.glob("*.md"):
    old.unlink()

index = ["# Appendices\n", "Edition 0.1 draft. Spine markers such as `[A-6.1]` resolve to the headings below.\n"]
for letter, (title, intro, sections) in DATA.items():
    n = NUM[letter]
    path = APP / f"{letter.lower()}-{slug(title)}.md"
    parts = [f"# Appendix {letter}. {title} {{#appendix-{letter.lower()}}}\n", intro + "\n"]
    for sec, (st, sb) in sections.items():
        hid = f"a-{n}-{sec}"
        marker = f"A-{n}.{sec}"
        parts.append(f"## {st} {{#{hid}}}\n\n{sb}\n")
    path.write_text("\n".join(parts), encoding="utf-8")
    index.append(f"- [Appendix {letter}. {title}]({path.name})")
(APP / "README.md").write_text("\n".join(index)+"\n", encoding="utf-8")
print("wrote", len(list(APP.glob('*.md'))), "appendix files")
# sample ids
print((APP/"a-control-register.md").read_text(encoding="utf-8").splitlines()[:8])
