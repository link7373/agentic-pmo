# Portfolio Register

> The canonical record of every project and program, on one comparable basis. Owned by `portfolio-analyst`;
> refreshed by `/track-portfolio` and quality-gated by `/review-portfolio-intake`. Sequencing decisions made on
> this data belong to `program-manager`. Schema and rules in `knowledge/methods/portfolio-management.md`.

## Register
_One row per project or program. Programs roll up their children; children name their parent. Never invent a
value to fill a cell — leave it blank and record the gap in **Data gaps** below._

| ID | Name | Type | Parent | Sponsor | Manager | Stage | Strategic link | Approach | Scope | Schedule | Cost | Next milestone | Due | RAG | Reason | Action | Top risk / dependency | Updated | Conf. |
|----|------|------|--------|---------|---------|-------|----------------|----------|-------|----------|------|----------------|-----|-----|--------|--------|----------------------|---------|-------|
|    |      |      |        |         |         |       |                |          |       |          |      |                |     |     |        |        |                      |         |       |

**Type:** project · program  ·  **Stage:** idea · assessed · approved · in-flight · closed · benefits-review
**Approach:** predictive · adaptive · hybrid  ·  **Scope / Schedule / Cost:** 🟢 on plan · 🟡 at risk · 🔴 breached

## Data confidence key
| Level | Meaning | How it's reported |
|-------|---------|-------------------|
| **High** | Complete, current, consistent | Used freely |
| **Medium** | Minor gaps or slightly stale | Used with a footnoted caveat |
| **Low** | Material gaps, stale, or contradictory | The gap is reported; not aggregated silently |
| **Missing** | No submission this cycle | Named in the report with its owner |

## Capacity summary
_Demand vs. supply per constrained team or role for the current cycle. Supply is a range, not a number.
Detail and scenarios live in the cycle artifact under `knowledge/portfolio/`._

| Team / role | Supply (range) | Demand | Variance | Constraint? | Notes |
|-------------|----------------|--------|----------|-------------|-------|
|             |                |        |          |             |       |

## Collisions & dependency clusters
_Two or more items needing the same scarce team in the same window, or dependency chains spanning several
items. These are invisible at project level — every colliding project is individually green._

| Items involved | Contended team / dependency | Window | Impact | Owner | Status |
|----------------|----------------------------|--------|--------|-------|--------|
|                |                            |        |        |       |        |

## Data gaps & chronic submitters
_Open gaps from the last intake review, by owner, with the specific ask. Chronic gaps are a portfolio risk —
escalate to `knowledge/raid-log.md` rather than absorbing them._

| Item | Owner | Missing / questioned | The ask | Cycles outstanding |
|------|-------|---------------------|---------|-------------------|
|      |       |                     |         |                   |

## Portfolio WIP
- **Items in flight:** _count_  ·  **Deliberate limit:** _set during `/setup-pmo` or a planning cycle_
- **Throughput:** _items completed per period — a more honest read than utilization._

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
