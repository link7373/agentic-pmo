---
name: plan-capacity
description: Plan capacity and balance load across teams — compare committed/planned work against available capacity, surface over-allocation and bottlenecks, and recommend sequencing or trade-offs. Use when staffing or load changes, or ahead of a planning cycle. Dispatches the program-manager with the scrum-master.
---

# /plan-capacity — Match work to capacity

## When to use
Before a planning cycle, when staffing/load changes, or when teams feel over-committed.

## Dispatches
`program-manager` (lead, cross-team view; owns the sequencing decision) + `resource-manager` (supply data) +
`scrum-master` (per-team velocity/availability) + `portfolio-analyst` (demand and collision data).

## Inputs
`knowledge/resources.md` (people, allocations, constraints — the supply side), `knowledge/cadence.md` (teams,
velocity history), `knowledge/portfolio.md` and project plans (demand), `knowledge/roadmap.md`,
`knowledge/backlog.md`, `knowledge/raid-log.md` (dependencies), prior cycles in `knowledge/capacity/`.

## Steps
1. Establish available capacity **after deductions** — leave, support and on-call, overhead, ramp, context
   switching — from `knowledge/resources.md`. Show the deductions; nominal headcount is not capacity. Where a
   team is measured in velocity rather than FTE, keep that in its own units and never add the two together.
2. Lay committed and proposed work against capacity; identify **over-allocation** and the **bottleneck role**,
   not just an aggregate shortfall. Portfolios rarely run out of people in general.
3. Map cross-team dependencies and collisions that constrain sequencing (from `knowledge/portfolio.md` and the
   program view).
4. Run scenarios — re-sequence, defer, reallocate, reduce scope, add capacity with its lead time — and show
   the effect of each on the constraint. Present options with consequences; the sequencing call belongs to
   `program-manager` and anything costing money to the sponsor per `knowledge/governance.md`.
5. Limit system-level WIP; protect the critical path across the portfolio. Flag sustained utilization above
   ~85% as a risk rather than reporting it as efficiency.
6. State data confidence — which demand estimates are measured versus guessed, and how stale the resource
   register is.

## Methods
`knowledge/methods/resource-management.md` (deductions, utilization, constraints),
`knowledge/methods/portfolio-management.md` (demand & capacity cycle, collisions, WIP),
`knowledge/methods/project-management.md` (dependencies, critical path),
`knowledge/methods/agile-scrum-mechanics.md` (velocity/forecasting).

## Output
Start from `templates/capacity-plan.md`. Save to `knowledge/capacity/YYYY-MM-DD-<cycle>-capacity.md`; reflect
accepted changes into `knowledge/roadmap.md` and project plans; log capacity decisions to
`knowledge/decision-log.md`. Report by role or team — individual allocation rows stay in
`knowledge/resources.md`. Follow `standards/document-standards.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
