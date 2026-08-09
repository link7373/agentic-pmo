# Governance

> **How work gets approved, escalated, and controlled.** Owned by `governance-lead`. Seeded by `/setup-pmo`
> from section 9 of `START-HERE.md`; used by `/run-gate-review`, `/manage-change`, `/close-project`, and by
> every agent that needs to know when to escalate.
>
> Governance that nobody can find is governance that doesn't exist. This file is deliberately short: the gates,
> who decides, when to escalate, and how much risk the org accepts. Techniques live in
> `knowledge/methods/governance-and-change.md`.

_Last reviewed: —   ·   Tailoring level: —_

## Stage gates
_The decision points a project passes through. Small orgs run two or three; heavily regulated ones run more.
A gate with no named decider is decoration — fill the column or delete the row._

| Gate | Question it answers | Entry criteria | Decider | Evidence required | Applies to |
|------|---------------------|----------------|---------|-------------------|------------|
| G0 — Idea |Is this worth investigating? | | | Intake entry | |
| G1 — Business case | Should we fund it? | | | `templates/business-case.md` | |
| G2 — Plan approved | Is the plan credible? | | | Project plan, baseline in `knowledge/financials.md` | |
| G3 — Ready to launch | Is it safe to ship? | | | Launch plan, readiness checklist | |
| G4 — Closure | Did it deliver, and what did we learn? | | | `templates/closure-report.md` | |

Gate outcomes are one of **go / go-with-conditions / hold / kill**. Conditions carry an owner and a date.
Records go to `knowledge/programs/YYYY-MM-DD-<project>-gate-<n>.md`.

## Decision rights
_Who can approve what, without asking anyone else._

| Decision | Threshold | Approver | Consulted | Escalates to |
|----------|-----------|----------|-----------|--------------|
| Spend commitment | | | | |
| Scope change | | | | |
| Schedule re-baseline | | | | |
| New project start | | | | |
| Project kill | | | | |

## Risk scoring & appetite
_The scales referenced by `knowledge/raid-log.md`. Score = Probability × Impact, both 1–5, so 1–25._

**Probability:** 1 rare · 2 unlikely · 3 possible · 4 likely · 5 near-certain
**Impact:** 1 negligible · 2 minor · 3 moderate · 4 major · 5 severe — define what each means in *this* org
(money, schedule days, customers affected, regulatory exposure) rather than leaving it to taste:

| Impact level | Cost | Schedule | Customer / reputational | Regulatory |
|--------------|------|----------|-------------------------|------------|
| 5 severe | | | | |
| 4 major | | | | |
| 3 moderate | | | | |

**Appetite** — the plain-English statement of what the org will and won't accept, per category:

| Category | Appetite (averse / cautious / open / seeking) | What that means concretely |
|----------|----------------------------------------------|----------------------------|
| Delivery schedule | | |
| Cost | | |
| Compliance / regulatory | | |
| Technical / architectural | | |

## Escalation matrix
_Severity is the RAID score for risks and issues. "Respond by" is the time to a first substantive response,
not to resolution._

| Trigger | Raise to | Respond by | Channel |
|---------|----------|------------|---------|
| Score 20–25, or any regulatory exposure | | | |
| Score 12–16 | | | |
| Score 6–10 | | | |
| Cross-project dependency slipping | `program-manager` | | |
| Data-quality gap blocking a portfolio rollup | Named submitter, then their manager | | |

## Steering committee
| Field | Value |
|-------|-------|
| Members | |
| Cadence | |
| Standing agenda | Decisions needed · exceptions · portfolio health · financials · gate outcomes |
| Pack produced by | `/make-deliverable` from `templates/steerco-pack.md` |
| Pack circulated | _(how long before the meeting)_ |

## Methodology tailoring
_What this PMO deliberately does and does not do, and why. The honest record that stops a heavyweight process
being applied to a two-week project._

| Practice | Applied to | Deliberately skipped for | Rationale |
|----------|------------|--------------------------|-----------|
|          |            |                          |           |

## Compliance & audit obligations
_Anything externally imposed. If none apply, say so explicitly — "none identified" is a useful record._

| Obligation | Source | What it requires of the PMO | Evidence held where | Owner |
|------------|--------|-----------------------------|---------------------|-------|
|            |        |                             |                     |       |

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
