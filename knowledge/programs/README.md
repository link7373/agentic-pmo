# Programs

Program-level and governance artifacts. Two producers:

| Artifact | Skill | Owner | Naming | Template |
|----------|-------|-------|--------|----------|
| Program coordination view (dependency map, sequencing, integration plan) | `/coordinate-program` | `program-manager` | `YYYY-MM-DD-<program>-coordination.md` | — |
| Gate review record | `/run-gate-review` | `governance-lead` | `YYYY-MM-DD-<project>-gate-<n>.md` | `templates/gate-review.md` |

Coordination views are the program-manager's decision record: what depends on what, in what order, and what was
traded off. Cross-project risks and dependencies still live in `knowledge/raid-log.md` at `Level = program` —
this directory holds the reasoning, not the register.

Gate outcomes are one of go / go-with-conditions / hold / kill, with conditions carrying an owner and a date.
The gate definitions themselves live in `knowledge/governance.md`.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
