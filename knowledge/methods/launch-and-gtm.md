# Method: Launch & Go-To-Market

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

A launch turns a built product into adopted value. Launch is a cross-functional event — product,
engineering, marketing, sales, support, and operations must be ready together. The goal isn't just to
ship; it's to drive **adoption** of value and to learn from real-world use.

## Release vs. launch
- **Release** — making the software available (technical deployment).
- **Launch** — the coordinated go-to-market motion that drives awareness, adoption, and feedback.
You can release without launching (silent/dark release) and launch without a same-day release (pre-announce).

## Lifecycle phases & gate reviews

Bringing a product to market is a staged journey, each stage ending in a **gate review** — an explicit
go/kill/hold/recycle decision before committing the next round of investment:

**Conceive → Plan → Develop → Qualify → Launch → Deliver → Retire**

- **Conceive** — identify and screen the opportunity; preliminary business case.
- **Plan** — define the product, roadmap, business case, and launch/marketing strategy.
- **Develop** — build, refine requirements, validate with the market (alpha/beta), detail the launch plan.
- **Qualify** — beta/market test, confirm launch readiness, make the final launch decision.
- **Launch** — execute go-to-market; run the launch and immediate post-launch activities.
- **Deliver** — manage the product through growth, maturity, and decline.
- **Retire** — sunset deliberately with an end-of-life plan.

Gates prevent good money chasing weak concepts; make the criteria explicit and honor a "kill" as a valid outcome.

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

## Positioning & messaging platform

Before the campaign, agree the message once so every channel is consistent. A messaging platform captures:
- **Target audience & the job/pain** it addresses.
- **Positioning statement** (see `product-strategy.md`) and the **value proposition**.
- **Key messages** — 3–4 proof-backed claims, laddering benefit → feature → evidence.
- **Differentiators** vs. the main alternatives, and the objections to pre-empt.
- **Proof points** — data, customers, demos that make claims believable.
Everything downstream (site, sales deck, PR, ads, release notes) inherits from this single source.

## Market type shapes the launch

The launch strategy depends on the market you're entering: a **new/unknown category** needs education and
demand *creation* (teach the problem before selling the product); an **existing category** needs sharp
differentiation and demand *capture*; a **resegmented** play leads with the niche or the price/positioning
wedge. Don't run an existing-market playbook into a category that doesn't know it has the problem yet.

## Demand generation & channel enablement

Adoption needs a pipeline, not just an announcement:
- **Demand generation** — the plan to create awareness and interest (content, PR/analyst relations, events,
  paid/organic) sized to the launch tier.
- **Sales & channel enablement** — equip whoever sells or onboards: positioning, demo, pricing/packaging,
  objection handling, and training — ready *before* launch day, not after.
- **Support & success readiness** — docs, FAQs, and escalation paths so early adopters don't churn on friction.

## Rollout & monitoring
- Define **success metrics and guardrail metrics** before launch (adoption, activation, error rate, latency,
  support volume). Decide the thresholds that mean "expand," "hold," or "roll back."
- Monitor closely during the rollout window; keep rollback cheap and rehearsed.
- Run a **post-launch review**: did we hit the success metrics? what did we learn? what's next?

## Change management (for internal/enterprise rollouts)
- Communicate the *why*, train users, stage the change, and support the transition; adoption is a behavior
  change, not just an availability change.

## End-of-life / retirement

Retiring a product is a managed launch in reverse. Plan the sunset: notify and migrate customers, set the
support wind-down timeline, handle data export/retention and contractual/regulatory obligations, brief sales
and support, and capture the lessons learned. A deliberate end-of-life protects trust and frees capacity for
the next bet; a neglected one erodes both.

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
- [ ] Phase gates have explicit go/kill criteria; a "kill" is treated as a valid outcome.
- [ ] Messaging platform agreed once; launch strategy matches the market type; enablement ready before launch day.

## Related methods
- [[roadmapping]] · [[project-management]] · [[metrics-and-experimentation]] · [[product-strategy]]
