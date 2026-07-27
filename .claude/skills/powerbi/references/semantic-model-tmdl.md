# TMDL — authoring the semantic model

> Source of truth: [Microsoft — TMDL overview](https://learn.microsoft.com/analysis-services/tmdl/tmdl-overview)
> and [project semantic model folder](https://learn.microsoft.com/power-bi/developer/projects/projects-dataset).

TMDL is YAML-like: indentation denotes the object tree, minimal punctuation, one file
per table. It exposes the full Tabular Object Model, so any TOM property is settable.

## Folder layout

```
ExecRevenue.SemanticModel/
├── definition.pbism            REQUIRED
└── definition/
    ├── database.tmdl           compatibility level
    ├── model.tmdl              model properties + ref ordering
    ├── relationships.tmdl      ALL relationships
    ├── expressions.tmdl        ALL shared M expressions / parameters
    ├── dataSources.tmdl        ALL data sources
    ├── functions.tmdl          DAX user-defined functions
    ├── tables/<Table>.tmdl     one file per table
    ├── cultures/<culture>.tmdl
    ├── perspectives/
    └── roles/
```

One file per *table*, *role*, *culture*, *perspective*. Everything else — all
relationships, all expressions — collapses into a single shared file. Columns,
measures, hierarchies, and partitions live inside their parent table's file.

## Syntax rules that actually bite

**Indentation is a single tab per level**, and the levels mean something:

1. object declaration
2. object properties
3. multi-line expressions

Getting this wrong is a parse error, not a style problem. Multi-line expressions must
be indented one level deeper than the properties they sit under.

**Names need single quotes** if they contain a dot, equals, colon, single quote, or
whitespace. `table 'Date'` — quoted because `Date` is fine but the convention avoids
ambiguity; `column 'Net Price'` — quoted because of the space. Escape an internal
quote by doubling it.

**Two delimiters, and they are not interchangeable:**
- `=` assigns a default property or an expression (measures, partitions)
- `:` assigns every other property

**Booleans have a shorthand.** `isHidden` on its own means `isHidden: true`.

**Descriptions use `///` above the declaration** and are first-class — this is the
cheapest documentation you will ever write, and it surfaces in Desktop's field list.

## A table

```tmdl
/// Fact table. One row per order line. Grain: order_line_id.
table Sales
	lineageTag: e9374b9a-faee-4f9e-b2e7-d9aafb9d6a91

	/// Net revenue after discounts and returns. Catalog: net_revenue.
	measure 'Net Revenue' = SUM(Sales[net_amount])
		formatString: \$#,##0
		displayFolder: Revenue

	measure 'Net Revenue LY' =
			VAR ly = CALCULATE([Net Revenue], SAMEPERIODLASTYEAR('Date'[Date]))
			RETURN ly
		formatString: \$#,##0
		displayFolder: Revenue

	column net_amount
		dataType: double
		isHidden
		sourceColumn: net_amount
		summarizeBy: none

	column order_date
		dataType: dateTime
		isHidden
		sourceColumn: order_date
		summarizeBy: none

	partition Sales = m
		mode: import
		source =
				let
					Source = Sql.Database(ServerName, DatabaseName),
					mart = Source{[Schema="marts", Item="fct_order_lines"]}[Data]
				in
					mart
```

Note `summarizeBy: none` on numeric columns. Power BI defaults to `sum`, which puts
an implicit measure next to your explicit one and guarantees somebody eventually uses
the wrong one. Turn it off; expose measures only.

## Relationships

All of them in `relationships.tmdl`, keyed by GUID:

```tmdl
relationship cdb6e6a9-c9d1-42b9-b9e0-484a1bc7e123
	fromColumn: Sales.order_date
	toColumn: 'Date'.Date
```

Default cardinality is many-to-one and default filter direction is single. **Leave
both alone unless you can state why.** Bidirectional filtering creates ambiguous
paths and non-obvious wrong numbers — the failure mode is a plausible figure, not an
error. If you set one, record the reason in `knowledge/decision-log.md`.

## The date table

Every model gets exactly one, marked as the date table, with a contiguous date range
covering the fact data. Without it, time intelligence (`SAMEPERIODLASTYEAR`, `DATESYTD`)
silently misbehaves at period boundaries.

Turn **off** Power BI's Auto date/time (`File → Options → Data Load`). It generates a
hidden date table per date column, bloating the model and fragmenting your time logic.

Respect the fiscal calendar recorded in `knowledge/cadence.md` — a fiscal calendar that
disagrees with the organization is a reconciliation bug waiting to be discovered by an
executive.

## `model.tmdl` and `ref`

```tmdl
model Model
	culture: en-US
	defaultPowerBIDataSourceVersion: powerBI_V3

ref table 'Date'
ref table Sales
ref table Customer
```

`ref` fixes collection order so serialization round-trips don't churn the diff. Two
deserialization rules matter:

- a `ref` whose file is missing is **ignored** — the table vanishes silently
- a file with no `ref` is appended at the end — it still loads

## Shared expressions

```tmdl
expression ServerName = "prod-replica.internal" meta [IsParameterQuery=true, Type="Text", IsParameterQueryRequired=true]
```

**Expressions and tables share one namespace.** `expression Sales` alongside
`table Sales` means the model will not load. Naming parameters after fact tables is
the usual way into this. Prefix them (`p_ServerName`) and it can't happen.

Never commit a real credential here. Parameterise the server and database and keep
secrets in the environment; the repo `.gitignore` covers the usual files, but it can
only protect you from the mistakes it knows about.
Parameterise the server and database; keep secrets in the environment.

## Partial declaration

A table's definition can be split across files, C#-style. Tempting for putting all
measures in one place — but the same property cannot be declared twice, and the
convention here is one table per file. Deviate only with a reason.

## Editing safely

Close Power BI Desktop before editing TMDL and restart it after. Desktop holds the
model in memory, is unaware of your changes, and will overwrite them on its next
save. Then run `validate_pbip.py`, which checks expression/table collisions, `ref`
integrity, duplicate declarations, relationship endpoints, and indentation.
