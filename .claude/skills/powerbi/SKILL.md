---
name: powerbi
description: Build and edit Power BI portfolio dashboards as code via PBIP projects — semantic model in TMDL, report pages and visuals in PBIR, theme JSON, deterministic validation, and publishing. Use when a portfolio dashboard, measure, or model needs building, fixing, or reviewing. Dispatches the portfolio-analyst with powerbi-validator.
---

# /powerbi — PBIP authoring & validation

Owner: `portfolio-analyst`, with `powerbi-validator` for the validation gate. Args describe the work, e.g.
`/powerbi build the leadership portfolio rollup`.

A PBIP project is plain text — TMDL for the model, JSON for the report. That makes a Power BI dashboard an
ordinary artifact: spec'd, built, diffed, reviewed, and version-controlled like everything else the PMO ships.
Work it as code, not as a GUI you can't reach.

## When to use
After `/design-dashboard` has produced a spec and the portfolio's reporting platform is Power BI. This skill
owns **implementation only** — it does not re-derive requirements.

## Procedure

1. **Check this is the right path.** Confirm Power BI is the portfolio's reporting platform in
   `knowledge/integrations.md`. If it's Tableau or something else, stop — none of the guidance below transfers.
   If no platform is recorded, ask before building anything.

2. **Orient in the project format.** If this is your first pass on a project (or it was built elsewhere),
   read `references/pbip-project-format.md` for the PBIP folder anatomy — what each file is, what Desktop
   generates, and what must never be hand-written.

3. **Detect what you can actually do.** Read `references/tooling-tiers.md` and run the detection commands.
   State the tier you're working in before you start — it determines whether you can bulk-format, publish, or
   only author files. Never install anything yourself; recommend it, say what the licence costs are, and let
   the user decide.

4. **Spec before building.** Do not re-derive the requirements here — `/design-dashboard` owns the audience
   tier, the one-to-three questions, the measures, the grain and model, the filters, the drill paths and the
   layout. If there is no spec at `knowledge/portfolio/dashboard-<surface>.md` yet, go write one first.

5. **Build the model layer.** Star schema, exactly one dedicated date table honouring the fiscal calendar in
   `knowledge/cadence.md`, reading from the portfolio register and its cycle artifacts — no heavy
   transformation inside Power BI (`standards/powerbi-standards.md`). Author TMDL per
   `references/semantic-model-tmdl.md`; write measures per `references/dax-patterns.md`, named **exactly** as
   `knowledge/portfolio-measures.md` names them. A measure whose name or logic drifts from the catalog is a
   defect, not a variation — route conflicts back to the catalog, don't resolve them in DAX.

6. **Build the report layer.** Pages and visuals per `references/pbir-visuals.md`. Chart choice, colour,
   layout, and decluttering come from `standards/dashboard-standards.md` — that file is the single source of
   truth for design and this skill does not restate or override it. Name every page and visual folder in
   `[A-Za-z0-9_-]` only; anything else is silently discarded by Desktop (`references/gotchas.md`).

7. **Set the theme once.** Encode the palette, semantic status colours, and typography in a theme file rather
   than formatting visuals individually (`references/theme-json.md`). Theme-first is what makes the design
   standard hold across every page without hand-editing each visual — and what makes a rebrand a one-file change.

8. **Validate before anyone opens it.** Run the checker:
   ```bash
   python .claude/skills/powerbi/scripts/validate_pbip.py dashboards/<name>
   ```
   Fix every ERROR — those either block Desktop from opening or cause pages and visuals to vanish silently.
   Triage WARNs, don't ignore them. At Tier 2+, also run `pbir validate`. For anything stakeholder-facing, hand
   off to `powerbi-validator` for an independent pass.

9. **Reconcile, then ship.** Open the project in Power BI Desktop and confirm it renders — validation proves
   the files are well-formed, only Desktop proves the report works. Cross-check every displayed number against
   the register and cycle artifacts it came from, saving the checks in `dashboards/<name>/checks/`. Test the
   empty state and a single-category filter. Screenshot into `dashboards/<name>/`, update the
   `dashboards/README.md` inventory. Publishing to a broad audience → confirm with the user first
   (`references/publishing.md`).

10. **Record what you learned.** Model quirks or data oddities → the spec's open questions and
   `knowledge/portfolio.md`. Measure semantics, exclusions, fiscal handling → `knowledge/decision-log.md`,
   since a measure definition binds every other surface.

## Hard rules

- **Write every file as UTF-8 without BOM.** A BOM anywhere in the project — including the gitignored
  `.pbi/localSettings.json` — stops Desktop opening it entirely. On Windows, `Set-Content -Encoding utf8`,
  `Out-File`, and `>` in PowerShell 5.1 all add one; write from Python with `encoding="utf-8"` instead.
- **Never hand-edit a `.pbix`.** It is a binary. Convert to PBIP, or work through Desktop.
- **Never generate a `.platform` file.** Its `logicalId` is assigned by Fabric; a hand-written one corrupts the
  Git link. Missing is a warning, not something to fix.
- **Never rewrite a DAX measure silently.** Surface the change and the reason.
- **Restart Desktop after external edits.** It does not watch the filesystem and will overwrite your work from
  its in-memory copy.
- **Never leave a person's name in saved filter state.** A portfolio surface names sponsors, managers and gap
  owners; filter and slicer selections persist into `visual.json` and then into git.

## Methods & standards
`standards/powerbi-standards.md` (mechanics), `standards/dashboard-standards.md` (design — the authority),
`knowledge/methods/portfolio-management.md` (what the surface is for, reporting tiers, privacy).

## Output
A PBIP project at `dashboards/<name>/`, validated clean, with reconciliation checks in
`dashboards/<name>/checks/`, a screenshot, and an inventory row in `dashboards/README.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
