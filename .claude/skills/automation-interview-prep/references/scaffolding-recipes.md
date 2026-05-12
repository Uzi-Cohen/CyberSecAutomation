# Scaffolding Recipes

Canonical project layouts per stack. Each recipe is a starting point — adjust to match the posting's exact wording (e.g., if the posting says "pytest", use pytest, not unittest).

All recipes ship with:
- a working test against a public sandbox
- a README with run instructions
- optional `.github/workflows/tests.yml`

---

## Recipe A — Python + Selenium + pytest (Web UI)

```
examples/web-selenium-py/
├── README.md
├── requirements.txt
├── pytest.ini
├── conftest.py                  # webdriver fixture, screenshot-on-fail
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   └── login_page.py
├── tests/
│   ├── __init__.py
│   └── test_login.py            # against https://the-internet.herokuapp.com/login
└── .github/workflows/tests.yml
```

**requirements.txt**
```
selenium>=4.20
pytest>=8
pytest-html
webdriver-manager
```

**Key choices to explain in interview**
- Why POM (single source of truth for selectors)
- Why fixture-scoped driver (per-test isolation vs. session-speed tradeoff)
- Screenshot-on-fail hook (`pytest_runtest_makereport`)

---

## Recipe B — Python + Playwright + pytest

```
examples/web-playwright-py/
├── README.md
├── requirements.txt
├── playwright.config.py (or pyproject)
├── tests/
│   └── test_login.py
└── .github/workflows/tests.yml
```

**requirements.txt**
```
playwright>=1.45
pytest-playwright
pytest>=8
```

Setup: `playwright install chromium`

**Why pick over Selenium**: auto-wait, trace viewer, network interception, faster, modern context isolation.

---

## Recipe C — JavaScript + Playwright

```
examples/web-playwright-js/
├── README.md
├── package.json
├── playwright.config.ts
├── tests/
│   └── login.spec.ts
└── .github/workflows/tests.yml
```

**package.json deps**
```
@playwright/test
typescript
```

Run: `npx playwright install && npx playwright test`

---

## Recipe D — Cypress (JavaScript)

```
examples/web-cypress/
├── README.md
├── package.json
├── cypress.config.ts
├── cypress/
│   └── e2e/
│       └── login.cy.ts
└── .github/workflows/tests.yml
```

Note in interview: Cypress runs in-browser, so cross-origin and multi-tab cases need workarounds.

---

## Recipe E — Python + requests + pytest (API)

```
examples/api-pytest/
├── README.md
├── requirements.txt
├── conftest.py                  # session-scoped requests.Session, base URL fixture
├── clients/
│   └── reqres_client.py         # thin wrapper around the public API
├── schemas/
│   └── user.schema.json
└── tests/
    ├── test_users_happy.py
    ├── test_users_negative.py
    └── test_users_schema.py     # jsonschema validation
```

**requirements.txt**
```
requests
pytest
jsonschema
pytest-html
```

Target: https://reqres.in or https://jsonplaceholder.typicode.com

**Demo highlights**
- Happy + negative + schema layers
- Parametrized tests for boundary cases
- Schema validation catches breaking contract changes

---

## Recipe F — Postman + Newman (no-code API)

```
examples/api-postman/
├── README.md
├── collections/
│   └── reqres.postman_collection.json
├── environments/
│   └── dev.postman_environment.json
└── .github/workflows/newman.yml
```

CI step: `npx newman run collections/reqres.postman_collection.json -e environments/dev.postman_environment.json`

---

## Recipe G — REST Assured + JUnit (Java)

```
examples/api-restassured/
├── README.md
├── pom.xml
└── src/test/java/com/example/
    └── UsersIT.java
```

**pom.xml deps**
```
rest-assured
junit-jupiter
jackson-databind
```

---

## Recipe H — End-to-end Client-Server demo

Combine recipes A/B with recipe E into one project to demo full E2E:

```
examples/e2e-client-server/
├── README.md
├── requirements.txt
├── api_tests/                   # backend contract tests (recipe E layout)
├── ui_tests/                    # UI tests hitting the same backend (recipe A/B)
└── shared/
    ├── config.py
    └── data_factory.py          # creates test data via API, asserts via UI
```

Talking point: "Set up via API (fast), verify via UI (real user path)."

---

## Recipe I — PowerShell test framework (Pester)

```
examples/powershell-pester/
├── README.md
├── src/
│   └── Get-ServerHealth.ps1
└── tests/
    └── Get-ServerHealth.Tests.ps1
```

Run: `Invoke-Pester ./tests`

Pitch: Pester is the canonical PS testing framework — Describe/Context/It blocks, mocks, code coverage.

---

## CI workflow template (GitHub Actions, Python example)

```yaml
name: tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - run: pytest --html=report.html --self-contained-html
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: report
          path: report.html
```

---

## Picking the right recipe

| Posting says...                     | Use recipe |
|-------------------------------------|------------|
| Selenium + Python                   | A          |
| Selenium + Java                     | A (port) or G layout |
| Playwright (any lang)               | B or C     |
| Cypress                             | D          |
| API + Python                        | E          |
| API + Postman                       | F          |
| API + Java / REST Assured           | G          |
| End-to-End / Client-Server          | H          |
| PowerShell scripting required       | I          |
| Multiple languages listed (OR)      | Ask user which to demo; default to Python |
