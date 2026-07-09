---
name: plan-launch
description: Plan a release/launch — choose a rollout strategy, build the cross-functional readiness checklist, set success and guardrail metrics with thresholds, and define Go/No-Go and rollback. Use before shipping a notable change. Dispatches the release-manager.
---

# /plan-launch — Ship safely, drive adoption

## When to use
Before releasing/launching a notable feature or product; planning a go-to-market motion.

## Dispatches
`release-manager` (lead) + `product-analyst` (success/guardrail metrics). Consult `comms-lead` for
announcements; `project-manager`/`program-manager` for cross-team coordination.

## Inputs
`knowledge/roadmap.md`, relevant PRDs, `knowledge/product-context.md`, `knowledge/cadence.md`.

## Steps
1. Separate the **release** (deployment) from the **launch** (GTM motion); plan both. Confirm the phase gate is
   passed (go/kill/hold) before committing launch spend.
2. Choose a rollout strategy that minimizes blast radius and still yields a real signal (phased/canary/flags).
3. Agree the **positioning & messaging platform** once; match launch strategy to **market type** (create
   demand in a new category vs. capture it in an existing one).
4. Build the cross-functional **readiness checklist** (product, eng, quality/security, support, marketing,
   sales/CS, legal); ensure **demand generation and sales/channel enablement** are ready before launch day;
   tier launch effort to impact.
5. Define **success and guardrail metrics with thresholds before launch**; decide expand/hold/rollback rules.
6. Name a **Go/No-Go owner** and a clear **rollback trigger**; plan the post-launch review (and, for sunsets,
   an end-of-life plan).

## Methods
`knowledge/methods/launch-and-gtm.md`, `knowledge/methods/metrics-and-experimentation.md`,
`knowledge/methods/project-management.md`.

## Output
Start from `templates/launch-plan.md`. Save a launch/release plan + readiness checklist artifact (e.g.,
`knowledge/launches/<YYYY-MM-DD>-<name>.md`);
log Go/No-Go and rollout decisions to `knowledge/decision-log.md`. Follow `standards/document-standards.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
