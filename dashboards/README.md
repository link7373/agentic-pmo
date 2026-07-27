# Dashboards

Built dashboard projects. One folder per surface, named in `[A-Za-z0-9_-]` only. Specs live separately in
`knowledge/portfolio/` — a spec is portfolio knowledge and outlives any one implementation.

Power BI surfaces are **PBIP projects**: plain text, tracked in git, built and validated by `/powerbi`. Only
binaries and per-user state are ignored (`.pbix`, `.pbit`, `.pbi/cache.abf`, `.pbi/localSettings.json`).

Projects live here at the repo root rather than under `knowledge/` for a mechanical reason: PBIP nests deeply and
Windows still enforces a 260-character path limit, so every folder level in the prefix is spent on all of them.

## Inventory

| Dashboard | Tier / audience | Spec | Source | Refresh | Owner | Validated | Reviewed |
|-----------|-----------------|------|--------|---------|-------|-----------|----------|
|           |                 |      |        |         |       |           |          |

**Validated** means `validate_pbip.py` clean *and* opened in Desktop *and* every number reconciled — not just
the first of those. **Reviewed** is the retirement check: every quarter, an unused dashboard gets archived rather
than abandoned.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
