# Integrations (optional)

> **Files in `knowledge/` are the source of truth.** Tool sync is optional and layered on top. If nothing is
> configured here, the PMO runs fully file-only and all skills skip their sync steps silently.

## Configured tools
| Tool | Purpose | Sync direction | Status |
|------|---------|----------------|--------|
| _Jira / Linear_ | backlog & sprints | push / pull / two-way | not configured |
| _Notion_ | docs & roadmap | push / pull | not configured |
| _Slack / Teams_ | status & announcements | push | not configured |

## How sync works
- Skills that manage trackable items (`/groom-backlog`, `/plan-sprint`, `/track-status`, `/make-deliverable`)
  update the canonical `knowledge/` file **first**, then offer to sync to a configured tool.
- Sync uses the available MCP connector for that tool. If the connector isn't connected/authenticated, the
  skill reports it and continues file-only — never blocks.

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
