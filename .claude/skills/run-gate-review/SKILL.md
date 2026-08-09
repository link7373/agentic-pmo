---
name: run-gate-review
description: Run a stage-gate review — check evidence against pre-agreed entry criteria, assess delivery, financial and benefits position, and record a go / go-with-conditions / hold / kill decision with named conditions. Use at any gate defined in knowledge/governance.md. Dispatches the governance-lead.
---

# /run-gate-review — Decide whether it proceeds

## When to use
At any gate defined in `knowledge/governance.md` — typically before funding, before build, before launch, and
at closure. Also use when someone asks for more money or time on an initiative that has never been gated.

## Dispatches
`governance-lead` (lead) + `financial-analyst` (cost and benefits position) + `delivery-monitor` (delivery
position) + `portfolio-analyst` (portfolio context and data confidence) + `comms-lead` (formats the pack via
`/make-deliverable` from `templates/steerco-pack.md` where the gate goes to a committee).

## Inputs
`knowledge/governance.md` (this gate's criteria, decider, evidence required), the business case in
`knowledge/financials/`, the project plan, `knowledge/status/`, `knowledge/financials.md`,
`knowledge/raid-log.md`, `knowledge/change-log.md`.

## Steps
1. **Restate the gate's one question** from `knowledge/governance.md`. Gates answer one question; everything
   else is evidence for it. If the gate has no recorded criteria or decider, fix that first — an ungated
   review is a status meeting.
2. **Test each entry criterion against evidence.** Record a verdict and a link per criterion. "Testing is
   complete" is a claim; a test report is evidence. Where evidence doesn't exist, the criterion is **not met** —
   say so and let the decider weigh it rather than softening the verdict.
3. **Assess the three positions** — delivery (schedule and scope vs. baseline), financial (spend, forecast,
   CPI/SPI where a baseline exists; otherwise state that it doesn't), and benefits (are the business case's
   claims still credible, and what changed since approval?).
4. **Surface risk at this gate.** Top RAID entries at the relevant level with scores; anything above the
   escalation threshold in `knowledge/governance.md` is named explicitly.
5. **Frame the decision strictly forward.** Ignoring everything already spent, is the *remaining* cost the best
   use of that money? This is the counter to the sunk-cost trap that makes late gates rubber-stamps.
6. **Record one of four outcomes** — go, go-with-conditions, hold, kill. Conditions carry an owner and a date
   or they are decoration. **Record dissent honestly**; a gate record showing unanimous agreement every time is
   not being used properly.
7. **Set the next gate** and what must be true to enter it.

## Methods
`knowledge/methods/governance-and-change.md` (gates, sunk-cost trap, decision rights, dissent),
`knowledge/methods/financial-management.md` (what a gate should demand of a case),
`knowledge/methods/portfolio-management.md` (portfolio governance and stage gates).

## Output
Start from `templates/gate-review.md`. Save to `knowledge/programs/YYYY-MM-DD-<project>-gate-<n>.md`; update
the stage and RAG in `knowledge/portfolio.md`; log the decision and its conditions in
`knowledge/decision-log.md`. Where the gate went to a committee, the pack goes to `knowledge/deliverables/`.
Follow `standards/document-standards.md`.

## Optional sync
If `knowledge/integrations.md` configures Slack/Notion, offer to circulate the decision and conditions to the
named owners. Files remain source of truth; skip if not configured.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
