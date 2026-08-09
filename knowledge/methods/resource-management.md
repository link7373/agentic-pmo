# Method: Resource Management

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

Capacity is the constraint that decides what a portfolio can actually take on, and it is the one most often
answered from optimism. This method covers the supply side — who is available, to what, at what cost, and where
the real constraint sits. The register lives in `knowledge/resources.md`; demand lives in
`knowledge/portfolio.md` and the project plans.

**Keep supply and demand in separate files and separate units.** The most common capacity error is arithmetic
that quietly mixes team velocity (story points) with named-person allocation (FTE) and produces a number that
means nothing. State which basis any conclusion rests on.

## What "available" actually means

Nominal headcount is not capacity. Work down from it deliberately:

| Deduction | Typical scale | Why it's missed |
|-----------|---------------|-----------------|
| Leave, holidays, sickness | 10–15% | Averaged away, then hits in one quarter |
| Support, on-call, escalations | 10–30% | Unplanned, so unbudgeted |
| Meetings, admin, org overhead | 10–20% | Invisible to the person planning |
| Onboarding & ramp | Weeks per joiner | New capacity counted from day one |
| Context switching across projects | 20%+ at three projects | Assumed free |

A "1.0 FTE" engineer typically delivers 0.5–0.7 FTE of project work. Planning to nominal capacity guarantees
overcommitment, and the shortfall surfaces as unexplained slippage rather than as the planning error it was.

**Ramp is not linear.** A person added to a project mid-flight consumes existing team capacity before adding
any — the classic result being that adding people to a late project makes it later.

## Utilization

Utilization above roughly 85% removes the slack that absorbs variability, and queue times grow non-linearly
past that point — the same effect that makes a motorway seize at 90% occupancy rather than flowing 90% as fast.
A portfolio planned to 100% utilization has no capacity to respond to anything, so every arrival becomes a
crisis and every estimate becomes wrong.

Treat sustained high utilization as a finding to surface, not an efficiency to report. And measure it by role,
never by naming individuals in anything stakeholder-facing.

## Constraints and scarce skills

Portfolio throughput is set by its constraint, not its average capacity. One database specialist, one person
who understands the billing system, one certified reviewer — these gate delivery regardless of how much
capacity exists elsewhere, and adding capacity away from the constraint changes nothing.

So: identify the constraint explicitly, sequence work around it, and treat relieving it (hiring, training a
second person, contracting, or redesigning the work to need it less) as a portfolio-level decision with its
own lead time. Key-person dependency is simultaneously a capacity constraint and a risk — it belongs in
`knowledge/raid-log.md` as well as the register.

## Allocation

- Express allocation as a **percentage over a window**, not a binary assignment. "60% to Project A from March
  through May" is plannable; "on Project A" is not.
- **Allocations over 100% for a person are a finding**, not a rounding error. Surface them; someone has
  committed capacity that doesn't exist.
- **Distinguish committed from proposed.** Proposed allocations on unapproved work are the main way a portfolio
  looks full before anything has actually been decided.
- **Fewer projects per person is faster overall.** Three concurrent projects can cost 20–40% of a person's time
  to switching. Two is usually the practical ceiling for meaningful contribution.

## Vendors and contractors

External capacity is real capacity with different properties: a lead time to onboard, a rate that hits
`knowledge/financials.md`, a contract end date that is a capacity cliff, and knowledge that leaves when they do.

Track scope of work, owner, contract type (time-and-materials shifts risk to you; fixed-price shifts it to
them and reduces your flexibility), dates, and rate basis. Two things to plan for deliberately: the **knowledge
transfer** before the contract ends, and the **renewal decision** early enough that "we had no choice" isn't
the reason for extending.

## Forecasting supply

The register is a snapshot; planning needs the trajectory. Record known changes — joiners with their ramp,
leavers with their notice period, contract ends, parental leave, planned hiring with a realistic time-to-
productive (typically months, not weeks, once recruitment and ramp are both counted).

Capacity plans built on hiring that hasn't started are the most reliably wrong artifacts a PMO produces. Mark
unstarted hiring as low-confidence supply, or exclude it and show it as a scenario.

## Answering "can we take this on?"

1. Available supply by role, after deductions.
2. Committed demand by role, from approved work.
3. The gap — and specifically at the **constraint**, not on average.
4. If the answer is no: the options are defer, descope, add capacity (with its lead time), or accept the
   overrun explicitly. Present all four; the choice belongs to `program-manager` and, where it costs money, to
   the sponsor per `knowledge/governance.md`.

An honest "no, unless something gives" delivered during planning is worth far more than a yes that becomes a
slipped date four months later.

## Privacy

This register names people and describes their commitments and utilization. Treat it as internal-restricted.
Roll up to role or team for anything stakeholder-facing or on a dashboard — individual utilization presented to
leadership turns a planning tool into a performance instrument, and the data stops being honest the moment
people notice.

## Quality checklist
- [ ] Supply stated after deductions, with the deductions shown.
- [ ] Supply and demand kept in separate units; the basis of any conclusion stated.
- [ ] Allocations expressed as % over a window; over-100% flagged; committed separated from proposed.
- [ ] The constraint identified by role, and sequencing built around it.
- [ ] Utilization above ~85% surfaced as a risk, not reported as efficiency.
- [ ] Vendor contract ends carry a knowledge-transfer plan and a renewal decision date.
- [ ] Unstarted hiring marked low-confidence or shown only as a scenario.
- [ ] Individual-level data kept out of stakeholder-facing artifacts.

## Related methods
- [[portfolio-management]] · [[project-management]] · [[agile-scrum-mechanics]] · [[financial-management]] ·
  [[governance-and-change]]
