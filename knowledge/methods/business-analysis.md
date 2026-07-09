# Method: Business Analysis

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

Business analysis is the discipline of understanding a need, defining a change that satisfies it, and making
sure the resulting solution actually delivers value. It sits upstream of and alongside product and delivery
work: it turns fuzzy problems and stakeholder demands into clear, traceable, testable requirements — and it
evaluates whether the solution, once built, is worth what it cost. Use it whenever the problem is unclear,
the stakeholders disagree, the process is complex, or the requirements are ambiguous.

## The core concept model (six ideas held in balance)

Every analysis balances six interlocking concepts — change one and reconsider the rest:

- **Change** — the transformation you're making (to a process, product, or capability), in response to a need.
- **Need** — the problem or opportunity that motivates the change. Analyze needs before solutions.
- **Solution** — a specific way of satisfying the need. There are always several; compare before committing.
- **Stakeholder** — anyone affected by, or influencing, the change (users, sponsors, ops, support, regulators).
- **Value** — the worth of the change to stakeholders in a context: benefits gained less costs and losses.
- **Context** — the environment (constraints, culture, systems, market) that the change lives in.

State the six for any initiative; if you can't name the need, value, and affected stakeholders, you're not
ready to define a solution.

## Requirements classification

Separate requirements by *what they describe* — mixing levels is a common source of confusion:

- **Business requirements** — goals/outcomes the organization wants (the *why*). Highest level.
- **Stakeholder requirements** — what a specific stakeholder group needs from the solution.
- **Solution requirements** — what the solution must do:
  - **Functional** — behaviors and information the solution handles.
  - **Non-functional (quality attributes)** — how well it must perform (see below).
- **Transition requirements** — temporary capabilities needed to move from current to future state (data
  migration, training, cutover). They disappear once the change is done.

## Elicitation (prepare → conduct → confirm)

Requirements are *elicited*, not simply collected — stakeholders rarely hand you complete, correct needs.

1. **Prepare** — pick techniques for the goal, identify participants, gather materials, set logistics.
2. **Conduct** — draw out needs actively; probe the *why*; separate stated wants from underlying needs.
3. **Confirm** — play findings back to stakeholders; resolve conflicts and gaps before you build on them.

Match the technique to the situation:

| Goal | Technique |
|------|-----------|
| Deep individual understanding | **Interviews** (structured or open) |
| Cross-stakeholder alignment, fast convergence | **Workshops**, **collaborative games** |
| See real behavior, not reported behavior | **Observation** (shadowing, apprenticing) |
| Broad input at scale, quantify sentiment | **Surveys / questionnaires** |
| Understand existing system/rules | **Document analysis** |
| Generate options, open the space | **Brainstorming** |
| Reactions to a concept in group | **Focus groups** |
| Make an abstract solution concrete | **Prototyping** (from sketch to interactive) |

## Current state → future state → gap → change strategy

Frame most analysis as a journey between two states:

1. **Analyze the current state** — how things work today, the pain, and the boundaries of the problem.
2. **Define the future state** — the target condition and the measurable business objectives that define success.
3. **Gap analysis** — the difference between the two; the capabilities to add, change, or remove.
4. **Change strategy** — the approach to cross the gap (increments, phases, pilots), plus transition needs
   and the risks of the change itself.

## Process analysis & modeling

- **As-is / to-be models** — map the current process, then design the improved one; the delta is the change.
- **Functional decomposition** — break a capability or process into smaller parts until each is understandable
  and ownable.
- **Root cause analysis** — get past symptoms to causes before designing a fix:
  - **5 Whys** — ask "why" repeatedly until you reach a root cause you can act on.
  - **Cause-and-effect (fishbone)** — group candidate causes by category to structure the hunt.
- Model to *communicate and decide*, not to document for its own sake — the lightest model that aligns people wins.

## Requirements lifecycle & traceability

Requirements are managed from inception to retirement, not written once:

- **Trace** — link each requirement backward to the need/goal it serves and forward to the design, build, and
  test that satisfy it. Traceability enables impact analysis and coverage checks.
- **Maintain** — keep requirements current and reusable as things change.
- **Prioritize** — order by value, risk, dependency, cost/time, and regulatory or policy constraints
  (see `prioritization-frameworks.md`).
- **Assess changes** — evaluate every proposed change for benefit, cost, impact, and risk before accepting it.
- **Approve** — get the right stakeholders to formally agree before work proceeds.

## Verify vs. validate requirements

- **Verify** — are the requirements *well-formed*? Clear, consistent, feasible, testable, unambiguous. (Built right.)
- **Validate** — do the requirements *deliver the intended value* and align to the business need? (Right thing.)

Both matter: a beautifully specified requirement for the wrong outcome still fails.

## Non-functional requirements (quality attributes)

Easy to forget, expensive to retrofit. Specify measurable targets, not adjectives:

- Performance & scalability · availability & reliability · security & privacy · usability & accessibility ·
  compatibility & portability · maintainability & supportability · compliance & auditability.
- "Fast" is not a requirement; "95th-percentile response under 300 ms at 1,000 concurrent users" is.

## Decision analysis

When a choice is hard, make the reasoning explicit: define options, criteria, and weights; score each option;
surface trade-offs and the assumptions behind them. Model recurring operational decisions (decision tables)
so business rules are transparent and consistent. Log consequential decisions to `decision-log.md`.

## Solution evaluation (did it work?)

After delivery, close the loop:

- **Measure solution performance** against the value and objectives set for the future state.
- **Assess limitations** — is the solution itself underperforming, or is the surrounding organization the
  constraint? Different problems, different fixes.
- **Recommend actions** — increase value, adjust, or retire. Solutions that no longer earn their keep should
  be sunset deliberately.

## Quality checklist
- [ ] Need, value, affected stakeholders, and context are named before any solution is chosen.
- [ ] Requirements are classified (business / stakeholder / solution / transition) and traceable to a need.
- [ ] Elicitation technique fits the goal; findings confirmed with stakeholders before building on them.
- [ ] Non-functional requirements are specified with measurable targets.
- [ ] Requirements are both verified (well-formed) and validated (deliver value).
- [ ] Post-delivery, solution performance is measured against the objectives that justified it.

## Related methods
- [[requirements-and-stories]] · [[discovery-and-validation]] · [[project-management]] · [[prioritization-frameworks]] · [[metrics-and-experimentation]]
