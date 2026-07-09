---
name: run-ceremony
description: Facilitate and produce artifacts for an agile ceremony — sprint planning, daily standup, sprint review, or retrospective. Use to run or prepare a ceremony and capture its outputs (decisions, actions, retro improvements). Dispatches the scrum-master.
---

# /run-ceremony — Facilitate the cadence

## When to use
Running or preparing a standup, sprint planning, sprint review, or retrospective.

## Dispatches
`scrum-master` (lead). For planning, also `product-owner`; for review, pull status from `delivery-monitor`.

## Inputs
Current sprint plan, `knowledge/backlog.md`, `knowledge/cadence.md`, `knowledge/raid-log.md`.

## Steps (by ceremony)
- **Planning** → set one Sprint Goal, select ready items to capacity (or invoke `/plan-sprint`).
- **Standup** → inspect progress to the Sprint Goal; capture impediments; re-plan the day.
- **Review** → inspect the increment vs. the goal; capture stakeholder feedback; adapt the backlog.
- **Retrospective** → inspect how the team worked; produce a few **specific, owned** improvement actions.

Facilitate each to its purpose; keep notes to decisions, actions (owner + due), and open questions.

## Methods
`knowledge/methods/agile-scrum-mechanics.md`, `standards/agile-standards.md`,
`standards/communication-standards.md` (ceremony-notes guidance).

## Output
A ceremony-notes artifact (e.g., `knowledge/ceremonies/<date>-<type>.md`); update `knowledge/raid-log.md`
with impediments; log consequential decisions/improvements to `knowledge/decision-log.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
