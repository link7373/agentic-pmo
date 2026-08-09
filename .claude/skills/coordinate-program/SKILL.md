---
name: coordinate-program
description: Coordinate related projects — map cross-team dependencies with owners and needed-by dates, sequence against value, capacity and the critical path, limit system-level WIP, and align integration and shared Definition of Done. Use when multiple projects must combine into one outcome. Dispatches the program-manager.
---

# /coordinate-program — Make the pieces fit

## When to use
When several projects or teams must deliver one outcome together; when a dependency is slipping across a team
boundary; when the portfolio needs re-sequencing after a capacity or funding change.

## Dispatches
`program-manager` (lead) + `portfolio-analyst` (collision, constraint and register data) + `resource-manager`
(supply) + `delivery-monitor` (current project health).

## Inputs
All relevant project plans in `knowledge/projects/`, `knowledge/portfolio.md` (collisions, constraints),
`knowledge/capacity/` and `knowledge/resources.md` (supply), `knowledge/raid-log.md`, `knowledge/roadmap.md`,
`knowledge/cadence.md`, `knowledge/governance.md` (what needs a sponsor's decision).

## Steps
1. **Map dependencies explicitly** across teams and projects — direction, owner on both sides, and a needed-by
   date. A dependency without a needed-by date is a hope. Record them in `knowledge/raid-log.md` at
   `Level = program`.
2. **Find the program critical path** — the longest dependent chain across projects, which is rarely the
   critical path of any single one. Protect it, and watch the near-critical chains that become critical the
   moment it slips.
3. **Sequence by value, dependency and capacity**, using the constraint from `knowledge/capacity/` rather than
   aggregate headcount. Show the trade-off you made and what you gave up — the reasoning is the artifact's
   whole value later.
4. **Limit system-level WIP.** Too many concurrent items is the most common cause of slow delivery and the
   least often diagnosed: everything progresses, nothing finishes. Track items in flight against a deliberate
   limit and prefer throughput over utilization as the health signal.
5. **Surface the collisions no project can see.** Two projects needing the same scarce team in the same window
   are each individually green. Escalate cross-team risks that no single project owns.
6. **Align integration and a shared Definition of Done** so increments actually combine into a releasable
   whole, and name the integration points and who owns each.
7. **Present options with consequences** where the call costs money or belongs to a sponsor per
   `knowledge/governance.md` — defer, descope, re-sequence, add capacity — rather than deciding for them.

## Methods
`knowledge/methods/project-management.md` (dependencies, critical path, program coordination, tailoring),
`knowledge/methods/portfolio-management.md` (collisions, WIP, the three altitudes),
`knowledge/methods/resource-management.md` (constraints and lead times),
`knowledge/methods/roadmapping.md` (sequencing and communicating direction).

## Output
A coordination artifact at `knowledge/programs/YYYY-MM-DD-<program>-coordination.md` — dependency map,
sequencing with its rationale, integration plan, WIP position, and the decisions needed. Cross-project entries
in `knowledge/raid-log.md` at `Level = program`. Log sequencing and trade-off decisions to
`knowledge/decision-log.md`. Follow `standards/document-standards.md`.

## Optional sync
If `knowledge/integrations.md` configures Jira/Linear, offer to reflect dependency links on the affected
items. Files remain source of truth; skip if not configured.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
