---
name: elicit-requirements
description: Elicit and analyze requirements for a problem or feature — frame the need, choose elicitation techniques, model current vs. future state, classify and specify requirements (including non-functional), keep them traceable, and verify/validate. Use when the problem is unclear, stakeholders disagree, or requirements are ambiguous, before a PRD is locked. Dispatches the business-analyst.
---

# /elicit-requirements — Understand the need before building

## When to use
The problem is fuzzy, stakeholders disagree, the process is complex, or requirements are ambiguous — and you
need a rigorous, traceable requirements package before (or to strengthen) a PRD.

## Dispatches
`business-analyst` (lead). Pull evidence from `discovery-researcher`; hand analyzed requirements to
`product-manager` for the PRD and to `product-owner` for backlog detailing; partner with `project-manager` on
scope/change impact.

## Inputs
`knowledge/product-context.md`, `knowledge/stakeholder-map.md`, `knowledge/intake.md`, any existing PRD/notes.

## Steps
1. Frame the six core concepts — name the **need, value, stakeholders, and context** before any solution.
2. Plan and run **elicitation** — choose techniques that fit the goal (interviews, workshops, observation,
   surveys, document analysis, prototyping); probe the *why*; **confirm** findings back with stakeholders.
3. Model **current state → future state → gap**; run root-cause analysis (5 Whys, cause-and-effect) on the
   real pain so the change targets causes, not symptoms.
4. **Classify** requirements (business / stakeholder / solution [functional + non-functional] / transition);
   specify non-functional attributes with **measurable targets**.
5. Establish **traceability** (need → requirement → design/test); **verify** each requirement is well-formed
   and **validate** it delivers value; prioritize by value, risk, dependency, and constraint.
6. Compare solution options against explicit criteria; state assumptions, open questions, and confidence.

## Methods
`knowledge/methods/business-analysis.md`, `knowledge/methods/requirements-and-stories.md`,
`knowledge/methods/discovery-and-validation.md`, `knowledge/methods/prioritization-frameworks.md`.

## Output
Start from `templates/requirements-package.md`. Save the package at
`knowledge/prds/<YYYY-MM-DD>-<feature>-analysis.md` (or as a section feeding `/write-prd`); log scope/solution
decisions to `knowledge/decision-log.md`. Follow
`standards/document-standards.md` — classify requirements, make non-functional targets measurable, and keep
everything traceable to a need.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
