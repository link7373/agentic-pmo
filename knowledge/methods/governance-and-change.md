# Method: Governance, Change Control & Closure

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

Governance is the set of decisions the PMO does *not* make on its own — which work gets funded, when it
proceeds, what changes are accepted, and when something stops. Done well it is a small number of clear
decision points with named deciders. Done badly it is a review calendar that consumes delivery capacity and
approves everything anyway. The configuration for a specific org lives in `knowledge/governance.md`.

The test for any governance mechanism: **name a decision it has changed.** A gate that has never held anything,
a committee that has never said no, a change process that approves everything raised — these are cost without
control, and removing them is the right call.

## Stage gates

A gate is a go/no-go decision point where evidence is checked against pre-agreed criteria before more money is
committed. Its purpose is not to check the team is working hard; it is to make **stopping a legitimate,
low-drama outcome** at a point where stopping is still cheap.

A workable default:

| Gate | Question | Kill is most valuable here because |
|------|----------|-----------------------------------|
| G0 Idea | Worth investigating? | Almost nothing is sunk |
| G1 Business case | Worth funding? | The last point before real money |
| G2 Plan approved | Is the plan credible? | Estimates now rest on real design |
| G3 Ready to launch | Safe to ship? | Reputational cost is ahead, not behind |
| G4 Closure | Did it deliver, and what did we learn? | The only gate that improves future estimates |

Four properties separate a gate from a status meeting:

1. **Criteria agreed before the work starts**, so the bar can't be adjusted to fit what was delivered.
2. **A named decider** with the authority to stop it. A gate whose decider cannot say no is a briefing.
3. **Evidence, not assertion.** "Testing is complete" is a claim; a test report is evidence.
4. **Four possible outcomes** — go, go-with-conditions, hold, kill. Conditions carry an owner and a date, or
   they are decoration.

**The sunk-cost trap** is the reason gates exist and also the reason they fail. By G3 the money is spent and
killing feels like waste, so committees approve. The counter is to frame the question strictly forward:
ignoring everything already spent, is the *remaining* cost the best use of that money? Recording dissent in the
gate record matters here — it is the only thing that makes an override visible later.

## Decision rights

Most governance dysfunction is not missing process; it is unclear authority. Write down, per decision type, the
threshold, the approver, who is consulted, and where it escalates. Two rules keep it honest:

- **Push authority down until it hurts.** Every decision escalated is delay plus a decision made further from
  the information.
- **One accountable per decision.** Committees consult; individuals decide. A decision "owned by the steering
  committee" is owned by nobody.

## Steering committees

A steerco earns its cost only if it decides things. Structure the pack around **decisions needed first**, then
exceptions, then health. Anything green belongs in an appendix — reading status aloud to people who received
the pack is the single most common way these meetings become theatre.

Circulate far enough ahead that the meeting is for deciding, not for reading. If the same items appear as
"decisions needed" three meetings running, the problem is decision rights, not the pack.

## Escalation

An escalation path needs three things: a **trigger** (usually a RAID score threshold or a category like
regulatory exposure), a **destination**, and a **response time** — time to first substantive response, not to
resolution. Without the response time, escalation is a message into a void.

Escalation is not failure or blame. Treat it as a routing decision: this needs authority or resources the
current level doesn't have. Teams that are punished for escalating stop escalating, and the PMO loses its
early warning entirely.

## Risk scoring and appetite

Score = probability × impact, both on a 1–5 scale, giving 1–25. The scales are only useful if **impact levels
are defined in this organization's terms** — money, schedule days, customers affected, regulatory exposure.
Left undefined, "major" means whatever the person filling in the register felt that morning, and the scores
aren't comparable across projects, which is the entire point of scoring.

**Risk appetite** states what the org will accept, per category, in plain language. It is what lets a team act
without asking: an org that is *open* on schedule risk and *averse* on compliance risk has told its projects
how to trade off. Appetite that only exists as an adjective ("balanced") tells nobody anything — pair each with
a concrete consequence.

Watch two known distortions: scores cluster at the middle when people avoid extremes, and a risk owned by the
person who scores it tends to score low. Periodic calibration across projects catches both.

## Change control

A change is anything that moves **approved scope, schedule, or cost**. Work that fits inside the baseline is
not a change — inflating the change log with normal backlog churn buries the changes that matter.

The loop: capture → assess impact separately on each dimension → present options with a recommendation →
decide with a named approver → **re-baseline** → communicate.

Two failure modes bracket this:

- **Too heavy** — a formal CR for a two-day adjustment. Teams route around it, and the log stops reflecting
  reality. Set a threshold below which the project manager just decides.
- **Too light** — changes absorbed silently "to be helpful." Scope creep is rarely one big decision; it is
  thirty small accommodations nobody logged. By the time the variance shows, no one can reconstruct where it
  went.

**The re-baseline is the step that gets skipped**, and skipping it is what makes every subsequent variance
report meaningless. Approving a change without updating the plan and the cost baseline means the project is
now measured against a target everyone has already agreed is wrong.

On adaptive work, scope inside a fixed capacity flexes by design and does not need a CR each time; the *fixed*
things — the budget envelope, the date, the outcome committed to — are still baselined and still change-
controlled.

## Closure

Projects that fade out rather than close cost the organization three things: resources never formally
released, benefits nobody owns, and lessons never captured.

Closure is a real activity with a checklist: deliverables accepted or formally descoped, final actuals
recorded, benefits handed to named owners with review dates, open RAID entries resolved or transferred or
explicitly accepted, resources released, contracts closed, register row set to Closed.

**Cancelled projects need closure most.** They carry the most valuable lessons and are the most likely to be
skipped because nobody wants to write the report. A cancellation closed cleanly, with the reasoning recorded,
is a functioning portfolio doing its job.

## Lessons learned

The reason lessons-learned repositories usually fail is that they are written but never read. Three habits fix
that:

1. **A lesson must imply a change in behavior.** "Communication could have been better" is a feeling.
   "We sized the migration from the vendor's row counts, which excluded archived records — get a live count
   before baselining" is a lesson.
2. **Convert repeats into systemic change.** The same lesson three times is not bad luck; it is a defect in a
   standard, a template, or a skill. Change the artifact, then retire the lesson.
3. **Read them at the start**, not just write them at the end. A lessons review is a G1/G2 entry criterion or
   it is an archive.

## Assurance, lightly

Assurance asks whether the PMO's own reporting is trustworthy: does status reflect reality, do the numbers
reconcile to their sources, are approvals actually recorded. Keep it proportionate — a short periodic check
across a sample of projects, run by someone not reporting on them, finds most of what a heavyweight audit
would.

**Audit trail** is a by-product of doing the rest properly: the decision log, the change log, gate records,
and dated artifacts together reconstruct who decided what, when, and on what evidence. If an obligation
requires more than that, record it explicitly in `knowledge/governance.md` rather than assuming the
file-based record satisfies it.

## Tailoring

Governance is a cost, paid by delivery. Scale it to the risk, spend, and reversibility of the work — a
two-week internal tool and a regulated platform migration should not pass through the same gates. Record what
was deliberately skipped and why, so the light-touch path is a documented choice rather than an oversight
someone gets blamed for later.

## Quality checklist
- [ ] Every gate has criteria set in advance, a named decider who can say no, and four possible outcomes.
- [ ] Conditions of approval carry an owner and a date.
- [ ] Decision rights recorded per decision type with thresholds and escalation.
- [ ] Impact levels defined in this org's terms; appetite stated with concrete consequences.
- [ ] Escalation triggers name a destination *and* a response time.
- [ ] Change threshold set, so small adjustments don't need a CR and large ones can't skip it.
- [ ] Every approved change re-baselines the plan and the cost baseline.
- [ ] Closure checklist completed, including for cancelled projects.
- [ ] Lessons imply behavior change; repeats become systemic fixes.
- [ ] Tailoring decisions recorded, including what was deliberately skipped.

## Related methods
- [[project-management]] · [[financial-management]] · [[portfolio-management]] · [[resource-management]]
