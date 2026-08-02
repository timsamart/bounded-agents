# Appendix C. Threat model and method {#appendix-c}

Threat set for a hostile model with real tools. Method for regenerating threats when the set ages.

## Primary adversary {#a-3-1}

The primary adversary can shape inputs the agent reads – documents, web pages, email, tool descriptions, memory entries – and needs one successful instruction to act with authority the agent already holds. The model itself is treated as hostile at any moment, including between tool calls. The adversary is a person. The model is not the villain; it is an unreliable intermediary.

Secondary adversaries (insider misuse of approval, supply-chain compromise of a tool server, availability attacks on the evidence path) are in scope where they falsify an invariant. Physical robots, consumer agents, and model-training attacks are out of scope per chapter 1.

## Method {#a-3-2}

Derive threats from invariants I1–I8 (Appendix F). A threat that does not falsify an invariant is out of scope for this register. Refresh the set when a protocol, vendor, or regulation changes an assumption named in an ADR reopen trigger. Prefer threats with a worked path on the Borealis cast over abstract STRIDE categories without a seam attachment point.
