# Power BI validator tests

> **Created by Colin Beck**
> LinkedIn: https://www.linkedin.com/in/beckcolin/
> GitHub: https://github.com/link7373


> Regression suite for `../scripts/validate_pbip.py`. Standard library only, no
> installs, runs anywhere Python does. Fixtures are built in a temp directory and
> cleaned up — nothing touches the repo.

```bash
python .claude/skills/powerbi/tests/run_tests.py      # -v to show each finding
```

Exit 0 = all pass. **Run it after any change to the validator.**

## What it asserts

1. The clean fixture validates with zero errors and exit 0.
2. Each of 16 injected defects raises **its specific code** at the **right severity**,
   with the right exit code.

| File | Purpose |
|---|---|
| `make_fixture.py` | Builds a minimal PBIP; `[defect]` injects one named fault. `--list` shows them all. |
| `run_tests.py` | Builds every case, runs the validator's `--json` output, asserts codes. |

## The fixture is a real project

Not a stub. Two-table star schema with **inline data** (no external files), one page,
a card and a column chart, a registered theme. Open it in Power BI Desktop and
refresh: the card reads **$112,000** and the chart shows six months of 2026.

```bash
python .claude/skills/powerbi/tests/make_fixture.py /tmp/scratch
```

That makes it useful beyond testing — it's the fastest way to get a known-good PBIP
in front of Desktop when you're debugging whether a problem is yours or the project's.

## Don't "tidy" the schema versions

`make_fixture.py` pins a proven combination — `version.json` value `2.0.0`,
`report/3.0.0`, `page/2.0.0`, `visualContainer/2.4.0`. Every type also has a `1.0.0`
folder, which looks like the safe default and is the one value that fails **silently**:
Desktop loads the model and renders no pages, with no error. `PBIR014` exists to catch
exactly that. See `../references/pbir-visuals.md`.

## Why this suite exists

Every check here was written after a real failure, and several were found only by
opening the project in Desktop *after* the validator reported clean:

- `ENC001` — a BOM in the gitignored `.pbi/localSettings.json`. Git never shows it;
  Desktop refuses to open the project.
- `PBIR014` — schema versions pinned at `1.0.0`. Model loaded, zero pages, no error.
- `THEME003` / `THEME004` — theme registration needs *two* blocks (`themeCollection`
  **and** `resourcePackages`), and the original `THEME001` resolved paths under the
  item's type instead of the package's. That version passed a fixture built with the
  same misunderstanding, and would have thrown **false errors on every real report**.

That last one is the point. A check can look right, pass your own fixture, and still
be wrong about real files — which is worse than no check, because it teaches people to
ignore the validator. A clean run here is necessary, not sufficient: `/powerbi` step 8
still requires opening the project in Desktop.
