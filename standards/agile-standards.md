# Standards: Agile Delivery

Conventions for backlog items, estimation, and the agile cadence. These are house defaults; confirm and
tune them during `/setup-pmo` to match the team's methodology and tools. Mechanics live in
`knowledge/methods/agile-scrum-mechanics.md`; this file is the team's agreed conventions.

## Backlog item hierarchy
- **Epic** → **Story** → **Task**. Bugs and spikes are first-class items.
- Spikes are time-boxed research items with a question to answer, not open-ended work.

## User story format
```
As a <user/persona>, I want <capability>, so that <benefit/outcome>.
Acceptance criteria:
- Given <context>, when <action>, then <expected outcome>.
- ... (cover happy path, key edge cases, error states)
```
Stories must satisfy **INVEST**. Split oversized stories into thin end-to-end slices.

## Definition of Ready (default)
A story may enter sprint planning when it:
- [ ] Describes user value clearly and is sized/estimated.
- [ ] Has testable acceptance criteria.
- [ ] Has dependencies identified and blockers cleared.
- [ ] Is small enough to complete within one sprint.

## Definition of Done (default)
An increment is done when it is:
- [ ] Implemented to acceptance criteria, reviewed, and tested.
- [ ] Integrated and not breaking the build; no known critical defects.
- [ ] Documented as needed and potentially releasable.
(Strengthen over time; "done" means done — not "done except…")

## Estimation
- **Story points** on a modified Fibonacci scale (1, 2, 3, 5, 8, 13, 20, 40, 100).
- Estimate **relatively** (effort + complexity + uncertainty), not in hours.
- Use **Planning Poker** to surface differing assumptions; discuss outliers, re-estimate.
- **T-shirt sizes** (S/M/L/XL) for epics/early estimation.
- Velocity = average points completed over recent sprints; used for **forecast ranges**, never as a target
  or for cross-team comparison.

## Cadence (defaults — confirm at setup)
- Sprint length: 2 weeks (configurable).
- Events: Planning, Daily standup, Review, Retrospective; ongoing Backlog Refinement.
- Each sprint has exactly one **Sprint Goal**.

## Board & flow conventions
- Columns reflect the real workflow (e.g., Backlog → Ready → In Progress → In Review → Done).
- Apply **WIP limits** to keep flow healthy; track cycle time and throughput.
- A burnup ceiling that keeps rising signals scope creep — flag it.

## Metrics
- Track velocity (forecasting), burndown/burnup (progress + scope change), and cycle time/throughput (flow).
- Use metrics to improve the system in retrospectives — never to rank individuals.
