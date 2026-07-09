---
name: plan-capacity
description: Plan capacity and balance load across teams — compare committed/planned work against available capacity, surface over-allocation and bottlenecks, and recommend sequencing or trade-offs. Use when staffing or load changes, or ahead of a planning cycle. Dispatches the program-manager with the scrum-master.
---

# /plan-capacity — Match work to capacity

## When to use
Before a planning cycle, when staffing/load changes, or when teams feel over-committed.

## Dispatches
`program-manager` (lead, cross-team view) + `scrum-master` (per-team velocity/availability).

## Inputs
`knowledge/cadence.md` (teams, velocity history), `knowledge/roadmap.md`, project plans,
`knowledge/backlog.md`, `knowledge/raid-log.md` (dependencies).

## Steps
1. Establish available capacity per team (headcount, availability, recent velocity as a range).
2. Lay committed + planned work against capacity; identify **over-allocation** and **bottleneck** teams.
3. Map cross-team dependencies that constrain sequencing (pull from RAID/program view).
4. Recommend trade-offs: re-sequence, defer, reallocate, or reduce scope — tied to priorities/goals.
5. Limit system-level WIP; protect the critical path across the portfolio.

## Methods
`knowledge/methods/project-management.md` (program/portfolio, dependencies, WIP),
`knowledge/methods/agile-scrum-mechanics.md` (velocity/forecasting).

## Output
A capacity view + recommended sequencing/trade-offs; reflect accepted changes into `knowledge/roadmap.md`
and project plans; log capacity decisions to `knowledge/decision-log.md`. Follow `standards/document-standards.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
