# Method: Portfolio Management & Reporting

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

Portfolio management is the discipline of seeing *all* the work at once — every project and program, on one
comparable basis — so the organization can decide what to fund, what to sequence, and what to stop. Where
project management asks "is this delivering?" and program management asks "are these delivering together?",
portfolio management asks **"are we doing the right work at all, and can we actually staff it?"**

This method covers the analyst's half of that discipline: the *data layer*. Governance and investment
decisions belong to leadership; sequencing belongs to the program level. What belongs here is making the
picture trustworthy — a canonical register, a quality gate on what comes in, capacity analytics, and the
reporting and automation that carry it to each audience.

## Guiding principles

- **Trust before insight.** An analysis built on stale or invented data is worse than no analysis, because it
  gets believed. Gate the data first; say plainly what's missing.
- **One number, one definition.** Every measure is defined once and reused everywhere. Two dashboards that
  disagree about "on track" destroy more credibility than either creates.
- **Compare across, don't drill down.** The portfolio's value is comparison and pattern — themes, collisions,
  concentration. Depth on any single project belongs to that project's manager.
- **Same numbers, different altitude.** Leadership and delivery teams see the same underlying data, summarized
  differently. Never maintain two versions of the truth for two audiences.
- **Report the exception.** A portfolio report that lists everything hides everything. Lead with what has
  changed, breached, or needs a decision.
- **Inform the decision; don't take it.** Supply the evidence and the trade-off. Sequencing, funding, and
  stopping are other people's calls.
- **Automate the collection, not the judgment.** Machines move and validate data; humans interpret it.

## The three altitudes

| Altitude | Question it answers | Owns | Horizon |
|----------|--------------------|------|---------|
| **Project** | Is this deliverable on scope, schedule, cost? | A defined outcome and its constraints | Weeks–months |
| **Program** | Are these related efforts delivering a shared outcome? | Cross-project dependencies, sequencing, benefits | Months–quarters |
| **Portfolio** | Are we doing the right work, and can we staff it? | The mix, the capacity, the investment picture | Quarters–years |

Keep the altitudes distinct. The most common failure is a portfolio view that has collapsed into a long list
of project statuses — technically complete, decision-useless.

## Portfolio governance & stage gates

Work moves through stages; the register records which one each item is in. A minimal, tailorable set:

1. **Idea** — captured, not yet assessed. No capacity assumed.
2. **Assessed** — sized, strategically linked, rough capacity draw understood.
3. **Approved** — funded and slotted; capacity reserved.
4. **In flight** — actively delivering; reports status on the cadence.
5. **Closed** — delivered or stopped.
6. **Benefits review** — did the expected value actually arrive? (See *Benefits realization*.)

A **stage gate** is a decision point, not a formality: continue, change, hold, or stop. Every gate needs a
named decision-maker and a recorded outcome — log it in `decision-log.md`. Gates that only ever say "continue"
aren't gates; either enforce them or drop the ceremony.

## The portfolio register

The canonical record — one row per project or program, on a schema consistent enough to compare. Fields:

| Field | Why it's there |
|-------|----------------|
| ID · Name · Type (project/program) | Identity; programs roll up their children |
| Parent program | Enables rollup without duplicating rows |
| Sponsor · Manager | Who decides, who runs it — accountability for the data too |
| Stage | Where it sits in governance (above) |
| Strategic link | Which goal/OKR it serves — items with none are a finding, not an omission |
| Delivery approach | Predictive / adaptive / hybrid — determines which metrics are meaningful |
| Scope · Schedule · Cost status | The triple constraint, each with its own signal |
| Next milestone + date | The nearest falsifiable commitment |
| RAG + reason + action | Health, never a bare colour |
| Capacity draw | Demand by team or role — the input to capacity analysis |
| Top risk / dependency | The one thing most likely to derail it |
| Last updated · Confidence | Data currency and trust (see below) |

Two rules keep the register honest: **never invent a value to fill a cell** — mark it missing and attribute
the gap to an owner; and **never let a program's row contradict its children's rows** without saying so.

## Data quality & the intake contract

Project and program managers submit status; the analyst is accountable for whether it can be relied on. The
contract has four tests, applied *before* any analysis:

- **Complete** — every required field has a value or an explicit "not applicable/unknown".
- **Current** — updated within the reporting window. An unchanged update is not the same as a current one;
  check the timestamp, not just the content.
- **Consistent** — internally coherent (a green RAG next to a slipped milestone and a scope change is a
  contradiction), and coherent with adjacent sources (RAID log, roadmap, sprint data).
- **Credible** — the narrative and the numbers agree. Watermelon status — green outside, red inside — usually
  shows as a stable RAG with a steadily receding milestone date.

Record a **confidence** level per row:

| Level | Meaning | Effect on reporting |
|-------|---------|--------------------|
| **High** | Complete, current, consistent | Use freely |
| **Medium** | Minor gaps or slightly stale | Use, footnote the caveat |
| **Low** | Material gaps, stale, or contradictory | Report the gap itself; do not aggregate silently |
| **Missing** | No submission this cycle | Name it in the report with the owner |

**The feedback loop is the point.** Don't silently repair a bad submission — the same gap recurs next cycle.
Return it to the named manager with the specific field and a concrete ask ("the March milestone date has moved
twice while RAG stayed green — what's the revised date and the reason?"). Track chronic gaps; a manager who
misses three cycles is a portfolio risk, not an admin nuisance.

## Demand & capacity management

Run on a regular cycle (monthly suits most organizations — long enough to change, short enough to steer):

1. **Establish supply.** Available capacity by team or role — headcount, adjusted for leave, run/support load,
   and a realistic productive fraction. Supply is a range, not a number.
2. **Collect demand.** Estimated effort by period from each in-flight and approved item, plus a view of the
   assessed pipeline. Estimates state confidence and get refined as items mature.
3. **Compare and find the constraint.** Where demand exceeds supply, and — more usefully — *which specific
   role or team* is the binding constraint. Portfolios rarely run out of people in general; they run out of
   one scarce skill.
4. **Detect collisions.** Two or more items needing the same scarce team in the same window. Collisions are
   the highest-value finding a portfolio analyst produces, because they are invisible at project level — every
   colliding project is individually green.
5. **Run scenarios.** For each realistic option — defer, re-sequence, reduce scope, add capacity — show the
   effect on the constraint and the cost. Present options with consequences; let the decision-maker choose.

Watch **portfolio WIP**. Too many concurrent items is the most common cause of slow delivery, and the least
often diagnosed — everything is progressing, nothing is finishing. Track items in flight against a deliberate
limit, and treat throughput (items completed per period) as more honest than utilization.

## Portfolio KPIs & the balanced view

No single number describes a portfolio. Cover the dimensions, keep the set small, and define each one once:

- **Delivery** — milestone hit rate, schedule variance/SPI, throughput, cycle time from approval to delivery.
- **Financial** — cost variance/CPI, forecast vs. budget (EAC), spend by strategic theme.
- **Risk** — count and severity of open risks, aging issues, overdue mitigations, concentration of risk.
- **Capacity** — demand vs. supply by constrained role, collision count, portfolio WIP.
- **Strategic alignment** — share of investment per goal/OKR; items with no strategic link.
- **Data health** — submission completeness and currency rates. The measure of the reporting system itself.

Apply the usual metric hygiene (see `metrics-and-experimentation.md`): prefer trends to snapshots, don't react
to single-period noise, and be alert to any measure that can be improved without improving reality.

## Reporting layers & audience tiers

One semantic model, three altitudes:

| Tier | Audience | Contains | Cadence |
|------|----------|----------|---------|
| **Operational** | PMs, PgMs, POs | Their own submitted data reflected back; gaps and validation errors | Continuous / weekly |
| **Tactical** | Portfolio, delivery leads | Cross-portfolio themes, collisions, dependency clusters, capacity | Monthly |
| **Executive** | Leadership, board | Exceptions, decisions needed, investment vs. strategy, top risks | Monthly / quarterly |

Each tier is a **summarization** of the same model, never a separate dataset. The executive tier is not a
prettier operational report — it answers different questions and omits far more. If leadership routinely asks
for the detail behind a number, the drill path is missing, not the detail.

## Dashboard design principles

Applies to any BI surface — the discipline is tool-independent:

- **Start from the decisions**, not the data. List what each tier must decide; every visual earns its place by
  serving one. Visuals that serve none get cut.
- **One to three questions per surface.** A dashboard that answers everything answers nothing well. When the
  list grows past three, that is a second dashboard, not a bigger one.
- **Define the grain explicitly** — what one row means (one project per reporting period, one resource per
  period). Ambiguous grain is the root of most double-counting.
- **Measures live in one catalog** with name, plain-English definition, formula, and owner. "On track" must
  mean exactly one thing across the whole portfolio.
- **Design the drill path.** Executive summary → tactical breakdown → the underlying project row. Every
  aggregate should be traceable to its source in one or two clicks.
- **State refresh cadence and lineage** on the surface itself. A reader must know how old the data is and
  where it came from without asking.
- **Never a bare RAG.** A colour without a reason and an action is decoration.
- **Show data confidence**, not just values. A number derived from three low-confidence submissions should
  visibly say so.

## Specifying a surface someone else builds

The portfolio analyst specifies; a build capability implements. A specification is only finished if it can be
built from without a follow-up question, so a few decisions belong upstream rather than being left to the builder:

- **Model as a star schema with exactly one date table.** A fact table surrounded by dimensions — not one wide
  table, not snowflaked — honouring the organization's fiscal calendar. Keep relationships single-direction
  unless bidirectional is justified in writing; ambiguous filter paths produce *believable wrong numbers*,
  which is more dangerous than an error.
- **Treat the measure name as a contract.** The builder implements it character for character. A name that
  drifts between spec and surface is a defect, not a variation. Never let a new measure be invented during a
  build — it goes in the catalog first.
- **Compute ratios from summed numerator and denominator**, never as an average of ratios; the latter gives a
  wrong total row that nobody notices until a leader quotes it.
- **Give every page and visual a build-safe name** — letters, digits, underscores and hyphens only. Spaces and
  punctuation are discarded silently by some platforms, taking the whole object with them, and a later rename
  breaks the drill paths that referenced it.
- **Specify what a visual must show and why; leave how it looks to the builder's design standard.** Encode
  palette, status colours and typography once in a theme rather than formatting visuals individually — that is
  what keeps a standard holding across every page, and what makes a rebrand a one-file change.
- **Rendering is not done.** A surface is finished when every displayed number has been reconciled against an
  independent query and the empty state and a single-category filter have both been tested. Structural
  validity proves the files are well-formed; only use proves the report is right.
- **Mind what a portfolio surface leaks.** It carries sponsor and manager names, and saved filter or slicer
  selections can persist into the built report's own files — leaving a visual filtered to a named person
  writes that name into a stored artifact. Specify an impersonal default filter state. And keep the scope
  honest: these surfaces report the health of *work*, not the performance of *people*. Attributing a data gap
  to an owner exists so it gets fixed, not so anyone gets ranked.

## Automation patterns

The reporting cycle is mostly collection and validation — the two things machines do well and humans do
grudgingly. A standard flow:

**Trigger → collect → validate → transform → store → publish → notify**

- **Trigger** — schedule (cycle open/close) or event (a tracker item changes state).
- **Validate at the boundary.** Reject or quarantine bad input where it arrives, with a message naming the
  field and the fix. Validation downstream of storage means the bad data is already in the reports.
- **Be idempotent.** Re-running must not double-count or duplicate. Assume every flow runs twice.
- **Handle errors explicitly** — retry transient failures, escalate persistent ones to a named human. A flow
  that fails silently is worse than no flow; the report still renders, just wrongly.
- **Keep a human in the loop** for judgment: automate the chase, the validation, and the movement of data;
  never automate the interpretation of a RAG or the decision to escalate.
- **Preserve a manual fallback.** The cycle must be completable by hand when the automation is down.
- **Log the run** — what ran, when, how many records, what failed. This is the data-health metric's source.

## Benefits realization

The portfolio's honest scorecard is what happened *after* delivery. At closure, record the expected benefit,
its measure, and the date it should be observable; at the benefits review, compare against what actually
arrived and feed the delta back into estimating and prioritization. A portfolio that never checks whether its
completed work produced value is optimizing throughput of output, not outcomes.

## Quality checklist

- [ ] Every register row has an owner, a strategic link, a next milestone, and a confidence level.
- [ ] Data was gated for completeness, currency, consistency and credibility *before* analysis; gaps are named
      with owners rather than silently filled.
- [ ] RAG values carry a reason and an action; no bare colours anywhere.
- [ ] Capacity analysis names the *constrained role or team*, not just an aggregate shortfall.
- [ ] Collisions and dependency clusters are surfaced explicitly — the findings project-level views can't see.
- [ ] Scenarios present options with consequences; the decision is left to the accountable person.
- [ ] Every measure appears in the catalog with one definition; no two surfaces disagree.
- [ ] Reports lead with exceptions and decisions needed, not a complete inventory.
- [ ] Automation specs state trigger, validation, idempotency, error escalation, and manual fallback.
- [ ] Nothing is presented as measured when it was estimated, or as current when it is stale.

## Related methods
- [[project-management]] · [[agile-scrum-mechanics]] · [[roadmapping]] · [[metrics-and-experimentation]] ·
  [[prioritization-frameworks]]
