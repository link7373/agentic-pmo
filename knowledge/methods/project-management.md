# Method: Project & Program Management

Project management delivers a defined outcome within constraints by planning the work, coordinating people
and dependencies, managing risk, and communicating status. It complements agile delivery: agile manages
*how* the team builds; project/program management manages *scope, schedule, dependencies, risk, and
stakeholders* across the whole effort. Use the lightest process that keeps the work coordinated and predictable.

## The triple constraint (and quality)

Scope, schedule, and cost are interdependent — change one and at least one other must give, with quality at
the center. Make the trade-off explicit when pressure hits: "If we add this scope, we move the date or add
people." Never silently absorb scope by sacrificing quality.

## Scope & Work Breakdown Structure (WBS)

- Define scope as deliverables and acceptance criteria; state what's out of scope.
- Decompose deliverables into a **WBS** — a hierarchy of work packages small enough to estimate, assign,
  and track. The lowest level should be a unit you can confidently size and own.

## Scheduling & critical path
- Sequence work by dependencies; estimate durations; identify **milestones** (meaningful checkpoints).
- The **critical path** is the longest chain of dependent tasks — it determines the earliest finish. Slip on
  the critical path slips the project; protect it and watch near-critical paths too.
- Track **dependencies** explicitly (finish-to-start is most common). Cross-team dependencies are the most
  common cause of delay — surface and manage them actively.

## RAID log (risks, assumptions, issues, dependencies)

The PMO's running register of what could derail delivery:
- **Risks** — uncertain future events. Track probability × impact; assign an owner; plan response
  (avoid / mitigate / transfer / accept) and a trigger.
- **Assumptions** — things taken as true for planning; revisit as evidence arrives (assumptions that fail
  become risks or issues).
- **Issues** — problems happening now; assign owner, severity, and resolution path.
- **Dependencies** — internal/external reliances; track direction, owner, needed-by date, and status.

Review the RAID log on a regular cadence; escalate top risks/issues in status reports.

## Risk management loop
Identify → assess (probability × impact) → prioritize → plan response → assign owner → monitor → review.
Keep a small "top risks" list visible; don't let the register become a graveyard.

## Stakeholder management
- **Map stakeholders** by influence × interest; tailor engagement to each quadrant (manage closely / keep
  satisfied / keep informed / monitor).
- **RACI** clarifies who is **R**esponsible, **A**ccountable (one), **C**onsulted, **I**nformed per decision
  or deliverable. Resolve any cell with zero or multiple Accountables.
- Match communication frequency and depth to each audience (see `communication-standards.md`).

## Change control
Manage scope changes deliberately: capture the request, assess impact on scope/schedule/cost/risk, get the
right approval, then update plan and baselines. Prevents silent scope creep while staying responsive.

## Status reporting & health
- **RAG status** (Red / Amber / Green) for overall and per-workstream health, with the *reason* and the
  *action* — never a color alone.
- A good status report states: progress since last, what's next, decisions/help needed, top risks/issues,
  and any change to scope/schedule/budget. Lead with what the audience must act on.

## Program & portfolio coordination
- A **program** coordinates related projects to deliver outcomes none could alone; manage shared
  dependencies, sequencing, and benefits, not just individual schedules.
- At **portfolio** level, balance the mix against strategy and capacity; sequence by value and dependency,
  and protect against over-committing the system (limit WIP at the org level too).

## Quality checklist
- [ ] Scope, schedule, cost trade-offs are explicit when pressure arises; quality isn't silently traded.
- [ ] Critical path and cross-team dependencies are identified and actively managed.
- [ ] RAID log is current; top risks/issues have owners and are escalated.
- [ ] RACI has exactly one Accountable per decision/deliverable.
- [ ] Status reports lead with decisions/help needed and give the reason behind any RAG color.

## Related methods
- [[agile-scrum-mechanics]] · [[roadmapping]] · [[launch-and-gtm]] · [[product-strategy]]
