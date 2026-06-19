# Method: Lean Product Process (Achieving Product-Market Fit)

Product-market fit means you've built something a well-defined group of customers genuinely needs and
values. The lean approach reaches fit through a disciplined sequence and tight build-measure-learn loops,
minimizing wasted effort on the wrong product.

## Problem space vs. solution space

- **Problem space** = the customer's needs, problems, and desired outcomes — independent of any solution.
- **Solution space** = any specific product, feature, design, or technology that addresses them.

Always define the problem before jumping to a solution. Most product failures are solutions to problems
nobody urgently has, or the wrong solution to a real problem. Validate the problem first.

## The product-market fit pyramid (bottom → top)

1. **Target customer** — the specific segment you serve.
2. **Underserved needs** — the customer needs that are important but poorly met today.
3. **Value proposition** — how your product meets those needs better than alternatives.
4. **Feature set** — the specific capabilities that deliver the value proposition (your MVP).
5. **UX** — how those features are made usable and delightful.

The bottom three are **problem space + strategy**; the top two are **solution space**. Lower layers are the
foundation — fix problems there before polishing layers above.

## The six-step process

1. **Determine your target customer.** Segment the market; pick a beachhead. Build personas grounded in real
   attributes and behaviors, not demographics alone (see `discovery-and-validation.md`).
2. **Identify underserved needs.** Enumerate the customer's needs as outcomes. Score each on **importance**
   (how much the customer cares) and **satisfaction** (how well current solutions deliver). The biggest
   opportunities are **high-importance, low-satisfaction** needs. *Opportunity ≈ importance + (importance − satisfaction).*
3. **Define your value proposition.** Decide which underserved needs you'll address and how you'll beat
   alternatives on them. Be explicit about the needs you will *not* serve well — focus creates differentiation.
4. **Specify your MVP feature set.** The smallest set of features that delivers the core value and lets you
   test the value proposition with real customers (see "MVP scoping" below).
5. **Create your MVP prototype.** Make the value tangible at the cheapest fidelity that yields a real signal —
   from clickable mockups to a thin working slice.
6. **Test the MVP with customers.** Put it in front of target customers, observe behavior, gather feedback,
   measure. Then **iterate or pivot** based on evidence.

## Importance vs. satisfaction (opportunity scoring)

Plot needs on a 2×2 of importance (y) vs. satisfaction (x):
- **High importance / low satisfaction** → prime opportunity. Build here.
- **High importance / high satisfaction** → table stakes; match, don't over-invest.
- **Low importance** → ignore regardless of satisfaction.

Relate to Kano (see `prioritization-frameworks.md`): underserved important needs are where delighters and
strong performance features live.

## MVP scoping

- **Minimum** and **Viable** are in tension — hold both. Cut scope aggressively, but the slice must still
  deliver real value and produce a valid learning signal.
- Define MVP scope as a **hypothesis to test**, with explicit success criteria, before building.
- Prefer the cheapest experiment that reduces the biggest risk (concierge, Wizard-of-Oz, landing page,
  prototype) before writing production code.
- Guard scope ruthlessly: every added feature delays the learning and dilutes the signal.

## Build–measure–learn

Run tight loops: ship the smallest increment → measure real behavior against your hypothesis → learn →
decide. Minimize cycle time; the team that learns fastest wins. Persevere when evidence supports the
hypothesis; **pivot** when evidence demands it (change target, problem, or solution while preserving learning).

## Quality checklist
- [ ] Problem validated before solution committed.
- [ ] Target customer is specific; needs are framed as outcomes and scored on importance × satisfaction.
- [ ] Value proposition names the needs served *and* deliberately not served.
- [ ] MVP is the smallest slice that still delivers value and tests a clear hypothesis with success criteria.
- [ ] Each loop ends in an explicit persevere/iterate/pivot decision logged with evidence.

## Related methods
- [[discovery-and-validation]] · [[product-strategy]] · [[prioritization-frameworks]] · [[metrics-and-experimentation]] · [[requirements-and-stories]]
