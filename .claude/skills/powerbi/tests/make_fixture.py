#!/usr/bin/env python3
"""Build a minimal PBIP fixture, optionally injecting one named defect.

Used by run_tests.py to regression-test validate_pbip.py. Also handy on its own
when you want a tiny, known-good PBIP to open in Power BI Desktop.

    python make_fixture.py <dest> [defect]
    python make_fixture.py --list

The clean fixture is a genuinely working project: a two-table star schema with
inline data (no external files), one page, a card and a column chart. Opened in
Desktop and refreshed, the card reads $112,000 and the chart shows six months.

Every schema version here is pinned to a combination proven to load. Do not
"tidy" them to 1.0.0 — see references/pbir-visuals.md for why that silently
produces a blank report.

Standard library only. Part of the Agentic BI Team. Created by Colin Beck.
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

S = "https://developer.microsoft.com/json-schemas/fabric/item/report"

V_VERSION = "2.0.0"                                    # value inside version.json
SCH_REPORT = f"{S}/definition/report/3.0.0/schema.json"
SCH_PAGE = f"{S}/definition/page/2.0.0/schema.json"
SCH_VISUAL = f"{S}/definition/visualContainer/2.4.0/schema.json"
SCH_PAGES_META = f"{S}/definition/pagesMetadata/1.0.0/schema.json"
SCH_VERSION_META = f"{S}/definition/versionMetadata/1.0.0/schema.json"
SCH_BOOKMARK = f"{S}/definition/bookmark/1.0.0/schema.json"
SCH_PBIR = f"{S}/definitionProperties/2.0.0/schema.json"
SCH_PBISM = ("https://developer.microsoft.com/json-schemas/fabric/item/"
             "semanticModel/definitionProperties/1.0.0/schema.json")
SCH_PLATFORM = ("https://developer.microsoft.com/json-schemas/fabric/"
                "gitIntegration/platformProperties/2.0.0/schema.json")

# defect -> the validator code it must raise
DEFECTS = {
    "page-space":     "PBIR006",   # space in a page folder name
    "bookmark-bad":   "PBIR006",   # punctuation in a bookmark name
    "no-version":     "PBIR001",   # version.json absent
    "stale-version":  "PBIR014",   # version 1.0.0 -> silent blank report
    "missing-req":    "PBIR004",   # page.json missing displayOption
    "dup-page":       "PBIR009",   # two pages sharing a name
    "both-formats":   "PBIR012",   # PBIR and PBIR-Legacy together
    "unknown-root":   "PBIR015",   # stray property in report.json
    "theme-missing":  "THEME001",  # registered resource not on disk
    "theme-path":     "THEME003",  # 'path' inside themeCollection
    "theme-noversion": "THEME003",  # reportVersionAtImport absent
    "theme-badname":  "THEME004",   # themeCollection name not in the package
    "bad-field":      "XREF001",   # visual bound to a table not in the model
    "tmdl-collision": "SM005",     # expression name collides with a table
    "spaces-indent":  "SM004",     # TMDL indented with spaces (WARN)
    "bom":            "ENC001",    # UTF-8 BOM
}

# Defects that are warnings rather than hard errors.
WARN_ONLY = {"stale-version", "spaces-indent", "unknown-root"}


def w(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    # UTF-8 without BOM, LF — exactly what Power BI Desktop requires.
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8", newline="\n")


def wt(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def build(dest: Path, defect: str | None = None) -> Path:
    if defect is not None and defect not in DEFECTS:
        raise SystemExit(f"unknown defect '{defect}'. Known: "
                         f"{', '.join(sorted(DEFECTS))}")
    if dest.exists():
        shutil.rmtree(dest)

    rpt, mdl = dest / "Scratch.Report", dest / "Scratch.SemanticModel"
    defn = rpt / "definition"

    w(dest / "Scratch.pbip", {
        "$schema": "https://developer.microsoft.com/json-schemas/fabric/pbip/"
                   "pbipProperties/1.0.0/schema.json",
        "version": "1.0",
        "artifacts": [{"report": {"path": "Scratch.Report"}}],
        "settings": {"enableAutoRecovery": True},
    })

    w(rpt / ".platform", {
        "$schema": SCH_PLATFORM,
        "metadata": {"type": "Report", "displayName": "Scratch"},
        "config": {"version": "2.0",
                   "logicalId": "00000000-0000-0000-0000-000000000001"},
    })
    w(rpt / "definition.pbir", {
        "$schema": SCH_PBIR,
        "version": "4.0",
        "datasetReference": {"byPath": {"path": "../Scratch.SemanticModel"}},
    })

    # ---- theme ----------------------------------------------------------
    # Resource names carry the .json extension and must match across both
    # themeCollection and resourcePackages.
    theme_name = "ScratchTheme.json"
    w(rpt / "StaticResources" / "RegisteredResources" / theme_name, {
        "name": "ScratchTheme",
        "dataColors": ["#2E5C8A", "#D97706", "#0F766E", "#7C3AED",
                       "#B91C1C", "#4D7C0F"],
        "good": "#16A34A", "neutral": "#D97706", "bad": "#DC2626",
        "background": "#FFFFFF", "foreground": "#1F2937",
    })

    custom_theme = {
        "name": theme_name,
        "reportVersionAtImport": {"visual": "2.4.0", "page": "2.0.0",
                                  "report": "3.0.0"},
        "type": "RegisteredResources",
    }
    if defect == "theme-path":
        custom_theme["path"] = theme_name          # rejected: no path here
    if defect == "theme-noversion":
        del custom_theme["reportVersionAtImport"]
    if defect == "theme-badname":
        custom_theme["name"] = "NotDeclared.json"

    report_obj = {
        "$schema": SCH_REPORT,
        "themeCollection": {"customTheme": custom_theme},
        "resourcePackages": [{
            "name": "RegisteredResources",
            "type": "RegisteredResources",
            "items": [{"name": theme_name, "path": theme_name,
                       "type": "CustomTheme"}],
        }],
    }
    if defect == "theme-missing":
        report_obj["resourcePackages"][0]["items"][0]["path"] = "NotThere.json"
    if defect == "unknown-root":
        report_obj["layoutOptimization"] = "None"
    w(defn / "report.json", report_obj)

    # ---- version --------------------------------------------------------
    if defect != "no-version":
        w(defn / "version.json", {
            "$schema": SCH_VERSION_META,
            "version": "1.0.0" if defect == "stale-version" else V_VERSION,
        })

    # ---- page -----------------------------------------------------------
    page_folder = "My Page" if defect == "page-space" else "Overview"
    page_obj = {
        "$schema": SCH_PAGE,
        "name": "Overview",
        "displayName": "Overview",
        "displayOption": "FitToPage",
        "height": 720,
        "width": 1280,
    }
    if defect == "missing-req":
        del page_obj["displayOption"]
    w(defn / "pages" / page_folder / "page.json", page_obj)

    entity = "NoSuchTable" if defect == "bad-field" else "Sales"
    visuals = defn / "pages" / page_folder / "visuals"

    w(visuals / "RevenueCard" / "visual.json", {
        "$schema": SCH_VISUAL,
        "name": "RevenueCard",
        "position": {"x": 16, "y": 16, "z": 0, "width": 320, "height": 180,
                     "tabOrder": 1000},
        "visual": {
            "visualType": "card",
            "query": {"queryState": {"Values": {"projections": [{
                "field": {"Measure": {
                    "Expression": {"SourceRef": {"Entity": entity}},
                    "Property": "Revenue"}},
                "queryRef": f"{entity}.Revenue",
                "nativeQueryRef": "Revenue"}]}}},
            "drillFilterOtherVisuals": True,
        },
    })

    # A chart as well: exercises the Sales<->Date relationship, which a scalar
    # card alone never touches.
    w(visuals / "RevenueByDate" / "visual.json", {
        "$schema": SCH_VISUAL,
        "name": "RevenueByDate",
        "position": {"x": 368, "y": 16, "z": 1000, "width": 560, "height": 320,
                     "tabOrder": 2000},
        "visual": {
            "visualType": "columnChart",
            "query": {"queryState": {
                "Category": {"projections": [{
                    "field": {"Column": {
                        "Expression": {"SourceRef": {"Entity": "Date"}},
                        "Property": "Date"}},
                    "queryRef": "Date.Date", "nativeQueryRef": "Date"}]},
                "Y": {"projections": [{
                    "field": {"Measure": {
                        "Expression": {"SourceRef": {"Entity": entity}},
                        "Property": "Revenue"}},
                    "queryRef": f"{entity}.Revenue",
                    "nativeQueryRef": "Revenue"}]}}},
            "drillFilterOtherVisuals": True,
        },
    })

    if defect == "dup-page":
        w(defn / "pages" / "Second" / "page.json",
          dict(page_obj, displayName="Second"))

    w(defn / "pages" / "pages.json", {
        "$schema": SCH_PAGES_META,
        "pageOrder": ["Overview"],
        "activePageName": "Overview",
    })

    if defect == "bookmark-bad":
        w(defn / "bookmarks" / "Q1 2026!.bookmark.json",
          {"$schema": SCH_BOOKMARK, "name": "Q1", "displayName": "Q1"})

    if defect == "both-formats":
        w(rpt / "report.json", {"legacy": True})

    # ---- semantic model -------------------------------------------------
    w(mdl / "definition.pbism", {"$schema": SCH_PBISM, "version": "4.0",
                                 "settings": {}})
    w(mdl / ".platform", {
        "$schema": SCH_PLATFORM,
        "metadata": {"type": "SemanticModel", "displayName": "Scratch"},
        "config": {"version": "2.0",
                   "logicalId": "00000000-0000-0000-0000-000000000002"},
    })

    d = mdl / "definition"
    wt(d / "database.tmdl", "database Scratch\n\tcompatibilityLevel: 1567\n")
    wt(d / "model.tmdl",
       "model Model\n\tculture: en-US\n"
       "\tdefaultPowerBIDataSourceVersion: powerBI_V3\n\n"
       "ref table Sales\nref table 'Date'\n")

    # TMDL indents with tabs. Spaces here are the injected defect.
    indent = "    " if defect == "spaces-indent" else "\t"
    dup = ("\n\tmeasure Revenue = SUM(Sales[Amount])\n"
           "\t\tformatString: \\$#,##0\n" if defect == "tmdl-collision" else "")

    wt(d / "tables" / "Sales.tmdl",
       "/// Fact table, one row per order line.\n"
       "table Sales\n"
       f"{indent}lineageTag: 11111111-1111-1111-1111-111111111111\n\n"
       "\tmeasure Revenue = SUM(Sales[Amount])\n"
       "\t\tformatString: \\$#,##0\n"
       f"{dup}"
       "\n\tcolumn Amount\n\t\tdataType: double\n\t\tsourceColumn: Amount\n"
       "\t\tsummarizeBy: sum\n\n"
       "\tcolumn OrderDate\n\t\tdataType: dateTime\n"
       "\t\tsourceColumn: OrderDate\n\t\tsummarizeBy: none\n\n"
       "\tpartition Sales = m\n\t\tmode: import\n\t\tsource =\n"
       "\t\t\t\tlet\n"
       "\t\t\t\t\tSource = #table(\n"
       "\t\t\t\t\t\ttype table [OrderDate = datetime, Amount = number],\n"
       "\t\t\t\t\t\t{\n"
       "\t\t\t\t\t\t\t{#datetime(2026, 1, 15, 0, 0, 0), 12500},\n"
       "\t\t\t\t\t\t\t{#datetime(2026, 2, 12, 0, 0, 0), 18300},\n"
       "\t\t\t\t\t\t\t{#datetime(2026, 3, 9, 0, 0, 0), 15750},\n"
       "\t\t\t\t\t\t\t{#datetime(2026, 4, 22, 0, 0, 0), 21400},\n"
       "\t\t\t\t\t\t\t{#datetime(2026, 5, 30, 0, 0, 0), 19850},\n"
       "\t\t\t\t\t\t\t{#datetime(2026, 6, 18, 0, 0, 0), 24200}\n"
       "\t\t\t\t\t\t}\n"
       "\t\t\t\t\t)\n"
       "\t\t\t\tin\n\t\t\t\t\tSource\n")

    wt(d / "tables" / "Date.tmdl",
       "/// Date dimension covering calendar 2026.\n"
       "table 'Date'\n\tlineageTag: 22222222-2222-2222-2222-222222222222\n\n"
       "\tcolumn Date\n\t\tdataType: dateTime\n\t\tisKey\n"
       "\t\tsourceColumn: Date\n\t\tsummarizeBy: none\n\n"
       "\tpartition 'Date' = m\n\t\tmode: import\n\t\tsource =\n"
       "\t\t\t\tlet\n"
       "\t\t\t\t\tStart = #datetime(2026, 1, 1, 0, 0, 0),\n"
       "\t\t\t\t\tDates = List.Transform({0..364}, each Start + "
       "#duration(_, 0, 0, 0)),\n"
       "\t\t\t\t\tSource = #table(type table [Date = datetime], "
       "List.Transform(Dates, each {_}))\n"
       "\t\t\t\tin\n\t\t\t\t\tSource\n")

    wt(d / "relationships.tmdl",
       "relationship 33333333-3333-3333-3333-333333333333\n"
       "\tfromColumn: Sales.OrderDate\n\ttoColumn: 'Date'.Date\n")

    # A shared expression named after a table stops the model loading.
    expr = "Sales" if defect == "tmdl-collision" else "p_ServerName"
    wt(d / "expressions.tmdl",
       f"expression {expr} = \"localhost\" meta [IsParameterQuery=true, "
       "Type=\"Text\", IsParameterQueryRequired=true]\n")

    if defect == "bom":
        p = defn / "version.json"
        p.write_bytes(b"\xef\xbb\xbf" + p.read_bytes())

    return dest


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--list":
        for name, code in sorted(DEFECTS.items()):
            kind = "WARN " if name in WARN_ONLY else "ERROR"
            print(f"  {name:<16} {kind}  {code}")
        raise SystemExit(0)
    if len(sys.argv) < 2:
        print(__doc__)
        raise SystemExit(2)
    target = build(Path(sys.argv[1]).resolve(),
                   sys.argv[2] if len(sys.argv) > 2 else None)
    which = sys.argv[2] if len(sys.argv) > 2 else None
    print(f"built {target}" + (f" with defect '{which}'" if which else " (clean)"))
