---
name: manage-change
description: Run a change request against an approved baseline — assess impact on scope, schedule, cost and risk separately, present options with a recommendation, get the named approval, and re-baseline. Use whenever approved scope, schedule or cost would move. Dispatches the project-manager.
---

# /manage-change — Control the baseline

## When to use
Whenever something would move **approved scope, schedule, or cost**. Work that fits inside the baseline is not
a change — don't inflate the log with normal backlog churn. But when in doubt, log it: an unrecorded
re-baseline makes every later variance report meaningless.

## Dispatches
`project-manager` (lead) + `financial-analyst` (cost impact and re-baselining) + `governance-lead` (policy,
and any change crossing projects) + `program-manager` (where other projects are affected).

## Inputs
The change request or the event that triggered it, the project plan in `knowledge/projects/`,
`knowledge/financials.md` (cost baseline), `knowledge/governance.md` (thresholds and approvers),
`knowledge/raid-log.md`, `knowledge/change-log.md` (prior changes and cumulative drift).

## Steps
1. **Check it's actually a change, and whose.** Compare against the approved baseline. Below the threshold in
   `knowledge/governance.md`, the project manager just decides — say so and stop. Above it, or crossing
   projects, continue.
2. **Capture the change and why now.** What is moving, and what prompted it — new information, a missed
   requirement, an external event, a discovered defect. "The stakeholder asked" is a source, not a reason.
3. **Assess each dimension separately** — scope, schedule, cost, risk, resources, quality/NFRs, and other
   projects. A change that "has no impact" usually means the impact hasn't been looked for. State the
   do-nothing consequence too.
4. **Present options, not just the request.** Reject/absorb, approve as requested, approve with modification —
   each with its impact. Recommend one plainly; the approver is agreeing or disagreeing, not deciding from
   scratch.
5. **Get the named approval** per `knowledge/governance.md`. No CR is approved without a named approver and a
   date.
6. **Re-baseline.** This is the step that gets skipped. Update the project plan, the cost baseline in
   `knowledge/financials.md`, the schedule and milestones, and the backlog. Then update the cumulative
   baseline-movement table so the drift from the original approval stays visible.
7. **Communicate and log.** Tell the affected stakeholders what changed, and record the decision.

## Methods
`knowledge/methods/governance-and-change.md` (change control, the two failure modes, re-baselining),
`knowledge/methods/project-management.md` (triple constraint, change control),
`knowledge/methods/financial-management.md` (cost baseline integrity).

## Output
Start from `templates/change-request.md`. Record the request in `knowledge/change-log.md` (open, then moved to
decided), update the affected plan and baselines, and log the decision in `knowledge/decision-log.md`. Follow
`standards/document-standards.md`.

## Optional sync
If `knowledge/integrations.md` configures Jira/Linear, offer to adjust the affected tickets after the
re-baseline. Files remain source of truth; skip if not configured.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
