# Operating Rhythm

> The PMO's cadence — what happens daily, weekly, per sprint, and per quarter. The Head of PMO follows this
> to run a *rhythm* rather than only reacting to one-off requests. Confirm/adjust during `/setup-pmo` to
> match the team. Each entry names the skill that does the work, so the rhythm is executable.

## Daily
- **Standup** — `/run-ceremony` (standup): inspect progress to the Sprint Goal; capture impediments.
- **Intake sweep** — `/capture-feedback`: log new inbound signals into `knowledge/intake.md`.

## Weekly
- **Triage** — review open intake; route items (explore / backlog / roadmap / decline).
- **Backlog refinement** — `/groom-backlog`: keep top items at Definition of Ready.
- **Status** — `/track-status`: RAG health, velocity/burndown, RAID update; share via `/make-deliverable`.

## Per sprint
- **Planning** — `/plan-sprint` + `/run-ceremony` (planning): set one Sprint Goal, commit ready work.
- **Review** — `/run-ceremony` (review): inspect the increment with stakeholders; adapt the backlog.
- **Retro** — `/run-ceremony` (retro): a few specific, owned improvements.
- **Capacity look-ahead** — `/plan-capacity` when load or staffing is changing.

## Per quarter (or planning cycle)
- **Strategy & OKRs** — `/define-strategy`: set/refresh objectives and key results.
- **OKR review** — `/review-okrs`: grade last cycle, carry learnings forward.
- **Roadmap** — `/build-roadmap`: re-prioritize Now/Next/Later against new goals.
- **Portfolio sequencing** — `program-manager`: rebalance across teams and dependencies.

## Continuous (event-driven)
- **Discovery** — `/run-discovery` whenever a risky assumption needs validating before build.
- **PRD → prioritize** — `/write-prd`, `/prioritize` as initiatives mature.
- **Launch** — `/plan-launch` before any notable release; post-launch review after.

## Automation note
This rhythm is executable today by invoking the named skills on cadence. The recurring items (standup,
weekly status, sprint events) can also be automated with scheduled routines so the PMO prompts the team
on time rather than waiting to be asked.
