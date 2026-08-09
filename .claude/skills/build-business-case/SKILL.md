---
name: build-business-case
description: Build an investment case for an initiative — options including do-nothing, whole-life costs, quantified benefits with named owners, ROI/NPV/payback with a sensitivity run, and a clear recommendation. Use before committing significant money or at a funding gate. Dispatches the financial-analyst.
---

# /build-business-case — Justify the investment

## When to use
Before funding an initiative, at gate G1, or whenever someone asks "is this worth doing?" and the answer needs
to survive scrutiny. Also use to refresh a case whose assumptions have visibly changed.

## Dispatches
`financial-analyst` (lead) + `product-strategist` (strategic fit) + `product-manager` (scope and sizing).
Where the initiative needs people, pull supply constraints from `resource-manager`.

## Inputs
The initiative (idea, PRD, or intake item), `knowledge/product-context.md` (goals it must serve),
`knowledge/financials.md` (funding envelopes, comparable costs), `knowledge/resources.md` (people cost and
availability), `knowledge/governance.md` (which gate this feeds and who approves).

## Steps
1. **Frame the problem in business terms** and name the goal or OKR it serves. If it ladders up to nothing,
   surface that before doing the analysis — it is the finding.
2. **Build the options, always including do-nothing — priced.** What does the status quo cost over the
   appraisal period in lost revenue, manual effort, risk, or attrition? Cases that look marginal against zero
   often look obvious against a properly costed status quo, and vice versa.
3. **Cost the whole life.** Build, licences, hosting, support, maintenance, training, and decommissioning what
   this replaces. Separate one-off from recurring — they come from different budgets and different approvers.
   Label every figure measured or estimated, with its basis.
4. **Quantify benefits with owners.** Classify each as cash, cost-avoidance, productivity, or non-financial.
   A productivity saving is only cash if the hours are actually redeployed or removed — otherwise claim it as
   capacity. Every benefit needs an owner who will still be there when it's measured, and a measurement method
   that exists today.
5. **Appraise with at least two measures** (ROI, payback, NPV) — each misleads differently — then **run the
   sensitivity**: halve the main benefit, add 50% to the main cost. If the recommendation only survives at the
   optimistic end of every assumption, say so plainly rather than letting the headline number carry it.
6. **State the recommendation, the ask, and the deadline** — the funds, the people, the decision needed, and
   the date past which delay starts costing something.
7. **Seed the benefits register** in `knowledge/financials.md` so every claim here can be checked later.

## Methods
`knowledge/methods/financial-management.md` (case anatomy, appraisal measures, benefit types, sensitivity),
`knowledge/methods/product-strategy.md` (strategic fit), `knowledge/methods/governance-and-change.md` (what a
gate demands of a case).

## Output
Start from `templates/business-case.md`. Save to
`knowledge/financials/YYYY-MM-DD-<initiative>-business-case.md`; add the claimed benefits to the benefits
register in `knowledge/financials.md`; log the funding decision to `knowledge/decision-log.md` once made.
Follow `standards/document-standards.md`.

## Optional sync
If `knowledge/integrations.md` configures Notion or Slack, offer to post the recommendation and ask. Files
remain source of truth; skip if not configured.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
