---
name: groom-backlog
description: Write and refine the product backlog — break epics into INVEST user stories, add testable acceptance criteria, estimate, and order to Definition of Ready. Use to prepare work for sprints. Dispatches the product-owner. Supports optional tool sync.
---

# /groom-backlog — Make work ready

## When to use
Turning roadmap/PRD intent into well-formed, ordered, ready backlog items; ongoing refinement.

## Dispatches
`product-owner` (lead). Consult `scrum-master` for readiness/estimation facilitation.

## Inputs
`knowledge/roadmap.md`, PRDs, `knowledge/product-context.md`, existing `knowledge/backlog.md`.

## Steps
1. Pull intent from roadmap/PRDs; break epics into thin, valuable stories.
2. Write each as `As a <user>, I want <capability>, so that <outcome>` with testable acceptance criteria;
   capture non-functional needs (performance, security, accessibility) as explicit, measurable items too.
3. Enforce INVEST; split oversized stories into end-to-end slices; keep each item traceable to a need/goal.
4. Estimate (story points / t-shirt) per `standards/agile-standards.md`; note dependencies.
5. Order the backlog by value/priority; bring top items to Definition of Ready.

## Methods
`knowledge/methods/requirements-and-stories.md`, `knowledge/methods/business-analysis.md`,
`knowledge/methods/agile-scrum-mechanics.md`, `knowledge/methods/prioritization-frameworks.md`.

## Output
Update `knowledge/backlog.md` (source of truth); log ordering/scope decisions to `knowledge/decision-log.md`.
Follow `standards/document-standards.md` and `standards/agile-standards.md`.

## Optional sync
If `knowledge/integrations.md` configures a tool (Jira/Linear/Notion), after updating `knowledge/backlog.md`
offer to sync new/changed stories to it via the available connector. Files remain the source of truth; if no
integration is configured, skip silently.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
