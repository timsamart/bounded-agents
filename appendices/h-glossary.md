# Appendix H. Glossary {#appendix-h}

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
