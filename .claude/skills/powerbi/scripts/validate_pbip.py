#!/usr/bin/env python3
"""Validate a Power BI Project (PBIP) before it ever reaches Power BI Desktop.

Catches the failure classes that Desktop either refuses to open or — worse —
accepts while silently dropping your work (see the ^[\\w-]+$ naming rule).

Usage:
    python validate_pbip.py <path> [--json] [--quiet] [--no-warn]

<path> may be a PBIP project root, a *.Report folder, or any folder containing
them; projects are discovered recursively.

Exit codes: 0 = no errors, 1 = at least one ERROR, 2 = bad invocation.

Standard library only (Python 3.9+) — no pip install required.

Checks are grounded in Microsoft's published PBIP/PBIR/TMDL documentation and
JSON schemas:
  https://learn.microsoft.com/power-bi/developer/projects/projects-overview
  https://learn.microsoft.com/power-bi/developer/projects/projects-report
  https://learn.microsoft.com/power-bi/developer/projects/projects-dataset
  https://learn.microsoft.com/analysis-services/tmdl/tmdl-overview
  https://github.com/microsoft/json-schemas/tree/main/fabric

TMDL handling here is a deliberately shallow line-scanner, not a real parser.
It reliably finds object declarations at known indent levels; it does not
evaluate DAX or M. Findings it cannot prove are reported as WARN, never ERROR.

Part of the Agentic BI Team. Created by Colin Beck.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Microsoft: object and file/folder names "must consist of one or more word
# characters (letters, digits, underscores) or hyphens". Violations are not an
# error in Desktop — it silently ignores the object and treats it as a private
# user file, so the page or visual just vanishes. That is why this is an ERROR.
NAME_RE = re.compile(r"^[\w-]+$")

# version.json: major.minor.patch, major >= 1, patch always 0.
PBIR_VERSION_RE = re.compile(r"^[1-9][0-9]*\.(0|[1-9][0-9]*)\.0$")

UTF8_BOM = b"\xef\xbb\xbf"

# Every file Power BI Desktop reads as text. It rejects a BOM in *any* of them,
# including files git ignores (.pbi/localSettings.json is the classic — Desktop
# reads it, git doesn't track it, so a BOM there is invisible until the project
# refuses to open). Binary siblings like .abf are excluded deliberately.
TEXT_SUFFIXES = {".json", ".tmdl", ".pbir", ".pbip", ".pbism", ".bim", ".dax"}
TEXT_NAMES = {".platform"}

# definition/report.json is additionalProperties:false. Allowed set per the
# report/3.0.0 schema; widen if a later schema version adds properties.
REPORT_TOP_LEVEL = {
    "$schema", "themeCollection", "filterConfig", "objects", "reportSource",
    "publicCustomVisuals", "organizationCustomVisuals", "resourcePackages",
    "annotations", "dataSourceVariables", "settings", "slowDataSourceSettings",
}

# Windows MAX_PATH. PBIP nests deeply, so long table names blow this.
MAX_PATH_WINDOWS = 260

ERROR, WARN, INFO = "ERROR", "WARN", "INFO"
_RANK = {ERROR: 0, WARN: 1, INFO: 2}


@dataclass
class Finding:
    code: str
    severity: str
    path: str
    message: str
    hint: str = ""


@dataclass
class Report:
    findings: list[Finding] = field(default_factory=list)
    bom_reported: set = field(default_factory=set)

    def add(self, code, severity, path, message, hint=""):
        self.findings.append(Finding(code, severity, str(path), message, hint))

    def note_bom(self, path):
        """Report a BOM once per file, wherever it's first noticed."""
        key = str(Path(path).resolve())
        if key in self.bom_reported:
            return
        self.bom_reported.add(key)
        self.add("ENC001", ERROR, path,
                 "File starts with a UTF-8 BOM.",
                 "Power BI Desktop refuses to open the project: 'Only text with "
                 "UTF8 encoding without BOM is supported'. On Windows, "
                 "PowerShell's Set-Content/Out-File add one by default — write "
                 "with Python's encoding='utf-8' or -Encoding utf8NoBOM.")

    @property
    def errors(self):
        return [f for f in self.findings if f.severity == ERROR]

    @property
    def warnings(self):
        return [f for f in self.findings if f.severity == WARN]


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def read_text(path: Path) -> tuple[str | None, bool]:
    """Return (text, had_bom). text is None if the file can't be decoded."""
    try:
        raw = path.read_bytes()
    except OSError:
        return None, False
    had_bom = raw.startswith(UTF8_BOM)
    if had_bom:
        raw = raw[len(UTF8_BOM):]
    try:
        return raw.decode("utf-8"), had_bom
    except UnicodeDecodeError:
        return None, had_bom


def load_json(path: Path, rep: Report, code_prefix: str):
    """Parse JSON, recording BOM/syntax problems. Returns dict/list or None."""
    text, had_bom = read_text(path)
    if text is None:
        rep.add(f"{code_prefix}-ENC", ERROR, path,
                "File is not valid UTF-8.",
                "PBIP files must be saved as UTF-8 without BOM.")
        return None
    if had_bom:
        rep.note_bom(path)
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        rep.add(f"{code_prefix}-JSON", ERROR, path,
                f"Invalid JSON: {exc.msg} (line {exc.lineno}, col {exc.colno}).",
                "PBIR JSON does not permit comments or trailing commas.")
        return None


def require_keys(obj, keys, path, rep, code):
    missing = [k for k in keys if k not in obj]
    if missing:
        rep.add(code, ERROR, path,
                f"Missing required propert{'y' if len(missing) == 1 else 'ies'}: "
                f"{', '.join(missing)}.",
                "Required by the file's published JSON schema; Desktop treats "
                "this as a blocking error.")
    return not missing


def check_path_length(path: Path, rep: Report):
    if len(str(path.resolve())) > MAX_PATH_WINDOWS:
        rep.add("ENC002", WARN, path,
                f"Absolute path is {len(str(path.resolve()))} characters "
                f"(Windows default limit is {MAX_PATH_WINDOWS}).",
                "Shorten the repo root or the object name, or enable Windows "
                "long-path support.")


def walk_json(node):
    """Yield every dict nested anywhere inside node."""
    if isinstance(node, dict):
        yield node
        for v in node.values():
            yield from walk_json(v)
    elif isinstance(node, list):
        for v in node:
            yield from walk_json(v)


def scan_encoding(root: Path, rep: Report):
    """Sweep every text file in the project for a BOM.

    Deliberately walks the whole tree — including .pbi/, which git ignores but
    Desktop reads. A BOM anywhere in here is a hard open failure, and the
    happy-path checks alone never touch those files.
    """
    for f in root.rglob("*"):
        if not f.is_file():
            continue
        if f.suffix.lower() not in TEXT_SUFFIXES and f.name not in TEXT_NAMES:
            continue
        try:
            with f.open("rb") as fh:
                if fh.read(3) == UTF8_BOM:
                    rep.note_bom(f)
        except OSError:
            continue


# --------------------------------------------------------------------------
# discovery
# --------------------------------------------------------------------------

def find_report_folders(root: Path) -> list[Path]:
    if root.name.endswith(".Report") and (root / "definition.pbir").exists():
        return [root]
    return sorted(
        p for p in root.rglob("*.Report")
        if p.is_dir() and (p / "definition.pbir").exists()
    )


def find_model_folders(root: Path) -> list[Path]:
    if root.name.endswith(".SemanticModel"):
        return [root]
    return sorted(p for p in root.rglob("*.SemanticModel") if p.is_dir())


# --------------------------------------------------------------------------
# PBIP root
# --------------------------------------------------------------------------

def validate_pbip_root(root: Path, rep: Report):
    for pbip in sorted(root.rglob("*.pbip")):
        data = load_json(pbip, rep, "PBIP001")
        if data is None:
            continue
        artifacts = data.get("artifacts")
        if not artifacts:
            rep.add("PBIP001", WARN, pbip,
                    "No 'artifacts' entry — the .pbip file points at nothing.",
                    "The .pbip is a shortcut to a report folder. It is optional; "
                    "you can open definition.pbir directly instead.")
            continue
        for art in artifacts:
            target = art.get("report", {}).get("path")
            if target and not (pbip.parent / target).exists():
                rep.add("PBIP002", ERROR, pbip,
                        f"Points to report folder '{target}', which does not exist.",
                        "Fix the path or delete the stale .pbip.")


# --------------------------------------------------------------------------
# report folder
# --------------------------------------------------------------------------

def validate_report(report_dir: Path, rep: Report) -> dict:
    """Validate one *.Report folder. Returns {'model_path', 'field_refs'}."""
    result = {"model_path": None, "field_refs": []}
    check_path_length(report_dir, rep)

    # ---- .platform ------------------------------------------------------
    # Fabric Git-integration file. Absent is fine for a purely local project,
    # so this is a WARN. Never generate one: its contents (logicalId) are
    # assigned by Fabric, and a hand-made file corrupts the Git link.
    if not (report_dir / ".platform").exists():
        rep.add("PBIP005", WARN, report_dir,
                "No .platform file.",
                "Fine for a local-only project. Required for Fabric Git "
                "integration — let Fabric or Desktop create it; never hand-write it.")

    # ---- definition.pbir ------------------------------------------------
    pbir = report_dir / "definition.pbir"
    if not pbir.exists():
        rep.add("PBIP003", ERROR, report_dir,
                "Missing definition.pbir.",
                "This file is required in every report folder.")
        return result

    pbir_data = load_json(pbir, rep, "PBIP003")
    definition_dir = report_dir / "definition"
    legacy_report = report_dir / "report.json"

    if pbir_data is not None:
        version = str(pbir_data.get("version", ""))
        ref = pbir_data.get("datasetReference")
        if ref is None:
            rep.add("PBIP004", ERROR, pbir,
                    "Missing 'datasetReference'.",
                    "Must reference a semantic model byPath or byConnection.")
        else:
            by_path, by_conn = ref.get("byPath"), ref.get("byConnection")
            if by_path and by_conn:
                rep.add("PBIP004", ERROR, pbir,
                        "Both 'byPath' and 'byConnection' are set.",
                        "Use exactly one.")
            elif not by_path and not by_conn:
                rep.add("PBIP004", ERROR, pbir,
                        "'datasetReference' has neither 'byPath' nor 'byConnection'.")
            elif by_path:
                rel = by_path.get("path", "")
                if rel.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:", rel):
                    rep.add("PBIP006", ERROR, pbir,
                            f"byPath '{rel}' is absolute.",
                            "Only relative paths are supported; use forward slashes.")
                target = (report_dir / rel).resolve()
                if not target.exists():
                    rep.add("PBIP006", ERROR, pbir,
                            f"byPath target '{rel}' does not exist.",
                            "Fix the relative path to the .SemanticModel folder.")
                else:
                    result["model_path"] = target
            # byConnection: nothing local to resolve. A thin report with no
            # sibling .SemanticModel is perfectly valid, not an error.

        if definition_dir.is_dir():
            try:
                if float(".".join(version.split(".")[:2])) < 4.0:
                    rep.add("PBIP007", ERROR, pbir,
                            f"version '{version}' with a definition/ folder present.",
                            "PBIR (definition/ folder) requires version 4.0 or higher.")
            except ValueError:
                rep.add("PBIP007", WARN, pbir, f"Unreadable version '{version}'.")

    # ---- PBIR vs PBIR-Legacy -------------------------------------------
    if definition_dir.is_dir() and legacy_report.exists():
        rep.add("PBIR012", ERROR, report_dir,
                "Both definition/ (PBIR) and report.json (PBIR-Legacy) are present.",
                "These formats are mutually exclusive. Keep definition/ and "
                "delete the root report.json.")
    if not definition_dir.is_dir():
        if legacy_report.exists():
            rep.add("PBIR000", INFO, report_dir,
                    "Report uses PBIR-Legacy (report.json); structural checks skipped.",
                    "Legacy report.json is undocumented and unsupported for "
                    "external editing. Convert to PBIR to make it agent-editable.")
        else:
            rep.add("PBIR000", ERROR, report_dir,
                    "Neither definition/ nor report.json found.",
                    "The report has no definition.")
        return result

    validate_pbir_definition(definition_dir, rep, result)
    validate_theme_resources(report_dir, definition_dir, rep)
    return result


def validate_pbir_definition(definition_dir: Path, rep: Report, result: dict):
    # ---- version.json ---------------------------------------------------
    version_file = definition_dir / "version.json"
    if not version_file.exists():
        rep.add("PBIR001", ERROR, definition_dir,
                "Missing definition/version.json.", "Required by PBIR.")
    else:
        data = load_json(version_file, rep, "PBIR001")
        if isinstance(data, dict):
            require_keys(data, ["$schema", "version"], version_file, rep, "PBIR001")
            v = data.get("version")
            if isinstance(v, str) and not PBIR_VERSION_RE.match(v):
                rep.add("PBIR001", ERROR, version_file,
                        f"version '{v}' does not match major.minor.patch "
                        f"with patch = 0.",
                        "Example: 2.0.0")
            elif isinstance(v, str) and v.split(".")[0] == "1":
                # Observed directly: version 1.0.0 with a normal PBIR layout
                # makes Desktop load the model, render no pages, and report
                # nothing at all. WARN rather than ERROR because an genuinely
                # old report may legitimately sit at 1.x.
                rep.add("PBIR014", WARN, version_file,
                        f"version is '{v}'. Desktop uses this to decide which "
                        f"files to load.",
                        "If pages don't appear but the model loads fine, this "
                        "is the cause — a blank report with no error. Newly "
                        "authored PBIR should use 2.0.0.")

    # ---- report.json (PBIR) --------------------------------------------
    report_json = definition_dir / "report.json"
    if not report_json.exists():
        rep.add("PBIR002", ERROR, definition_dir,
                "Missing definition/report.json.", "Required by PBIR.")
    else:
        data = load_json(report_json, rep, "PBIR002")
        if isinstance(data, dict):
            if "$schema" not in data:
                rep.add("PBIR002", ERROR, report_json, "Missing '$schema'.")
            # report.json is additionalProperties:false — anything outside this
            # set is rejected. WARN, not ERROR: the set grows with the schema
            # version, and Desktop treats it as non-blocking.
            unknown = sorted(set(data) - REPORT_TOP_LEVEL)
            for key in unknown:
                rep.add("PBIR015", WARN, report_json,
                        f"Unexpected top-level property '{key}'.",
                        "report.json rejects additional properties. Desktop "
                        "reports this on open and ignores the value. Remove it, "
                        "or confirm it against the schema version in $schema.")

    # ---- pages ----------------------------------------------------------
    pages_dir = definition_dir / "pages"
    if not pages_dir.is_dir():
        rep.add("PBIR003", ERROR, definition_dir,
                "Missing definition/pages/ folder.", "Required by PBIR.")
        return

    page_folders = sorted(p for p in pages_dir.iterdir() if p.is_dir())
    if not page_folders:
        rep.add("PBIR003", ERROR, pages_dir, "No page folders found.",
                "A report needs at least one page.")

    seen_page_names: dict[str, Path] = {}
    for page_dir in page_folders:
        validate_page(page_dir, rep, seen_page_names, result)

    # ---- pages.json (optional) -----------------------------------------
    pages_json = pages_dir / "pages.json"
    if pages_json.exists():
        data = load_json(pages_json, rep, "PBIR010")
        if isinstance(data, dict):
            order = data.get("pageOrder") or []
            folder_names = {p.name for p in page_folders}
            for name in order:
                if name not in folder_names:
                    rep.add("PBIR010", ERROR, pages_json,
                            f"pageOrder lists '{name}', but no such page folder exists.",
                            "Remove the entry or restore the folder.")
            for name in sorted(folder_names - set(order)):
                rep.add("PBIR010", WARN, pages_dir / name,
                        f"Page folder '{name}' is not listed in pages.json pageOrder.",
                        "It will still load, but page order is undefined.")
            active = data.get("activePageName")
            if active and active not in folder_names:
                rep.add("PBIR011", WARN, pages_json,
                        f"activePageName '{active}' does not match any page folder.",
                        "Desktop treats this as a non-blocking error and "
                        "auto-fixes it on save.")

    # ---- bookmarks (optional) ------------------------------------------
    bookmarks_dir = definition_dir / "bookmarks"
    if bookmarks_dir.is_dir():
        for bm in sorted(bookmarks_dir.glob("*.bookmark.json")):
            stem = bm.name[: -len(".bookmark.json")]
            if not NAME_RE.match(stem):
                rep.add("PBIR006", ERROR, bm,
                        f"Bookmark name '{stem}' contains characters outside "
                        f"[A-Za-z0-9_-].",
                        "Desktop silently ignores it — the bookmark disappears.")
            load_json(bm, rep, "PBIR006")


def validate_page(page_dir: Path, rep: Report, seen: dict, result: dict):
    check_path_length(page_dir, rep)

    if not NAME_RE.match(page_dir.name):
        rep.add("PBIR006", ERROR, page_dir,
                f"Page folder name '{page_dir.name}' contains characters "
                f"outside [A-Za-z0-9_-] (spaces are the usual culprit).",
                "Desktop silently ignores the folder and the page vanishes "
                "from the report. Rename it, then restart Desktop.")

    page_json = page_dir / "page.json"
    if not page_json.exists():
        rep.add("PBIR004", ERROR, page_dir, "Missing page.json.",
                "Required in every page folder.")
        return

    data = load_json(page_json, rep, "PBIR004")
    if not isinstance(data, dict):
        return

    require_keys(data, ["$schema", "name", "displayName", "displayOption"],
                 page_json, rep, "PBIR004")

    name = data.get("name")
    if isinstance(name, str):
        if not NAME_RE.match(name):
            rep.add("PBIR007", ERROR, page_json,
                    f"Page 'name' property '{name}' contains characters "
                    f"outside [A-Za-z0-9_-].")
        if name != page_dir.name:
            rep.add("PBIR008", WARN, page_json,
                    f"'name' is '{name}' but the folder is '{page_dir.name}'.",
                    "Desktop tolerates the mismatch, but bookmarks and "
                    "drillthrough reference the name — keep them identical.")
        if name in seen:
            rep.add("PBIR009", ERROR, page_json,
                    f"Duplicate page name '{name}' (also in {seen[name].name}).",
                    "Page names must be unique across the report.")
        else:
            seen[name] = page_dir

    visuals_dir = page_dir / "visuals"
    if not visuals_dir.is_dir():
        return

    seen_visuals: dict[str, Path] = {}
    for visual_dir in sorted(p for p in visuals_dir.iterdir() if p.is_dir()):
        validate_visual(visual_dir, rep, seen_visuals, result)


def validate_visual(visual_dir: Path, rep: Report, seen: dict, result: dict):
    check_path_length(visual_dir, rep)

    if not NAME_RE.match(visual_dir.name):
        rep.add("PBIR006", ERROR, visual_dir,
                f"Visual folder name '{visual_dir.name}' contains characters "
                f"outside [A-Za-z0-9_-].",
                "Desktop silently ignores the folder and the visual vanishes.")

    visual_json = visual_dir / "visual.json"
    if not visual_json.exists():
        rep.add("PBIR005", ERROR, visual_dir, "Missing visual.json.",
                "Required in every visual folder.")
        return

    data = load_json(visual_json, rep, "PBIR005")
    if not isinstance(data, dict):
        return

    require_keys(data, ["$schema", "name", "position"], visual_json, rep, "PBIR005")

    name = data.get("name")
    if isinstance(name, str):
        if not NAME_RE.match(name):
            rep.add("PBIR007", ERROR, visual_json,
                    f"Visual 'name' property '{name}' contains characters "
                    f"outside [A-Za-z0-9_-].")
        if len(name) > 50:
            rep.add("PBIR013", ERROR, visual_json,
                    f"Visual 'name' is {len(name)} characters; the schema "
                    f"maximum is 50.")
        if name in seen:
            rep.add("PBIR009", ERROR, visual_json,
                    f"Duplicate visual name '{name}' on this page "
                    f"(also in {seen[name].name}).",
                    "Visual names must be unique within a page.")
        else:
            seen[name] = visual_dir

    has_visual, has_group = "visual" in data, "visualGroup" in data
    if has_visual and has_group:
        rep.add("PBIR005", ERROR, visual_json,
                "Has both 'visual' and 'visualGroup'.",
                "The schema permits exactly one.")
    elif not has_visual and not has_group:
        rep.add("PBIR005", ERROR, visual_json,
                "Has neither 'visual' nor 'visualGroup'.",
                "The schema requires exactly one.")

    result["field_refs"].extend(collect_field_refs(data, visual_json))


def collect_field_refs(node, source: Path) -> list[tuple[str, str, Path]]:
    """Best-effort extraction of (table, field) pairs bound by a visual.

    PBIR expresses bindings as {"Expression": {"SourceRef": {"Entity": ...}},
    "Property": ...}. We also read "queryRef" strings ("Table.Field") because
    they survive in places the structured form does not.
    """
    refs: list[tuple[str, str, Path]] = []
    for d in walk_json(node):
        expr, prop = d.get("Expression"), d.get("Property")
        if isinstance(expr, dict) and isinstance(prop, str):
            entity = expr.get("SourceRef", {}).get("Entity")
            if isinstance(entity, str):
                refs.append((entity, prop, source))
        qref = d.get("queryRef")
        if isinstance(qref, str) and qref.count(".") == 1:
            table, _, fieldname = qref.partition(".")
            if table and fieldname:
                refs.append((table, fieldname, source))
    return refs


def validate_theme_resources(report_dir: Path, definition_dir: Path, rep: Report):
    report_json = definition_dir / "report.json"
    if not report_json.exists():
        return
    text, _ = read_text(report_json)
    if text is None:
        return
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return

    static_root = report_dir / "StaticResources"

    # resourcePackages maps a resource NAME to a PATH. The path resolves under
    # the *package's* type (RegisteredResources / SharedResources), not the
    # item's type (CustomTheme / BaseTheme) — an easy and silent mix-up.
    declared: dict[str, set[str]] = {}
    resolved_files: set[Path] = set()
    for pkg in data.get("resourcePackages") or []:
        if not isinstance(pkg, dict):
            continue
        pkg_type = pkg.get("type")
        if not isinstance(pkg_type, str):
            continue
        for item in pkg.get("items") or []:
            if not isinstance(item, dict):
                continue
            item_path, item_name = item.get("path"), item.get("name")
            if isinstance(item_name, str):
                declared.setdefault(pkg_type, set()).add(item_name)
            if not isinstance(item_path, str):
                continue
            candidate = static_root / pkg_type / item_path
            resolved_files.add(candidate.resolve())
            if not candidate.exists():
                rep.add("THEME001", ERROR, report_json,
                        f"Resource '{item_path}' in package '{pkg_type}' not "
                        f"found at StaticResources/{pkg_type}/{item_path}.",
                        "Every item in resourcePackages must exist on disk or "
                        "the resource silently fails to load.")

    # themeCollection selects a theme by NAME; that name must be declared in
    # the matching package. Built-in themes carry no package — skip those.
    themes = data.get("themeCollection")
    if isinstance(themes, dict):
        for slot, theme in themes.items():
            if not isinstance(theme, dict):
                continue
            missing = [k for k in ("name", "reportVersionAtImport", "type")
                       if k not in theme]
            if missing:
                rep.add("THEME003", ERROR, report_json,
                        f"themeCollection/{slot} is missing required "
                        f"propert{'y' if len(missing) == 1 else 'ies'}: "
                        f"{', '.join(missing)}.",
                        "Required shape is {name, reportVersionAtImport: "
                        "{visual, page, report}, type}. Note there is no "
                        "'path' property here — the path lives in "
                        "resourcePackages.")
            if "path" in theme:
                rep.add("THEME003", ERROR, report_json,
                        f"themeCollection/{slot} has an unexpected 'path' "
                        f"property.",
                        "Themes are located via resourcePackages, not via a "
                        "path here. Desktop rejects the extra property.")
            name, ttype = theme.get("name"), theme.get("type")
            if (isinstance(name, str) and isinstance(ttype, str)
                    and ttype in declared and name not in declared[ttype]):
                rep.add("THEME004", ERROR, report_json,
                        f"themeCollection/{slot} references '{name}', which is "
                        f"not declared in the '{ttype}' resource package.",
                        "Add a matching item to resourcePackages, or the theme "
                        "silently does not apply.")

    reg = static_root / "RegisteredResources"
    if reg.is_dir():
        for f in sorted(reg.rglob("*")):
            if f.is_file() and f.resolve() not in resolved_files:
                rep.add("THEME002", INFO, f,
                        "File in RegisteredResources is not listed in "
                        "resourcePackages.",
                        "Desktop only loads registered resources; this file is inert.")


# --------------------------------------------------------------------------
# semantic model
# --------------------------------------------------------------------------

def strip_tmdl_name(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("'"):
        end = raw.find("'", 1)
        while end != -1 and end + 1 < len(raw) and raw[end + 1] == "'":
            end = raw.find("'", end + 2)
        if end != -1:
            return raw[1:end].replace("''", "'")
    return raw.split()[0] if raw.split() else raw


def scan_tmdl_declarations(path: Path, keyword: str) -> list[str]:
    """Find `<keyword> <name>` declarations. Shallow by design — see module docstring."""
    text, _ = read_text(path)
    if text is None:
        return []
    names = []
    pattern = re.compile(rf"^(\s*)(?:ref\s+)?{keyword}\s+(.+?)\s*(?:=.*)?$")
    for line in text.splitlines():
        if not line.strip() or line.strip().startswith("///"):
            continue
        m = pattern.match(line)
        if m:
            names.append(strip_tmdl_name(m.group(2)))
    return names


def validate_semantic_model(model_dir: Path, rep: Report) -> dict:
    """Returns {'tables': {name: {fields}}} for cross-referencing."""
    known: dict[str, set[str]] = {}
    check_path_length(model_dir, rep)

    if not (model_dir / "definition.pbism").exists():
        rep.add("SM001", ERROR, model_dir, "Missing definition.pbism.",
                "Required in every .SemanticModel folder.")
    else:
        load_json(model_dir / "definition.pbism", rep, "SM001")

    if not (model_dir / ".platform").exists():
        rep.add("PBIP005", WARN, model_dir,
                "No .platform file.",
                "Fine locally; required for Fabric Git integration. Never hand-write it.")

    tmdl_dir = model_dir / "definition"
    tmsl_file = model_dir / "model.bim"

    if tmdl_dir.is_dir() and tmsl_file.exists():
        rep.add("SM002", ERROR, model_dir,
                "Both definition/ (TMDL) and model.bim (TMSL) are present.",
                "These formats are mutually exclusive — the model will not load. "
                "Keep one.")
    if not tmdl_dir.is_dir() and not tmsl_file.exists():
        rep.add("SM002", ERROR, model_dir,
                "Neither definition/ (TMDL) nor model.bim (TMSL) found.",
                "The model has no definition.")
        return {"tables": known}
    if not tmdl_dir.is_dir():
        rep.add("SM000", INFO, model_dir,
                "Model uses TMSL (model.bim); TMDL checks skipped.",
                "TMDL is far friendlier to diffs and agent edits — consider converting.")
        return {"tables": known}

    model_tmdl = tmdl_dir / "model.tmdl"
    if not model_tmdl.exists():
        rep.add("SM003", ERROR, tmdl_dir, "Missing definition/model.tmdl.",
                "Required in a TMDL folder.")

    # ---- tables ---------------------------------------------------------
    tables_dir = tmdl_dir / "tables"
    table_files: dict[str, Path] = {}
    if tables_dir.is_dir():
        for f in sorted(tables_dir.glob("*.tmdl")):
            for t in scan_tmdl_declarations(f, "table"):
                if t in table_files:
                    rep.add("SM007", ERROR, f,
                            f"Table '{t}' is also declared in "
                            f"{table_files[t].name}.",
                            "TMDL allows partial declarations, but the same "
                            "property cannot be declared twice.")
                else:
                    table_files[t] = f
                known.setdefault(t, set())

        for f in sorted(tables_dir.glob("*.tmdl")):
            tables_here = scan_tmdl_declarations(f, "table")
            current = tables_here[0] if tables_here else None
            if current is None:
                continue
            for kind in ("column", "measure", "hierarchy"):
                for obj in scan_tmdl_declarations(f, kind):
                    known.setdefault(current, set()).add(obj)
            # duplicate measures inside one file => parse error
            measures = scan_tmdl_declarations(f, "measure")
            dupes = {m for m in measures if measures.count(m) > 1}
            for d in sorted(dupes):
                rep.add("SM007", ERROR, f,
                        f"Measure '{d}' is declared more than once.",
                        "TMDL raises a parsing error on duplicate declarations.")

    # ---- expression / table name collision ------------------------------
    expressions_file = tmdl_dir / "expressions.tmdl"
    if expressions_file.exists():
        for expr in scan_tmdl_declarations(expressions_file, "expression"):
            if expr in table_files:
                rep.add("SM005", ERROR, expressions_file,
                        f"Shared expression '{expr}' collides with the table of "
                        f"the same name in {table_files[expr].name}.",
                        "Tables and shared M expressions share one namespace; "
                        "the model will not load. Rename one.")

    # ---- ref integrity in model.tmdl ------------------------------------
    if model_tmdl.exists():
        for ref in scan_tmdl_declarations(model_tmdl, "table"):
            if ref not in table_files:
                rep.add("SM006", WARN, model_tmdl,
                        f"model.tmdl references table '{ref}' but "
                        f"tables/{ref}.tmdl does not declare it.",
                        "TMDL ignores refs whose file is missing, so the table "
                        "silently drops out of the model.")

    # ---- relationships --------------------------------------------------
    rel_file = tmdl_dir / "relationships.tmdl"
    if rel_file.exists():
        text, _ = read_text(rel_file)
        if text:
            for m in re.finditer(r"^\s*(fromColumn|toColumn):\s*(.+?)\s*$",
                                 text, re.MULTILINE):
                target = m.group(2)
                if "." not in target:
                    continue
                table_part = strip_tmdl_name(target.split(".", 1)[0])
                if table_files and table_part not in table_files:
                    rep.add("SM008", ERROR, rel_file,
                            f"Relationship {m.group(1)} references table "
                            f"'{table_part}', which is not defined.",
                            "Every relationship endpoint must resolve to a table.")

    # ---- indentation ----------------------------------------------------
    for f in sorted(tmdl_dir.rglob("*.tmdl")):
        text, had_bom = read_text(f)
        if had_bom:
            rep.note_bom(f)
        if not text:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            if line.startswith(" ") and not line.strip().startswith("///"):
                rep.add("SM004", WARN, f,
                        f"Line {i} is indented with spaces.",
                        "TMDL's default indentation is a single tab per level. "
                        "Mixed indentation is a common cause of parse errors.")
                break

    return {"tables": known}


# --------------------------------------------------------------------------
# cross-reference
# --------------------------------------------------------------------------

def cross_reference(field_refs, model_info, rep: Report):
    tables = model_info.get("tables") or {}
    if not tables:
        return
    reported = set()
    for table, fieldname, source in field_refs:
        key = (table, fieldname)
        if key in reported:
            continue
        if table not in tables:
            reported.add(key)
            rep.add("XREF001", ERROR, source,
                    f"Visual binds to table '{table}', which is not in the model.",
                    "Rename the binding or add the table. Desktop shows a "
                    "broken-field error for this.")
        elif tables[table] and fieldname not in tables[table]:
            reported.add(key)
            rep.add("XREF002", WARN, source,
                    f"Visual binds to '{table}'[{fieldname}], which was not "
                    f"found in the model.",
                    "May be a calculated/implicit field this shallow scanner "
                    "cannot see — verify in Desktop before changing anything.")


# --------------------------------------------------------------------------
# output
# --------------------------------------------------------------------------

def emit_text(rep: Report, root: Path, quiet: bool, show_warn: bool) -> None:
    shown = [f for f in rep.findings
             if f.severity == ERROR or (show_warn and f.severity != INFO)
             or (not quiet and f.severity == INFO)]
    if not shown:
        print(f"PBIP validation passed — no issues found in {root}")
        return

    by_file: dict[str, list[Finding]] = {}
    for f in shown:
        by_file.setdefault(f.path, []).append(f)

    for path in sorted(by_file):
        try:
            display = Path(path).relative_to(root)
        except ValueError:
            display = Path(path)
        print(f"\n{display}")
        for f in sorted(by_file[path], key=lambda x: _RANK[x.severity]):
            print(f"  [{f.severity:<5}] {f.code}: {f.message}")
            if f.hint and not quiet:
                print(f"          -> {f.hint}")

    n_err, n_warn = len(rep.errors), len(rep.warnings)
    print(f"\n{'-' * 60}")
    print(f"{n_err} error(s), {n_warn} warning(s).")
    if n_err:
        print("Errors will prevent Power BI Desktop from opening the project, "
              "or cause objects to be silently dropped.")


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a Power BI Project (PBIP) before opening it in Desktop.")
    parser.add_argument("path", help="PBIP project root, *.Report folder, or parent folder")
    parser.add_argument("--json", action="store_true", dest="as_json",
                        help="emit findings as JSON")
    parser.add_argument("--quiet", action="store_true", help="suppress hints and INFO")
    parser.add_argument("--no-warn", action="store_true", help="report errors only")
    args = parser.parse_args(argv)

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"error: path not found: {root}", file=sys.stderr)
        return 2

    rep = Report()
    scan_encoding(root, rep)
    validate_pbip_root(root, rep)

    report_dirs = find_report_folders(root)
    model_dirs = find_model_folders(root)

    if not report_dirs and not model_dirs:
        print(f"error: no *.Report or *.SemanticModel folder found under {root}",
              file=sys.stderr)
        return 2

    models: dict[Path, dict] = {}
    for model_dir in model_dirs:
        models[model_dir.resolve()] = validate_semantic_model(model_dir, rep)

    for report_dir in report_dirs:
        result = validate_report(report_dir, rep)
        model_path = result["model_path"]
        if model_path and model_path.resolve() in models:
            cross_reference(result["field_refs"],
                            models[model_path.resolve()], rep)

    if args.as_json:
        print(json.dumps(
            {"root": str(root),
             "errors": len(rep.errors),
             "warnings": len(rep.warnings),
             "findings": [f.__dict__ for f in rep.findings]},
            indent=2))
    else:
        emit_text(rep, root, args.quiet, not args.no_warn)

    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
