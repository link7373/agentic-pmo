---
name: define-metrics
description: Define product metrics precisely — north star, input metrics and guardrails, exact formulas with denominators and segments, named funnels, and honest instrumentation gaps. Use before measuring a launch or OKR, or when two teams disagree about what a number means. Dispatches the product-analyst.
---

# /define-metrics — Make the numbers mean one thing

## When to use
Before a launch or an OKR cycle needs measuring; when a metric is being quoted with two different values; when
an experiment needs a primary metric and guardrails agreed before it starts.

## Dispatches
`product-analyst` (lead) + `product-strategist` (which outcomes matter) + `product-manager` (what the feature
is supposed to change).

## Inputs
`knowledge/metrics.md` (existing catalog), `knowledge/product-context.md` (goals/OKRs),
`knowledge/prds/`, launch plans in `knowledge/launches/`, `knowledge/portfolio-measures.md` (to avoid
colliding with a delivery measure).

## Steps
1. **Tie every metric to a goal or OKR.** A metric that serves nothing gets deleted, not defined — the catalog
   is only useful if it stays small.
2. **Propose the north star with its guardrails.** A single optimizing metric without counter-metrics reliably
   produces the wrong behavior; name what must *not* degrade while it improves.
3. **Define precisely enough that a stranger could compute it** — the event, the numerator and denominator,
   the filters, the period, and which segments the metric is and is not valid across. Ambiguity here is what
   produces two numbers for one name.
4. **Name the funnels.** A "conversion rate" means nothing until the step sequence and window are fixed.
5. **Say measured or estimated, and name the limitations** — what it excludes, where it misleads, what
   instrumentation it depends on.
6. **Check the boundary.** Product metrics live here; delivery measures (SPI, CPI, milestone hit rate) live in
   `knowledge/portfolio-measures.md`. Never define the same thing in both — if a dashboard needs a product
   metric, it cites this catalog rather than restating it.
7. **Record instrumentation gaps honestly.** Metrics you want but cannot currently measure belong in the gaps
   table, with the proxy in use if any. Being explicit here is what stops a proxy quietly becoming the truth.

## Methods
`knowledge/methods/metrics-and-experimentation.md` (north star, metrics tree, hygiene, experiment design),
`knowledge/methods/product-strategy.md` (outcomes and OKRs),
`knowledge/methods/lean-product-process.md` (build-measure-learn).

## Output
Updated `knowledge/metrics.md` — north star and input metrics, full definitions, funnels, experiment index,
instrumentation gaps. Reflect success measures into `knowledge/product-context.md`. Changing a definition
already in use is a breaking change: version it and log it in `knowledge/decision-log.md`. Follow
`standards/document-standards.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
