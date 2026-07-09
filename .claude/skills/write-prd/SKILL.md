---
name: write-prd
description: Write a product requirements document for a feature or initiative — problem, goals/success metrics, users, scope (in and out), requirements/stories, UX, risks, and rollout plan. Use when defining what to build. Dispatches the product-manager.
---

# /write-prd — Define what to build

## When to use
Defining a feature/initiative for the team to build, after the problem is validated.

## Dispatches
`product-manager` (lead). For ambiguous or contested requirements, run `/elicit-requirements`
(`business-analyst`) first. Pull evidence from `discovery-researcher`; success metrics from `product-analyst`;
hand to `product-owner` for backlog detailing.

## Inputs
`knowledge/product-context.md`, `knowledge/roadmap.md`, discovery findings.

## Steps
1. State the problem and context with discovery evidence; confirm the goal/OKR it serves.
2. Define goals and the success metric(s); name target users/personas and their jobs.
3. Set scope — what's in and **explicitly what's out** this release.
4. Capture requirements/user stories with acceptance criteria; specify **non-functional requirements**
   (performance, security, accessibility, …) with measurable targets; note UX flows and key states.
5. List dependencies, risks, assumptions, open questions; add a rollout & measurement plan.

## Methods
`knowledge/methods/requirements-and-stories.md`, `knowledge/methods/business-analysis.md`,
`knowledge/methods/lean-product-process.md`, `knowledge/methods/metrics-and-experimentation.md`.

## Output
Start from `templates/prd.md`. Save a PRD artifact at `knowledge/prds/<YYYY-MM-DD>-<feature>.md`; log scope decisions to
`knowledge/decision-log.md`. Follow `standards/document-standards.md` (lead with problem + success metric;
always include out-of-scope).

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
