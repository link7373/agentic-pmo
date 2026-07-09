# PRD: Auto-detected blocker flags (example — "Cadence")

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373
Status: In review   ·   Owner: product-manager   ·   Date: 2026-06-19
Links: product-context (Cadence) · roadmap "Now" item · discovery: blocker-trust interviews

## 1. Problem & context
Managers tell us the painful part of standups isn't knowing *what people did* — it's catching *what's stuck*
before it slips. Cadence already digests updates; it doesn't yet surface blockers. Serves the Q3 objective
"prove teams adopt the digest" and KR3 (blocker-flag action rate ≥ 40%).

## 2. Goals & success metrics
- **Goal:** managers catch and act on blockers earlier, from the digest alone.
- **Success metric:** blocker-flag action rate ≥ 40% within 4 weeks of release.
- **Guardrail:** false-positive blocker rate < 20% (or managers will stop trusting flags).

## 3. Target users / personas
Primary: the engineering manager (persona "Maya") who skims the digest each morning and wants a short,
trustworthy "needs attention" list. Job: *When I start my day, I want to know what's blocked, so I can
unblock it before it slips.*

## 4. Scope
**In scope:** detect likely blockers from update text; show a ranked "needs attention" section in the digest
with a confidence (blocker score); let managers confirm/dismiss a flag (feedback signal).
**Out of scope (for now):** auto-pinging the blocked person; cross-team blocker routing; Slack-side actions.

## 5. Requirements / user stories
| ID | Story | Acceptance criteria | Priority |
|----|-------|---------------------|----------|
| B1 | As a manager, I want blocked items surfaced in the digest, so I act early | Given a daily digest, when an update implies a blocker, then it appears in "Needs attention" with a blocker score | Must |
| B2 | As a manager, I want to confirm or dismiss a flag, so the system learns | Given a flag, when I confirm/dismiss, then it's recorded and the flag updates | Must |
| B3 | As a manager, I want flags ranked by confidence, so I scan the top first | Given multiple flags, when the digest renders, then they're ordered by blocker score | Should |

## 6. UX
"Needs attention" section at the top of the digest; each flag shows the item, the signal, a confidence
badge, and confirm/dismiss. Empty state when nothing's blocked.

## 7. Dependencies, risks, assumptions, open questions
- **Dependency:** digest pipeline (already shipped).
- **Risk:** false positives erode trust → guardrail metric + easy dismiss.
- **Assumption:** update text contains enough signal to detect blockers (validate in beta).
- **Open question:** show confidence as a number or a label?

## 8. Rollout & measurement plan
Feature-flagged to 5 friendly teams first; instrument flag impressions, confirm/dismiss, and action rate.
Expand when action rate ≥ 40% and false-positive rate < 20% hold for one week; otherwise iterate on detection.
