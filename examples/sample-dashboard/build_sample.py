#!/usr/bin/env python3
"""Build the sample portfolio dashboard as a PBIP project.

    python examples/sample-dashboard/build_sample.py [dest]

Default dest is `Portfolio_Sample/` beside this script. Re-running replaces it,
so the project is reproducible rather than a artifact nobody can regenerate.

Everything is written from Python with encoding="utf-8" and newline="\\n" —
deliberately, because Power BI Desktop refuses to open a project containing a
UTF-8 BOM, and Windows PowerShell 5.1 adds one to every file it writes. This is
the hard rule in `.claude/skills/powerbi/SKILL.md` applied to its own sample.

Data is fictional and inline (M `#table`), so there is nothing to connect and
no credential anywhere. Six projects across two programs, six monthly periods.

Schema versions are pinned to the combination proven to load. Do not "tidy"
version.json's value to 1.0.0 — Desktop then opens the project, loads the model
perfectly, and renders no pages at all, with no error.

Standard library only (Python 3.9+).
"""

from __future__ import annotations

import json
import shutil
import sys
from datetime import date, timedelta
from pathlib import Path

NAME = "Portfolio_Sample"

S = "https://developer.microsoft.com/json-schemas/fabric/item/report"
V_VERSION = "2.0.0"                    # the *value* inside version.json
SCH_REPORT = f"{S}/definition/report/3.0.0/schema.json"
SCH_PAGE = f"{S}/definition/page/2.0.0/schema.json"
SCH_VISUAL = f"{S}/definition/visualContainer/2.4.0/schema.json"
SCH_PAGES_META = f"{S}/definition/pagesMetadata/1.0.0/schema.json"
SCH_VERSION_META = f"{S}/definition/versionMetadata/1.0.0/schema.json"
SCH_PBIR = f"{S}/definitionProperties/2.0.0/schema.json"
SCH_PBISM = ("https://developer.microsoft.com/json-schemas/fabric/item/"
             "semanticModel/definitionProperties/1.0.0/schema.json")
SCH_PBIP = ("https://developer.microsoft.com/json-schemas/fabric/pbip/"
            "pbipProperties/1.0.0/schema.json")

THEME_FILE = "PortfolioTheme.json"

# ---------------------------------------------------------------- fictional data
# Two programs. Modernisation is the story: milestone hit rate slides from 0.90
# to 0.55 while its RAG stays green for the first four periods — the watermelon
# pattern the intake contract exists to catch.
PROJECTS = [
    # id,   name,                 program,          sponsor,     manager,     stage,      approach,    strategic link
    ("P001", "Core_Ledger_Uplift", "Modernisation", "A_Sponsor", "M_Alvarez", "in-flight", "hybrid",    "Reduce_Run_Cost"),
    ("P002", "Identity_Migration", "Modernisation", "A_Sponsor", "M_Alvarez", "in-flight", "predictive", "Reduce_Run_Cost"),
    ("P003", "Data_Platform_v2",   "Modernisation", "B_Sponsor", "R_Okafor",  "in-flight", "adaptive",  "Faster_Insight"),
    ("P004", "Self_Serve_Portal",  "Customer",      "C_Sponsor", "R_Okafor",  "in-flight", "adaptive",  "Grow_Adoption"),
    ("P005", "Billing_Refresh",    "Customer",      "C_Sponsor", "T_Nguyen",  "in-flight", "hybrid",    "Grow_Adoption"),
    ("P006", "Partner_Onboarding", "Customer",      "C_Sponsor", "T_Nguyen",  "approved",  "adaptive",  "Grow_Adoption"),
]

MONTHS = [(2026, m, 1) for m in range(1, 7)]

# project -> per-month (planned, earned, actual, due, hit, rag, confidence, fte)
FACTS = {
    "P001": [(100, 98, 102, 4, 4, "Green", "High", 6.0), (210, 200, 218, 3, 3, "Green", "High", 6.5),
             (330, 300, 350, 4, 3, "Green", "High", 7.0), (450, 395, 480, 4, 3, "Green", "Medium", 7.5),
             (580, 480, 620, 5, 3, "Amber", "Medium", 8.0), (700, 560, 760, 5, 2, "Red", "Low", 8.5)],
    "P002": [(80, 80, 78, 2, 2, "Green", "High", 3.0), (160, 158, 160, 2, 2, "Green", "High", 3.0),
             (250, 240, 255, 3, 3, "Green", "High", 3.5), (340, 320, 350, 3, 2, "Amber", "High", 4.0),
             (430, 400, 450, 3, 2, "Amber", "Medium", 4.0), (520, 470, 560, 3, 2, "Amber", "Medium", 4.5)],
    "P003": [(120, 125, 115, 3, 3, "Green", "High", 5.0), (250, 260, 240, 3, 3, "Green", "High", 5.5),
             (390, 400, 380, 4, 4, "Green", "High", 6.0), (530, 545, 520, 4, 4, "Green", "High", 6.5),
             (670, 690, 660, 4, 4, "Green", "High", 7.0), (810, 835, 800, 4, 4, "Green", "High", 7.0)],
    "P004": [(60, 58, 62, 2, 2, "Green", "High", 2.5), (130, 124, 135, 2, 2, "Green", "High", 3.0),
             (200, 190, 210, 2, 2, "Green", "Medium", 3.0), (275, 258, 290, 3, 2, "Amber", "Medium", 3.5),
             (350, 330, 370, 3, 3, "Green", "High", 3.5), (430, 410, 450, 3, 3, "Green", "High", 4.0)],
    "P005": [(90, 88, 92, 2, 2, "Green", "High", 4.0), (185, 180, 190, 3, 3, "Green", "High", 4.0),
             (285, 270, 295, 3, 2, "Amber", "Medium", 4.5), (390, 360, 410, 3, 2, "Amber", "Low", 5.0),
             (500, 455, 530, 4, 2, "Red", "Low", 5.5), (610, 550, 650, 4, 3, "Amber", "Medium", 5.5)],
    "P006": [(0, 0, 0, 0, 0, "Green", "High", 0.5), (0, 0, 0, 0, 0, "Green", "High", 0.5),
             (20, 18, 22, 1, 1, "Green", "Medium", 1.5), (55, 50, 58, 1, 1, "Green", "Medium", 2.5),
             (95, 85, 100, 2, 1, "Amber", "Medium", 3.5), (140, 125, 150, 2, 1, "Amber", "Low", 4.5)],
}


def w(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2), encoding="utf-8", newline="\n")


def wt(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def card(name, x, y, measure, width=300, height=160, z=0):
    return name, {
        "$schema": SCH_VISUAL,
        "name": name,
        "position": {"x": x, "y": y, "z": z, "width": width, "height": height,
                     "tabOrder": z + 1000},
        "visual": {
            "visualType": "card",
            "query": {"queryState": {"Values": {"projections": [{
                "field": {"Measure": {
                    "Expression": {"SourceRef": {"Entity": "Fact_Status"}},
                    "Property": measure}},
                "queryRef": f"Fact_Status.{measure}",
                "nativeQueryRef": measure}]}}},
            "drillFilterOtherVisuals": True,
        },
    }


def cartesian(name, vtype, x, y, cat_entity, cat_col, measure,
              width=600, height=300, z=0):
    """columnChart / lineChart — both use the Category + Y roles."""
    return name, {
        "$schema": SCH_VISUAL,
        "name": name,
        "position": {"x": x, "y": y, "z": z, "width": width, "height": height,
                     "tabOrder": z + 1000},
        "visual": {
            "visualType": vtype,
            "query": {"queryState": {
                "Category": {"projections": [{
                    "field": {"Column": {
                        "Expression": {"SourceRef": {"Entity": cat_entity}},
                        "Property": cat_col}},
                    "queryRef": f"{cat_entity}.{cat_col}",
                    "nativeQueryRef": cat_col}]},
                "Y": {"projections": [{
                    "field": {"Measure": {
                        "Expression": {"SourceRef": {"Entity": "Fact_Status"}},
                        "Property": measure}},
                    "queryRef": f"Fact_Status.{measure}",
                    "nativeQueryRef": measure}]}}},
            "drillFilterOtherVisuals": True,
        },
    }


def build(dest: Path) -> Path:
    if dest.exists():
        shutil.rmtree(dest)

    rpt, mdl = dest / f"{NAME}.Report", dest / f"{NAME}.SemanticModel"
    defn = rpt / "definition"

    w(dest / f"{NAME}.pbip", {
        "$schema": SCH_PBIP,
        "version": "1.0",
        "artifacts": [{"report": {"path": f"{NAME}.Report"}}],
        "settings": {"enableAutoRecovery": True},
    })

    # No .platform file, deliberately: its logicalId is assigned by Fabric and a
    # hand-written one corrupts the Git link. The validator warns that it's
    # missing; that warning is correct and expected here.

    w(rpt / "definition.pbir", {
        "$schema": SCH_PBIR,
        "version": "4.0",
        "datasetReference": {"byPath": {"path": f"../{NAME}.SemanticModel"}},
    })

    # ---- theme: colours come from standards/dashboard-standards.md ----------
    w(rpt / "StaticResources" / "RegisteredResources" / THEME_FILE, {
        "name": "PortfolioTheme",
        # Muted first so grey-by-default holds and colour marks the point.
        "dataColors": ["#64748B", "#2563EB", "#0F766E", "#7C3AED",
                       "#B45309", "#4D7C0F"],
        "good": "#16A34A", "neutral": "#D97706", "bad": "#DC2626",
        "background": "#FFFFFF", "foreground": "#1F2937",
        "tableAccent": "#2563EB",
        "textClasses": {
            "title":   {"fontSize": 13, "fontFace": "Segoe UI Semibold",
                        "color": "#1F2937"},
            "label":   {"fontSize": 10, "fontFace": "Segoe UI",
                        "color": "#4B5563"},
            "callout": {"fontSize": 30, "fontFace": "Segoe UI Light",
                        "color": "#1F2937"},
        },
        # Declutter rules expressed once, per standards/dashboard-standards.md.
        "visualStyles": {
            "*": {"*": {
                "background":   [{"show": False}],
                "border":       [{"show": False}],
                "visualHeader": [{"show": False}],
                "title":        [{"show": True, "fontSize": 12,
                                  "fontColor": {"solid": {"color": "#1F2937"}}}],
            }},
            "columnChart": {"*": {
                "categoryAxis": [{"gridlineShow": False}],
                "valueAxis": [{"gridlineShow": True,
                               "gridlineColor": {"solid": {"color": "#F3F4F6"}}}],
            }},
            "lineChart": {"*": {
                "categoryAxis": [{"gridlineShow": False}],
                "valueAxis": [{"gridlineShow": True,
                               "gridlineColor": {"solid": {"color": "#F3F4F6"}}}],
            }},
        },
    })

    w(defn / "report.json", {
        "$schema": SCH_REPORT,
        "themeCollection": {"customTheme": {
            "name": THEME_FILE,
            "reportVersionAtImport": {"visual": "2.4.0", "page": "2.0.0",
                                      "report": "3.0.0"},
            "type": "RegisteredResources",
        }},
        "resourcePackages": [{
            "name": "RegisteredResources",
            "type": "RegisteredResources",
            "items": [{"name": THEME_FILE, "path": THEME_FILE,
                       "type": "CustomTheme"}],
        }],
    })

    w(defn / "version.json", {"$schema": SCH_VERSION_META, "version": V_VERSION})

    # ---- page 1: Portfolio_Overview ----------------------------------------
    # Z-pattern: the number that matters most is top-left (lowest x and y).
    page = "Portfolio_Overview"
    w(defn / "pages" / page / "page.json", {
        "$schema": SCH_PAGE, "name": page, "displayName": "Portfolio Overview",
        "displayOption": "FitToPage", "height": 720, "width": 1280,
    })
    for n, obj in [
        card("Milestone_Hit_Rate_Card", 16, 16, "Milestone Hit Rate", z=0),
        card("SPI_Card", 332, 16, "SPI", z=100),
        card("CPI_Card", 648, 16, "CPI", z=200),
        card("Projects_Reporting_Card", 964, 16, "Projects Reporting", z=300),
        cartesian("Milestone_Hit_Rate_Trend", "lineChart", 16, 200,
                  "Date", "Month_Label", "Milestone Hit Rate",
                  width=616, height=300, z=400),
        cartesian("Capacity_Demand_By_Program", "columnChart", 648, 200,
                  "Project", "Program", "Capacity Demand FTE",
                  width=616, height=300, z=500),
    ]:
        w(defn / "pages" / page / "visuals" / n / "visual.json", obj)

    # ---- page 2: Delivery_Detail -------------------------------------------
    page2 = "Delivery_Detail"
    w(defn / "pages" / page2 / "page.json", {
        "$schema": SCH_PAGE, "name": page2, "displayName": "Delivery Detail",
        "displayOption": "FitToPage", "height": 720, "width": 1280,
    })
    for n, obj in [
        card("Data_Confidence_Rate_Card", 16, 16, "Data Confidence Rate", z=0),
        cartesian("SPI_By_Project", "columnChart", 16, 200,
                  "Project", "Project_Name", "SPI",
                  width=800, height=320, z=100),
        cartesian("Capacity_Demand_By_Manager", "columnChart", 832, 200,
                  "Project", "Manager", "Capacity Demand FTE",
                  width=432, height=320, z=200),
    ]:
        w(defn / "pages" / page2 / "visuals" / n / "visual.json", obj)

    w(defn / "pages" / "pages.json", {
        "$schema": SCH_PAGES_META,
        "pageOrder": [page, page2],
        "activePageName": page,
    })

    # ---- semantic model ----------------------------------------------------
    w(mdl / "definition.pbism", {"$schema": SCH_PBISM, "version": "4.0",
                                 "settings": {}})

    d = mdl / "definition"
    wt(d / "database.tmdl", f"database {NAME}\n\tcompatibilityLevel: 1567\n")
    wt(d / "model.tmdl",
       "model Model\n\tculture: en-US\n"
       "\tdefaultPowerBIDataSourceVersion: powerBI_V3\n\n"
       "ref table Fact_Status\nref table Project\nref table 'Date'\n")

    # -- Date dimension: contiguous daily calendar for 2026, so that "Mark as
    #    date table" works in Desktop if you want it. Not marked here — see
    #    README; no time-intelligence DAX is used by this sample.
    date_rows = ",\n".join(
        "\t\t\t\t\t\t\t{"
        f"#datetime({dt.year}, {dt.month}, {dt.day}, 0, 0, 0), "
        f'"{dt.year}-{dt.month:02d}"' "}"
        for dt in (date(2026, 1, 1) + timedelta(days=i) for i in range(365)))

    wt(d / "tables" / "Date.tmdl",
       "/// Date dimension. Contiguous daily calendar for 2026.\n"
       "table 'Date'\n"
       "\tlineageTag: 22222222-2222-2222-2222-222222222222\n\n"
       "\tcolumn Date\n\t\tdataType: dateTime\n\t\tisKey\n"
       "\t\tsourceColumn: Date\n\t\tsummarizeBy: none\n"
       "\t\tformatString: yyyy-mm-dd\n\n"
       "\t/// Sortable month label, e.g. 2026-03.\n"
       "\tcolumn Month_Label\n\t\tdataType: string\n"
       "\t\tsourceColumn: Month_Label\n\t\tsummarizeBy: none\n\n"
       # Every row is an explicit literal, computed here in Python rather than
       # by date functions in Power Query. Two reasons, both deliberate:
       #
       #   1. `standards/powerbi-standards.md` says no transformation in Power
       #      Query — compute upstream where it's visible and testable. Python
       #      *is* upstream for this sample.
       #   2. M's date functions are fussy about their input type. Date.ToText
       #      takes a `date`; handing it a `datetime` fails outright with
       #      "We cannot convert the value #datetime(...) to type Date". Doing
       #      the arithmetic here means no M evaluation can surprise us.
       #
       # Verbose, and worth it: this table cannot fail to load.
       "\tpartition 'Date' = m\n\t\tmode: import\n\t\tsource =\n"
       "\t\t\t\tlet\n"
       "\t\t\t\t\tSource = #table(\n"
       "\t\t\t\t\t\ttype table [Date = datetime, Month_Label = text],\n"
       "\t\t\t\t\t\t{\n" + date_rows + "\n"
       "\t\t\t\t\t\t}\n"
       "\t\t\t\t\t)\n"
       "\t\t\t\tin\n\t\t\t\t\tSource\n")

    # -- Project dimension
    proj_rows = ",\n".join(
        "\t\t\t\t\t\t\t{" + ", ".join(f'"{v}"' for v in p) + "}"
        for p in PROJECTS)
    wt(d / "tables" / "Project.tmdl",
       "/// Project dimension. One row per project or program item.\n"
       "table Project\n"
       "\tlineageTag: 11111111-1111-1111-1111-111111111111\n\n"
       "\tcolumn Project_Id\n\t\tdataType: string\n"
       "\t\tsourceColumn: Project_Id\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Project_Name\n\t\tdataType: string\n"
       "\t\tsourceColumn: Project_Name\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Program\n\t\tdataType: string\n"
       "\t\tsourceColumn: Program\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Sponsor\n\t\tdataType: string\n"
       "\t\tsourceColumn: Sponsor\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Manager\n\t\tdataType: string\n"
       "\t\tsourceColumn: Manager\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Stage\n\t\tdataType: string\n"
       "\t\tsourceColumn: Stage\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Approach\n\t\tdataType: string\n"
       "\t\tsourceColumn: Approach\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Strategic_Link\n\t\tdataType: string\n"
       "\t\tsourceColumn: Strategic_Link\n\t\tsummarizeBy: none\n\n"
       "\tpartition Project = m\n\t\tmode: import\n\t\tsource =\n"
       "\t\t\t\tlet\n"
       "\t\t\t\t\tSource = #table(\n"
       "\t\t\t\t\t\ttype table [Project_Id = text, Project_Name = text, "
       "Program = text, Sponsor = text, Manager = text, Stage = text, "
       "Approach = text, Strategic_Link = text],\n"
       "\t\t\t\t\t\t{\n" + proj_rows + "\n"
       "\t\t\t\t\t\t}\n"
       "\t\t\t\t\t)\n"
       "\t\t\t\tin\n\t\t\t\t\tSource\n")

    # -- Fact table. Grain: one row per project per reporting month.
    fact_rows = []
    for pid, series in FACTS.items():
        for (y, m, day), (pv, ev, ac, due, hit, rag, conf, fte) in zip(MONTHS, series):
            fact_rows.append(
                "\t\t\t\t\t\t\t{" + f'"{pid}", #datetime({y}, {m}, {day}, 0, 0, 0), '
                f'{pv}, {ev}, {ac}, {due}, {hit}, "{rag}", "{conf}", {fte}' + "}")
    fact_block = ",\n".join(fact_rows)

    wt(d / "tables" / "Fact_Status.tmdl",
       "/// Portfolio status fact. Grain: one row per project per reporting month.\n"
       "table Fact_Status\n"
       "\tlineageTag: 33333333-3333-3333-3333-333333333333\n\n"
       # Measures. DIVIDE over '/', ratios from summed numerator and
       # denominator — never an average of ratios, which gives a wrong total row.
       "\t/// Share of milestones due in the period that were met.\n"
       "\tmeasure 'Milestone Hit Rate' = DIVIDE(SUM(Fact_Status[Milestones_Hit]), "
       "SUM(Fact_Status[Milestones_Due]))\n"
       "\t\tformatString: 0.0%\n\n"
       "\t/// Schedule Performance Index. Below 1.00 is behind schedule.\n"
       "\tmeasure SPI = DIVIDE(SUM(Fact_Status[Earned_Value]), "
       "SUM(Fact_Status[Planned_Value]))\n"
       "\t\tformatString: 0.00\n\n"
       "\t/// Cost Performance Index. Below 1.00 is over budget.\n"
       "\tmeasure CPI = DIVIDE(SUM(Fact_Status[Earned_Value]), "
       "SUM(Fact_Status[Actual_Cost]))\n"
       "\t\tformatString: 0.00\n\n"
       "\t/// Distinct projects that submitted in the filtered period.\n"
       "\tmeasure 'Projects Reporting' = "
       "DISTINCTCOUNT(Fact_Status[Project_Id])\n"
       "\t\tformatString: 0\n\n"
       "\t/// Total capacity drawn, in full-time equivalents.\n"
       "\tmeasure 'Capacity Demand FTE' = "
       "SUM(Fact_Status[Capacity_Demand_Fte])\n"
       "\t\tformatString: 0.0\n\n"
       "\t/// Share of submissions at High or Medium confidence. The health of\n"
       "\t/// the reporting system itself, not of the work.\n"
       "\tmeasure 'Data Confidence Rate' = "
       "DIVIDE(CALCULATE(COUNTROWS(Fact_Status), "
       "Fact_Status[Confidence] IN {\"High\", \"Medium\"}), "
       "COUNTROWS(Fact_Status))\n"
       "\t\tformatString: 0.0%\n\n"
       # Columns. summarizeBy: none on every numeric column so nobody sums a
       # column two different ways — measures are the only way in.
       "\tcolumn Project_Id\n\t\tdataType: string\n"
       "\t\tsourceColumn: Project_Id\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Report_Month\n\t\tdataType: dateTime\n"
       "\t\tsourceColumn: Report_Month\n\t\tsummarizeBy: none\n"
       "\t\tformatString: yyyy-mm-dd\n\n"
       "\tcolumn Planned_Value\n\t\tdataType: double\n"
       "\t\tsourceColumn: Planned_Value\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Earned_Value\n\t\tdataType: double\n"
       "\t\tsourceColumn: Earned_Value\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Actual_Cost\n\t\tdataType: double\n"
       "\t\tsourceColumn: Actual_Cost\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Milestones_Due\n\t\tdataType: int64\n"
       "\t\tsourceColumn: Milestones_Due\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Milestones_Hit\n\t\tdataType: int64\n"
       "\t\tsourceColumn: Milestones_Hit\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Rag\n\t\tdataType: string\n"
       "\t\tsourceColumn: Rag\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Confidence\n\t\tdataType: string\n"
       "\t\tsourceColumn: Confidence\n\t\tsummarizeBy: none\n\n"
       "\tcolumn Capacity_Demand_Fte\n\t\tdataType: double\n"
       "\t\tsourceColumn: Capacity_Demand_Fte\n\t\tsummarizeBy: none\n\n"
       "\tpartition Fact_Status = m\n\t\tmode: import\n\t\tsource =\n"
       "\t\t\t\tlet\n"
       "\t\t\t\t\tSource = #table(\n"
       "\t\t\t\t\t\ttype table [Project_Id = text, Report_Month = datetime, "
       "Planned_Value = number, Earned_Value = number, Actual_Cost = number, "
       "Milestones_Due = Int64.Type, Milestones_Hit = Int64.Type, Rag = text, "
       "Confidence = text, Capacity_Demand_Fte = number],\n"
       "\t\t\t\t\t\t{\n" + fact_block + "\n"
       "\t\t\t\t\t\t}\n"
       "\t\t\t\t\t)\n"
       "\t\t\t\tin\n\t\t\t\t\tSource\n")

    # Single-direction relationships only. A bidirectional one here would make
    # the filter path ambiguous, and the symptom is a believable wrong number.
    wt(d / "relationships.tmdl",
       "relationship 44444444-4444-4444-4444-444444444444\n"
       "\tfromColumn: Fact_Status.Project_Id\n"
       "\ttoColumn: Project.Project_Id\n\n"
       "relationship 55555555-5555-5555-5555-555555555555\n"
       "\tfromColumn: Fact_Status.Report_Month\n"
       "\ttoColumn: 'Date'.Date\n")

    # Parameters are prefixed: shared expressions and tables share one
    # namespace, and a collision stops the model loading.
    wt(d / "expressions.tmdl",
       "/// Unused by the inline sample data; present to show the convention.\n"
       "expression p_ServerName = \"localhost\" meta "
       "[IsParameterQuery=true, Type=\"Text\", IsParameterQueryRequired=true]\n")

    return dest


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent / NAME
    out = build(target.resolve())
    print(f"built {out}")
