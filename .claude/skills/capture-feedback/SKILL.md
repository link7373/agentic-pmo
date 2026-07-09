---
name: capture-feedback
description: Capture and triage inbound signals — customer feedback, support themes, sales asks, stakeholder requests, ideas, bug trends — into the intake register, then route each to discovery, backlog, roadmap, or decline. Use whenever new input arrives or for a triage sweep. Dispatches the product-manager.
---

# /capture-feedback — The PMO's front door

## When to use
Whenever inbound arrives (feedback, requests, ideas, support/bug themes), or for a regular triage sweep of
open intake.

## Dispatches
`product-manager` (lead/triage). Consult `discovery-researcher` for items needing validation;
`product-owner` for items going straight to backlog.

## Inputs
The raw signal(s), `knowledge/intake.md`, `knowledge/product-context.md` (goals/OKRs), `knowledge/roadmap.md`.

## Steps
1. **Capture** each signal into `knowledge/intake.md`: date, source, raw request, type.
2. **Classify** type (problem / idea / request / bug / insight) and link the goal/OKR it relates to (if any).
3. **Look for themes** — does this match a recurring pattern? Update the themes section if so.
4. **Triage decision** per item:
   - **Explore** → `/run-discovery` (unvalidated problem worth investigating)
   - **Backlog** → `/groom-backlog` (clear, valuable, ready to shape)
   - **Roadmap** → `/build-roadmap` (strategic, larger than a story)
   - **Now/quick** → top of backlog (small, urgent, clear value)
   - **Decline / Watch** → record with a reason (so it doesn't keep re-entering)
5. **Route** and record where each item went and its status.

## Methods
`knowledge/methods/discovery-and-validation.md` (signal strength), `knowledge/methods/prioritization-frameworks.md`.

## Output
Updated `knowledge/intake.md`; items routed to the right skill/agent. Log consequential decline/accept
decisions to `knowledge/decision-log.md`. Follow `standards/document-standards.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
