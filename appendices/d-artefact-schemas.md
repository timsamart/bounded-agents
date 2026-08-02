# Appendix D. Artefact schemas {#appendix-d}

Wire formats summarised. Edition 0.1 gives field inventories; JSON Schema files follow in a later cut.

## Run credential {#a-4-1}

Claims include sub (run), act (workload and principal), aud, cnf or proof-of-possession, envelope reference, expiry. The credential references the envelope; it does not embed derivation inputs.

## Envelope, mandate, budget {#a-4-2}

Envelope: operations allow-list, object scopes, derived_from, no widen field. Standing mandate: human, task class, ceiling, expiry. Budget: tool-call counter shared across a delegation tree.

## Mediated tool call {#a-4-3}

Agent-supplied name and arguments plus gateway-injected run id, envelope digest, budget remaining, and decision reference. Authority fields never originate on the agent side of the seam.

## Approval binding {#a-4-4}

Triple digests: frozen call, shown view, execution compare. Child delegation budget fields: shared counter; null fields that stay null by schema.

## Evidence event and refusal {#a-4-5}

Evidence event with effect_state, settled_by, content ciphertext reference. Refusal object with excluded_by naming which derivation input blocked the call. Foreign-attestation receipt is local evidence, not a foreign chain.

## Manifest promotion block {#a-4-6}

promotion.evaluation carries fail number, acceptor, and override expiry.

## Memory item and degraded refusal {#a-4-7}

Memory item: provenance, version, retention, purpose. Degraded-mode refusal carries posture, matrix version, and capability set for UI. Human system-of-record actions enter the same evidence chain without a run id.
