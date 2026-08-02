# Appendix B. Architecture decision records {#appendix-b}

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
