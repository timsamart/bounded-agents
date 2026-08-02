# Appendix A. Control register {#appendix-a}

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
