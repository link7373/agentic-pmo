# Financials

> **The portfolio's money.** Owned by `financial-analyst`. Maintained by `/build-business-case`,
> `/track-financials`, `/manage-change` (cost impact) and `/close-project` (final actuals).
>
> Two rules make this file trustworthy. **Every figure is labelled measured or estimated** — a forecast that
> reads like an actual is worse than no forecast. And **no cost baseline means no earned value**: if a project
> has no approved baseline below, say "CPI unavailable — no cost baseline" rather than deriving one from a
> guess. Currency and fiscal calendar come from `knowledge/cadence.md`.

_Currency: —   ·   Fiscal year start: —   ·   Last updated: —_

## Funding summary
_Portfolio-level view. One row per funding source or budget envelope._

| Envelope | Owner / sponsor | Approved | Committed | Spent to date | Remaining | Period | Notes |
|----------|-----------------|----------|-----------|---------------|-----------|--------|-------|
|          |                 |          |           |               |           |        |       |

## Project cost baselines & actuals
_One row per project in `knowledge/portfolio.md`. `Baseline` is the approved cost baseline (BAC) — blank means
this project is not under cost control and its EVM columns must stay blank._

| Project | Envelope | Baseline (BAC) | Actuals to date (AC) | Earned value (EV) | Planned value (PV) | Forecast (EAC) | Variance (VAC) | Basis (measured/estimated) | As of |
|---------|----------|----------------|----------------------|-------------------|--------------------|----------------|----------------|----------------------------|-------|
|         |          |                |                      |                   |                    |                |                |                            |       |

## Earned-value indices
_Derived, never entered by hand. CPI = EV / AC; SPI = EV / PV. Blank where the inputs above are blank._

| Project | CPI | SPI | Trend vs. last period | Read (what it means) | Action |
|---------|-----|-----|-----------------------|----------------------|--------|
|         |     |     |                       |                      |        |

## Benefits register
_Every benefit claimed in a business case lands here so someone can be asked about it later. Seeded by
`/build-business-case`; reviewed by `/track-financials`; handed over at `/close-project`._

| Benefit | Source business case | Type (cash / cost-avoidance / non-financial) | Value | Measured how | Owner | Realization starts | Status |
|---------|----------------------|----------------------------------------------|-------|--------------|-------|--------------------|--------|
|         |                      |                                              |       |              |       |                    |        |

## Assumptions & open questions
_Rates, contingency, exchange rates, capitalization treatment — anything a number here depends on._

| Assumption | Affects | Confidence | Revisit when |
|------------|---------|------------|--------------|
|            |         |            |              |

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
