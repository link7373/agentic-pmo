# Operating Rhythm

> The PMO's cadence — what happens daily, weekly, per sprint, monthly, and per quarter. The Head of PMO follows this
> to run a *rhythm* rather than only reacting to one-off requests. Confirm/adjust during `/setup-pmo` to
> match the team. Each entry names the skill that does the work, so the rhythm is executable.

## Daily
- **Standup** — `/run-ceremony` (standup): inspect progress to the Sprint Goal; capture impediments.
- **Intake sweep** — `/capture-feedback`: log new inbound signals into `knowledge/intake.md`.

## Weekly
- **Triage** — review open intake; route items (explore / backlog / roadmap / decline).
- **Backlog refinement** — `/groom-backlog`: keep top items at Definition of Ready.
- **Status** — `/track-status`: RAG health, velocity/burndown, RAID update; share via `/make-deliverable`.
- **Portfolio intake QA** — `/review-portfolio-intake`: check submissions for completeness and currency;
  return specific asks to named owners before gaps compound.

## Per sprint
- **Planning** — `/plan-sprint` + `/run-ceremony` (planning): set one Sprint Goal, commit ready work.
- **Review** — `/run-ceremony` (review): inspect the increment with stakeholders; adapt the backlog.
- **Retro** — `/run-ceremony` (retro): a few specific, owned improvements.
- **Capacity look-ahead** — `/plan-capacity` when load or staffing is changing.

## Monthly (the portfolio cycle)
- **Intake close** — `/review-portfolio-intake`: gate the cycle's submissions; set confidence per item.
- **Resource refresh** — `/manage-resources`: update allocations, utilization and vendor status before any
  capacity conclusion is drawn from them.
- **Demand & capacity** — `/track-portfolio`: supply vs. demand by role, collisions, the binding constraint;
  hand scenarios to `/plan-capacity` when a re-balance is needed.
- **Financial cycle** — `/track-financials`: actuals against baselines, CPI/EAC where a baseline exists,
  envelopes at risk, and any benefit whose review window has opened.
- **Portfolio rollup** — `/track-portfolio`: two-tier report — delivery detail and the leadership rollup.
- **Steering committee** — `/make-deliverable` from `templates/steerco-pack.md`, if one is configured in
  `knowledge/governance.md`. Decisions needed first; everything green in the appendix.

## Per quarter (or planning cycle)
- **Strategy & OKRs** — `/define-strategy`: set/refresh objectives and key results.
- **OKR review** — `/review-okrs`: grade last cycle, carry learnings forward.
- **Roadmap** — `/build-roadmap`: re-prioritize Now/Next/Later against new goals.
- **Portfolio sequencing** — `/coordinate-program`: rebalance across teams and dependencies, on the collision
  and constraint data `portfolio-analyst` supplies from the monthly cycle.
- **Lessons review** — read `knowledge/lessons-learned.md` before planning the next cycle, and convert any
  pattern seen three times into a change to a standard, template, or skill. A repository only written to is
  an archive.

## Continuous (event-driven)
- **Discovery** — `/run-discovery` whenever a risky assumption needs validating before build.
- **Business case** — `/build-business-case` before committing significant money to an initiative.
- **PRD → prioritize** — `/write-prd`, `/prioritize` as initiatives mature.
- **Gate reviews** — `/run-gate-review` at each gate defined in `knowledge/governance.md`.
- **Change requests** — `/manage-change` whenever approved scope, schedule, or cost would move.
- **Launch** — `/plan-launch` before any notable release; post-launch review after.
- **Closure** — `/close-project` at completion *or cancellation*. Cancellations carry the best lessons and are
  the most likely to be skipped.

## Automation note
This rhythm is executable today by invoking the named skills on cadence. The recurring items (standup,
weekly status, sprint events) can also be automated with scheduled routines so the PMO prompts the team
on time rather than waiting to be asked.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
