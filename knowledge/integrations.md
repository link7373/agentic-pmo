# Integrations (optional)

> **Files in `knowledge/` are the source of truth.** Tool sync is optional and layered on top. If nothing is
> configured here, the PMO runs fully file-only and all skills skip their sync steps silently.

## Configured tools
| Tool | Purpose | Sync direction | Status |
|------|---------|----------------|--------|
| _Jira / Linear_ | backlog & sprints | push / pull / two-way | not configured |
| _Notion_ | docs & roadmap | push / pull | not configured |
| _Slack / Teams_ | status & announcements | push | not configured |
| _Power BI_ | portfolio dashboards | spec handoff → build | available via the BI capability (below) |
| _Tableau / other BI_ | portfolio dashboards | spec handoff → build | not configured |
| _Power Automate_ | status intake & data flow | push / pull | **no capability — spec only** |
| _OnePlan / PPM platform_ | resource & capacity data | pull | **no capability — spec only** |

## How sync works
- Skills that manage trackable items (`/groom-backlog`, `/plan-sprint`, `/track-status`, `/track-portfolio`,
  `/make-deliverable`) update the canonical `knowledge/` file **first**, then offer to sync to a configured tool.
- Sync uses the available MCP connector for that tool. If the connector isn't connected/authenticated, the
  skill reports it and continues file-only — never blocks.

## Dashboards — the BI build capability
Power BI dashboards are buildable **as code**: the project is plain text — the semantic model, the report
pages and visuals, and the theme — so a dashboard is an ordinary reviewable artifact rather than something
only clickable in a GUI. That capability lives in a companion kit, `agentic-bi-team`
(https://github.com/link7373/agentic-bi-team), not in this one.

**The division of labour:**

| This kit (`/design-dashboard`) | The BI capability |
|---|---|
| Questions, decisions, audience tiers | Project authoring and platform mechanics |
| Grain, star schema, relationships | Model implementation |
| Measure catalog — names and definitions | Measure implementation, named exactly as specified |
| Page layout, safe names, drill paths | Chart formatting against its own design standard, theme |
| Refresh, lineage, access, privacy constraints | Validation, reconciliation, publishing |

**Capability tiers.** What a handoff delivers depends on what's installed at the far end — from spec-only, up
through full project authoring, to a workspace-connected deployment. Confirm the tier before promising a date;
`/design-dashboard` records it in the spec's `## Handoff` section. Spec-only is a legitimate stop: a complete,
correct specification is real work product.

**Rules that hold regardless of tier:**
- Measure names are a contract. A name that drifts between spec and build is a defect, not a variation. New
  portfolio measures are defined in the spec's catalog first, never invented during the build.
- A surface isn't done when it renders. Every displayed number reconciles against an independent query, and
  the empty state is tested, before anyone sees it.
- Publishing to a wider or external audience is a decision that needs confirming, not a step in the build.

## Automation — no capability today
Power Automate, SharePoint, OnePlan and Jira-side flow automation have **no build capability available**, in
this kit or the companion one. `/plan-portfolio-automation` therefore produces a **specification only** — a
buildable design a person or another tool implements. Say so plainly when handing one over; do not imply a
flow will appear. If that changes, update the rows above and the specs stay valid as written.

## Mapping notes
_Record any field/status mappings between `knowledge/` files and the external tool (e.g., backlog status →
Jira workflow states) so sync stays consistent._

## Setup
Configured during or after `/setup-pmo`. To enable a tool: connect its MCP connector, then record it above
with the desired sync direction.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
