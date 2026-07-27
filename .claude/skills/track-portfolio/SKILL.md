---
name: track-portfolio
description: Roll up the whole portfolio — refresh the register, gate the data, and surface themes, collisions, dependency clusters and the binding capacity constraint — then report it in two tiers, delivery detail and leadership rollup. Use for the portfolio cycle or an on-demand portfolio read. Dispatches the portfolio-analyst with delivery-monitor, then comms-lead. Supports optional tool sync.
---

# /track-portfolio — How the whole portfolio is doing

## When to use
The monthly portfolio cycle, ahead of a planning or investment decision, or when leadership asks "what's
actually going on across everything?". For a single project or sprint, use `/track-status` instead.

## Dispatches
`portfolio-analyst` (lead) + `delivery-monitor` (project- and sprint-level health inputs) →
`comms-lead` (format the leadership tier).

## Inputs
`knowledge/portfolio.md`, `knowledge/projects/`, `knowledge/sprints/`, `knowledge/roadmap.md`,
`knowledge/raid-log.md`, `knowledge/cadence.md` (teams, velocity, calendar),
`knowledge/product-context.md` (goals/OKRs to link investment against).

## Steps
1. Refresh the register — one row per project/program on the standard schema; reconcile any program row that
   contradicts its children rather than averaging over it.
2. Gate the data first. If `/review-portfolio-intake` hasn't run this cycle, run its checks now and carry the
   confidence levels through. **Report on gaps rather than aggregating over them** — say what could not be
   assessed and why.
3. Roll up health: triple constraint per item, milestone hit rate, RAG with reason and action; where a
   cost/schedule baseline exists add SPI/CPI; take velocity and burndown reads from `delivery-monitor`.
4. Analyze **across**: themes and recurring patterns, **collisions** (two or more items needing the same
   scarce team in the same window), dependency clusters, the binding capacity constraint by role, portfolio
   WIP and throughput, and concentration of risk.
5. Run scenarios on any breach — defer / re-sequence / reduce scope / add capacity — each with its effect on
   the constraint and its cost. Present options with consequences; hand the sequencing decision to
   `program-manager` and the investment decision to leadership.
6. Have `comms-lead` format the leadership tier: exceptions and decisions needed, not an inventory.

## Methods
`knowledge/methods/portfolio-management.md` (register, capacity cycle, collisions, KPIs, reporting tiers),
`knowledge/methods/project-management.md` (triple constraint, earned value, RAID, RAG),
`knowledge/methods/metrics-and-experimentation.md` (trends over snapshots; don't over-react to noise),
`standards/communication-standards.md`.

## Output
Start from `templates/portfolio-report.md`. A two-tier portfolio report saved to
`knowledge/portfolio/YYYY-MM-DD-portfolio-report.md`, an updated `knowledge/portfolio.md` (register, capacity
summary, collisions), a capacity cycle artifact when the demand/supply run is part of this cycle, and any
portfolio-level decision logged to `knowledge/decision-log.md`. Follow `standards/document-standards.md`.

## Optional sync
If `knowledge/integrations.md` configures Slack/Teams or Notion, offer to post the leadership tier there.
Files remain source of truth; skip silently if not configured.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
