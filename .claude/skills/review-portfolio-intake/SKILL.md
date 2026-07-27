---
name: review-portfolio-intake
description: Quality-gate the status and capacity submissions from project and program managers — test each for completeness, currency, consistency and credibility, set a confidence level per item, and return specific asks to named owners. Run before any portfolio rollup. Dispatches the portfolio-analyst.
---

# /review-portfolio-intake — Can this data be trusted?

## When to use
At the close of a reporting cycle, before `/track-portfolio`. Also on demand when a portfolio number looks
wrong, when leadership questions a report, or when a manager's submissions have been drifting.

## Dispatches
`portfolio-analyst`.

## Inputs
`knowledge/portfolio.md` (the register and its last confidence flags), `knowledge/projects/`,
`knowledge/sprints/`, `knowledge/raid-log.md`, `knowledge/roadmap.md`, `knowledge/cadence.md`.

## Steps
1. Collect the submissions for the cycle and check each against the **intake contract**: complete (every
   required field has a value or an explicit "unknown"), current (updated inside the window — check the
   timestamp, not just the content), consistent (internally coherent, and coherent with the RAID log, roadmap
   and sprint data), credible (narrative and numbers agree).
2. Flag the specific contradictions rather than general concerns — a green RAG beside a slipped milestone; a
   date that has moved twice while the colour held; an unchanged update on a moving project.
3. Set a **confidence level** per register row (high / medium / low / missing) and write it to
   `knowledge/portfolio.md`.
4. Build the ask list **by named owner with a concrete request** — the field, what's wrong, and what to
   supply. Never silently repair a submission; the same gap recurs next cycle if the loop doesn't close.
5. Track chronic gaps. An owner missing several cycles is a portfolio risk, not an admin nuisance — escalate
   to `knowledge/raid-log.md` with an owner.

## Methods
`knowledge/methods/portfolio-management.md` (the intake contract, confidence levels, the feedback loop),
`knowledge/methods/project-management.md` (RAG discipline, RAID), `standards/communication-standards.md`.

## Output
An intake quality review saved to `knowledge/portfolio/YYYY-MM-DD-intake-review.md`, plus updated confidence
flags and the **Data gaps** table in `knowledge/portfolio.md`. Feedback is specific and constructive — aimed at
improving the next submission, not grading the last one. Follow `standards/document-standards.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
