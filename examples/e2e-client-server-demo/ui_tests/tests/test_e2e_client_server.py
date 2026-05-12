"""
E2E Client-Server test.

Pattern: query / seed a backend record via the *server* API (deterministic,
fast), then drive the *client* (UI) and assert it reflects server-side
reality. This is the canonical way to keep E2E suites stable and fast —
the UI is only used for what UI uniquely verifies (rendering, user-visible
behavior).

In a real Client-Server product the API would be the same backend the UI
talks to. This demo composes two unrelated public services (JSONPlaceholder
+ the-internet.herokuapp.com), so we cannot literally verify the same
record across both. What we *do* demonstrate is the structural pattern: an
API precondition step, then a UI verification step, with a shared piece of
test data carried between them.
"""
from __future__ import annotations

import pytest

from shared.config import Config
from shared.data_factory import new_user_payload
from ui_tests.pages.login_page import LoginPage

pytestmark = [pytest.mark.e2e, pytest.mark.ui]


def test_user_created_via_api_can_login_in_ui(driver, api):
    api_response = api.create_user(new_user_payload(name="E2E-User"))
    assert api_response.status_code == 201, "API precondition failed"
    created = api_response.json()
    assert created["name"] == "E2E-User"

    page = LoginPage(driver).open()
    page.login(Config.UI_USERNAME, Config.UI_PASSWORD)

    assert page.is_logged_in(), (
        f"UI login failed after API setup. Created user id={created.get('id')}. "
        "In a real product, the UI would log in as the API-created user."
    )
    assert "You logged into a secure area" in page.flash_message()
