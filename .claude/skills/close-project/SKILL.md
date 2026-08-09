---
name: close-project
description: Close a project properly — accept or descope every deliverable, record final cost and schedule variance, hand benefits to named owners, resolve or transfer open RAID entries, release resources, and capture lessons. Use at completion or cancellation. Dispatches the project-manager.
---

# /close-project — Finish, don't fade

## When to use
When a project completes, is cancelled, or is superseded. **Cancellations need this most** — they carry the
most valuable lessons and are the most likely to be skipped because nobody wants to write the report.

## Dispatches
`project-manager` (lead) + `financial-analyst` (final actuals and benefits handoff) + `governance-lead`
(closure quality gate and lessons curation) + `scrum-master` (harvest retro actions and team lessons) +
`resource-manager` (release allocations).

## Inputs
The project plan in `knowledge/projects/`, `knowledge/status/` history, `knowledge/raid-log.md`,
`knowledge/change-log.md`, `knowledge/financials.md`, `knowledge/ceremonies/` (retro notes),
`knowledge/resources.md`, `knowledge/portfolio.md`.

## Steps
1. **Compare delivered against baselined scope**, accounting for approved changes in
   `knowledge/change-log.md`. Anything not delivered is formally descoped with a destination — backlog,
   another project, or dropped — not left ambiguous.
2. **Record final schedule and cost variance.** Baseline vs. actual with the reason. Where no cost baseline
   existed, say so — do not reconstruct one at closure to produce a tidy variance.
3. **Hand over the benefits.** Every benefit from the business case goes to a named owner *outside the project
   team*, with a first review date, recorded in the benefits register in `knowledge/financials.md`. The team
   disbands; benefits take quarters. This is the step whose absence makes claimed value disappear.
4. **Clear the RAID log.** Every open entry is resolved, transferred to a named owner, or explicitly accepted.
   Nothing is closed by being ignored.
5. **Release the resources.** Update allocations in `knowledge/resources.md`, and close out vendor and
   contract obligations — including any knowledge transfer that was supposed to happen before a contract ended.
6. **Capture lessons that would change behavior.** "Communication could be better" is a feeling; a specific
   recommendation someone could act on is a lesson. Append each to `knowledge/lessons-learned.md`, and check
   whether it is the third occurrence of a pattern — if so, change the standard, template, or skill rather than
   filing another row.
7. **Close the record.** Set the register row in `knowledge/portfolio.md` to Closed and log the closure
   decision, including the reason for a cancellation.

## Methods
`knowledge/methods/governance-and-change.md` (closure, lessons that get read, cancellations),
`knowledge/methods/financial-management.md` (benefits handoff),
`knowledge/methods/project-management.md` (closing a project).

## Output
Start from `templates/closure-report.md`. Save to `knowledge/projects/<name>-closure.md`; update
`knowledge/financials.md` (final actuals, benefits owners), `knowledge/resources.md` (released allocations),
`knowledge/raid-log.md` (closed/transferred), `knowledge/lessons-learned.md` (appended), and
`knowledge/portfolio.md` (status Closed). Log the closure in `knowledge/decision-log.md`. Follow
`standards/document-standards.md`.

## Optional sync
If `knowledge/integrations.md` configures Jira/Linear/Notion, offer to close or archive the project's board
and post the closure summary. Files remain source of truth; skip if not configured.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
