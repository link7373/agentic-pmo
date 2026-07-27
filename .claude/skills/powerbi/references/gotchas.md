# Gotchas — the failures that don't announce themselves

> The dangerous PBIP failures are not the ones that throw. They're the ones where
> Desktop opens happily and your work is quietly gone. `scripts/validate_pbip.py`
> catches every item marked **[checked]**.

## Silent data loss

**Object names outside `[A-Za-z0-9_-]`.** **[checked — PBIR006/PBIR007]**
Microsoft's rule: page, visual, and bookmark names — both the folder name *and* the
`name` property inside the JSON — must be word characters or hyphens. Violate it and
Desktop does not error. It treats the folder as a private user file, ignores it, and
the page or visual simply isn't in the report. A space is the usual culprit
(`My Page`, `Revenue Card`). This is the single most costly PBIP mistake.

**`ref table X` in `model.tmdl` with no matching `tables/X.tmdl`.** **[checked — SM006]**
TMDL deserialization ignores refs whose file is missing. The table drops out of the
model without complaint, and every measure depending on it breaks downstream.

**A stale `version.json` version, or `$schema` URLs pinned at `1.0.0`.**
**[checked — PBIR014]** Microsoft's docs say `version.json`'s `version` value
"determines the required files to be loaded". Set it to `1.0.0` and Desktop opens the
project, loads the semantic model perfectly, and then renders **no pages at all** —
empty canvas, no page tabs, no error, nothing in the log. Because the model loads,
every instinct points at the report JSON being malformed, which it isn't.

`1.0.0` is a trap precisely because every schema type has a `1.0.0` folder, so it
looks like the safe default. It isn't. See the version table in `pbir-visuals.md`.

**Copying a bookmark file between reports.** Bookmarks capture page state including
specific visual IDs. Paste one into a report whose visuals differ and the invalid
entries are stripped on save — most of the configuration disappears. Copy the page
and its visuals too, or rebuild the bookmark.

**Filter values persist into the files.** A visual filtered to
`Manager = 'A. Named Person'` stores that name in `visual.json`. Slicer selections and
per-series formatting do the same. Before committing, check you aren't writing real
people's names into git — a portfolio surface is full of sponsors, managers and gap
owners. See the privacy guidance in `knowledge/methods/portfolio-management.md`; it
applies to report metadata just as much as to an exported report.

## Model won't load

**A shared M expression sharing a name with a table.** **[checked — SM005]**
`expressions.tmdl` and `tables/*.tmdl` occupy one namespace. Declare
`expression Sales` alongside `table Sales` and the model fails to load. Parameters
named after fact tables are the common trap.

**TMDL and TMSL both present.** **[checked — SM002]** `definition/` and `model.bim`
are mutually exclusive. Same for the report: `definition/` (PBIR) and root
`report.json` (PBIR-Legacy) **[checked — PBIR012]**. Usually left behind by a
half-finished format upgrade.

**The same property declared twice.** **[checked — SM007]** TMDL supports partial
declaration across files, but declaring one measure twice is a parse error.

**A partition whose M cannot evaluate.** **[NOT checked — the validator is static]**
`validate_pbip.py` parses structure; it never executes Power Query. A partition that
fails on refresh therefore passes validation with zero errors, and "0 errors" reads as
"the model works". M's date functions are the usual culprit because they are strict
about input type — `Date.ToText` takes a `date` and rejects a `datetime` outright
(`We cannot convert the value #datetime(...) to type Date`), while `Date.Year` and
`Date.Month` accept either.

The fix is not a better check, it's less M: compute derived values **upstream** and let
the partition carry literals or a plain source query. That is what
`standards/powerbi-standards.md` already asks for, and it converts a refresh-time
failure into something that cannot fail. Where M is unavoidable, only a refresh in
Desktop proves it — treat an unrefreshed model as unverified.

## Encoding and paths

**UTF-8 with BOM.** **[checked — ENC001]** Microsoft requires UTF-8 *without* BOM, and
Desktop enforces it absolutely: the project refuses to open with
`Only text with UTF8 encoding without BOM (byte order marks) is supported`.

On Windows this is the single easiest mistake to make. **Windows PowerShell 5.1's
`Set-Content -Encoding utf8`, `Out-File`, and `>` all write a BOM.** Use
`-Encoding utf8NoBOM` (PowerShell 6+), or write from Python with
`encoding="utf-8"`, which never adds one.

The nastiest instance is **`.pbi/localSettings.json`**. Git ignores it, so it never
shows in a diff or a review — but Desktop reads it on open, and a BOM there kills the
whole project with an error that names a file you weren't even thinking about. The
validator sweeps *every* text file in the project tree for BOMs, including ignored
ones, precisely because being gitignored doesn't mean Desktop skips it.

**260-character path limit.** **[checked — ENC002]** PBIP nests deeply
(`…/definition/pages/<page>/visuals/<visual>/visual.json`). A long table name plus a
deep repo path silently breaks saves on Windows. Keep the repo root short.

**Line endings.** Desktop writes CRLF. Without `core.autocrlf` configured, every save
looks like a whole-file diff and code review becomes useless.

## Desktop behaviour

**Desktop does not watch the filesystem.** Edit files while a project is open and
Desktop will overwrite them from memory on next save. **Always close Desktop before
editing, and restart it after.** This is the most common way to lose an afternoon.

**Renaming files requires a restart** before Desktop will preserve the new names.

**Format upgrades are one-way.** PBIR-Legacy → PBIR and TMSL → TMDL cannot be
reverted through the UI. Desktop keeps a 30-day backup, but take your own copy first.

**Publishing from Desktop uploads data, not just metadata.** Unlike Fabric Git
integration or the REST API — which deploy metadata only — Desktop's Publish pushes
the local data cache too. Consider that before publishing a model built against a
local extract.

## Report structure

**`pages.json` is optional; `page.json` is not.** A page folder without `page.json`
is invalid **[checked — PBIR004]**. But a missing `pages.json` only means page order
is undefined, so treat a mismatch there as a warning **[checked — PBIR010]**.

**Page names must be unique across the report; visual names unique within a page.**
**[checked — PBIR009]** Copying a page folder without changing `name` breaks
drillthrough and tooltips.

**Theme resources must actually exist** at `StaticResources/<packageType>/<path>`,
and must be registered in `report.json` **[checked — THEME001/THEME002]**. Dropping a
theme file into `RegisteredResources` without a matching entry does nothing at all.

**Automatic visual filters only materialise after the filter pane has been expanded
once** while editing. Don't conclude they're missing from a report you generated.

## Scale limits

1,000 pages per report; 1,000 visuals per page; 300 MB total report files; 300 MB of
resource files. Reports over ~500 files get slow to *author* (viewing is unaffected).
If you're near any of these, the answer is a better-scoped dashboard, not a bigger
one — see the dead-end dashboard warning in `standards/dashboard-standards.md`.
