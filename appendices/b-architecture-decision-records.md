# Appendix B. Architecture decision records {#appendix-b}

The thirty-nine ADRs live as individual files under decisions/. This appendix indexes them and holds the C4 views.

## Decision index {#a-2-0}

See decisions/README.md and files ADR-01 through ADR-39. Each record is in Nygard form: context, decision, consequences, rejected alternatives, reopen trigger.

## C4 views {#a-2-1}

Context (level 1), container, and component views for the Borealis reference deployment. Section semantics follow arc42; view levels follow the C4 model. Edition 0.1 states the placement rule: views live here, not in the spine.

## Unbuildable across the organisational boundary {#a-2-30}

Claims that cannot be checked by the recipient without a live call into the issuer's TCB. Portable full envelopes, mutual mediation-coverage attestation as a hard gate, and shared risk scores without verification paths. Paired with ADR-30.
