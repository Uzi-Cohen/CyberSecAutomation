# Interview Question Bank — QA / Automation / SDET

Use this as a *source* — always tailor wording to the specific posting. Mix categories per the rules in SKILL.md.

---

## Selenium / WebDriver

**Fundamentals**
- Difference between `findElement` and `findElements`. What happens when nothing matches?
- Explicit vs. implicit vs. fluent wait. When does mixing them break tests?
- Page Object Model — why use it, what to avoid (fat page objects, assertions inside POs).
- Same-origin / iframe / new-tab handling.
- Headless vs. headed runs — what only breaks in one mode?

**Scenario**
- A test passes locally but flakes in CI 30% of the time. Walk through your debugging.
- The dev team just moved to a shadow DOM web component library — what changes in your selectors?
- How would you parallelize a 400-test suite that currently runs serially in 90 minutes?

**Deep**
- How does WebDriver's wire protocol work end to end (client → driver → browser)?
- When would you use CDP directly instead of Selenium?

---

## Playwright / Cypress (alternatives)

- Auto-waiting in Playwright vs. Cypress vs. Selenium — what guarantees does each give?
- Network interception: how would you stub a flaky third-party API?
- Trace viewer / time-travel debugging — when has it saved you?

---

## API testing

**Fundamentals**
- Idempotent vs. safe methods. Which HTTP verbs are which?
- Status code families — give a real bug you found tied to a wrong 2xx/4xx.
- Contract testing vs. integration testing vs. E2E — when to use each.
- Authentication flows: Basic, Bearer, OAuth2 code flow, API key — testing pitfalls of each.

**Tools**
- Postman: collections, environments, pre-request scripts, Newman in CI.
- Python: `requests` + `pytest`, parametrization, fixtures, schema validation with `jsonschema` or pydantic.
- JavaScript: `supertest`, `axios`, `vitest`/`jest`.
- REST Assured (Java): given/when/then DSL, JSON path assertions.

**Scenario**
- A POST returns 201 but no resource is created. How do you isolate the cause?
- The API contract changed — backwards-incompatible. How do your tests detect this *before* prod?

---

## End-to-End / Client-Server testing

- Define the boundary between integration, system, and E2E in your previous project.
- Test data management across services — strategies (factories, fixtures, snapshots, anonymized prod dumps).
- How do you keep E2E suites fast and stable as the system grows? (Quarantine, retries, sharding, env-per-PR.)
- Client-server scenarios: thick client + backend API + DB. Where do you draw verification boundaries?

---

## Scripting — Python / JavaScript / PowerShell

**Python**
- Mutable default arguments — why dangerous, show the gotcha.
- `__init__` vs. `__new__`. When have you actually used `__new__`?
- Generators vs. list comprehensions — memory and use cases.
- `pytest` fixtures: scope, autouse, parametrize, conftest layering.

**JavaScript / Node**
- Event loop — micro vs. macro task queues. Predict the output of a `Promise` / `setTimeout` mix.
- `==` vs. `===`, `Object.freeze` depth, structured clone.
- async/await error handling — `Promise.allSettled` vs. `Promise.all`.

**PowerShell**
- Pipeline binding by value vs. by property name.
- `ForEach-Object` vs. `foreach` keyword — perf difference at scale.
- Remoting basics, JEA, credential handling without storing plaintext.

---

## CI/CD

- Stages of a healthy QA pipeline you've built.
- Test impact analysis — running only what changed.
- Flaky-test policy: detect, quarantine, fix SLA.
- Secrets in CI — what *not* to do.

---

## Agile / process

- Definition of Done for a feature — what's QA's input?
- How do you handle a sprint where dev hands you everything on day 9 of 10?
- Test plan for a feature with unclear requirements — your first three moves.
- Bug triage: severity vs. priority, who owns the call.

---

## Test documentation

- Anatomy of a good test case (preconditions, steps, expected, data, traceability).
- Traceability matrix — requirement → test → defect. When has it actually helped?
- Test plan vs. test strategy vs. test charter — when to use which.

---

## Behavioral

- A bug you missed that hit production — what changed in your process after?
- A time you pushed back on dev or PM about quality and were right. About when you were wrong.
- Onboarding to a codebase with zero tests — your first month.
- Worst flaky test you ever hunted down.

---

## Take-home / live-coding prompts

- Build a Selenium/Playwright test for a public login page (e.g., the-internet.herokuapp.com). Requirements: POM, retries, screenshot on fail.
- Given an OpenAPI spec, write a pytest suite covering happy path + 3 negative cases per endpoint.
- Write a PowerShell script that pulls error logs from N servers in parallel and aggregates by error code.
- Refactor a flaky test (sample provided) — explain each change.
