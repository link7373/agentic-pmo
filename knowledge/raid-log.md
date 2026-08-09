# RAID Log

> Risks, Assumptions, Issues, Dependencies. Updated by `/plan-project`, `/track-status`, `/run-ceremony`,
> `/coordinate-program`, `/manage-change`, `/close-project`. Reviewed on a regular cadence.

## Ownership & precedence

Four roles touch this file. Without a precedence rule they overwrite each other, so:

- **`project-manager` owns every entry at `Level = project`** — its Response, Resolution path, and closure.
- **`program-manager` owns every entry at `Level = program`** (cross-project, integration, shared-dependency).
- **`delivery-monitor` may add new entries and update `Score` and `Status` during `/track-status`**, but never
  overwrites an owner's Response or Resolution. Where it disagrees, it adds a dated note and flags the owner.
- **`portfolio-analyst` never writes here.** `/review-portfolio-intake` returns gaps and doubts to the named
  manager, who records them. Portfolio-level risks live in `knowledge/portfolio.md`.
- **`governance-lead`** sets the scoring scale and escalation thresholds in `knowledge/governance.md`; it does
  not re-score individual entries.

Every entry carries a `Level` and, for risks and issues, a `Score`. Escalation between levels follows the
matrix in `knowledge/governance.md` — a project risk crossing the threshold is raised to program level by the
project-manager, not silently re-owned.

**Scoring:** `Score = Probability × Impact` on the 1–5 scales defined in `knowledge/governance.md`
(1 = very low … 5 = very high), so scores run 1–25. Thresholds for escalation live there too, not here.

_Last reviewed: —_

## Risks (uncertain future events)
| ID | Level | Risk | Prob (1-5) | Impact (1-5) | Score | Response (avoid/mitigate/transfer/accept) | Owner | Trigger | Status |
|----|-------|------|------------|--------------|-------|-------------------------------------------|-------|---------|--------|
|    |       |      |            |              |       |                                           |       |         |        |

## Assumptions (taken as true for planning)
| ID | Level | Assumption | Why it matters | Revisit when | Status |
|----|-------|------------|----------------|--------------|--------|
|    |       |            |                |              |        |

## Issues (happening now)
| ID | Level | Issue | Severity (1-5) | Owner | Resolution path | Escalated to | Status |
|----|-------|-------|----------------|-------|-----------------|--------------|--------|
|    |       |       |                |       |                 |              |        |

## Dependencies
| ID | Level | Dependency | Direction (need from / provide to) | Owner | Needed by | Status |
|----|-------|------------|------------------------------------|-------|-----------|--------|
|    |       |            |                                    |       |           |        |

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
