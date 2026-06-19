---
name: plan-project
description: Build a project plan — scope (in/out), work breakdown, schedule and milestones, dependencies and critical path, and an initial RAID log. Use for a defined deliverable with constraints. Dispatches the project-manager.
---

# /plan-project — Plan a defined deliverable

## When to use
Planning a project/initiative with a defined outcome, schedule, or dependencies (beyond a single sprint).

## Dispatches
`project-manager` (lead). Consult `program-manager` for cross-team dependencies; `delivery-monitor` for the
RAID/health setup.

## Inputs
`knowledge/product-context.md`, `knowledge/roadmap.md`, `knowledge/cadence.md`, `knowledge/stakeholder-map.md`.

## Steps
1. Define scope as deliverables with acceptance criteria; state what's out of scope.
2. Decompose into a **WBS** of work packages small enough to estimate and own.
3. Sequence by dependency; estimate durations; identify **milestones** and the **critical path**.
4. Set up the **RAID log**: top risks (prob × impact, owner, response), assumptions, issues, dependencies.
5. Confirm RACI for key deliverables (exactly one Accountable each); note the change-control approach.

## Methods
`knowledge/methods/project-management.md`, `knowledge/methods/agile-scrum-mechanics.md`.

## Output
Start from `templates/project-plan.md`. Save a project plan artifact (e.g., `knowledge/projects/<name>.md`) and initialized/updated `knowledge/raid-log.md`;
log scope/schedule decisions to `knowledge/decision-log.md`. Follow `standards/document-standards.md`.
