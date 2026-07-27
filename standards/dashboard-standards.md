# Standards: Dashboards

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

> Visual and structural rules for every dashboard the PMO ships, whatever the tool. Goal: any two PMO
> dashboards feel like siblings, and a new viewer gets the headline in five seconds. This is the **single
> source of truth for design** — `standards/powerbi-standards.md` covers Power BI mechanics only and does not
> restate anything here. Colour and cadence values below are sensible defaults; confirm or adjust them during
> `/setup-pmo`.

## Layout

- **Z-pattern hierarchy:** most important number top-left; KPI band across the top (≤6 numbers, each with a
  trend indicator and a comparison); trends and breakdowns in the middle; detail tables below the fold.
- **One dashboard, one job:** it answers the 1–3 named questions in its spec. A dashboard trying to serve
  everyone serves no one — split it instead.
- **Five-second test:** before shipping, look at it cold. Can you state the portfolio's condition in five
  seconds? If not, restructure.
- Max ~10–12 visuals per view. Filters grouped top or left, defaulted to the most common use — usually the
  latest complete period, all workstreams.

## Titles & annotation

- Chart titles state the **insight**, not the metric: "Milestone hit rate, monthly — three-period decline"
  beats "Milestone hit rate".
- Every chart shows the period covered and data freshness ("data through <date>"), with a source footnote where
  space allows.
- Targets and thresholds are drawn as reference lines, not described in tooltips only.
- **Never a bare RAG.** A status colour carries its reason and its action, on the surface — the rule from
  `standards/communication-standards.md` applies to pixels exactly as it does to prose.
- **Show data confidence.** A number aggregated from low-confidence or missing submissions must visibly say so;
  see the intake contract in `knowledge/methods/portfolio-management.md`.

## Charts — choosing

> Encode with the attributes the eye reads most accurately. **Length** (bars from a zero baseline) and
> **position** (dots, scatter) are the most precise — default to them. Colour-hue and shape are for
> *categories*; colour-intensity for sequential magnitude; **area and size are imprecise** (a 10× value looks
> about 3×) — use them only as a rough secondary encoding, never for the comparison that carries the message.
> One or two encodings per chart; more is noise.

| Need | Use | Avoid |
|---|---|---|
| Trend over time | Line (bars for few periods) | Area stacks > 3 series |
| Compare categories | Horizontal bar, sorted by value | Pie > 3 slices, 3-D anything |
| Part-of-whole over time | 100% stacked bar (≤ 4–5 parts) | Multiple pies |
| Two-metric relationship | Scatter | Dual axes (unless strongly justified and clearly labelled) |
| Single KPI status | Big number + sparkline + Δ | Gauges / speedometers |
| Actual vs target | Bullet graph (bar + target line + bands) | Gauges, a bare % with no context |
| Distribution | Histogram / box plot / jitter plot | Mean-only summaries of skewed data |
| "Where do we sit?" (one item vs peers) | Dot or jitter plot with quartile bands, marker highlighted | A bare ranking number |
| Rank over time | Bump chart | Spaghetti line chart of values |
| Schedule / milestones over time | Gantt or timeline with today-line | A table of dates with no visual span |

**Never use** (people read them wrong): pie or donut for comparison (angles and arcs aren't comparable — use
sorted bars), packed-bubble and radial or concentric bars (area and differing-radius arcs distort), word clouds
(size ≠ quantity), any 3-D chart (perspective distorts length). **Pie's one acceptable use:** a single KPI
showing progress to a fixed 100% target, with no cross-category comparison.

## Colour

> Consistent colour means consistent meaning across every PMO dashboard.

- **Brand palette:** primary `#2563EB`, neutral greys. Replace with the organization's palette during
  `/setup-pmo` if there is one.
- **Semantic status:** on track `#16A34A`, at risk `#D97706`, breached `#DC2626` — reserved for status only,
  never decoration. These are the pixel equivalents of 🟢 🟡 🔴 as used throughout `knowledge/`.
- Sequential data → single-hue ramps. **Diverging** (two hues from a meaningful midpoint — target, prior
  period, zero) only when that midpoint is real. Categorical → at most 6–7 distinguishable hues.
- **Colour-blind safety** (around 8% of men have a colour vision deficiency; red and green both read as brown):
  never rely on colour alone. Prefer **blue–orange** over red–green for diverging scales; where traffic-light
  colours are required, add a second encoding — icon, arrow, or text. Test with a simulator before shipping.
  A RAG dashboard that only works in colour is a RAG dashboard that fails for one reader in twelve.
- Grey is the default; colour highlights the point. Use colour with a purpose, never for decoration.

## Declutter & grouping

- **Remove non-data ink.** Heavy gridlines, chart borders, backgrounds, drop shadows, redundant legends, and
  false-precision decimals add cognitive load without information — strip them. Everything left on the page
  should be there because it carries meaning.
- **Group with the eye's rules, not with boxes.** Related tiles read as a group through **proximity** and
  **alignment**; use whitespace and a grid to separate sections rather than borders and colour blocks. A clean
  alignment grid is worth more than any divider line.
- **One focal point per view.** Lead the eye to the single most important thing first (position plus one accent
  colour), then let it travel outward. If everything is emphasised, nothing is.

## Honesty rules

- Bar charts start at zero. Always.
- Line chart axes may zoom but must be labelled, and consistent across panels being compared.
- The same measure gets the same scale when shown side by side.
- No cumulative chart to disguise flat progress without also showing the per-period series.
- Never present an estimate as measured, or stale data as current. The as-of date is not optional.
- Report the exception, not the inventory — a dashboard that shows everything hides everything.

## Technical

- Every tile reads from the portfolio register and its cycle artifacts — no heavy logic in the BI tool.
- Measure names match `knowledge/portfolio-measures.md` exactly.
- Load target: interactive in under 5 seconds; use extracts or aggregates to hit it.
- Every dashboard has: a spec in `knowledge/portfolio/`, reconciliation checks in `checks/`, a screenshot, and
  an inventory row in `dashboards/README.md`.
- Review for retirement every quarter — unused dashboards get archived, not abandoned. **Beware the dead-end
  dashboard:** a measure that has sat on target for months is no longer informative — rotate it out and track
  usage. A good dashboard answers one question and raises the next.
- **Functional before beautiful:** analytical clarity is the foundation; decoration that doesn't encode data —
  and "interesting" chart types chosen to avoid bar charts — gets cut.

## Privacy

A portfolio surface names sponsors, managers, and the owner of every data gap. Two rules follow:

- **Default filter state stays impersonal.** Saved filter and slicer selections persist into the report's own
  files and then into git.
- **These surfaces report the health of work, not the performance of people.** Attributing a gap to an owner
  exists so it gets fixed, not so anyone gets ranked.
