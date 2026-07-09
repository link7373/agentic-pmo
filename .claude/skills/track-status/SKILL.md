---
name: track-status
description: Produce a status report — RAG health with reason and action, progress, velocity/burndown, milestone status, and an updated RAID log. Use for regular reporting or an on-demand health check. Dispatches delivery-monitor then comms-lead. Supports optional tool sync.
---

# /track-status — Where things stand

## When to use
Regular status cadence, or an on-demand "how are we doing?" health check.

## Dispatches
`delivery-monitor` (gather + analyze) → `comms-lead` (format for the audience).

## Inputs
Project/sprint plans, `knowledge/backlog.md`, `knowledge/roadmap.md`, `knowledge/raid-log.md`,
`knowledge/cadence.md`, velocity history.

## Steps
1. Roll up progress: milestone/sprint status, velocity trend, burndown/burnup, scope changes; where a
   cost/schedule baseline exists, add earned-value indices (SPI/CPI) for an objective read on progress.
2. Compute **RAG per workstream with a reason and an action** — never a bare color.
3. Detect anomalies/emerging risks (slipping critical path, rising burnup ceiling, stalled items); update
   `knowledge/raid-log.md` with owners.
4. Have `comms-lead` format the report for the target audience (lead with decisions/help needed).

## Methods
`knowledge/methods/project-management.md`, `knowledge/methods/agile-scrum-mechanics.md`,
`standards/communication-standards.md` (RAG discipline, status template).

## Output
Start from `templates/status-report.md`. A status report artifact and an updated `knowledge/raid-log.md`. Follow `standards/document-standards.md`
and `standards/communication-standards.md`.

## Optional sync
If `knowledge/integrations.md` configures Slack/Notion, offer to post the formatted status there. Files
remain source of truth; skip if not configured.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
