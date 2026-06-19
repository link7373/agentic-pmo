# Method: Launch & Go-To-Market

A launch turns a built product into adopted value. Launch is a cross-functional event — product,
engineering, marketing, sales, support, and operations must be ready together. The goal isn't just to
ship; it's to drive **adoption** of value and to learn from real-world use.

## Release vs. launch
- **Release** — making the software available (technical deployment).
- **Launch** — the coordinated go-to-market motion that drives awareness, adoption, and feedback.
You can release without launching (silent/dark release) and launch without a same-day release (pre-announce).

## Release strategies
- **Major / minor / functional releases** — size the release to the value and the audience's tolerance for change.
- **Phased rollout / rings** — internal → beta → % of users → general availability, watching health at each ring.
- **Feature flags / canary** — release to a small slice first; monitor; expand or roll back fast.
- **Dark launch** — ship inactive code to de-risk deployment, then enable behind a flag.
Choose the strategy that minimizes blast radius while still producing a real adoption/quality signal.

## Launch readiness checklist (cross-functional)
- **Product** — scope locked, acceptance criteria met, success metrics & instrumentation in place.
- **Engineering** — deploy/rollback plan, monitoring/alerts, performance & load validated, on-call ready.
- **Quality/Security** — testing complete; security/compliance/privacy sign-off where relevant.
- **Support** — docs, FAQs, known-issues, escalation path, team trained.
- **Marketing** — positioning, messaging, assets, announcement plan.
- **Sales/CS** — enablement, demo, pricing/packaging, objection handling (for relevant products).
- **Legal/Compliance** — terms, data handling, regulatory requirements addressed.
- **Go/No-Go** — named owner, decision criteria, and a clear rollback trigger.

## Launch tiers
Scale the motion to the impact: **Tier 1** (major, full GTM push) → **Tier 2** (notable, targeted) →
**Tier 3** (minor, release notes only). Don't over-invest launch effort on low-impact changes.

## Rollout & monitoring
- Define **success metrics and guardrail metrics** before launch (adoption, activation, error rate, latency,
  support volume). Decide the thresholds that mean "expand," "hold," or "roll back."
- Monitor closely during the rollout window; keep rollback cheap and rehearsed.
- Run a **post-launch review**: did we hit the success metrics? what did we learn? what's next?

## Change management (for internal/enterprise rollouts)
- Communicate the *why*, train users, stage the change, and support the transition; adoption is a behavior
  change, not just an availability change.

## GTM for early-stage / AI products
- Sequence by **stage**: idea → MVP → launch → scale, each with its own goal, challenges, and exit criteria.
- Don't scale GTM before product-market fit — premature scaling burns capital on an unproven motion.
- For AI products: set expectations about probabilistic behavior, build trust/safety messaging in, and
  instrument heavily to learn from real usage from day one.

## Quality checklist
- [ ] Release strategy minimizes blast radius and still yields a real signal.
- [ ] Cross-functional readiness verified; Go/No-Go owner and rollback trigger named.
- [ ] Success and guardrail metrics + thresholds defined *before* launch.
- [ ] Launch effort is tiered to impact.
- [ ] Post-launch review captures results and learnings.

## Related methods
- [[roadmapping]] · [[project-management]] · [[metrics-and-experimentation]] · [[product-strategy]]
