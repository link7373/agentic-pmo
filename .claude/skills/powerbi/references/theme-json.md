# Theme JSON — encoding the design standard once

> A theme is `standards/dashboard-standards.md` made executable. Every rule you put
> here applies to every visual, forever, including ones nobody has built yet.

## Why theme-first

The formatting cascade is: defaults → theme wildcards → theme visual types →
`visual.json`. Working at the theme level means a rebrand is a one-file change and a
new visual is correct the moment it's created. Working at the `visual.json` level
means forty files to keep in sync and a slow drift back toward inconsistency.

**Only format an individual visual when the requirement genuinely applies to that
visual alone.**

## Where it lives

```
<Name>.Report/
├── StaticResources/RegisteredResources/CompanyTheme.json
└── definition/report.json          <- must register it
```

Registration in `definition/report.json` takes **two blocks, both required**.
`themeCollection` says *which* theme is active; `resourcePackages` maps that name to a
file on disk. Miss either and the theme silently does not apply.

```json
{
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

Three things that are easy to get wrong, all of which Desktop reports as
**non-blocking** errors — meaning the report opens, the theme just isn't there:

- **There is no `path` in `themeCollection`.** The path lives only in
  `resourcePackages`. Putting one here is rejected as an additional property.
- **`reportVersionAtImport` is required**, and it's an object of three version
  strings (`visual`, `page`, `report`), not a single string.
- **Resource names include the `.json` extension** — `CompanyTheme.json`, not
  `CompanyTheme` — and the `name` must match between the two blocks.

The item's `type` is `CustomTheme` or `BaseTheme`, but the file resolves under the
**package's** type: `StaticResources/RegisteredResources/CompanyTheme.json`. Mixing
those two up is the classic mistake.

The validator checks all of this: THEME001 (file missing), THEME002 (file present but
unregistered, so inert), THEME003 (wrong shape in `themeCollection`), THEME004 (name
not declared in the package).

`report.json` is `additionalProperties: false` — any stray property is rejected. Its
allowed top-level set is `$schema`, `themeCollection`, `filterConfig`, `objects`,
`reportSource`, `publicCustomVisuals`, `organizationCustomVisuals`, `resourcePackages`,
`annotations`, `dataSourceVariables`, `settings`, `slowDataSourceSettings`.

## Structure

```json
{
  "name": "CompanyTheme",
  "dataColors": ["#2E5C8A", "#D97706", "#0F766E", "#7C3AED", "#B91C1C", "#4D7C0F"],
  "good": "#16A34A",
  "neutral": "#D97706",
  "bad": "#DC2626",
  "background": "#FFFFFF",
  "foreground": "#1F2937",
  "tableAccent": "#2E5C8A",
  "textClasses": {
    "title":    { "fontSize": 14, "fontFace": "Segoe UI Semibold", "color": "#1F2937" },
    "label":    { "fontSize": 10, "fontFace": "Segoe UI", "color": "#4B5563" },
    "callout":  { "fontSize": 32, "fontFace": "Segoe UI Light", "color": "#1F2937" }
  },
  "visualStyles": {
    "*": {
      "*": {
        "background":  [{ "show": false }],
        "border":      [{ "show": false }],
        "visualHeader":[{ "show": false }],
        "title":       [{ "show": true, "fontSize": 12, "fontColor": { "solid": { "color": "#1F2937" } } }]
      }
    },
    "columnChart": {
      "*": { "categoryAxis": [{ "gridlineShow": false }], "valueAxis": [{ "gridlineShow": true, "gridlineColor": { "solid": { "color": "#F3F4F6" } } }] }
    },
    "card": {
      "*": { "labels": [{ "fontSize": 32 }], "categoryLabels": [{ "fontSize": 10 }] }
    }
  }
}
```

`"*": { "*": {...} }` is the wildcard — all visual types, all series. Start there,
then narrow.

## Wiring it to the standards

Fill these from `standards/dashboard-standards.md` — that file holds the actual values,
so a colour changes in one place and every theme follows:

| Standard | Theme property |
|---|---|
| Brand palette (primary + neutrals) | `dataColors` |
| Semantic status: on track / at risk / breached | `good` / `neutral` / `bad` |
| Declutter — no borders, no backgrounds | `visualStyles.*.*.background.show: false`, `border.show: false` |
| Grey default, colour as the highlight | a muted `dataColors[0]`, accents later in the array |
| Titles state the insight | `textClasses.title` — the theme sets the *look*; you still write the words |

**Colour-blind safety is a constraint, not a preference.** Roughly 8% of men have
some CVD. Order `dataColors` blue-first, orange-second — never red/green adjacent as
the only distinction. Where traffic lights are unavoidable, carry a second encoding
(icon, position, label) so colour isn't doing the work alone.

Keep `dataColors` to 6–7 hues. A longer palette isn't more expressive; it just means
the 8th category is indistinguishable from the 3rd.

## Base themes

`report.json` may also carry a `baseTheme` from `SharedResources` (Microsoft's
built-ins, e.g. `CY24SU10`). A `customTheme` layers on top. Setting a base theme you
didn't intend is a common source of "why did all the colours change" after an import.

## Practical notes

- Validate the JSON before saving — a malformed theme fails quietly and Desktop falls
  back to defaults, which reads as "my theme didn't work" rather than an error.
- Changing the theme file requires a **Desktop restart** to take effect.
- Themes are portable across reports. Once the company theme exists, every subsequent
  dashboard should reference the same file rather than growing its own.
- At Tier 2, `pbir` can swap themes across many reports at once — useful for a
  rebrand, and exactly the kind of bulk change you don't want to do by hand.
