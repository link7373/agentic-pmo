# Requirements Package: <initiative / feature>
Status: Draft | In review | Baselined   ·   Owner: business-analyst   ·   Date: YYYY-MM-DD
Sponsor: <name>   ·   Feeds: `knowledge/prds/<date>-<feature>.md`

## Business need
<The problem in business terms and the outcome required. Not the solution. If this section describes a
solution, the analysis hasn't happened yet.>

## Scope of analysis
**In:** <processes, systems, user groups examined>
**Out:** <explicitly excluded, and why>

## Stakeholders consulted
| Stakeholder | Role | Elicitation method | Date | Key input |
|-------------|------|--------------------|------|-----------|
|             |      |                    |      |           |

_Elicitation methods used: <interview · workshop · observation · document analysis · survey · prototype>._

## Current state
<How it works today — the process, the systems, the handoffs, the workarounds people have built. Workarounds
are requirements evidence: they show where the current state fails.>

**Pain points:**
| Pain | Where it occurs | Frequency / cost | Root cause |
|------|-----------------|------------------|------------|
|      |                 |                  |            |

## Future state
<How it should work, at the same level of detail as current state. What changes, and what deliberately doesn't.>

## Requirements
_Classified. Each requirement is atomic, testable, and traced to the business need. A requirement nobody can
write a test for is a wish._

### Business requirements
| ID | Requirement | Priority (MoSCoW) | Rationale | Source |
|----|-------------|-------------------|-----------|--------|
| BR-1 | | | | |

### Stakeholder requirements
| ID | Requirement | Stakeholder | Priority | Traces to |
|----|-------------|-------------|----------|-----------|
| SR-1 | | | | BR- |

### Functional (solution) requirements
| ID | Requirement | Priority | Acceptance criteria | Traces to |
|----|-------------|----------|---------------------|-----------|
| FR-1 | | | | SR- |

### Non-functional requirements
_Named, quantified, and testable. "Fast" is not an NFR; "95th-percentile response under 400ms at 200
concurrent users" is._

| ID | Category (performance / availability / security / usability / compliance / scalability / supportability) | Requirement | How it will be verified |
|----|-----------------------------------------------------------------------------------------------------------|-------------|-------------------------|
| NFR-1 | | | |

### Transition requirements
_Temporary needs that exist only to get from current to future state — migration, parallel running, training,
cutover. They disappear afterward, which is why they get missed._

| ID | Requirement | When needed | Retired when |
|----|-------------|-------------|--------------|
| TR-1 | | | |

## Business rules & constraints
| ID | Rule / constraint | Source (policy / regulation / technical) | Negotiable? |
|----|-------------------|------------------------------------------|-------------|
|    |                   |                                          |             |

## Data requirements
| Entity | Attributes | Source of truth | Volume | Retention / privacy class |
|--------|------------|-----------------|--------|---------------------------|
|        |            |                 |        |                           |

## Traceability
_Every requirement traces up to a business need and down to something that will verify it. Gaps in this matrix
are the requirements most likely to be silently dropped._

| Requirement ID | Business need | Design / story | Test | Status |
|----------------|---------------|----------------|------|--------|
|                |               |                |      |        |

## Assumptions, open questions & risks
| # | Item | Type | Impact if wrong | Owner | Resolve by |
|---|------|------|-----------------|-------|------------|
|   |      |      |                 |       |            |

## Solution options assessed
| Option | Fit to requirements | Cost / effort | Risk | Recommendation |
|--------|---------------------|---------------|------|----------------|
|        |                     |               |      |                |

---

**Created by Colin Beck**<br>
LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
GitHub: https://github.com/link7373
