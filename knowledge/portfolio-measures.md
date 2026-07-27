# Portfolio Measure Catalog

> **The single definition of every portfolio measure.** Owned by `portfolio-analyst`. No measure appears on a
> dashboard, in a portfolio report, or in a deliverable unless it is defined here, and it is computed exactly as
> defined here. Changing an in-use definition is a breaking change — version it and log it in
> `knowledge/decision-log.md`, because every surface that uses it changes meaning the same day.
>
> Names in this file are a **contract**. A build implements them character for character; a name that drifts
> between here and a dashboard is a defect, not a variation.

## Reported measure set
_The fixed set that appears on the portfolio surfaces. Additions and removals go through `portfolio-analyst`._

| Measure | Cadence | Target | 🟢 | 🟡 | 🔴 |
|---------|---------|--------|----|----|----|
|         |         |        |    |    |    |

---

## Definitions

> One entry per measure, using the full template. A stranger must be able to compute the measure from its entry
> alone — if they'd have to ask you a question, the entry isn't finished.

### <Measure_Name>

- **Status:** <draft | ratified> (v<1>, <YYYY-MM-DD>)
- **Plain-English definition:** <what it means, in a sentence a sponsor would accept>
- **Exact formula:** <the computation, unambiguously — including the filter and the period>
- **Source:** <`knowledge/portfolio.md` register field, or the cycle artifact it comes from>
- **Grain / valid segments:** <e.g. "one project per reporting month; valid by program, sponsor, delivery
  approach; NOT valid by team — capacity draw is not team-attributed at project level">
- **Owner:** <who is accountable for the definition>
- **Target / threshold:** <value, and where it came from>
- **Measured or estimated:** <say which. Never let an estimate be read as measured.>
- **Known limitations:** <what it excludes, where it misleads>
- **Change history:** <YYYY-MM-DD: created>

### <Measure_Name_2>

- (same template)

---

## Candidate measures
_Common portfolio measures, listed as starting points only. Nothing here is active until it has a full
definition above — a name without a definition is exactly the ambiguity this file exists to prevent._

**Delivery** — milestone hit rate · schedule variance · SPI · throughput · cycle time from approval to delivery
**Financial** — cost variance · CPI · estimate at completion · spend by strategic theme
**Risk** — open risk count by severity · aging issues · overdue mitigations · concentration of risk
**Capacity** — demand vs. supply by role · collision count · portfolio WIP · items in flight vs. limit
**Strategic alignment** — investment share per goal · count of items with no strategic link
**Data health** — submission completeness rate · submission currency rate · items at low or missing confidence

Definitions and thresholds for these live in `knowledge/methods/portfolio-management.md`; the numbers they
resolve to for this portfolio belong above.

## Deprecated / renamed measures

| Old name | Replaced by | Date | Why |
|----------|-------------|------|-----|
|          |             |      |     |

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
