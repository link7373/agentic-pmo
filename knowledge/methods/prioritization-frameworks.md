# Method: Prioritization Frameworks

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

Prioritization allocates scarce capacity to the work that creates the most value per unit of effort, in
service of the current strategy/goals. No framework replaces judgment — they make trade-offs explicit and
debatable. Pick the framework that fits the decision; always tie scores back to a goal.

## RICE

Score each item and rank by the RICE score:

```
RICE = (Reach × Impact × Confidence) / Effort
```

- **Reach** — how many users/events in a period (e.g., users/quarter).
- **Impact** — effect per user on the goal (massive 3 / high 2 / medium 1 / low 0.5 / minimal 0.25).
- **Confidence** — how sure you are of the estimates (100% / 80% / 50%); guards against hype.
- **Effort** — person-time (e.g., person-months).

Best for comparing many features against a single goal. Keep estimates honest; confidence penalizes guesswork.

## WSJF (Weighted Shortest Job First)

For sequencing under limited capacity, maximize value delivered per unit time:

```
WSJF = Cost of Delay / Job Duration (size)
Cost of Delay = User/Business value + Time criticality + Risk reduction / Opportunity enablement
```

Score components on a relative scale (e.g., modified Fibonacci 1,2,3,5,8,13,20). Do the highest-WSJF job
first. Best for a flow of similarly-framed initiatives where timing matters.

## Kano model

Classify features by how they affect satisfaction:
- **Basic (must-be)** — expected; absence causes dissatisfaction, presence is neutral. Table stakes.
- **Performance (linear)** — more is better; satisfaction scales with how well you do it.
- **Delighters (exciters)** — unexpected; presence delights, absence isn't missed. Source of differentiation.
- **Indifferent / Reverse** — no effect, or actively unwanted.

Delighters decay into expectations over time. Cover basics fully, compete on performance, sprinkle
delighters. Survey by asking the functional/dysfunctional question pair per feature.

## Value vs. Effort (2×2)

Plot items by value (y) and effort (x):
- **High value / low effort** → quick wins, do first.
- **High value / high effort** → big bets, plan deliberately.
- **Low value / low effort** → fill-ins / maybes.
- **Low value / high effort** → avoid.

Fast and intuitive for small lists and workshops.

## MoSCoW

Sort scope into **Must / Should / Could / Won't (this time)**. Excellent for release/sprint scope and
stakeholder negotiation. Keep "Must" genuinely minimal — if everything is a Must, nothing is prioritized.
"Won't this time" makes deferrals explicit and reduces churn.

## Weighted scoring (custom)

When multiple criteria matter, define criteria with weights (e.g., strategic fit 30%, revenue 25%, reach 20%,
effort 15%, risk 10%), score each item per criterion, and compute the weighted total. Transparent and
tunable, but only as good as the weights — agree on them up front.

## Prioritization bases (what to weigh)

Whatever framework you use, the underlying factors that move priority are consistent — weigh them explicitly:
- **Business/customer value** — benefit to the outcome or goal.
- **Cost / effort** — the investment required.
- **Risk** — do risky, uncertain, or foundational items early to learn or de-risk (or defer if avoidable).
- **Dependencies** — enablers must precede the work they unblock; sequence accordingly.
- **Time sensitivity** — deadlines, market windows, seasonality, cost of delay.
- **Regulatory / policy** — compliance and contractual obligations can override pure value scoring.

## Choosing a framework
- Many features, one goal → **RICE**.
- Sequencing a flow where timing matters → **WSJF**.
- Designing the feature mix / satisfaction strategy → **Kano**.
- Quick workshop triage → **Value/Effort 2×2**.
- Scoping a release with stakeholders → **MoSCoW**.
- Multi-criteria strategic calls → **Weighted scoring**.

## Practices
- Always state which goal/OKR the score serves; deprioritize anything that doesn't ladder up.
- Record assumptions and confidence; revisit when evidence changes.
- Beware HiPPO (highest-paid person's opinion) overriding the model without new evidence — log the rationale.

## Quality checklist
- [ ] Framework matches the decision type.
- [ ] Every item is tied to a goal/OKR.
- [ ] Estimates include confidence; assumptions recorded.
- [ ] Output is a ranked, defensible order — not a flat wish list.

## Related methods
- [[lean-product-process]] · [[roadmapping]] · [[agile-scrum-mechanics]] · [[product-strategy]] · [[business-analysis]]
