# Templates

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

Fill-in starting points for the PMO's deliverables. Skills copy the relevant template, then populate it and
save the result to the right `knowledge/` location. Keep these generic; project-specific content lives in
`knowledge/`, never here.

| Template | Used by | Output goes to |
|----------|---------|----------------|
| `prd.md` | `/write-prd` | `knowledge/prds/` |
| `requirements-package.md` | `/elicit-requirements` | `knowledge/prds/` (as `<date>-<feature>-analysis.md`) |
| `status-report.md` | `/track-status`, `/make-deliverable` | `knowledge/status/` |
| `sprint-plan.md` | `/plan-sprint` | `knowledge/sprints/` |
| `retro.md` | `/run-ceremony` (retrospective) | `knowledge/ceremonies/` |
| `project-plan.md` | `/plan-project` | `knowledge/projects/` |
| `capacity-plan.md` | `/plan-capacity` | `knowledge/capacity/` |
| `launch-plan.md` | `/plan-launch` | `knowledge/launches/` |
| `persona.md` | `/run-discovery` | `knowledge/discovery/` |
| `roadmap.md` | `/build-roadmap` | `knowledge/roadmap.md` |
| `okr.md` | `/define-strategy`, `/review-okrs` | `knowledge/product-context.md` |
| `business-case.md` | `/build-business-case` | `knowledge/financials/` |
| `change-request.md` | `/manage-change` | `knowledge/change-log.md` |
| `gate-review.md` | `/run-gate-review` | `knowledge/programs/` |
| `closure-report.md` | `/close-project` | `knowledge/projects/` |
| `exec-update.md` | `/make-deliverable` | `knowledge/deliverables/` |
| `steerco-pack.md` | `/make-deliverable` (steering committee) | `knowledge/deliverables/` |
| `portfolio-report.md` | `/track-portfolio` | `knowledge/portfolio/` |
| `dashboard-spec.md` | `/design-dashboard` | `knowledge/portfolio/` |
| `automation-spec.md` | `/plan-portfolio-automation` | `knowledge/portfolio/` |

## Skills that deliberately have no template

Not every skill needs one. These write structured content directly into an existing `knowledge/` file, whose
own scaffold already defines the shape — a separate template would be a second place for the format to drift:

- `/prioritize` — writes scored rows into `knowledge/roadmap.md` or `knowledge/backlog.md`.
- `/capture-feedback` — writes into the triage register in `knowledge/intake.md`.
- `/define-metrics` — writes into the definition template already inside `knowledge/metrics.md`.
- `/manage-resources` — writes into `knowledge/resources.md`.
- `/review-portfolio-intake` — its gap-report format is specified in the skill itself.
- `/coordinate-program`, `/track-financials` — produce dated artifacts whose structure is set by the skill.

All artifacts follow `standards/document-standards.md` (header, lead with the decision, state assumptions).
