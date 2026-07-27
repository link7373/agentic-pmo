---
name: plan-portfolio-automation
description: Design the automation behind the portfolio cycle — status intake, validation, data flow to the reporting surface — with triggers, validation rules, idempotency, error escalation and a manual fallback. Automates collection and validation, never judgment. Produces a buildable spec, not a built flow. Dispatches the portfolio-analyst.
---

# /plan-portfolio-automation — Take the manual cost out of the cycle

## When to use
When the reporting cycle is consuming the time that analysis needs, when intake chasing is manual, when data
moves between tools by copy-paste, or when the same validation errors recur every period.

## Dispatches
`portfolio-analyst`.

## Inputs
`knowledge/portfolio.md` (the intake contract in practice — what's missing and how often), the latest intake
review in `knowledge/portfolio/`, existing dashboard specs (destination and measure definitions),
`knowledge/integrations.md` (available connectors and their status), `knowledge/cadence.md` (cycle timing).

## Steps
1. Map the current cycle end to end and mark where the time and the errors actually go — chasing submissions,
   re-keying data, fixing validation problems, rebuilding the same summary.
2. Pick candidates on the rule that **collection and validation automate well; judgment does not**. Automate
   the chase, the checks, and the movement of data. Never automate interpreting a RAG or deciding to escalate.
3. Design each flow: trigger → collect → validate → transform → store → publish → notify. Validate **at the
   boundary** — bad input rejected on arrival never reaches a report, and rejection messages name the field,
   the problem, and the fix.
4. Make it idempotent. Define the dedupe key and the re-run behaviour; assume every run happens twice, and
   specify how a past period is safely backfilled.
5. Specify error handling by failure class — retry transient, halt and alert on persistent, process-the-rest
   and report the rejects on partial — each escalating to a **named human** within a stated time. A flow that
   fails silently is worse than none: the report still renders, just wrongly.
6. Define the human-in-the-loop points, the run log (what ran, when, record counts, failures — the source for
   the data-health measure), the manual fallback, and the rollout and rollback plan.
7. Fill in `## Handoff` with the build route and any open question blocking implementation. Check
   `knowledge/integrations.md` first: **there is no automation build capability today**, so this spec is
   implemented by a person or another tool. State that plainly rather than implying a flow will appear.

## Methods
`knowledge/methods/portfolio-management.md` (automation patterns, the intake contract, data health),
`knowledge/methods/project-management.md` (change control and risk for the rollout).

## Output
Start from `templates/automation-spec.md`. A spec saved to `knowledge/portfolio/automation-<flow>.md` — a
living document, updated in place. `knowledge/` remains the source of truth; no flow may become the only
record of portfolio data. Note any new tool dependency in `knowledge/integrations.md` and log the decision to
`knowledge/decision-log.md`. Follow `standards/document-standards.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
