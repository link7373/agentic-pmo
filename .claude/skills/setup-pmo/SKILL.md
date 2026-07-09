---
name: setup-pmo
description: Initialize the Agentic PMO from the START-HERE.md charter. Reads the user's answers, validates them, confirms process conventions, optionally tests tool integrations, and seeds the knowledge/ memory files. Run this first, and re-run after editing START-HERE.md.
---

# /setup-pmo — Stand up the PMO

The bootstrap workflow. Turns the filled-in `START-HERE.md` charter into a working, seeded PMO.

## When to use
- First time setting up the PMO, or after the user edits `START-HERE.md`.

## Steps
1. **Read the charter.** Parse all 8 sections of `START-HERE.md`. Note blanks and "no idea" answers.
2. **Clarify gaps.** Ask only about gaps that block setup (e.g., target customer, methodology, top goal).
   For everything else, apply sensible defaults and record them as assumptions.
3. **Confirm process conventions.** Reconcile the charter's process/cadence answers with
   `standards/agile-standards.md` defaults (sprint length, ceremonies, estimation scale). Confirm or adjust.
4. **Seed the knowledge base.** Populate from the charter:
   - `knowledge/product-context.md` — product, stage, vision, users, market, goals/OKRs, north star.
   - `knowledge/stakeholder-map.md` — stakeholders, decision-makers, RACI skeleton.
   - `knowledge/cadence.md` — methodology, sprint length, ceremonies, calendar, teams.
   - `knowledge/glossary.md` — seed from the charter's terminology/acronyms (section 8).
   - `knowledge/operating-rhythm.md` — confirm/adjust the cadence to match the team's process answers.
   - `knowledge/roadmap.md`, `knowledge/backlog.md`, `knowledge/raid-log.md`, `knowledge/intake.md` —
     initialize empty with headers.
   - `knowledge/integrations.md` — record any tools named and whether sync is desired (default: file-only).
   - `knowledge/decision-log.md` — log the setup decisions and assumptions made.
   - **Create the artifact output directories** (each already holds a README): `knowledge/prds/`,
     `knowledge/sprints/`, `knowledge/projects/`, `knowledge/launches/`, `knowledge/ceremonies/`.
5. **(Optional) Test integrations.** If the user wants tool sync and a connector is available, verify access.
   If not configured, confirm the PMO runs file-only (the default) and move on.
6. **Report readiness.** Summarize what was seeded, which assumptions you made, and the next actions the user
   can take (e.g., `/define-strategy`, `/run-discovery`, `/build-roadmap`). Point to
   `knowledge/operating-rhythm.md` so they know the ongoing cadence, and to `examples/` for the quality bar.

## Methods & standards
- Apply `knowledge/methods/product-strategy.md` to structure goals/OKRs in product-context.
- Follow `standards/document-standards.md` for all seeded files.

## Output
Seeded `knowledge/*` files and a readiness summary.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
