# PBIR — pages, visuals, and how they bind to data

> Source of truth: [Microsoft — project report folder](https://learn.microsoft.com/power-bi/developer/projects/projects-report)
> and the [published JSON schemas](https://github.com/microsoft/json-schemas/tree/main/fabric/item/report/definition).
> Every file carries a `$schema` URL — follow it when you need a property this page
> doesn't cover. **Do not guess property names.** Check the schema or ask.

## The `definition/` tree

```
definition/
├── version.json          REQUIRED
├── report.json           REQUIRED   report-level filters, theme, annotations
├── reportExtensions.json optional   report-level measures
├── pages/
│   ├── pages.json        optional   page order + active page
│   └── <PageName>/
│       ├── page.json     REQUIRED
│       └── visuals/
│           └── <VisualName>/
│               ├── visual.json  REQUIRED
│               └── mobile.json  optional
└── bookmarks/
    ├── bookmarks.json         optional
    └── <name>.bookmark.json   optional
```

Every `<PageName>`, `<VisualName>`, and bookmark name — folder **and** the `name`
property inside — must match `[A-Za-z0-9_-]+`. Anything else and Desktop silently
ignores the object. See `gotchas.md`.

## Picking schema versions — read this first

Every PBIR file declares its format through a `$schema` URL, and **the version in that
URL is not cosmetic.** Each object type has its own independently-evolving version
folder in [microsoft/json-schemas](https://github.com/microsoft/json-schemas/tree/main/fabric/item/report/definition)
— `visualContainer` alone is past 2.9.0 while `versionMetadata` is still on 1.0.0.

**Do not default to `1.0.0`.** It exists for every type, so it looks like a safe
choice, and it is the single worst one: Desktop opens the project, loads the semantic
model, renders **nothing**, and reports no error. You get a blank report and no clue
why.

Before authoring, check the current version folder for each type you're writing, or
copy the versions from a report Desktop saved recently. A known-good working set:

| File | `$schema` type/version | Notes |
|---|---|---|
| `version.json` | `versionMetadata/1.0.0` | but its `version` **value** is `2.0.0` |
| `report.json` | `report/3.0.0` | |
| `pages.json` | `pagesMetadata/1.0.0` | |
| `page.json` | `page/2.0.0` | |
| `visual.json` | `visualContainer/2.4.0` | latest is higher; 2.4.0 is proven |

## `version.json`

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/versionMetadata/1.0.0/schema.json",
  "version": "2.0.0"
}
```

The `version` **value** is the one that matters most: Microsoft's docs say it
"determines the required files to be loaded". Set it to `1.0.0` and Desktop looks for
a layout you didn't write, finds no pages, and silently shows an empty report. Use
`2.0.0`.

Format is `major.minor.patch`, major ≥ 1, **patch always 0**.

## `page.json`

Required: `$schema`, `name`, `displayName`, `displayOption`.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/page/2.0.0/schema.json",
  "name": "Overview",
  "displayName": "Revenue Overview",
  "displayOption": "FitToPage",
  "height": 720,
  "width": 1280
}
```

`name` is the identifier other objects reference and must be unique across the
report; `displayName` is what users see and can be anything. Keep `name` identical to
the folder name — nothing enforces it, but drillthrough and bookmarks resolve by
`name`, and a mismatch is confusing to debug.

Default canvas is 1280×720. `standards/dashboard-standards.md` governs what goes
where on it.

## `visual.json`

Required: `$schema`, `name`, `position`. Plus **exactly one** of `visual` or
`visualGroup`. `name` is capped at 50 characters.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/visualContainer/2.4.0/schema.json",
  "name": "RevenueCard",
  "position": { "x": 16, "y": 16, "z": 0, "width": 300, "height": 160 },
  "visual": {
    "visualType": "card",
    "query": {
      "queryState": {
        "Values": {
          "projections": [
            {
              "field": {
                "Measure": {
                  "Expression": { "SourceRef": { "Entity": "Sales" } },
                  "Property": "Net Revenue"
                }
              },
              "queryRef": "Sales.Net Revenue",
              "nativeQueryRef": "Net Revenue"
            }
          ]
        }
      }
    },
    "objects": { "general": [ { "properties": { "title": { "expr": { "Literal": { "Value": "'Net revenue, month to date'" } } } } } ] },
    "drillFilterOtherVisuals": true
  }
}
```

### Reading the binding

- `Expression.SourceRef.Entity` — the **table**.
- `Property` — the **column or measure**.
- `Measure` vs `Column` — which kind of field it is.
- `queryRef` — `"Table.Field"`, the same reference flattened.
- `nativeQueryRef` — the display label.

`validate_pbip.py` walks these and checks each one resolves against the TMDL model
(XREF001/XREF002), which is how you catch a measure rename before Desktop does.

### Data roles

The key under `queryState` is the visual's data role, and it differs per visual type
— `Values`, `Category`, `Y`, `Series`, `Rows`, `Columns`. Bind a field to a role the
visual doesn't have and it's ignored. Check an existing visual of the same type
before inventing role names.

### Position

`x`/`y` from the top-left of the canvas, `z` for stacking. `standards/dashboard-standards.md`
puts the most important number top-left — that means the lowest `x` and `y`, and it
is a real constraint on your layout, not a suggestion.

## Formatting cascade

Four levels, each overriding the one before:

1. Power BI defaults
2. Theme wildcards (`*` — all visuals)
3. Theme `visualStyles` for a specific visual type
4. `visual.json` `objects` — this visual only

**Work as far up the cascade as you can.** A rule expressed in the theme applies
everywhere and survives new visuals; the same rule pasted into forty `visual.json`
files is forty things to keep in sync. Per-visual formatting should be reserved for
genuine one-offs. See `theme-json.md`.

## `report.json` (the PBIR one)

Report-level filters, theme registration, annotations. **`additionalProperties` is
`false`** — any property outside the allowed set is rejected. Allowed top level:
`$schema`, `themeCollection`, `filterConfig`, `objects`, `reportSource`,
`publicCustomVisuals`, `organizationCustomVisuals`, `resourcePackages`, `annotations`,
`dataSourceVariables`, `settings`, `slowDataSourceSettings`.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/report/3.0.0/schema.json",
  "themeCollection": {
    "customTheme": {
      "name": "CompanyTheme.json",
      "reportVersionAtImport": { "visual": "2.4.0", "page": "2.0.0", "report": "3.0.0" },
      "type": "RegisteredResources"
    }
  },
  "resourcePackages": [
    {
      "name": "RegisteredResources",
      "type": "RegisteredResources",
      "items": [
        { "name": "CompanyTheme.json", "path": "CompanyTheme.json", "type": "CustomTheme" }
      ]
    }
  ]
}
```

Themes need **both** blocks: `themeCollection` selects by name,
`resourcePackages` maps name → path. The path resolves under the *package's* type
(`StaticResources/RegisteredResources/…`), not the item's. Full detail and the
failure modes are in `theme-json.md`.

## `pages.json`

Optional. Sets page order and the active page.

```json
{
  "$schema": "https://developer.microsoft.com/json-schemas/fabric/item/report/definition/pagesMetadata/1.0.0/schema.json",
  "pageOrder": ["Overview", "Detail", "Definitions"],
  "activePageName": "Overview"
}
```

A page folder missing from `pageOrder` still loads, just in undefined order —
warning, not error. An `activePageName` pointing nowhere is a non-blocking error
Desktop auto-fixes on save.

## Editing existing reports

Both source projects converged on the same rule, and it holds here: **treat report
JSON as an implementation detail.** Read it freely. When writing, prefer the highest
available leverage — theme over per-visual, `pbir set` over hand-editing at Tier 2 —
and always validate afterwards. Blind text-replacement across `visual.json` files is
how you end up with a report that opens but is subtly wrong.
