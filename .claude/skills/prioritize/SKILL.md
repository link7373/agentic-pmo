---
name: prioritize
description: Score and rank features, ideas, or backlog items against goals using the right framework (RICE, WSJF, Kano, value/effort, MoSCoW, or weighted scoring). Use when deciding what to build next or sequencing work. Dispatches the product-manager.
---

# /prioritize — Rank work against goals

## When to use
Choosing what to build next, sequencing initiatives, or scoping a release among competing items.

## Dispatches
`product-manager` (lead). Pull effort estimates from `product-owner`/team; impact evidence from
`product-analyst`/`discovery-researcher`.

## Inputs
Candidate items (from roadmap, backlog, stakeholders), `knowledge/product-context.md` (goals/OKRs).

## Steps
1. Confirm the goal/OKR the ranking serves; drop items that don't ladder up to it.
2. Pick the framework that fits the decision:
   - many features, one goal → **RICE**; sequencing a flow with timing → **WSJF**;
   - satisfaction strategy / feature mix → **Kano**; quick triage → **value/effort 2×2**;
   - release scope with stakeholders → **MoSCoW**; multi-criteria → **weighted scoring**.
3. Score each item; record estimates, **confidence**, and assumptions. Weigh the underlying bases — value,
   cost/effort, risk, dependencies, time-sensitivity, and any regulatory/policy constraints that can override
   pure scoring.
4. Produce a ranked, defensible order with the rationale.

## Methods
`knowledge/methods/prioritization-frameworks.md`.

## Output
A ranked list with scores and rationale; reflect ordering into `knowledge/roadmap.md` or
`knowledge/backlog.md` as relevant; log the prioritization decision to `knowledge/decision-log.md`.
Follow `standards/document-standards.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
