---
name: track-financials
description: Run the financial cycle — refresh actuals against cost baselines, compute earned-value indices (CPI/EAC/VAC), forecast the remaining work, check funding envelopes, and review whether claimed benefits actually arrived. Use monthly or before a gate. Dispatches the financial-analyst.
---

# /track-financials — Where the money actually is

## When to use
The monthly financial cycle, before a gate or steering committee, or when a project's spend stops matching its
progress.

## Dispatches
`financial-analyst` (lead) + `delivery-monitor` (schedule-side earned value and completion evidence).

## Inputs
`knowledge/financials.md` (baselines, actuals, benefits register), `knowledge/projects/`,
`knowledge/status/`, `knowledge/change-log.md` (approved changes that moved a baseline),
`knowledge/portfolio.md`, `knowledge/cadence.md` (fiscal calendar).

## Steps
1. **Refresh actuals.** Record spend to date per project against its envelope. Where spend data hasn't been
   provided, the actual is **unknown** — not zero and not the forecast. Name the gap and its owner.
2. **Check baseline integrity.** Every approved change in `knowledge/change-log.md` should have re-baselined
   `knowledge/financials.md`. Any that didn't is the first finding — without it, every variance below is
   measured against a target everyone has already agreed is wrong.
3. **Compute earned value where a baseline exists.** CPI = EV/AC, SPI = EV/PV, EAC = BAC/CPI, VAC = BAC−EAC.
   Where there is no cost baseline, write "CPI unavailable — no cost baseline" rather than deriving one. EV
   needs objective completion criteria; percent-complete self-reported by the team is not objective.
4. **Forecast the remaining work.** Sunk cost is data, not an input. Use `EAC = AC + (BAC − EV)` only when you
   can name what specifically changed about the remaining work — "we'll catch up" is not that. Give a range
   with its drivers.
5. **Check the envelopes.** Approved vs. committed vs. spent per funding source; flag any envelope that the
   current forecast breaches, and by when.
6. **Review benefits.** For each benefit in the register whose realization window has started, compare actual
   against claim — **including when it didn't arrive**. Feed the delta back into estimating; that loop is what
   makes the whole exercise worth running.
7. **Lead with the exceptions.** Projects where CPI is deteriorating, an envelope is at risk, or a benefit has
   silently disappeared. Everything on plan goes in a table, not in prose.

## Methods
`knowledge/methods/financial-management.md` (forecasting discipline, EAC choice, benefits realization),
`knowledge/methods/project-management.md` (full EVM mechanics),
`knowledge/methods/portfolio-management.md` (portfolio KPIs, reporting tiers).

## Output
Updated registers in `knowledge/financials.md` (actuals, EVM, benefits, assumptions) and a review artifact at
`knowledge/financials/YYYY-MM-DD-<period>-financial-review.md`; benefits reviews as
`YYYY-MM-DD-<initiative>-benefits-review.md`. Log any re-forecast or benefit write-off to
`knowledge/decision-log.md`. Follow `standards/document-standards.md`.

## Optional sync
If `knowledge/integrations.md` configures Slack or Notion, offer to post the exceptions summary. Never post
project-level cost detail to a broad channel without confirming the audience. Files remain source of truth.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
