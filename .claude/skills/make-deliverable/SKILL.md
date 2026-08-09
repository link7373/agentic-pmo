---
name: make-deliverable
description: Produce a stakeholder-ready deliverable — executive summary, status update, steering-committee/board deck, or announcement — tailored to a specific audience. Use to package PMO substance for communication. Dispatches the comms-lead. Supports optional tool sync.
---

# /make-deliverable — Package it for the audience

## When to use
Turning PMO substance (status, roadmap, plan, decision) into a polished, audience-specific communication.

## Dispatches
`comms-lead` (lead). Pull substance from the relevant agent first (`delivery-monitor` for status,
`product-manager` for roadmap, etc.) — never fabricate content.

## Inputs
The source substance/artifact, `knowledge/stakeholder-map.md`, `knowledge/product-context.md`. For a steering
committee: `knowledge/portfolio/`, `knowledge/status/`, `knowledge/financials.md`, `knowledge/raid-log.md`,
`knowledge/change-log.md`, and recent gate records in `knowledge/programs/`.

## Steps
1. Identify the audience and the decision/action they need.
2. Lead with the bottom line (BLUF); match altitude (executives → outcomes/decisions; teams → detail).
3. Use RAG with reason + action; quantify where possible; flag uncertainty honestly.
4. Format to the requested medium (one-pager, deck outline, email, announcement); keep it scannable.
5. Put detail in appendices or link to the canonical `knowledge/` artifact.
6. Check every number traces to a `knowledge/` file. A deliverable is a rendering, not a source — if you need
   a fact that doesn't exist upstream, send it back to the agent that owns it rather than deriving it here.

## Methods
`standards/communication-standards.md` (primary), `knowledge/methods/roadmapping.md` (audience views).

## Output
Start from the matching template — `templates/exec-update.md`, `templates/status-report.md`, or
`templates/steerco-pack.md` for a steering committee. Save to `knowledge/deliverables/` as
`YYYY-MM-DD-<audience>-<topic>.md`; log only consequential communication decisions to
`knowledge/decision-log.md`. Circulated deliverables are never edited — supersede them with a new dated file so
the record of what was said, and when, stays intact. Follow `standards/communication-standards.md` and
`standards/document-standards.md`.

## Optional sync
If `knowledge/integrations.md` configures Slack/Notion, offer to post/share the deliverable there. Skip if
not configured.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
