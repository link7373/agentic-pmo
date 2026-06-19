# Method: Requirements & User Stories

Requirements communicate intent — what to build and why — so a team can build the right thing. Good
requirements describe the **problem and desired outcome**, leaving room for the team to find the best
solution. They are living artifacts, refined continuously, not frozen specs thrown over a wall.

## What a requirement really is

A requirement is a **placeholder for a conversation** about a customer need, not an exhaustive contract.
Capture enough to align and decide; defer detail until just before it's needed (last responsible moment).

## PRD (Product Requirements Document) anatomy

A lightweight PRD for a feature/initiative typically covers:
1. **Problem & context** — the customer need, opportunity, and why now (link to discovery evidence).
2. **Goals & success metrics** — the outcomes this should move; how we'll measure success.
3. **Target users / personas** — who this is for; the jobs to be done.
4. **Scope** — what's in and explicitly what's out (this release).
5. **Requirements / user stories** — the capabilities, with acceptance criteria.
6. **UX** — flows, key states, edge cases (link to designs).
7. **Dependencies, risks, assumptions** — and open questions.
8. **Rollout & measurement plan** — release strategy, instrumentation, success thresholds.

Keep it as short as it can be while still aligning the team. Favor clarity over completeness.

## User stories

Express needs from the user's perspective:
> As a **[type of user]**, I want **[capability]**, so that **[benefit/outcome]**.

The story is the reminder; the real value is in the conversation and the confirmation (acceptance criteria).
Stories should describe value to a user — avoid technical-task-only stories on the product backlog.

## INVEST (qualities of a good story)
- **Independent** — minimally coupled; can be built/ordered on its own.
- **Negotiable** — a basis for conversation, not a rigid contract.
- **Valuable** — delivers value to a user or customer.
- **Estimable** — the team can size it.
- **Small** — fits comfortably within a sprint; split if not.
- **Testable** — clear, verifiable acceptance criteria.

## Acceptance criteria

Define "done" for the story in verifiable terms. Two common styles:
- **Rule/checklist:** bullet list of conditions that must hold.
- **Scenario (Given/When/Then):**
  > **Given** [context], **When** [action], **Then** [expected outcome].

Cover the happy path, key edge cases, and error states. Criteria are the basis of testing and the
definition of done for the item.

## Epics, features, stories, tasks
- **Epic** — a large body of work spanning many stories / multiple sprints; often a theme on the roadmap.
- **Feature / capability** — a coherent chunk of user-facing value within an epic.
- **Story** — a small, valuable, sprint-sized slice.
- **Task** — implementation sub-step of a story (team-internal).

## Story splitting patterns (when a story is too big)
- By workflow steps · by business-rule variations · by happy path vs. edge cases · by data types/inputs ·
  by operations (create/read/update/delete) · by simple-then-enhance · by deferring performance.
  Each split should still deliver a thin slice of end-to-end value.

## Definition of Ready (DoR) vs. Definition of Done (DoD)
- **DoR** — what a backlog item needs before it's pulled into a sprint (clear, valuable, estimated,
  acceptance criteria, dependencies known). See `agile-scrum-mechanics.md`.
- **DoD** — the quality bar every increment must meet to be "done" (coded, tested, reviewed, documented,
  meets acceptance criteria, potentially releasable).

## Quality checklist
- [ ] Each story states user, capability, and outcome — and delivers user value.
- [ ] Stories pass INVEST; oversized ones are split into thin end-to-end slices.
- [ ] Every story has testable acceptance criteria covering happy path, edges, and errors.
- [ ] PRD names what's out of scope and the success metric, not just what's in.

## Related methods
- [[agile-scrum-mechanics]] · [[discovery-and-validation]] · [[lean-product-process]] · [[prioritization-frameworks]]
