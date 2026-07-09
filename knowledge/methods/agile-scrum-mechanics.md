# Method: Agile & Scrum Mechanics

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

Scrum is a lightweight framework for delivering value iteratively under uncertainty. It rests on
**empiricism** — make decisions from what is observed, in short cycles — and works best when the
team adapts the framework to its context rather than following it ritualistically.

## Empiricism & the three pillars
- **Transparency** — the work and its state are visible to those who need it.
- **Inspection** — frequently examine artifacts and progress toward goals.
- **Adaptation** — adjust based on what inspection reveals.

Use empiricism for **complex** work (more unknowns than knowns). For obvious/complicated work, simpler
methods may fit; for chaotic situations, act to stabilize first. (A complexity lens: obvious → complicated
→ complex → chaotic; most product work is complex.)

## Roles (accountabilities)
- **Product Owner** — maximizes value; owns and orders the Product Backlog; single voice of "what & why."
- **Scrum Master** — enables the team; coaches, facilitates events, removes impediments; serves process health.
- **Developers / Team** — build a "done" increment each sprint; own "how" and the estimates.

## Events (cadence)
- **Sprint** — fixed-length container (commonly 1–4 weeks) producing a releasable increment.
- **Sprint Planning** — set the **Sprint Goal**, select backlog items, plan the work.
- **Daily Scrum / standup** — short daily sync to inspect progress toward the Sprint Goal and re-plan the day.
- **Sprint Review** — inspect the increment with stakeholders; gather feedback; adapt the backlog.
- **Sprint Retrospective** — inspect how the team worked; pick concrete improvements for next sprint.
- **Backlog Refinement** — ongoing: clarify, split, estimate, and order upcoming items toward Definition of Ready.

## Artifacts & their commitments
- **Product Backlog** → commitment: **Product Goal**. The ordered, emergent list of everything that might
  add value; the single source of work.
- **Sprint Backlog** → commitment: **Sprint Goal**. The selected items plus the plan to deliver them.
- **Increment** → commitment: **Definition of Done**. A usable, potentially releasable slice of value.

## Definition of Ready (DoR)
A backlog item is ready to plan when it is: clearly described, valuable, sized/estimable, has acceptance
criteria, dependencies understood, and small enough to finish in a sprint. DoR prevents pulling fuzzy work.

## Definition of Done (DoD)
The shared quality bar an increment must meet (e.g., coded, tested, reviewed, integrated, documented, meets
acceptance criteria, no known defects, deployable). Strengthen it over time; "done" means done.

## Estimation & velocity
- **Relative estimation** — size items relative to each other, not in absolute hours. **Story points**
  (often modified Fibonacci 1,2,3,5,8,13) capture effort + complexity + uncertainty.
- **Planning Poker** — team estimates simultaneously to surface differing assumptions, then discuss outliers.
- **Velocity** — points completed per sprint, averaged over recent sprints; use it to forecast a *range*,
  not a promise. Velocity is a planning aid, never a productivity target or cross-team comparison.
- **T-shirt sizing** — coarse S/M/L/XL for early/portfolio estimation.

## Forecasting & flow
- Forecast a release as a range: (remaining points) ÷ (low/high velocity) → optimistic/pessimistic sprints.
- **Burndown** (work remaining over time) and **burnup** (work done vs. scope) charts visualize progress and
  scope change. A rising burnup ceiling = scope creep.
- **Kanban lens:** limit work-in-progress, manage flow, watch cycle time and throughput; good for continuous/
  support-style work or to complement Scrum.

## Scaling to multiple teams
- Keep teams aligned to one Product Goal and one ordered backlog where possible.
- Make cross-team **dependencies** explicit and manage them actively (see `project-management.md`).
- Coordinate integration and a shared Definition of Done so increments combine into a releasable whole.

## Quality checklist
- [ ] Every sprint has a single, clear Sprint Goal.
- [ ] Items entering a sprint meet DoR; increments meet DoD.
- [ ] Estimates are relative; velocity is used as a forecast range, not a target.
- [ ] Retrospective produces specific, owned improvements.
- [ ] Empiricism is real: decisions trace to observed evidence, and the framework is adapted to context.

## Related methods
- [[requirements-and-stories]] · [[project-management]] · [[roadmapping]] · [[metrics-and-experimentation]]
