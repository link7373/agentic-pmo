# Integrations (optional)

> **Files in `knowledge/` are the source of truth.** Tool sync is optional and layered on top. If nothing is
> configured here, the PMO runs fully file-only and all skills skip their sync steps silently.

## Configured tools
| Tool | Purpose | Sync direction | Status |
|------|---------|----------------|--------|
| _Jira / Linear_ | backlog & sprints | push / pull / two-way | not configured |
| _Notion_ | docs & roadmap | push / pull | not configured |
| _Slack / Teams_ | status & announcements | push | not configured |
| _Power BI_ | portfolio dashboards | built in-kit via `/powerbi` | **available — the default platform** |
| _Tableau / other BI_ | portfolio dashboards | spec only | not configured |
| _Power Automate_ | status intake & data flow | push / pull | **no capability — spec only** |
| _OnePlan / PPM platform_ | resource & capacity data | pull | **no capability — spec only** |

## How sync works
- Skills that manage trackable items (`/groom-backlog`, `/plan-sprint`, `/track-status`, `/track-portfolio`,
  `/make-deliverable`) update the canonical `knowledge/` file **first**, then offer to sync to a configured tool.
- Sync uses the available MCP connector for that tool. If the connector isn't connected/authenticated, the
  skill reports it and continues file-only — never blocks.

## Dashboards — built in-kit
Power BI is the default reporting platform and the PMO **builds** its dashboards rather than only specifying
them. A PBIP project is plain text — semantic model in TMDL, pages and visuals in PBIR, theme JSON — so a
dashboard is an ordinary reviewable artifact rather than something only clickable in a GUI.

**The path:** `/design-dashboard` (spec → `knowledge/portfolio/`) → `/powerbi` (build → `dashboards/`) →
`powerbi-validator` (independent gate). Standards: `standards/dashboard-standards.md` for design — the single
authority — and `standards/powerbi-standards.md` for Power BI mechanics.

**Capability tiers.** What a build delivers depends on what's installed locally: spec-only needs nothing; full
project authoring needs Power BI Desktop plus Python and is the default; CLI-accelerated and
workspace-connected tiers need extra tooling the user chooses to install. `/powerbi` detects and states the tier
before it starts. Spec-only is a legitimate stop, not a failure. Detection commands are in
`.claude/skills/powerbi/references/tooling-tiers.md`.

**Rules that hold regardless of tier:**
- Measure names are a contract. A name that drifts between `knowledge/portfolio-measures.md` and a built surface
  is a defect, not a variation. New measures go in the catalog first, never invented during a build.
- A project that validates is only well-formed. It isn't done until it renders in Desktop, every number
  reconciles against the register or cycle artifact it came from, and the empty state is tested.
- Publishing to a wider or external audience is a decision that needs confirming, not a step in the build.
- A portfolio surface names real people. Saved filter state persists into tracked files — keep the default
  impersonal.

**Another platform?** If the portfolio reports through Tableau or anything else, `/powerbi` does not apply and
none of its mechanics transfer. `/design-dashboard` still produces a complete spec; a person builds from it.

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
