# Tooling Tiers — what the team can actually do

> Read at `/powerbi` step 2. Detect the tier, state it, then work within it.

Power BI capability is not binary. Each tier below unlocks more, and **any one of
them is enough to be useful** — the same philosophy as the optional tool sync in
`knowledge/integrations.md`. Tier 1 needs nothing beyond Power BI Desktop and Python.

## Detect

```bash
python --version                      # Tier 1 needs 3.9+
pbir --version                        # Tier 2 (absent = not installed)
fab --version                         # Tier 3 (Fabric CLI)
```

On Windows, Power BI Desktop is normally at
`C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe` or installed from
the Microsoft Store.

## The tiers

| Tier | Needs | Unlocks |
|---|---|---|
| **0 — Spec only** | nothing | `SPEC.md`, layout sketch, measure list, DAX drafts, theme JSON. Everything except the project itself. |
| **1 — PBIP authoring** *(default)* | Power BI Desktop + Python | Author and edit the whole project: TMDL model, PBIR pages/visuals, theme, bookmarks. Validate with `scripts/validate_pbip.py`. User opens in Desktop. |
| **2 — CLI-accelerated** | user installs `pbir-cli` | Bulk formatting across globbed visuals, structural introspection, backup/restore, publish. |
| **3 — Fabric-connected** | user installs Fabric CLI, or a Fabric MCP server | Deploy to workspaces, read remote items, trigger refresh, inspect tenant state. |

**Tier 1 is not a fallback.** It is the honest default and it is genuinely
sufficient to build a complete, correct dashboard. Do not stall waiting for
Tier 2.

## Enabling the formats

PBIP and its text formats are Microsoft **preview** features and are off by
default. In Power BI Desktop, under
**File → Options and settings → Options → Preview features**, the user must enable:

- **Power BI Project (.pbip) save option** — without it, there is no project to edit.
- **Store semantic model using TMDL format** — otherwise the model saves as a single
  `model.bim` JSON blob, which is far harder to diff and edit.
- **Store reports using enhanced metadata format (PBIR)** — otherwise the report saves
  as `report.json`, which Microsoft does not document and does not support editing.

If the user has a PBIP already saved in the legacy formats, saving again after
enabling these prompts an upgrade. **The upgrade is one-way** — tell them to keep a
copy first.

## Tier 2 — `pbir-cli`, and its licence

[`pbir.tools`](https://github.com/maxanatsko/pbir.tools) by Maxim Anatsko and Kurt
Buhler is a CLI that makes PBIR reports path-addressable
(`Report.Report/Page.Page/Visual.Visual`, with globs). Its real value to this team is
that it turns `standards/dashboard-standards.md` from advice into a command — one
glob applies a formatting rule to every visual in a report.

**Before recommending it, tell the user this:** pbir.tools is released under a
**custom non-commercial licence** that also forbids derivative works. It is free for
personal and educational use; **commercial use requires written permission from the
authors.** If this team operates in a commercial setting, that is the user's call to
make with full information, not ours to make silently. Tier 1 remains fully
available either way.

This repository does not bundle, vendor, wrap, or depend on it. If it is installed,
we call it. If it is not, we do the same work in Python.

```bash
# only if the user decides to install it
uv tool install pbir-cli   # or: pip install pbir-cli
```

Useful once present: `pbir ls`, `pbir tree <report> -v`, `pbir model <report> -d`,
`pbir validate <report>`, `pbir backup <report> -m "<why>"`, `pbir set <glob> --value <v> -f`.

Its own safety conventions are worth adopting regardless of tier: **back up before
mutating, validate after, and require an explicit force flag for anything that
touches many objects at once.**

## Tier 3 — Fabric CLI

Microsoft's `fab` CLI covers workspaces, deployment pipelines, and refreshes. Treat
every write as outward-facing: publishing a portfolio dashboard to a workspace needs
the user's confirmation first, every time. See `publishing.md`.

## Credit

The architecture of this Power BI module — splitting knowledge by artifact type,
keeping the skill thin with reference files loaded on demand, pairing a builder with
a separate validator, and treating deterministic checks as more trustworthy than
model confidence — was learned from
[**power-bi-agentic-development**](https://github.com/data-goblin/power-bi-agentic-development)
by Kurt Buhler (Data Goblins), and the report-as-addressable-object workflow from
[**pbir.tools**](https://github.com/maxanatsko/pbir.tools). Both are worth reading
directly.

**No code or text was copied from either project.** This module is original work
written against Microsoft's published PBIP/PBIR/TMDL documentation and JSON schemas,
because this repository is MIT-licensed while power-bi-agentic-development is
GPL-3.0 and pbir.tools forbids derivative works. If you want their skills
themselves, install them from their own marketplace — they are excellent, and more
specialised than this module aims to be.
