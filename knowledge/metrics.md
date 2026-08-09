# Product Metric Catalog

> **The single definition of every product and outcome metric.** Owned by `product-analyst`. Maintained by
> `/define-metrics`; used by `/review-okrs`, `/write-prd`, `/plan-launch`, and any experiment.
>
> **Boundary with `knowledge/portfolio-measures.md`:** this file defines *product* metrics — activation,
> retention, conversion, north star, guardrails. That file defines *portfolio delivery* measures — SPI, CPI,
> milestone hit rate, capacity. They never define the same thing twice. When a dashboard surfaces a product
> metric, the measure catalog **cites the definition here** rather than restating it; if the two ever disagree,
> this file wins for product metrics and that file wins for delivery measures.
>
> Names here are a contract, same as in the measure catalog. Changing a definition that's already in use is a
> breaking change — version it and log it in `knowledge/decision-log.md`.

_Last reviewed: —_

## North star & input metrics
| Metric | Role (north star / input / guardrail) | Current | Target | Cadence | Owner |
|--------|---------------------------------------|---------|--------|---------|-------|
|        |                                       |         |        |         |       |

---

## Definitions

> One entry per metric. A stranger must be able to compute it from the entry alone.

### <Metric_Name>

- **Status:** <draft | ratified> (v<1>, <YYYY-MM-DD>)
- **Plain-English definition:** <what it means, in a sentence a stakeholder would accept>
- **Exact formula:** <numerator, denominator, filters, and the period>
- **Source:** <the event, table, or instrument it comes from>
- **Grain / valid segments:** <what you may and may not slice it by, and why>
- **Owner:** <who is accountable for the definition>
- **Target / threshold:** <value, and where it came from>
- **Measured or estimated:** <say which>
- **Known limitations:** <what it excludes, where it misleads, known instrumentation gaps>
- **Change history:** <YYYY-MM-DD: created>

### <Metric_Name_2>

- (same template)

---

## Funnels
_Named step sequences, so a "conversion rate" always means the same steps._

| Funnel | Steps (in order) | Window | Owner |
|--------|------------------|--------|-------|
|        |                  |        |       |

## Experiments
_Live and recent tests. Full design lives in the experiment artifact; this is the index._

| Experiment | Hypothesis | Primary metric | Guardrails | Status | Started | Result |
|------------|------------|----------------|------------|--------|---------|--------|
|            |            |                |            |        |         |        |

## Instrumentation gaps
_Metrics we want but cannot currently measure. Being explicit here prevents a proxy quietly becoming the truth._

| Wanted metric | Why we can't measure it | Proxy in use (if any) | What it would take | Owner |
|---------------|-------------------------|-----------------------|--------------------|-------|
|               |                         |                       |                    |       |

## Deprecated / renamed metrics
| Old name | Replaced by | Date | Why |
|----------|-------------|------|-----|
|          |             |      |     |

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
