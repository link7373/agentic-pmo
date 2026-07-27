# Standards: Power BI

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

> Applies when the portfolio's reporting platform is Power BI (recorded in `knowledge/integrations.md`). This
> file covers **Power BI mechanics only.** All chart selection, colour, layout, and decluttering rules live in
> `standards/dashboard-standards.md` and are not restated here — there is one source of truth for design, and
> this isn't it.

## Project layout

Every dashboard is a PBIP project inside its own folder, at the repository root:

```
dashboards/<name>/
├── <Name>.pbip
├── <Name>.Report/
├── <Name>.SemanticModel/
├── checks/                      reconciliation queries
└── screenshot.png
```

The **spec lives separately**, at `knowledge/portfolio/dashboard-<surface>.md`, because it is portfolio
knowledge rather than build output and it outlives any one implementation.

Projects sit at the repo root, not under `knowledge/`, for a mechanical reason: PBIP nests deeply and Windows
still enforces a 260-character path limit. Every extra folder level in the prefix is spent on all of them.

Use the current text formats — **PBIR** for the report, **TMDL** for the model. The legacy formats
(`report.json`, `model.bim`) are undocumented, unsupported for external editing, and cannot be worked as code.
Converting is the first step on any inherited project, not an optional improvement.

The text is **tracked in git deliberately**; only binaries and per-user state are ignored (`.pbix`, `.pbit`,
`.pbi/cache.abf`, `.pbi/localSettings.json`). A dashboard is reproducible work product like every other artifact
the PMO ships.

## Naming

**Page, visual, and bookmark names — folder and `name` property — must match `[A-Za-z0-9_-]+`.** No spaces, no
punctuation. This is not style: Desktop silently ignores anything else and the object disappears from the report
with no error. Decide safe names in the spec so nobody has to rename later and break a drill path.

Keep the `name` property identical to its folder name. Nothing enforces it, but bookmarks and drillthrough
resolve by `name`.

Prefix model parameters (`p_ServerName`) — shared expressions and tables share one namespace, and a collision
stops the model loading.

## Semantic model

- **Star schema.** Facts surrounded by dimensions. Not snowflaked, not one wide table.
- **Exactly one date table**, marked as the date table, contiguous, respecting the fiscal calendar recorded in
  `knowledge/cadence.md`. Auto date/time turned **off**.
- **Read from the portfolio register and its cycle artifacts.** No heavy transformation in Power Query — if it
  needs a join, a window function, or portfolio logic, it belongs upstream in the data or in the measure
  catalog, where it is reviewable.
- **Single-direction relationships** unless bidirectional is justified *in writing* in
  `knowledge/decision-log.md`. Ambiguous filter paths produce believable wrong numbers, which is worse than an
  error.
- **`summarizeBy: none`** on numeric columns. Expose explicit measures, not implicit ones — otherwise two people
  sum the same column two ways.
- **Describe every table and measure** with `///`. It costs one line and surfaces in Desktop's field list.

## Measures & DAX

- Names match `knowledge/portfolio-measures.md` **character for character**. A measure not in the catalog goes
  into the catalog first; never invent a definition inside a measure.
- Define a base measure once; derive variants from it. No copy-pasted aggregations.
- Thin measures. If one needs a paragraph to explain, the logic belongs upstream. Nothing resembling a 200-line
  calculated field belongs here.
- `DIVIDE` over `/`. Ratios computed from summed numerator and denominator, never as an average of ratios — that
  gives a wrong total row, and the total row is where a leader reads it.
- Format via `formatString`, not `FORMAT()`, which returns text that won't sort or chart.

## Report

Design rules come from `standards/dashboard-standards.md`. Power BI adds only:

- **Theme-first.** Encode the palette, status colours, and typography once in a registered theme file.
  Per-visual formatting is for genuine one-offs. A rebrand should be a one-file change.
- Every tile reads from the model — no report-level data wrangling.
- Sync slicers across pages that share a filter context; don't make users re-filter.
- Bookmarks are for deliberate states, not a substitute for a clear layout.
- Keep well inside the platform limits (1,000 pages per report, 1,000 visuals per page, 300 MB). Approaching
  them means the dashboard is trying to answer too many questions — split it or cut it.

## Privacy

Filter and slicer selections **persist into `visual.json`**. A visual filtered to a named manager writes that
name into a tracked file. A portfolio surface is full of sponsors, managers and gap owners, so check before
committing — the privacy rules in `standards/dashboard-standards.md` and
`knowledge/methods/portfolio-management.md` apply to report metadata exactly as they do to an exported report.

Never commit credentials in `expressions.tmdl`. Parameterise server and database; keep secrets in the environment.

## Validation gate

Nothing ships without:

1. `python .claude/skills/powerbi/scripts/validate_pbip.py dashboards/<name>` clean of errors — warnings
   triaged, not ignored.
2. The project opened in Power BI Desktop and confirmed to render. Validation proves the files are well-formed;
   only Desktop proves the report works.
3. Every displayed number reconciled against the register or cycle artifact it came from, with the check saved
   in `dashboards/<name>/checks/`.
4. Empty state and single-category filter tested.
5. `dashboards/README.md` inventory updated, with a review date.

For anything stakeholder-facing, `powerbi-validator` runs an independent pass before release.

## Working on an open project

Close Power BI Desktop before editing project files and restart it afterwards. Desktop does not watch the
filesystem and will overwrite external edits from its in-memory copy on the next save. This is the most common
way to lose work in PBIP.
