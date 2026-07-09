# Method: Product Strategy

> **Created by Colin Beck**<br>
> LinkedIn: https://www.linkedin.com/in/beckcolin/<br>
> GitHub: https://github.com/link7373

Product strategy is the bridge between a company's vision and the day-to-day work of building.
It answers: **who** we serve, **what** value we create for them, **why** we win, and **how** we'll
measure success. A good strategy makes prioritization decisions easy because it tells you what to say no to.

## The strategy stack (vision → execution)

1. **Vision** — the long-term change in the world you're working toward. Aspirational, durable, qualitative.
2. **Strategy** — the chosen path to the vision: target market, positioning, and the few bets that matter.
3. **Goals / OKRs** — measurable outcomes for the current cycle that move you along the strategy.
4. **Roadmap** — the sequence of themes/initiatives that deliver the goals (see `roadmapping.md`).
5. **Backlog & sprints** — the concrete work (see `agile-scrum-mechanics.md`).

Each layer should trace cleanly up to the one above it. If a backlog item doesn't ladder up to a goal,
and the goal to the strategy, question why it exists.

## Positioning

Define positioning with a crisp statement:

> For **[target customer]** who **[need/opportunity]**, our product is a **[category]** that **[key benefit]**.
> Unlike **[primary alternative]**, we **[key differentiation]**.

Test it against: Is the target specific? Is the need real and urgent? Is the differentiation defensible and
something customers actually value?

## Business model thinking (lightweight canvas)

Capture the economic logic on one page:
- **Customer segments** — who pays, who uses (may differ).
- **Value proposition** — the job done / pain relieved / gain created.
- **Channels** — how you reach and deliver to customers.
- **Revenue model** — how you capture value (subscription, usage, transaction, license).
- **Cost structure** — the main cost drivers.
- **Key resources & partners** — what you must own or rely on.
- **Unfair advantage / moat** — what compounds and is hard to copy (data, network effects, switching costs, brand).

## Market sizing (TAM / SAM / SOM)

- **TAM** — total addressable market if everyone who could buy, did.
- **SAM** — the serviceable slice your model can actually reach.
- **SOM** — the share you can realistically obtain in the planning horizon.

Size **bottom-up** (units × price × reachable customers) where possible — it's more credible than top-down
percentages of a giant number. State assumptions explicitly so they can be challenged.

## Levels of a product

A product is more than its features. Design and position all three layers:
- **Core** — the fundamental benefit/job the customer is really buying.
- **Actual** — the tangible product: features, quality, design, brand.
- **Augmented** — everything around it: onboarding, support, docs, warranty, community, ecosystem.
Competitors often match the actual product; differentiation and retention are frequently won at the augmented layer.

## Product lifecycle (and why strategy changes by stage)

Products move through stages, and the right strategy differs at each:
- **Introduction** — prove value, drive awareness and first adoption; expect losses.
- **Growth** — scale adoption, widen the moat, invest in differentiation; watch for fast-followers.
- **Maturity** — defend share, optimize margin, extend via new segments/features; competition is fiercest.
- **Decline** — harvest, reposition, or retire deliberately (see end-of-life in `launch-and-gtm.md`).
Know which stage each product is in; managing a mature product like a new one (or vice versa) wastes capital.

## Market segmentation & targeting

Divide the market into segments with shared needs and behavior, then choose which to serve:
- Segment by need, job-to-be-done, behavior, or firmographic/demographic traits — needs and jobs beat
  demographics for product decisions.
- Evaluate each segment's size, growth, reachability, and fit with your advantage; **target** the few you can
  win and **position** distinctly for each (see Positioning above).
Serving "everyone" is a non-strategy; a sharp beachhead segment usually beats a diffuse broad play.

## Innovation types & the portfolio

- **Innovation types** — **incremental** (improve the core), **adjacent** (new segment/use of existing
  strengths), and **disruptive/breakthrough** (new market or model). Balance the mix; don't fund only safe bets.
- **Portfolio management** — across multiple products/bets, balance risk, lifecycle stage, and resource draw.
  Classify by market growth × relative strength (star / cash-cow / question-mark / low-priority) and fund
  deliberately: milk the cash cows, back the stars, test the questions, retire the laggards.

## OKRs (objectives & key results)

- **Objective** — qualitative, ambitious, time-boxed ("Make onboarding effortless for new teams").
- **Key Results** — 2–4 measurable outcomes that prove the objective ("Median time-to-first-value < 10 min";
  "Week-1 activation rate 40% → 60%").
- KRs measure **outcomes** (changes in user/business behavior), not **output** (features shipped).
- Set a confidence level; review mid-cycle; grade at the end and carry learnings forward.

## Strategy for AI / data products (special considerations)

- **Capability uncertainty:** model behavior is probabilistic — frame bets as hypotheses to validate, not specs.
- **Data as moat:** proprietary usage data compounds into a defensible advantage over time; design to capture it.
- **Cost & latency are product constraints:** treat inference cost and response time as first-class requirements.
- **Trust, safety, and evaluation** are product workstreams, not afterthoughts.

## Quality checklist
- [ ] Vision is durable and inspiring; strategy is a clear, narrow path to it.
- [ ] Target customer and positioning are specific, not "everyone."
- [ ] Differentiation is something customers value and competitors can't easily copy.
- [ ] OKRs measure outcomes, ladder to strategy, and are honestly gradeable.
- [ ] Market size is built bottom-up with stated assumptions.

## Related methods
- [[lean-product-process]] · [[roadmapping]] · [[metrics-and-experimentation]] · [[discovery-and-validation]] · [[launch-and-gtm]]
