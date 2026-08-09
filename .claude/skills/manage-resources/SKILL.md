---
name: manage-resources
description: Maintain the supply side of capacity — the people and roles register, allocations and utilization, vendor and contractor status, scarce-skill constraints, and forecast supply changes. Use before capacity planning, when onboarding or losing people, or when allocations stop adding up. Dispatches the resource-manager.
---

# /manage-resources — Who we actually have

## When to use
Before a capacity planning cycle, when people join or leave, when a contract is approaching its end, or when
someone asks "do we have the people for this?"

## Dispatches
`resource-manager` (lead) + `program-manager` (decides any rebalancing) + `financial-analyst` (vendor and
contractor cost).

## Inputs
`knowledge/resources.md` (the current register), `knowledge/cadence.md` (teams, calendar),
`knowledge/portfolio.md` and `knowledge/projects/` (what people are committed to),
`knowledge/financials.md` (vendor spend).

## Steps
1. **Refresh the register** — people, roles and skills, teams, employment type, and available FTE. Where leave
   or availability data hasn't been provided, record unknown; an assumed figure propagates into a capacity
   conclusion that looks computed.
2. **Work down from nominal to real.** Deduct leave, support and on-call, meetings and overhead, ramp, and
   context-switching — and show the deductions. A 1.0 FTE person typically delivers 0.5–0.7 FTE of project work.
3. **Reconcile allocations.** Percentage over a window, committed separated from proposed. **Anyone over 100%
   is a finding** — someone has committed capacity that doesn't exist. Flag anyone spread across three or more
   projects; switching cost is eating 20%+ of their time.
4. **Roll up utilization by role**, never by naming individuals in anything that will be seen outside this
   file. Treat sustained utilization above ~85% as a risk to surface, not an efficiency to report.
5. **Name the constraint.** Which scarce role or skill actually gates the portfolio, what it gates, and the
   lead time on each way of relieving it — hire, contract, train a second person, or redesign the work. Add
   key-person dependencies to `knowledge/raid-log.md`.
6. **Review vendors and contractors.** Contract ends are capacity cliffs: check each has a knowledge-transfer
   plan and a renewal decision date early enough that "we had no choice" isn't the reason for extending.
7. **Forecast the trajectory.** Joiners with ramp, leavers with notice, leave, planned hiring. Mark unstarted
   hiring as low-confidence supply or show it only as a scenario — capacity plans built on hiring that hasn't
   started are reliably wrong.

## Methods
`knowledge/methods/resource-management.md` (deductions, utilization, constraints, vendors, forecasting),
`knowledge/methods/portfolio-management.md` (how supply joins the demand cycle),
`knowledge/methods/agile-scrum-mechanics.md` (team velocity — a different unit, never added to FTE).

## Output
Updated `knowledge/resources.md` (people, allocations, utilization, vendors, constraints, planned changes);
key-person dependencies in `knowledge/raid-log.md`; findings feed `/plan-capacity`, whose plans land in
`knowledge/capacity/`. Log resourcing decisions to `knowledge/decision-log.md`. Follow
`standards/document-standards.md`.

## Privacy
This register names people. Never copy individual allocation or utilization rows into a deliverable, a
dashboard, or a message to leadership — roll up to role or team. Individual utilization shown upward turns a
planning tool into a performance instrument, and the data stops being honest the moment people notice.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
