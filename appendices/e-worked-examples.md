# Appendix E. Worked examples {#appendix-e}

Compiled from spine worked moments. Edition 0.1 indexes the walkthroughs with the decision points a reader must be able to defend; full byte-level traces follow in a later cut.

## Onboard a tool {#a-5-1}

1. Publisher signs tool description and side-effect class.
2. Registry promotion requires conformance checks on push.
3. Pin digest into agent manifest; no runtime discovery.
4. First live call under mediation; refusal canary registered.

Compiles chapters 7–8. Constraint inventory template from chapter 2 belongs in the same onboarding pack: imposed / obligation / convention rows before the first envelope is derived.

## Derive an envelope {#a-5-2}

Intersection: declared need ∩ principal reach ∩ tier ceiling. Worked Borealis case: `claims-triage` under Marta's reach yields four typed operations against one claim. Unattended variant substitutes standing mandate for interactive principal.

## Graduate to unattended {#a-5-3}

Standing mandate signing ceremony, gate measurement for the human queue left behind, bundle staleness budget agreed. Compiles chapters 5, 9, 12.

## Work a suspected compromise {#a-5-4}

Stop within stated interval (chapter 15), evidence chain verify (chapter 11), coverage gap check (chapter 7). Eleven-minute historical stop at Borealis (2026-03-02) is the negative example: wrong lever first.

## Possible software solutions {#a-5-5}

The spine names architectural categories, not products. A single vendor or open-source name in the main argument would read as a hard dependency. This section lists *possible* products per category so a reader who must map the design onto an estate has somewhere to look.

Listing a name here is not a recommendation, not an endorsement, and not a statement that the product satisfies any control in Appendix A. The lists are non-exhaustive, mix commercial and open-source options where that is honest, and will age. Prefer the category language in Parts I–IV; use this catalogue only when filling a constraint inventory or procurement shortlist.

### Workforce identity provider {#a-5-5-1}

Category: enterprise identity provider for people and (often) service accounts. Issues credentials the broker must not treat as run credentials.

Examples of products in this category (non-exhaustive, not endorsed): Microsoft Entra ID; Okta Workforce Identity; Keycloak; Ping Identity / PingFederate; Auth0 (workforce configurations).

### Privileged access, secrets and PAM {#a-5-5-2}

Category: privileged access management, secrets vaulting and interactive session recording. The incumbent the broker fronts and whose session records the gateway should emit into.

Examples of products in this category (non-exhaustive, not endorsed): CyberArk Privileged Access Manager; HashiCorp Vault; BeyondTrust Privileged Remote Access / Password Safe; cloud-native PAM and secrets offerings (for example AWS Secrets Manager with privileged session tooling, Azure Key Vault with Privileged Identity Management, Google Secret Manager with companion PAM); Akeyless or similar secrets brokers.

### Policy-as-code and authorisation engines {#a-5-5-3}

Category: engines that evaluate signed, versioned policy bundles on the decision path.

Examples of products in this category (non-exhaustive, not endorsed): Open Policy Agent (OPA) / Gatekeeper; Cedar (and Amazon Verified Permissions where that is the deployment form); Styra Declarative Authorization Service; OpenFGA; Casbin (where the estate already standardises on it).

### Workload identity (SPIFFE-compatible) {#a-5-5-4}

Category: workload identity issuers and meshes that can present SPIFFE IDs / SVIDs. SPIFFE itself is a standard and may appear in the spine; the products below are implementation options.

Examples of products in this category (non-exhaustive, not endorsed): SPIRE; Istio (SPIFFE-compatible identity); Linkerd; Consul Connect; cloud workload identity issuers that can mint SPIFFE-compatible identities for the broker's audience checks.

### Agent and tool gateways (protocol versus product) {#a-5-5-5}

Category: mediation gateways and MCP-related infrastructure that sit on the seam. MCP is a protocol and belongs in the spine as such; products that speak it are options here.

Examples of products and open projects in this category (non-exhaustive, not endorsed): self-built or in-house agent gateways conforming to this document's seam properties; MCP gateway / proxy implementations published by platform vendors and open-source projects; API management platforms used as a temporary outer shell only where they can inject authority rather than trust client-supplied claims. Prefer measuring against the six seam properties in chapter 8 over any product label.

### Evidence, immutable logging and SIEM {#a-5-5-6}

Category: tamper-evident or WORM-capable stores, integrity-preserving append paths, and SIEM / security analytics that ingest gateway session and evidence events. The evidence store in chapter 11 is a design role; SIEM is usually a downstream consumer, not a substitute.

Examples of products in this category (non-exhaustive, not endorsed): integrity-preserving object / ledger stores (for example Amazon QLDB-style ledgers, Azure confidential ledger, or equivalent WORM object locks); enterprise SIEM platforms (Splunk; Microsoft Sentinel; Elastic Security; Chronicle / Google Security Operations); open-source append and verification stacks built on signed hash chains with external checkpoints.

### Systems of record (insurance and adjacent cores) {#a-5-5-7}

Category: core claims, policy and billing systems that agents call as tools. The spine uses “claims system of record” and similar category language; Borealis’s failure to offer token exchange is a property of that category cell, not of one SKU.

Examples of products in this category (non-exhaustive, not endorsed): Guidewire InsuranceSuite; Duck Creek; Sapiens; Majesco; in-house or regional core platforms. Treat any of them as a tool that either joins token exchange or forces the custodian path in chapter 8.

### Hosted model providers {#a-5-5-8}

Category: providers of pinned hosted model strings subject to vendor deprecation calendars. Citations in References may name publishers of specifications and deprecation notices; the spine itself keeps to the category.

Examples of products in this category (non-exhaustive, not endorsed): OpenAI API model catalogue; Anthropic API model catalogue; Google Gemini / Vertex AI model catalogue; Amazon Bedrock model catalogue; open-weight models operated inside the estate under the same pin-and-revalidate discipline.
