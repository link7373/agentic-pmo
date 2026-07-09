---
name: plan-sprint
description: Plan the next sprint — set a single Sprint Goal, check capacity, and select ready backlog items that fit. Use at the start of a sprint cycle. Dispatches the scrum-master with the product-owner. Supports optional tool sync.
---

# /plan-sprint — Commit the next sprint

## When to use
At the start of a sprint cycle, or to re-plan a sprint.

## Dispatches
`scrum-master` (facilitation) + `product-owner` (backlog/priority).

## Inputs
`knowledge/backlog.md` (ordered, ready items), `knowledge/cadence.md` (sprint length, team), velocity history.

## Steps
1. Set one clear **Sprint Goal** aligned to the roadmap/current objective.
2. Estimate capacity for the sprint (team availability, sprint length).
3. Select top-priority items that meet Definition of Ready and fit capacity (use velocity as a forecast range).
4. Confirm each selected item has acceptance criteria and no blocking dependencies.
5. Record the sprint plan: goal, selected items, capacity, commitments.

## Methods
`knowledge/methods/agile-scrum-mechanics.md`, `knowledge/methods/requirements-and-stories.md`.

## Output
Start from `templates/sprint-plan.md`. Save a sprint plan artifact (e.g., `knowledge/sprints/<sprint-id>.md`); update item status in
`knowledge/backlog.md`. Follow `standards/agile-standards.md` and `standards/document-standards.md`.

## Optional sync
If a tool is configured in `knowledge/integrations.md`, offer to create/update the sprint and its items in
that tool after recording the plan. Files remain source of truth; skip if not configured.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
