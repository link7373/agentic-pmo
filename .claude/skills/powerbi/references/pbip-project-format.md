# PBIP Project Format — the shape of the thing

> Source of truth: [Microsoft — Power BI Desktop projects](https://learn.microsoft.com/power-bi/developer/projects/projects-overview).
> Preview feature; verify against the docs when something looks off.

## Layout

```
dashboards/exec-revenue/
├── ExecRevenue.pbip                  # optional shortcut to the report folder
├── .gitignore                        # Desktop writes this itself
├── ExecRevenue.Report/
│   ├── .platform                     # Fabric Git identity — never hand-write
│   ├── definition.pbir               # REQUIRED — model reference + format version
│   ├── definition/                   # PBIR report definition (see pbir-visuals.md)
│   ├── StaticResources/
│   │   └── RegisteredResources/      # themes, images
│   └── .pbi/localSettings.json       # per-user — gitignored
└── ExecRevenue.SemanticModel/
    ├── .platform
    ├── definition.pbism              # REQUIRED — model format version
    ├── definition/                   # TMDL (see semantic-model-tmdl.md)
    └── .pbi/cache.abf                # local data cache — gitignored
```

The `.pbip` file is **optional** — it just points at a report folder. Desktop opens
`definition.pbir` directly just as well. One folder can hold several reports against
one model; Fabric Git integration only ever reads `definition.pbir` and ignores other
`*.pbir` files.

## `definition.pbir`

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/2.0.0/schema.json",
  "version": "4.0",
  "datasetReference": {
    "byPath": { "path": "../ExecRevenue.SemanticModel" }
  }
}
```

`version` must be **4.0 or higher** for the PBIR `definition/` folder to be used.
Version 1.0 forces the legacy `report.json`.

`datasetReference` carries exactly one of:

- **`byPath`** — relative path, forward slashes, no absolute paths. Desktop opens the
  model in full edit mode alongside the report. This is what you want while
  developing.
- **`byConnection`** — a connection string to a model already in a Fabric workspace.
  Desktop opens the report live-connected and will not edit the model. **Required
  when deploying via the Fabric REST API.**

A report with `byConnection` and no sibling `.SemanticModel` folder is a *thin
report*. That is a normal, valid arrangement — not a missing file.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definitionProperties/2.0.0/schema.json",
  "version": "4.0",
  "datasetReference": {
    "byConnection": { "connectionString": "semanticmodelid=<id>" }
  }
}
```

A useful trick: keep `definition.pbir` on `byPath` for development and a second
`definition-liveConnect.pbir` on `byConnection` beside it. Git integration ignores
the second file, but you can open it when you need report-level measures.

## `.platform`

Fabric's identity file for Git integration. It carries a `logicalId` that **Fabric
assigns** — a hand-written one silently breaks the link between the folder and the
workspace item.

**Never generate this file.** If it's missing, the project still works locally; the
validator reports a warning, and the fix is to let Desktop or Fabric create it, not
to invent one.

## Two format decisions, both one-way

| Artifact | Legacy | Current | Notes |
|---|---|---|---|
| Report | `report.json` (PBIR-Legacy) | `definition/` (PBIR) | Legacy is undocumented and unsupported for external editing |
| Model | `model.bim` (TMSL) | `definition/` (TMDL) | TMSL is one large JSON blob |

Both upgrades happen by enabling the preview feature and saving. **Neither can be
reverted from the UI.** Desktop keeps a 30-day backup, but take your own copy first.

Having both formats present at once means the project won't load — the validator
treats it as an error.

Only the current formats are agent-editable. If a project is still on the legacy
formats, converting it is the first real step, not an optional nicety.

## Files that are never externally editable

`report.json` (the legacy one at the report root), `mobileState.json`,
`semanticModelDiagramLayout.json`, and `diagramLayout.json`. Microsoft does not
document their schemas and does not support changes. Leave them alone; let Desktop
own them.

Note the name collision: **`definition/report.json` (PBIR) is documented, schema'd,
and fully editable** — it holds report-level filters, theme registration, and
annotations. The undocumented one is the file at the *report folder root*.

## Git

Desktop writes its own `.gitignore` when saving a PBIP:

```
**/.pbi/localSettings.json
**/.pbi/cache.abf
```

The repo's root `.gitignore` already covers these plus `*.pbix` and `*.pbit`.
Everything else in a PBIP is text and **is tracked deliberately** — that's the whole
point (`CLAUDE.md` principle 3).

Configure line endings once, or every save looks like a whole-file rewrite:

```bash
git config core.autocrlf true
```

## Annotations

`report.json`, `page.json`, and `visual.json` all accept free-form `annotations` as
name/value pairs. Desktop ignores them entirely, which makes them a clean place to
stash machine-readable metadata — the spec that generated a page, a
`portfolio-measures` key, a deployment target.

```json
"annotations": [
  { "name": "specVersion", "value": "2026-07-27" },
  { "name": "catalogMeasure", "value": "milestone_hit_rate" }
]
```
