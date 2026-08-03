#!/usr/bin/env python3
"""Rewrite all ADRs for answer-first clarity. No boilerplate templates."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEC = ROOT / "decisions"

# n: (title, chapters, plain, context, decision, rejected, why_reject, consequences, cost, reopen)
ADRS: dict[int, tuple] = {
    1: (
        "Containment over prevention-as-claim",
        ["1.1-introduction.md", "1.4-solution-strategy.md"],
        "Keep filters and prompts, but do not treat them as the safety claim. The claim is what still holds when the filter misses.",
        "After a claim-document injection, Borealis's review mixed two kinds of action: raise the classifier threshold and harden the prompt (frequency reducers), with nine items that actually bound what a fooled run can do. Listing both in the same â€œcontrolsâ€ column makes a miss rate the adversary chooses look like a design parameter the organisation chose.",
        "Prefer containment bounds the organisation sets over prevention rates an adversary selects. Keep detection; keep it out of the column that carries the safety claim.",
        "Put filter or prompt false-negative rate in the safety claim as if it were a controlled design parameter.",
        "A filter can be right most of the time and still fail once. The adversary chooses inputs and can adapt. A rate you do not control cannot be the thing you promise supervisors.",
        "Hygiene stays funded and honest under â€œreduces frequency.â€ The claim column only holds bounds you can test: envelope, mediation, evidence, stop. Assurance packs must not list classifiers beside containment as if they did the same job.",
        "Better prompts and thresholds are cheap. Measuring and maintaining coverage and enumeration is not. That maintenance is the price of a claim you can defend.",
        "Prevention shows a measured false-negative rate of zero against adaptive adversaries (not vendor marketing rates).",
    ),
    2: (
        "Run as unit of authority",
        ["1.3-context-and-scope.md", "1.4-solution-strategy.md"],
        "Authority, budget, evidence, and revocation attach to one run ID â€” not to the agentâ€™s standing identity forever.",
        "Asked about an agent, â€œwhat are we revoking?â€ and â€œhow much had it spent?â€ have answers of the form â€œit depends when you ask.â€ Asked about a run ID, each question has one durable answer.",
        "Make the run the unit of authority, budget, evidence, and revocation. Derive at start; expire with the run.",
        "Let the agentâ€™s service principal accumulate standing authority that every run inherits.",
        "A standing identity has no natural end, no per-task budget, and no single evidence chain. Revocation becomes ambiguous and blast radius grows with every new permission.",
        "Every mechanism later in the document can name one object. Incident review reconstructs one run. Unattended work still needs a principal story (see ADR-31), but the unit of effect remains the run.",
        "Run-start derivation and per-run credentials add a hop and an artefact. You pay that to make revocation and audit answerable.",
        "Long-running agents force a unit larger than a run without a security-parameter duration you can defend.",
    ),
    3: (
        "Frozen trusted computing base",
        ["1.3-context-and-scope.md"],
        "Only three things plus keys are trusted: gateway, decision path, evidence path. Everything else â€” model, agent, tools â€” sits outside.",
        "Every new â€œtrustedâ€ component is a place the claim can fail silently. Teams grow the trusted set whenever something is hard to mediate.",
        "Freeze the trusted computing base at the gateway, the decision path, the evidence path, and the key material beneath them. Refuse growth without reopening this record.",
        "Treat the model, framework, tools, or orchestration as part of the trusted computing base.",
        "Those components take attacker-shaped input or change without your version string. Putting them inside the TCB imports their failure modes into the claim.",
        "Later chapters may not add TCB members by stealth. If a design needs a fourth trusted component, it needs a new decision with an explicit cost.",
        "Some features become harder: anything that requires trusting model output for authority is out of scope by construction.",
        "A competent design review shows the TCB must grow and can still be defended.",
    ),
    4: (
        "Obligation-derived requirements",
        ["1.2-constraints.md"],
        "Write requirements from the legal or business obligation, not by mapping a vendor control catalogue.",
        "Catalogue mapping is fast and auditor-familiar. It also produces controls that satisfy a citation and stop nothing â€” with the gap marked closed.",
        "Derive every requirement from a named obligation. Never start from a vendor control catalogue.",
        "Map obligations onto a vendor catalogue for speed and familiar labels.",
        "You inherit someone elseâ€™s questions. The matrix looks complete while the mechanism may not exist.",
        "Appendix A rows carry an argument someone can contest. Design reviews take longer; audits get cheaper because the story is coherent.",
        "About two weeks of careful derivation versus two weeks of theatre that fails later. Pay upfront.",
        "A regulation is shown to require a named control product rather than evidence of an outcome.",
    ),
    5: (
        "Discrete risk tiers",
        ["1.2-constraints.md"],
        "Use a few named risk tiers. When a case sits between tiers, assign the higher one.",
        "Continuous scores invite negotiation at every boundary. Discrete tiers force an argument about which bucket â€” a better argument to have.",
        "Use discrete risk tiers; assign borderline cases upward.",
        "Use a continuous risk score as the primary scheme.",
        "Scores become bargained parameters. Reviewers argue decimals instead of consequences.",
        "Some agents carry heavier controls than their owners prefer. At Borealis roughly 15% landed one tier high. Watch bypass and coverage if over-control drives shortcuts.",
        "Expressiveness lost at the boundaries; clarity gained in governance.",
        "Supervisors expect continuous scores that discrete tiers cannot map.",
    ),
    6: (
        "Two identity chains joined per run",
        ["2.1-identity-and-binding.md"],
        "Keep â€œwho authorised this?â€ and â€œwhich workload is presenting?â€ as separate chains, joined once at run start.",
        "Collapsing both into one agent identity makes intersection arithmetic impossible and hides which human or mandate stands behind the run.",
        "Keep principal and workload chains distinct. Join them once per run in the credential.",
        "Collapse both questions into one agent identity.",
        "You can no longer tell whether authority came from a person (or mandate) or from a machine identity with broad reach.",
        "Credentials carry `sub` (run) and `act` (workload + principal). Envelope derivation reads both. Complexity rises; accountability rises with it.",
        "Issuer and broker must understand two chains. See ADR-08.",
        "Unattended operation outgrows the standing-mandate artefact (ADR-31).",
    ),
    7: (
        "Sender-constrained credentials",
        ["2.1-identity-and-binding.md"],
        "A stolen run token must not be usable from another machine. Bind the credential to the workloadâ€™s key.",
        "Bearer tokens stolen from agent or CI contexts can be replayed immediately. Short TTL alone does not stop same-second reuse.",
        "Require holder-of-key proof (sender constraint) for run credentials.",
        "Rely on short-lived bearer tokens alone.",
        "Theft-to-use can be faster than expiry. Without proof-of-possession, presentation anywhere succeeds.",
        "Every workload instance needs key material, rotation, and revocation. Mesh estates already have most of this; others buy an operations skill.",
        "Ongoing key-management cost for every runtime that holds a run credential.",
        "Bearer-only becomes unacceptable to every system of record in the estate â€” or proof-of-possession becomes universal free infrastructure.",
    ),
    8: (
        "Brokered token exchange",
        ["2.1-identity-and-binding.md"],
        "Mint and join run credentials in one broker, not as a separate grant from every toolâ€™s issuer.",
        "Direct per-tool grants avoid a new component but multiply grant count by agents Ã— tools and force every issuer to learn â€œrun.â€",
        "Broker and join run credentials in one place rather than issue direct per-tool grants.",
        "Issue direct per-tool grants from the existing identity provider for each tool.",
        "Revocation multiplies, join semantics diverge across issuers, and â€œwhat is a run?â€ leaks into n systems.",
        "One new component on the run-start path with its own fail posture (chapter 14). One place that understands run semantics.",
        "Broker availability and correctness become load-bearing. Price the fail posture before launch.",
        "The IdP gains first-class per-tool, audience-bound, run-aware grants that remove the broker.",
    ),
    9: (
        "Envelope as three-way intersection",
        ["2.2-the-envelope.md"],
        "A run may only do what the task needs AND the human can reach AND the risk tier allows - all three.",
        "Three parties decide what a run may do. The agent team declares need; the identity estate supplies the human's reach; risk supplies the tier ceiling. Need alone is self-grant. Reach alone inherits a human's whole working life. Ceiling alone permits the worst case.",
        "Derive the envelope as declared need AND principal reach AND tier ceiling at run start.",
        "Treat any single input as sufficient authority.",
        "Each alone recreates a familiar enterprise failure mode with a new blast radius.",
        "Three owners will disagree; that disagreement is the control. Derivation removes operations without a meeting.",
        "Manifests must declare need; identity and risk must supply the other two on time at run start.",
        "Production measurements show one input always dominates so the other two are decorative.",
    ),
    10: (
        "Attenuation by construction",
        ["2.2-the-envelope.md"],
        "There is no â€œwiden authorityâ€ operation. Child runs can only get less, never more.",
        "A policy rule â€œchild â‰¤ parentâ€ is reviewable and still violable by a bug. A widened envelope looks like a working system.",
        "Make envelope widening unrepresentable. The interface offers narrowing and revocation only.",
        "Enforce non-widening only as a policy-engine rule.",
        "Rules fail open into escalation. Absent operations fail into errors.",
        "Dynamic â€œjust give the child what it needsâ€ composition dies. Spawns go through derivation (ADR-29).",
        "Some product fantasies become unexpressible. That is intentional.",
        "A legitimate widening case cannot be expressed as a new run.",
    ),
    11: (
        "Allow-list of typed operations",
        ["2.2-the-envelope.md"],
        "Only named, registered operations may run. Everything else is refused.",
        "Deny-lists grow with fear and never finish. Failure mode is an effect. Allow-lists fail closed.",
        "Allow-list callable operations; refuse anything undeclared.",
        "Deny-list frightening operations and permit the rest by default.",
        "Completeness depends on enumerating adversary ideas while catalogues grow faster than reviews.",
        "New operations cannot ship the day they are written â€” they need registration and side-effect class (ADR-17). Chapter 17 is about making that friction small.",
        "Onboarding cost per operation; security gain on every unknown call.",
        "Untyped effect paths become dominant above the reversibility line.",
    ),
    12: (
        "Publish coverage as a dated ratio",
        ["1.4-solution-strategy.md", "2.3-complete-mediation.md"],
        "Publish what fraction of effect paths are mediated, with a date â€” not an adjective like â€œcomplete.â€",
        "First measurements are never 100%. Adjectives cannot be tracked quarter over quarter and get gamed when they become targets.",
        "Publish mediated-path coverage as a dated ratio. Separate discovery ownership from closure ownership.",
        "Assert complete mediation without a denominator.",
        "You cannot manage what you will not count. Gaming starts when one team owns both the numerator story and the discovery of gaps.",
        "Uncomfortable numbers appear in governance. That discomfort funds mediation work.",
        "Discovery function is standing cost. Publishing is political cost. Both are required.",
        "Discovery finds a path class mediation cannot cover without a different primitive.",
    ),
    13: (
        "Single mediation topology by default",
        ["2.3-complete-mediation.md"],
        "Prefer one mediation gateway topology. Federation relocates difficulty into policy freshness and double-counting.",
        "Multiple gateways feel organisationally natural. They create signed-bundle lag and coverage sums that disagree.",
        "Prefer a single mediation gateway topology. Treat federation as an expensive relocation of difficulty, not the default.",
        "Federated multi-gateway as the default shape.",
        "Staleness becomes a security parameter in many places at once; coverage becomes a reconciled sum with double-count risk.",
        "Latency and blast-radius arguments must be met with co-location and clear ownership, not with silent second gateways.",
        "Organisations that cannot share a gateway pay in policy distribution (chapter 13).",
        "Estate shape or protocol forces a different topology with measured benefit.",
    ),
    14: (
        "Protocol seam with authority in the gateway",
        ["2.4-the-seam.md"],
        "Speak the shared tool protocol at the seam, but keep credentials and authority decisions in the platform gateway - never in the agent.",
        "The gateway is a protocol server to the agent and a protocol client to real tools. It is the only component on the path that holds a credential. A proprietary calling convention buys semantics early and costs every integration. Waiting for the protocol to grow authority semantics waits on someone else's roadmap.",
        "Adopt the external tool protocol (e.g. MCP) as the seam. Keep authority in the gateway: translate, inject, refuse, forward.",
        "Proprietary internal calling convention - or wait until the protocol carries full authority semantics.",
        "Proprietary locks you in. Waiting leaves mediation unmeasurable until a date you do not own.",
        "Extra hop on every tool call; registry and pinning required (ADR-16). Agent never sees a credential.",
        "Single-digit milliseconds if co-located; worse if not. Additive to the decision path.",
        "Protocol gains native per-call authority the gateway can verify without re-deriving.",
    ),
    15: (
        "Server-originated content untrusted",
        ["2.4-the-seam.md"],
        "Tool descriptions, resources, and prompt templates are untrusted data with provenance â€” never a source of authority.",
        "Registered catalogue text feels like â€œour metadata.â€ It reaches the model like an instruction and has a supply chain behind it.",
        "Treat all server-originated content as untrusted data requiring provenance. Never derive authority from it.",
        "Trust registered tool descriptions as safe configuration.",
        "Description injection and malicious servers are demonstrated classes of attack. Trusting the text is trusting the attackerâ€™s channel.",
        "Onboarding records hashes; runs re-verify. Authority stays in envelope and policy.",
        "Provenance and pin discipline on every tool artefact.",
        "Protocol carries signed provenance for every server-originated payload as a required field.",
    ),
    16: (
        "Pinned signed registry, no runtime discovery",
        ["2.4-the-seam.md", "3.1-agent-manifest.md"],
        "Tools come from a signed internal registry at pinned versions. Runtime discovery of new servers is off.",
        "Runtime discovery lets the callable set change without a decision â€” an allow-list with the adversary on the write path.",
        "Remove runtime discovery. Pin-and-sign from an internal registry; pin agentâ†”tool bindings by digest.",
        "Discover tools at runtime from external registries; bind by mutable pointers.",
        "Pointers move under you. Digests do not.",
        "Developers lose the protocolâ€™s favourite convenience feature. Say so plainly. Promotion becomes a control.",
        "Registry, signing, and onboarding friction â€” priced against bypass in chapter 17.",
        "External registries offer pin-and-sign semantics the internal registry monopolises today.",
    ),
    17: (
        "Declared side-effect class",
        ["2.4-the-seam.md"],
        "A human declares whether an operation is reversible, irreversible, etc. Do not infer that from the name.",
        "`get-quote` that emails is a real failure mode. Names lie; declarations can be reviewed.",
        "Require a human-declared side-effect class (and idempotency where needed) for operations above the reversibility line.",
        "Infer side-effect class from operation names.",
        "Inference fails toward effects. The approval card and stop logic then lie.",
        "One minute of thought at onboarding becomes the cheapest control in the chain.",
        "Onboarding ceremony per operation.",
        "Protocol standardises side-effect class and idempotency on the call itself.",
    ),
    18: (
        "Approval bound to frozen call digest",
        ["2.5-approval-and-effect-integrity.md"],
        "Humans approve a frozen call artefact. Execution checks the digest. A regenerated call voids the approval.",
        "Approving a rendered summary and letting orchestration produce the call later makes â€œapprovedâ€ name a description, not bytes.",
        "Bind approval to a frozen call via digest comparison at execution.",
        "Approve a summary or UI view and allow the system to build the call afterwards.",
        "Seen-versus-done divergence becomes inexpressible eighteen months later.",
        "Approval UX must show the frozen artefact (effect class, irreversibility, diff, budget) â€” not the prompt or the modelâ€™s story about itself.",
        "Engineering for hash binding and UI that can display it.",
        "An approval UX that cannot display a frozen artefact becomes mandatory somewhere.",
    ),
    19: (
        "Failed gates fixed or removed",
        ["2.5-approval-and-effect-integrity.md"],
        "If a human gate fails its measurement (unread, rubber-stamped), fix it or remove it. Keeping a known-failing gate is not allowed.",
        "Organisations keep gates that look good in the register while clickers become the accountability sink.",
        "A gate that fails measurement is fixed or removed with tier demotion. There is no third option.",
        "Leave a failing gate in place because the control register looks stronger with it.",
        "Theatre relocates blame onto tired humans without reducing risk.",
        "Some actions move to tiers that do not require a human gate â€” honestly.",
        "Measurement instrumentation per gate; political cost when a gate is removed.",
        "Every remaining gate is unread for a quarter with no safe demotion path.",
    ),
    20: (
        "Entitlement-resolved retrieval",
        ["2.6-data-retrieval-memory.md"],
        "Search only what the principal may see. Do not retrieve-then-filter â€” filters leak via counts, ranks, and timing.",
        "Post-filters still score forbidden partitions. Side channels remain.",
        "Resolve entitlements inside retrieval against a partitioned index so unreachable items never score, count, or rank.",
        "Retrieve first, filter afterwards.",
        "Leakage is structural, not a bug in the filter expression.",
        "Index design and query planning get harder. Confidentiality gets real.",
        "Engineering cost in the retrieval path; worth it above sensitive tiers.",
        "A data owner requires retrieval under a non-principal identity the model cannot avoid.",
    ),
    21: (
        "Memory as governed primary store",
        ["2.6-data-retrieval-memory.md"],
        "Agent memory is a governed store with provenance, purpose, and retention â€” not an unmanaged vector â€œcache.â€",
        "Framework memory accumulates personal data with no ceremony and surfaces in subject-access requests.",
        "Treat agent memory as a governed primary store.",
        "Treat framework vector stores as droppable caches.",
        "Caches that hold personal data are primary stores whether you named them that or not.",
        "Write-time purpose checks (ADR-36); retention jobs; provenance fields.",
        "Platform ownership of memory lifecycle.",
        "Product value requires memory shared across principals in a way this model forbids.",
    ),
    22: (
        "Erasure by key destruction",
        ["2.7-evidence.md"],
        "Evidence content is encrypted per subject. Erasure destroys the key. The hash chain still verifies; content becomes unreadable.",
        "Tamper-evident logs fight erasure. Redacting bytes in place fights tamper-evidence.",
        "Split chained metadata from encrypted content. Erase by destroying the per-subject key.",
        "Redact in place, delete bytes only, or encrypt the entire chain as one blob.",
        "In-place redact breaks integrity stories; whole-chain encryption makes selective erasure clumsy or impossible.",
        "Key-management estate; witnessed destruction; backup/replica regimes in Appendix A.",
        "Real key-management cost â€” the price of both integrity and erasure.",
        "A supervisory interpretation rejects key destruction as erasure and the organisation must comply another way.",
    ),
    23: (
        "Fail closed on evidence",
        ["1.4-solution-strategy.md", "2.7-evidence.md", "3.3-failure-postures.md"],
        "If evidence cannot be written, refuse the effect â€” every tier, no busy-hour carve-out.",
        "Best-effort logging preserves availability and loses the claim for every unrecorded irreversible act.",
        "If evidence cannot write, no effects. Every tier. Every dependency.",
        "Best-effort logging or an availability exception for peak hours.",
        "An hour of unrecorded irreversible effects is not recoverable. A stopped queue is.",
        "Evidence-store availability becomes part of agent availability. Adversaries will notice. Accept that.",
        "Coupled availability; storage line item for high-volume agents.",
        "An availability regime forbids fail-closed on evidence and leadership accepts the residual.",
    ),
    24: (
        "Embedded policy evaluation",
        ["3.2-hot-path.md"],
        "Evaluate policy locally from signed, versioned bundles on the hot path â€” not a remote call on every tool call.",
        "Central synchronous decision adds network to p99 and correlates outage across every agent.",
        "Embed local policy evaluation from signed bundles with a declared staleness budget.",
        "Remote central decision service call on every call.",
        "Governance outage becomes estate outage; latency budget dies.",
        "Freshness becomes the security parameter. Stale bundles fail closed (see chapter 13).",
        "Bundle distribution and signing; local CPU on the enforcement path.",
        "Measured p99 of embedded evaluation exceeds a staleness budget a central call can meet.",
    ),
    25: (
        "Signed fail-posture matrix",
        ["1.4-solution-strategy.md", "3.3-failure-postures.md"],
        "Before launch, fill dependency Ã— tier with refuse/degrade/terminate â€” and get the consequence ownerâ€™s signature.",
        "Unsigned recommendations lose to a 03:00 phone call. Then posture is invented under pressure.",
        "Require a signed fail-posture matrix by the person who owns the business consequence, before launch.",
        "Leave posture as an unsigned platform recommendation to be decided on the incident bridge.",
        "Urgent defaults become permanent architecture without a decider.",
        "Some cells are uncomfortable (terminate run on model outage). That discomfort belongs before launch.",
        "Meeting time with business owners; matrix storage reachable at 03:00.",
        "A dependency appears for which no declared fail posture is honest.",
    ),
    26: (
        "Five stop mechanisms",
        ["3.4-stopping-it.md"],
        "Design five different stops (halt run, revoke authority, disable operation, quarantine version, cut egress). One â€œkill switchâ€ is not enough.",
        "Singular kill switches are either too narrow or so wide they take the business offline with the adversary.",
        "Design five distinct stop mechanisms. If underfunded, build the two widest and leave the residual visible.",
        "Treat a single kill switch as sufficient architecture.",
        "The stop you need at 03:00 depends on what you just learned. One reach profile cannot cover five situations.",
        "Build, own, and drill five paths. Underfund honestly rather than pretend.",
        "Engineering and drill calendar cost â€” non-optional for the claimâ€™s third leg.",
        "An incident requires a sixth distinct stop the five did not cover.",
    ),
    27: (
        "Unexercised controls are absent",
        ["1.4-solution-strategy.md", "3.4-stopping-it.md", "3.5-decay.md"],
        "If a stop or control has not been exercised against a live run this quarter, treat it as absent.",
        "Unlike database failover, agent stops have no organic exercise. Undrilled switches have never run.",
        "A control unexercised against a live run in a quarter is absent. The drill calendar is load-bearing architecture.",
        "Treat drills as optional SRE hygiene demoted out of architecture.",
        "First execution during the real incident is training under fire with production stakes.",
        "Quarterly drills with owners and measured intervals (Appendix G).",
        "Calendar time and incident-like inconvenience â€” cheaper than fiction.",
        "An auditor rejects exercised-set evidence and requires an alternative you must meet.",
    ),
    28: (
        "Paved road as product",
        ["3.6-the-paved-road.md"],
        "Own the sanctioned path as a product measured in adoption (days of friction), not as a project that ends with the last ticket.",
        "Projects die; estates change weekly. Nobody owns the duration metric that predicts bypass.",
        "Own the paved road as a product with an adoption objective.",
        "Fund a time-boxed security project and declare victory at closure.",
        "Coverage falls after the project ends and gets blamed on culture.",
        "A named owner, backlog from road users, published friction targets.",
        "Standing product funding â€” the price of used controls.",
        "The paved road loses adoption for a quarter despite funded ownership.",
    ),
    29: (
        "Derived child envelopes",
        ["4.1-composition.md"],
        "Sub-agents get their own attenuated envelope. Do not pass the parentâ€™s credentials or approvals.",
        "Framework default is to hand the child the parentâ€™s client. Under hostile input that is widening with extra steps.",
        "Derive attenuated child envelopes from the parent envelope and the manifestâ€™s delegation graph. Do not propagate parent credentials or approvals.",
        "Pass parent authority and approval to spawned sub-agents.",
        "Child calls become indistinguishable from parent calls with full reach.",
        "Dynamic free-form composition dies; static delegation graphs live. Shared budget counters across the tree.",
        "Less â€œmagicâ€ composition; more predictable blast radius.",
        "Dynamic sub-agent composition becomes mandatory and a static graph cannot express it.",
    ),
    30: (
        "No shared cross-org policy domain",
        ["4.2-across-the-boundary.md"],
        "Across organisations, use bilateral checkable claims â€” not one shared policy domain or shared broker TCB.",
        "Shared domains make Parts IIâ€“III easy and concentrate secrets and shared incident appetite you may not want.",
        "Keep the organisational boundary. Use verifiable credentials, checkable claims, and contracts. List what remains unbuildable.",
        "Dissolve into one policy domain or a federated broker both sides trust with full envelope semantics.",
        "You inherit another organisationâ€™s failure modes and politics.",
        "Narrower claims; visible unbuildable list (Appendix B). Honesty over portable fantasy.",
        "Contract and credential operations cost; less engineering fantasy cost.",
        "A counterparty demands a shared policy domain this model cannot satisfy.",
    ),
    31: (
        "Standing mandate for unattended runs",
        ["2.1-identity-and-binding.md"],
        "Overnight runs resolve the principal chain to a signed standing mandate (who, task class, ceiling, expiry) â€” not to a naked service account.",
        "Service identities have no human entitlements story. Team queues have no recognisable principal.",
        "Unattended principal chain resolves to a signed standing mandate.",
        "Fall back to a service identity or an undifferentiated team queue.",
        "Intersection with reach becomes fiction; accountability dissolves.",
        "Mandate is an upper bound; attenuation still applies. Expiry and recertification required.",
        "Mandate lifecycle operations.",
        "Unattended work outgrows what a mandate can honestly express.",
    ),
    32: (
        "Recertify ceiling, need, and exercised set",
        ["3.5-decay.md"],
        "Each quarter, recertify what was allowed and compare it to what was actually used.",
        "Static entitlement lists alone rot into fiction. Over-declaration becomes permanent authority.",
        "Recertify tier ceiling and declared need together with the platformâ€™s exercised-set report.",
        "Recertify only static entitlements and ignore what ran.",
        "Intersection becomes a constant nobody revisits.",
        "Data owners see unused reach and can shrink need. Platform must produce the exercised set from evidence.",
        "Quarterly ceremony time â€” funded from ADR-27â€™s calendar.",
        "An auditor rejects exercised-set recertification and requires another form.",
    ),
    33: (
        "No break-glass agent derivation",
        ["3.3-failure-postures.md", "3.4-stopping-it.md"],
        "Emergencies are humans acting on the system of record with their own credentials â€” never a widened agent run.",
        "Emergency mandates are the most attractive seldom-exercised high-authority objects you can build.",
        "No break-glass agent derivation. Emergency path is human-direct on the system of record, recorded in evidence.",
        "Issue an emergency mandate or widened envelope for the agent under dual control.",
        "The break-glass path becomes the incident, eventually.",
        "Manual path must be drilled (screens change). No agent shortcut.",
        "Human on-call competence and drilled SoR procedures.",
        "A class of incident cannot be contained without an agent-held emergency path.",
    ),
    34: (
        "Temporary deny-only fast path",
        ["3.2-hot-path.md"],
        "Incidents may push a temporary deny list with hard expiry. Never a fast permit path.",
        "Fast permits bypass review. Permanent incident narrowing without review becomes shadow policy.",
        "Allow a temporary deny-only incident path with hard expiry; never a permit-fast path.",
        "Add a fast permit path, or make incident narrowing permanent without the ordinary bundle path.",
        "Permit-fast is how authority leaks. Permanent bypass is how policy forks.",
        "Second policy channel with clear precedence and expiry. Worst case is self-inflicted refusal.",
        "Operational complexity of two channels â€” bounded by expiry.",
        "Incident response requires permanent narrowing that cannot wait for the ordinary path.",
    ),
    35: (
        "Asymmetric in-flight policy",
        ["2.2-the-envelope.md"],
        "If policy narrows mid-run, the next call sees it. If policy widens, the current run keeps its birth ceiling.",
        "An envelope that tracks live policy in both directions is a cache with staleness, not a ceiling.",
        "Narrowing mid-run takes effect on the next call. Widening applies only to the next derivation.",
        "Let the envelope track live policy upward and downward.",
        "Upward tracking destroys the meaning of a ceiling derived at start.",
        "Runs in flight may finish under a withdrawn ceiling for at most max-run-duration. Revoke if that window is too long.",
        "Max run duration becomes a security parameter.",
        "A legitimate mid-run ceiling raise cannot wait for a new run.",
    ),
    36: (
        "Purpose check on memory write",
        ["2.6-data-retrieval-memory.md"],
        "Block forbidden combinations when memory is written â€” not later when someone reads it.",
        "Read-time checks miss what already became a stored fact.",
        "Run purpose and composition checks on the memory write path for cross-context items.",
        "Catch forbidden composites only at read or audit time.",
        "Once stored, the composite is a durable leak and a GDPR purpose problem.",
        "Write path gets stricter; some â€œcleverâ€ memory features die.",
        "Enforcement cost on writes.",
        "Product value requires write-time combinations the purpose model cannot express.",
    ),
    37: (
        "Separate artefacts bound by manifest",
        ["3.1-agent-manifest.md"],
        "Instructions, policy, and tools stay separately owned. A signed manifest binds the versions that may run together.",
        "Monorepo atomic deploy is stronger on join integrity and forces specialists into pipelines they will bypass with shadow text.",
        "Keep owned artefacts separate; bind them with a signed manifest.",
        "Force instructions, policy, and tool bindings into one atomic repository deploy unit.",
        "Shadow instructions appear when claims people cannot reach the only pipeline.",
        "Manifest is the security object. Promotion gates apply to the binding.",
        "Join complexity; human-reachable ownership.",
        "A deployment model that cannot join separately owned artefacts becomes mandatory.",
    ),
    38: (
        "Pinned model set per tier",
        ["3.1-agent-manifest.md"],
        "The manifest lists which models may run for this tier. Auto-routing to a cheaper or other-region model is a safety-case change.",
        "Routers change refusal profile and residency without touching the envelope.",
        "Pin the allowed model set per tier in the manifest. Treat routing and fallback as a safety-case change.",
        "Allow unreviewed automatic per-call model routing under load, price, or latency.",
        "Different model, different residual. Silently.",
        "Deprecation calendars become standing jobs. Fallbacks need review.",
        "Less automatic cost optimisation; more honest evaluation.",
        "Vendor platforms make pinned sets impossible while still meeting residency obligations.",
    ),
    39: (
        "Context hash above reversibility line",
        ["2.7-evidence.md"],
        "For irreversible effects, evidence includes a hash of the assembled context. Below that line, references can suffice.",
        "Always storing full context is expensive. Never committing context makes reconstruction theatre.",
        "Require a content hash of the full assembled context above the reversibility line; references suffice below.",
        "Always store full context, or never commit context content.",
        "All-or-nothing misses the reversibility distinction the rest of the design uses.",
        "Canonical serialisation ownership required so hashes are stable.",
        "Storage and CPU for hashing above the line.",
        "Reconstruction obligations require full context retention beyond hashing.",
    ),
}


def slug(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]


def render(n: int, meta: tuple) -> str:
    title, chapters, plain, context, decision, rejected, why, consequences, cost, reopen = meta
    sid = f"ADR-{n:02d}"
    ch = ", ".join(f"`chapters/{c}`" for c in chapters)
    return f"""# {sid}. {title} {{#{sid.lower()}}}

**Status:** Accepted (edition 0.2.0 draft)  
**Date:** 2026-08-01  
**Deciders:** Lead author (Timotheos Samartzidis)  
**Argued in:** {ch}

**In plain terms:** {plain}

## Context

{context}

## Decision

{decision}

## Why not the alternative

**Rejected:** {rejected}

{why}

## What changes if you follow this

{consequences}

## Cost

{cost}

## Reopen when

{reopen}
"""


def main() -> None:
    DEC.mkdir(exist_ok=True)
    # Remove old ADR files to avoid orphans with stale slugs
    for old in DEC.glob("ADR-*.md"):
        old.unlink()
    index = [
        "# Architecture decision records\n",
        "Nygard-form records for edition 0.2.0. Each opens with **In plain terms** so a cold reader gets the point before the apparatus.\n",
        "| ID | Title | File |",
        "|---|---|---|",
    ]
    for n in range(1, 40):
        meta = ADRS[n]
        title = meta[0]
        fname = f"ADR-{n:02d}-{slug(title)}.md"
        (DEC / fname).write_text(render(n, meta), encoding="utf-8")
        index.append(f"| ADR-{n:02d} | {title} | [{fname}]({fname}) |")
    (DEC / "README.md").write_text("\n".join(index) + "\n", encoding="utf-8")
    # Sanity: no boilerplate left
    left = 0
    for p in DEC.glob("ADR-*.md"):
        t = p.read_text(encoding="utf-8")
        if "competent architect reaches" in t or "Priced in the arguing chapter" in t:
            left += 1
            print("STILL BAD", p.name)
    print("wrote 39 ADRs; boilerplate remaining", left)


if __name__ == "__main__":
    main()

