# Examples

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

A worked sample so you can see the quality bar before running your own. **Nothing here is wired into the
live PMO** — the real PMO reads from `knowledge/`, not `examples/`. Use these to calibrate what good output
looks like, then delete or ignore.

## `sample-product/` — "Cadence" (a fictional B2B standup-notes assistant)
- `START-HERE-filled.md` — the charter, filled in, as a model answer.
- `product-context.md` — what `/setup-pmo` + `/define-strategy` would seed from that charter.
- `sample-prd.md` — a `/write-prd` output for one feature, using `templates/prd.md`.
- `sample-roadmap.md` — a `/build-roadmap` output in Now/Next/Later form.

## `sample-dashboard/` — a working Power BI portfolio dashboard
A real, openable PBIP project, for checking the Power BI capability renders end to end on your machine.
- `SPEC.md` — what `/design-dashboard` produces, using `templates/dashboard-spec.md`.
- `build_sample.py` — the generator; re-run it to rebuild the project from scratch.
- `Portfolio_Sample/` — the built project: TMDL semantic model, PBIR pages and visuals, theme.

**Start with [`sample-dashboard/README.md`](sample-dashboard/README.md)** — three Power BI preview features must
be enabled first or the project won't open, and it lists the exact card values to expect so you can tell
"rendered correctly" from "rendered blank".
