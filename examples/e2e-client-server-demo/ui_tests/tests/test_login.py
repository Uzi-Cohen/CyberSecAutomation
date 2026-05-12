import pytest

from shared.config import Config
from ui_tests.pages.login_page import LoginPage

pytestmark = [pytest.mark.ui]


@pytest.mark.smoke
def test_valid_login_lands_on_secure_area(driver):
    page = LoginPage(driver).open()
    page.login(Config.UI_USERNAME, Config.UI_PASSWORD)

    assert page.is_logged_in(), "Logout button should be visible after successful login"
    assert "You logged into a secure area" in page.flash_message()


def test_invalid_password_shows_error(driver):
    page = LoginPage(driver).open()
    page.login(Config.UI_USERNAME, "wrong-password")

    assert not page.is_logged_in()
    assert "Your password is invalid" in page.flash_message()


def test_invalid_username_shows_error(driver):
    page = LoginPage(driver).open()
    page.login("no-such-user", Config.UI_PASSWORD)

    assert "Your username is invalid" in page.flash_message()
