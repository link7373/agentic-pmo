# Method: Project & Program Management

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

Project management delivers a defined outcome within constraints by planning the work, coordinating people
and dependencies, managing risk, and communicating status. It complements agile delivery: agile manages
*how* the team builds; project/program management manages *scope, schedule, dependencies, risk, and
stakeholders* across the whole effort. Use the lightest process that keeps the work coordinated and predictable.

## Guiding principles

Modern delivery is principle-led, not process-led. Let these shape judgment when the playbook runs out:

- **Focus on value** — tie every activity to the outcome it produces; kill work that doesn't.
- **Build quality in** — embed quality into process and deliverables, don't inspect it in at the end.
- **Hold a holistic, systems view** — decisions ripple; watch the whole, not just your slice.
- **Be an accountable, empowering leader** — own outcomes; push decisions to the people closest to the work.
- **Tailor to context** — match the approach to the project (see *Tailoring* below); there is no one right way.
- **Navigate complexity and optimize risk responses** — expect uncertainty; make it visible and manage it.
- **Enable change and adaptability** — help people adopt the change, not just receive the deliverable.

## Development approach & delivery cadence

Pick the approach that fits the work, then tailor:

- **Predictive (plan-driven)** — scope is well understood and stable; plan thoroughly up front, deliver in
  sequence. Best when requirements are clear and change is costly.
- **Adaptive (agile/iterative)** — requirements are uncertain or evolving; deliver in short increments and
  learn. Best when feedback is cheap and change is expected.
- **Hybrid** — mix the two (e.g., predictive infrastructure with adaptive feature build). Most real programs.

Decide the **delivery cadence** — one-time, multiple, or continuous delivery — from how often value can and
should reach users. Approach and cadence are choices to revisit, not defaults to inherit.

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

## Estimating techniques

Estimates are ranges, not promises — state confidence and refine as you learn (progressive elaboration):

- **Analogous** — scale from a similar past project. Fast, rough; good early when little is known.
- **Parametric** — multiply a measured rate by quantity (e.g., cost per unit × units). Accurate when you have
  reliable historical rates.
- **Bottom-up** — estimate each work package and roll up. Most accurate, most effort; use once scope is decomposed.
- **Three-point (PERT)** — combine optimistic (O), most-likely (M), and pessimistic (P) to account for
  uncertainty: `Expected = (O + 4M + P) / 6`. Widen the range where risk is high.

Hold **reserves** deliberately: **contingency reserve** for known risks (inside the baseline), **management
reserve** for unknown-unknowns (outside it). Don't pad every task silently — reserve explicitly and manage it.

## Earned Value Management (objective progress)

EVM measures progress by *value delivered*, not effort spent or time elapsed. Three inputs:

- **PV** (Planned Value) — budgeted cost of work scheduled by now.
- **EV** (Earned Value) — budgeted cost of work actually completed.
- **AC** (Actual Cost) — what that completed work actually cost.

Derive health from them:

| Measure | Formula | Reading |
|---------|---------|---------|
| Schedule Variance | `SV = EV − PV` | < 0 behind schedule |
| Cost Variance | `CV = EV − AC` | < 0 over budget |
| Schedule Performance Index | `SPI = EV / PV` | < 1 behind schedule |
| Cost Performance Index | `CPI = EV / AC` | < 1 over budget |
| Estimate at Completion | `EAC = BAC / CPI` | forecast total cost |
| To-Complete Performance Index | `TCPI = (BAC − EV) / (BAC − AC)` | efficiency needed to finish on budget |

A CPI of 0.8 means you're getting 80 cents of value per dollar spent — a far earlier, harder signal than a
green status. Use EVM where a cost/schedule baseline exists; pair with burndown/velocity on adaptive work.

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

## Tailoring the approach

There is no universal process — deliberately adapt the method to the project's size, risk, complexity, team
maturity, and organizational context. Start from a sensible default, then add ceremony only where it earns its
keep and strip it where it doesn't. Tailoring is a first-class decision: make it explicitly, revisit it, and
avoid both under-managing (chaos) and over-managing (bureaucracy that slows value).

## Quality checklist
- [ ] Scope, schedule, cost trade-offs are explicit when pressure arises; quality isn't silently traded.
- [ ] Critical path and cross-team dependencies are identified and actively managed.
- [ ] RAID log is current; top risks/issues have owners and are escalated.
- [ ] RACI has exactly one Accountable per decision/deliverable.
- [ ] Status reports lead with decisions/help needed and give the reason behind any RAG color.
- [ ] Development approach and cadence are chosen deliberately and tailored to context.
- [ ] Estimates state confidence; reserves are explicit; progress is measured by value delivered, not effort spent.

## Related methods
- [[agile-scrum-mechanics]] · [[roadmapping]] · [[launch-and-gtm]] · [[product-strategy]] · [[business-analysis]]
