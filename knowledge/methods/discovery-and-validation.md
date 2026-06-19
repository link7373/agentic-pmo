# Method: Discovery & Validation

Discovery is how we reduce the risk of building the wrong thing. We turn assumptions into hypotheses and
test them with evidence from real customers before committing significant build effort. Validation is
continuous, not a one-time gate.

## Assumptions → hypotheses → tests

1. List the assumptions your product/feature depends on (value, usability, feasibility, viability).
2. Rank by **risk** = (impact if wrong) × (uncertainty). Attack the riskiest first.
3. Reframe each risky assumption as a falsifiable **hypothesis**:
   > We believe **[customer]** will **[behavior/outcome]** because **[reason]**.
   > We'll know we're right when we see **[measurable signal]**.
4. Choose the cheapest test that produces a real signal; define the success threshold *before* testing.

## Four big product risks
- **Value risk** — will customers want it / pay for it?
- **Usability risk** — can they figure out how to use it?
- **Feasibility risk** — can we build it with our tech/time?
- **Viability risk** — does it work for the business (legal, cost, GTM, support)?

## Customer interviews

- Recruit real target customers; talk to enough to see patterns (often ~5–8 per segment reveal most usability
  issues; more for generative discovery).
- Ask about **past and present behavior**, not hypothetical futures ("Tell me about the last time you…"
  beats "Would you use…").
- Avoid leading questions; stay silent and let them talk; dig into the *why* behind answers.
- Separate the **problem interview** (is the problem real and painful?) from the **solution interview**
  (does our approach resonate?).

## Jobs To Be Done (JTBD)

Frame needs as the "job" a customer hires a product to do:
> When **[situation]**, I want to **[motivation]**, so I can **[expected outcome]**.

Jobs are stable over time even as solutions change. Capture functional, emotional, and social dimensions.
JTBD prevents anchoring on the current solution and surfaces the real outcome customers seek.

## Personas

Built from research, a persona summarizes a target segment: goals, context, behaviors, pains, and the jobs
they're trying to get done. Keep them behavior-based and evidence-backed — avoid demographic stereotypes.
Use them to keep the team aligned on *who* we serve and to evaluate decisions ("Would this help [persona]?").

## Opportunity Solution Tree

A visual map connecting outcome → opportunities → solutions → experiments:
- **Desired outcome** at the root (tied to a goal/OKR).
- **Opportunities** (customer needs/pains/desires discovered in research) as branches.
- **Solutions** under each opportunity.
- **Experiments** under each solution to validate it.

It keeps discovery outcome-driven, makes the opportunity space explicit, and forces comparison of multiple
solutions before committing.

## Validation signals (strongest → weakest)
1. Customers pay / commit real resources.
2. Customers use it repeatedly (retention/behavior).
3. Customers complete the key task in a test.
4. Customers say they want it (weakest — discount stated intent).

## Sources of validation evidence
- **Stakeholder feedback** — sponsors, internal experts, support, sales (context and constraints).
- **Marketplace feedback** — real usage data, analytics, A/B tests, sales/retention (the strongest signal).

## Quality checklist
- [ ] Riskiest assumption identified and tested first.
- [ ] Each hypothesis is falsifiable with a pre-stated success threshold.
- [ ] Evidence comes from real target customers and observed behavior, not just opinions.
- [ ] Needs captured as jobs/outcomes, not features.
- [ ] Multiple solutions considered per opportunity before committing.

## Related methods
- [[lean-product-process]] · [[metrics-and-experimentation]] · [[requirements-and-stories]] · [[product-strategy]]
