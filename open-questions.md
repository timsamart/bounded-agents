<!--
Subject-matter questions whose answers change the architecture, as distinct
from the editorial queries held in the chapter cards of outline.md.

A question belongs here if answering it differently would change a mechanism,
an invariant, a decision record or the chapter list. A question belongs in a
chapter card if answering it differently would only change a paragraph.

Referenced from outline.md and from drafts as [OQ-nn]. Per CONV-007 the
marker is deletable: no sentence in a draft may depend on it for sense.
-->

# Open Questions – Subject Matter

- **Project:** Governed Agentic Infrastructure *(working title)*
- **Linked artifacts:** `manifesto.md`, `concept.md`, `toc.md`, `outline.md`, `conventions.md`, `worked-moments.md`
- **Opened:** 2026-07-31
- **Status of the register:** resolved v0.2 – 2026-07-31. Thirty-one questions, positions chosen, propagated to `outline.md`, `worked-moments.md`, and `toc.md`.

## What this file is for

The outline currently contains twenty chapters, thirty decision records and seven invariants, and it reads as though the mechanism set were closed. It is not. This register holds the questions the architecture has not answered, separated from the questions the manuscript has not answered, because the two decay at different rates and are resolved by different work. An editorial query is settled by an author deciding. A subject-matter question is settled by evidence, by a design derivation, or by an admission that the field has no answer – and the third outcome is a legitimate result here, provided it is stated where a reader will find it rather than left as a silence.

Three of these questions are load-bearing enough that the document is currently wrong without them, not merely incomplete. They are marked `[BLOCKING]`. The rest are marked `[OPEN]` where no defensible position exists yet, `[POSITION]` where a position exists and has not been argued or tested against its strongest objection, and `[SCOPE]` where the honest first move is to decide whether the subject belongs in the document at all.

## The card

Each question carries six fields, deliberately short. A card that needs more than a screen is two questions.

| Field | What it holds |
|---|---|
| **Question** | One sentence, answerable, and phrased so that two competent architects could disagree about it |
| **Status and reach** | Flag, plus the chapters and decision records the answer moves |
| **Why it is open** | What the outline currently says and precisely where it stops |
| **Boundary rule** | The verdict under `manifesto.md` §4: does a hostile model change the answer? A question that fails this test is cited, not explained, and the card says so |
| **Positions** | The candidate answers, each stated at its strongest, because a position with no rival is a preference |
| **What would settle it** | Evidence, a derivation, an ADR, or an admission – named, so the work is schedulable |

---

# Cluster A. Identity, and the principal the model assumes exists

The two-chain model `[ADR-06]` binds a workload identity to a human principal at run start, and almost everything downstream – entitlement-scoped retrieval `[ADR-20]`, the envelope intersection `[ADR-09]`, the approval record – reads the second chain. The cluster below is what happens when that chain is absent, when it is machine-shaped, or when the enterprise already owns a control plane that claims the same job.

## OQ-01 · Unattended runs have no human principal

**Question.** When a run starts on a schedule, on an inbound event or at the end of another system's workflow, what occupies the human chain, and under whose entitlements does that run retrieve and act?

**Status and reach.** `[BLOCKING]` · ch. 3, 5, 6, 10, 19 · `[ADR-06]`, `[ADR-09]`, `[ADR-20]`

**Why it is open.** The introduction's intersection test names unattended operation as one of the three conditions that justify building any of this, and chapter 19 repeats it. So the case the document exists for is the case its identity model handles worst: there is no human at run start, and every mechanism that reads the second chain either fails or silently falls back to a service identity, which is the arrangement chapter 5 was written to abolish. The outline never states this and no card mentions it.

**Boundary rule.** Passes decisively. With a benign model the fallback to a service identity is a mild audit inconvenience. With a hostile one it is the whole blast radius, because the agent now acts under the union of everything the service account can reach.

**Positions.**
- **A standing mandate.** A human signs a durable delegation artefact – a principal, a task class, a ceiling, an expiry – and the unattended run derives its envelope against that artefact rather than against a live human. Attenuation is preserved because the mandate is itself an upper bound. The cost is a new artefact class, a new expiry to watch, and an approval that is one step further from the action than anyone would like.
- **An organisational principal.** The second chain resolves to a team or a queue rather than a person, and accountability is held at that level. Honest about how enterprises actually work, and it destroys entitlement-scoped retrieval, because a queue has no entitlements a data owner would recognise.
- **Refusal.** Unattended operation caps the tier. An agent with no human principal is not permitted operations above the reversibility line, regardless of what the mandate says. Clean, defensible, and it disqualifies a large fraction of the deployments the reader wants to build – which the document is allowed to do, but not by accident.

**What would settle it.** A derivation, in chapter 5 or a section of it, plus a decision record. The mandate artefact needs a schema in Appendix D if position one survives. Test the result against the case that decides it: the 03:00 batch that finds a claim requiring a payment adjustment.

## OQ-02 · Non-human identity lifecycle, and authority that is not enumerable at rest

**Question.** Who owns an agent identity, what recertifies it, and what does an identity governance tool report when asked what an agent has access to – given that the answer is derived per run and does not exist between runs?

**Status and reach.** `[BLOCKING]` · ch. 5, 6, 15 · `[ADR-09]`, `[ADR-27]`, Appendix A

**Why it is open.** The document issues run credentials beautifully and never says where agent identities come from, who is accountable for one, what happens when that person leaves, or how an orphaned agent identity is detected. Worse, the architecture deliberately makes the standard identity governance question unanswerable: an entitlement review asks what an account can reach, and the envelope model's whole contribution is that the answer is nothing until a run derives it. Every access recertification process in a regulated enterprise is built on the assumption that authority is a static attribute of an identity. This design breaks that assumption on purpose, and the document currently does not notice.

**Boundary rule.** Passes, but only on one half. Ownership and joiner-mover-leaver hygiene for non-human identities is ordinary practice and is cited, not explained. The un-enumerable entitlement is specific to this architecture and has to be derived, because it is the point at which the design collides with an existing, mandatory, audited process.

**Positions.**
- **Report the ceiling.** Recertification reviews the tier ceiling and the declared need, which are static, rather than the derived envelope, which is not. Reviewers see an upper bound they can reason about. The risk is that the ceiling becomes the thing everyone optimises and the intersection quietly becomes a constant, which is already chapter 6's decay question.
- **Report the exercised set.** Recertification reviews what was actually used last quarter, which is a stronger statement than any entitlement list and is only possible because chapter 11 exists. It also inverts the process every access-governance tool implements, so it is a build rather than an integration.
- **Both, with different owners.** The ceiling is recertified by the data owner and the exercised set by the platform. Plausible, and it doubles the recertification load that chapter 15 already prices.

**What would settle it.** A decision record, and one honest paragraph in chapter 15 about what an identity governance platform can and cannot be told. Position two is the interesting one and it needs the evidence schema to support the query, which is a requirement on chapter 11 that is not currently there.

## OQ-03 · Privileged access management is already in the building

**Question.** Is the gateway a new privileged access management estate for a new principal class, an integration with the one the organisation already runs, or a deliberate replacement – and does just-in-time elevation have any representation at all in an attenuation-only model?

**Status and reach.** `[OPEN]` · ch. 5, 6, 7, 16 · `[ADR-08]`, `[ADR-10]`, `[ADR-13]`

**Why it is open.** Every regulated enterprise in the target audience already operates vaulting, session brokering, session recording, approval workflows and time-bound elevation. The document proposes a broker and a gateway that do structurally the same job – mediate access, hold the credential, record the session, bound the authority – for a principal class the incumbent product was not designed for. The outline mentions none of this, which means the first design review will produce the question *why is this not our existing privileged access platform*, and the document has no answer prepared. Separately, the core motion of privileged identity management is temporary elevation, and chapter 6 makes widening unrepresentable. That is a real and defensible collision, and stating it deliberately is very different from discovering it in someone's architecture board.

**Boundary rule.** Passes on the elevation question, because a hostile model makes a time-bound elevation into a fully usable window. Fails, mostly, on vaulting and session recording, which are ordinary controls that apply unchanged and should be cited as such.

**Positions.**
- **Integration.** The broker fronts the incumbent vault and the gateway emits sessions the existing platform can record. Politically cheap, and it inherits a product designed around interactive human sessions, which run credentials are not.
- **Distinct estate, explicitly.** Agent authority is derived, not checked out, and the document says plainly that the incumbent product answers a different question. Honest, expensive, and it makes an enemy of a team with a budget.
- **Elevation as a new run.** The chapter 6 answer, generalised: an agent never elevates. It ends, and a new run is derived with a new envelope and a human in the derivation. This is already the position the document implies and it has never been argued against the strongest version of its rival.

**What would settle it.** A decision record on elevation, written to be read by someone who owns the privileged access platform, plus one paragraph in chapter 16 on what integrates and what does not. Also worth a row in the constraint inventory of chapter 2, since for most readers the incumbent estate is an imposed constraint rather than a choice.

## OQ-04 · The gateway becomes the richest secret in the estate

**Question.** If the agent never holds a credential, the gateway holds all of them – so what is the gateway's own key custody, compromise posture and blast radius, and is that a better position than the one it replaced?

**Status and reach.** `[OPEN]` · ch. 7, 8, 20 · `[ADR-14]`

**Why it is open.** `[ADR-14]` moves every downstream credential behind one component, and chapter 20 disposes of the consequence in a single line about control-plane compromise offering nothing beyond what any control-plane compromise offers. That is true and insufficient. Concentration is a design choice with a stated benefit, and the document prices the benefit and not the concentration. A reader who has run a secrets platform will ask whether the gateway holds long-lived material at all, or brokers short-lived material it cannot replay, and the answer changes the residual chapter materially.

**Boundary rule.** Passes indirectly. The model is the reason the credential was moved; the concentration is the price, and pricing a control is a manifesto obligation.

**Positions.**
- **Broker only.** The gateway holds no long-lived secret and exchanges evidence of the run for a short-lived, audience-bound downstream credential. Requires every system of record to support exchange, which most legacy estates do not.
- **Custodian, with hardware backing.** The gateway holds material in a hardware security module with per-tool separation, and the compromise story is the module's. Buildable today and the honest answer for legacy tools.
- **Hybrid, declared per tool.** Realistic, and it means the coverage number of chapter 7 acquires a second dimension nobody wants to publish.

**What would settle it.** A derivation in chapter 8 and an itemised entry in chapter 20's residual. This is one of the few places where the document currently understates its own risk.

## OQ-05 · Break-glass has no representation

**Question.** What happens when a human needs an agent to do something outside its envelope, immediately, during an incident – and if the architecture has no answer, what does the organisation build instead?

**Status and reach.** `[POSITION]` · ch. 6, 13, 14

**Why it is open.** Chapter 13 decides fail postures and chapter 14 decides how to stop things. Nothing decides how to go faster under emergency, and every enterprise has that procedure. An architecture that does not represent break-glass does not prevent it; it exports it, and the exported version is a long-lived token in a vault with a four-eyes procedure nobody has drilled. Chapter 15's argument about decay applies here with unusual force.

**Boundary rule.** Passes. Break-glass is the case where the human is under pressure and the model is the fastest thing in the room, which is exactly the confluence the document is about.

**Positions.**
- **There is no agent break-glass.** The emergency path is a human acting directly against the system of record, and the platform's obligation is that this path exists, is as fast as the agent path, and is recorded. This is almost certainly right and it has a cost the document has not stated: the manual path has to be maintained and exercised, which is another row on the drill calendar.
- **A break-glass run.** A run derived under an emergency mandate with a hard expiry, two human signatures and a mandatory review. Attenuation survives because the mandate is bounded. It also creates a legitimate high-authority derivation path, which is precisely what an adversary would like to reach.

**What would settle it.** A decision record and a drill in Appendix G. If the answer is position one, chapter 14 gains a short beat, because *what no switch can undo* and *what no envelope permits* are the same conversation from opposite ends.

---

# Cluster B. Policy as code, treated as software rather than configuration

Chapter 12 decides how policy is evaluated and distributed. Nothing decides how it is written, reviewed, tested, versioned, or reconciled with the envelope – which is the second authority representation in the same system.

## OQ-06 · The policy bundle is a deployable artefact with no stated lifecycle

**Question.** Who authors a policy bundle, who reviews it, what tests gate it, how is it rolled back, and does a policy change carry the same change control as a code change?

**Status and reach.** `[OPEN]` · ch. 12, 16 · `[ADR-24]`, Appendix A

**Why it is open.** A signed bundle distributed to every enforcement point has a larger blast radius than most application releases and the outline treats it as an input. The tension is sharp and unresolved. Full change control means the fastest way to widen authority during an incident is slower than the incident. No change control means there is an unreviewed path to widening authority, which defeats the whole apparatus more cheaply than any attack in the threat model.

**Boundary rule.** Passes. The bundle is the object that decides what a hostile model may do, and its supply chain is therefore in scope on the same argument that puts tool manifests in scope in chapter 8.

**Positions.**
- **Symmetric with code.** Same review, same pipeline, same rollback. Predictable, and it makes emergency narrowing slow, which is the wrong direction to be slow in.
- **Asymmetric by direction.** Narrowing deploys fast with one signature; widening takes the full path. Attractive, and it requires the pipeline to determine reliably whether a change narrows, which for a non-trivial policy language is not decidable in general and is the reason this is a question rather than an answer.
- **Two artefacts.** A slow-moving bundle and a fast-moving deny list with its own signing authority and a mandatory expiry. Operationally honest, and it is a second policy system with everything that implies.

**What would settle it.** A decision record, and a derivation of whether narrowing is mechanically detectable in the chosen policy language – which, usefully, constrains the choice of language.

## OQ-07 · Conflict, totality and the hot path

**Question.** When two policy sources disagree, what resolves them, and is the policy language total – that is, does every evaluation terminate within the latency budget by construction rather than by testing?

**Status and reach.** `[OPEN]` · ch. 12, 13 · `[ADR-24]`

**Why it is open.** Chapter 6 states that three owners disagreeing is the mechanism working, which is true at derivation time and says nothing about evaluation time. Deny-overrides is the obvious resolution and it has a failure mode the document should name: it makes every policy author able to break production alone, which changes who is willing to author policy. Termination is the less obvious half. A policy evaluation that can loop or backtrack unboundedly is a denial of service on the decision path, reachable by whoever controls the inputs, and the mitigation is a language property rather than a timeout.

**Boundary rule.** Passes on termination, because the input to the decision is partly attacker-shaped. The conflict question passes only weakly and could reasonably be handled in an appendix.

**Positions.** Deny-overrides with an explicit precedence order for the exceptional case, against a single composed bundle with conflicts detected at build time. The second is stronger and requires the build to be able to detect them, which returns to the language choice in OQ-06.

**What would settle it.** A short section in chapter 12 and a requirement in Appendix A that the evaluation is bounded. One paragraph, high value, currently absent.

## OQ-08 · Policy coverage, dead rules and the tests nobody wrote

**Question.** How is a policy bundle tested, what does coverage mean for a rule set, and what happens to a rule that has not fired in a year?

**Status and reach.** `[POSITION]` · ch. 12, 15

**Why it is open.** Chapter 15 gives every control a canary and gives policy itself nothing. An unreachable rule is dead code with an audit trail, and a rule that fires on every request is either load-bearing or vestigial and nobody can tell which without measurement. This is a small addition with a large effect on the decay chapter's credibility, because policy is the control most likely to rot invisibly.

**Boundary rule.** Passes weakly. It is ordinary software hygiene applied to an unusual artefact, and its inclusion is justified by chapter 15's thesis rather than by the boundary rule.

**Positions.** Rule-level firing telemetry with a quarterly review of the never-fired and the always-fired, against a test suite with required coverage at build time. They are complementary and the question is only which one the document requires.

**What would settle it.** Two rows in chapter 15's decay catalogue and a paragraph in chapter 12. No new chapter.

## OQ-09 · The envelope and the policy engine are two representations of one thing

**Question.** Is the envelope a cached, materialised result of a policy evaluation, or an independent object that policy is evaluated against – and if it is the former, what is its staleness budget?

**Status and reach.** `[BLOCKING]` · ch. 6, 12 · `[ADR-09]`, `[ADR-24]`

**Why it is open.** This is the seam a hostile reviewer will find fastest. Chapter 6 derives authority as a data object at run start. Chapter 12 evaluates a decision function per call against distributed policy. If policy changes mid-run, does the envelope change? If it does, the envelope is a cache and chapter 12's staleness table needs a row for it, and chapter 6's claim that authority is fixed at derivation is wrong. If it does not, the platform is knowingly enforcing withdrawn policy for the length of a run, which is defensible only if the run is short and is never stated as a bound. The two chapters currently do not know about each other.

**Boundary rule.** Passes. The gap between derived and enforced authority is a window, and windows are the document's subject.

**Positions.**
- **Envelope as derived cache with a bounded run length.** Coherent, and it makes maximum run duration a security parameter rather than an operational one – which connects to OQ-30 and to the streaming question already in chapter 3's card.
- **Envelope as an upper bound, policy as a per-call check inside it.** Also coherent, arguably stronger, and it means the envelope is a ceiling rather than an authority. That is a different chapter 6 from the one currently outlined.

**What would settle it.** A derivation that has to happen before either chapter can be drafted. This is the single most structurally important question in the register.

---

# Cluster C. The seam, and what happens when the protocol is asked to be the security layer

Chapter 8 is the strongest card in the outline and it is written against a version of the protocol that no longer describes the whole surface. The questions below are the ones that decide whether the chapter's thesis – that the seam is a one-way transition from non-deterministic to deterministic compute – actually holds.

## OQ-10 · Sampling and elicitation reverse the direction of the seam

**Question.** What happens to the seam's thesis when the protocol lets a server initiate a model completion through the client, or ask the human principal a question directly?

**Status and reach.** `[BLOCKING]` · ch. 8, 9, 10 · `[ADR-14]`, `[ADR-15]`

**Why it is open.** Chapter 8 argues that the only governable moment is the transition from guessing to executing, and that the transition runs one way. Two capabilities in the protocol run the other way. Server-initiated sampling lets the far side of the seam cause inference to happen with content it supplies, which makes a tool server an injection source with a return path rather than a passive callee. Elicitation lets a server put text in front of the human principal, which turns the approval surface of chapter 9 into a channel a third-party server can address. The card mentions neither, and the six-property wish list is incomplete without them.

**Boundary rule.** Passes at the highest weight in the register. These are the mechanisms by which the deterministic side stops being deterministic.

**Positions.**
- **The gateway does not forward them.** Sampling and elicitation are terminated at the gateway and never reach the model or the human. Simple, enforceable, and it removes capabilities that some legitimate tools are built on.
- **Forwarded under a declared capability.** A server may sample or elicit only if its pinned manifest declares it, the content is marked as untrusted at the quarantine level of chapter 10, and elicited text is rendered in a surface that cannot be mistaken for the platform's own. More useful, considerably more machinery, and it puts a trust decision on the manifest supply chain.
- **Elicitation never, sampling under declaration.** Probably the answer, because the human-facing channel is the one where impersonation is cheapest and hardest to detect.

**What would settle it.** Pin the protocol revision, read the capability negotiation, and derive. This changes chapter 8's beats and adds a paragraph to chapter 9. `[PENDING: pin the revision that carries sampling and elicitation, with a retrieval date]`

## OQ-11 · Resources and prompt templates are unclassified surface

**Question.** Do the protocol's non-tool payloads – resources and server-supplied prompt templates – carry the same provenance, pinning and side-effect obligations as tool descriptions, and if not, why not?

**Status and reach.** `[POSITION]` · ch. 8, 10 · `[ADR-15]`, `[ADR-17]`

**Why it is open.** The card treats tool descriptions as untrusted data with provenance, which is right, and stops there. Resources are content a server hands the client to place in context, and prompt templates are instructions a server hands the client to send to the model. Both reach the model with the same directness as a description and neither has a side-effect class, because neither has an effect – which is the point: they change what the model does without ever appearing at the seam.

**Boundary rule.** Passes. This is the metadata channel argument extended to the payload channel.

**Positions.** Extend `[ADR-15]` to cover every server-originated payload, against a separate record for content that enters context. The first is cleaner and makes the existing record stronger.

**What would settle it.** One beat in chapter 8, and a check that chapter 10's quarantine tier is the same mechanism – because it should be, and if it is, the two chapters are describing one control from two sides.

## OQ-12 · The agent runtime is also a protocol client

**Question.** When the vendor runtime, the desktop application or the developer's editor speaks the protocol natively and holds its own connector configuration, is controlling that configuration in scope – and if so, which chapter owns a control that is enforced by device management?

**Status and reach.** `[SCOPE]` · ch. 7, 8, 16

**Why it is open.** Chapter 7 measures coverage against discovered paths and itemises how paths escape, and the list is a 2024 list: sidecars, laptops with production credentials, legacy service accounts. The path that escapes today is a developer adding a connector to a runtime that already has a credential, in a configuration file the platform does not read. Coverage then depends on endpoint configuration management, which is a real control owned by a team that will not read this document.

**Boundary rule.** Passes. Under a benign model an unsanctioned connector is a productivity story. Under a hostile one it is an unmediated path with a fully authenticated user behind it.

**Positions.** In scope as a discovery input, with the enforcement cited and not designed, against out of scope with a named residual in chapter 20. The first is more useful and requires chapter 7 to admit a control it does not own.

**What would settle it.** A scope decision, then either two sentences in chapter 7's discovery beat or a line in the residual. Cheap either way; expensive to omit.

## OQ-13 · The far side is not always deterministic, and increasingly is not typed

**Question.** What does the architecture do with agents that act through a browser or a desktop rather than through typed calls, where there is no operation name, no argument schema and no declarable side-effect class?

**Status and reach.** `[SCOPE]` · ch. 7, 8, 20 · `[ADR-11]`, `[ADR-17]`

**Why it is open.** The allow-list of typed operations and the declared side-effect class are two of the load-bearing decisions in Part II, and both assume the effect has a name. A click does not. This deployment shape is growing faster than the one the document describes, and a reader will ask on the first page of chapter 8. The answer may well be that it is out of scope, and that answer is worth a paragraph rather than a silence, because the reasoning – that the architecture requires a typed seam and browser automation does not have one – is itself the most useful thing the document can say about it.

**Boundary rule.** Passes. It is precisely the case where a hostile model's options are widest and the control set is thinnest.

**Positions.** Out of scope with a stated reason and a residual entry, against a tier rule that treats an untyped effect path as unmediated by definition and therefore ineligible above the reversibility line. The second is stronger and costs a paragraph.

**What would settle it.** A scope decision recorded in the manifesto's non-goals, and a residual entry in chapter 20 either way.

## OQ-14 · The six properties need a recipient

**Question.** Is the protocol wish list a specification contribution the author submits and tracks, or a private list that ages inside a PDF?

**Status and reach.** `[POSITION]` · ch. 8, 20

**Why it is open.** The card already flags the tone question. The larger question is what the list is for. A wish list with a named venue and a submission is a different artefact from a wish list in a chapter, and it changes how the chapter is written, because a proposal has to be implementable by its reader and a complaint does not.

**Boundary rule.** Not applicable. This is a project decision with a subject-matter consequence.

**Positions.** Submit and cite the discussion, against publish and let the specification community find it. The first is more work and makes the chapter's revisit triggers real.

**What would settle it.** An author decision, and it should be taken before chapter 8 is drafted rather than after.

---

# Cluster D. Memory across bounded contexts

Chapter 10 treats memory as a writable data system with an adversarial write path, which is the right frame and covers one run's retrieval. It does not cover memory as a thing that spans contexts, principals and time – which is where the interesting failures are, because the interesting failures are the ones that separate the write from the exploitation.

## OQ-15 · Memory that spans bounded contexts is an aggregation channel

**Question.** When one agent operates across two bounded contexts, may a fact derived in one be carried into the other by memory – given that every individual retrieval was entitled and the composite was authorised by nobody?

**Status and reach.** `[BLOCKING]` · ch. 10, 17 · `[ADR-20]`, `[ADR-21]`

**Why it is open.** Entitlement checks are per item and per principal, and they are blind to composition. An agent that reads claims history under a valid entitlement and underwriting history under a valid entitlement, and writes the joined inference to memory, has created a fact that neither data owner released and that no policy evaluated. Purpose limitation is the obligation that bites, and chapter 10 currently invokes purpose binding as a blast-radius control without noticing that it is the only control here. This is also the mechanism by which a governed agent estate becomes a shadow data warehouse with no schema and no owner.

**Boundary rule.** Passes. A hostile model is an aggregation engine with a legitimate reason to read everything.

**Positions.**
- **Partition by construction.** Memory is scoped to a bounded context and carry-over across contexts does not exist. Clean, enforceable, and it forbids the cross-domain work that is the reason the organisation wanted an agent.
- **Carry with derived provenance and a purpose check at write time.** A memory item records the contexts that contributed to it, and the write is evaluated against the purpose of both. Expensive, novel, and it moves the control from read time to write time, which is the only place the composition is visible.
- **Carry freely, control at the seam.** Composite knowledge may inform but may not be the sole justification for an operation above a tier. This is chapter 10's quarantine idea generalised, and it has the same problem the card already flags: the distinction is clean on paper and hard inside a context window.

**What would settle it.** A derivation, and probably a decision record. Position two is the contribution nobody else has published, which is an argument for taking it seriously and a warning about the evidence base.

## OQ-16 · Whose memory is it

**Question.** Is memory scoped to the agent, to the principal, or to the organisation – and what does the answer do to erasure, entitlement and the value of the memory at all?

**Status and reach.** `[BLOCKING]` · ch. 10, 11 · `[ADR-21]`, `[ADR-22]`

**Why it is open.** The outline assumes a scope without stating one. It matters more than it looks. Agent-scoped memory means one principal's content shapes another principal's run, which defeats entitlement-scoped retrieval on the write side rather than the read side, and no amount of care at retrieval time repairs it. Principal-scoped memory preserves the entitlement model and destroys most of the value, because the organisational learning an agent estate is bought for is exactly the cross-principal part. Organisation-scoped memory is the aggregation problem of OQ-15 as a design goal.

**Boundary rule.** Passes. The scope decides what an injected instruction can reach and how long it waits.

**Positions.** Three scopes, or a tiered arrangement where organisation-scoped memory holds only content that was authored rather than retrieved, and everything derived from a principal's data stays with that principal. The tiered version is probably right and it needs the provenance model to distinguish authored from derived, which is a requirement chapter 10 does not currently place on itself.

**What would settle it.** A derivation in chapter 10, and a consequence for chapter 11: if memory items can become evidence, they inherit the chain, and if they cannot, the evidence record has to reference them without containing them.

## OQ-17 · Attenuation holds within a run and not across a sequence

**Question.** What stops an agent that cannot widen its own envelope from writing something to memory that causes a later, legitimately derived run to request and receive a wider one?

**Status and reach.** `[OPEN]` · ch. 6, 10, 17 · `[ADR-10]`, `[ADR-21]`

**Why it is open.** `[ADR-10]` makes widening unrepresentable, which is a strong property and is scoped to a delegation chain. Memory is a channel between runs, and the derivation of a new envelope reads declared need, which is influenced by the task, which is influenced by memory. Chapter 17 handles composition in space – parent and child. Nothing handles composition in time, and time is where this architecture is weakest, because the whole design bounds a run and then lets runs talk to each other through a store it treats as a data problem.

**Boundary rule.** Passes. This is the patient adversary, and patience is the one advantage the document grants Kai everywhere else.

**Positions.**
- **Declared need is never derived from memory.** The need declaration is a static, reviewed artefact of the agent version, not a runtime computation. This is probably already the intent and it is nowhere stated, and stating it converts a vulnerability into an invariant.
- **Memory-influenced derivation is permitted below a tier.** Pragmatic, and it puts a laundering path directly into the authority model.

**What would settle it.** One sentence in chapter 6, promoted to an invariant if it survives: authority derivation reads no input the agent can write. That sentence, if it holds, is one of the more valuable lines in the document and it does not currently exist.

## OQ-18 · Forgetting is a control, and it fights the evidence chain

**Question.** Does memory inherit the evidence chain's integrity properties, and can a memory item be entered as evidence at all given that memory is designed to be mutable and evidence is designed not to be?

**Status and reach.** `[OPEN]` · ch. 10, 11 · `[ADR-21]`, `[ADR-22]`

**Why it is open.** Chapter 11 resolves the immutability and erasure conflict elegantly for evidence. Memory has the opposite default: it should forget, retention is per item, and correction is normal operation. Yet the question asked eighteen months later is often *what did it know when it did that*, which is a question about memory answered from evidence. If evidence references a memory item that has since been corrected or forgotten, the record is verifiable and no longer reconstructible, and the document should say which of those two properties it is claiming.

**Boundary rule.** Passes weakly. It is mostly a data governance problem, and it becomes a security problem at the point where the ability to correct memory is the ability to change what the record appears to say.

**Positions.** Evidence records the retrieval reference and a content hash rather than the content, against evidence containing the content under a per-subject key like everything else. The first is cheap and admits it cannot reconstruct; the second is expensive and duplicates personal data into an immutable store, which the data protection officer will notice. See OQ-28, which is the same trade-off at a different scale.

**What would settle it.** A decision record covering both this and OQ-28, since one construction answers both.

---

# Cluster E. Agents as code, and the lifecycle nobody bound to them

Chapter 14 quarantines an agent version. No chapter says what a version is. This cluster is the largest structural gap in the outline: the document governs what an agent does at runtime and says nothing about how an agent comes to exist, what it is made of, who reviewed it, and what changed when it stopped behaving.

## OQ-19 · What is the deployable unit

**Question.** Is an agent a single signed, versioned artefact composed of instructions, tool bindings, model identity and parameters, memory scope, declared need and policy references – and if not, what exactly does chapter 14 quarantine?

**Status and reach.** `[BLOCKING]` · ch. 6, 8, 14, 15, 16 · `[ADR-16]`, `[ADR-26]`, `[ADR-27]`

**Why it is open.** Three separate mechanisms already assume this artefact exists. Chapter 6 needs a declared need that somebody wrote and keeps true. Chapter 8 pins and signs tool manifests but not the binding between an agent and the tools it may reach. Chapter 14 quarantines a version. Each assumes a different half of the same object and no chapter defines it. Once defined, it is the thing that makes the estate governable: a signed composite with an owner, a version, a diff, a promotion path and a rollback. Without it, every control in Part II attaches to something the organisation cannot name.

**Boundary rule.** Passes. The composite is what determines what the model can attempt, and its integrity is the precondition for every other integrity claim in the document.

**Positions.**
- **One artefact, signed, promoted through environments.** The strong position. It gives chapter 14 something real to quarantine and chapter 15 something real to recertify.
- **Several artefacts with a manifest binding them.** More realistic in an estate where prompts live in a product tool and policy lives in a repository, and it means the binding is the security object and the parts are not.

**What would settle it.** A derivation, and almost certainly a chapter. See the structural note at the end of this file.

## OQ-20 · Instructions are code that no compiler checks

**Question.** What gates a change to an agent's instructions, given that an instruction change can widen effective behaviour without touching the envelope, and no static analysis will tell a reviewer that it did?

**Status and reach.** `[OPEN]` · ch. 6, 9, 15

**Why it is open.** The envelope bounds what an agent may do. Instructions determine what it will attempt within that bound, and the difference between a cautious agent and a reckless one at the same tier is entirely instruction text. Change control on that text is therefore a security control, and it is the only one in the document with no mechanical check behind it. Review by reading does not scale and does not catch the subtle case, which is the addition of a sentence that makes an existing permitted operation routine.

**Boundary rule.** Passes. An instruction change is the cheapest way to change behaviour without tripping a single control the document describes.

**Positions.**
- **Behavioural gates rather than textual review.** An instruction change is gated by an evaluation suite that measures what the agent attempts, not by a reviewer reading a diff. See OQ-21.
- **Tier-proportionate review.** Above a tier, an instruction change requires the same approval as a widening of declared need. Cheap to state, and it moves the bottleneck onto the same people who are already the bottleneck.

**What would settle it.** A derivation, joined to OQ-21, and one honest sentence admitting that this is the control with the weakest mechanical backing in the whole design.

## OQ-21 · Evaluations are gates, canaries are their production twin

**Question.** What is a security evaluation for an agent version, what does a pass mean statistically, and is a failed evaluation a deployment blocker?

**Status and reach.** `[OPEN]` · ch. 15, 16 · `[ADR-27]`

**Why it is open.** Chapter 15 already has canary runs – adversarial cases that should be refused, executed continuously against production – and describes them as the only mechanism that detects a control's absence. The same instrument belongs at deployment time, and the document does not connect them. The hard part is what a pass means. The system is non-deterministic, so the gate is statistical, and a refusal rate of 98 per cent against a red-team suite is either excellent or unacceptable depending on a judgement nobody has made. Stating the judgement is more useful than any of the tooling around it.

**Boundary rule.** Passes. The evaluation measures behaviour under adversarial input, which is the document's subject.

**Positions.** A hard gate with a stated threshold per tier, against an advisory measurement with a trend requirement. The first is the only one that constrains anything and it will be overridden in the first quarter, which is an argument for designing the override rather than pretending it will not happen.

**What would settle it.** A derivation joined to chapter 15's canary section, and a threshold decision that has to be the author's rather than the literature's, because the literature does not have one. `[PENDING: published agent red-team suites and any reported refusal rates, cited as preprints]`

## OQ-22 · The model changes underneath the artefact

**Question.** Does the platform pin model versions, how does it detect that a pinned model has silently changed behaviour, and what forced-migration deadline does the vendor get to set?

**Status and reach.** `[OPEN]` · ch. 2, 15, 20 · `[ADR-04]`

**Why it is open.** The model is the only dependency in the system that can change behaviour without changing a version string, and the only one whose supplier can deprecate it on a schedule the organisation does not control. Both facts are third-party risk in the sense that chapter 2's obligations mean, and both are absent from the outline. The second is the more interesting: an agent estate has a vendor-imposed migration cadence that no other part of the platform has, and the operational cost of revalidating every agent version against a new model is the cost nobody has budgeted.

**Boundary rule.** Passes. A model that changes is a change to the thing the entire threat model is about.

**Positions.** Pin and revalidate on change, with the canary suite as the detector, against float and rely on continuous canaries alone. The first is right for tier-0 and expensive; the second is what everyone does.

**What would settle it.** A derivation in chapter 15 with a decision record, plus a row in chapter 2's constraint inventory, since for most readers the vendor's deprecation calendar is an imposed constraint of exactly the kind that chapter exists to identify.

## OQ-23 · There is no local development story

**Question.** How does a developer build and test an agent against a gateway, a policy bundle and a registry that do not exist on a laptop?

**Status and reach.** `[POSITION]` · ch. 16 · `[ADR-28]`

**Why it is open.** Chapter 16's beats already name this as one of the places the minutes go, and then the chapter moves on. It is the single largest determinant of whether the paved road is used, and the answer is a real engineering commitment: a local gateway, a signed development bundle with a hard tier ceiling, a test tenant with synthetic systems of record, and seeded evidence. Naming it as a cost without designing it is the pattern chapter 16 is written to criticise.

**Boundary rule.** Fails, mostly, and belongs in the document anyway on chapter 16's own argument that adoption is a security property.

**Positions.** A development tier with its own ceiling, against a full local emulation of the control plane. The first is cheaper and leaks less.

**What would settle it.** A worked example in Appendix E and a paragraph in chapter 16.

---

# Cluster F. Delegation, sub-agents and routing

Chapter 17 handles which invariants survive an agent calling an agent. It does not handle which model executes what, which is the delegation decision made most often and governed least.

## OQ-24 · Model routing is an authority decision wearing an optimisation's clothes

**Question.** Is model identity part of the envelope – and what happens when a router sends a tier-2 operation to a cheaper, a fallback or a differently located model?

**Status and reach.** `[BLOCKING]` · ch. 2, 6, 12, 13, 17 · `[ADR-09]`, `[ADR-25]`

**Why it is open.** Routing changes capability, cost, vendor, jurisdiction and failure profile, and it happens per call, automatically, under load, decided by a component that is optimising for latency and price. Nothing in the outline mentions it. Three consequences follow and none is currently visible in the document. A fallback route under vendor outage is a silent change to the safety case, made by an availability mechanism during exactly the degraded conditions chapter 13 is about. A route to a different vendor may move data across a boundary chapter 2's obligations constrain, without any of chapter 10's controls firing, because nothing was retrieved. And a cheaper model at the same tier has a different refusal profile, which means the evaluation result in OQ-21 was measured against a model that is not the one executing.

**Boundary rule.** Passes at high weight. The routing decision selects the adversary's substrate.

**Positions.**
- **Allowed model set as a tier property.** The envelope carries the permitted models, a route outside it terminates the run rather than degrading it, and the fail posture matrix gains a row for model unavailability. Strong, buildable, and as far as the author's reading goes, nobody does it.
- **Routing free below a tier, pinned above it.** The pragmatic version, and the line has to be argued rather than assumed.
- **Out of scope, model choice is a product decision.** Defensible only if stated, and it undermines OQ-21 and OQ-22 together.

**What would settle it.** A derivation, a decision record, and a row in chapter 13's matrix. This is the strongest single addition available to the document, because it is a real control nobody has proposed and it follows in three lines from machinery the document already has.

## OQ-25 · Who derives the sub-agent's envelope

**Question.** Does the parent derive the child's envelope, or does the platform derive it on the parent's behalf – and does the parent therefore hold a meta-authority that the model has no way to represent?

**Status and reach.** `[OPEN]` · ch. 6, 17, 18 · `[ADR-10]`, `[ADR-29]`

**Why it is open.** `[ADR-29]` gives sub-agents derived envelopes and does not say who derives. If the parent derives, the parent holds an authority to create authority, which is not an operation in the allow-list and is not attenuation in any obvious sense. If the platform derives, the parent has to declare need for its child, which is a static artefact for a dynamic decision and pushes back into OQ-19. The distinction decides whether delegation depth is bounded by policy or by construction.

**Boundary rule.** Passes. It is the mechanism by which a compromised parent would attempt to manufacture reach.

**Positions.** Platform-derived from a declared delegation graph in the agent artefact, against parent-requested with the platform intersecting. The first bounds the graph statically and forbids the dynamic composition people actually want.

**What would settle it.** A derivation in chapter 17, which cannot be written before OQ-19 is answered.

---

# Cluster G. The economics, where the cost is context and the context is the attack surface

Almost all of what an agent consumes is assembled input, not the agent's own logic. That single fact relocates cost governance into the same components that carry the security properties, and it makes several security questions into budget questions and several budget questions into security questions. The outline mentions a budget four times and never defines its unit.

## OQ-26 · The budget has no unit, and its unit decides whether it composes

**Question.** Is a run's budget denominated in tokens, in money, in tool calls or in wall clock – and is exhaustion a stop mechanism?

**Status and reach.** `[OPEN]` · ch. 3, 13, 14, 17

**Why it is open.** Chapter 3 makes budget one of the four things a run owns. Chapter 17 says budget composes only if centrally held and prices the contention. Neither says what is being counted. It matters, because the unit determines who can exhaust it and how fast: a token budget is exhausted by the platform's own retrieval choices, a money budget moves when the vendor changes prices, and a call budget is the only one an allow-list can reason about. Fan-out then makes this a denial-of-wallet question as well as an amplification question, and chapter 17 currently treats amplification as an authority threat only.

**Boundary rule.** Passes. A hostile model with a legitimate envelope and no budget ceiling is a cost attack that no other control in the document notices.

**Positions.** Tokens as the primitive with money derived, against calls as the primitive with tokens as telemetry. The first is honest about where the cost is and makes the ceiling depend on a vendor's tokenizer; the second is enforceable at the seam, which is where enforcement already lives.

**What would settle it.** A definition in chapter 3, a sixth entry in chapter 14 or an explicit argument for why exhaustion is not a stop, and a paragraph in chapter 17.

## OQ-27 · Prompt caching is a security boundary nobody has drawn

**Question.** Does the platform require context cache isolation per principal and per tenant, and what does the isolation cost in the unit everyone is optimising?

**Status and reach.** `[OPEN]` · ch. 10, 12 · `[ADR-20]`

**Why it is open.** Providers cache context prefixes to reduce cost and latency, and the saving is large enough that it drives architecture: teams deliberately structure prompts so the expensive shared prefix is reused. A cache shared across principals is a channel between them, and cache hit behaviour is observable in latency, which makes it an oracle for whether a given prefix has been seen. Everything chapter 10 does to keep one principal's content out of another principal's run is undone if the content is in a shared prefix. The outline does not mention caching, and the economics guarantee that someone will introduce it after the architecture is signed off.

**Boundary rule.** Passes. It is a cross-principal channel created by a cost optimisation, which is the purest form of the problem this document is about.

**Positions.** Per-principal cache partitioning with the cost stated, against shared caching restricted to platform-authored content that contains nothing principal-derived. The second is probably right and requires the context assembly to be structured so that the boundary between platform content and principal content is mechanical rather than conventional.

**What would settle it.** A derivation in chapter 10 or 12 and a decision record. `[PENDING: vendor caching semantics and isolation guarantees, dated, per provider]`

## OQ-28 · Evidence of context is the largest, most sensitive and most useful record

**Question.** To answer *what did it read*, does the evidence record contain the assembled context, or references and hashes – and what is the document claiming when it says a run can be examined afterwards?

**Status and reach.** `[BLOCKING]` · ch. 10, 11, 20 · `[ADR-22]`, `[ADR-23]`

**Why it is open.** Chapter 11 promises that the evidence answers what the platform knew at the time. The assembled context is that knowledge, it is the largest object in the system, it is full of personal data, and it is regenerated on every call. Storing it is a storage cost measured against run volume and an erasure obligation measured against subjects. Not storing it means the record cannot reconstruct what the model saw, which is exactly the question a supervisor asks. The document currently promises the strong version and prices the weak one.

**Boundary rule.** Passes. What was in context is what an injection reached, and it is therefore the only record that can establish how an incident happened rather than what it did.

**Positions.**
- **References and a hash of the assembled context.** Cheap, verifiable, and reconstructible only if every referenced item is unchanged – which OQ-18 says it will not be.
- **Full context under a per-subject key, with the chapter 11 construction.** Complete, expensive, and it duplicates personal data into the one store designed to resist deletion.
- **Tier-dependent.** Full context above the reversibility line and references below it. Probably the answer, and it needs the cost stated per tier rather than as a single figure.

**What would settle it.** A derivation joined to OQ-18, and a correction to whatever chapter 11 currently promises, so that the promise and the price describe the same system.

---

# Cluster H. Time, proof and the boundary of the estate

## OQ-29 · What counts as proof when the reasoning is not evidence

**Question.** Can a run be reconstructed eighteen months later, and if the reasoning cannot be reproduced, what standard of proof is the document actually claiming?

**Status and reach.** `[POSITION]` · ch. 9, 11, 20 · `[ADR-22]`

**Why it is open.** The sequence of effects is mechanical and provable. The reasoning is not reproducible even in principle, and the model's account of itself is the most persuasive and least evidential artefact available – which chapter 9 says well about the approval screen and never generalises to the evidence chapter. The position is defensible and it needs checking against what oversight obligations actually demand, because a regulator asking why an action was taken is not satisfied by a hash chain proving that it was.

**Boundary rule.** Passes weakly. It is mostly an evidentiary question, and it becomes a security question at the point where a plausible generated explanation is admitted as a record.

**Positions.** Effects are evidence and reasoning is not, stated plainly and once, against recording the model's stated rationale as a labelled non-evidential artefact. The second is more useful to an incident responder and more dangerous in a hearing.

**What would settle it.** A short passage in chapter 11, checked against the oversight provisions chapter 2 pins.

## OQ-30 · A run that outlives a policy change

**Question.** When policy changes mid-run, does the run finish under the policy in force at its start or at each call – and what bounds a run's duration for that reason rather than for an operational one?

**Status and reach.** `[OPEN]` · ch. 3, 12, 14 · `[ADR-02]`, `[ADR-24]`

**Why it is open.** Chapter 3's card already flags long-running agents as the place a hostile reviewer will push. This is the sharper version of the same question and it is joined to OQ-09. Chapter 12's staleness budgets bound how old an input may be; nothing bounds how long a decision already taken remains in force. Revocation is exempted by `[ADR-26]` and `[ADR-24]`, which is a strong hint that maximum run duration is a security parameter that the document has not yet named as one.

**Boundary rule.** Passes. It is the interval during which the platform knowingly enforces a decision it has withdrawn.

**Positions.** Bounded run length with forced re-derivation at the boundary, against per-call evaluation that makes run length irrelevant to policy but not to the envelope. The two are the two halves of OQ-09 and should be decided together.

**What would settle it.** The OQ-09 derivation, extended by one paragraph in chapter 3.

## OQ-31 · Tenancy, residency and the vendor at the bottom of the stack

**Question.** What are the tenancy and data residency properties of the platform, and how do they survive a model vendor whose inference happens somewhere the organisation did not choose?

**Status and reach.** `[SCOPE]` · ch. 2, 18, 20

**Why it is open.** The cast fixes a tenant identifier and no chapter says what tenancy means – whether the platform is multi-tenant, whether policy bundles and memory are partitioned by tenant, whether the gateway is. For a single enterprise it may not matter. For the cross-organisational part it certainly does, and it is joined to OQ-24, because routing decides where inference physically happens and therefore which residency claim the organisation can make. This may be out of scope, and the reason should be stated.

**Boundary rule.** Fails on the general tenancy question, which is ordinary platform engineering. Passes on the routing and residency intersection, which is specific.

**Positions.** In scope as a constraint in chapter 2 and a residual in chapter 20, against a full treatment in chapter 18. The first is proportionate.

**What would settle it.** A scope decision and a row in the constraint inventory.

---

# Resolutions (2026-07-31)

Positions chosen below. Each is argued in the chapter named; new ADRs marked *new* are to be added to Appendix B during drafting.

| ID | Resolution | Primary home |
|---|---|---|
| OQ-01 | **Standing mandate** for unattended runs: durable delegation artefact (principal, task class, ceiling, expiry); envelope derived against mandate, not live human. Schema in Appendix D. | ch. 5 · *ADR-31 new* |
| OQ-02 | **Both recertification views:** tier ceiling + declared need (data owner); exercised set last quarter (platform, via ch. 11). | ch. 15 · *ADR-32 new* |
| OQ-03 | **Integrate** incumbent PAM for vaulting and session recording; **elevation as new run** with human in derivation, never in-run widening. | ch. 5, 16 · ch. 2 constraint row |
| OQ-04 | **Hybrid per tool:** broker-only where exchange exists; HSM custodian for legacy; second coverage dimension published. | ch. 8, 20 |
| OQ-05 | **No agent break-glass.** Emergency path is human acting directly on system of record; path maintained and drilled. | ch. 14 · *ADR-33 new* · Appendix G |
| OQ-06 | **Two policy artefacts:** slow signed bundle + fast deny list with own signing authority and mandatory expiry. | ch. 12 · *ADR-34 new* |
| OQ-07 | **Deny-overrides** with explicit precedence; evaluation **bounded by construction** in chosen language. | ch. 12 · Appendix A |
| OQ-08 | **Both:** rule-level firing telemetry (quarterly never-fired / always-fired review) and build-time test suite with required coverage. | ch. 12, 15 |
| OQ-09 | **Envelope is upper bound** at derivation (intersection ceiling); **policy evaluated per call** within envelope; **max run duration** forces re-derivation. | ch. 6, 12 · *ADR-35 new* |
| OQ-10 | **Elicitation never forwarded**; **sampling only** under declared manifest capability with quarantine marking. | ch. 8, 9 |
| OQ-11 | **Extend `[ADR-15]`** to all server-originated payloads (resources, prompt templates). | ch. 8, 10 |
| OQ-12 | **In scope as discovery input** for coverage; endpoint connector config counted; enforcement cited, not designed. | ch. 7 |
| OQ-13 | **Typed seam required** above reversibility line; browser/desktop automation **out of scope** with stated reason and ch. 20 residual. | ch. 8, manifesto §4 · ch. 20 |
| OQ-14 | **Submit** six-property list to MCP/spec venue; cite discussion in ch. 8. | ch. 8 |
| OQ-15 | **Carry with derived provenance** and purpose check at write time. | ch. 10 · *ADR-36 new* |
| OQ-16 | **Tiered scopes:** org memory holds **authored only**; principal-derived stays principal-scoped; provenance distinguishes. | ch. 10 |
| OQ-17 | **Declared need is static reviewed artefact**; authority derivation reads **no agent-writable input**. Promote to invariant **I8**. | ch. 6, 12 · *I8 new* |
| OQ-18 | Evidence records **retrieval reference + content hash**; not full mutable memory content. | ch. 11 · with OQ-28 |
| OQ-19 | **Signed agent manifest** binding prompt hash, tool refs, declared need, policy refs, model set, delegation graph. | **ch. 12 new** · *ADR-37 new* |
| OQ-20 | **Tier-proportionate instruction review** + behavioural eval gates (joined OQ-21); weakest mechanical backing stated plainly. | ch. 12 |
| OQ-21 | **Hard deployment gate** per tier with stated refusal threshold; override logged with mandatory review. | ch. 12, 15 |
| OQ-22 | **Pin model versions**; revalidate on change via canary suite; vendor deprecation as ch. 2 constraint row. | ch. 12, 15 |
| OQ-23 | **Development tier** with synthetic tenant and hard ceiling; not full local control-plane emulation. | ch. 16 · Appendix E |
| OQ-24 | **Allowed model set as tier property** in envelope; route outside set terminates run. | ch. 12, 13 · *ADR-38 new* |
| OQ-25 | **Platform derives** sub-agent envelope from declared delegation graph in manifest. | ch. 17 |
| OQ-26 | **Tool calls** as budget primitive; tokens as telemetry. | ch. 3, 14, 17 |
| OQ-27 | **Shared cache** only for platform-authored prefix; principal-derived content in isolated prefix. | ch. 10, 12 |
| OQ-28 | **Tier-dependent context evidence:** full assembled-context hash + refs above reversibility line; refs only below. | ch. 11 · *ADR-39 new* |
| OQ-29 | **Effects are evidence; reasoning is not.** Model rationale may be recorded as labelled non-evidential artefact only. | ch. 11 |
| OQ-30 | Decided with OQ-09: per-call policy within fixed envelope; max run duration as security parameter. | ch. 3, 12 |
| OQ-31 | **Tenancy/residency** as ch. 2 constraint row; routing–residency intersection in ch. 18 and ch. 20 residual. | ch. 2, 18, 20 |

# What this register does to the structure

Four subjects were chapter-sized; three are now absorbed, one adds a chapter.

| Subject | Questions | Home (resolved) |
|---|---|---|
| Agents as code: deployable unit, lifecycle, evaluations, model pinning, routing | OQ-19 to OQ-24 | **New chapter 12: The Agent Manifest** (Part III head). Old chapters 12–20 renumbered 13–21 |
| Unattended principal, mandate, identity lifecycle, PAM | OQ-01 to OQ-05 | Extension of chapter 5; recertification in chapter 15 |
| Economics of context: budget, caching, evidence of context | OQ-26 to OQ-28 | Distributed: chapters 3, 10, 11, 12, 14 |
| Memory across contexts and time | OQ-15 to OQ-18 | Chapter 10 extended; invariant I8 in chapter 6 |

**Draft-ready gate.** OQ-09, OQ-19, and OQ-01 were the three pre-draft blockers; all three are resolved above. Remaining `[BLOCKING]` items block only their named chapters.

**Length.** Spine projection revised to **170–180 pages** narrative (`toc.md`, `manifesto.md` decision 16). Material grew because the subject did; compressing derivations into paragraphs is not the response.

# Working order (revised)

1. ~~OQ-09 and OQ-19~~ – resolved.
2. ~~OQ-01, OQ-02~~ – resolved; draft into ch. 5 and mandate schema.
3. **OQ-10 and OQ-11** – pin protocol revision during ch. 8 outline integration.
4. Draft **chapter 12 (Agent Manifest)** card to `[BEATS]` before Part III mechanism chapters 13+.
5. **OQ-15 through OQ-18** – one derivation pass into ch. 10.
6. **OQ-26 through OQ-28** – one derivation pass into ch. 3, 10, 11, 12.
7. Everything else at draft time in the owning chapter.

---

*Register v0.2 – 2026-07-31. Thirty-one questions resolved. Propagated to `outline.md`, `worked-moments.md`, `toc.md`, `manifesto.md`.*
