# Automation Spec: <flow name>
Owner: portfolio-analyst   ·   Date: YYYY-MM-DD   ·   Status: <draft | approved | live>
Target platform: <Power Automate | scripted | other | undecided>

> This is a **specification, not a built flow**. It defines the behaviour precisely enough to implement and to
> test. See `## Handoff` for the current build route.

## Problem this removes
- **Current manual step:** <what a person does today>
- **Cost:** <time per cycle · error rate · what it delays>
- **Why automate this one:** <collection and validation automate well; judgment does not>

## Flow overview
`Trigger → collect → validate → transform → store → publish → notify`

| Stage | What happens | Source / destination |
|-------|--------------|---------------------|
| Trigger |  |  |
| Collect |  |  |
| Validate |  |  |
| Transform |  |  |
| Store |  |  |
| Publish |  |  |
| Notify |  |  |

## Trigger
- **Type:** <schedule | event | manual>
- **Detail:** <cron/cadence, or the event and its source>
- **Window:** <what period of data each run covers>

## Inputs
| Input | Source | Required? | Format | Notes |
|-------|--------|-----------|--------|-------|
|       |        |           |        |       |

## Validation rules
_Validate at the boundary. Bad input rejected here never reaches a report; validation after storage means the
bad data is already believed._

| Field | Rule | On failure |
|-------|------|-----------|
|       |      | <reject with message naming the field and the fix · quarantine · flag low-confidence> |

**Rejection message style:** name the field, say what's wrong, say what to do. Never a generic error.

## Transform
- **Logic:** <mapping, derivation, aggregation>
- **Measure definitions used:** <reference the dashboard spec's measure catalog — do not redefine here>

## Destination
- **Writes to:** <file / table / surface>  ·  **Mode:** <append | upsert | replace>
- **Canonical source of truth remains:** `knowledge/` — this flow must not become the only record.

## Idempotency
_Assume every run happens twice._
- **Dedupe key:** <what makes a record unique>
- **Re-run behaviour:** <what a repeat run does — must not double-count or duplicate>
- **Backfill:** <how to re-process a past period safely>

## Error handling & escalation
| Failure | Detection | Response | Escalates to | Within |
|---------|-----------|----------|--------------|--------|
| Transient (timeout, throttle) | | retry <n> with backoff | | |
| Persistent (auth, schema change) | | halt, alert | named human | |
| Partial (some records rejected) | | process the rest, report the rejects | submitting owner | |

**A flow that fails silently is worse than no flow** — the report still renders, just wrongly. Every run logs:
what ran, when, record counts, and what failed. That log is the source for the data-health measure.

## Human in the loop
- **Automated:** <chasing, validating, moving data>
- **Never automated:** <interpreting a RAG, deciding to escalate, judging credibility>
- **Approval gates:** <any point where a person must confirm before the flow continues>

## Manual fallback
_The cycle must be completable by hand when the automation is down._
- **Fallback procedure:** <steps>
- **How anyone knows to use it:** <the alert that triggers falling back>

## Rollout
- **Pilot scope:** <a subset first>  ·  **Success criteria:** <what makes it safe to widen>
- **Rollback:** <how to disable and revert cleanly>

## Handoff
> **There is no automation build capability available today** — not in this kit and not in the companion BI
> kit, which covers dashboards only. This spec is implemented by a person or another tool. Say so when handing
> it over; do not imply a flow will appear.

- **Build route:** <named person | platform team | undecided>
- **Ready to hand over:** trigger, inputs, validation rules, transform logic, destination, idempotency rules,
  the error matrix, human-in-the-loop points, and the manual fallback.
- **The builder owns:** platform mechanics, connection and credential setup, and testing the failure paths —
  particularly that a failed run is *visible*, since a silent failure still renders a report, just a wrong one.
- **Not done until:** a deliberately bad input has been rejected with a useful message, a duplicate run has
  been shown not to double-count, and the manual fallback has been walked through once.
- **Open questions blocking the build:**
  - <question — owner — needed by>

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
