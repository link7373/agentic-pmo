# Method: Financial Management

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

Money is the constraint that makes prioritization real. This method covers the four financial jobs a PMO
actually does: justify an investment (business case), set and hold a cost baseline, forecast honestly, and
check afterward whether the promised benefit arrived. The registers live in `knowledge/financials.md`.

The discipline underneath all of it: **every figure is labelled measured or estimated.** A forecast presented
with the same confidence as an actual is worse than no forecast, because it survives into decisions that
should have paused for better data.

## Building a business case

A business case answers one question: *is this the best use of this money, compared with the alternatives?*
That framing forces two things weak cases skip.

**Always include the do-nothing option.** Not as a formality — priced. What does the current state cost over
the appraisal period in lost revenue, manual effort, risk exposure, or attrition? Many cases that look
marginal against zero look obvious against a properly costed status quo, and some that look compelling turn
out to beat a do-nothing baseline that was already improving on its own.

**Cost the whole life, not the build.** Total cost of ownership includes licences, hosting, support,
maintenance, training, and the decommissioning of whatever this replaces. Build cost is usually the minority
of a multi-year number, which is why cases justified on build cost alone tend to come back for more money.

Separate one-off from recurring cost, because they come from different budgets and are approved by different
people.

## Appraising the numbers

| Measure | Formula | What it tells you | Where it misleads |
|---------|---------|-------------------|-------------------|
| ROI | `(Net benefit − Cost) / Cost` | Simple return ratio | Ignores timing entirely |
| Payback period | Time until cumulative benefit = cost | Liquidity and risk exposure | Ignores everything after payback |
| NPV | `Σ (Cash flow_t / (1+r)^t)` | Value in today's money | Sensitive to the discount rate chosen |
| IRR | Discount rate where NPV = 0 | Comparable rate across options | Unstable with irregular cash flows |

Use at least two. ROI alone rewards a project that returns everything in year five over one that returns it in
year one. Payback alone rewards short-termism.

**Run the sensitivity.** Halve the main benefit, add 50% to the main cost, and see whether the recommendation
survives. If the case only works at the optimistic end of every assumption, that is the finding — state it,
rather than letting a single headline number carry a decision it can't support.

## Benefit types, and the honesty problem

- **Cash benefit** — money that actually arrives or stops leaving. Verifiable in the accounts.
- **Cost avoidance** — spend that would have happened but won't. Real, but invisible in the accounts, so it
  needs a named counterfactual agreed in advance.
- **Productivity benefit** — hours saved. Only becomes financial if those hours are *redeployed or removed*.
  Twenty people saving an hour a week is not a headcount reduction unless someone acts on it; claim it as
  capacity, not cash, unless there is a concrete plan.
- **Non-financial benefit** — risk reduction, compliance, customer satisfaction, strategic optionality. Claim
  it openly rather than inventing a monetary proxy that nobody believes.

Every benefit needs an **owner who will still be there** when it's measured, and a **measurement method that
exists today**. A benefit whose measurement requires instrumentation nobody has built is not a benefit yet.

## Cost baselines

The baseline is the approved cost plan against which variance is measured. It has three properties:

1. **Time-phased** — spend spread across the schedule, not a single total. Without phasing you cannot tell
   "under budget" from "behind schedule."
2. **Includes contingency reserve** for identified risks; **excludes management reserve** for unknown-unknowns,
   which sits outside the baseline and is released deliberately.
3. **Changes only through change control.** A baseline that quietly moves makes every variance number
   meaningless. Re-baselining is legitimate and normal — doing it without recording it in
   `knowledge/change-log.md` is not.

Projects too small or too uncertain to warrant a baseline simply don't get one. That is a valid choice; the
consequence is that earned value is unavailable for them, and the honest answer to "what's the CPI?" is that
there isn't one.

## Earned value, the cost side

The full mechanics live in [[project-management]]. What matters financially:

**CPI = EV / AC** — the value received per unit spent. CPI of 0.8 means eighty cents of delivered value per
dollar. Its power is that it is stable early: by roughly 20% complete, CPI is usually a better predictor of
final cost than any re-estimate the team produces, because the same conditions that caused the overrun keep
operating.

**EAC = BAC / CPI** is the default forecast — it assumes past efficiency continues. Use `EAC = AC + (BAC − EV)`
only when you can name what specifically changed to make the remaining work behave differently. "We'll catch
up" is not that.

**VAC = BAC − EAC** is the forecast variance at completion, and it is the number a sponsor actually wants.

Earned value requires a credible EV, which requires objective completion criteria per work package. Percent-
complete reported by the person doing the work is not objective — use 0/100 or 0/50/100 rules on small packages
instead.

## Forecasting discipline

- Forecast the **remaining** work, not the total. Sunk cost is data, not a decision input.
- Update the forecast when reality changes, not on the reporting calendar. A forecast unchanged for three
  periods across a visibly deteriorating project is a reporting artifact, not a forecast.
- Give a **range** with the drivers named. A single number implies a precision that doesn't exist.
- Never let the forecast converge on the baseline because that's the comfortable answer. The gap between them
  is the most useful signal the PMO produces.

## Benefits realization

Delivery ends; benefits start. The gap between them is where most claimed value quietly disappears.

1. **Baseline before you change anything.** A benefit measured only after the fact has no counterfactual.
2. **Hand over at closure**, in the closure report, to an owner outside the project team with a first review
   date. Project teams disband; benefits take quarters.
3. **Review on the schedule the business case set**, and record the actual against the claim in the benefits
   register — including when it didn't arrive.
4. **Feed the answer back into estimating.** An organization that never checks its benefit claims will keep
   approving the same optimistic cases forever. This loop, not any individual case, is what makes financial
   governance worth having.

## Capital vs. operating expenditure

Some work can be capitalized (spread across future periods) and some cannot; the rules vary by jurisdiction and
accounting policy. The PMO's job is not to make that call — it is to **record which treatment finance applied**
so cost reporting is consistent, and to flag when a scope change moves work between categories, because that
changes the budget it lands on.

## Quality checklist
- [ ] Do-nothing option costed, not just listed.
- [ ] Whole-life cost, with one-off and recurring separated.
- [ ] At least two appraisal measures, plus a sensitivity run.
- [ ] Every benefit has a type, an owner, a measurement method that exists, and a start date.
- [ ] Every figure labelled measured or estimated, with its basis.
- [ ] Cost baseline is time-phased, reserves explicit, and changes only via change control.
- [ ] EVM reported only where a baseline exists; absence stated plainly rather than approximated.
- [ ] Forecast covers remaining work, carries a range, and moves when reality does.
- [ ] Benefits handed to a named owner at closure with a first review date.

## Related methods
- [[project-management]] · [[portfolio-management]] · [[governance-and-change]] · [[product-strategy]] ·
  [[prioritization-frameworks]]
