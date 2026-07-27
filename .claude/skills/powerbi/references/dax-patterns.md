# DAX — thin measures over a clean model

> The PMO's position: **DAX is a presentation layer, not a transformation layer.**
> Complexity belongs upstream in the portfolio data itself, where it is visible and
> reviewable, rather than buried in a measure only Desktop can show you.

## Naming is not negotiable

Every measure name must match `knowledge/portfolio-measures.md` **character for
character**. Not "close enough" — identical. The catalog is the single definition, and
the moment a dashboard shows `Schedule Variance` while the catalog says
`Schedule Variance Days`, somebody is comparing two numbers that were never the same
thing.

If the measure you need isn't in the catalog, stop and add it there first, through
`portfolio-analyst`. Do not invent a definition inside a measure — that's how a
portfolio ends up with four versions of "on track" and no way to reconcile them.

Document the link in the measure description, where it shows up in Desktop's field
list:

```tmdl
	/// Net revenue after discounts and returns. Catalog: net_revenue.
	measure 'Net Revenue' = SUM(Sales[net_amount])
		formatString: \$#,##0
```

## Build on base measures

Define the metric once; derive everything else from it.

```tmdl
	measure 'Net Revenue' = SUM(Sales[net_amount])

	measure 'Net Revenue LY' =
			CALCULATE([Net Revenue], SAMEPERIODLASTYEAR('Date'[Date]))

	measure 'Net Revenue YoY %' =
			VAR current = [Net Revenue]
			VAR prior = [Net Revenue LY]
			RETURN DIVIDE(current - prior, prior)
		formatString: 0.0%
```

Change the definition of net revenue once and every derived measure follows. Repeat
`SUM(Sales[net_amount])` in twelve places and you have twelve things to update and
eleven you'll miss.

## Patterns worth knowing

**`DIVIDE`, never `/`.** `DIVIDE(a, b)` returns blank on divide-by-zero instead of an
error. A single zero denominator otherwise breaks the whole visual.

**Fully qualify columns, never qualify measures.** `Sales[amount]` and `[Net Revenue]`.
This is the community convention and it makes the two visually distinguishable —
worth following precisely because DAX won't stop you doing the opposite.

**`VAR` for anything non-trivial.** Variables evaluate once, in the filter context
where they're declared. They make intent legible and prevent accidental re-evaluation
under a changed context.

**`SELECTEDVALUE` over `VALUES`** when you want a single value with a graceful
fallback: `SELECTEDVALUE(Product[category], "All categories")`.

**Format in `formatString`, not in DAX.** `FORMAT()` returns text, which then sorts
alphabetically and won't chart. This surprises people repeatedly.

## Things that quietly go wrong

**`CALCULATE` replaces filters; it doesn't add to them.** `CALCULATE([Revenue], Product[category] = "A")`
overrides any existing category filter. To narrow within the current context use
`KEEPFILTERS`.

**Percentages don't sum.** A measure defined as an average of ratios gives the wrong
total row. Compute the ratio from summed numerator and denominator instead —
`DIVIDE(SUM(numerator), SUM(denominator))`. This is Simpson's paradox arriving
through the back door, and the total row is usually where someone notices.

**Time intelligence needs a real date table**, marked as such, contiguous. Without it
`SAMEPERIODLASTYEAR` and `DATESYTD` return subtly wrong results at period edges
rather than failing.

**Blank ≠ zero.** A blank measure hides its row in a visual; zero shows it. Decide
which you want and be explicit — `+ 0` or `COALESCE` — rather than discovering it in
a review.

**Bidirectional relationships plus `CALCULATE` produce ambiguous filter paths.** The
symptom is a believable wrong number. Prefer single-direction and explicit
`CROSSFILTER` where genuinely needed.

## When a measure is getting long

Ten lines of DAX with nested `FILTER`s over a large fact table is a signal, not an
achievement. Ask:

1. Can this be a derived column in the source data instead? Push it upstream.
2. Is it slow because the model is wrong — snowflaked, wrong grain, missing star?
3. Is it portfolio logic that belongs in `knowledge/portfolio-measures.md` rather than
   in one report?

`standards/powerbi-standards.md` sets the ceiling: no measure should need a paragraph
to explain, and nothing resembling a 200-line calculated field belongs here.

## Validating

`validate_pbip.py` checks that every field a visual binds to exists in the model, but
it does **not** evaluate DAX — it can't tell you a measure is wrong, only that it's
referenced. Correctness still requires opening Desktop and reconciling against a
direct query, which is `/powerbi` step 8 and not optional.

At Tier 3, `fab` can run DAX queries against a published model for automated
reconciliation. Until then, reconcile by hand and save the query in
`dashboards/<name>/checks/`.
