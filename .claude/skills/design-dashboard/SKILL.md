---
name: design-dashboard
description: Specify a portfolio dashboard — the decisions each audience tier must make, the semantic model and grain, a measure catalog with one definition per number, page layout, drill paths, refresh cadence and lineage. Produces a buildable spec, not a built dashboard. Dispatches the portfolio-analyst with comms-lead.
---

# /design-dashboard — Specify the reporting surface

## When to use
When a portfolio reporting surface is needed or is being rebuilt, when two reports disagree about the same
number, or when leadership keeps asking for detail the current surface can't reach.

## Dispatches
`portfolio-analyst` (lead) + `comms-lead` (the leadership tier's narrative and framing).

## Inputs
`knowledge/portfolio.md` (what data actually exists and at what confidence), existing specs in
`knowledge/portfolio/`, `knowledge/product-context.md` (goals to report against),
`knowledge/stakeholder-map.md` (who consumes which tier), `knowledge/integrations.md` (platform and sync
reality).

## Steps
1. **Start from the decisions, not the data.** List what each audience must decide, how often, and what they
   need to see to decide it. Name **one to three questions** the surface answers; more than three means it
   answers none of them well — split it. Every visual later earns its place by serving one.
2. Pick the tier — operational (managers see their own data and gaps), tactical (themes, collisions,
   capacity), or executive (exceptions, decisions, investment vs. strategy). One semantic model, different
   altitudes — never a second dataset for a second audience.
3. Define the **grain** explicitly (what one row means), then model it as a **star schema with exactly one
   date table** honouring the fiscal calendar in `knowledge/cadence.md`. Relationships single-direction unless
   bidirectional is justified in writing — ambiguous filter paths produce believable wrong numbers.
4. Write the **measure catalog** — every measure with a plain-English definition, formula, format and owner.
   Resolve any term with more than one plausible reading ("active", "on track", "complete") to a single
   definition here; this table is the arbiter when surfaces disagree, and the **name is a contract** the
   builder implements character for character.
5. Lay out pages and visuals against the questions from step 1, define the drill paths so every aggregate
   reaches its source rows in one or two steps, and specify the empty state. **Give every page and visual a
   safe name** — letters, digits, underscores, hyphens only. Leave chart formatting to the build target's
   design standard; specify what each visual must show and why, not how it looks.
6. Specify refresh cadence, lineage, access, publishing rights, and failure behaviour — **stale data must
   announce itself**. Show data confidence on the surface, not just values.
7. Work the **privacy** section deliberately. A portfolio surface carries sponsor and manager names, saved
   filter states can persist into the built report's files, and this surface reports the health of work — not
   the performance of people.
8. Fill in `## Handoff`: the build route, the capability tier actually available, what's ready to hand over,
   what the builder owns, and any open question blocking the build. Check
   `knowledge/integrations.md` for the current route before naming one. State plainly that this is a
   specification — the PMO specifies, a build capability implements.

## Methods
`knowledge/methods/portfolio-management.md` (reporting layers, dashboard design principles, KPIs),
`knowledge/methods/metrics-and-experimentation.md` (metric hygiene, vanity measures),
`standards/communication-standards.md` (audience playbook, BLUF, RAG discipline).

## Output
Start from `templates/dashboard-spec.md`. A spec saved to `knowledge/portfolio/dashboard-<surface>.md` — a
living document, updated in place so there is one current definition per surface. Log any measure-definition
decision to `knowledge/decision-log.md`, since it binds every other report. Follow
`standards/document-standards.md`.

The spec is complete when someone could build the surface from it without asking a further question. It is not
"done" when it renders — only when every displayed number reconciles against an independent query and the
empty state has been tested. Track that as an open item until the builder confirms it.

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
