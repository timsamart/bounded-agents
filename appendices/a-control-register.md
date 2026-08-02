# Appendix A. Control register {#appendix-a}

Normative requirements traced threat to control to test to evidence. RFC 2119 language lives here, not in the spine.

## Trusted computing base {#a-1-1}

The TCB is the gateway, the decision path, the evidence path, and the key material beneath them. The agent, model, framework, tools, and orchestration sit outside. No later mechanism adds a member without reopening ADR-03.

## Constraint classes and register framing {#a-1-2}

Constraints sort into imposed, conventional, and self-imposed. Appendix A is a control register only when every row traces to an obligation; otherwise it is compliance theatre with citations.

## Approval card content {#a-1-4}

The approval surface shows effect class, irreversibility, diff against current state, and budget consumed. Prompt text and model rationale are recorded as non-evidential and are not shown as the thing being approved.

## Key management and exit authority {#a-1-6}

Per-subject evidence keys, witnessed destruction, and backup or replica deletion regimes. Stop-exit authority is not entry authority; restart uses dual control recorded on the evidence path.

## Risk tiers and acceptance register {#a-1-7}

Tier definitions (illustrative Borealis: T2 about 5,000 EUR irreversible exposure). Open unmediated paths are named risk acceptances with owners and review dates, not silent exceptions.

## Promotion gates and policy-language bounds {#a-1-9}

Hard evaluation gates with signed time-bounded overrides. Policy language evaluation is build-time bounded: no unbounded recursion or iteration on the hot path.
