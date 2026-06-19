# Roadmap (example — "Cadence")

> A `/build-roadmap` output in Now/Next/Later form. Every item ladders to the Q3 objective "prove teams
> adopt the daily digest."

_Last updated: 2026-06-19_

## Now (committed, in active development)
| Theme / initiative | Outcome it targets | Goal/OKR | Confidence | Notes |
|--------------------|--------------------|----------|------------|-------|
| Auto-detected blocker flags | Managers act on blockers from the digest | KR3 action rate ≥ 40% | High | See sample PRD |
| Digest reliability & open rate | Teams open the digest daily | KR2 open rate → 60% | High | Send-time tuning, content polish |

## Next (shaped, coming up)
| Theme / initiative | Outcome it targets | Goal/OKR | Confidence | Notes |
|--------------------|--------------------|----------|------------|-------|
| Linear backlog sync | Updates reflect real work without manual entry | KR1 active teams | Medium | Reduces setup friction |
| Blocker confidence tuning | Lower false positives, keep trust | Guardrail < 20% | Medium | Uses confirm/dismiss signal |

## Later (directional, exploratory)
| Theme / opportunity | Outcome it targets | Goal/OKR | Notes |
|---------------------|--------------------|----------|-------|
| Slack-side blocker actions | Unblock without leaving Slack | Adoption | Out of MVP scope |
| Cross-team blocker routing | Surface dependencies between teams | Future | Needs multi-team data |

## Assumptions & open questions
Assumes blocker detection is trustworthy enough to drive action (the core Now bet). If KR3 misses, re-examine
the bet before expanding scope.
