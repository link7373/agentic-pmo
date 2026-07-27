# Sample dashboard — `Portfolio_Sample`

A working Power BI portfolio dashboard, built as a PBIP project by `/powerbi`, for checking that the capability
renders end to end on your machine. **The data is fictional** — six invented projects across two programs, six
monthly periods, inline in the model. Nothing connects to anything and there are no credentials.

Illustrative only. The live PMO reads from `knowledge/`, never from `examples/`.

---

## ⚠️ Before you open it: enable three preview features

PBIP and its text formats are Microsoft **preview** features and are **off by default**. Without them the
project either won't open or won't be editable as text. In Power BI Desktop:

**File → Options and settings → Options → Preview features**, tick:

1. **Power BI Project (.pbip) save option**
2. **Store semantic model using TMDL format**
3. **Store reports using enhanced metadata format (PBIR)**

Restart Desktop. If a project doesn't open and you skipped this, that's the reason.

## Open it

```bash
start examples/sample-dashboard/Portfolio_Sample/Portfolio_Sample.pbip
```

Then **Refresh** to load the inline data.

## What you should see

Two pages. If these match, the capability works end to end.

**`Portfolio Overview`** — four KPI cards across the top, most important top-left per
`standards/dashboard-standards.md`:

With no filters applied, the cards show all six projects across all six periods:

| Card | Expected | Why that number |
|------|----------|-----------------|
| Milestone Hit Rate | **82.5%** | 85 of 103 milestones hit |
| SPI | **0.94** | earned 10,107 against planned 10,735 |
| CPI | **0.91** | earned 10,107 against actual 11,112 |
| Projects Reporting | **6** | distinct projects submitting |

Below them: a **line chart** of Milestone Hit Rate by month, and a **column chart** of Capacity Demand FTE by
program.

**`Delivery Detail`** — a Data Confidence Rate card (**88.9%** — 32 of 36 submissions at High or Medium), SPI by
project, and Capacity Demand FTE by manager.

The data tells a deliberate story. `Core_Ledger_Uplift`'s milestone hit rate slides 1.00 → 1.00 → 0.75 → 0.75 →
0.60 → 0.40 while its RAG stays **Green for the first four periods**, only turning Amber in period 5 and Red in
period 6. That's the watermelon pattern the intake contract in `knowledge/methods/portfolio-management.md` exists
to catch — green outside, red inside, and visible in the trend long before the status colour admits it.

> Card totals are computed from the source data in `build_sample.py`, not read off a rendered report. If a card
> disagrees with the table above, that's a finding worth telling me about — it means the model aggregates
> differently than the arithmetic predicts.

## What is and isn't verified

**Verified here, by running it:**
- `validate_pbip.py` → **0 errors**, exit 0. The only warnings are two `PBIP005` (no `.platform`), which are
  deliberate — see below.
- No UTF-8 BOM anywhere (the validator sweeps every file, including gitignored ones; a BOM stops Desktop opening
  the project at all).
- Every field binding resolves against the model. A wrong measure name raises `XREF002`, and there are none —
  so all six measure names and all four dimension columns referenced by visuals exist as named.

**Confirmed in Power BI Desktop on 2026-07-27:** the project opens, both pages render, the model refreshes, and
all five card values match the table above. `lineChart` data roles work as expected. Verified by the repo owner
on Windows — validation alone never proved any of this.

## If something still fails

**`Expression.Error: We cannot convert the value #datetime(...) to type Date`** — fixed as of the rebuild on
2026-07-27. The `Date` table used to compute its month label with `Date.ToText`, which takes a `date` and
rejects a `datetime`. Every partition now contains **only literal values**, computed in Python by
`build_sample.py`, so no Power Query expression is evaluated at all and this class of failure can't recur. If
you still see it, you're on the old generated files — re-run the generator.

**A blank visual** — check the visual's `visualType` against its data roles in
`.claude/skills/powerbi/references/pbir-visuals.md`. Binding a field to a role the visual doesn't have is
ignored silently. `card` (Values), `columnChart` and `lineChart` (Category/Y) are all confirmed working here.

**The project won't open at all** — almost always the preview features at the top of this file, or a UTF-8 BOM.
The generator writes BOM-free and the validator sweeps for BOMs, so if you haven't hand-edited a file, it's the
preview features.

## Known gaps, deliberately

- **The date table is not marked as a date table**, which `standards/powerbi-standards.md` requires. The
  reference files don't document that TMDL property's syntax and I wasn't willing to put unverified syntax into
  a model that then wouldn't load. Mark it in Desktop (right-click `Date` → *Mark as date table* → `Date`). No
  time-intelligence DAX is used here, so nothing in the sample depends on it.
- **No `.platform` files.** Their `logicalId` is assigned by Fabric and a hand-written one corrupts the Git
  link, so the hard rule is never to generate one. The two `PBIP005` warnings are the correct outcome, not a
  defect. Fabric or Desktop creates them if you ever connect this to a workspace.
- **Auto date/time** should be off (**Options → Data Load**). It generates a hidden date table per date column.

## Regenerating

```bash
python examples/sample-dashboard/build_sample.py
```

Replaces the project in place. The generator is the artifact — it writes every file from Python with
`encoding="utf-8"`, deliberately, because Windows PowerShell 5.1's `Set-Content -Encoding utf8`, `Out-File`, and
`>` all add a BOM and Desktop then refuses to open the project. **Close Desktop before regenerating** — it does
not watch the filesystem and will overwrite the new files from its in-memory copy on the next save.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
