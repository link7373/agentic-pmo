# Method: Metrics & Experimentation

Metrics tell us whether the product is creating value and whether our bets are working. Experimentation lets
us learn causally and cheaply before committing. Measure **outcomes** (changes in user/business behavior),
not just **output** (things shipped). A few well-chosen metrics beat a dashboard nobody reads.

## North Star metric
A single metric that best captures the value customers get from the product (e.g., weekly active teams
completing the core action). It aligns the org and sits above supporting input metrics that teams can move.
Pair it with **guardrail metrics** so you don't optimize the North Star at the expense of health (quality,
churn, cost, trust).

## The metrics tree
North Star → input metrics (the few levers that drive it) → team/feature metrics. Each team should know
which input metric they move and how it rolls up. This keeps local work tied to the outcome that matters.

## AARRR (pirate metrics) — the funnel
- **Acquisition** — users arrive.
- **Activation** — first valuable experience ("aha" / time-to-value).
- **Retention** — they come back; the truest signal of value.
- **Referral** — they bring others.
- **Revenue** — they pay.
Find the biggest leak in the funnel and fix that first.

## Value & evidence-based measurement
Track value across complementary dimensions:
- **Current value** — value delivered to users/business *today*.
- **Unrealized value** — the gap to the full opportunity (room to grow).
- **Time to market** — how fast you can deliver new value (responsiveness).
- **Ability to innovate** — capacity not lost to technical debt, overhead, or low-value work.
Manage by evidence: form a hypothesis, run a small experiment, measure, decide — repeat.

## Metric hygiene
- **Actionable, not vanity** — a metric you can't act on (or that always goes up) doesn't guide decisions.
- **Ratios/rates over raw counts** where they normalize for growth (conversion %, retention curve).
- **Leading vs. lagging** — pair fast leading indicators with slower lagging outcomes.
- **Segment** — averages hide truth; look by cohort, segment, and over time (retention curves, cohort tables).
- **Counter-metrics** — for every target metric, watch what it might harm (Goodhart's law: a metric pushed too
  hard stops being a good metric).

## Experimentation
- **A/B test** when you have enough traffic and a clear single change; randomize, define the primary metric
  and the minimum detectable effect, run to significance, and watch guardrails.
- State the **hypothesis** and success threshold before running (see `discovery-and-validation.md`).
- For low traffic, prefer qualitative tests, painted-door/fake-door tests, or holdouts over underpowered A/Bs.
- Beware peeking (stopping early when it looks good), novelty effects, and unrepresentative samples.

## Instrumentation
Decide what to measure *before* launch and instrument it as part of the work, not after. Define each event
and metric precisely (a shared metrics catalog) so numbers mean the same thing to everyone.

## Quality checklist
- [ ] A clear North Star with guardrail/counter-metrics; teams know their input metric.
- [ ] Metrics are actionable and segmented, not vanity averages.
- [ ] Experiments state hypothesis + success threshold up front and respect significance.
- [ ] Instrumentation is planned before launch; definitions are shared and consistent.

## Related methods
- [[lean-product-process]] · [[discovery-and-validation]] · [[product-strategy]] · [[launch-and-gtm]]
