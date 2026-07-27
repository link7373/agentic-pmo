# Dashboard Spec: <surface name>
Tier: <operational | tactical | executive>   ·   Owner: portfolio-analyst   ·   Date: YYYY-MM-DD
Status: <draft | approved | handed off | built>   ·   Target platform: <Power BI | Tableau | other | undecided>

> This is a **specification, not a built dashboard**. It defines the questions, model, measures, and layout
> precisely enough to be built without further interpretation. See `## Handoff` for the build route.

## The questions this surface answers
_Name **one to three**. A surface that answers more than three questions answers none of them well — split it._

1. <question>
2. <question>
3. <question>

## Decisions this surface must support
_Every visual below earns its place by serving one of these; visuals serving none get cut._

| Decision | Who makes it | How often | What they need to see |
|----------|--------------|-----------|----------------------|
|          |              |           |                      |

## Audience & scope
- **Primary audience:** <role>  ·  **Secondary:** <role>
- **In scope:** <which portfolio, which stages, which period>
- **Out of scope:** <state it — prevents the surface sprawling into a second report>

## Semantic model
**Grain:** _what exactly one row represents (e.g., one project per reporting period). Ambiguous grain is the
root of most double-counting — be explicit._

Model as a **star schema** — a fact table surrounded by dimensions, not one wide table and not snowflaked —
with **exactly one date table** honouring the fiscal calendar in `knowledge/cadence.md`. Specify it this way
even when the target platform is undecided; it is the shape every BI tool wants, and specifying anything else
means the builder redesigns the model before they can start.

| Table | Fact / dimension | Grain | Source | Key fields | Refresh |
|-------|------------------|-------|--------|-----------|---------|
|       |                  |       |        |           |         |

**Relationships:** _single-direction unless bidirectional is justified in writing below. Ambiguous filter
paths produce believable wrong numbers, which is worse than an error._

| From | To | Cardinality | Direction | Justification if bidirectional |
|------|----|-------------|-----------|-------------------------------|
|      |    |             |           |                               |

## Measure catalog
_Every measure defined once, here. If two surfaces disagree about "on track", this table is the arbiter._

**The measure name is a contract.** Whoever builds this implements the name character for character. A name
that drifts between this spec and the built surface is a defect, not a variation. Ratios are computed from
summed numerator and denominator, never as an average of ratios — that gives a wrong total row.

| Measure | Plain-English definition | Formula / logic | Format | Owner |
|---------|-------------------------|-----------------|--------|-------|
|         |                         |                 |        |       |

**Ambiguity notes:** <any term with more than one plausible reading — "active", "on track", "complete" — and
the single definition adopted.>

## Pages & layout
> **Name every page and visual using letters, digits, underscores and hyphens only** — `Portfolio_Overview`,
> not `Portfolio Overview`. Spaces and punctuation are silently discarded by some build targets, taking the
> whole page with them. Decide the safe name here so the builder never has to rename and break a drill path.

### Page <n>: <Safe_Name>
- **Answers:** <which question/decision from above>
- **Visuals:** <safe name · type · measure(s) · dimension(s) · why this form>
- **Filters / slicers:** <what the reader can change, and the default state>
- **Empty state:** <what shows when there's no data — never a blank canvas>

**Visual design** — chart selection, colour, and decluttering follow the build target's design standard
rather than being restated here. This spec fixes *what each visual must show and why*; the builder fixes how
it looks. Encode palette, status colours and typography **once in a theme**, not per visual.

## Drill paths
_Every aggregate should reach its source rows in one or two steps._

| From | To | Passes context | Purpose |
|------|----|----------------|---------|
|      |    |                |         |

## Data confidence display
_How the surface shows the trustworthiness of what it's displaying — not just the values._
- <e.g., confidence badge per item; a visible count of low/missing submissions feeding each aggregate>

## Refresh, lineage & access
- **Refresh cadence:** <schedule>  ·  **Data as-of shown on the surface:** <where>
- **Lineage:** <source → transform → surface, so a reader can trace any number>
- **Access:** <who can see which tier; any row-level restriction>
- **Failure behaviour:** <what the surface shows when a refresh fails — stale data must announce itself>
- **Publishing:** <who may publish this, and to whom. Widening the audience is a decision, not a step.>

## Privacy
A portfolio surface carries people's names — sponsors, managers, the owner of every gap. Two consequences the
builder must be told about:

- **Saved filter and slicer selections can persist into the report's own files.** A visual left filtered to a
  named manager writes that name into a file that then gets committed. Specify the default filter state, and
  keep it impersonal.
- **Individual-level performance is out of scope.** This surface reports the health of *work*, not the
  performance of *people*. Data-quality gaps are attributed to an owner so they can be fixed, not ranked.

## Handoff
_The PMO specifies; a build capability implements. This section is the contract between them._

- **Build route:** <the BI capability | a report developer | undecided>
- **Capability tier available:** <spec only | full project authoring | CLI-accelerated | workspace-connected>
  — this determines what "handed off" actually delivers; confirm it before promising a date.
- **Ready to hand over:** the questions, decision list, semantic model, measure catalog, page layout and safe
  names, drill paths, refresh/lineage/access, and the privacy constraints above.
- **The builder owns:** platform mechanics, chart formatting against their design standard, theme
  implementation, validation, and reconciling every displayed number against an independent query.
- **Not done until:** the surface has been opened and confirmed to render, every number reconciles, and the
  empty state and a single-category filter have both been tested. A spec that validates is not a spec that works.
- **Open questions blocking the build:**
  - <question — owner — needed by>

## Review
- **Validated against the decisions above by:** <name, date>
- **Next review:** <date — specs drift as the portfolio changes>

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
