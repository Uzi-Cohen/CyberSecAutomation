from pathlib import Path

import pytest
import requests

from shared.config import Config
from api_tests.clients.jsonplaceholder_client import JSONPlaceholderClient

SCREENSHOT_DIR = Path(__file__).parent / "screenshots"


@pytest.fixture(scope="session")
def http_session():
    session = requests.Session()
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()


@pytest.fixture(scope="session")
def api(http_session):
    return JSONPlaceholderClient(base_url=Config.API_BASE_URL, session=http_session, timeout=Config.HTTP_TIMEOUT)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or report.passed:
        return

    driver = item.funcargs.get("driver")
    if driver is None:
        return

    SCREENSHOT_DIR.mkdir(exist_ok=True)
    safe_name = item.nodeid.replace("/", "__").replace("::", "__")
    path = SCREENSHOT_DIR / f"{safe_name}.png"
    try:
        driver.save_screenshot(str(path))
        print(f"\n[screenshot] {path}")
    except Exception as exc:
        print(f"\n[screenshot failed] {exc}")
