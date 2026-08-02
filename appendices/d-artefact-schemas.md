# Appendix D. Artefact schemas {#appendix-d}

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
