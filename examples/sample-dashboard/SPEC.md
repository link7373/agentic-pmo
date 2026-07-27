# Dashboard Spec: Portfolio_Sample
Tier: tactical   ·   Owner: portfolio-analyst   ·   Date: 2026-07-27
Status: built   ·   Target platform: Power BI

> Illustrative. This is what `/design-dashboard` produces from `templates/dashboard-spec.md`, and what
> `/powerbi` then builds. Fictional data; the live PMO reads from `knowledge/`, not `examples/`.

## The questions this surface answers

1. Is the portfolio delivering to plan, and is that getting better or worse?
2. Which program is drawing the most capacity?
3. Can we trust this month's numbers?

Three questions, deliberately. A fourth would mean a second dashboard.

## Decisions this surface must support

| Decision | Who makes it | How often | What they need to see |
|----------|--------------|-----------|----------------------|
| Re-sequence or defer work | program-manager | Monthly | Capacity demand by program; SPI trend |
| Escalate a project | portfolio-analyst → sponsor | Monthly | Milestone hit rate per project; RAG vs. trend divergence |
| Whether to act on this report at all | leadership | Monthly | Data Confidence Rate |

## Audience & scope
- **Primary:** portfolio and delivery leads.  **Secondary:** program-manager.
- **In scope:** in-flight and approved items, six trailing monthly periods.
- **Out of scope:** individual performance, task-level detail, financial forecasting beyond CPI.

## Semantic model

**Grain:** one row per project per reporting month. Star schema, one date table.

| Table | Fact / dimension | Grain | Source | Key fields | Refresh |
|-------|------------------|-------|--------|-----------|---------|
| `Fact_Status` | fact | project × month | register + cycle artifacts | `Project_Id`, `Report_Month` | monthly |
| `Project` | dimension | one per item | `knowledge/portfolio.md` | `Project_Id` | on change |
| `Date` | dimension | one per day, 2026 | generated | `Date` | static |

**Relationships** — single-direction only:

| From | To | Cardinality | Direction | Justification if bidirectional |
|------|----|-------------|-----------|-------------------------------|
| `Fact_Status.Project_Id` | `Project.Project_Id` | many-to-one | single | — |
| `Fact_Status.Report_Month` | `Date.Date` | many-to-one | single | — |

## Measure catalog

Names are the contract; the build implements them character for character. Ratios come from summed numerator and
denominator — never an average of ratios, which gives a wrong total row.

| Measure | Plain-English definition | Formula / logic | Format | Owner |
|---------|-------------------------|-----------------|--------|-------|
| `Milestone Hit Rate` | Share of milestones due in the period that were met | `DIVIDE(SUM(Milestones_Hit), SUM(Milestones_Due))` | 0.0% | portfolio-analyst |
| `SPI` | Schedule Performance Index; below 1.00 is behind | `DIVIDE(SUM(Earned_Value), SUM(Planned_Value))` | 0.00 | portfolio-analyst |
| `CPI` | Cost Performance Index; below 1.00 is over budget | `DIVIDE(SUM(Earned_Value), SUM(Actual_Cost))` | 0.00 | portfolio-analyst |
| `Projects Reporting` | Distinct projects that submitted | `DISTINCTCOUNT(Project_Id)` | 0 | portfolio-analyst |
| `Capacity Demand FTE` | Total capacity drawn, in FTE | `SUM(Capacity_Demand_Fte)` | 0.0 | portfolio-analyst |
| `Data Confidence Rate` | Share of submissions at High or Medium confidence | `DIVIDE(CALCULATE(COUNTROWS(), Confidence IN {"High","Medium"}), COUNTROWS())` | 0.0% | portfolio-analyst |

**Ambiguity notes:** "on track" is deliberately **not** a measure here — it would need a threshold nobody has
agreed. RAG is a stored submitted value, not derived, so the surface can show where a submitted RAG disagrees
with the trend. That divergence is the point of question 1.

## Pages & layout

> Names use letters, digits and underscores only. Spaces are silently discarded by Desktop, taking the object
> with them, and a later rename breaks any drill path pointing at it.

### Page 1: `Portfolio_Overview`
- **Answers:** questions 1 and 2.
- **Visuals:** `Milestone_Hit_Rate_Card`, `SPI_Card`, `CPI_Card`, `Projects_Reporting_Card` (KPI band, most
  important top-left) · `Milestone_Hit_Rate_Trend` (line, by month) · `Capacity_Demand_By_Program` (column).
- **Filters / slicers:** none in the sample; production adds period and program, defaulted to the latest
  complete period and all programs.
- **Empty state — intent, untested:** a card should read blank rather than zero when no submissions exist. Blank
  says "nothing reported"; zero claims "reported as none", which is a different and wrong statement. `DIVIDE`
  returns blank on a zero denominator so the ratio measures should behave; `Projects Reporting`
  (`DISTINCTCOUNT`) may return 0 instead. **Worth checking when you test the empty state** — and if it returns
  zero, that's a real defect in the spec, not a cosmetic one.

### Page 2: `Delivery_Detail`
- **Answers:** question 3, and question 1 per project.
- **Visuals:** `Data_Confidence_Rate_Card` · `SPI_By_Project` (column) · `Capacity_Demand_By_Manager` (column).

**Visual design** follows `standards/dashboard-standards.md`: length and position over area, bars from zero, grey
default with colour as the highlight, no borders or backgrounds. Palette, status colours and typography are set
**once** in the theme, not per visual.

## Drill paths

| From | To | Passes context | Purpose |
|------|----|----------------|---------|
| `Capacity_Demand_By_Program` | `Delivery_Detail` | selected program | Which projects and managers make up that demand |
| `Milestone_Hit_Rate_Trend` | `Delivery_Detail` | selected month | Which projects drove the change |

_Not implemented in the sample — cross-page drillthrough needs a drillthrough filter on the target page. Called
out here because an aggregate the reader can't trace back is the gap this section exists to close._

## Data confidence display
`Data_Confidence_Rate_Card` on page 2. Production should also badge any visual whose aggregate includes
low-confidence rows — a number built from three doubtful submissions must say so on the surface.

## Refresh, lineage & access
- **Refresh:** monthly, after `/review-portfolio-intake` closes the cycle. Never before the gate.
- **Data as-of:** shown in the page header in production; the sample has static inline data.
- **Lineage:** `knowledge/portfolio.md` → cycle artifact in `knowledge/portfolio/` → model → surface.
- **Access:** tactical tier — portfolio and delivery leads. The leadership rollup is a separate surface.
- **Failure behaviour:** a failed refresh must leave the as-of date visibly stale, never silently serve old
  numbers as current.
- **Publishing:** portfolio-analyst may publish to the delivery workspace. Anything wider is the user's call.

## Privacy
- Default filter state is impersonal. Saved filter and slicer selections persist into `visual.json` and then into
  git — a visual left filtered to a named manager commits that name.
- `Manager` appears on page 2 to attribute **capacity draw**, so load can be rebalanced. This surface reports the
  health of work, not the performance of people.
- Sample names (`M_Alvarez`, `R_Okafor`, `T_Nguyen`, `A_Sponsor`…) are invented.

## Handoff
- **Build route:** `/powerbi` (in-kit).
- **Capability tier available:** full project authoring — Power BI Desktop plus Python 3.12.
- **Project location:** `examples/sample-dashboard/Portfolio_Sample/`. Real surfaces go in `dashboards/`.
- **Not done until:** it renders in Desktop, every number reconciles, and the empty state and a single-category
  filter are tested. **Validation only proves the files are well-formed.**
- **Open questions blocking the build:** none.

## Build log
| Date | What changed | Validated clean | Reconciled | By |
|------|--------------|-----------------|-----------|----|
| 2026-07-27 | Initial build, 2 pages, 9 visuals, 6 measures | ✅ 0 errors (2 expected `.platform` warns) | ⬜ card totals computed from source; **not** read off a rendered report | portfolio-analyst |
| 2026-07-27 | **Fix:** `Date` partition failed to load — `Date.ToText` rejects a `datetime`. All partitions rewritten as pure literals computed upstream in Python; no Power Query expression is evaluated now. | ✅ 0 errors | ✅ 365 contiguous rows and all 12 month labels verified programmatically | portfolio-analyst |
| 2026-07-27 | **Rendered and reconciled in Power BI Desktop.** Both pages render, model refreshes, all five card values match the computed source. `lineChart` roles confirmed. | ✅ 0 errors | ✅ read off the rendered report and matching | repo owner |
| | Date table marked as date table | ⬜ | ⬜ | _pending — do this in Desktop_ |

**Lesson worth keeping:** the validator is a *static* checker — it never executes M, so a partition that cannot
load passes validation cleanly. That is the same "validation is not rendering" gap the standards insist on,
showing up in the data layer rather than the report layer. Computing upstream instead of in Power Query removes
the risk rather than testing for it.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
