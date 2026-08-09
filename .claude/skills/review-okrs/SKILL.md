---
name: review-okrs
description: Run an OKR check-in or end-of-cycle review — pull current values, grade each key result, assess confidence, and capture learnings to carry forward. Use mid-cycle or at cycle end. Dispatches the product-strategist with the product-analyst.
---

# /review-okrs — Close the goals loop

## When to use
Mid-cycle OKR check-in, or end-of-cycle grading before setting the next cycle's objectives.

## Dispatches
`product-strategist` (lead) + `product-analyst` (pull actuals, validate metric definitions).

## Inputs
`knowledge/product-context.md` (current OKRs), the metrics catalog/actuals, prior review notes.

## Steps
1. For each key result, pull the **current value** vs. baseline and target; update the OKR table.
2. **Grade** each KR (e.g., 0.0–1.0) and the objective overall; set/update confidence.
3. Diagnose: what's driving over/under-performance? Was the KR the right outcome measure?
4. Capture **learnings** and decide carry-forward: keep / adjust / drop, and what changes next cycle.
5. Flag any strategy implications (a missed objective may mean re-examining the bet, not just trying harder).

## Methods
`knowledge/methods/product-strategy.md` (OKRs), `knowledge/methods/metrics-and-experimentation.md`.

## Output
Use `templates/okr.md` as the structure for the graded OKR tables. Updated OKRs in
`knowledge/product-context.md` with grades/learnings; log the review outcome and any
strategy implications to `knowledge/decision-log.md`. Feeds `/define-strategy` for the next cycle.
Follow `standards/document-standards.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
