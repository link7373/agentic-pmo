# Standards: Documents & Artifacts

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

House style for every artifact the PMO produces. Skills and agents must follow these so outputs are
consistent, scannable, and decision-ready. Adjust the specifics during `/setup-pmo` to fit the org.

## Universal rules
- **Lead with the decision/outcome.** First lines say what this is, who it's for, and what action is needed.
- **Scannable structure.** Headings, short paragraphs, bullets, and tables over walls of text.
- **State assumptions and confidence.** Mark estimates, open questions, and what would change the conclusion.
- **Link, don't duplicate.** Reference the relevant `knowledge/` file as the source of truth instead of copying.
- **Date and own it.** Every artifact has a title, date, owner (agent), and status.
- **Plain language.** Define acronyms on first use; prefer concrete nouns and active voice.
- **Empty-scaffold protocol.** If a `knowledge/` file you need is empty or header-only, say so plainly, name
  the skill that populates it (e.g., "`knowledge/financials.md` has no cost baseline — run
  `/build-business-case` or `/track-financials`"), and proceed only on assumptions you mark as assumptions.
  Never fabricate content to fill a scaffold, and never present a derived figure as if the underlying data
  existed.

## Standard artifact header
```
# <Artifact type>: <Title>
Status: Draft | In review | Approved   ·   Owner: <agent>   ·   Date: YYYY-MM-DD
Links: <related knowledge/ files, upstream artifacts>
```

## Per-artifact conventions
- **PRD** — follow the anatomy in `knowledge/methods/requirements-and-stories.md`; always include
  out-of-scope and a success metric.
- **Roadmap** — default to Now/Next/Later; each item shows the goal/outcome it serves and a confidence/horizon.
- **User stories** — `As a <user>, I want <capability>, so that <outcome>` + acceptance criteria; satisfy INVEST.
- **Status report** — RAG with reason + action; lead with decisions/help needed; include top risks/issues.
- **Sprint plan** — one clear Sprint Goal, selected items, capacity, and commitments.
- **Project plan** — scope (in/out), milestones, dependencies, RAID summary, key dates.
- **Business case** — problem, options considered (including do-nothing), costs, quantified benefits with
  their owner and measurement method, ROI/payback, risks, and the recommendation. Every number is labelled
  estimate or measured.
- **Change request** — the change, why now, impact on scope/schedule/cost/risk stated separately, options,
  recommendation, and the approver. No CR is "approved" without a named approver and a date.
- **Gate review** — the gate's entry criteria, evidence against each, unresolved items, and one of
  go / go-with-conditions / hold / kill with named conditions and owner.
- **Closure report** — what was delivered vs. baselined scope, final schedule and cost variance, benefits
  handoff (who tracks what, from when), open items and where they went, and lessons learned.
- **Decision** — logged to `knowledge/decision-log.md` (see format below).

## Decision log entry format
```
## YYYY-MM-DD — <decision title>
- Context: <why this came up>
- Options considered: <brief>
- Decision: <what we chose>
- Rationale / evidence: <why; methods or data used>
- Owner: <agent/role>   ·   Revisit: <trigger or date, if any>
```

## File & naming conventions
- Persistent state lives in `knowledge/`; reusable techniques in `knowledge/methods/`.
- Generated deliverables go under `knowledge/` in the relevant file (roadmap, backlog, raid-log) or a dated
  artifact file (e.g., `knowledge/prds/2026-06-19-<feature>.md`) — keep one source of truth per concern.
- Use kebab-case filenames and ISO dates (YYYY-MM-DD).

## Quality bar before "done"
- [ ] Header present (type, status, owner, date, links).
- [ ] Leads with the decision/action; scannable.
- [ ] Assumptions, confidence, and open questions stated.
- [ ] Links to the right `knowledge/` file as the source of truth; no duplication.
