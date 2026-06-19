# Standards: Communication

How the PMO communicates with different audiences. Match the message to the reader's altitude and the
decision they need to make. The same facts get framed very differently for an executive, a customer, and
an engineering team.

## Core principles
- **Audience first.** Decide who's reading and what they must decide before writing a word.
- **BLUF — Bottom Line Up Front.** Put the conclusion, ask, or status in the first sentence.
- **Right altitude.** Executives want outcomes and decisions; teams want detail and dependencies.
- **Honest and specific.** No green-washing. If something is at risk, say so, with the reason and the plan.
- **Action-oriented.** Every update makes clear what (if anything) the reader needs to do.

## Audience playbook

**Executives / sponsors**
- Lead with outcome, status (RAG + reason), and the decision/help needed.
- Themes and big rocks, not feature lists; tie to goals/OKRs and business impact.
- One page or less; detail in an appendix or linked artifact.

**Customers / sales**
- Value and benefits in their language; directional timing, never hard commitments you can't keep.
- Set expectations honestly, especially for probabilistic/AI features.

**Engineering / delivery team**
- Specifics: scope, acceptance criteria, dependencies, risks, sequence.
- Context for *why* so the team can make good local trade-offs.

**Cross-functional (marketing, support, ops)**
- What's changing, when, what they need to do to be ready (link to the launch readiness checklist).

## RAG status discipline
- **Green** — on track; no help needed.
- **Amber** — at risk; state the risk and the mitigation/ask.
- **Red** — off track; state the impact, the recovery plan, and the decision needed.
Never a color without a **reason** and an **action**.

## Status update template
```
<Workstream> — <RAG>
- Since last: <key progress>
- Next: <what's coming>
- Risks/issues: <top items + owner>
- Decisions/help needed: <explicit asks>
```

## Meeting & ceremony notes
- Capture: decisions made, action items (owner + due date), and open questions — not a transcript.
- Decisions of consequence are also logged to `knowledge/decision-log.md`.

## Tone
- Clear, concise, confident, and respectful. Prefer plain words over jargon. Active voice.
- Quantify where you can; flag uncertainty honestly rather than hiding it.
