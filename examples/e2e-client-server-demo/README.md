# E2E Client-Server Demo — QA Automation Engineer

A working demo project showcasing the must-have requirements from a QA Automation Engineer role:

| Posting requirement (חובה) | Where in this repo |
|---|---|
| Web site testing | `ui_tests/` — Selenium + pytest, Page Object Model |
| API testing | `api_tests/` — requests + pytest, happy/negative/schema layers |
| End-to-End in Client-Server form | `ui_tests/tests/test_e2e_client_server.py` — seeds data via API, verifies via UI |
| Test documentation per procedures & standards | `docs/test_plan.md`, `docs/test_case_template.md` |
| Scripting in Python | the whole project |
| Working with testing tools | pytest, pytest-html reports, GitHub Actions CI |

Selenium is included explicitly (posting lists it as יתרון).

## Layout

```
.
├── shared/                      # config + data factory shared across layers
├── api_tests/                   # backend contract tests (reqres.in sandbox)
│   ├── clients/                 # thin API wrappers
│   ├── schemas/                 # JSON Schema for response validation
│   └── tests/                   # happy / negative / schema test files
├── ui_tests/                    # UI tests (the-internet.herokuapp.com sandbox)
│   ├── pages/                   # Page Object Model
│   └── tests/                   # login, form interactions, E2E client-server
├── docs/                        # formal test documentation
├── conftest.py                  # root fixtures
├── pytest.ini                   # markers, default opts
├── requirements.txt
└── .github/workflows/tests.yml  # CI: install, run, upload report
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# offline smoke (no network — schema validation, factories, plumbing)
pytest api_tests/tests/test_offline_smoke.py

# all API tests (needs internet to JSONPlaceholder)
pytest -m api

# UI tests (needs Chrome + internet to the-internet.herokuapp.com)
pytest -m ui

# everything + HTML report
pytest --html=report.html --self-contained-html
```

The Selenium tests use `webdriver-manager` to download a matching ChromeDriver automatically. Chrome must be installed.

## Sandboxes used

| Layer | Target | Why |
|---|---|---|
| API | https://jsonplaceholder.typicode.com | Free public REST API: 10 stable users, full CRUD-shaped endpoints (writes simulate success and echo the payload), zero auth needed |
| UI | https://the-internet.herokuapp.com | Stable QA-friendly UI sandbox with login, dynamic content, alerts |

Switch targets via env vars: `API_BASE_URL`, `UI_BASE_URL`.

## Interview talking points this repo enables

- **POM**: `pages/base_page.py` centralizes wait strategy; `login_page.py` exposes intent-level methods, not selectors.
- **Wait strategy**: explicit waits only — no implicit waits, no `time.sleep`. Explain the difference.
- **Screenshot on fail**: `pytest_runtest_makereport` hook in root `conftest.py`.
- **API test layers**: happy path → negative cases → schema validation. Each catches a different class of regression.
- **E2E Client-Server**: `test_e2e_client_server.py` demonstrates the "set up via API, verify via UI" pattern — the cheapest way to keep E2E fast.
- **Docs**: `docs/test_plan.md` follows IEEE 829-style sections — directly addresses the "test documents per procedures, standards, methodologies" must-have.
- **CI**: GitHub Actions runs the full suite on every push, uploads HTML report as artifact.
